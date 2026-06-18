<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Phrase Representations Using RNN Encoder-Decoder for Statistical Machine Translation

Topics include Neural networks, Recurrent neural networks, Learning, Recurrent neural network encoder-decoder, Machine translation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a novel neural network model called RNN Encoder-Decoder that consists of two recurrent neural networks (RNN). One RNN encodes a sequence of symbols into a fixed-length vector representation, and the other decodes the representation into another sequence of symbols. The encoder and decoder of the proposed model are jointly trained to maximize the conditional probability of a target sequence given a source sequence. The performance of a statistical machine translation system is empirically found to improve by using the conditional probabilities of phrase pairs computed by the RNN Encoder-Decoder as an additional feature in the existing log-linear model. Qualitatively, we show that the proposed model learns a semantically and syntactically meaningful representation of linguistic phrases.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep neural networks have shown great success in various applications such as objection recognition and speech recognition. Furthermore, many recent works showed that neural networks can be successfully used in a number of tasks in natural language processing (NLP). These include, but are not limited to, language modeling \[Bengio et al., 2003\], paraphrase detection \[Socher et al., 2011\] and word embedding extraction \[Mikolov et al., 2013\]. In the field of statistical machine translation (SMT), deep neural networks have begun to show promising results. \[Schwenk, 2012\] summarizes a successful usage of feedforward neural networks in the framework of phrase-based SMT system.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Along this line of research on using neural networks for SMT, this paper focuses on a novel neural network architecture that can be used as a part of the conventional phrase-based SMT system. The proposed neural network architecture, which we will refer to as an RNN Encoder--Decoder, consists of two recurrent neural networks (RNN) that act as an encoder and a decoder pair. The encoder maps a variable-length source sequence to a fixed-length vector, and the decoder maps the vector representation back to a variable-length target sequence. The two networks are trained jointly to maximize the conditional probability of the target sequence given a source sequence. Additionally, we propose to use a rather sophisticated hidden unit in order to improve both the memory capacity and the ease of training.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed RNN Encoder--Decoder with a novel hidden unit is empirically evaluated on the task of translating from English to French. We train the model to learn the translation probability of an English phrase to a corresponding French phrase. The model is then used as a part of a standard phrase-based SMT system by scoring each phrase pair in the phrase table. The empirical evaluation reveals that this approach of scoring phrase pairs with an RNN Encoder--Decoder improves the translation performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We qualitatively analyze the trained RNN Encoder--Decoder by comparing its phrase scores with those given by the existing translation model. The qualitative analysis shows that the RNN Encoder--Decoder is better at capturing the linguistic regularities in the phrase table, indirectly explaining the quantitative improvements in the overall translation performance. The further analysis of the model reveals that the RNN Encoder--Decoder learns a continuous space representation of a phrase that preserves both the semantic and syntactic structure of the phrase.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Preliminary: Recurrent Neural Networks", "weight": 1.0} -->

A recurrent neural network (RNN) is a neural network that consists of a hidden state $\mathbf{h}$ and an optional output $\mathbf{y}$ which operates on a variable-length sequence $\mathbf{x} = {(x_{1},\ldots,x_{T})}$. At each time step $t$, the hidden state $\mathbf{h}_{\langle t\rangle}$ of the RNN is updated by

<!-- chunk {"id": "body-0008", "role": "body", "section": "Preliminary: Recurrent Neural Networks", "weight": 1.0} -->

where $f$ is a non-linear activation function. $f$ may be as simple as an element-wise logistic sigmoid function and as complex as a long short-term memory (LSTM) unit \[Hochreiter and Schmidhuber, 1997\].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Preliminary: Recurrent Neural Networks", "weight": 1.0} -->

An RNN can learn a probability distribution over a sequence by being trained to predict the next symbol in a sequence. In that case, the output at each timestep $t$ is the conditional distribution $p{({x_{t} \mid {x_{t - 1},\ldots,x_{1}}})}$. For example, a multinomial distribution ($1$-of-$K$ coding) can be output using a softmax activation function

<!-- chunk {"id": "body-0010", "role": "body", "section": "Preliminary: Recurrent Neural Networks", "weight": 1.0} -->

for all possible symbols $j = {1,\ldots,K}$, where $\mathbf{w}_{j}$ are the rows of a weight matrix $\mathbf{W}$. By combining these probabilities, we can compute the probability of the sequence $\mathbf{x}$ using

<!-- chunk {"id": "body-0011", "role": "body", "section": "Preliminary: Recurrent Neural Networks", "weight": 1.0} -->

From this learned distribution, it is straightforward to sample a new sequence by iteratively sampling a symbol at each time step.

<!-- chunk {"id": "body-0012", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

In this paper, we propose a novel neural network architecture that learns to encode a variable-length sequence into a fixed-length vector representation and to decode a given fixed-length vector representation back into a variable-length sequence. From a probabilistic perspective, this new model is a general method to learn the conditional distribution over a variable-length sequence conditioned on yet another variable-length sequence, e.g. $p{(y_{1},\ldots,{y_{T^{\prime}} \mid {x_{1},\ldots,x_{T}}})}$, where one should note that the input and output sequence lengths $T$ and $T^{\prime}$ may differ.

<!-- chunk {"id": "body-0013", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

The encoder is an RNN that reads each symbol of an input sequence $\mathbf{x}$ sequentially. As it reads each symbol, the hidden state of the RNN changes according to Eq.. After reading the end of the sequence (marked by an end-of-sequence symbol), the hidden state of the RNN is a summary $\mathbf{c}$ of the whole input sequence.

<!-- chunk {"id": "body-0014", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

The decoder of the proposed model is another RNN which is trained to generate the output sequence by predicting the next symbol $y_{t}$ given the hidden state $\mathbf{h}_{\langle t\rangle}$. However, unlike the RNN described in Sec. 2.1, both $y_{t}$ and $\mathbf{h}_{\langle t\rangle}$ are also conditioned on $y_{t - 1}$ and on the summary $\mathbf{c}$ of the input sequence. Hence, the hidden state of the decoder at time $t$ is computed,

<!-- chunk {"id": "body-0015", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

and similarly, the conditional distribution of the next symbol is

<!-- chunk {"id": "body-0016", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

for given activation functions $f$ and $g$ (the latter must produce valid probabilities, e.g. with a softmax).

<!-- chunk {"id": "body-0017", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

See Fig. 1 for a graphical depiction of the proposed model architecture.

<!-- chunk {"id": "body-0018", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

The two components of the proposed RNN Encoder--Decoder are jointly trained to maximize the conditional log-likelihood

<!-- chunk {"id": "body-0019", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

where $\mathbf{θ}$ is the set of the model parameters and each $\left( \mathbf{x}_{n},\mathbf{y}_{n} \right)$ is an (input sequence, output sequence) pair from the training set. In our case, as the output of the decoder, starting from the input, is differentiable, we can use a gradient-based algorithm to estimate the model parameters.

<!-- chunk {"id": "body-0020", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

Once the RNN Encoder--Decoder is trained, the model can be used in two ways. One way is to use the model to generate a target sequence given an input sequence. On the other hand, the model can be used to score a given pair of input and output sequences, where the score is simply a probability $p_{\mathbf{θ}}{({\mathbf{y} \mid \mathbf{x}})}$ from Eqs. and.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

In addition to a novel model architecture, we also propose a new type of hidden unit ($f$ in Eq. ) that has been motivated by the LSTM unit but is much simpler to compute and implement.^11^1 The LSTM unit, which has shown impressive results in several applications such as speech recognition, has a memory cell and four gating units that adaptively control the information flow inside the unit, compared to only two gating units in the proposed hidden unit. For details on LSTM networks, see, e.g., \[Graves, 2012\]. Fig. 2 shows the graphical depiction of the proposed hidden unit.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

Let us describe how the activation of the $j$-th hidden unit is computed. First, the reset gate $r_{j}$ is computed by

<!-- chunk {"id": "body-0023", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

where $\sigma$ is the logistic sigmoid function, and $\left\lbrack. \right\rbrack_{j}$ denotes the $j$-th element of a vector. $\mathbf{x}$ and $\mathbf{h}_{t - 1}$ are the input and the previous hidden state, respectively. $\mathbf{W}_{r}$ and $\mathbf{U}_{r}$ are weight matrices which are learned.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

Similarly, the update gate $z_{j}$ is computed by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

The actual activation of the proposed unit $h_{j}$ is then computed by

<!-- chunk {"id": "body-0026", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

In this formulation, when the reset gate is close to 0, the hidden state is forced to ignore the previous hidden state and reset with the current input only. This effectively allows the hidden state to drop any information that is found to be irrelevant later in the future, thus, allowing a more compact representation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

On the other hand, the update gate controls how much information from the previous hidden state will carry over to the current hidden state. This acts similarly to the memory cell in the LSTM network and helps the RNN to remember long-term information. Furthermore, this may be considered an adaptive variant of a leaky-integration unit \[Bengio et al., 2013\].

<!-- chunk {"id": "body-0028", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

As each hidden unit has separate reset and update gates, each hidden unit will learn to capture dependencies over different time scales. Those units that learn to capture short-term dependencies will tend to have reset gates that are frequently active, but those that capture longer-term dependencies will have update gates that are mostly active.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Hidden Unit that Adaptively Remembers and Forgets", "weight": 1.0} -->

In our preliminary experiments, we found that it is crucial to use this new unit with gating units. We were not able to get meaningful result with an oft-used $\tanh$ unit without any gating.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Statistical Machine Translation", "weight": 1.0} -->

In a commonly used statistical machine translation system (SMT), the goal of the system (decoder, specifically) is to find a translation $\mathbf{f}$ given a source sentence $\mathbf{e}$, which maximizes

<!-- chunk {"id": "body-0031", "role": "body", "section": "Statistical Machine Translation", "weight": 1.0} -->

where the first term at the right hand side is called translation model and the latter language model.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Statistical Machine Translation", "weight": 1.0} -->

where $f_{n}$ and $w_{n}$ are the $n$-th feature and weight, respectively. $Z{(\mathbf{e})}$ is a normalization constant that does not depend on the weights. The weights are often optimized to maximize the BLEU score on a development set.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Statistical Machine Translation", "weight": 1.0} -->

In the phrase-based SMT framework introduced in \[Koehn et al., 2003\] and \[Marcu and Wong, 2002\], the translation model ${\log p}{({\mathbf{e} \mid \mathbf{f}})}$ is factorized into the translation probabilities of matching phrases in the source and target sentences.^22^2 Without loss of generality, from here, we refer to $p{({\mathbf{e} \mid \mathbf{f}})}$ for each phrase pair as a translation model as well These probabilities are once again considered additional features in the log-linear model (see Eq. ) and are weighted accordingly to maximize the BLEU score.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Statistical Machine Translation", "weight": 1.0} -->

Since the neural net language model was proposed in \[Bengio et al., 2003\], neural networks have been used widely in SMT systems. In many cases, neural networks have been used to rescore translation hypotheses ($n$-best lists). Recently, however, there has been interest in training neural networks to score the translated sentence (or phrase pairs) using a representation of the source sentence as an additional input. See, e.g., \[Schwenk, 2012\], \[Son et al., 2012\] and \[Zou et al., 2013\].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Scoring Phrase Pairs with RNN Encoder--Decoder", "weight": 1.0} -->

Here we propose to train the RNN Encoder--Decoder (see Sec. 2.2) on a table of phrase pairs and use its scores as additional features in the log-linear model in Eq. when tuning the SMT decoder.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Scoring Phrase Pairs with RNN Encoder--Decoder", "weight": 1.0} -->

When we train the RNN Encoder--Decoder, we ignore the (normalized) frequencies of each phrase pair in the original corpora. This measure was taken in order to reduce the computational expense of randomly selecting phrase pairs from a large phrase table according to the normalized frequencies and to ensure that the RNN Encoder--Decoder does not simply learn to rank the phrase pairs according to their numbers of occurrences. One underlying reason for this choice was that the existing translation probability in the phrase table already reflects the frequencies of the phrase pairs in the original corpus. With a fixed capacity of the RNN Encoder--Decoder, we try to ensure that most of the capacity of the model is focused toward learning linguistic regularities, i.e., distinguishing between plausible and implausible translations, or learning the "manifold" (region of probability concentration) of plausible translations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Scoring Phrase Pairs with RNN Encoder--Decoder", "weight": 1.0} -->

Once the RNN Encoder--Decoder is trained, we add a new score for each phrase pair to the existing phrase table. This allows the new scores to enter into the existing tuning algorithm with minimal additional overhead in computation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Scoring Phrase Pairs with RNN Encoder--Decoder", "weight": 1.0} -->

As Schwenk pointed out in \[Schwenk, 2012\], it is possible to completely replace the existing phrase table with the proposed RNN Encoder--Decoder. In that case, for a given source phrase, the RNN Encoder--Decoder will need to generate a list of (good) target phrases. This requires, however, an expensive sampling procedure to be performed repeatedly. In this paper, thus, we only consider rescoring the phrase pairs in the phrase table.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

Before presenting the empirical results, we discuss a number of recent works that have proposed to use neural networks in the context of SMT.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

Schwenk in \[Schwenk, 2012\] proposed a similar approach of scoring phrase pairs. Instead of the RNN-based neural network, he used a feedforward neural network that has fixed-size inputs (7 words in his case, with zero-padding for shorter phrases) and fixed-size outputs (7 words in the target language). When it is used specifically for scoring phrases for the SMT system, the maximum phrase length is often chosen to be small. However, as the length of phrases increases or as we apply neural networks to other variable-length sequence data, it is important that the neural network can handle variable-length input and output. The proposed RNN Encoder--Decoder is well-suited for these applications.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

Similar to \[Schwenk, 2012\], Devlin et al. \[Devlin et al., 2014\] proposed to use a feedforward neural network to model a translation model, however, by predicting one word in a target phrase at a time. They reported an impressive improvement, but their approach still requires the maximum length of the input phrase (or context words) to be fixed a priori.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

Although it is not exactly a neural network they train, the authors of \[Zou et al., 2013\] proposed to learn a bilingual embedding of words/phrases. They use the learned embedding to compute the distance between a pair of phrases which is used as an additional score of the phrase pair in an SMT system.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

In \[Chandar et al., 2014\], a feedforward neural network was trained to learn a mapping from a bag-of-words representation of an input phrase to an output phrase. This is closely related to both the proposed RNN Encoder--Decoder and the model proposed in \[Schwenk, 2012\], except that their input representation of a phrase is a bag-of-words. A similar approach of using bag-of-words representations was proposed in \[Gao et al., 2013\] as well. Earlier, a similar encoder--decoder model using two recursive neural networks was proposed in \[Socher et al., 2011\], but their model was restricted to a monolingual setting, i.e. the model reconstructs an input sentence. More recently, another encoder--decoder model using an RNN was proposed in \[Auli et al., 2013\], where the decoder is conditioned on a representation of either a source sentence or a source context.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

One important difference between the proposed RNN Encoder--Decoder and the approaches in \[Zou et al., 2013\] and \[Chandar et al., 2014\] is that the order of the words in source and target phrases is taken into account. The RNN Encoder--Decoder naturally distinguishes between sequences that have the same words but in a different order, whereas the aforementioned approaches effectively ignore order information.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Related Approaches: Neural Networks in Machine Translation", "weight": 1.0} -->

The closest approach related to the proposed RNN Encoder--Decoder is the Recurrent Continuous Translation Model (Model 2) proposed in \[Kalchbrenner and Blunsom, 2013\]. In their paper, they proposed a similar model that consists of an encoder and decoder. The difference with our model is that they used a convolutional $n$-gram model (CGM) for the encoder and the hybrid of an inverse CGM and a recurrent neural network for the decoder. They, however, evaluated their model on rescoring the $n$-best list proposed by the conventional SMT system and computing the perplexity of the gold standard translations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our approach on the English/French translation task of the WMT'14 workshop.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Data and Baseline System", "weight": 1.0} -->

Large amounts of resources are available to build an English/French SMT system in the framework of the WMT'14 translation task. The bilingual corpora include Europarl (61M words), news commentary (5.5M), UN (421M), and two crawled corpora of 90M and 780M words respectively. The last two corpora are quite noisy. To train the French language model, about 712M words of crawled newspaper material is available in addition to the target side of the bitexts. All the word counts refer to French words after tokenization.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Data and Baseline System", "weight": 1.0} -->

It is commonly acknowledged that training statistical models on the concatenation of all this data does not necessarily lead to optimal performance, and results in extremely large models which are difficult to handle. Instead, one should focus on the most relevant subset of the data for a given task. We have done so by applying the data selection method proposed in \[Moore and Lewis, 2010\], and its extension to bitexts \[Axelrod et al., 2011\]. By these means we selected a subset of 418M words out of more than 2G words for language modeling and a subset of 348M out of 850M words for training the RNN Encoder--Decoder. We used the test set newstest2012 and 2013 for data selection and weight tuning with MERT, and newstest2014 as our test set. Each set has more than 70 thousand words and a single reference translation.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Data and Baseline System", "weight": 1.0} -->

For training the neural networks, including the proposed RNN Encoder--Decoder, we limited the source and target vocabulary to the most frequent 15,000 words for both English and French. This covers approximately 93% of the dataset. All the out-of-vocabulary words were mapped to a special token ($\left\lbrack \text{UNK} \right\rbrack$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Data and Baseline System", "weight": 1.0} -->

The baseline phrase-based SMT system was built using Moses with default settings. This system achieves a BLEU score of 30.64 and 33.3 on the development and test sets, respectively (see Table 1).

<!-- chunk {"id": "body-0051", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

The RNN Encoder--Decoder used in the experiment had 1000 hidden units with the proposed gates at the encoder and at the decoder. The input matrix between each input symbol $x_{\langle t\rangle}$ and the hidden unit is approximated with two lower-rank matrices, and the output matrix is approximated similarly. We used rank-100 matrices, equivalent to learning an embedding of dimension 100 for each word. The activation function used for $\overset{\sim}{h}$ in Eq. is a hyperbolic tangent function. The computation from the hidden state in the decoder to the output is implemented as a deep neural network \[Pascanu et al., 2014\] with a single intermediate layer having 500 maxout units each pooling 2 inputs \[Goodfellow et al., 2013\].

<!-- chunk {"id": "body-0052", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

All the weight parameters in the RNN Encoder--Decoder were initialized by sampling from an isotropic zero-mean (white) Gaussian distribution with its standard deviation fixed to $0.01$, except for the recurrent weight parameters. For the recurrent weight matrices, we first sampled from a white Gaussian distribution and used its left singular vectors matrix, following \[Saxe et al., 2014\].

<!-- chunk {"id": "body-0053", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

We used Adadelta and stochastic gradient descent to train the RNN Encoder--Decoder with hyperparameters $\epsilon = 10^{- 6}$ and $\rho = 0.95$ \[Zeiler, 2012\]. At each update, we used 64 randomly selected phrase pairs from a phrase table (which was created from 348M words). The model was trained for approximately three days.

<!-- chunk {"id": "body-0054", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

Details of the architecture used in the experiments are explained in more depth in the supplementary material.

<!-- chunk {"id": "body-0055", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

at the end of the
[a la fin de la] [ŕ la fin des années] [être supprimés à la fin de la]
[à la fin du] [à la fin des] [à la fin de la]

<!-- chunk {"id": "body-0056", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

for the first time
[r © pour la premirëre fois] [été donnés pour la première fois] [été commémorée pour la première fois]
[pour la première fois] [pour la première fois,] [pour la première fois que]

<!-- chunk {"id": "body-0057", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

in the United States and
[? aux ?tats-Unis et] [été ouvertes aux États-Unis et] [été constatées aux États-Unis et]
[aux Etats-Unis et] [des Etats-Unis et] [des États-Unis et]

<!-- chunk {"id": "body-0058", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

[?s, qu’] [?s, ainsi que] [?re aussi bien que]
[, ainsi qu’] [, ainsi que] [, ainsi que les]

<!-- chunk {"id": "body-0059", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

one of the most
[?t ?l’ un des plus] [?l’ un des plus] [être retenue comme un de ses plus]

<!-- chunk {"id": "body-0060", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

, Minister of Communications and Transport
[Secrétaire aux communications et aux transports:] [Secrétaire aux communications et aux transports]
[Secrétaire aux communications et aux transports] [Secrétaire aux communications et aux transports:]

<!-- chunk {"id": "body-0061", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

did not comply with the
[vestimentaire, ne correspondaient pas à des] [susmentionnée n’ était pas conforme aux] [présentées n’ étaient pas conformes à la]
[n’ ont pas respecté les] [n’ était pas conforme aux] [n’ ont pas respecté la]

<!-- chunk {"id": "body-0062", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

parts of the world.
[© gions du monde.] [régions du monde considérées.] [région du monde considérée.]
[parties du monde.] [les parties du monde.] [des parties du monde.]

<!-- chunk {"id": "body-0063", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

the past few days.
[le petit texte.] [cours des tout derniers jours.] [les tout derniers jours.]
[ces derniers jours.] [les derniers jours.] [cours des derniers jours.]

<!-- chunk {"id": "body-0064", "role": "body", "section": "RNN Encoder--Decoder", "weight": 1.0} -->

on Friday and Saturday
[vendredi et samedi à la] [vendredi et samedi à] [se déroulera vendredi et samedi,]
[le vendredi et le samedi] [le vendredi et samedi] [vendredi et samedi]

<!-- chunk {"id": "body-0065", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

In order to assess the effectiveness of scoring phrase pairs with the proposed RNN Encoder--Decoder, we also tried a more traditional approach of using a neural network for learning a target language model (CSLM) \[Schwenk, 2007\]. Especially, the comparison between the SMT system using CSLM and that using the proposed approach of phrase scoring by RNN Encoder--Decoder will clarify whether the contributions from multiple neural networks in different parts of the SMT system add up or are redundant.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

We trained the CSLM model on 7-grams from the target corpus. Each input word was projected into the embedding space ${\mathbb{R}}^{512}$, and they were concatenated to form a 3072-dimensional vector. The concatenated vector was fed through two rectified layers (of size 1536 and 1024) \[Glorot et al., 2011\]. The output layer was a simple softmax layer (see Eq. ). All the weight parameters were initialized uniformly between $- 0.01$ and $0.01$, and the model was trained until the validation perplexity did not improve for 10 epochs. After training, the language model achieved a perplexity of 45.80. The validation set was a random selection of 0.1% of the corpus. The model was used to score partial translations during the decoding process, which generally leads to higher gains in BLEU score than n-best list rescoring \[Vaswani et al., 2013\].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

To address the computational complexity of using a CSLM in the decoder a buffer was used to aggregate n-grams during the stack-search performed by the decoder. Only when the buffer is full, or a stack is about to be pruned, the n-grams are scored by the CSLM. This allows us to perform fast matrix-matrix multiplication on GPU using Theano \[Bergstra et al., 2010, Bastien et al., 2012\].

<!-- chunk {"id": "body-0068", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

Samples from RNN Encoder–Decoder

<!-- chunk {"id": "body-0069", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

for the first time
[pour la première fois] ( × 24) [pour la première fois que] ( × 2)

<!-- chunk {"id": "body-0070", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

in the United States and
[aux États-Unis et] ( × 6) [dans les États-Unis et] ( × 4)

<!-- chunk {"id": "body-0071", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

[, ainsi que] [ainsi que] [, ainsi qu’] [et UNK]

<!-- chunk {"id": "body-0072", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

one of the most
[l’ un des plus] ( × 9) [l’ un des] ( × 5) [l’ une des plus] ( × 2)

<!-- chunk {"id": "body-0073", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

Samples from RNN Encoder–Decoder

<!-- chunk {"id": "body-0074", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

, Minister of Communications and Transport
[, ministre des communications et le transport] ( × 13)

<!-- chunk {"id": "body-0075", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

did not comply with the
[n’ tait pas conforme aux] [n’ a pas respect l’] ( × 2) [n’ a pas respect la] ( × 3)

<!-- chunk {"id": "body-0076", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

parts of the world.
[arts du monde.] ( × 11) [des arts du monde.] ( × 7)

<!-- chunk {"id": "body-0077", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

the past few days.
[quelques jours.] ( × 5) [les derniers jours.] ( × 5) [ces derniers jours.] ( × 2)

<!-- chunk {"id": "body-0078", "role": "body", "section": "Neural Language Model", "weight": 1.0} -->

on Friday and Saturday
[vendredi et samedi] ( × 5) [le vendredi et samedi] ( × 7) [le vendredi et le samedi] ( × 4)

<!-- chunk {"id": "body-0079", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

Baseline + CSLM + RNN + Word penalty

<!-- chunk {"id": "body-0080", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

The results are presented in Table 1. As expected, adding features computed by neural networks consistently improves the performance over the baseline performance.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

The best performance was achieved when we used both CSLM and the phrase scores from the RNN Encoder--Decoder. This suggests that the contributions of the CSLM and the RNN Encoder--Decoder are not too correlated and that one can expect better results by improving each method independently. Furthermore, we tried penalizing the number of words that are unknown to the neural networks (i.e. words which are not in the shortlist). We do so by simply adding the number of unknown words as an additional feature the log-linear model in Eq..^33^3 To understand the effect of the penalty, consider the set of all words in the 15,000 large shortlist, SL. All words $x^{i} \notin \text{SL}$ are replaced by a special token $\left\lbrack \text{UNK} \right\rbrack$ before being scored by the neural networks. Hence, the conditional probability of any $x_{t}^{i} \notin \text{SL}$ is actually given by the model as $p\left( x_{t} = \right.$ $\left.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

\left\lbrack \text{UNK} \right\rbrack \mid x_{< t} \right) = p\left( x_{t} \notin \text{SL} \mid x_{< t} \right)$ ${= {\sum\limits_{x_{t}^{j} \notin {SL}}{p\left( {x_{t}^{j} \mid x_{< t}} \right)}} \geq {p\left( {x_{t}^{i} \mid x_{< t}} \right)}},$ where $x_{< t}$ is a shorthand notation for $x_{t - 1},\ldots,x_{1}$. As a result, the probability of words not in the shortlist is always overestimated. It is possible to address this issue by backing off to an existing model that contain non-shortlisted words In this paper, however, we opt for introducing a word penalty instead, which counteracts the word probability overestimation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

However, in this case we were not able to achieve better performance on the test set, but only on the development set.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

In order to understand where the performance improvement comes, we analyze the phrase pair scores computed by the RNN Encoder--Decoder against the corresponding $p{({\mathbf{f} \mid \mathbf{e}})}$ from the translation model. Since the existing translation model relies solely on the statistics of the phrase pairs in the corpus, we expect its scores to be better estimated for the frequent phrases but badly estimated for rare phrases. Also, as we mentioned earlier in Sec. 3.1, we further expect the RNN Encoder--Decoder which was trained without any frequency information to score the phrase pairs based rather on the linguistic regularities than on the statistics of their occurrences in the corpus.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

We focus on those pairs whose source phrase is long (more than 3 words per source phrase) and frequent. For each such source phrase, we look at the target phrases that have been scored high either by the translation probability $p{({\mathbf{f} \mid \mathbf{e}})}$ or by the RNN Encoder--Decoder. Similarly, we perform the same procedure with those pairs whose source phrase is long but rare in the corpus.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Table 2 lists the top-$3$ target phrases per source phrase favored either by the translation model or by the RNN Encoder--Decoder. The source phrases were randomly chosen among long ones having more than 4 or 5 words.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

In most cases, the choices of the target phrases by the RNN Encoder--Decoder are closer to actual or literal translations. We can observe that the RNN Encoder--Decoder prefers shorter phrases in general.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Interestingly, many phrase pairs were scored similarly by both the translation model and the RNN Encoder--Decoder, but there were as many other phrase pairs that were scored radically different (see Fig. 3). This could arise from the proposed approach of training the RNN Encoder--Decoder on a set of unique phrase pairs, discouraging the RNN Encoder--Decoder from learning simply the frequencies of the phrase pairs from the corpus, as explained earlier.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Furthermore, in Table 3, we show for each of the source phrases in Table 2, the generated samples from the RNN Encoder--Decoder. For each source phrase, we generated 50 samples and show the top-five phrases accordingly to their scores. We can see that the RNN Encoder--Decoder is able to propose well-formed target phrases without looking at the actual phrase table. Importantly, the generated phrases do not overlap completely with the target phrases from the phrase table. This encourages us to further investigate the possibility of replacing the whole or a part of the phrase table with the proposed RNN Encoder--Decoder in the future.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Word and Phrase Representations", "weight": 1.0} -->

Since the proposed RNN Encoder--Decoder is not specifically designed only for the task of machine translation, here we briefly look at the properties of the trained model.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Word and Phrase Representations", "weight": 1.0} -->

It has been known for some time that continuous space language models using neural networks are able to learn semantically meaningful embeddings. Since the proposed RNN Encoder--Decoder also projects to and maps back from a sequence of words into a continuous space vector, we expect to see a similar property with the proposed model as well.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Word and Phrase Representations", "weight": 1.0} -->

The left plot in Fig. 4 shows the 2--D embedding of the words using the word embedding matrix learned by the RNN Encoder--Decoder. The projection was done by the recently proposed Barnes-Hut-SNE \[van der Maaten, 2013\]. We can clearly see that semantically similar words are clustered with each other (see the zoomed-in plots in Fig. 4).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Word and Phrase Representations", "weight": 1.0} -->

The proposed RNN Encoder--Decoder naturally generates a continuous-space representation of a phrase. The representation ($\mathbf{c}$ in Fig. 1) in this case is a 1000-dimensional vector. Similarly to the word representations, we visualize the representations of the phrases that consists of four or more words using the Barnes-Hut-SNE in Fig. 5.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Word and Phrase Representations", "weight": 1.0} -->

From the visualization, it is clear that the RNN Encoder--Decoder captures both semantic and syntactic structures of the phrases. For instance, in the bottom-left plot, most of the phrases are about the duration of time, while those phrases that are syntactically similar are clustered together. The bottom-right plot shows the cluster of phrases that are semantically similar (countries or regions). On the other hand, the top-right plot shows the phrases that are syntactically similar.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a new neural network architecture, called an RNN Encoder--Decoder that is able to learn the mapping from a sequence of an arbitrary length to another sequence, possibly from a different set, of an arbitrary length. The proposed RNN Encoder--Decoder is able to either score a pair of sequences (in terms of a conditional probability) or generate a target sequence given a source sequence. Along with the new architecture, we proposed a novel hidden unit that includes a reset gate and an update gate that adaptively control how much each hidden unit remembers or forgets while reading/generating a sequence.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We evaluated the proposed model with the task of statistical machine translation, where we used the RNN Encoder--Decoder to score each phrase pair in the phrase table. Qualitatively, we were able to show that the new model is able to capture linguistic regularities in the phrase pairs well and also that the RNN Encoder--Decoder is able to propose well-formed target phrases.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The scores by the RNN Encoder--Decoder were found to improve the overall translation performance in terms of BLEU scores. Also, we found that the contribution by the RNN Encoder--Decoder is rather orthogonal to the existing approach of using neural networks in the SMT system, so that we can improve further the performance by using, for instance, the RNN Encoder--Decoder and the neural net language model together.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our qualitative analysis of the trained model shows that it indeed captures the linguistic regularities in multiple levels i.e. at the word level as well as phrase level. This suggests that there may be more natural language related applications that may benefit from the proposed RNN Encoder--Decoder.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The proposed architecture has large potential for further improvement and analysis. One approach that was not investigated here is to replace the whole, or a part of the phrase table by letting the RNN Encoder--Decoder propose target phrases. Also, noting that the proposed model is not limited to being used with written language, it will be an important future research to apply the proposed architecture to other applications such as speech transcription.
