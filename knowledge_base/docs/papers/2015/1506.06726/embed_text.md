## Introduction

Developing learning algorithms for distributed compositional semantics of words has been a long-standing open problem at the intersection of language understanding and machine learning. In recent years, several approaches have been developed for learning composition operators that map word vectors to sentence vectors including recursive networks socher2013recursive, recurrent networks hochreiter1997long, convolutional networks kalchbrenner2014convolutional; kim2014convolutional and recursive-convolutional methods cho2014properties; zhao2015self among others. All of these methods produce sentence representations that are passed to a supervised task and depend on a class label in order to backpropagate through the composition weights. Consequently, these methods learn high-quality sentence representations but are tuned only for their respective task. The paragraph vector of le2014distributed is an alternative to the above models in that it can learn unsupervised sentence representations by introducing a distributed sentence indicator as part of a neural language model. The downside is at test time, inference needs to be performed to compute a new vector.

In this paper we abstract away from the composition methods themselves and consider an alternative loss function that can be applied with any composition operator. We consider the following question: is there a task and a corresponding loss that will allow us to learn highly generic sentence representations? We give evidence for this by proposing a model for learning high-quality sentence vectors without a particular supervised task in mind. Using word vector learning as inspiration, we propose an objective function that abstracts the skip-gram model of mikolov2013efficient to the sentence level. That is, instead of using a word to predict its surrounding context, we instead encode a sentence to predict the sentences around it. Thus, any composition operator can be substituted as a sentence encoder and only the objective function becomes modified. Figure 1 illustrates the model. We call our model skip-thoughts and vectors induced by our model are called skip-thought vectors.

Our model depends on having a training corpus of contiguous text. We chose to use a large collection of novels, namely the BookCorpus dataset moviebook15 for training our models. These are free books written by yet unpublished authors. The dataset has books in 16 different genres, e.g., *Romance* (2,865 books), *Fantasy*, *Science fiction*, *Teen*, etc. Table 1 highlights the summary statistics of the book corpus. Along with narratives, books contain dialogue, emotion and a wide range of interaction between characters. Furthermore, with a large enough collection the training set is not biased towards any particular domain or application. Table 2 shows nearest neighbours of sentences from a model trained on the BookCorpus dataset. These results show that skip-thought vectors learn to accurately capture semantics and syntax of the sentences they encode.

We evaluate our vectors in a newly proposed setting: after learning skip-thoughts, freeze the model and use the encoder as a generic feature extractor for arbitrary tasks. In our experiments we consider 8 tasks: semantic-relatedness, paraphrase detection, image-sentence ranking and 5 standard classification benchmarks. In these experiments, we extract skip-thought vectors and train linear models to evaluate the representations directly, without any additional fine-tuning. As it turns out, skip-thoughts yield generic representations that perform robustly across all tasks considered.

One difficulty that arises with such an experimental setup is being able to construct a large enough word vocabulary to encode arbitrary sentences. For example, a sentence from a Wikipedia article might contain nouns that are highly unlikely to appear in our book vocabulary. We solve this problem by learning a mapping that transfers word representations from one model to another. Using pre-trained word2vec representations learned with a continuous bag-of-words model mikolov2013efficient, we learn a linear mapping from a word in word2vec space to a word in the encoder's vocabulary space. The mapping is learned using all words that are shared between vocabularies. After training, any word that appears in word2vec can then get a vector in the encoder word embedding space.

## Approach

Figure 1: The skip-thoughts model. Given a tuple (si − 1, si, si + 1) of contiguous sentences, with si the i-th sentence of a book, the sentence si is encoded and tries to reconstruct the previous sentence si − 1 and next sentence si + 1. In this example, the input is the sentence triplet I got back home. I could see the cat on the steps. This was strange. Unattached arrows are connected to the encoder output. Colors indicate which components share parameters. ⟨eos⟩ is the end of sentence token.

## of books # of sentences # of words # of unique words mean # of words per sentence 11,038 74,004,228 984,846,357 1,316,420 13
Table 1: Summary statistics of the BookCorpus dataset moviebook15. We use this corpus to training our model.

Query and nearest sentence

he ran his hand inside his coat, double-checking that the unopened letter was still there.

he slipped his hand between his coat and his shirt, where the folded copies lay in a brown envelope.

im sure youll have a glamorous evening, she said, giving an exaggerated wink.

im really glad you came to the party tonight, he said, turning to her.

although she could tell he had n’t been too invested in any of their other chitchat, he seemed genuinely curious about this.

although he had n’t been following her career with a microscope, he ’d definitely taken notice of her appearances.

an annoying buzz started to ring in my ears, becoming louder and louder as my vision began to swim.

a weighty pressure landed on my lungs and my vision blurred at the edges, threatening my consciousness altogether.

if he had a weapon, he could maybe take out their last imp, and then beat up errol and vanessa.

if he could ram them from behind, send them sailing over the far side of the levee, he had a chance of stopping them.

then, with a stroke of luck, they saw the pair head together towards the portaloos.

then, from out back of the house, they heard a horse scream probably in answer to a pair of sharp spurs digging deep into its flanks.

“ i ’ll take care of it, ” goodman said, taking the phonebook.

“ i ’ll do that, ” julia said, coming in.

he finished rolling up scrolls and, placing them to one side, began the more urgent task of finding ale and tankards.

he righted the table, set the candle on a piece of broken plate, and reached for his flint, steel, and tinder.

Table 2: In each example, the first sentence is a query while the second sentence is its nearest neighbour. Nearest neighbours were scored by cosine similarity from a random sample of 500,000 sentences from our corpus.

### Inducing skip-thought vectors

We treat skip-thoughts in the framework of encoder-decoder models ^11^1A preliminary version of our model was developed in the context of a computer vision application moviebook15.. That is, an encoder maps words to a sentence vector and a decoder is used to generate the surrounding sentences. Encoder-decoder models have gained a lot of traction for neural machine translation. In this setting, an encoder is used to map e.g. an English sentence into a vector. The decoder then conditions on this vector to generate a translation for the source English sentence. Several choices of encoder-decoder pairs have been explored, including ConvNet-RNN kalchbrenner2013recurrent, RNN-RNN cho2014learning and LSTM-LSTM sutskever2014sequence. The source sentence representation can also dynamically change through the use of an attention mechanism bahdanau2014neural to take into account only the relevant words for translation at any given time. In our model, we use an RNN encoder with GRU chung2014empirical activations and an RNN decoder with a conditional GRU. This model combination is nearly identical to the RNN encoder-decoder of cho2014learning used in neural machine translation. GRU has been shown to perform as well as LSTM hochreiter1997long on sequence modelling tasks chung2014empirical while being conceptually simpler. GRU units have only 2 gates and do not require the use of a cell. While we use RNNs for our model, any encoder and decoder can be used so long as we can backpropagate through it.

Assume we are given a sentence tuple ($s_{i - 1},s_{i},s_{i + 1}$). Let $w_{i}^{t}$ denote the $t$-th word for sentence $s_{i}$ and let $\mathbf{x}_{i}^{t}$ denote its word embedding. We describe the model in three parts: the encoder, decoder and objective function.

Encoder. Let $w_{i}^{1},\ldots,w_{i}^{N}$ be the words in sentence $s_{i}$ where $N$ is the number of words in the sentence. At each time step, the encoder produces a hidden state $\mathbf{h}_{i}^{t}$ which can be interpreted as the representation of the sequence $w_{i}^{1},\ldots,w_{i}^{t}$. The hidden state $\mathbf{h}_{i}^{N}$ thus represents the full sentence. To encode a sentence, we iterate the following sequence of equations (dropping the subscript $i$):

where ${\overline{\mathbf{h}}}^{t}$ is the proposed state update at time $t$, $\mathbf{z}^{t}$ is the update gate, $\mathbf{r}_{t}$ is the reset gate ($\odot$) denotes a component-wise product. Both update gates takes values between zero and one.

Decoder. The decoder is a neural language model which conditions on the encoder output $\mathbf{h}_{i}$. The computation is similar to that of the encoder except we introduce matrices $\mathbf{C}_{z}$, $\mathbf{C}_{r}$ and $\mathbf{C}$ that are used to bias the update gate, reset gate and hidden state computation by the sentence vector. One decoder is used for the next sentence $s_{i + 1}$ while a second decoder is used for the previous sentence $s_{i - 1}$. Separate parameters are used for each decoder with the exception of the vocabulary matrix $\mathbf{V}$, which is the weight matrix connecting the decoder's hidden state for computing a distribution over words. In what follows we describe the decoder for the next sentence $s_{i + 1}$ although an analogous computation is used for the previous sentence $s_{i - 1}$. Let $\mathbf{h}_{i + 1}^{t}$ denote the hidden state of the decoder at time $t$. Decoding involves iterating through the following sequence of equations (dropping the subscript $i + 1$):

Given $\mathbf{h}_{i + 1}^{t}$, the probability of word $w_{i + 1}^{t}$ given the previous $t - 1$ words and the encoder vector is

where $\mathbf{v}_{w_{i + 1}^{t}}$ denotes the row of $\mathbf{V}$ corresponding to the word of $w_{i + 1}^{t}$. An analogous computation is performed for the previous sentence $s_{i - 1}$.

Objective. Given a tuple ($s_{i - 1},s_{i},s_{i + 1}$), the objective optimized is the sum of the log-probabilities for the forward and backward sentences conditioned on the encoder representation:

The total objective is the above summed over all such training tuples.

### Vocabulary expansion

##QAM

Table 3: Nearest neighbours of words after vocabulary expansion. Each query is a word that does not appear in our 20,000 word training vocabulary.

We now describe how to expand our encoder's vocabulary to words it has not seen during training. Suppose we have a model that was trained to induce word representations, such as word2vec. Let $\mathcal{V}_{w2v}$ denote the word embedding space of these word representations and let $\mathcal{V}_{rnn}$ denote the RNN word embedding space. We assume the vocabulary of $\mathcal{V}_{w2v}$ is much larger than that of $\mathcal{V}_{rnn}$. Our goal is to construct a mapping $f:{\mathcal{V}_{w2v}\rightarrow\mathcal{V}_{rnn}}$ parameterized by a matrix $\mathbf{W}$ such that $\mathbf{v}^{\prime} = {\mathbf{W}\mathbf{v}}$ for $\mathbf{v} \in \mathcal{V}_{w2v}$ and $\mathbf{v}^{\prime} \in \mathcal{V}_{rnn}$. Inspired by mikolov2013exploiting, which learned linear mappings between translation word spaces, we solve an un-regularized L2 linear regression loss for the matrix $\mathbf{W}$. Thus, any word from $\mathcal{V}_{w2v}$ can now be mapped into $\mathcal{V}_{rnn}$ for encoding sentences. Table 3 shows examples of nearest neighbour words for queries that did not appear in our training vocabulary.

We note that there are alternate strategies for solving the vocabulary problem. One alternative is to initialize the RNN embedding space to that of pre-trained word vectors. This would require a more sophisticated softmax for decoding, or clipping the vocabulary of the decoder as it would be too computationally expensive to naively decode with vocabularies of hundreds of thousands of words. An alternative strategy is to avoid words altogether and train at the character level.

## Experiments

In our experiments, we evaluate the capability of our encoder as a generic feature extractor after training on the BookCorpus dataset. Our experimentation setup on each task is as follows:

Using the learned encoder as a feature extractor, extract skip-thought vectors for all sentences.

If the task involves computing scores between pairs of sentences, compute component-wise features between pairs. This is described in more detail specifically for each experiment.

Train a linear classifier on top of the extracted features, with no additional fine-tuning or backpropagation through the skip-thoughts model.

We restrict ourselves to linear classifiers for two reasons. The first is to directly evaluate the representation quality of the computed vectors. It is possible that additional performance gains can be made throughout our experiments with non-linear models but this falls out of scope of our goal. Furthermore, it allows us to better analyze the strengths and weaknesses of the learned representations. The second reason is that reproducibility now becomes very straightforward.

### Details of training

To induce skip-thought vectors, we train two separate models on our book corpus. One is a unidirectional encoder with 2400 dimensions, which we subsequently refer to as uni-skip. The other is a bidirectional model with forward and backward encoders of 1200 dimensions each. This model contains two encoders with different parameters: one encoder is given the sentence in correct order, while the other is given the sentence in reverse. The outputs are then concatenated to form a 2400 dimensional vector. We refer to this model as bi-skip. For training, we initialize all recurrent matricies with orthogonal initialization saxe2013exact. Non-recurrent weights are initialized from a uniform distribution in \[-0.1,0.1\]. Mini-batches of size 128 are used and gradients are clipped if the norm of the parameter vector exceeds 10. We used the Adam algorithm kingma2014adam for optimization. Both models were trained for roughly two weeks. As an additional experiment, we also report experimental results using a combined model, consisting of the concatenation of the vectors from uni-skip and bi-skip, resulting in a 4800 dimensional vector. Since we are using linear classifiers for evaluation, we were curious to what extent performance gains can be made by trivially increasing the vector dimensionality post-training of the skip-thought models. We refer to this model throughout as combine-skip.

After our models are trained, we then employ vocabulary expansion to map word embeddings into the RNN encoder space. The publically available CBOW word vectors are used for this purpose ^22^2[http://code.google.com/p/word2vec/](http://code.google.com/p/word2vec/). The skip-thought models are trained with a vocabulary size of 20,000 words. After removing multiple word examples from the CBOW model, this results in a vocabulary size of 930,911 words. Thus even though our skip-thoughts model was trained with only 20,000 words, after vocabulary expansion we can now successfully encode 930,911 possible words.

Since our goal is to evaluate skip-thoughts as a general feature extractor, we keep text pre-processing to a minimum. When encoding new sentences, no additional preprocessing is done other than basic tokenization. This is done to test the robustness of our vectors.

### Semantic relatedness

Illinois-LH lai2014illinois

UNAL-NLP jimenez2014unal

Meaning Factory bjerva2014meaning

ECNU zhao2014ecnu

Mean vectors tai2015improved

DT-RNN socher2014grounded

SDT-RNN socher2014grounded

LSTM tai2015improved

Bidirectional LSTM tai2015improved

Dependency Tree-LSTM tai2015improved

feats socher2011dynamic

RAE+DP socher2011dynamic

RAE+feats socher2011dynamic

RAE+DP+feats socher2011dynamic

FHS finch2005using

WDDP wan2006using

Table 4: Left: Test set results on the SICK semantic relatedness subtask. The evaluation metrics are Pearson’s r, Spearman’s ρ, and mean squared error. The first group of results are SemEval 2014 submissions, while the second group are results reported by tai2015improved. Right: Test set results on the Microsoft Paraphrase Corpus. The evaluation metrics are classification accuracy and F1 score. Top: recursive autoencoder variants. Middle: the best published results on this dataset.

Our first experiment is on the SemEval 2014 Task 1: semantic relatedness SICK dataset marelli2014semeval. Given two sentences, our goal is to produce a score of how semantically related these sentences are, based on human generated scores. Each score is the average of 10 different human annotators. Scores take values between 1 and 5. A score of 1 indicates that the sentence pair is not at all related, while a score of 5 indicates they are highly related. The dataset comes with a predefined split of 4500 training pairs, 500 development pairs and 4927 testing pairs. All sentences are derived from existing image and video annotation datasets. The evaluation metrics are Pearson's $r$, Spearman's $\rho$, and mean squared error.

Given the difficulty of this task, many existing systems employ a large amount of feature engineering and additional resources. Thus, we test how well our learned representations fair against heavily engineered pipelines. Recently, tai2015improved showed that learning representations with LSTM or Tree-LSTM for the task at hand is able to outperform these existing systems. We take this one step further and see how well our vectors learned from a completely different task are able to capture semantic relatedness when only a linear model is used on top to predict scores.

To represent a sentence pair, we use two features. Given two skip-thought vectors $u$ and $v$, we compute their component-wise product $u \cdot v$ and their absolute difference $|{u - v}|$ and concatenate them together. These two features were also used by tai2015improved. To predict a score, we use the same setup as tai2015improved. Let $r^{\top} = {\lbrack 1,\ldots,5\rbrack}$ be an integer vector from 1 to 5. We compute a distribution $p$ as a function of prediction scores $y$ given by $p_{i} = {y - {\lfloor y\rfloor}}$ if $i = {{\lfloor y\rfloor} + 1}$, $p_{i} = {{{\lfloor y\rfloor} - y} + 1}$ if $i = {\lfloor y\rfloor}$ and 0 otherwise. These then become our targets for a logistic regression classifier. At test time, given new sentence pairs we first compute targets $\hat{p}$ and then compute the related score as $r^{\top}\hat{p}$. As an additional comparison, we also explored appending features derived from an image-sentence embedding model trained on COCO (see section 3.4). Given vectors $u$ and $v$, we obtain vectors $u^{\prime}$ and $v^{\prime}$ from the learned linear embedding model and compute features $u^{\prime} \cdot v^{\prime}$ and $|{u^{\prime} - v^{\prime}}|$. These are then concatenated to the existing features.

Table 4 (left) presents our results. First, we observe that our models are able to outperform all previous systems from the SemEval 2014 competition. This is remarkable, given the simplicity of our approach and the lack of feature engineering. It highlights that skip-thought vectors learn representations that are well suited for semantic relatedness. Our results are comparable to LSTMs whose representations are trained from scratch on this task. Only the dependency tree-LSTM of tai2015improved performs better than our results. We note that the dependency tree-LSTM relies on parsers whose training data is very expensive to collect and does not exist for all languages. We also observe using features learned from an image-sentence embedding model on COCO gives an additional performance boost, resulting in a model that performs on par with the dependency tree-LSTM. To get a feel for the model outputs, Table 5 shows example cases of test set pairs. Our model is able to accurately predict relatedness on many challenging cases. On some examples, it fails to pick up on small distinctions that drastically change a sentence meaning, such as tricks on a motorcycle versus tricking a person on a motorcycle.

A little girl is looking at a woman in costume
A young girl is looking at a woman in costume

A little girl is looking at a woman in costume
The little girl is looking at a man in costume

A little girl is looking at a woman in costume
A little girl in costume looks like a woman

A sea turtle is hunting for fish
A sea turtle is hunting for food

A sea turtle is not hunting for fish
A sea turtle is hunting for fish

A man is driving a car
The car is being driven by a man

There is no man driving the car
A man is driving a car

A large duck is flying over a rocky stream
A duck, which is large, is flying over a rocky stream

A large duck is flying over a rocky stream
A large stream is full of rocks, ducks and flies

A person is performing acrobatics on a motorcycle
A person is performing tricks on a motorcycle

A person is performing tricks on a motorcycle
The performer is tricking a person on a motorcycle

Someone is pouring ingredients into a pot
Someone is adding ingredients to a pot

Nobody is pouring ingredients into a pot
Someone is pouring ingredients into a pot

Someone is pouring ingredients into a pot
A man is removing vegetables from a pot

Table 5: Example predictions from the SICK test set. GT is the ground truth relatedness, scored between 1 and 5. The last few results show examples where slight changes in sentence structure result in large changes in relatedness which our model was unable to score correctly.

### Paraphrase detection

The next task we consider is paraphrase detection on the Microsoft Research Paraphrase Corpus dolan2004unsupervised. On this task, two sentences are given and one must predict whether or not they are paraphrases. The training set consists of 4076 sentence pairs (2753 which are positive) and the test set has 1725 pairs (1147 are positive). We compute a vector representing the pair of sentences in the same way as on the SICK dataset, using the component-wise product $u \cdot v$ and their absolute difference $|{u - v}|$ which are then concatenated together. We then train logistic regression on top to predict whether the sentences are paraphrases. Cross-validation is used for tuning the L2 penalty.

As in the semantic relatedness task, paraphrase detection has largely been dominated by extensive feature engineering, or a combination of feature engineering with semantic spaces. We report experiments in two settings: one using the features as above and the other incorporating basic statistics between sentence pairs, the same features used by socher2011dynamic. These are referred to as feats in our results. We isolate the results and baselines used in socher2011dynamic as well as the top published results on this task.

Table 4 (right) presents our results, from which we can observe the following: skip-thoughts alone outperform recursive nets with dynamic pooling when no hand-crafted features are used, when other features are used, recursive nets with dynamic pooling works better, and when skip-thoughts are combined with basic pairwise statistics, it becomes competitive with the state-of-the-art which incorporate much more complicated features and hand-engineering. This is a promising result as many of the sentence pairs have very fine-grained details that signal if they are paraphrases.

### Image-sentence ranking

GMM+HGLMM klein2015associating

m-RNN mao2014deep

Table 6: COCO test-set results for image-sentence retrieval experiments. R@K is Recall@K (high is good). Med r is the median rank (low is good).

We next consider the task of retrieving images and their sentence descriptions. For this experiment, we use the Microsoft COCO dataset lin2014microsoft which is the largest publicly available dataset of images with high-quality sentence descriptions. Each image is annotated with 5 captions, each from different annotators. Following previous work, we consider two tasks: image annotation and image search. For image annotation, an image is presented and sentences are ranked based on how well they describe the query image. The image search task is the reverse: given a caption, we retrieve images that are a good fit to the query. The training set comes with over 80,000 images each with 5 captions. For development and testing we use the same splits as. The development and test sets each contain 1000 images and 5000 captions. Evaluation is performed using Recall@K, namely the mean number of images for which the correct caption is ranked within the top-K retrieved results (and vice-versa for sentences). We also report the median rank of the closest ground truth result from the ranked list.

The best performing results on image-sentence ranking have all used RNNs for encoding sentences, where the sentence representation is learned jointly. Recently, klein2015associating showed that by using Fisher vectors for representing sentences, linear CCA can be applied to obtain performance that is as strong as using RNNs for this task. Thus the method of klein2015associating is a strong baseline to compare our sentence representations with. For our experiments, we represent images using 4096-dimensional OxfordNet features from their 19-layer model simonyan2014very. For sentences, we simply extract skip-thought vectors for each caption. The training objective we use is a pairwise ranking loss that has been previously used by many other methods. The only difference is the scores are computed using only linear transformations of image and sentence inputs. The loss is given by:

where $\mathbf{x}$ is an image vector, $\mathbf{y}$ is the skip-thought vector for the groundtruth sentence, $\mathbf{y}_{k}$ are vectors for constrastive (incorrect) sentences and $s{( \cdot, \cdot )}$ is the image-sentence score. Cosine similarity is used for scoring. The model parameters are $\{\mathbf{U},\mathbf{V}\}$ where $\mathbf{U}$ is the image embedding matrix and $\mathbf{V}$ is the sentence embedding matrix. In our experiments, we use a 1000 dimensional embedding, margin $\alpha = 0.2$ and $k = 50$ contrastive terms. We trained for 15 epochs and saved our model anytime the performance improved on the development set.

Table 6 illustrates our results on this task. Using skip-thought vectors for sentences, we get performance that is on par with both and klein2015associating except for R@1 on image annotation, where other methods perform much better. Our results indicate that skip-thought vectors are representative enough to capture image descriptions without having to learn their representations from scratch. Combined with the results of klein2015associating, it also highlights that simple, scalable embedding techniques perform very well provided that high-quality image and sentence vectors are available.

### Classification benchmarks

For our final quantitative experiments, we report results on several classification benchmarks which are commonly used for evaluating sentence representation learning methods.

We use 5 datasets: movie review sentiment (MR) pang2005seeing, customer product reviews (CR) hu2004mining, subjectivity/objectivity classification (SUBJ) pang2004sentimental, opinion polarity (MPQA) wiebe2005annotating and question-type classification (TREC) li2002learning. On all datasets, we simply extract skip-thought vectors and train a logistic regression classifier on top. 10-fold cross-validation is used for evaluation on the first 4 datasets, while TREC has a pre-defined train/test split. We tune the L2 penality using cross-validation (and thus use a nested cross-validation for the first 4 datasets).

NB-SVM wang2012baselines

MNB wang2012baselines

cBoW zhao2015self

GrConv zhao2015self

RNN zhao2015self

BRNN zhao2015self

CNN kim2014convolutional

AdaSent zhao2015self

Table 7: Classification accuracies on several standard benchmarks. Results are grouped as follows: (a): bag-of-words models; (b): supervised compositional models; (c) Paragraph Vector (unsupervised learning of sentence representations); (d) ours. Best results overall are bold while best results outside of group (b) are underlined.

On these tasks, properly tuned bag-of-words models have been shown to perform exceptionally well. In particular, the NB-SVM of wang2012baselines is a fast and robust performer on these tasks. Skip-thought vectors potentially give an alternative to these baselines being just as fast and easy to use. For an additional comparison, we also see to what effect augmenting skip-thoughts with bigram Naive Bayes (NB) features improves performance ^33^3We use the code available at [https://github.com/mesnilgr/nbsvm](https://github.com/mesnilgr/nbsvm).

Table 7 presents our results. On most tasks, skip-thoughts performs about as well as the bag-of-words baselines but fails to improve over methods whose sentence representations are learned directly for the task at hand. This indicates that for tasks like sentiment classification, tuning the representations, even on small datasets, are likely to perform better than learning a generic unsupervised sentence vector on much bigger datasets. Finally, we observe that the skip-thoughts-NB combination is effective, particularly on MR. This results in a very strong new baseline for text classification: combine skip-thoughts with bag-of-words and train a linear model.

### Visualizing skip-thoughts and generating stories

Figure 2: t-SNE embeddings of skip-thought vectors on different datasets. Points are colored based on their labels (question type for TREC, subjectivity/objectivity for SUBJ). On the SICK dataset, each point represents a sentence pair and points are colored on a gradient based on their relatedness labels. Results best seen in electronic form.

As a final experiment, we applied t-SNE van2008visualizing to skip-thought vectors extracted from TREC, SUBJ and SICK datasets and the visualizations are shown in Figure 2. For the SICK visualization, each point represents a sentence pair, computed using the concatenation of component-wise and absolute difference of features. Remarkably, sentence pairs that are similar to each other are embedded next to other similar pairs. Even without the use of relatedness labels, skip-thought vectors learn to accurately capture this property.

Since our decoder is a neural language model, we can also generate from it. We can perform generation by conditioning on a sentence, generating a new sentence, concatenating the generated example to the previous text and continuing. Since our model was trained on books, the generated samples reads like a novel, albeit a nonsensical one. Below is a 20 sentence sample generated by our model:

she grabbed my hand. " come on. " she fluttered her bag in the air. " i think we 're at your place. i ca n't come get you. " he locked himself back up. " no. she will. " kyrian shook his head. " we met... that congratulations... said no. " the sweat on their fingertips 's deeper from what had done it all of his flesh hard did n't fade. cassie tensed between her arms suddenly grasping him as her sudden her senses returned to its big form. her chin trembled softly as she felt something unreadable in her light. it was dark. my body shook as i lost what i knew and be betrayed and i realize just how it ended. it was n't as if i did n't open a vein. this was all my fault, damaged me. i should have told toby before i was screaming. i should 've told someone that was an accident. never helped it. how can i do this, to steal my baby 's prints ? "

## Conclusion

We evaluated the effectiveness of skip-thought vectors as an off-the-shelf sentence representation with linear classifiers across 8 tasks. Many of the methods we compare against were only evaluated on 1 task. The fact that skip-thought vectors perform well on all tasks considered highlight the robustness of our representations.

We believe our model for learning skip-thought vectors only scratches the surface of possible objectives. Many variations have yet to be explored, including (a) deep encoders and decoders, (b) larger context windows, (c) encoding and decoding paragraphs, (d) other encoders, such as convnets. It is likely the case that more exploration of this space will result in even higher quality representations.
