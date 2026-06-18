<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence

Topics include Deterministic transforms, Datasets, Generalization, Out-of-distribution generalization, Learning, Epiplexity, Information theory, Kolmogorov complexity.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Can we learn more from data than existed in the generating process itself? Can new and useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without considering a downstream task? On these questions, Shannon information and Kolmogorov complexity come up nearly empty-handed, in part because they assume observers with unlimited computational capacity and do not target the useful information content. In this work, we identify and exemplify three seeming paradoxes in information theory: information cannot be increased by deterministic transformations; information is independent of the order of data; likelihood modeling is merely distribution matching. To shed light on the tension between these results and modern practice, and to quantify the value of data, we introduce epiplexity, a formalization of information capturing what computationally bounded observers can learn from data. Epiplexity captures the structural content in data while excluding time-bounded entropy, the random unpredictable content exemplified by pseudorandom number generators and chaotic dynamical systems. With these concepts, we demonstrate how information can be created with computation, how it depends on the ordering of the data, and how likelihood modeling can produce more complex programs than present in the data generating process itself.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also present practical procedures to estimate epiplexity which we show capture differences across data sources, track with downstream performance, and highlight dataset interventions that improve out-of-distribution generalization. In contrast to principles of model selection, epiplexity provides a theoretical foundation for data selection, guiding how to select, generate, or transform data for learning systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

^00^footnotetext: Equal contribution.^00^footnotetext: Code available at

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As AI research progresses towards more general-purpose intelligent systems, cracks are beginning to show in mechanisms for grounding mathematical intuitions. Much of learning theory is built around controlling generalization error with respect to a given distribution, treating the training distribution as fixed and focusing optimization effort on the choice of model. Yet modern systems are expected to transfer across tasks, domains, and objectives that were not specified at training time, often after large-scale pretraining on diverse and heterogeneous data. In this regime, success or failure frequently hinges less on architectural choices than on what data the model was exposed to in the first place. Pursuing broad generalization to diverse out-of-distribution tasks forces a shift in perspective: instead of treating data as given and optimizing for in-distribution performance, we need to choose and curate data to facilitate generalization to unseen tasks. This shift makes the value of data itself a central question---how much usable, transferable information can a model acquire from training? In other words, instead of model selection, how do we perform *data selection*? On this question, existing theory offers little guidance and often naively contradicts empirical observations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider synthetic data, crucial for further developing model capabilities when existing natural data are exhausted. Existing concepts in information theory like the data processing inequality appear to suggest that synthetic data adds no additional value. Questions about what information is transferred to a given model seem naturally within the purview of information theory, yet, quantifying this information with existing tools proves to be elusive. Even basic questions, such as the source of the information in the weights of an AlphaZero game-playing model, are surprisingly tricky to answer. AlphaZero takes in zero human data, learning merely from the deterministic rules of the game and the AlphaZero RL algorithm, both of which are simple to describe. Yet the resulting models achieve superhuman performance and are large in size. To assert that AlphaZero has learned little to no information in this process is clearly missing the mark, and yet both Shannon and algorithmic information theory appear to say so.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we argue that the amount of structural information a *computationally bounded* observer can extract from a dataset is a fundamental concept that underlies many observed empirical phenomena. As we will show, existing notions from Shannon and algorithmic information theory are inadequate when forced to quantify this type of information. These frameworks often lend intuitive or mathematical support to beliefs that, in fact, obscure important aspects of empirical phenomena. To highlight the limitations of classical frameworks and motivate the role of computational constraints in quantifying information, we identify and demonstrate three *apparent paradoxes*: statements which can be justified mathematically by Shannon and algorithmic information theory, and yet are in tension with intuitions and empirical phenomena.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Information cannot be increased by deterministic processes. For both Shannon entropy and Kolmogorov complexity, deterministic transformations cannot meaningfully increase the information content of an object. And yet, we use pseudorandom number generators to produce randomness, synthetic data improves model capabilities, mathematicians can derive new knowledge by reasoning from axioms without external information, dynamical systems produce emergent phenomena, and self-play loops like AlphaZero learn sophisticated strategies from games.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Information is independent of factorization order. A property of both Shannon entropy and Kolmogorov complexity is that total information content is invariant to factorization: the information from observing first $X$ and then $Y$ is the same as observing $Y$ followed by $X$. On the other hand, LLMs learn better on English text ordered left-to-right than reverse ordered text, picking out an "*arrow of time*", and we have cryptography built on the existence of functions that are computationally hard to predict in one direction and easy in another.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Likelihood modeling is merely distribution matching. Maximizing the likelihood is often equated with matching the training data generating process: the true data-generating process is a perfect model of itself, and no model can achieve a higher expected likelihood. As a consequence, it is often assumed that a model trained on a dataset cannot extract more structure or learn useful features that were not used in generating the data. However, we show that a computationally-limited observer can in fact uncover much more structure than is in the data generating process. For example, in Conway's game of life the data are generated via simple programmatic rules that operate on two-dimensional arrays of bits. Applying these simple rules sequentially, we see emergent structures, such as different species of objects that move and interact in a predictable way. While an unbounded observer can simply simulate the evolution of the environment exactly, a computationally bounded observer would make use of the emergent structures and learn the different types of objects and their behaviors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The tension between these theoretical statements and empirical phenomena can be resolved by imposing computational constraints on the observer and separating the random content from the structural content. Drawing on ideas from cryptography, algorithmic information theory, and these unexplained empirical phenomena, we define a new information measure, epiplexity (epistemic complexity), which formally defines the amount of structural information that a computationally bounded observer can extract from the data (Section 3, Definition 8 ‣ 3 Epiplexity: Structural Information Extractable by a Computationally Bounded Observer ‣ From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence")). Briefly, epiplexity is the information in the model that minimizes the description length of data under computational constraints. A simple heuristic measurement is the area under the loss curve above the final loss, while a more rigorous approach uses the cumulative KL divergence between a teacher and student model (Section 4, Figure 2).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our definitions capture the intuition that an object contains both random, inherently unpredictable information (entropy), and predictable structured information that enables observers to generalize by identifying patterns (epiplexity). In Figure 1 (left) we illustrate this divide. In the top row, we have highly redundant and repetitive code and simple color gradients, which have little information content, be it structural or random. In the middle row, we have the inner workings of an algorithm and pictures of animals, showing complex, long-range interdependencies between the elements from which a model can learn complex features and subcircuits that are helpful even for different tasks. In contrast, on the bottom, we have random data with little structure: configuration files with randomly generated API keys, file paths, hashes, arbitrary boolean flags have negligible learnable content and no long-range dependencies or complex circuits that result from learning on this task. Similarly, uniformly shuffled pixels from the animal pictures have high entropy but are fundamentally unpredictable, and no complex features or circuits arise from training on these data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

An essential property of our formulation is that information is *observer dependent*: the same object may appear random or structured depending on the computational resources of the observer. For instance, the output of a strong pseudorandom generator appears indistinguishable from true randomness to any polynomial-time observer lacking the secret key (seed), regardless of the algorithm or function class. In other situations, such as chaotic dynamical systems, both apparently random behavior is produced along with structure: the state of the system cannot be predicted precisely over long time-scales, but such observers may still learn meaningful predictive distributions, as shown by the invariant measure in Figure˜1 (top right).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Models trained to represent these distributions are computer programs, and substructures within these programs, like circuits for performing specific tasks, or induction heads, can be reused even for seemingly unrelated data. This view motivates selecting high epiplexity data that induces more structural information in the model, since these structures can then be reused for unseen out-of-distribution (OOD) tasks, as illustrated in Figure˜1 (bottom right). We emphasize, however, that epiplexity is a measure of information, *not* a guarantee of OOD generalization to specific tasks. Epiplexity quantifies the amount of structural information a model extracts, while being agnostic to whether these structures are relevant to a *specific* downstream task.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

To build intuition, we explore a range of phenomena and provide experimental evidence for behaviours that are poorly accounted for by existing information-theoretic tools, yet naturally accommodated by epiplexity. We show that information *can* be created purely through computation, giving insights into synthetic data (subsection 5.1). We examine how certain factorizations of the same data can increase structural information and downstream OOD performance---even as they result in worse training loss (subsection 5.2). We show why likelihood modeling is more than distribution matching, identifying induction and emergence as two settings where the observer can learn more information than was present in the data generating process (subsection 5.3). By measuring epiplexity, we can better understand why pre-training on text data transfers more broadly than image data, and why certain data selection strategies for LLMs are empirically successful (Section 6). Together, our results provide clarity on the motivating questions: the information content of data can be compared independently of a specific task, new information can be created by computation, and models can learn more information than their generating processes contain.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

In short, we identify a disparity between existing concepts in information theory and modern practice, embodied by three apparent paradoxes, and introduce epiplexity as a measurement of structural information acquired by a computationally bounded observer to help resolve them. We formally define epiplexity in Section 3 (Definition 8 ‣ 3 Epiplexity: Structural Information Extractable by a Computationally Bounded Observer ‣ From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence")) and present measurement procedures in Section 4. In Section 5, we show how epiplexity and time-bounded entropy shed light on these paradoxes, including induction and emergent phenomena. Finally, in Section 6, we demonstrate that epiplexity correlates with OOD generalization, helping explain why certain data enable broader generalization than others.

<!-- chunk {"id": "body-0017", "role": "body", "section": "What Does it Mean for An Object to Be Random?", "weight": 1.0} -->

Random Variables and Shannon Information. Many common intuitions about randomness start from random variables and Shannon information. A random variable defines a map from a given measurable probability space to different outcomes, with probabilities corresponding to the measure of the space that lead to a certain outcome. Shannon information assigns to each outcome $x$ a self-information (or surprisal) ${\log{1/P}}{(x)}$ based on the probability $P$, and an entropy for the random variable ${H{(X)}} = {{\mathbb{E}}{\lbrack{{\log{1/P}}{(X)}}\rbrack}}$, which provides a lower bound on the average code length needed to *communicate* samples to another party. In Shannon's theory, information comes only from distributions and random variables---objects that are not random must contain no information. As a result, non-random information is seemingly contradictory, and thus we must draw from a broader mathematical perspective to describe such concepts.

<!-- chunk {"id": "body-0018", "role": "body", "section": "What Does it Mean for An Object to Be Random?", "weight": 1.0} -->

In the mid 1900s, mathematicians were interested in formalizing precisely what it means for a given sample to be a random draw from a given distribution, to ground the theory of probability and random variables. A central consideration involves a uniformly sampled binary sequence $u_{1:\infty}$ from which other distributions of interest can be constructed. This sequence can also be interpreted as the binary expression of a number $\lbrack 0,1)$. Intuitively, one might think that all sequences should be regarded as equally random, as they are all equally likely according to the probability distribution: $1111111\ldots$ has the same probability mass as $10011101\ldots$ and also the same self-information. However, looking at statistics on these sequences reveals something missing from this perspective; from the law of large numbers, for example, it must be that ${\lim_{N\rightarrow\infty}{\frac{1}{N}{\sum_{i = 1}^{N}u_{i}}}} = 0.5$, which is clearly not satisfied by the first sequence of $1$s.

<!-- chunk {"id": "body-0019", "role": "body", "section": "What Does it Mean for An Object to Be Random?", "weight": 1.0} -->

Martin-Löf Randomness: No algorithm exists to predict the sequence. Initial attempts were made to formalize randomness as sequences which pass all statistical tests for randomness, such as the law of large numbers for selected substrings. However, under such definitions all sequences fail to be random since tests like $u_{1:\infty} \neq y_{1:\infty}$ for any particular sequence $y$ must also be included. The solution to these issues was found by defining random sequences not as those that pass all tests of randomness, but those that pass all *computable* tests of randomness, in a formalization known as Martin-Löf randomness. As it turned out, this definition is equivalent to a number of seemingly distinct definitions, such as the inability for any gambler to exploit properties of the sequence to make a profit, or that all prefixes of the random sequence should be nearly incompressible. For this last definition, we must invoke Kolmogorov complexity, a notion of compressibility and a key concept in this paper.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Random vs Structural Information", "weight": 1.0} -->

With these notions of randomness in hand, we can use what is random to define what is not random. In algorithmic information theory, there is a lesser known concept that captures exactly this idea, known as *sophistication*, which has no direct analog in Shannon information theory.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Minimum Description Length Principle", "weight": 1.0} -->

Finally, we review the minimum description length principle (MDL), used as a theoretical criterion for model selection, which we will use in defining epiplexity. The principle states that among models for the data, the best explanation minimizes the total description length of the data, including both the description of the data using the model and the description of the model itself. The most common instantiation of this idea is via the statistical two-part code MDL.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Epiplexity: Structural Information Extractable by a Computationally Bounded Observer", "weight": 1.0} -->

Keeping in mind the distinction between structural and random information in the unbounded compute setting, and the computational nature of pseudorandomness in cryptography, we now introduce epiplexity. *Epiplexity* captures the structural information present to a computationally bounded observer. As the computational constraints of this observer change, so too does the division between random and structured content. After introducing epiplexity here, we present ways of measuring epiplexity in Section 4. In Sections 5 and 6 we show how epiplexity can shed light on seeming paradoxes in information theory around the value of data, and OOD generalization.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Epiplexity: Structural Information Extractable by a Computationally Bounded Observer", "weight": 1.0} -->

First we will define what it means for a probability distribution to have an efficient implementation, requiring that it be implemented on a prefix-free universal Turing machine (UTM) and halt in a fixed number of steps.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Pseudorandom number sequences have high random content and little structure", "weight": 1.0} -->

Unlike Shannon entropy, Kolmogorov complexity, or even resource bounded forms of Kolmogorov complexity, we show that CSPRNGs have nearly maximal time-bounded entropy for polynomial time observers. Additionally, while CSPRNGs produce random content, they do not produce structured content as the epiplexity is negligibly larger than constant. Formally, let $U_{k}$ be the uniform distribution on $k$ bits.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Existence of Random Variables with High Epiplexity", "weight": 1.0} -->

One may wonder whether any high epiplexity random variables exist at all. Indeed, assuming the existence of one-way functions, we can show via a counting argument that there exists a sequence of random variables whose epiplexity grows at least logarithmically with the dimension.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Measuring Epiplexity and Time-Bounded Entropy", "weight": 1.0} -->

We have now introduced epiplexity and time-bounded entropy as measures of structural and random information of the data. In this section, we present practical procedures to estimate upper bounds and empirical proxies for these quantities.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Measuring Epiplexity and Time-Bounded Entropy", "weight": 1.0} -->

Intuitively, we want to find a probabilistic model $P{( \cdot )}$ of the data $X$ that achieves low expected loss ${\mathbb{E}}{\lbrack{{\log{1/P}}{(X)}}\rbrack}$, is described by a short program $P,$ and evaluating $P{(X)}$ takes time at most ${T{({|X|})}},$ which we will abbreviate as $T.$ Using this model, we thereby decompose the information of the data into its structural and random components, namely, epiplexity $S_{T}{(X)}$: the length of the program ${|P|},$ accounting for the bits required to model the data distribution, and time-bounded entropy $H_{T}{(X)}$: the expected length for entropy coding the data using this model, which accounts for the bits required to specify the particular realization of $X$ within that distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Measuring Epiplexity and Time-Bounded Entropy", "weight": 1.0} -->

We estimate conditional epiplexity analogously, providing random variable conditioning as input into the model.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Measuring Epiplexity and Time-Bounded Entropy", "weight": 1.0} -->

Since directly searching over the space of programs is intractable, we restrict attention to probabilistic models parameterized by neural networks, as they achieve strong empirical compression across data modalities and capture the most relevant ML phenomenology. While a naive approach is to let $P$ be a program that directly stores the architecture and weights of a neural network and evaluates it on the given data, this approach can significantly overestimate the information content in the weights, particularly for large models trained on relatively little data. Instead, we will use a more efficient approach that encodes the training process that produces the weights. We will discuss two approaches for encoding neural network training processes, based on *prequential coding* and *requential coding*, respectively. The former is more straightforward to understand and evaluate, but relies on a heuristic argument to separate structure bits from noise bits, while the latter is rigorous at the cost of being more difficult to evaluate. Fortunately, both approaches often yield comparable rankings of epiplexity across datasets (Section˜4.3).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Measuring Epiplexity and Time-Bounded Entropy", "weight": 1.0} -->

Moving forward, we will measure time by the number of floating-point operations (FLOPs) and dataset size by number of tokens, so that training a model with $N$ parameters on $D$ tokens takes time approximately $6ND$, while evaluating it on $X$ takes time $2N\mathcal{D}$ with $\mathcal{D} = {|X|}$ the number of tokens in $X.$ To distinguish $X$ from the training dataset, which we are free to choose, we will refer to $X$ as the test dataset, as it is the data we need to perform inference.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

Prequential coding provides a classic approach for compressing the training process of a neural network. We assume a batch size of one for simplicity, but generalizing to batch sizes larger than one is straightforward. Starting with a randomly initialized network $P_{0}$ (where the subscript indicates timestep), we proceed iteratively: at each step $i$, we entropy encode the current training token $Z_{i}$ using ${\log{1/P_{i}}}{(Z_{i})}$ bits, then train the model on this token to produce $P_{i + 1}$. Typically $Z_{i}$'s are drawn i.i.d. from the same distribution as $X.$ On the side of the decoder, a synchronized model is maintained; the model decodes $Z_{i}$ using $P_{i}$ and then trains on it to produce the identical $P_{i + 1}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

Omitting small constant overheads for specifying the random initialization, architecture, and training algorithm, a total of ${L{(Z_{:M},P_{M})}} = {\sum_{i = 0}^{M - 1}{{\log{1/P_{i}}}{(Z_{i})}}}$ bits yields an explicit code for both the training data $Z_{:M} = {\{ Z_{0},\ldots,Z_{M - 1}\}}$ and the final model weights $P_{M}$, which can be decoded in time $6ND$ for a model with $N$ parameters trained on $D$ tokens (typically $D > M$ as each example contains multiple tokens). Despite having an explicit code for $Z,P_{M}$, we cannot easily separate this into a code for $P_{M}$ alone for estimating epiplexity.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

To isolate the description length of $P_{M}$ alone, we adopt the heuristic in Zhang et al. and Finzi et al.: we first estimate the description length of the training data given $P_{M}$ as its entropy code length under the final model, ${L{(\left. Z_{:M} \middle| P_{M} \right.)}} = {\sum_{i = 0}^{M - 1}{{\log{1/P_{M}}}{(Z_{i})}}}$. Then, appealing to the symmetry of information, which states ${K{(P_{M})}} = {{K{(Z_{:M},P_{M})}} - {K{(\left.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

If $Z_{i}$ is sampled i.i.d., as is typically the case, then the code length for the model *can be visualized as the area under the loss curve above the final loss* in Figure˜2. Intuitively, the model absorbs a significant amount of information from the data if training yields a sustained and substantial reduction in loss. For random data, ${\log{1/P_{i}}}{(Z_{i})}$ never decreases, while for simple data, ${\log{1/P_{i}}}{(Z_{i})}$ drops rapidly and stabilizes, both leading to small ${|P_{preq}|}.$ We note that the prequential loss values are effectively taken on estimates of the *test loss*, because they evaluate the log probabilities on a batch before it is trained, a central detail to the coding scheme. In cases where train and test diverge, such as when there is overfitting, this difference could become important important.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

Encoding the test dataset $X$ (not to be confused with the training data) using this model, we obtain a two-part code of expected length ${|P_{preq}|} + {{\mathbb{E}}{\lbrack{{\log{1/P_{M}}}{(X)}}\rbrack}}$ that runs in time ${{6ND} + {2N\mathcal{D}}}.$ We optimize the training hyperparameters (e.g., learning rate) and the trade-off between $N$ and $D$ subject to the time bound ${{6ND} + {2N\mathcal{D}}} \leq T$ to find the optimal $P^{\star}$ that minimizes the two-part code within this family, and estimate epiplexity and time-bounded entropy as ${S_{T}{(X)}} = {|P_{preq}^{\star}|}$ and ${{H_{T}{(X)}} =

<!-- chunk {"id": "body-0036", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

{{\mathbb{E}}{\lbrack{{\log{1/P^{\star}}}{(X)}}\rbrack}}}.$ The better these hyperparameters are optimized, the more accurate our estimates become.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

We use the Maximal Update Parameterization ($\mu$P) to ensure the optimal learning rate and initialization are consistent across model sizes, simplifying tuning. We estimate the expectation ${\mathbb{E}}{\lbrack{{\log{1/P_{M}}}{(X)}}\rbrack}$ by its empirical value on held-out validation data, i.e., the validation loss scaled by the size of $X$. We detail the full procedure in Appendix˜B, such as how we choose the hyperparameters and estimate the Pareto frontier of MDL vs compute.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

While conceptually simple, practically useful, and easy to evaluate, this prequential approach to approximating epiplexity is not rigorous for two reasons. First, both $L{(Z_{:M},P_{M})}$ and $L{(\left. Z_{:M} \middle| P_{M} \right.)}$ can only upper-bound the respective Kolmogorov complexities, and thus their difference does not yield an upper bound for ${K{(P_{M})}}.$^44^4We have ${{{L{(Z_{:M},P_{M})}} + {O{}}} \geq {K{(Z_{:M},P_{M})}}},$ but not that ${{{L{(\left. Z_{:M} \middle| P_{M} \right.)}} + {O{}}} \leq {K{(\left.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Approximating Model Description Length with Prequential Coding", "weight": 1.0} -->

Z_{:M} \middle| P_{M} \right.)}}}.$ Second, even setting this issue aside, the argument only establishes the existence of a program that encodes $P_{M}$ with length ${|P_{preq}|},$ but does not guarantee that its runtime falls within ${6ND},$ since the symmetry of information does not extend to time-bounded Kolmogorov complexity. Nevertheless, prequential coding can serve as a useful starting point for crudely estimating epiplexity, particularly convenient when one already has access to the loss curve from an existing training run.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Explicitly Coding the Model with Requential Coding", "weight": 1.0} -->

To address the shortcomings of the previous approach based on prequential coding, we adopt requential coding for constructing an explicit code of the model with a known runtime. Rather than trying to code a particular training dataset, with requential coding one can use the insensitivity to the exact data points sampled to code for *a* sampled dataset that leads to a performant model but without paying for the entropy of the data. Specifically, it encodes a training run where at step $i$ a student model $P_{i}^{s}$ is trained on a synthetic token sampled randomly from a teacher model $P_{i}^{t}$, where the sequence $P_{0}^{t},\ldots,P_{M - 1}^{t}$ are arbitrary teacher model checkpoints. We typically choose $P_{i}^{t}$ to be the checkpoints from training on the original *real* training set, as in prequential coding.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Explicitly Coding the Model with Requential Coding", "weight": 1.0} -->

where the logarithmic and constant overheads are typically negligible due to large sequence length and batch size, and as before we omit the small constant cost of specifying the random initialization, architecture, and training algorithm. In addition to providing an explicit code, a key advantage of requential coding is its flexibility in choosing the teacher sequence: by selecting teachers $P_{i}^{t}$ that remain close to the student $P_{i}^{s}$ while still pointing toward the target distribution, we keep the per-step coding cost ${KL}{({P_{i}^{t} \parallel P_{i}^{s}})}$ small while effectively guiding the student's learning.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Explicitly Coding the Model with Requential Coding", "weight": 1.0} -->

Figure˜2 connects requential coding to the student's and teacher's loss curves: suppose we take as teachers the checkpoints $P_{0}^{t},\ldots,P_{M - 1}^{t}$ from a model trained on real data ${Z_{0},\ldots,Z_{M - 2}} \sim P_{X}$. For visualization, we can then estimate ${KL}{({P_{i}^{t} \parallel P_{i}^{s}})}$ by the loss gap ${{\log{1/P_{i}^{s}}}{(Z_{i})}} - {{\log{1/P_{i}^{t}}}{(Z_{i})}}$, which is accurate when $P_{i}^{t} \approx P_{X}$. We can thus visualize the code length for the student as approximately the area between the teacher's and student's loss curves on real data, as shown in Figure˜2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Explicitly Coding the Model with Requential Coding", "weight": 1.0} -->

The two-part code has expected length ${{|P_{req}|} + {{\mathbb{E}}{\lbrack{{\log{1/P_{M}^{s}}}{(X)}}\rbrack}}},$ consisting of first decoding $P_{M}^{s}$ by replaying the training process, which takes time $6ND$ for a total of $D$ requential training tokens, and then evaluating $P_{M}^{s}$ on the test dataset $X,$ taking an additional time ${2N\mathcal{D}},$ for a total runtime of ${6ND} + {2N\mathcal{D}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Explicitly Coding the Model with Requential Coding", "weight": 1.0} -->

We optimize the training hyperparameters, teacher choices, and the trade-off between $N$ and $D$ subject to the specified time bound $T$ to find the optimal model $P^{\star}$ minimizing the two-part code, and estimate ${S_{T}{(X)}} = {|P_{req}^{\star}|}$ and ${{H_{T}{(X)}} = {{\mathbb{E}}{\lbrack{{\log{1/P^{\star}}}{(X)}}\rbrack}}}.$ See details in Section˜B.1.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison Between the Two Approaches and Practical Recommendations", "weight": 1.0} -->

Figure˜2 compares the estimated epiplexity obtained by the two approaches across four groups of datasets used in this work: ECA (Section˜5.1), easy and hard induction (Section˜5.3.1), and natural datasets (Section˜6.2). While the prequential estimate is typically several times larger than the requential estimate, the two estimates correlate well, particularly within each group where the datasets yield similar learning dynamics. We detail the datasets and time bounds used in Section˜C.7. This general agreement is expected since the prequential estimate can be viewed as an approximation of requential coding with a static teacher (Section˜B.2). In general, however, the discrepancy between the two estimates will depend on particular datasets and training configurations, and a good correlation between the two is not guaranteed.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison Between the Two Approaches and Practical Recommendations", "weight": 1.0} -->

While requential coding is the more rigorous approach, it is typically $2 \times$ to $10 \times$ slower than prequential coding, which requires only standard training. The overhead depends on batch size, sequence length, and inference implementation (smaller overhead for large batches and short sequences), as requential coding requires repeatedly sampling from the teacher, though it is possible that the overhead can be reduced with more efficient algorithms. Therefore, we recommend using prequential coding for crudely estimating epiplexity and ranking the epiplexity of different datasets, particularly when one has access to the loss curve from an existing expensive training run (e.g., see an application in Section˜6.2), and requential coding for obtaining the most accurate estimates otherwise.

<!-- chunk {"id": "body-0047", "role": "body", "section": "How Epiplexity and Time-Bounded Entropy Scale with Compute and Data", "weight": 1.0} -->

Under natural assumptions about neural network training---namely, that larger models are more sample-efficient and that there are diminishing returns to scaling model size or data alone---we expect epiplexity and time-bounded entropy to exhibit certain generic scaling behavior as a function of the compute budget $T$ and dataset size $\mathcal{D}$. In Section˜B.4, we show that, under these assumptions, the compute-optimal model size $N^{\star}{(T)}$ and training data size $D^{\star}{(T)}$ are generally increasing in the compute budget $T$, which implies that epiplexity $S_{T}{(X)}$ typically grows with $T$ while time-bounded entropy $H_{T}{(X)}$ decreases.

<!-- chunk {"id": "body-0048", "role": "body", "section": "How Epiplexity and Time-Bounded Entropy Scale with Compute and Data", "weight": 1.0} -->

In the infinite-compute limit, epiplexity $S_{\infty}{(X)}$ typically grows with the test set size $\mathcal{D} = {|X|}$, while the per-token time-bounded entropy ${H_{\infty}{(X)}}/\mathcal{D}$ decreases. These results align with our intuition that larger compute budgets and more data allow the model to extract more structural information from the dataset and reduce the apparent randomness remaining in each sample. However, they should be understood only as typical trends, with a counterexample shown in Section˜5.3.2 relating to the phenomenon of emergence.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Three Apparent Paradoxes of Information", "weight": 1.0} -->

To illustrate the lacunae in existing information theory perspectives, we highlight three *apparent paradoxes* of information: information cannot be created by deterministic transformations; total information content of an object is the same regardless of the factorization; and likelihood modeling can only learn to match the data-generating process. Each statement captures some existing sentiment within the machine learning community, can be justified mathematically by Shannon and algorithmic information theory, and yet seems to be in conflict with intuitions and experimental observations. In this section, we will show with both theoretical results and empirical evidence that time bounding and epiplexity help resolve these apparent paradoxes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Paradox 1: Information Cannot be Created by Deterministic Transformations", "weight": 1.0} -->

Both Shannon and algorithmic information theory state in some form that the total information cannot be increased by applying deterministic transformations on existing data. The data processing inequality (DPI) states that if some information source $W$ produces natural data $X$ that are collected, then no deterministic *or stochastic* transformations used to produce $Y$ from $X$ can increase the mutual information with the variable of interest $W$: ${I{(Y;W)}} \leq {I{(X;W)}}$. Similarly, information non-increase states that a deterministic transformation $f$ can only preserve or decrease the Shannon information, a property that holds pointwise ${- {{\log P_{Y}}{({f{(x)}})}}} \leq {- {{\log P_{X}}{(x)}}}$ and in expectation: ${H{({f{(X)}})}} \leq {H{(X)}}$ (we note $X$ here is a discrete random variable).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Paradox 1: Information Cannot be Created by Deterministic Transformations", "weight": 1.0} -->

In algorithmic information theory, there is a corresponding property: ${K{({f{(x)}})}} \leq {{K{(x)}} + {K{(f)}} + c}$ for a fixed constant $c$. These inequalities appear to rule out creating new information with deterministic computational processes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Paradox 1: Information Cannot be Created by Deterministic Transformations", "weight": 1.0} -->

How can we reconcile this fact with algorithms like AlphaZero that can be run in a closed environment from a small deterministic program on the game of chess, extracting insights about the game, different openings, the relative values of pieces in different positions, tactics and high level strategy, and requiring megabytes of information stored in the weights? Similarly we have dynamical systems with simple descriptions of the underlying laws that produce rich and unexpected structures, from which we can learn new things about them and mathematics.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Paradox 1: Information Cannot be Created by Deterministic Transformations", "weight": 1.0} -->

We also have evidence that synthetic data is helpful for model capabilities. Moreover, if we believe that the processes that create natural data could in principle have been simulated to sufficient precision on a large computer, then all data could have been equivalently replaced with synthetic data. For practical synthetic data produced from transformations of samples from a given model and prompt, this sampling is performed with pseudorandom number generators, making the entire transformation deterministic. If we consider $f$ as the transformations we use to produce synthetic data and $x$ was the limited real data we started, these inequalities appear to state very concretely that our synthetic data adds no additional information beyond the model and training data.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Paradox 1: Information Cannot be Created by Deterministic Transformations", "weight": 1.0} -->

Whatever information it is that we mean when we say that AlphaZero has produced new and unexpected insights in chess, or new theoretical results in mathematics, or with synthetic data, it is not Shannon or algorithmic information. We argue that these unintuitive properties of information theory are a consequence of assuming unlimited computation for the observer. With limited computation, a description of the AlphaZero algorithm and the result of running AlphaZero for thousands of TPU hours are distinct. To build intuition, we start with the humble CSPRNG which also creates time-bounded information through computation (albeit random information).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Paradox 2: Information Content is Independent of Factorization", "weight": 1.0} -->

An important property of Shannon's information is the symmetry of information, which states that the amount of information content does not change with factorization. The information we acquire when predicting $x$ and then $y$ is exactly equal to when predicting $y$ and then $x$: Shannon entropy satisfies ${{H{({Y \mid X})}} + {H{(X)}}} = {H{(X,Y)}} = {{H{({X \mid Y})}} + {H{(Y)}}}$. An analogous property also holds for Kolmogorov complexity, known as the symmetry of information identity: ${{K{({y \mid x})}} + {K{(x)}}} = {{K{({x \mid y})}} + {K{(y)}} + {O{}}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Paradox 2: Information Content is Independent of Factorization", "weight": 1.0} -->

On the other hand, multiple works have observed that natural text is better compressed (with final model achieving higher likelihoods) when modeled in the left-to-right order (for English) than when modeled in reverse order, picking out an arrow of time in LLMs where one direction of modeling is preferred over the other. It seems likely that for many documents, other orderings may lead to more information extracted by LLMs. Similarly, as we will show later, small rearrangements of the data can lead to substantially different losses and downstream performance. Cryptographic primitives like one way functions and block cyphers also provide examples where the order of conditioning can make all the difference to how entropic the data appears, for example considering autoregressive modeling of two prime numbers followed by their product vs the reverse ordering. These experimental results and cryptographic ideas indicate what can be learned is dependent on the ordering of the data, which in turn suggests that different amounts of "information" are extracted from these different orderings.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Paradox 2: Information Content is Independent of Factorization", "weight": 1.0} -->

Our time-bounded definitions capture this discrepancy. Under the existence of one way permutations, we can prove that a gap in prediction exists over different factorizations for time bounded entropy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Paradox 3: Likelihood Modeling is Merely Distribution Matching", "weight": 1.0} -->

There is a prevailing view that from a particular training distribution, we can at best hope to match the data generating process. If there is a property or function that is not present in the data-generating process, then we should not expect to learn it in our models. As an extension, if the generating process is simple, then so are models that attempt to match it. This viewpoint can be supported by considering the likelihood maximization process abstractly, ${{{{\arg\min}_{P}{\mathbb{E}}_{X \sim Q}}{\lbrack{- {{\log P}{(X)}}}\rbrack}} = Q};$ the test NLL is minimized when the two distributions match. The extent to which the distributions differ is regarded as a failure either from too limited a function class or insufficient data for generalization. From these arguments we could reasonably believe that AI models cannot surpass human intelligence when pretraining on human data. Here we provide two classes of phenomena that seem to contradict this viewpoint: induction, and emergence.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Paradox 3: Likelihood Modeling is Merely Distribution Matching", "weight": 1.0} -->

In both cases, restricting the compute available to AI models leads them to extract more structural information than what is required for implementing the generating process itself.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Induction", "weight": 1.0} -->

The generative modeling community is often challenged with simultaneously wanting a tractable sampling process and tractable likelihood evaluation, with autoregressors, diffusion models, VAEs, GANs, and normalizing flows each providing different approaches. For natural generative processes, it is often the case that one direction may be much more straightforward than the other. Here we investigate generative processes which can be constructed by transforming latent variables such that computing likelihoods requires inducting on the values of those latents.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Induction", "weight": 1.0} -->

> "*You're reading a murder mystery and at some point the text reveals the identity of the criminal.... If the model can predict \[the name\] then it must have figured out \[who perpetrated the murder from the evidence provided\].*"

<!-- chunk {"id": "body-0062", "role": "body", "section": "Induction", "weight": 1.0} -->

The author of the book on the other hand, need not have made that same induction. Instead, they may have chosen the murderer first and then painted a compelling story of their actions. This example highlights a gap between the generating process and the requirements of a predictive model, a gap which we explore with the following more mathematical setup.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Induction", "weight": 1.0} -->

As we illustrate in Figure 5(a), consider a simple to model random variable $Z$ over ${\{ 0,1\}}^{n}$ which we transform with two functions $m$ and $f$, which are both short in length and efficient to compute, and produce the data $Y = {({m{(Z)}},{f{(Z)}})}$. We choose $m:{{\{ 0,1\}}^{n}\rightarrow{\{ 0,1\}}^{n - h}}$ as a masking function which removes the bits at a total of $h$ fixed locations in the input, leaving the rest unchanged. The generating process is simple to implement and can be executed efficiently. Now consider a likelihood generative model learning to model $Y$, under any given factorization. With appropriate properties of the function $f$, in producing the likelihoods the model must learn to induct on the missing information in the state $Z$, and then apply the transformation given by the data generating process.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Induction", "weight": 1.0} -->

We consider cases both where the function $f$ is hard to invert and those where $f$ is not especially hard to invert. In both cases, predictive circuits must be learned that were not present in the data generating process, but with hard $f$ these circuits only appear at exponentially high compute.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Induction", "weight": 1.0} -->

Induction Hard: Rule 30 ECA. For the first setting we use uniform $Z = U_{n}$ and $f$ as $4$ steps of the rule 30 ECA on state size $n = 32$, $m$ simply removes the first $h$ bits, and we also compute the loss only on $f{(Z)}$ (conditioned on $m{(Z)}$) as the bits in $m{(Z)}$ are uniform and only add noise. We use an LLM, and the loss curves and measured epiplexities are shown in Figure˜5. The loss converges to the number of hidden bits ${- {{\log P}{({{f{(Z)}} \mid {m{(Z)}}})}}} = h$, representing the $2^{h}$ possible inductions on the hidden state.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Induction", "weight": 1.0} -->

However, the total compute required for this loss to converge grows exponentially with $h$, an overall behavior consistent with a strategy of passing all $2^{h}$ candidates through $f$ and then eliminating inconsistent candidates as values of $f{(Z)}_{i}$ are observed with the autoregressive factorization. This complex learned function stands in contrast with the mere $f{(Z)}$ and simple postprocessing removing bits with masking. This picture is mirrored by the measured epiplexity: as the model is forced to induct on the missing bits, the epiplexity grows.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Induction", "weight": 1.0} -->

Induction Easy: Random Markov Chains. In the second setting, we leverage the statistical induction heads setup with a few modifications. $Z$ is given by a random Markov chain transition matrix with $V = 8$ symbols, and $m$ removes $h$ columns of the matrix at fixed random locations. The function $f{(Z)}$ computes a sampled sequence from the Markov chain of length $n = 512$. When $h > 0$, the optimal solution involves 1) using the provided rows $Z$ to perfectly predict next-token probabilities on $V - h$ of the symbols, and 2) inducting on the missing rows of $Z$ in-context based on the empirically observed transitions to improve remaining predictions. For ${h = 0},$ the first is sufficient, and for $h = 8$ the second is sufficient. In Figure˜5, we find evidence that both strategies are employed whenever $0 < h < 8$ as the final loss achieved matches the theoretical loss of both (the lower of the two dotted lines).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Induction", "weight": 1.0} -->

The higher horizontal line marks the loss achievable using 1) along with a simple unigram strategy, showing that the transformer learns 1) first and later the induction strategy 2). While the data generating program only only involves strategy one followed by the postprocessing masking step, the model must learn both strategies to reach these values. Measured epiplexity matches this picture, with values $0 < h < 8$ having higher epiplexity than $h = 0$ or $h = 8$. We emphasize that the induction strategy was never present in the data-generating process, yet it is learned by a generative model trained on that same data distribution.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Induction", "weight": 1.0} -->

In Appendix˜G, we argue the induction phenomena are not specific to autoregressive models, but occur more generally for models trained via Maximum Likelihood Estimation as they need to be able to evaluate the likelihood $P{(x)}$ for an arbitrary data point $x$ rather than merely sample random $x$ from $P.$ VAEs provide a clear example of explicitly performing induction in non-autoregressive models: the encoder is trained specifically to approximate the posterior $P_{Z|X}$, enabling tractable likelihood estimation, yet this encoder is entirely unnecessary if the goal is merely to sample from the model.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Induction", "weight": 1.0} -->

In both of the hard and easy induction examples, the size of the program needed to perform the induction strategy is greater than the size of the program needed generate the data. We can expect that with limited computational constraints, it will not be generically possible to invert the generation process using brute force, and thus, in cases where alternative inverse strategies exist (like the easy induction example with the statistical induction heads), those additional strategies increase the epiplexity. Given that there is likely no single generally applicable strategy for these computationally efficient inverses across problems, it is likely to be possible as a source of epiplexity.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Induction", "weight": 1.0} -->

In other words, there is no bound on how much larger the MDL optimal probability model will be than the generating program even when the model is allowed more compute than the generating program. We present this phenomenon in contrast to Shannon information or Kolmogorov complexity, where a function and its inverse can differ in complexity by at most a fixed constant: ${K{(F^{- 1})}} = {{K{(F)}} + {O{}}}$. When the computational constraints are lifted, the brute force inverse is possible, and there is no essential gap between deduction and induction, or between sampling and likelihood computation.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

One of the most striking counterexamples to the "distribution matching" viewpoint is *emergence*. Even when a system's underlying dynamics admit a simple description, an observer with limited computation may need to learn a richer, and seemingly unrelated, set of concepts to predict or explain its behavior. As articulated by Anderson, reductionism---that a complex object's behavior follows from its parts---does not guarantee that knowing those parts lets us predict the whole. Across biology and physics, many‐body interactions give rise to behaviors (e.g. bird flocking, Conway's Game of Life patterns, molecular chemistry, superconductivity) that are not apparent from the microscopic laws alone. Here we sketch how emergence critically relates to the computational constraints of the observer, demonstrating how observers predicting future states may be required to learn *more* than their unbounded counterparts who can execute the full generating process.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

Consider Type‐Ib emergence in the Carroll and Parola classification, in which higher‐level patterns arise from local rules yet resist prediction from those rules. A canonical example is Conway's Game of Life (see Appendix E for definition), where iterating a simple computational rule $\Phi$ on a $2$D grid leads to complex emergent behavior. For observers that lack the computational resources to directly compute the iterated evolution $\Phi^{k}$, an alternate description must be found. In the state evolution, one can identify localized "species" (static blocks, oscillators, gliders, guns) which propagate through space and time. By classifying these species, learning their velocities, and how they are altered under collisions with other species, as well as the ability to identify their presence in the initial state, computationally more limited observers can make predictions about the future state of the system. Doing so, however, requires a more complex program in the sense of description length, and the epiplexity will be higher. We can formalize this intuition into the following definition of emergence.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

In words, $\Phi,X$ displays emergent phenomena if two observers see equivalent structural complexity in the one step map, but asymptotically more structural complexity in the multistep map for the observer with fewer computational resources.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

Considering $\Phi$ from the Game of Life as an example, $P{({{\Phi{(X)}} \mid {X,n}})}$ could be well estimated by both $T_{1}$ and $T_{2}$-bounded observers using the exact time evolution rule, using constant bits for both. $P{({{\Phi^{k}{(X)}} \mid {X,n,k}})}$ could be estimated by $T_{2}$ using the iterated rule, but not by $T_{1}$. Using knowledge of the different pattern species improves predictions of ${\Phi^{k}{(X)}} \mid X$, so they would need to be learned; however, the number of patterns that needs to be considered in the time-bounded optimal solution is unbounded, and grows with the size of the board $n$, and thus the gap in epiplexity for the two time bounds grows with $n$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

We have not proven that the Game of Life satisfies this definition, which is likely difficult as small changes to the evolution rule can destroy the emergent behavior; however, we provide empirical evidence for this set being non-empty with the example below.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

In Figure˜6, we empirically demonstrate the emergence phenomenon by training a transformer to predict the iterated dynamics of ECA rule 54, a class IV rule that produces complex patterns. As in Conway's Game of Life, a model with sufficient computation can exactly simulate the dynamics by directly iterating the per-step rule---a brute-force solution with a short description length. However, a compute-limited model cannot afford this approach and must instead learn emergent patterns (e.g., gliders and their collision rules) that approximately shortcut the infeasible exact simulation. The brute-force solution can be naturally implemented by learning to autoregressively unroll intermediate ECA states rather than directly predicting the final state, resembling the use of chain-of-thought or looped transformers. We provide experiment details in Section˜C.8. While initially the non-looped model (directly predicting final state) gradually achieves better MDL and higher epiplexity as compute increases, we identify a compute threshold beyond which the looped model suddenly becomes favorable, causing an abrupt drop in MDL and epiplexity, likely by learning the simple, brute-force solution.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

Below this threshold, the looped model underperforms likely because it lacks the compute to fully unroll the dynamics. The non-looped model, unable to rely on brute-force simulation, must instead learn increasingly sophisticated emergent rules, recognizing more species and their interactions, thus causing epiplexity to initially rise with compute before eventually falling.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

While this experiment cleanly demonstrates how compute-limited models can learn richer structure from data, it is a more uncommon situation where the brute-force solution is accessible, and where training with more compute reveals a much simpler underlying structure. With natural data and compute bounds that are not extraordinarily high, we expect that expending additional compute leads to increased rather than decreased observed structure.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Emergent Phenomena", "weight": 1.0} -->

We explore other kinds of emergence, such as in chaotic dynamical systems or in the optimal strategies of game playing agents in Appendix F. Each of these examples presents clear evidence that in pursuit of the best probability distribution to explain the data, observers with limited compute will require models with greater description length than the minimal data generating process in order to achieve comparable predictive performance. Epiplexity provides a general tool for understanding and quantifying these phenomena of emergence, and how simple rules can create meaningful, complex structures that AI models can learn, as recently demonstrated empirically by Zhang et al..

<!-- chunk {"id": "body-0081", "role": "body", "section": "Epiplexity, Pre-Training, and OOD Generalization", "weight": 1.0} -->

Pre-training on internet-scale data has led to remarkable OOD generalization, yet a thorough understanding of this phenomenon remains elusive. What kinds of data provide the best signal for enabling broad generalization? Why does pre-training on text yield capabilities that transfer across domains while image data does not? As high-quality internet data becomes exhausted, what metric should guide the selection or synthesis of new pre-training data? In this section, we show how epiplexity helps answer these foundational questions.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Epiplexity, Pre-Training, and OOD Generalization", "weight": 1.0} -->

OOD generalization is fundamentally about how much reusable structure the model acquires, not how well it predicts in-distribution. Two models trained on different corpora can achieve the same in-distribution loss, yet differ dramatically in their ability to transfer to OOD tasks. This happens because loss captures only the residual unpredictability, corresponding to the time-bounded entropy, not how much reusable structure the model has internalized to achieve that loss. Epiplexity measures exactly this missing component: the amount of information in the learned program. Intuitively, loss indicates how random the data looks to the model, while epiplexity indicates how much structure the model must acquire to explain away the non-random part. If OOD generalization depends on reusing learned mechanisms rather than memorizing superficial statistics, then epiplexity is a natural lens through which to understand the relationship between pre-training data and OOD transfer.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Epiplexity, Pre-Training, and OOD Generalization", "weight": 1.0} -->

As a motivating toy example, Zhang et al. observed that downstream task performance benefits most from training on type IV ECA rules over the other ECA rules, aligned with Figure 3 where we showed that rule 54 (a type IV rule) induces much higher epiplexity compared to other rules.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Epiplexity Correlates with OOD Generalization in Chess", "weight": 1.0} -->

We finetune models trained on either ordering from Section˜5.2 on two downstream tasks: solving chess puzzles, where the model must predict the *optimal* next move given a board state, and predicting centipawn evaluation, where the model evaluates positional advantage from FEN notation---a more substantial distribution shift from next-move prediction learned in pre-training. Experiment details are in Section˜C.4. As shown in Figure 7, the reverse (board-then-moves) ordering yields higher epiplexity and better downstream performance: matching accuracy on chess puzzles but significantly higher accuracy on the centipawn task. This result supports our hypothesis: the reverse order forces the model to develop richer board-state representations needed to infer the intermediate moves, and these representations transfer to OOD tasks like centipawn evaluation that similarly require understanding the board state. This example reflects a more general principle: epiplexity measures the learnable structural information a model extracts from data to its weights, which is precisely the source of the information transferable to novel tasks, making epiplexity a plausible indicator for the potential of OOD generalization.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Epiplexity Correlates with OOD Generalization in Chess", "weight": 1.0} -->

However, we emphasize that higher epiplexity does not guarantee better generalization to any specific task: epiplexity measures the amount of structural information, irrespective of its content. A model trained on high epiplexity data can learn a lot of structures, but these structures may or may not be relevant to the particular downstream task of interest.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Epiplexity Correlates with OOD Generalization in Chess", "weight": 1.0} -->

(c) ADO: epiplexity and downstream metrics

<!-- chunk {"id": "body-0087", "role": "body", "section": "Measuring Structural Information in Natural Data", "weight": 1.0} -->

Among different modalities of natural data, language has proven uniquely fruitful for pre-training, not only for improving in-distribution performance such as language understanding, but also for out-of-distribution tasks such as robotics control, formal theorem proving, and time-series forecasting. While equally abundant total information is available in other modalities, such as images and videos, pre-training on those data sources typically does not confer a similarly broad increase in capabilities. We now show that epiplexity helps explain this asymmetry by revealing differences in their structural information content. In Figure˜8, we show the estimated decomposition of the information in 5B tokens of data from OpenWebText, Lichess, and CIFAR-5M into epiplexity (structural) and time-bounded entropy (random) with a time-bound of $6 \times 10^{18}$ FLOPs, by training models of up to 160M parameters on at most 5B tokens using requential coding. In all cases, epiplexity accounts for only a tiny fraction of the total information, with the OpenWebText carrying the most epiplexity, followed by chess data.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Measuring Structural Information in Natural Data", "weight": 1.0} -->

Despite having the most total information, CIFAR-5M data has the least epiplexity, as over $99\%$ of its information is random (e.g., unpredictability of the exact pixels).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Estimating Epiplexity from Scaling Laws", "weight": 1.0} -->

We can estimate the epiplexities of larger datasets at higher compute budgets using reported scaling laws, which describe the loss achieved by an $N$-parameter model trained on $D$ tokens as ${\mathcal{L}{(N,D)}} = {E + \left( {N/N_{0}} \right)^{- \alpha} + \left( {D/D_{0}} \right)^{- \beta}}$, for some dataset-specific constants $\alpha,\beta,N_{0},D_{0},E$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Estimating Epiplexity from Scaling Laws", "weight": 1.0} -->

By estimating the model's description length via the prequential coding approach (Section˜4.3), we obtain estimates for the epiplexity and time-bounded entropy for language, image, and video datasets, with varying resolutions and tokenizations of size $\mathcal{D} = 10^{12}$ (1T) tokens under a compute budget of $10^{25}$ FLOPs (equivalent to the training compute of Llama3 70B), illustrated in Figure˜8 (see details in Section˜C.9). Consistent with our smaller-scale experiments, we find that language data has the highest epiplexity, while image data has the least. For image data, applying VQ tokenization leads to a significant increase in epiplexity, likely as a result of allowing the model to focus on higher-level semantic structures. Video data has less time-bounded entropy and epiplexity than image data with the same resolution, likely due to significant redundancy across the temporal dimension.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Estimating Epiplexity from Scaling Laws", "weight": 1.0} -->

Using this approach, we can also gain some analytical insights about epiplexity for data admitting scaling laws of this form. As we derive in Section˜B.3, for a fixed dataset $X$ with $\mathcal{D}$ tokens, the optimal split of the compute budget between training and inference (evaluating the trained model on $X$) approaches a fixed ratio as compute increases, with the optimal asymptotic training tokens $D_{\infty}^{\star} = \mathcal{D}$ and asymptotic epiplexity ${{S_{\infty}{(X)}} = {\frac{\beta}{1 - \beta}D_{0}^{\beta}\mathcal{D}^{1 - \beta}}},$ both illustrated in Figure˜9. As expected, the maximum amount of extractable structural information is ultimately capped by the dataset size $\mathcal{D}$ when compute is not the bottleneck, and epiplexity can increase further if we also grow the dataset size.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Estimating Epiplexity from Scaling Laws", "weight": 1.0} -->

For large $\mathcal{D},$ the scale of the asymptotic epiplexity is primarily determined by $\beta$ and $D_{0},$ with smaller $\beta$ and larger $D_{0}$ leading to higher epiplexity, corresponding to slower improvement in loss and thus more (estimated) information absorbed per token. In line with our discussion on emergence in Section˜5.3.2, it is possible that with significantly more compute much simpler programs can model these natural datasets, such as by directly simulating the basic laws of physics from which the natural world emerges, but the amount of required computation is likely so high that such programs remain inaccessible to any physically realizable observer and we must treat natural data as having high epiplexity for all practical purposes.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Pre-Training Data Selection and Curriculum for Language Models", "weight": 1.0} -->

A crucial step in pretraining a language model is designing the composition of the pretraining data, but there lack clear guidelines for this step. Existing data mixtures are designed through extensive trial-and-error and rely on heuristic guidelines such as "diversity" or "high-quality". More importantly, the primary way of comparing different training data is via perplexity metrics of held-out datasets and downstream performance. These procedures are highly susceptible to data contamination, overfitting to a narrow set of downstream evaluations, and Goodhart's law. After all, no suite of downstream evaluations is extensive enough to faithfully capture the range of tasks that a general-purpose language model will encounter in the real world.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Pre-Training Data Selection and Curriculum for Language Models", "weight": 1.0} -->

As we argued above, epiplexity measures the structural information learned by the model, which could be affected by data selection strategies. Jiang et al. demonstrated that models of the loss curves for different data subsets can be used to dynamically adjust the data distribution online to favor data subsets whose training losses are *decreasing faster*^55^5It is worth noting that choosing data subsets with faster-decreasing loss does not mean that the observed training loss would be smaller because such data subsets tend to have higher loss values since there is more learnable information in them. Consequently, training on them often leads to a larger area under the training loss curve.. Intuitively, this objective aligns with increasing the prequential estimate of epiplexity described in Section˜4.1 by maximizing information absorbed per token. We hypothesize that the proposed algorithm, Adaptive Data Optimization (ADO), inadvertently achieves higher epiplexity. Experiments of Jiang et al. are conducted on decoder-only transformers with 1.3B parameters trained on 125B tokens from the Pile dataset.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Pre-Training Data Selection and Curriculum for Language Models", "weight": 1.0} -->

The models are evaluated on a suite of 7 zero-shot downstream tasks and two OOD validation datasets, SlimPajama and FineWeb.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Pre-Training Data Selection and Curriculum for Language Models", "weight": 1.0} -->

In Figure 8(c), we show the estimated epiplexity and the downstream performance as well as perplexity on two OOD datasets, adapted from Jiang et al.. As shown in Jiang et al., ADO achieves higher downstream performance than a standard data sampling strategy that uniformly samples from the entire dataset (denoted by *Natural* in Figure 8), despite not being optimized for any of these metrics. Interestingly, we see that ADO indeed achieves higher epiplexity measured by prequential coding. While these downstream evaluations do not capture everything about a pretrained model, they do offer evidence that epiplexity is a potentially useful concept for understanding the intrinsic value of pretraining data without particular downstream evaluations.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Epiplexity builds on a number of related ideas in algorithmic information theory and complexity science that attempt to theoretically characterize *meaningful information*. A group of closely related concepts are sophistication (subsection 2.2), effective complexity, and logical depth. Similar to sophistication, effective complexity aims to separate random from structural content. From a different starting point, Bennett introduced logical depth, measuring the number of time steps required by a nearly optimal program to produce a given string, and which was later shown to be equivalent to sophistication through the busy beaver function. Several other formal measures have been developed to quantify structured or meaningful complexity. Algorithmic statistics offers a principled decomposition of data into regular versus random components by introducing the notion of an algorithmic sufficient statistic, a concept closely tied to sophistication. Relatedly, statistical complexity in computational mechanics measures the entropy of causal states in an optimally predictive model, capturing structure in time-series data. As we argued above, these existing notions of complexity do not account for the limited computation available to the observer, which is essential for understanding machine learning algorithms.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Being oblivious to computational limits means that they cannot characterize CSPRNGs or encrypted objects as being random. One might think that these failures are surface-level; for example, a plausible strategy would be to upgrade sophistication by replacing Kolmogorov complexity with time-bounded Kolmogorov complexity in (Definition 5) ‣ 2.2 Random vs Structural Information ‣ 2 Background ‣ From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence")). However, this approach does not work for several reasons, the most obvious being that CSPRNG outputs do have short and efficiently runnable generating programs and thus their time-bounded Kolmogorov complexities are small. A more subtle reason is that doing so results in trivial sophistication for all strings, which we discuss in more detail in Appendix A.6.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Our work is also closely related to several lines of work trying to characterize observer-dependent notions of information. In cryptography, Barak et al. and Hsiao et al. discuss several possible definitions for *computational pseudoentropy*, an observer-dependent analogue of entropy. HILL-pseudoentropy is defined relative to a class of tests: a source is considered random if no test within the class can distinguish it from a high-entropy distribution with nontrivial advantage, and Yao-pseudoentropy is defined via compressing and decompressing an object for example. Both definitions are closely related to time-bounded entropy, which measures the random content to a given computationally bounded observer; however, our formulation directly maps on to machine learning practice and allows for separating out the structural information content, a key contribution of our work. More recently, Xu et al. propose $\mathcal{V}$-entropy, a generalization of Shannon entropy to the minimum expected negative log probability over a given family of probability models, such as those with given computational constraints.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

With $\mathcal{V}$-entropy, the symmetry of information can be violated, and so too can the data processing inequality, though neither is explicitly proven in the paper. Unlike time-bounded entropy, the computational constraint in $\mathcal{V}$-entropy only limits the inference time, and does not account for the time to find such a model. Hence, the minimizer can be far away from the regime that is practically evaluated (such as models that are *trained* on infinite data or with infinite compute). While these undesirable behaviors can be overcome by imposing further data constraints, we believe our formulation of imposing a single bound on both training and inference time leads to fewer complications. More importantly, both pseudoentropy and $\mathcal{V}$-entropy, much like time-bounded entropy, capture only the random component of information since it still measures the unpredictability of the random variable under the best feasible model. For understanding what useful information a model has learned, we are more interested in the non-random component of information as measured by epiplexity.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Using existing measures of complexity, such as the Lempel-Ziv complexity and Wolfram classification, Zhang et al. showed that models trained on complex data like Class IV ECA rules tend to perform better on downstream tasks.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Other parts, such as the area under the curve estimate of epiplexity, have seen some related exploration in prior work. The concept of excess entropy, independently introduced under various names and reviewed in Feldman, is defined as the area between finite-block entropy density estimates and the asymptotic entropy rate of a stationary process, an analogous construction to our prequential estimate of epiplexity. However, excess entropy is defined for stationary processes observed by computationally unbounded agents, lacking the explicit dependence on the observer's compute budget that we view as essential for the machine learning setting. More recently, Whitney et al. introduced surplus description length (SDL), which is the summed online loss of the training algorithm, with either the entropy of the data or a fixed baseline performance subtracted out. The authors use this measurement to evaluate pre-trained representations for solving a downstream task, arguing that smaller SDL is preferred as they lead to more efficient downstream learning. In contrast, we seek to create datasets and interventions to the data which *increase* epiplexity.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

More analogous to the spirit of epiplexity is information transfer from Zhang et al., which sums a variant of a loss difference, adapted to held out test data and for the classification setting. In this work, the authors present information transfer to measure how much is learned from the data. Epiplexity is complementary to these works, clarifying the role of computation in defining information, and explicitly separating random and structural information.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Several works have also explored how to quantify data complexity. Dziugaite and Roy suggests that the complexity of a minimal near-optimal reference model can be viewed as a measure of data complexity under the PAC-Bayes framework and how such data complexity gives rise to empirical scaling laws. This perspective is related to epiplexity in that both associate data complexity with the size of compact models that explain the data well. However, the two notions differ in important ways. In particular, the PAC-Bayes formulation is concerned with the existence of some small reference model achieving good in-distribution performance, whereas epiplexity characterizes the amount of structural information extractable by a computationally bounded observer, formalized through a two-part code that explicitly accounts for the cost of obtaining such a model. Further, our primary interest is not in characterizing in-distribution generalization, but in using epiplexity to measure the intrinsic value of data in settings that extend beyond supervised learning. Relatedly, Hutter shows that power-law learning curves can emerge under specific assumptions on the data-generating distribution, illustrating how properties of the data itself can shape empirical scaling behavior.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

While this line of work focuses on explaining observed learning dynamics rather than defining a complexity measure, it similarly emphasizes the role of data structure in determining learning outcomes. These perspectives on data complexity can be viewed as instances of *coarse graining*, where one seeks a compressed representation that preserves some notion of "relevant" structure. A canonical example is the information bottleneck framework, which formalizes coarse graining as a trade-off between compression and retained information about a relevant variable. Epiplexity is aligned with this perspective, but rather than defining relevance through a task variable or through distinguishability to tests, it measures the amount of structural information extractable by a computationally bounded learner, while explicitly accounting for the cost of obtaining the model.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

More broadly, our work is related to several lines of work on how resource constraints fundamentally alter the notion of simplicity and learnability. In algorithmic information theory, Schmidhuber proposes the speed prior, which replaces Solomonoff's universal prior with a *computable* semimeasure that favors both shorter program length and smaller computation time, thereby incorporating computational resources directly into the definition of simplicity. Achille and Soatto argue that in the transductive setting, the role of information from past data is to reduce the time needed to solve new tasks rather than to reduce uncertainty, with the optimal speedup tightly characterized by the amount of shared algorithmic information between past data and future tasks. In this setting, *larger* information content is shown to be more conducive to better performance. In learning theory, a related line of work shows that computational limitations can directly affect what can be learned from data. For instance, in the problem of sparse PCA detection, Berthet and Rigollet show that although there exist procedures that succeed with an information-theoretically minimal number of samples, any algorithm that runs in polynomial time necessarily requires more data under widely used average-case hardness assumptions.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Additional Related Work", "weight": 1.0} -->

Memory and space constraints alone can also qualitatively change learnability. Steinhardt et al. show that restricting a learner's memory can dramatically increase the amount of data required to learn, even when the target concept itself has a very concise description. They identify parity functions as a canonical example where this tension is conjectured to be sharp. Raz later resolves this conjecture by proving that any learner with sub-quadratic memory requires exponentially many samples to learn parity from random examples.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discussion", "weight": 1.5} -->

Much of classical information theory is concerned with the representation and transmission of information, and abstracts away key aspects of the computational processes by which information is extracted and used. While complexity theory and cryptography treat computation as fundamental, machine learning theory typically does not. Yet learning, whether biological or artificial, is an inherently computational process. What can be learned from data depends not only on statistical feasibility, but on the available resources. This perspective calls for more theoretical tools that place computation on an equal footing with information.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Discussion", "weight": 1.5} -->

This work reframes information as a property of data relative to a computationally bounded observer, and demonstrates that information can be decomposed into time-bounded entropy and epiplexity, a formalization of structural information. It also sheds light on how perceived information can be changed through computation. This perspective resolves several tensions between information theory and empirical machine learning---including the usefulness of synthetic data, the dependence of learning on factorization and ordering, and the emergence of structure beyond the data-generating process itself. Technically, epiplexity connects ideas from algorithmic statistics, cryptography, and learning theory, showing that standard assumptions (i.e., existence of one-way functions) suffice to produce distributions with high structural complexity for efficient learners.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our framework opens several exciting directions for future work. On the theoretical side, it invites a systematic and more fine-grained understanding of how structural information changes with computational budget, model class, and data transformations, potentially yielding new lower bounds and impossibility results for representation learning and transfer. Taking information and computation as the fundamental resources may offer new explanations for the relative universality observed in large-scale training, including why scaling law exponents depend only weakly on architectural and optimizer details. There is also a possibility of a compute-aware analogue of classical notions such as sufficient statistics and information bottlenecks. More broadly, framing emergence, induction, and generalization through the lens of computationally bounded observers may offer a unifying language across learning theory, algorithmic information theory, cryptography, and complexity theory.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Discussion", "weight": 1.5} -->

On the empirical side, epiplexity provides a way to reason about why some data sources, formatting, and transformations can lead to more transferable models than others, even when they do not improve training loss. The framework suggests that pretraining data should be evaluated not only by held-out perplexity, but by how much reusable structural information it induces in a computationally bounded model. This perspective helps explain empirical successes of curriculum design, data ordering, augmentation strategies, and even synthetic data that appear counterintuitive from a purely statistical viewpoint. Our empirical estimator offers a concrete starting point for comparing datasets and interventions in data centric research. In the long run, we believe epiplexity could provide guidance on how to generate new synthetic data from existing data.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, representation learning can be understood as the gradual accumulation of epiplexity: the construction of increasingly rich internal programs that approximate a data distribution within a fixed time budget. While epiplexity in isolation is not a measure of generalization, or a complete theory of learning, this perspective raises the possibility of new notions of hardness for learning and transfer that are orthogonal to classical PAC-style measures, capturing not sample complexity but the size of the structure that must be extracted. Such notions may help explain why certain tasks appear to require disproportionately large models or long training horizons despite admitting simple generative descriptions, and why improvements in generalization sometimes correlate more strongly with training dynamics or data structure than with likelihood alone.
