<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scaling Laws for Neural Language Models

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Language provides a natural domain for the study of artificial intelligence, as the vast majority of reasoning tasks can be efficiently expressed and evaluated in language, and the world's text provides a wealth of data for unsupervised learning via generative modeling. Deep learning has recently seen rapid progress in language modeling, with state of the art models \[ YDY^+^19, LOG^+^19, RSR^+^19\] approaching human-level performance on many specific tasks \[WPN^+^19\], including the composition of coherent multi-paragraph prompted text samples \[RWC^+^19\].

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

One might expect language modeling performance to depend on model architecture, the size of neural models, the computing power used to train them, and the data available for this training process. In this work we will empirically investigate the dependence of language modeling loss on all of these factors, focusing on the Transformer architecture \[VSP^+^17, LSP^+^18\]. The high ceiling and low floor for performance on language tasks allows us to study trends over more than seven orders of magnitude in scale.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Throughout we will observe precise power-law scalings for performance as a function of training time, context length, dataset size, model size, and compute budget.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Performance depends strongly on scale, weakly on model shape", "weight": 1.0} -->

Model performance depends most strongly on scale, which consists of three factors: the number of model parameters $N$ (excluding embeddings), the size of the dataset $D$, and the amount of compute $C$ used for training. Within reasonable limits, performance depends very weakly on other architectural hyperparameters such as depth vs. width. (Section 3)

<!-- chunk {"id": "body-0007", "role": "body", "section": "Smooth power laws", "weight": 1.0} -->

Performance has a power-law relationship with each of the three scale factors $N,D,C$ when not bottlenecked by the other two, with trends spanning more than six orders of magnitude (see Figure 1). We observe no signs of deviation from these trends on the upper end, though performance must flatten out eventually before reaching zero loss. (Section 3)

<!-- chunk {"id": "body-0008", "role": "body", "section": "Universality of overfitting", "weight": 1.0} -->

Performance improves predictably as long as we scale up $N$ and $D$ in tandem, but enters a regime of diminishing returns if either $N$ or $D$ is held fixed while the other increases. The performance penalty depends predictably on the ratio $N^{0.74}/D$, meaning that every time we increase the model size 8x, we only need to increase the data by roughly 5x to avoid a penalty. (Section 4)

<!-- chunk {"id": "body-0009", "role": "body", "section": "Universality of training", "weight": 1.0} -->

Training curves follow predictable power-laws whose parameters are roughly independent of the model size. By extrapolating the early part of a training curve, we can roughly predict the loss that would be achieved if we trained for much longer. (Section 5)

<!-- chunk {"id": "body-0010", "role": "body", "section": "Transfer improves with test performance", "weight": 1.0} -->

When we evaluate models on text with a different distribution than they were trained, the results are strongly correlated to those on the training validation set with a roughly constant offset in the loss -- in other words, transfer to a different distribution incurs a constant penalty but otherwise improves roughly in line with performance on the training set. (Section 3.2.2)

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sample efficiency", "weight": 1.0} -->

Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Convergence is inefficient", "weight": 1.0} -->

When working within a fixed compute budget $C$ but without any other restrictions on the model size $N$ or available data $D$, we attain optimal performance by training *very large models* and stopping *significantly short of convergence* (see Figure 3). Maximally compute-efficient training would therefore be far more sample efficient than one might expect based on training small models to convergence, with data requirements growing very slowly as $D \sim C^{0.27}$ with training compute. (Section 6)

<!-- chunk {"id": "body-0013", "role": "body", "section": "Optimal batch size", "weight": 1.0} -->

The ideal batch size for training these models is roughly a power of the loss only, and continues to be determinable by measuring the gradient noise scale; it is roughly 1-2 million tokens at convergence for the largest models we can train. (Section 5.1 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models"))

<!-- chunk {"id": "body-0014", "role": "body", "section": "Optimal batch size", "weight": 1.0} -->

Taken together, these results show that language modeling performance improves smoothly and predictably as we appropriately scale up model size, data, and compute. We expect that larger language models will perform better and be more sample efficient than current models.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

When training with a limited amount of compute, a sufficiently large dataset, an optimally-sized model, and a sufficiently small batch size (making optimal^22^2We also observe an empirical power-law trend with the training compute $C$ (Figure 1) while training at fixed batch size, but it is the trend with $C_{\min}$ that should be used to make predictions. They are related by equation (5.5 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

These relations hold across eight orders of magnitude in $C_{\min}$, six orders of magnitude in $N$, and over two orders of magnitude in $D$. They depend very weakly on model shape and other Transformer hyperparameters (depth, width, number of self-attention heads), with specific numerical values associated with the Webtext2 training set \[RWC^+^19\]. The power laws $\alpha_{N},\alpha_{D},\alpha_{C}^{\min}$ specify the degree of performance improvement expected as we scale up $N$, $D$, or $C_{\min}$; for example, doubling the number of parameters yields a loss that is smaller by a factor $2^{- \alpha_{N}} = 0.95$. The precise numerical values of ${N_{c},C_{c}^{\min}},$ and $D_{c}$ depend on the vocabulary size and tokenization and hence do not have a fundamental meaning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

Equation (1.1) and (1.2) together suggest that as we increase the model size, we should increase the dataset size sublinearly according to $D \propto N^{\frac{\alpha_{N}}{\alpha_{D}}} \sim N^{0.74}$. In fact, we find that there is a single equation combining (1.1) and (1.2)

<!-- chunk {"id": "body-0018", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

with fits pictured on the left in figure 4. We conjecture that this functional form may also parameterize the trained log-likelihood for other generative modeling tasks.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

When training a given model for a finite number of parameter update steps $S$ in the infinite data limit, after an initial transient period, the learning curves can be accurately fit by (see the right of figure 4)

<!-- chunk {"id": "body-0020", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

where $S_{c} \approx {2.1 \times 10^{3}}$ and $\alpha_{S} \approx 0.76$, and $S_{\min}{(S)}$ is the minimum possible number of optimization steps (parameter updates) estimated using Equation (5.4 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

When training within a fixed compute budget $C$, but with no other constraints, Equation (1.6) leads to the prediction that the optimal model size $N$, optimal batch size $B$, optimal number of steps $S$, and dataset size $D$ should grow as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

which closely matches the empirically optimal results $N \propto C_{\min}^{0.73}$, $B \propto C_{\min}^{0.24}$, and $S \propto C_{\min}^{0.03}$. As the computational budget $C$ increases, it should be spent primarily on larger models, without dramatic increases in training time or dataset size (see Figure 3). This also implies that as models grow larger, they become increasingly sample efficient. In practice, researchers typically train smaller models for longer than would be maximally compute-efficient because of hardware constraints. Optimal performance depends on total compute as a power law (see Equation (1.3)).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Summary of Scaling Laws", "weight": 1.0} -->

We provide some basic theoretical motivation for Equation (1.5), an analysis of learning curve fits and their implications for training time, and a breakdown of our results per token. We also make some brief comparisons to LSTMs and recurrent Transformers \[DGV^+^18\].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

nlayer dmodel 3 dattn
2 nlayer dmodel 3 dattn

<!-- chunk {"id": "body-0025", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

nlayer dattn dmodel
2 nlayer dattn dembd

<!-- chunk {"id": "body-0026", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

nlayer 2 dmodel dff
2 nlayer 2 dmodel dff

<!-- chunk {"id": "body-0027", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

N = 2 dmodel nlayer (2 dattn+dff)
Cforward = 2 N + 2 nlayer nctx dattn

<!-- chunk {"id": "body-0028", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

We parameterize the Transformer architecture using hyperparameters $n_{layer}$ (number of layers), $d_{model}$ (dimension of the residual stream), $d_{ff}$ (dimension of the intermediate feed-forward layer), $d_{attn}$ (dimension of the attention output), and $n_{heads}$ (number of attention heads per layer). We include $n_{ctx}$ tokens in the input context, with $n_{ctx} = 1024$ except where otherwise noted.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

where we have excluded biases and other sub-leading terms. Our models also have $n_{vocab}d_{model}$ parameters in an embedding matrix, and use $n_{ctx}d_{model}$ parameters for positional embeddings, but we do not include these when discussing the 'model size' $N$; we will see that this produces significantly cleaner scaling laws.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

Evaluating a forward pass of the Transformer involves roughly

<!-- chunk {"id": "body-0031", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

add-multiply operations, where the factor of two comes from the multiply-accumulate operation used in matrix multiplication. A more detailed per-operation parameter and compute count is included in Table 1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Parameter and Compute Scaling of Transformers", "weight": 1.0} -->

For contexts and models with $d_{model} > {n_{ctx}/12}$, the context-dependent computational cost per token is a relatively small fraction of the total compute. Since we primarily study models where $d_{model} \gg {n_{ctx}/12}$, we do not include context-dependent terms in our training compute estimate. Accounting for the backwards pass (approximately twice the compute as the forwards pass), we then define the estimated non-embedding compute as $C \approx {6N}$ floating point operators per training token.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Training Procedures", "weight": 1.0} -->

Unless otherwise noted, we train models with the Adam optimizer for a fixed $2.5 \times 10^{5}$ steps with a batch size of $512$ sequences of $1024$ tokens. Due to memory constraints, our largest models (more than 1B parameters) were trained with Adafactor. We experimented with a variety of learning rates and schedules, as discussed in Appendix D.6. We found that results at convergence were largely independent of learning rate schedule. Unless otherwise noted, all training runs included in our data used a learning rate schedule with a 3000 step linear warmup followed by a cosine decay to zero.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Datasets", "weight": 1.0} -->

We train our models on an extended version of the WebText dataset described in \[RWC^+^19\]. The original WebText dataset was a web scrape of outbound links from Reddit through December 2017 which received at least 3 karma. In the second version, WebText2, we added outbound Reddit links from the period of January to October 2018, also with a minimum of 3 karma. The karma threshold served as a heuristic for whether people found the link interesting or useful. The text of the new links was extracted with the Newspaper3k python library. In total, the dataset consists of 20.3M documents containing 96 GB of text and $1.62 \times 10^{10}$ words (as defined by wc). We then apply the reversible tokenizer described in \[RWC^+^19\], which yields $2.29 \times 10^{10}$ tokens.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Datasets", "weight": 1.0} -->

We reserve $6.6 \times 10^{8}$ of these tokens for use as a test set, and we also test on similarly-prepared samples of Books Corpus \[ZKZ^+^15\], Common Crawl \[Fou\], English Wikipedia, and a collection of publicly-available Internet Books.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Empirical Results and Basic Power Laws", "weight": 1.0} -->

Model size (ranging in size from 768 to 1.5 billion non-embedding parameters)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Empirical Results and Basic Power Laws", "weight": 1.0} -->

Dataset size (ranging from 22 million to 23 billion tokens)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Empirical Results and Basic Power Laws", "weight": 1.0} -->

Shape (including depth, width, attention heads, and feed-forward dimension)

<!-- chunk {"id": "body-0039", "role": "body", "section": "Empirical Results and Basic Power Laws", "weight": 1.0} -->

Context length (1024 for most runs, though we also experiment with shorter contexts)

<!-- chunk {"id": "body-0040", "role": "body", "section": "Empirical Results and Basic Power Laws", "weight": 1.0} -->

Batch size ($2^{19}$ for most runs, but we also vary it to measure the critical batch size)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Empirical Results and Basic Power Laws", "weight": 1.0} -->

In this section we will display data along with empirically-motivated fits, deferring theoretical analysis to later sections.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Approximate Transformer Shape and Hyperparameter Independence", "weight": 1.0} -->

Transformer performance depends very weakly on the shape parameters $n_{layer},n_{heads}$, and $d_{ff}$ when we hold the total non-embedding parameter count $N$ fixed. To establish these results we trained models with fixed size while varying a single hyperparameter. This was simplest for the case of $n_{heads}$. When varying $n_{layer}$, we simultaneously varied $d_{model}$ while keeping $N \approx {12n_{layer}d_{model}^{2}}$ fixed. Similarly, to vary $d_{ff}$ at fixed model size we also simultaneously varied the $d_{model}$ parameter, as required by the parameter counts in Table 1. Independence of $n_{layers}$ would follow if deeper Transformers effectively behave as ensembles of shallower models, as has been suggested for ResNets. The results are shown in Figure 5.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Performance with Non-Embedding Parameter Count $N$", "weight": 1.0} -->

In Figure 6 we display the performance of a wide variety of models, ranging from small models with shape ${(n_{layer},d_{model})} = {}$ through billion-parameter models, ranging in shape from $$ through $$. Here we have trained to near convergence on the full WebText2 dataset and observe no overfitting (except possibly for the very largest models).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Performance with Non-Embedding Parameter Count $N$", "weight": 1.0} -->

As shown in Figure 1, we find a steady trend with non-embedding parameter count $N$, which can be fit to the first term of Equation (1.5), so that

<!-- chunk {"id": "body-0045", "role": "body", "section": "Performance with Non-Embedding Parameter Count $N$", "weight": 1.0} -->

To observe these trends it is crucial to study performance as a function of $N$; if we instead use the total parameter count (including the embedding parameters) the trend is somewhat obscured (see Figure 6). This suggests that the embedding matrix can be made smaller without impacting performance, as has been seen in recent work \[LCG^+^19\].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Performance with Non-Embedding Parameter Count $N$", "weight": 1.0} -->

Although these models have been trained on the WebText2 dataset, their test loss on a variety of other datasets is also a power-law in $N$ with nearly identical power, as shown in Figure 8.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparing to LSTMs and Universal Transformers", "weight": 1.0} -->

In Figure 7 we compare LSTM and Transformer performance as a function of non-embedding parameter count $N$. The LSTMs were trained with the same dataset and context length. We see from these figures that the LSTMs perform as well as Transformers for tokens appearing early in the context, but cannot match the Transformer performance for later tokens. We present power-law relationships between performance and context position Appendix D.5, where increasingly large powers for larger models suggest improved ability to quickly recognize patterns.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparing to LSTMs and Universal Transformers", "weight": 1.0} -->

We also compare the performance of standard Transformers to recurrent Transformers \[DGV^+^18\] in Figure 17 in the appendix. These models re-use parameters, and so perform slightly better as a function of $N$, at the cost of additional compute per-parameter.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Generalization Among Data Distributions", "weight": 1.0} -->

We have also tested our models on a set of additional text data distributions. The test loss on these datasets as a function of model size is shown in Figure 8; in all cases the models were trained only on the WebText2 dataset. We see that the loss on these other data distributions improves smoothly with model size, in direct parallel with the improvement on WebText2. We find that generalization depends almost exclusively on the in-distribution validation loss, and does not depend on the duration of training or proximity to convergence. We also observe no dependence on model depth (see Appendix D.8).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Performance with Dataset Size and Compute", "weight": 1.0} -->

We display empirical trends for the test loss as a function of dataset size $D$ (in tokens) and training compute $C$ in Figure 1.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Performance with Dataset Size and Compute", "weight": 1.0} -->

For the trend with $D$ we trained a model with ${(n_{layer},n_{embd})} = {}$ on fixed subsets of the WebText2 dataset. We stopped training once the test loss ceased to decrease. We see that the resulting test losses can be fit with simple power-law

<!-- chunk {"id": "body-0052", "role": "body", "section": "Performance with Dataset Size and Compute", "weight": 1.0} -->

in the dataset size. The data and fit appear in Figure 1.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance with Dataset Size and Compute", "weight": 1.0} -->

The total amount of non-embedding compute used during training can be estimated as $C = {6NBS}$, where $B$ is the batch size, $S$ is the number of parameter updates, and the factor of $6$ accounts for the forward and backward passes. Thus for a given value of $C$ we can scan over all models with various $N$ to find the model with the best performance on step $S = \frac{C}{6BS}$. Note that in these results *the batch size $B$ remains fixed for all models*, which means that these empirical results are not truly optimal. We will account for this in later sections using an adjusted $C_{\min}$ to produce cleaner trends.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Performance with Dataset Size and Compute", "weight": 1.0} -->

The result appears as the heavy black line on the left-hand plot in Figure 1. It can be fit with

<!-- chunk {"id": "body-0055", "role": "body", "section": "Performance with Dataset Size and Compute", "weight": 1.0} -->

The figure also includes images of individual learning curves to clarify when individual models are optimal. We will study the optimal allocation of compute more closely later. The data strongly suggests that sample efficiency improves with model size, and we also illustrate this directly in Figure 19 in the appendix.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Charting the Infinite Data Limit and Overfitting", "weight": 1.0} -->

In Section 3 we found a number of basic scaling laws for language modeling performance. Here we will study the performance of a model of size $N$ trained on a dataset with $D$ tokens while varying $N$ and $D$ simultaneously. We will empirically demonstrate that the optimally trained test loss accords with the scaling law of Equation (1.5). This provides guidance on how much data we would need to train models of increasing size while keeping overfitting under control.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

Changes in vocabulary size or tokenization are expected to rescale the loss by an overall factor. The parameterization of $L{(N,D)}$ (and all models of the loss) must naturally allow for such a rescaling.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

Fixing $D$ and sending $N\rightarrow\infty$, the overall loss should approach $L{(D)}$. Conversely, fixing $N$ and sending $D\rightarrow\infty$ the loss must approach $L{(N)}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

$L{(N,D)}$ should be analytic at $D = \infty$, so that it has a series expansion in $1/D$ with integer powers. Theoretical support for this principle is significantly weaker than for the first two.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

Our choice of $L{(N,D)}$ satisfies the first requirement because we can rescale $N_{c},D_{c}$ with changes in the vocabulary. This also implies that the values of $N_{c},D_{c}$ have no fundamental meaning.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

Since we stop training early when the test loss ceases to improve and optimize all models in the same way, we expect that larger models should always perform better than smaller models. But with fixed finite $D$, we also do not expect any model to be capable of approaching the best possible loss (ie the entropy of text). Similarly, a model with fixed size will be capacity-limited. These considerations motivate our second principle. Note that knowledge of $L{(N)}$ at infinite $D$ and $L{(D)}$ at infinite $N$ fully determines all the parameters in $L{(N,D)}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

The third principle is more speculative. There is a simple and general reason one might expect overfitting to scale $\propto {1/D}$ at very large $D$. Overfitting should be related to the variance or the signal-to-noise ratio of the dataset, and this scales as $1/D$. This expectation should hold for any smooth loss function, since we expect to be able to expand the loss about the $D\rightarrow\infty$ limit. However, this argument assumes that $1/D$ corrections dominate over other sources of variance, such as the finite batch size and other limits on the efficacy of optimization. Without empirical confirmation, we would not be very confident of its applicability.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

Our third principle explains the asymmetry between the roles of $N$ and $D$ in Equation (1.5). Very similar symmetric expressions^33^3For example, one might have used ${L{(N,D)}} = \left\lbrack {\left( \frac{N_{c}}{N} \right)^{\alpha_{N}} + \left( \frac{D_{c}}{D} \right)^{\alpha_{D}}} \right\rbrack^{\beta}$, but this does not have a $1/D$ expansion. are possible, but they would not have a $1/D$ expansion with integer powers, and would require the introduction of an additional parameter.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Proposed $L{(N,D)}$ Equation", "weight": 1.0} -->

In any case, we will see that our equation for $L{(N,D)}$ fits the data well, which is the most important justification for our $L{(N,D)}$ ansatz.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Results", "weight": 1.0} -->

We regularize all our models with 10% dropout, and by tracking test loss and stopping once it is no longer decreasing. The results are displayed in Figure 9 Equation ‣ 4 Charting the Infinite Data Limit and Overfitting ‣ Scaling Laws for Neural Language Models"), including a fit to the four parameters $\alpha_{N},\alpha_{D},N_{c},D_{c}$ in Equation (1.5):

<!-- chunk {"id": "body-0066", "role": "body", "section": "Results", "weight": 1.0} -->

We obtain an excellent fit, with the exception of the runs where the dataset has been reduced by a factor of $1024$, to about $2 \times 10^{7}$ tokens. With such a small dataset, an epoch consists of only 40 parameter updates. Perhaps such a tiny dataset represents a different regime for language modeling, as overfitting happens very early in training (see Figure 16). Also note that the parameters differ very slightly from those obtained in Section 3, as here we are fitting the full $L{(N,D)}$ rather than just $L{(N,\infty)}$ or $L{(\infty,D)}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results", "weight": 1.0} -->

To chart the borderlands of the infinite data limit, we can directly study the extent of overfitting. For all but the largest models, we see no sign of overfitting when training with the full 22B token WebText2 dataset, so we can take it as representative of $D = \infty$. Thus we can compare finite $D$ to the infinite data limit by defining

<!-- chunk {"id": "body-0068", "role": "body", "section": "Results", "weight": 1.0} -->

and studying it as a function of $N,D$. In fact, we see empirically that $\deltaL$ depends only a specific combination of $N$ and $D$, as shown in Figure 16. This follows from the scaling law of Equation (1.5), which implies

<!-- chunk {"id": "body-0069", "role": "body", "section": "Results", "weight": 1.0} -->

Note that at large $D$ this formula also has a series expansion in powers of $1/D$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Results", "weight": 1.0} -->

We estimate that the variation in the loss with different random seeds is roughly $0.02$, which means that to avoid overfitting when training to within that threshold of convergence we require

<!-- chunk {"id": "body-0071", "role": "body", "section": "Results", "weight": 1.0} -->

With this relation, models smaller than $10^{9}$ parameters can be trained with minimal overfitting on the 22B token WebText2 dataset, but our largest models will encounter some mild overfitting. More generally, this relation shows that dataset size may grow sub-linearly in model size while avoiding overfitting. Note however that this does not typically represent maximally compute-efficient training. We should also emphasize that we have not optimized regularization (eg the dropout probability) while varying dataset and model size.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Scaling Laws with Model Size and Training Time", "weight": 1.0} -->

In this section we will demonstrate that a simple scaling law provides a good description for the loss as a function of model size $N$ and training time. First we will explain how to use the results of to define a universal training step $S_{\min}$, which accounts for the fact that most of our models have not been trained at an optimal batch size. Then we will demonstrate that we can fit the model size and training time dependence of the loss using Equation (1.6). Later we will use these results to predict the optimal allocation of training compute between model size and training time, and then confirm that prediction.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

A simple empirical theory for the batch size dependence of training was developed (see also \[SLA^+^18, ZLN^+^19\]). It was argued that there is a critical batch size $B_{crit}$ for training; for $B$ up to $B_{crit}$ the batch size can be increased with very minimal degradation in compute-efficiency, whereas for $B > B_{crit}$ increases in $B$ result in diminishing returns. It was also argued that the gradient noise scale provides a simple prediction for $B_{crit}$, and that neither depends directly on model size except through the value of the loss that has been attained. These results can be used to predict how training time and compute will vary with the batch size. To utilize both training time and compute as effectively as possible, it is best to train with a batch size $B \approx B_{crit}$. Training at $B \gg B_{crit}$ minimizes the number of training steps, while $B \ll B_{crit}$ minimizes the use of compute.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

More specifically, it was demonstrated that for a wide variety of neural network tasks, the number of training steps $S$ and the number of data examples processed $E = {BS}$ satisfy the simple relation

<!-- chunk {"id": "body-0075", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

when training to any fixed value of the loss $L$. Here $S_{\min}$ is the minimum number of steps necessary to reach $L$, while $E_{\min}$ is the minimum number of data examples that must be processed.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

We demonstrate the relation (5.1 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")) for Transformers in Figure 18 in the appendix. This relation defines the critical batch size

<!-- chunk {"id": "body-0077", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

which is a function of the target value of the loss. Training at the critical batch size makes a roughly optimal time/compute tradeoff, requiring $2S_{\min}$ training steps and processing $E = {2E_{\min}}$ data examples.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

In Figure 10 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models") we have plotted the critical batch size and gradient noise scale^44^4Although the critical batch size roughly matches the gradient noise scale, we are using a direct measurements of $B_{crit}$ from Figures 18 and 10 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models") for all our later analyses. as a function of training loss for two different models. We see that $B_{crit}{(L)}$ is independent of model size, and only depends on the loss $L$. So the predictions of continue to hold for Transformer language models. The critical batch size can be fit with a power-law in the loss

<!-- chunk {"id": "body-0079", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

We have chosen this parameterization for $B_{crit}{(L)}$ because as the loss approaches its minimum value $L_{\min}$, the gradient noise scale is expected to diverge, and we expect $B_{crit}$ to track this noise scale. We do not know $L_{\min}$, as we see no sign that our models are approaching it, but $L_{\min} > 0$ since the entropy of natural language is non-zero. Since apparently $L_{\min}$ is much smaller than the values of $L$ we have achieved, we used a parameterization where $B_{crit}$ diverges as $L\rightarrow 0$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

We will use $B_{crit}{(L)}$ to estimate the relation between the number of training steps $S$ while training at batch size $B = 2^{19}$ tokens and the number of training steps while training at $B \gg B_{crit}$. This is simply

<!-- chunk {"id": "body-0081", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

for any given target value $L$ for the loss. This also defines a critical value of the compute needed to train to $L$ with a model of size $N$ if we were to train at $B \ll {B_{crit}{(L)}}$. This is

<!-- chunk {"id": "body-0082", "role": "body", "section": "Adjustment for Training at $B_{crit}{(L)}$", "weight": 1.0} -->

where $C = {6NBS}$ estimates the (non-embedding) compute used at batch size $B$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Results for $L{(N,S_{\\min})}$ and Performance with Model Size and Compute", "weight": 1.0} -->

Now we will use $S_{\min}$ defined in Equation (5.4 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")) to obtain a simple and universal fit for the dependence of the loss on model size and training time in the infinite data limit. We will fit the stable, Adam-optimized training runs using Equation (1.6),

<!-- chunk {"id": "body-0084", "role": "body", "section": "Results for $L{(N,S_{\\min})}$ and Performance with Model Size and Compute", "weight": 1.0} -->

With these parameters, we obtain the learning curve fits in Figure 4. Though the fits are imperfect, we believe they are quite compelling given the simplicity of Equation (5.6 and Performance with Model Size and Compute ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Results for $L{(N,S_{\\min})}$ and Performance with Model Size and Compute", "weight": 1.0} -->

The data and fits can be visualized in a different and more interesting way, as shown in Figure 11 and Performance with Model Size and Compute ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models"). There we study the test loss as a function of model size while fixing either the total non-embedding compute $C$ used in training, or the number of steps $S$. For the fits we use Equation (5.5 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")) and (5.4 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")) along with the parameters above and Equation (5.6 and Performance with Model Size and Compute ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Results for $L{(N,S_{\\min})}$ and Performance with Model Size and Compute", "weight": 1.0} -->

The power-law dependence of the loss on $S_{\min}$ reflects the interplay of optimizer dynamics and the loss landscape. Since the fits are best late in training, when the loss may be approximately quadratic, the power-law should provide information about the spectrum of the Hessian of the loss. Its universality suggests that the Hessian eigenvalue density is roughly independent of model size.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Lower Bound on Early Stopping Step", "weight": 1.0} -->

The results for $L{(N,S_{\min})}$ can be used to derive a lower-bound (and rough estimate) of the step at which early stopping should occur when training is data limited. It is motivated by the idea that finite and infinite $D$ learning curves for a given model will be very similar until we reach $S_{\min} \approx S_{stop}$. Thus overfitting should be proportional to the correction from simply ending training at $S_{stop}$. This will underestimate $S_{stop}$, because in reality the test loss will decrease more slowly when we have a finite $D$, and therefore we will require more training steps to reach the optimal test loss at finite $D$. This line of reasoning leads to the inequality

<!-- chunk {"id": "body-0088", "role": "body", "section": "Lower Bound on Early Stopping Step", "weight": 1.0} -->

where $L{(N,\infty)}$ is the converged loss, evaluated with infinite available data. This inequality and its comparison to the empirical data is displayed in Figure 16 in the appendix. In that figure, the values of $S_{stop}$ and $L{(N,D)}$ are empirical (though $S_{stop}$ is adjusted to mimic training at $B \gg B_{crit}$), while $L{(N,\infty)}$ is computed from the fit to $L{(N,D)}$ evaluated at $D = \infty$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Optimal Allocation of the Compute Budget", "weight": 1.0} -->

We displayed the *empirical* trend of performance as a function of the computation used during training in the top-right of Figure 1. However, this result involved training at a fixed batch size $B$, whereas we know that in fact we could train more efficiently^55^5One might ask why we did not simply train at $B_{crit}$ in the first place. The reason is that it depends not only on the model but also on the target value of the loss we wish to achieve, and so is a moving target. by training at the batch size $B_{crit}$ discussed in Section 5.1 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models"). Large and small values of the loss could have been achieved with fewer samples or fewer steps, respectively, and correcting for this inefficiency by standardizing to the critical batch size results in cleaner and more predictable trends.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Optimal Allocation of the Compute Budget", "weight": 1.0} -->

In this section we will adjust for this oversight. More importantly, we will use the results of Section 5 to determine the optimal *allocation* of compute between model size $N$ and the quantity of data processed during training, namely $2B_{crit}S_{\min}$. We will determine this allocation both empirically and theoretically, by using the equation for $L{(N,S_{\min})}$, and we will demonstrate that these methods agree.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Optimal Performance and Allocations", "weight": 1.0} -->

Let us first study the loss as a function of the optimally allocated compute from Equation (5.5 ‣ 5 Scaling Laws with Model Size and Training Time ‣ Scaling Laws for Neural Language Models")). The result is plotted in Figure 13, along with a power-law fit. We see that as compared to the compute plot of Figure 1, the new fit with $C_{\min}$ is somewhat improved.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Optimal Performance and Allocations", "weight": 1.0} -->

Given $L{(C_{\min})}$, it is natural to ask for the optimal model size $N{(C_{\min})}$ that provides the minimal loss with a given quantity of training compute. The optimal model size is shown in Figure 14. We observe that $N{(C_{\min})}$ can be fit very well with a power-law

<!-- chunk {"id": "body-0093", "role": "body", "section": "Optimal Performance and Allocations", "weight": 1.0} -->

In Figure 12, we show the effect of training models of sub-optimal sizes (see Appendix B.4).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Optimal Performance and Allocations", "weight": 1.0} -->

By definition $C_{\min} \equiv {6NB_{crit}S}$, and so we can use $N{(C_{\min})}$ to extract further results. In particular, since prior fits show $B \propto L^{- 4.8}$ and $L \propto C_{\min}^{- 0.05}$, we can conclude that $B_{crit} \propto C_{\min}^{0.24}$. This leads us to conclude that the optimal number of steps will only grow very slowly with compute, as

<!-- chunk {"id": "body-0095", "role": "body", "section": "Optimal Performance and Allocations", "weight": 1.0} -->

matching the empirical results in Figure 14. In fact the measured exponent is sufficiently small that our results may even be consistent with an exponent of zero.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Optimal Performance and Allocations", "weight": 1.0} -->

Thus we conclude that as we scale up language modeling with an optimal allocation of computation, we should predominantly increase the model size $N$, while simultaneously scaling up the batch size via $B \propto B_{crit}$ with negligible increase in the number of serial steps. Since compute-efficient training uses relatively few optimization steps, additional work on speeding up early training dynamics may be warranted.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Predictions from $L{(N,S_{\\min})}$", "weight": 1.0} -->

The results for $L{(C_{\min})}$ and the allocations can be predicted from the $L{(N,S_{\min})}$ equation obtained in Section 5. Given our equation for $L{(N,S_{\min})}$, we can substitute $S_{\min} = \frac{C_{\min}}{6NB}$ and then find the minimum of the loss as a function of $N$, while fixing the training compute. We carry out this procedure in detail in Appendix B, where we also provide some additional predictions.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Predictions from $L{(N,S_{\\min})}$", "weight": 1.0} -->

For the loss as a function of training compute, we predict that

<!-- chunk {"id": "body-0099", "role": "body", "section": "Predictions from $L{(N,S_{\\min})}$", "weight": 1.0} -->

in excellent agreement with the exponent of Figure 13. We also predict that

<!-- chunk {"id": "body-0100", "role": "body", "section": "Predictions from $L{(N,S_{\\min})}$", "weight": 1.0} -->

which also matches the scaling of Figure 14 to within a few percent. Our scaling laws provide a predictive framework for the performance of language modeling.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

We observe no signs of deviation from straight power-law trends at large values of compute, data, or model size. Our trends must eventually level off, though, since natural language has non-zero entropy.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

Indeed, the trends for compute-efficient training described in this section already contain an apparent contradiction. At scales several orders of magnitude above those documented here, the performance predicted by the $L{(C_{\min})}$ scaling law decreases below what should be possible given the slow growth in training data with compute. This implies that our scaling laws must break down before this point, but we conjecture that the intersection point has a deeper meaning: it provides an estimate of the point at which Transformer language models reach maximal performance.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

Since the amount of data used by compute-efficient training grows slowly with the compute budget, the performance predicted by $L{(C_{\min})}$ eventually hits a lower bound set by the $L{(D)}$ power law (see Figure 15). Let us work this out in more detail.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

To keep overfitting under control, the results of Section 4 imply that we should scale the dataset size as

<!-- chunk {"id": "body-0105", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

where we have used the compute-efficient $N{(C_{\min})}$ from Figure 14.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

Let us compare this to the data requirements of compute-efficient training. If we train at the critical batch size (i.e. $C = {2C_{\min}}$) and never re-use data during training, we find that data usage grows with compute as

<!-- chunk {"id": "body-0107", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

This is the maximum rate at which the dataset size can productively grow with compute, since it means that we are only training for a single epoch. But it grows the dataset much more slowly than in Equation (6.6). It appears to imply that compute-efficient training will eventually run into a problem with overfitting, even if the training process never re-uses any data!

<!-- chunk {"id": "body-0108", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

According to Figure 1, we expect that when we are bottlenecked by the dataset size (ie by overfitting), the loss should scale as ${L{(D)}} \propto D^{- 0.095}$. This implies that the loss would scale with compute as ${L{({D{(C_{\min})}})}} \propto C_{\min}^{- 0.03}$ once we are data-limited. Once again, we have a contradiction, as this will eventually intersect with our prediction for $L{(C_{\min})}$ from Figure 13, where we found a scaling ${L{(C_{\min})}} \propto C_{\min}^{- 0.050}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

though the numerical values are highly uncertain, varying by an order or magnitude in either direction depending on the precise values of the exponents from the power-law fits. The most obvious interpretation is that our scaling laws break down at or before we reach this point, which is still many orders of magnitude away in both compute and model size.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

One might also conjecture that this intersection point has a deeper meaning. If we cannot increase the model size beyond $N^{\ast}$ without qualitatively different data requirements, perhaps this means that once we reach $C_{\min}^{\ast}$ and $N^{\ast}$, we have extracted all of the reliable information available in natural language data. In this interpretation, $L^{\ast}$ would provide a rough estimate for the entropy-per-token^66^6Defining words using the wc utility, the WebText2 dataset has $1.4$ tokens per word and $4.3$ characters per token. of natural language. In this scenario, we would expect the loss trend to level off at or before $L^{\ast}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Contradictions and a Conjecture", "weight": 1.0} -->

We can guess at the functional form of $L{(C_{\min})}$ as it levels off by considering a version of our training dataset with added noise. For example, we could append a random string of tokens to each context shown to the model to artificially boost the loss by a constant additive factor. Then, the distance from the noise floor $L - L_{noise}$ would be a more meaningful performance metric, with even a small decrease in this distance potentially representing a significant boost in qualitative performance. Since the artificial noise would affect all of our trends equally, the critical point of 6.8 would not change (aside from the absolute value of $L^{\ast}$), and may be meaningful even if it occurs after the leveling off.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have observed consistent scalings of language model log-likelihood loss with non-embedding parameter count $N$, dataset size $D$, and optimized training computation $C_{\min}$, as encapsulated in Equations (1.5) and (1.6). Conversely, we find very weak dependence on many architectural and optimization hyperparameters. Since scalings with $N,D,C_{\min}$ are power-laws, there are diminishing returns with increasing scale.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Discussion", "weight": 1.5} -->

We were able to precisely model the dependence of the loss on $N$ and $D$, and alternatively on $N$ and $S$, when these parameters are varied simultaneously. We used these relations to derive the compute scaling, magnitude of overfitting, early stopping step, and data requirements when training large language models. So our scaling relations go beyond mere observation to provide a predictive framework. One might interpret these relations as analogues of the ideal gas law, which relates the macroscopic properties of a gas in a universal way, independent of most of the details of its microscopic consituents.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Discussion", "weight": 1.5} -->

It is natural to conjecture that the scaling relations will apply to other generative modeling tasks with a maximum likelihood loss, and perhaps in other settings as well. To this purpose, it will be interesting to test these relations on other domains, such as images, audio, and video models, and perhaps also for random network distillation. At this point we do not know which of our results depend on the structure of natural language data, and which are universal. It would also be exciting to find a theoretical framework from which the scaling relations can be derived: a 'statistical mechanics' underlying the 'thermodynamics' we have observed. Such a theory might make it possible to derive other more precise predictions, and provide a systematic understanding of the limitations of the scaling laws.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the domain of natural language, it will be important to investigate whether continued improvement on the loss translates into improvement on relevant language tasks. Smooth quantitative change can mask major qualitative improvements: "more is different". For example, the smooth aggregate growth of the economy provides no indication of the specific technological developments that underwrite it. Similarly, the smooth improvements in language model loss may hide seemingly qualitative changes in capability.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our results strongly suggest that larger models will continue to perform better, and will also be much more sample efficient than has been previously appreciated. Big models may be more important than big data. In this context, further investigation into model parallelism is warranted. Deep models can be trained using pipelining \[HCC^+^18\], which splits parameters depth-wise between devices, but eventually requires increased batch sizes as more devices are used. Wide networks on the other hand are more amenable to parallelization \[SCP^+^18\], since large layers can be split between multiple workers with less serial dependency. Sparsity or branching (e.g. ) may allow for even faster training of large networks through increased model parallelism. And using methods like, which grow networks as they train, it might be possible to remain on the compute-efficient frontier for an entire training run.
