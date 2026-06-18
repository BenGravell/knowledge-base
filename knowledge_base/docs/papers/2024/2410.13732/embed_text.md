## INTRODUCTION

Recently, *Large Language Models* (LLMs) have shown impressive performance in producing complex text answers to given questions. Their outstanding feature is the massive size of parameter sets (up to billions). The rapidly growing parameter number has limited the possibility of developing such models (as well as objectively investigating their properties) to companies and institutions capable of making considerable investments in computing the model's parameters.

This is why it is of great interest to attempt to find more efficient configurations with fewer parameters without performance loss. A computing model with an excellent success record is based on the transformer architecture \[[Vaswani et al., 2017](https://arxiv.org/html/2410.13732v2#bib.bibx14)\]. Their success is due to an excellent ability to capture contextual information. Initially developed for language processing, transformers have also been successfully used in Computer Vision (CV). The analogy to language processing is the following: the semantics of individual words are determined by other words in the word sequence. Frequently, the basic units are not words but tokens (e.g., $n$-grams consisting of $n$ consecutive letters). Since the *Vision Transformer* \[[Dosovitskiy et al., 2021](https://arxiv.org/html/2410.13732v2#bib.bibx3)\], in an image, the tokens are represented by *patches* --- typically square regions of pixels in the image. Other patches can influence or disambiguate a patch's conceptual meaning. For example, the environment in which an individual object is embedded in the image may disambiguate the identification of a specific bird or mushroom species.

The fundamental concept of the transformer is that of *attention* \[[Bahdanau et al., 2016](https://arxiv.org/html/2410.13732v2#bib.bibx1)\]. It is based on the insight that a particular token's semantics are influenced by its close relationships with other tokens. The tokens are encoded as real-valued vectors in a high-dimensional space (frequently around $1,000$ dimensions or more). These vectors are called *embeddings*. The algebraic similarity between the embedding vectors measures the semantic proximity between the tokens. This similarity measure is the vector product or the cosine angle between the vectors. The weighting of tokens by such similarity measure is called attention, which, in analogy to human attention, focuses on relevant concepts. From the computational point of view, a transformer is a structure consisting of

an algorithm for consideration of token context, the *attention mechanism*, and

a *Multi-Layer Perceptron* (MLP) for nonlinear transformation of intermediary data.

### Multi-Head Attention

For every transformer in the stack, the following processing is done by the attention mechanism (*multi-head attention* or *MHA*). The input of a training sample in the stack's $s$-th Transformer (out of their total number $S$) is a sequence of input vectors $x_{si}$. This sequence is transformed into an equally long sequence of output embeddings $z_{si}$. Each of them is, for given weights, a formally linear transformation

i.e., a weighted average of input embeddings $x_{si}$, linearly transformed by matrix $W_{s}^{V}W_{s}^{O}$. The weight vectors $a_{si} = \left\lbrack a_{si1},a_{si2},\ldots,a_{sii} \right\rbrack$ are computed as

The vector argument of the $\text{Softmax}{()}$ function measures the similarity between a present token $x_{Q}$, "the query" and another token $x_{K}$, "the key".

This form of attention mechanism is referred to as *single-head*. A popular variant consists of an extension to multiple heads indexed by $h$:

Each head has its separate matrices $W_{h}^{Q}$, $W_{h}^{K}$, $W_{h}^{V}$, and $W_{h}^{O}$. The weights are also computed separately as

### Multi-Layer Perceptron

The second component is a standard MLP with a single hidden layer, applied to each intermediary embedding $z_{si}$:

with $f{()}$ being a nonlinear function, usually the *Gaussian Error Linear Unit (GELU)* \[[Hendrycks and Gimpel, 2023](https://arxiv.org/html/2410.13732v2#bib.bibx6)\], weight matrices $W_{s}^{}$ and $W_{s}^{}$ as well as bias vectors $b_{s}^{}$ and $b_{s}^{}$.

\[[He and Hofmann, 2024](https://arxiv.org/html/2410.13732v2#bib.bibx5)\] have investigated the possibilities of simplifying the transformer architecture. Their focus has been increasing the signal throughput through the network. The proposed changes primarily consist of modifying or omitting shortcut connections and normalizing layers. In addition, they have addressed the possibility of omitting matrices $W^{V}$ and $W^{O}$. The last idea has also been implemented in our modifications proposed in [Section 3](https://arxiv.org/html/2410.13732v2#S3 "3 SINGLE-HEAD CONFIGURATION ‣ Reducing the Transformer Architecture to a Minimum").

Our focus is different: we intend to substantially reduce trainable parameters to accelerate the training and improve convergence.

## TRANSFORMER WITHOUT THE MLP

The MLP requires the majority of the parameters to be fitted. This is justified by the argument that the MLP is the vehicle for implementing nonlinear mappings.

However, it can be argued that the first component, the attention mechanism, can also capture nonlinearities. It is the variable weights that make the mapping nonlinear. The argument of the $\text{Softmax}{()}$ function is already a quadratic function of input tokens, and the function itself is nonlinear. Even if the $\text{Softmax}{()}$ were linear, the multiplication of input tokens by the weights $a_{sij}$ (which are quadratic in these tokens) would result in a cubic function of input tokens. The nonlinearity of $\text{Softmax}{()}$ makes this mapping only more nonlinear.

So, a stack of $S$ transformers is a chain of $S$ at least cubic functions of the input, resulting in a function of polynomial order of at least $3S$. This makes clear that subsequent processing by an MLP is not the only nonlinear element of the processing. The extent of the task's nonlinearity cannot be assessed in advance. Still, the hypothesis that a reduced transformer without an MLP may cover the nonlinearity needs for some tasks is justified and can be validated by appropriate tests.

Without the MLPs, the transformer architecture can be described in more explicit terms. This is particularly the case if a single-head option is pursued.

## SINGLE-HEAD CONFIGURATION

Although the matrices $W_{s}^{Q}$, $W_{s}^{K}$, $W_{s}^{V}$, and $W_{s}^{O}$ can theoretically map the embedding vector to an arbitrary vector width, it is common to keep this width constant throughout the model, referring to the *model width* $N$. Then, in the case of a single head, these matrices are square. With square matrices, it is evident that $W_{s}^{V}W_{s}^{O}$ can be collapsed to a single matrix $W_{s}^{VO}$, and, analogically, $W_{s}^{Q}W_{s}^{KT}$ to $W_{s}^{QK}$. This saves $50\ \%$ of the attention module's parameters, from $4SN^{2}$ to $2SN^{2}$.

Concatenating the transformer-encoder layers without MLP leads to the following recursion:

When stacking the attention modules, the matrices $W_{s}^{VO}$ concatenate to their product over $s = {1,\ldots,S}$. Then, they collapse into a single matrix

Since every sum $\sum_{j = 1}^{i}a_{sij}$ is equal to unity (as a result of the softmax operation), every successive transformer layer performs a weighted mean of stacked inputs $x_{1j}$.

The total number of parameters with $S$ matrices $W_{s}^{QK}$ and a single matrix $W^{VO}$ is ${({S + 1})}N^{2}$, only slightly more than $25\ \%$ of the original size without MLP. So far, all this is possible without losing any expressive power of the single-head transformer without MLP --- only obsolete parameters are deleted.

In many NLP applications, the output of the last transformer of the stack is expected to produce an embedding of a word or a language token. These output embeddings can be expected to come from the space spanned by the input words or tokens. From this viewpoint, it may appear questionable to transform the input embeddings by matrices $W_{s}^{VO}$ and to re-transform them back into the word embeddings. Then, it may be worth attempting to delete the value transformations. This has also been the proposal of \[[He and Hofmann, 2024](https://arxiv.org/html/2410.13732v2#bib.bibx5)\], resulting in a simple weighted mean

The output embedding $z_{Si}$ is a convex combination of input embeddings $x_{1i}$. In other words, it is a member of the convex set spanned by $x_{1i}$.

This concept has been implemented in the Keras framework by setting the matrices $W_{s}^{V}$ and $W_{s}^{O}$ to unit matrices. Collapsing $W_{s}^{Q}W_{s}^{KT}$ to $W_{s}^{QK}$ has been reached by setting the matrix $W^{K}$ to a unit matrix. The newly defined matrix $W_{s}^{QK}$ replaces matrix $W_{s}^{Q}$.

## MULTI-HEAD CONFIGURATION

The relationships of [Section 3](https://arxiv.org/html/2410.13732v2#S3 "3 SINGLE-HEAD CONFIGURATION ‣ Reducing the Transformer Architecture to a Minimum") are valid wherever the matrices $W_{sh}^{V}$, $W_{sh}^{O}$, $W_{sh}^{Q}$, and $W_{sh}^{K}$ are square. This may also apply to multiple heads. However, it is usual to commit to a reduced dimension per head. With $H > 1$ heads, it is common to map the embedding vector to a narrower vector of width $N/H$, assumed to be integer.

In such cases, the matrices $W_{sh}^{V}$, $W_{sh}^{O}$, $W_{sh}^{Q}$, and $W_{sh}^{K}$ are not square but of dimension $\left( N,{N/H} \right)$. Collapsing $W_{sh}^{Q}W_{sh}^{KT}$ to $W_{sh}^{QK}$ is then no longer efficient since $W_{sh}^{QK}$ is of dimension $(N,N)$ and has thus $N^{2}$ parameters while $W_{sh}^{Q}$ and $W_{sh}^{K}$ together have ${2N^{2}}/H$, which is a smaller or equal number for $H > 1$.

Moreover, it is impossible to equivalently concatenate the value/projection matrices $W_{sh}^{VO}$ to a unique product because of varying index $h$ along various paths through the heads.

Nevertheless, omitting the $W_{sh}^{VO}$ at all would have the same justification as for single-head configuration: the output embedding $z_{Si}$ would become a convex combination of input embeddings $x_{1i}$, which can be expected to correspond to a meaningful word or token.

## SYMMETRY OF SIMILARITY

The expression [Eq. 3](https://arxiv.org/html/2410.13732v2#S1.E3 "In Multi-Head Attention ‣ 1 INTRODUCTION ‣ Reducing the Transformer Architecture to a Minimum") measures the similarity between queries and keys. The general concept of characterizing similarity between vectors by their product is symmetric: $a$ is equally similar to $b$ as is $b$ to $a$.

However, the similarity between a key and a query evaluated with the help of $x_{si}W_{sh}^{Q}W_{sh}^{KT}x_{sj}^{T}$ is asymmetric. This is because the matrices $W_{sh}^{Q}$ and $W_{sh}^{K}$ are potentially different.

This asymmetry leads to different similarities between $x_{si}$ and $x_{sj}$ in the roles of key and query: $x_{si}$ is not as similar to $x_{sj}$ as is $x_{sj}$ to $x_{si}$. The vector $x_{si}$ is also not the most similar to itself. The matrix product $W_{sh}^{Q}W_{sh}^{KT}$ is generally not positive definite, so it is not even guaranteed that the similarity of $x_{si}$ to itself is positive.

The asymmetry can be deliberate and justified from some viewpoints. It is not a matter of course that the roles of queries and keys are symmetric. However, some of the mentioned properties can make its use harmful.

The symmetry can be guaranteed by simply setting $W_{sh}^{Q} = W_{sh}^{K}$. Then, half of the parameters dedicated to the query and key matrices can be economized. In the single-head case, the same effect is reached by a symmetric matrix $W_{s}^{QK}$, with identical parameters mirrored over the diagonal, i.e., $w_{sij}^{QK} = w_{sji}^{QK}$. Another possibility is to parameterize a lower triangular matrix $T_{s}^{QK}$ and to multiply it by its transpose, getting

This amounts to the well-known *Cholesky decomposition* \[[Cholesky, 1924](https://arxiv.org/html/2410.13732v2#bib.bibx2)\] of a symmetric matrix.

With both methods, the number of parameters is $\frac{N{({N + 1})}}{2}$ instead of $N^{2}$, or even $2N^{2}$ of the original version without collapsing $W^{Q}$ and $W^{K}$.

The symmetry is implemented by reusing $W_{sh}^{Q}$ as $W_{sh}^{K}$, omitting the use of $W_{sh}^{K}$ at all.

## SETUP OF COMPUTING EXPERIMENTS

The benchmarks for the evaluation have been chosen from the CV domain. They are medium-sized problems that can be run for a sufficient number of experiments. This would not be possible with large models such as those used in language processing.

For the experiments, two well-known image classification datasets MNIST \[[LeCun et al., 1998](https://arxiv.org/html/2410.13732v2#bib.bibx10)\] and CIFAR-10 \[[Krizhevsky, 2009](https://arxiv.org/html/2410.13732v2#bib.bibx9)\] were used. MNIST contains grayscale images of handwritten digits (0--9) while CIFAR-10 contains color images of exclusively ten different mundane objects like "horse", "ship", or "dog". They contain $60,000$ (MNIST) and $50,000$ (CIFAR-10) training examples. Their respective preconfigured test split of each $10,000$ examples are used as validation sets. While CIFAR-10 is evenly distributed among all classes, MNIST can be considered almost equally distributed.

An important criterion is that the training set size is sufficient for good generalization. The training size (as related to the number of model parameters) must be large enough for the model not to be underdetermined so that we can fairly assess the models' performances. As a criterion for this, the overdetermination ratio of each benchmark candidate has been evaluated \[[Hrycej et al., 2023](https://arxiv.org/html/2410.13732v2#bib.bibx8)\]:

with $K$ being the number of training examples, $M$ being the output vector length (usually equal to the number of classes), and $P$ being the number of trainable model parameters.

This formula justifies itself by ensuring that the numerator $KM$ equals the number of constraints to be satisfied (the reference values for all training examples). This number must be larger than the number of trainable parameters for the system to be sufficiently determined. (Otherwise, there is an infinite number of solutions, most of which do not generalize.) This is equivalent to the requirement for the overdetermination ratio $Q$ to be larger than unity.

#Encs-#Heads

Table 1: Results of 16 experiments on the two datasets MNIST and CIFAR-10 with 6 or 12 consecutive transformer encoders and 1 or 4 attention heads per encoder layer either with the default MLP inside each encoder layer or skipping it entirely. The loss and accuracy for the training and validation sets are reported after each model is trained for exactly 500 epochs.

The losses and accuracies in [Table 1](https://arxiv.org/html/2410.13732v2#S6.T1 "In 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum") show that the performance with 12 encoders is not superior to that with 6 encoders. The parameter set sizes with 12 encoders have been $563,242$ with MLP and $198,100$ without MLP. This is substantially more than $287,686$ and $101,470$, respectively, with 6 encoders. Consequently, the latter variant has been adopted as a baseline.

### RESULTS FOR MNIST

Following the arguments of [Sections 2](https://arxiv.org/html/2410.13732v2#S2 "2 TRANSFORMER WITHOUT THE MLP ‣ Reducing the Transformer Architecture to a Minimum"), (https://arxiv.org/html/2410.13732v2#S3 "3 SINGLE-HEAD CONFIGURATION ‣ Reducing the Transformer Architecture to a Minimum"), (https://arxiv.org/html/2410.13732v2#S4 "4 MULTI-HEAD CONFIGURATION ‣ Reducing the Transformer Architecture to a Minimum") and (https://arxiv.org/html/2410.13732v2#S5 "5 SYMMETRY OF SIMILARITY ‣ Reducing the Transformer Architecture to a Minimum"), the following reduced transformer variants have been tested:

with and without an MLP in each transformer-encoder,

with 1 and 4 heads,

with the original matrix configuration as well matrix pair $W^{Q}$ and $W^{K}$ collapsed into one matrix, $W^{V}$ and $W^{O}$ omitted (one head variants only), and

with asymmetric and symmetric similarity measures.

## Heads
## Parameters

Table 2: Loss and accuracy for different variants of transformer-encoder modifications on MNIST: 1 or 4 heads, with or without the MLP, with a single Wqk matrix, no value and projection matrices, or a symmetric similarity measurement.

Figure 1: Training and validation losses attained by various reduced transformer-encoders with six encoder layers on MNIST.

The variants depicted refer to the matrix options:

unchanged corresponds to the original attention module matrix variety;

Wqk variants use a single matrix for the product $W^{Q}W^{KT}$; these variants are only available for a single attention head, and their similarity measure is asymmetric as in the original version;

noWv.Vo denotes omitting the value matrices $W^{V}$ as well as the projection matrices $W^{O}$; also, these variants imply a single attention head and asymmetric similarity measurement;

symmetric variants are committed to symmetric similarity measures; $W^{V}$ and $W^{O}$ are left untouched.

The performances of the individual variants are given in [Table 2](https://arxiv.org/html/2410.13732v2#S6.T2 "In 6.1 RESULTS FOR MNIST ‣ 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum"). For better comparability, the losses are additionally depicted in [Fig. 1](https://arxiv.org/html/2410.13732v2#S6.F1 "In 6.1 RESULTS FOR MNIST ‣ 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum").

The following observations can be made:

The original variants with MLPs perform better than those without MLPs on the training set.

By contrast, their advance disappears on the validation set, particularly if the symmetric similarity metrics are used.

The variant with asymmetric similarity without MLP is inferior to the analogical one with symmetric similarity.

The minimum variant with query and key matrices $W^{Q},W^{K}$ collapsed to $W^{QK} = {W^{Q}W^{KT}}$ and additionally omitted value and projection matrices show a higher loss than other variants. This may be due to its dramatically reduced parameter number, which may lead to an insufficient capacity to capture nonlinearities.

As MNIST is a relatively easy benchmark, the accuracy results are very close to each other. The parameter numbers are substantially different. The symmetric variant without MLP has only about $25\ \%$ of the parameter number of the original, full variant with MLP. The variant with collapsed matrices has about $33\ \%$ of the original parameters. The parameters include, in addition to the attention modules of all transformer-encoders, the embedding matrix reducing the image patch to the embedding vector.

The number of parameters has a strong effect on the generalization capability of the model. This can be quantified with the help of the overdetermination ratio from [Eq. 12](https://arxiv.org/html/2410.13732v2#S6.E12 "In 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum") in column $Q$ of [Table 2](https://arxiv.org/html/2410.13732v2#S6.T2 "In 6.1 RESULTS FOR MNIST ‣ 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum"). The loss gap between the training and validation sets is the largest for the original version with $Q$ close to unity while it shrinks towards the symmetric version without MLPs.

### RESULTS FOR CIFAR-10

The variants tested are analogical to those for MNIST. The losses and accuracies attained after $500$ epochs are given in [Table 3](https://arxiv.org/html/2410.13732v2#S6.T3 "In 6.2 RESULTS FOR CIFAR-10 ‣ 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum"), the losses additionally in [Fig. 2](https://arxiv.org/html/2410.13732v2#S6.F2 "In 6.2 RESULTS FOR CIFAR-10 ‣ 6 SETUP OF COMPUTING EXPERIMENTS ‣ Reducing the Transformer Architecture to a Minimum").

## Heads
## Parameters

Table 3: Loss and accuracy for different variants of transformer-encoder modifications on CIFAR-10: 1 or 4 heads, with or without MLP, with a single Wqk matrix, no value and projection matrices, or a symmetric similarity measurement.

Figure 2: Training and validation losses attained by various reduced transformer-encoders with six encoder layers on CIFAR-10.

The result characteristics are similar to those for MNIST but more distinct:

The original variant with MLP reaches the best training set loss but the worst validation set loss.

Compared to the original variant, the reduced variants without MLP and with symmetric similarity are superior in generalization.

This also applies to the variant with collapsed key and query matrices.

Even the minimum variant with all considered matrix reductions (except for symmetry), whose parameter count is only a tenth of the original version with MLP, shows a better validation set performance than the original variant with all matrices and MLP.

The measured accuracies are roughly consistent with the losses on the training set. On the validation set, some of them follow, paradoxically, a different ranking. However, the fact that the loss, not the accuracy, is explicitly trained justifies the arguments via loss rather than accuracy.

### TRIALS WITH IMAGENET

Several trials on the ImageNet dataset \[[Russakovsky et al., 2015](https://arxiv.org/html/2410.13732v2#bib.bibx12)\] have been conducted to support the hypotheses with a larger benchmark. Unfortunately, the baseline run with the original transformer architecture, including MLP, has not been successful. In all trials, *Adam* failed to find a substantial improvement in the initial parameter state. By contrast, without MLP, it has been converging at least to a state with a moderate classification performance. This is why we cannot present a serious study on ImageNet. It can only be concluded that discarding MLP is helpful for convergence. The proof that this variant's performance is acceptable is still pending, and further work will be required to provide it.

## CONCLUSIONS AND LIMITATIONS

The experiments presented have shown limited utility of some parameter-extensive components of the transformer architecture. In particular, the following findings can be formulated:

The MLP component is frequently presented as necessary for capturing nonlinearities in the modeled relationship. However, the inherent nonlinearity of the similarity measures seems powerful enough in many practical cases.

While the classification performance without the MLPs is not significantly inferior to that with MLPs, a substantial benefit is saving the parameters. With model size $N$, the attention mechanism requires $4N^{2}$ parameters in the form of matrices $W^{Q}$, $W^{K}W^{V}$, and $W^{O}$. The size of the MLP is usually chosen as an integer multiple of $h$ of the model size. Then, the MLP consists of weights and biases of two layers, with a total of ${{hN{({N + 1})}} + {N{({{hN} + 1})}}} = {{2hN^{2}} + {hN} + N} \approx {2hN^{2}}$. If the multiple is $h = 4$, MLP has double the number of parameters as the attention mechanism. Consequently, omitting MLP reduces the parameters to $33\ \%$ of the original size.

Symmetric similarity measures tend to perform better than asymmetric ones, with $50\ \%$ fewer query and key matrix parameters. This improvement may be reached by excluding undesirable freedoms, such as a token being dissimilar to itself. The parameter reduction can be expected to constrain the search for the optimum fit fruitfully.

Collapsing the value and the key matrix into one is another possibility of reducing the parameter set of these matrices by $50\ \%$.

Omitting the value matrix $W^{V}$ and the projection matrix $W^{O}$ reduces the parameters of the whole attention module by $50\ \%$. This variant has also been proposed by \[[He and Hofmann, 2024](https://arxiv.org/html/2410.13732v2#bib.bibx5)\], with the observation of no significant performance loss in NLP benchmarks.

Both preceding reductions amount to a reduction to $25\ \%$ of the original attention module size.

In our experiments, the variants with the collapsed query/key matrices, omitted value, and projection matrices are slightly inferior for MNIST but equal for CIFAR-10. These minimum variants have less than $10\ \%$ of parameters compared with the classical transformers, including MLP. Compared to the architecture with 12 encoders, it is as little as $5\ \%$.

The savings in computing time have been proportional to the savings in parameter numbers.

Our research has been limited to image processing benchmarks MNIST, CIFAR-10, and ImageNet. The experiments with the last benchmark have partially failed due to computing problems. Empirical evidence with the help of two medium-sized benchmarks and an incomplete test of a larger one is not satisfactory. This requests further research with more robust algorithms. There is considerable potential for second-order optimization methods such as the conjugate gradient algorithm of \[[Fletcher and Reeves, 1964](https://arxiv.org/html/2410.13732v2#bib.bibx4)\], thoroughly described in \[[Press et al., 1992](https://arxiv.org/html/2410.13732v2#bib.bibx11)\]. This algorithm's convergence is excellent, but implementing the stopping rule in widespread packages seems to improve its ability to prevent early stops before reaching the minimum region.

Limitations to image processing suggest further extension. The proper domain of transformers is NLP. An obstacle to its investigation is the size of benchmark problems, so most published investigations consist of observing the performance of fine-tuning pre-trained models. To use pre-trained parameter sets, these fine-tuned models must be identical or almost identical to the pre-trained models. This makes the testing of different architectures difficult. A possibility is to use a large model used for pre-training as a *teacher* and a medium-sized model as *student*, mimicking its performance. This procedure, referred to as *knowledge distillation*, has been proposed by \[[Hinton et al., 2015](https://arxiv.org/html/2410.13732v2#bib.bibx7)\] and used, e.g., by \[[Sun et al., 2019](https://arxiv.org/html/2410.13732v2#bib.bibx13)\].

These will be important focuses soon.
