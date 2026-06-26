<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reducing the Transformer Architecture to a Minimum

Topics include Neural networks, Transformers, Attention mechanisms, Computer vision, Classification, Benchmarks, Online algorithms, Natural language processing, NLP, CV, Multi-layer perceptron, MLP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Transformers are a widespread and successful model architecture, particularly in Natural Language Processing (NLP) and Computer Vision (CV). The essential innovation of this architecture is the Attention Mechanism, which solves the problem of extracting relevant context information from long sequences in NLP and realistic scenes in CV. A classical neural network component, a Multi-Layer Perceptron (MLP), complements the attention mechanism. Its necessity is frequently justified by its capability of modeling nonlinear relationships. However, the attention mechanism itself is nonlinear through its internal use of similarity measures. A possible hypothesis is that this nonlinearity is sufficient for modeling typical application problems. As the MLPs usually contain the most trainable parameters of the whole model, their omission would substantially reduce the parameter set size. Further components can also be reorganized to reduce the number of parameters. Under some conditions, query and key matrices can be collapsed into a single matrix of the same size. The same is true about value and projection matrices, which can also be omitted without eliminating the substance of the attention mechanism. Initially, the similarity measure was defined asymmetrically, with peculiar properties such as that a token is possibly dissimilar to itself. A possible symmetric definition requires only half of the parameters.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We have laid the groundwork by testing widespread CV benchmarks: MNIST and CIFAR-10. The tests have shown that simplified transformer architectures (a) without MLP, (b) with collapsed matrices, and (c) symmetric similarity matrices exhibit similar performance as the original architecture, saving up to 90% of parameters without hurting the classification performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Recently, *Large Language Models* (LLMs) have shown impressive performance in producing complex text answers to given questions. Their outstanding feature is the massive size of parameter sets (up to billions). The rapidly growing parameter number has limited the possibility of developing such models (as well as objectively investigating their properties) to companies and institutions capable of making considerable investments in computing the model's parameters.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This is why it is of great interest to attempt to find more efficient configurations with fewer parameters without performance loss. A computing model with an excellent success record is based on the transformer architecture \[Vaswani et al., 2017\]. Their success is due to an excellent ability to capture contextual information. Initially developed for language processing, transformers have also been successfully used in Computer Vision (CV). The analogy to language processing is the following: the semantics of individual words are determined by other words in the word sequence. Frequently, the basic units are not words but tokens (e.g., $n$-grams consisting of $n$ consecutive letters). Since the *Vision Transformer* \[Dosovitskiy et al., 2021\], in an image, the tokens are represented by *patches* --- typically square regions of pixels in the image. Other patches can influence or disambiguate a patch's conceptual meaning. For example, the environment in which an individual object is embedded in the image may disambiguate the identification of a specific bird or mushroom species.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The fundamental concept of the transformer is that of *attention* \[Bahdanau et al., 2016\]. It is based on the insight that a particular token's semantics are influenced by its close relationships with other tokens. The tokens are encoded as real-valued vectors in a high-dimensional space (frequently around $1,000$ dimensions or more). These vectors are called *embeddings*. The algebraic similarity between the embedding vectors measures the semantic proximity between the tokens. This similarity measure is the vector product or the cosine angle between the vectors. The weighting of tokens by such similarity measure is called attention, which, in analogy to human attention, focuses on relevant concepts. From the computational point of view, a transformer is a structure consisting of an algorithm for consideration of token context, the *attention mechanism*, and a *Multi-Layer Perceptron* (MLP) for nonlinear transformation of intermediary data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Multi-Head Attention", "weight": 1.0} -->

For every transformer in the stack, the following processing is done by the attention mechanism (*multi-head attention* or *MHA*). The input of a training sample in the stack's $s$-th Transformer (out of their total number $S$) is a sequence of input vectors $x_{si}$. This sequence is transformed into an equally long sequence of output embeddings $z_{si}$. Each of them is, for given weights, a formally linear transformation i.e., a weighted average of input embeddings $x_{si}$, linearly transformed by matrix $W_{s}^{V}W_{s}^{O}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Multi-Head Attention", "weight": 1.0} -->

The weight vectors $a_{si} = \left\lbrack a_{si1},a_{si2},\ldots,a_{sii} \right\rbrack$ are computed as The vector argument of the $\text{Softmax}{}$ function measures the similarity between a present token $x_{Q}$, "the query" and another token $x_{K}$, "the key".

<!-- chunk {"id": "body-0009", "role": "body", "section": "Multi-Head Attention", "weight": 1.0} -->

This form of attention mechanism is referred to as *single-head*. A popular variant consists of an extension to multiple heads indexed by $h$: Each head has its separate matrices $W_{h}^{Q}$, $W_{h}^{K}$, $W_{h}^{V}$, and $W_{h}^{O}$. The weights are also computed separately as

<!-- chunk {"id": "body-0010", "role": "body", "section": "Multi-Layer Perceptron", "weight": 1.0} -->

The second component is a standard MLP with a single hidden layer, applied to each intermediary embedding $z_{si}$: with $f{}$ being a nonlinear function, usually the *Gaussian Error Linear Unit (GELU)* \[Hendrycks and Gimpel, 2023\], weight matrices $W_{s}^{}$ and $W_{s}^{}$ as well as bias vectors $b_{s}^{}$ and $b_{s}^{}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Multi-Layer Perceptron", "weight": 1.0} -->

\[He and Hofmann, 2024\] have investigated the possibilities of simplifying the transformer architecture. Their focus has been increasing the signal throughput through the network. The proposed changes primarily consist of modifying or omitting shortcut connections and normalizing layers. In addition, they have addressed the possibility of omitting matrices $W^{V}$ and $W^{O}$. The last idea has also been implemented in our modifications proposed in Section 3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Multi-Layer Perceptron", "weight": 1.0} -->

Our focus is different: we intend to substantially reduce trainable parameters to accelerate the training and improve convergence.

<!-- chunk {"id": "body-0013", "role": "body", "section": "TRANSFORMER WITHOUT THE MLP", "weight": 1.0} -->

The MLP requires the majority of the parameters to be fitted. This is justified by the argument that the MLP is the vehicle for implementing nonlinear mappings.

<!-- chunk {"id": "body-0014", "role": "body", "section": "TRANSFORMER WITHOUT THE MLP", "weight": 1.0} -->

However, it can be argued that the first component, the attention mechanism, can also capture nonlinearities. It is the variable weights that make the mapping nonlinear. The argument of the $\text{Softmax}{}$ function is already a quadratic function of input tokens, and the function itself is nonlinear. Even if the $\text{Softmax}{}$ were linear, the multiplication of input tokens by the weights $a_{sij}$ (which are quadratic in these tokens) would result in a cubic function of input tokens. The nonlinearity of $\text{Softmax}{}$ makes this mapping only more nonlinear.

<!-- chunk {"id": "body-0015", "role": "body", "section": "TRANSFORMER WITHOUT THE MLP", "weight": 1.0} -->

So, a stack of $S$ transformers is a chain of $S$ at least cubic functions of the input, resulting in a function of polynomial order of at least $3S$. This makes clear that subsequent processing by an MLP is not the only nonlinear element of the processing. The extent of the task's nonlinearity cannot be assessed in advance. Still, the hypothesis that a reduced transformer without an MLP may cover the nonlinearity needs for some tasks is justified and can be validated by appropriate tests.

<!-- chunk {"id": "body-0016", "role": "body", "section": "TRANSFORMER WITHOUT THE MLP", "weight": 1.0} -->

Without the MLPs, the transformer architecture can be described in more explicit terms. This is particularly the case if a single-head option is pursued.

<!-- chunk {"id": "body-0017", "role": "body", "section": "SINGLE-HEAD CONFIGURATION", "weight": 1.0} -->

Although the matrices $W_{s}^{Q}$, $W_{s}^{K}$, $W_{s}^{V}$, and $W_{s}^{O}$ can theoretically map the embedding vector to an arbitrary vector width, it is common to keep this width constant throughout the model, referring to the *model width* $N$. Then, in the case of a single head, these matrices are square. With square matrices, it is evident that $W_{s}^{V}W_{s}^{O}$ can be collapsed to a single matrix $W_{s}^{VO}$, and, analogically, $W_{s}^{Q}W_{s}^{KT}$ to $W_{s}^{QK}$. This saves $50\ \%$ of the attention module's parameters, from $4SN^{2}$ to $2SN^{2}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SINGLE-HEAD CONFIGURATION", "weight": 1.0} -->

Concatenating the transformer-encoder layers without MLP leads to the following recursion: When stacking the attention modules, the matrices $W_{s}^{VO}$ concatenate to their product over $s = {1,\ldots,S}$. Then, they collapse into a single matrix Since every sum $\sum_{j = 1}^{i}a_{sij}$ is equal to unity (as a result of the softmax operation), every successive transformer layer performs a weighted mean of stacked inputs $x_{1j}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SINGLE-HEAD CONFIGURATION", "weight": 1.0} -->

The total number of parameters with $S$ matrices $W_{s}^{QK}$ and a single matrix $W^{VO}$ is ${({S + 1})}N^{2}$, only slightly more than $25\ \%$ of the original size without MLP. So far, all this is possible without losing any expressive power of the single-head transformer without MLP --- only obsolete parameters are deleted.

<!-- chunk {"id": "body-0020", "role": "body", "section": "SINGLE-HEAD CONFIGURATION", "weight": 1.0} -->

In many NLP applications, the output of the last transformer of the stack is expected to produce an embedding of a word or a language token. These output embeddings can be expected to come from the space spanned by the input words or tokens. From this viewpoint, it may appear questionable to transform the input embeddings by matrices $W_{s}^{VO}$ and to re-transform them back into the word embeddings. Then, it may be worth attempting to delete the value transformations. This has also been the proposal of \[He and Hofmann, 2024\], resulting in a simple weighted mean The output embedding $z_{Si}$ is a convex combination of input embeddings $x_{1i}$. In other words, it is a member of the convex set spanned by $x_{1i}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "SINGLE-HEAD CONFIGURATION", "weight": 1.0} -->

This concept has been implemented in the Keras framework by setting the matrices $W_{s}^{V}$ and $W_{s}^{O}$ to unit matrices. Collapsing $W_{s}^{Q}W_{s}^{KT}$ to $W_{s}^{QK}$ has been reached by setting the matrix $W^{K}$ to a unit matrix. The newly defined matrix $W_{s}^{QK}$ replaces matrix $W_{s}^{Q}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "MULTI-HEAD CONFIGURATION", "weight": 1.0} -->

The relationships of Section 3 are valid wherever the matrices $W_{sh}^{V}$, $W_{sh}^{O}$, $W_{sh}^{Q}$, and $W_{sh}^{K}$ are square. This may also apply to multiple heads. However, it is usual to commit to a reduced dimension per head. With $H > 1$ heads, it is common to map the embedding vector to a narrower vector of width $N/H$, assumed to be integer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "MULTI-HEAD CONFIGURATION", "weight": 1.0} -->

Moreover, it is impossible to equivalently concatenate the value/projection matrices $W_{sh}^{VO}$ to a unique product because of varying index $h$ along various paths through the heads.

<!-- chunk {"id": "body-0024", "role": "body", "section": "MULTI-HEAD CONFIGURATION", "weight": 1.0} -->

Nevertheless, omitting the $W_{sh}^{VO}$ at all would have the same justification as for single-head configuration: the output embedding $z_{Si}$ would become a convex combination of input embeddings $x_{1i}$, which can be expected to correspond to a meaningful word or token.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SYMMETRY OF SIMILARITY", "weight": 1.0} -->

The expression Eq. 3 measures the similarity between queries and keys. The general concept of characterizing similarity between vectors by their product is symmetric: $a$ is equally similar to $b$ as is $b$ to $a$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SYMMETRY OF SIMILARITY", "weight": 1.0} -->

However, the similarity between a key and a query evaluated with the help of $x_{si}W_{sh}^{Q}W_{sh}^{KT}x_{sj}^{T}$ is asymmetric. This is because the matrices $W_{sh}^{Q}$ and $W_{sh}^{K}$ are potentially different.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SYMMETRY OF SIMILARITY", "weight": 1.0} -->

This asymmetry leads to different similarities between $x_{si}$ and $x_{sj}$ in the roles of key and query: $x_{si}$ is not as similar to $x_{sj}$ as is $x_{sj}$ to $x_{si}$. The vector $x_{si}$ is also not the most similar to itself. The matrix product $W_{sh}^{Q}W_{sh}^{KT}$ is generally not positive definite, so it is not even guaranteed that the similarity of $x_{si}$ to itself is positive.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SYMMETRY OF SIMILARITY", "weight": 1.0} -->

The asymmetry can be deliberate and justified from some viewpoints. It is not a matter of course that the roles of queries and keys are symmetric. However, some of the mentioned properties can make its use harmful.

<!-- chunk {"id": "body-0029", "role": "body", "section": "SYMMETRY OF SIMILARITY", "weight": 1.0} -->

The symmetry can be guaranteed by simply setting $W_{sh}^{Q} = W_{sh}^{K}$. Then, half of the parameters dedicated to the query and key matrices can be economized. In the single-head case, the same effect is reached by a symmetric matrix $W_{s}^{QK}$, with identical parameters mirrored over the diagonal, i.e., $w_{sij}^{QK} = w_{sji}^{QK}$. Another possibility is to parameterize a lower triangular matrix $T_{s}^{QK}$ and to multiply it by its transpose, getting This amounts to the well-known *Cholesky decomposition* \[Cholesky, 1924\] of a symmetric matrix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "SYMMETRY OF SIMILARITY", "weight": 1.0} -->

With both methods, the number of parameters is $\frac{N{({N + 1})}}{2}$ instead of $N^{2}$, or even $2N^{2}$ of the original version without collapsing $W^{Q}$ and $W^{K}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "SETUP OF COMPUTING EXPERIMENTS", "weight": 1.0} -->

The benchmarks for the evaluation have been chosen from the CV domain. They are medium-sized problems that can be run for a sufficient number of experiments. This would not be possible with large models such as those used in language processing.

<!-- chunk {"id": "body-0032", "role": "body", "section": "SETUP OF COMPUTING EXPERIMENTS", "weight": 1.0} -->

For the experiments, two well-known image classification datasets MNIST \[LeCun et al., 1998\] and CIFAR-10 \[Krizhevsky, 2009\] were used. MNIST contains grayscale images of handwritten digits (0--9) while CIFAR-10 contains color images of exclusively ten different mundane objects like "horse", "ship", or "dog". They contain $60,000$ (MNIST) and $50,000$ (CIFAR-10) training examples. Their respective preconfigured test split of each $10,000$ examples are used as validation sets. While CIFAR-10 is evenly distributed among all classes, MNIST can be considered almost equally distributed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "SETUP OF COMPUTING EXPERIMENTS", "weight": 1.0} -->

An important criterion is that the training set size is sufficient for good generalization. The training size (as related to the number of model parameters) must be large enough for the model not to be underdetermined so that we can fairly assess the models' performances. As a criterion for this, the overdetermination ratio of each benchmark candidate has been evaluated \[Hrycej et al., 2023\]: with $K$ being the number of training examples, $M$ being the output vector length (usually equal to the number of classes), and $P$ being the number of trainable model parameters.

<!-- chunk {"id": "body-0034", "role": "body", "section": "SETUP OF COMPUTING EXPERIMENTS", "weight": 1.0} -->

This formula justifies itself by ensuring that the numerator $KM$ equals the number of constraints to be satisfied (the reference values for all training examples). This number must be larger than the number of trainable parameters for the system to be sufficiently determined. (Otherwise, there is an infinite number of solutions, most of which do not generalize.) This is equivalent to the requirement for the overdetermination ratio $Q$ to be larger than unity.

<!-- chunk {"id": "body-0035", "role": "body", "section": "SETUP OF COMPUTING EXPERIMENTS", "weight": 1.0} -->

#Encs-#Heads

<!-- chunk {"id": "body-0036", "role": "body", "section": "SETUP OF COMPUTING EXPERIMENTS", "weight": 1.0} -->

The losses and accuracies in Table 1 show that the performance with 12 encoders is not superior to that with 6 encoders. The parameter set sizes with 12 encoders have been $563,242$ with MLP and $198,100$ without MLP. This is substantially more than $287,686$ and $101,470$, respectively, with 6 encoders. Consequently, the latter variant has been adopted as a baseline.

<!-- chunk {"id": "body-0037", "role": "body", "section": "RESULTS FOR MNIST", "weight": 1.0} -->

Following the arguments of Sections 2, 3, 4 and 5, the following reduced transformer variants have been tested: with and without an MLP in each transformer-encoder, with 1 and 4 heads, with the original matrix configuration as well matrix pair $W^{Q}$ and $W^{K}$ collapsed into one matrix, $W^{V}$ and $W^{O}$ omitted (one head variants only), and with asymmetric and symmetric similarity measures.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Parameters", "weight": 1.0} -->

The variants depicted refer to the matrix options: unchanged corresponds to the original attention module matrix variety; Wqk variants use a single matrix for the product $W^{Q}W^{KT}$; these variants are only available for a single attention head, and their similarity measure is asymmetric as in the original version; noWv.Vo denotes omitting the value matrices $W^{V}$ as well as the projection matrices $W^{O}$; also, these variants imply a single attention head and asymmetric similarity measurement; symmetric variants are committed to symmetric similarity measures; $W^{V}$ and $W^{O}$ are left untouched.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Parameters", "weight": 1.0} -->

The performances of the individual variants are given in Table 2. For better comparability, the losses are additionally depicted in Fig. 1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Parameters", "weight": 1.0} -->

The following observations can be made: The original variants with MLPs perform better than those without MLPs on the training set.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Parameters", "weight": 1.0} -->

By contrast, their advance disappears on the validation set, particularly if the symmetric similarity metrics are used.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parameters", "weight": 1.0} -->

The variant with asymmetric similarity without MLP is inferior to the analogical one with symmetric similarity.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parameters", "weight": 1.0} -->

The minimum variant with query and key matrices $W^{Q},W^{K}$ collapsed to $W^{QK} = {W^{Q}W^{KT}}$ and additionally omitted value and projection matrices show a higher loss than other variants. This may be due to its dramatically reduced parameter number, which may lead to an insufficient capacity to capture nonlinearities.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Parameters", "weight": 1.0} -->

As MNIST is a relatively easy benchmark, the accuracy results are very close to each other. The parameter numbers are substantially different. The symmetric variant without MLP has only about $25\ \%$ of the parameter number of the original, full variant with MLP. The variant with collapsed matrices has about $33\ \%$ of the original parameters. The parameters include, in addition to the attention modules of all transformer-encoders, the embedding matrix reducing the image patch to the embedding vector.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Parameters", "weight": 1.0} -->

The number of parameters has a strong effect on the generalization capability of the model. This can be quantified with the help of the overdetermination ratio from Eq. 12 in column $Q$ of Table 2. The loss gap between the training and validation sets is the largest for the original version with $Q$ close to unity while it shrinks towards the symmetric version without MLPs.

<!-- chunk {"id": "body-0046", "role": "body", "section": "RESULTS FOR CIFAR-10", "weight": 1.0} -->

The variants tested are analogical to those for MNIST. The losses and accuracies attained after $500$ epochs are given in Table 3, the losses additionally in Fig. 2.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Parameters", "weight": 1.0} -->

The result characteristics are similar to those for MNIST but more distinct: The original variant with MLP reaches the best training set loss but the worst validation set loss.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Parameters", "weight": 1.0} -->

Compared to the original variant, the reduced variants without MLP and with symmetric similarity are superior in generalization.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Parameters", "weight": 1.0} -->

This also applies to the variant with collapsed key and query matrices.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Parameters", "weight": 1.0} -->

Even the minimum variant with all considered matrix reductions (except for symmetry), whose parameter count is only a tenth of the original version with MLP, shows a better validation set performance than the original variant with all matrices and MLP.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Parameters", "weight": 1.0} -->

The measured accuracies are roughly consistent with the losses on the training set. On the validation set, some of them follow, paradoxically, a different ranking. However, the fact that the loss, not the accuracy, is explicitly trained justifies the arguments via loss rather than accuracy.

<!-- chunk {"id": "body-0052", "role": "body", "section": "TRIALS WITH IMAGENET", "weight": 1.0} -->

Several trials on the ImageNet dataset \[Russakovsky et al., 2015\] have been conducted to support the hypotheses with a larger benchmark. Unfortunately, the baseline run with the original transformer architecture, including MLP, has not been successful. In all trials, *Adam* failed to find a substantial improvement in the initial parameter state. By contrast, without MLP, it has been converging at least to a state with a moderate classification performance. This is why we cannot present a serious study on ImageNet. It can only be concluded that discarding MLP is helpful for convergence. The proof that this variant's performance is acceptable is still pending, and further work will be required to provide it.

<!-- chunk {"id": "body-0053", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

The experiments presented have shown limited utility of some parameter-extensive components of the transformer architecture. In particular, the following findings can be formulated: The MLP component is frequently presented as necessary for capturing nonlinearities in the modeled relationship. However, the inherent nonlinearity of the similarity measures seems powerful enough in many practical cases.

<!-- chunk {"id": "body-0054", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

While the classification performance without the MLPs is not significantly inferior to that with MLPs, a substantial benefit is saving the parameters. With model size $N$, the attention mechanism requires $4N^{2}$ parameters in the form of matrices $W^{Q}$, $W^{K}W^{V}$, and $W^{O}$. The size of the MLP is usually chosen as an integer multiple of $h$ of the model size. Then, the MLP consists of weights and biases of two layers, with a total of ${{hN{({N + 1})}} + {N{({{hN} + 1})}}} = {{2hN^{2}} + {hN} + N} \approx {2hN^{2}}$. If the multiple is $h = 4$, MLP has double the number of parameters as the attention mechanism. Consequently, omitting MLP reduces the parameters to $33\ \%$ of the original size.

<!-- chunk {"id": "body-0055", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

Symmetric similarity measures tend to perform better than asymmetric ones, with $50\ \%$ fewer query and key matrix parameters. This improvement may be reached by excluding undesirable freedoms, such as a token being dissimilar to itself. The parameter reduction can be expected to constrain the search for the optimum fit fruitfully.

<!-- chunk {"id": "body-0056", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

Collapsing the value and the key matrix into one is another possibility of reducing the parameter set of these matrices by $50\ \%$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

Omitting the value matrix $W^{V}$ and the projection matrix $W^{O}$ reduces the parameters of the whole attention module by $50\ \%$. This variant has also been proposed by \[He and Hofmann, 2024\], with the observation of no significant performance loss in NLP benchmarks.

<!-- chunk {"id": "body-0058", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

Both preceding reductions amount to a reduction to $25\ \%$ of the original attention module size.

<!-- chunk {"id": "body-0059", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

In our experiments, the variants with the collapsed query/key matrices, omitted value, and projection matrices are slightly inferior for MNIST but equal for CIFAR-10. These minimum variants have less than $10\ \%$ of parameters compared with the classical transformers, including MLP. Compared to the architecture with 12 encoders, it is as little as $5\ \%$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

The savings in computing time have been proportional to the savings in parameter numbers.

<!-- chunk {"id": "body-0061", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

Our research has been limited to image processing benchmarks MNIST, CIFAR-10, and ImageNet. The experiments with the last benchmark have partially failed due to computing problems. Empirical evidence with the help of two medium-sized benchmarks and an incomplete test of a larger one is not satisfactory. This requests further research with more robust algorithms. There is considerable potential for second-order optimization methods such as the conjugate gradient algorithm of \[Fletcher and Reeves, 1964\], thoroughly described in \[Press et al., 1992\]. This algorithm's convergence is excellent, but implementing the stopping rule in widespread packages seems to improve its ability to prevent early stops before reaching the minimum region.

<!-- chunk {"id": "body-0062", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

Limitations to image processing suggest further extension. The proper domain of transformers is NLP. An obstacle to its investigation is the size of benchmark problems, so most published investigations consist of observing the performance of fine-tuning pre-trained models. To use pre-trained parameter sets, these fine-tuned models must be identical or almost identical to the pre-trained models. This makes the testing of different architectures difficult. A possibility is to use a large model used for pre-training as a *teacher* and a medium-sized model as *student*, mimicking its performance. This procedure, referred to as *knowledge distillation*, has been proposed by \[Hinton et al., 2015\] and used, e.g., by \[Sun et al., 2019\].

<!-- chunk {"id": "body-0063", "role": "body", "section": "CONCLUSIONS AND LIMITATIONS", "weight": 1.0} -->

These will be important focuses soon.
