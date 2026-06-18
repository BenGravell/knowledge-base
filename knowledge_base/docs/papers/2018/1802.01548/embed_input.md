<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regularized Evolution for Image Classifier Architecture Search

Topics include Reinforcement learning, Neural networks, Classifiers, Accuracy, Control, Learning, Tournament selection, Evolutionary algorithms.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The effort devoted to hand-crafting neural network image classifiers has motivated the use of architecture search to discover them automatically. Although evolutionary algorithms have been repeatedly applied to neural network topologies, the image classifiers thus discovered have remained inferior to human-crafted ones. Here, we evolve an image classifier - AmoebaNet-A - that surpasses hand-designs for the first time. To do this, we modify the tournament selection evolutionary algorithm by introducing an age property to favor the younger genotypes. Matching size, AmoebaNet-A has comparable accuracy to current state-of-the-art ImageNet models discovered with more complex architecture-search methods. Scaled to larger size, AmoebaNet-A sets a new state-of-the-art 83.9% / 96.6% top-5 ImageNet accuracy. In a controlled comparison against a well known reinforcement learning algorithm, we give evidence that evolution can obtain results faster with the same hardware, especially at the earlier stages of the search. This is relevant when fewer compute resources are available. Evolution is, thus, a simple method to effectively discover high-quality architectures.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

^00^footnotetext: Accepted for publication at AAAI 2019, the Thirty-Third AAAI Conference on Artificial Intelligence.^00^footnotetext: A brief talk from Nov 2018 summarizes this paper at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Until recently, most state-of-the-art image classifier architectures have been manually designed by human experts. To speed up the process, researchers have looked into automated methods. These methods are now collectively known as architecture-search algorithms. A traditional approach is neuro-evolution of topologies. Improved hardware now allows scaling up evolution to produce high-quality image classifiers. Yet, the architectures produced by evolutionary algorithms / genetic programming have not reached the accuracy of those directly designed by human experts. Here we evolve image classifiers that surpass hand-designs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To do this, we make two additions to the standard evolutionary process. First, we propose a change to the well-established tournament selection evolutionary algorithm that we refer to as aging evolution or regularized evolution. Whereas in tournament selection, the best genotypes (architectures) are kept, we propose to associate each genotype with an age, and bias the tournament selection to choose the younger genotypes. We will show that this change turns out to make a difference. The connection to regularization will be clarified in the Discussion section. Second, we implement the simplest set of mutations that would allow evolving in the NASNet search space. This search space associates convolutional neural network architectures with small directed graphs in which vertices represent hidden states and labeled edges represent common network operations (such as convolutions or pooling layers). Our mutation rules only alter architectures by randomly reconnecting the origin of edges to different vertices and by randomly relabeling the edges, covering the full search space.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Searching in the NASNet space allows a controlled comparison between evolution and the original method for which it was designed, reinforcement learning (RL). Thus, this paper presents the first comparative case study of architecture-search algorithms for the image classification task. Within this case study, we will demonstrate that evolution can attain similar results with a simpler method, as will be shown in the Discussion section. In particular, we will highlight that in all our experiments evolution searched faster than RL and random search, especially at the earlier stages, which is important when experiments cannot be run for long times due to compute resource limitations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its simplicity, our approach works well in our benchmark against RL. It also evolved a high-quality model, which we name AmoebaNet-A. This model is competitive with the best image classifiers obtained by any other algorithm today at similar sizes (82.8% top-1 / 96.1% top-5 ImageNet accuracy). When scaled up, it sets a new state-of-the-art accuracy (83.9% top-1 / 96.6% top-5 ImageNet accuracy)^11^1After our submission, a recent preprint has further scaled up and retrained AmoebaNet-A to reach 84.3% top-1 / 97.0% top-5 ImageNet accuracy..

<!-- chunk {"id": "body-0008", "role": "body", "section": "Methods", "weight": 1.0} -->

This section contains a readable description of the methods. The Methods Details section gives additional information.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Search Space", "weight": 1.0} -->

All experiments use the NASNet search space. This is a space of image classifiers, all of which have the fixed outer structure indicated in Figure 1 (left): a feed-forward stack of Inception-like modules called cells. Each cell receives a direct input from the previous cell (as depicted) and a skip input from the cell before it (Figure 1, middle). The cells in the stack are of two types: the normal cell and the reduction cell. All normal cells are constrained to have the same architecture, as are reduction cells, but the architecture of the normal cells is independent of that of the reduction cells. Other than this, the only difference between them is that every application of the reduction cell is followed by a stride of 2 that reduces the image size, whereas normal cells preserve the image size. As can be seen in the figure, normal cells are arranged in three stacks of N cells. The goal of the architecture-search process is to discover the architectures of the normal and reduction cells.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Search Space", "weight": 1.0} -->

As depicted in Figure 1 (middle and right), each cell has two input activation tensors and one output. The very first cell takes two copies of the input image. After that, the inputs are the outputs of the previous two cells.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Search Space", "weight": 1.0} -->

Both normal and reduction cells must conform to the following construction. The two cell input tensors are considered hidden states "0" and "1". More hidden states are then constructed through pairwise combinations. A pairwise combination is depicted in Figure 1 (right, inside dashed circle). It consists in applying an operation (or op) to an existing hidden state, applying another op to another existing hidden state, and adding the results to produce a new hidden state. Ops belong to a fixed set of common convnet operations such as convolutions and pooling layers. Repeating hidden states or operations within a combination is permitted. In the cell example of Figure 1 (right), the first pairwise combination applies a 3x3 average pool op to hidden state 0 and a 3x3 max pool op to hidden state 1, in order to produce hidden state 2. The next pairwise combination can now choose from hidden states 0, 1, and 2 to produce hidden state 3 (chose 0 and 1 in Figure 1), and so. After exactly five pairwise combinations, any hidden states that remain unused (hidden states 5 and 6 in Figure 1) are concatenated to form the output of the cell (hidden state 7).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Search Space", "weight": 1.0} -->

A given architecture is fully specified by the five pairwise combinations that make up the normal cell and the five that make up the reduction cell. Once the architecture is specified, the model still has two free parameters that can be used to alter its size (and its accuracy): the number of normal cells per stack (N) and the number of output filters of the convolution ops (F). N and F are determined manually.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

The evolutionary method we used is summarized in Algorithm 1. It keeps a population of P trained models throughout the experiment. The population is initialized with models with random architectures ("while $\left| {population} \right|$" in Algorithm 1). All architectures that conform to the search space described are possible and equally likely.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

p o p u l a t i o n← empty queue ⊳ The population.
h i s t o r y ← ⌀ ⊳ Will contain all models.
while |p o p u l a t i o n| &lt; P do ⊳ Initialize population.
model.accuracy ← TrainAndEval(model.arch)
while |h i s t o r y| &lt; C do ⊳ Evolve for C cycles.
c a n d i d a t e← random element from p o p u l a t i o n
⊳ The element stays in the p o p u l a t i o n.
child.arch ← Mutate(parent.arch)
child.accuracy ← TrainAndEval(child.arch)
remove d e a d from left of p o p u l a t i o n ⊳ Oldest.
return highest-accuracy model in h i s t o r y
Algorithm 1 Aging Evolution

<!-- chunk {"id": "body-0015", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

After this, evolution improves the initial population in cycles ("while $\left| {history} \right|$" in Algorithm 1). At each cycle, it samples S random models from the population, each drawn uniformly at random with replacement. The model with the highest validation fitness within this sample is selected as the parent. A new architecture, called the child, is constructed from the parent by the application of a transformation called a mutation. A mutation causes a simple and random modification of the architecture and is described in detail below. Once the child architecture is constructed, it is then trained, evaluated, and added to the population. This process is called tournament selection.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

It is common in tournament selection to keep the population size fixed at the initial value P. This is often accomplished with an additional step within each cycle: discarding (or killing) the worst model in the random S-sample. We will refer to this approach as non-aging evolution. In contrast, in this paper we prefer a novel approach: killing the oldest model in the population---that is, removing from the population the model that was trained the earliest ("remove dead from left of pop" in Algorithm 1). This favors the newer models in the population. We will refer to this approach as aging evolution. In the context of architecture search, aging evolution allows us to explore the search space more, instead of zooming in on good models too early, as non-aging evolution would (see Discussion section for details).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

In practice, this algorithm is parallelized by distributing the "while $\left| {history} \right|$" loop in Algorithm 1 over multiple workers. A full implementation can be found online.^22^2 Intuitively, the mutations can be thought of as providing exploration, while the parent selection provides exploitation. The parameter $S$ controls the aggressiveness of the exploitation: $S = 1$ reduces to a type of random search and $2 \leq S \leq P$ leads to evolution of varying greediness.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

New models are constructed by applying a mutation to existing models, transforming their architectures in random ways. To navigate the NASNet search space described above, we use two main mutations that we call the hidden state mutation and the op mutation. A third mutation, the identity, is also possible. Only one of these mutations is applied in each cycle, choosing between them at random.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

The hidden state mutation consists of first making a random choice of whether to modify the normal cell or the reduction cell. Once a cell is chosen, the mutation picks one of the five pairwise combinations uniformly at random. Once the pairwise combination is picked, one of the two elements of the pair is chosen uniformly at random. The chosen element has one hidden state. This hidden state is now replaced with another hidden state from within the cell, subject to the constraint that no loops are formed (to keep the feed-forward nature of the convnet). Figure 2 (top) shows an example.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Evolutionary Algorithm", "weight": 1.0} -->

The op mutation behaves like the hidden state mutation as far as choosing one of the two cells, one of the five pairwise combinations, and one of the two elements of the pair. Then it differs in that it modifies the op instead of the hidden state. It does this by replacing the existing op with a random choice from a fixed list of ops (see Methods Details). Figure 2 (bottom) shows an example.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Baseline Algorithms", "weight": 1.0} -->

Our main baseline is the application of RL to the same search space. RL was implemented using the algorithm and code in the baseline study. An LSTM controller outputs the architectures, constructing the pairwise combinations one at a time, and then gets a reward for each architecture by training and evaluating it. More detail can be found in the baseline study. We also compared against random search (RS). In our RS implementation, each model is constructed randomly so that all models in the search space are equally likely, as in the initial population in the evolutionary algorithm. In other words, the models in RS experiments are not constructed by mutating existing models, so as to make new models independent from previous ones.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We ran controlled comparisons at scale, ensuring identical conditions for evolution, RL and random search (RS). In particular, all methods used the same computer code for network construction, training and evaluation. Experiments always searched on the CIFAR-10 dataset.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

As in the baseline study, we first performed architecture search over small models (*i.e*. small N and F) until 20k models were evaluated. After that, we used the model augmentation trick: we took architectures discovered by the search (*e.g*. the output of an evolutionary experiment) and turn them into a full-size, accurate models. To accomplish this, we enlarged the models by increasing N and F so the resulting model sizes would match the baselines, and we trained the enlarged models for a longer time on the CIFAR-10 or the ImageNet classification datasets. For ImageNet, a stem was added at the input of the model to reduce the image size, as shown in Figure 5 (left). This is the same procedure as in the baseline study. To produce the largest model (see last paragraph of Results section; not included in tables), we increased N and F until we ran out of memory. Actual values of N and F for all models are listed in the Methods Details section.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Methods Details", "weight": 1.0} -->

This section complements the Methods section with the details necessary to reproduce our experiments. Possible ops: none (identity); 3x3, 5x5 and 7x7 separable (sep.) convolutions (convs.); 3x3 average (avg.) pool; 3x3 max pool; 3x3 dilated (dil.) sep. conv.; 1x7 then 7x1 conv. Evolved with $P$=$100$, $S$=$25$. CIFAR-10 dataset with 5k withheld examples for validation. Standard ImageNet dataset, 1.2M 331x331 images and 1k classes; 50k examples withheld for validation; standard validation set used for testing. During the search phase, each model trained for 25 epochs; N=3/F=24, 1 GPU. Each experiment ran on 450 K40 GPUs for 20k models (approx. 7 days). To optimize evolution, we tried 5 configurations with P/S of: 100/2, 100/50, 20/20, 100/25, 64/16, best was 100/25.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Methods Details", "weight": 1.0} -->

The probability of the identity mutation was fixed at the small, arbitrary value of 0.05 and was not tuned. Other mutation probabilities were uniform, as described in the Methods. To optimize RL, started with parameters already tuned in the baseline study and further optimized learning rate in 8 configurations: 0.00003, 0.00006, 0.00012, 0.0002, 0.0004, 0.0008, 0.0016, 0.0032; best was 0.0008. To avoid selection bias, plots do not include optimization runs, as was decided a priori. Best few models were selected from each experiment and augmented to N=6/F=32, as in baseline study; batch 128, SGD with momentum rate 0.9, L2 weight decay $5 \times 10^{- 4}$, initial lr 0.024 with cosine decay, 600 epochs, ScheduledDropPath to 0.7 prob; auxiliary softmax with half-weight of main softmax. For Table 1, we used N/F of 6/32 and 6/36.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Methods Details", "weight": 1.0} -->

For ImageNet table, N/F were 6/190 and 6/448 and standard training methods: distributed sync SGD with 100 P100 GPUs; RMSProp optimizer with 0.9 decay and $\epsilon$=0.1, $4 \times 10^{- 5}$ weight decay, 0.1 label smoothing, auxiliary softmax weighted by 0.4; dropout probability 0.5; ScheduledDropPath to 0.7 probability (as in baseline---note that this trick only contributes 0.3% top-1 ImageNet acc.); 0.001 initial lr, decaying every 2 epochs by 0.97. Largest model used N=6/F=448. F always refers to the number of filters of convolutions in the first stack; after each reduction cell, this number is doubled. Wherever applicable, we used the same conditions as the baseline study.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison With RL and RS Baselines", "weight": 1.0} -->

Currently, reinforcement learning (RL) is the predominant method for architecture search. In fact, today's state-of-the-art image classifiers have been obtained by architecture search with RL. Here we seek to compare our evolutionary approach against their RL algorithm. We performed large-scale side-by-side architecture-search experiments on CIFAR-10. We first optimized the hyper-parameters of the two approaches independently (details in Methods Details section). Then we ran 5 repeats of each of the two algorithms---and also of random search (RS).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparison With RL and RS Baselines", "weight": 1.0} -->

As in the baseline study, the architecture-search experiments above were performed over small models, to be able to train them quicker. We then used the model augmentation trick by which we take an architecture discovered by the search (*e.g*. the output of an evolutionary experiment) and turn it into a full-size, accurate model, as described in the Methods.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Comparison With RL and RS Baselines", "weight": 1.0} -->

So far we have been comparing evolution with our reproduction of the experiments in the baseline study, but it is also informative to compare directly against the results reported by the baseline study. We select our evolved architecture with highest validation accuracy and call it AmoebaNet-A (Figure 5). Table 1 compares its test accuracy with the top model of the baseline study, NASNet-A. Such a comparison is not entirely controlled, as we have no way of ensuring the network training code was identical and that the same number of experiments were done to obtain the final model. The table summarizes the results of training AmoebaNet-A at sizes comparable to a NASNet-A version, showing that AmoebaNet-A is slightly more accurate (when matching model size) or considerably smaller (when matching accuracy). We did not train our model at larger sizes on CIFAR-10. Instead, we moved to ImageNet to do further comparisons in the next section.

<!-- chunk {"id": "body-0030", "role": "body", "section": "ImageNet Results", "weight": 1.0} -->

Following the accepted standard, we compare our top model's classification accuracy on the popular ImageNet dataset against other top models from the literature. Again, we use AmoebaNet-A, the model with the highest validation accuracy on CIFAR-10 among our evolution experiments. We highlight that the model was evolved on CIFAR-10 and then transferred to ImageNet, so the evolved architecture cannot have overfit the ImageNet dataset. When re-trained on ImageNet, AmoebaNet-A performs comparably to the baseline for the same number of parameters (Table 2, model with F=190).

<!-- chunk {"id": "body-0031", "role": "body", "section": "ImageNet Results", "weight": 1.0} -->

## Parameters
## Multiply-Adds
Top-1 / Top-5 Accuracy (%)

<!-- chunk {"id": "body-0032", "role": "body", "section": "ImageNet Results", "weight": 1.0} -->

Finally, we focused on AmoebaNet-A exclusively and enlarged it, setting a new state-of-the-art accuracy on ImageNet of 83.9%/96.6% top-1/5 accuracy with 469M parameters (Table 2, model with F=448). Such high parameter counts may be beneficial in training other models too but we have not managed to do this yet.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

This section will suggest directions for future work, which we will motivate by speculating about the evolutionary process and by summarizing additional minor results. The details of these minor results have been relegated to the supplements, as they are not necessary to understand or reproduce our main results above.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

Scope of results. Some of our findings may be restricted to the search spaces and datasets we used. A natural direction for future work is to extend the controlled comparison to more search spaces, datasets, and tasks, to verify generality, or to more algorithms. Supplement A presents preliminary results, performing evolutionary and RL searches over three search spaces (SP-I: same as in the Results section; SP-II: like SP-I but with more possible ops; SP-III: like SP-II but with more pairwise combinations) and three datasets (gray-scale CIFAR-10, MNIST, and gray-scale ImageNet), at a small-compute scale (on CPU, $F$=$8$, $N$=$1$). Evolution reached equal or better accuracy in all cases (Figure 6, top).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

Algorithm speed. In our comparison study, Figure 3 suggested that both RL and evolution are approaching a common accuracy asymptote. That raises the question of which algorithm gets there faster. The plots indicate that evolution reaches half-maximum accuracy in roughly half the time. We abstain, nevertheless, from further quantifying this effect since it depends strongly on how speed is measured (the number of models necessary to reach accuracy $a$ depends on $a$; the natural choice of $a = {a_{max}/2}$ may be too low to be informative; *etc*.). Algorithm speed may be more important when exploring larger spaces, where reaching the optimum can require more compute than is available. We saw an example of this in the SP-III space, where evolution stood out (Figure 6, bottom-right). Therefore, future work could explore evolving on even larger spaces.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

Model speed. The speed of individual models produced is also relevant. Figure 4 demonstrated that evolved models are faster (lower FLOPs). We speculate that asynchronous evolution may be reducing the FLOPs because it is indirectly optimizing for speed even when training for a fixed number of epochs: fast models may do well because they "reproduce" quickly even if they initially lack the higher accuracy of their slower peers. Verifying this speculation could be the subject of future work. As mentioned in the Related Work section, in this work we only considered asynchronous algorithms (as opposed to generational evolutionary methods) to ensure high resource utilization. Future work may explore how asynchronous and generational algorithms compare with regard to model accuracy.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

Benefits of aging evolution. Aging evolution seemed advantageous in additional small-compute-scale experiments, shown in Figure 7 and presented in more detail in Supplement B. These were carried out on CPU instead of GPU, and used a gray-scale version of CIFAR-10, to reduce compute requirements. In the supplement, we also show that these results tend to hold when varying the dataset or the search space.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

Understanding aging evolution and regularization. We can speculate that aging may help navigate the training noise in evolutionary experiments, as follows. Noisy training means that models may sometimes reach high accuracy just by luck. In non-aging evolution (NAE, *i.e*. standard tournament selection), such lucky models may remain in the population for a long time---even for the whole experiment. One lucky model, therefore, can produce many children, causing the algorithm to focus on it, reducing exploration. Under aging evolution (AE), on the other hand, all models have a short lifespan, so the population is wholly renewed frequently, leading to more diversity and more exploration. In addition, another effect may be in play, which we describe next. In AE, because models die quickly, the only way an architecture can remain in the population for a long time is by being passed down from parent to child through the generations. Each time an architecture is inherited it must be re-trained. If it produces an inaccurate model when re-trained, that model is not selected by evolution and the architecture disappears from the population. The only way for an architecture to remain in the population for a long time is to re-train well repeatedly.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

In other words, AE can only improve a population through the inheritance of architectures that re-train well. (In contrast, NAE can improve a population by accumulating architectures/models that were lucky when they trained the first time). That is, AE is forced to pay attention to architectures rather than models. In other words, the addition of aging involves introducing additional information to the evolutionary process: architectures should re-train well. This additional information prevents overfitting to the training noise, which makes it a form of regularization in the broader mathematical sense^33^3 Regardless of the exact mechanism, in Supplement C we perform experiments to verify the plausibility of the conjecture that aging helps navigate noise. There we construct a toy search space where the only difficulty is a noisy evaluation. If our conjecture is true, AE should be better in that toy space too. We found this to be the case. We leave further verification of the conjecture to future work, noting that theoretical results may prove useful here.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

Simplicity of aging evolution. A desirable feature of evolutionary algorithms is their simplicity. By design, the application of a mutation causes a random change. The process of constructing new architectures, therefore, is entirely random. What makes evolution different from random search is that only the good models are selected to be mutated. This selection tends to improve the population over time. In this sense, evolution is simply "random search plus selection". In outline, the process can be described briefly: "keep a population of N models and proceed in cycles: at each cycle, copy-mutate the best of S random models and kill the oldest in the population". Implementation-wise, we believe the methods of this paper are sufficient for a reader to understand evolution. The sophisticated nature of the RL alternative introduces complexity in its implementation: it requires back-propagation and poses challenges to parallelization. Even different implementations of the same algorithm have been shown to produce different results. Finally, evolution is also simple in that it has few meta-parameters, most of which do not need tuning. In our study, we only adjusted 2 meta-parameters and only through a handful of attempts (see Methods Details section).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

In contrast, note that the RL baseline requires training an agent/controller which is often itself a neural network with many weights (such as an LSTM), and its optimization has more meta-parameters to adjust: learning rate schedule, greediness, batching, replay buffer, *etc*. (These meta-parameters are all in addition to the weights and training parameters of the image classifiers being searched, which are present in both approaches.) It is possible that through careful tuning, RL could be made to produce even better models than evolution, but such tuning would likely involve running many experiments, making it more costly. Evolution did not require much tuning, as described. It is also possible that random search would produce equally good models if run for a very long time, which would be very costly.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

Interpreting architecture search. Another important direction for future work is that of analyzing architecture-search experiments (regardless of the algorithm used) to try to discover new neural network design patterns. Anecdotally, for example, we found that architectures with high output vertex fan-in (number of edges into the output vertex) tend to be favored in all our experiments. In fact, the models in the final evolved populations have a mean fan-in value that is 3 standard deviations above what would be expected from randomly generated models. We verified this pattern by training various models with different fan-in values and the results confirm that accuracy increases with fan-, as had been found in ResNeXt. Discovering broader patterns may require designing search spaces specifically for this purpose.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

Additional AmoebaNets. Using variants of the evolutionary process described, we obtained three additional models, which we named AmoebaNet-B, AmoebaNet-C, and AmoebaNet-D. We describe these models and the process that led to them in detail in Supplement D, but we summarize here. AmoebaNet-B was obtained through through platform-aware architecture search over a larger version of the NASNet space. AmoebaNet-C is simply a model that showed promise early on in the above experiments by reaching high accuracy with relatively few parameters; we mention it here for completeness, as it has been referenced in other work. AmoebaNet-D was obtained by manually extrapolating the evolutionary process and optimizing the resulting architecture for training speed. It is very efficient: AmoebaNet-D won the Stanford DAWNBench competition for lowest training cost on ImageNet.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper used an evolutionary algorithm to discover image classifier architectures.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed aging evolution, a variant of tournament selection by which genotypes die according to their age, favoring the young. This improved upon standard tournament selection while still allowing for efficiency at scale through asynchronous population updating. We open-sourced the code.^44^4 We also implemented simple mutations that permit the application of evolution to the popular NASNet search space.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented the first controlled comparison of algorithms for image classifier architecture search in a case study of evolution, RL and random search. We showed that evolution had somewhat faster search speed and stood out in the regime of scarcer resources / early stopping. Evolution also matched RL in final model quality, employing a simpler method.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We evolved AmoebaNet-A (Figure 5), a competitive image classifier. On ImageNet, it is the first evolved model to surpass hand-designs. Matching size, AmoebaNet-A has comparable accuracy to top image-classifiers discovered with other architecture-search methods. At large size, it sets a new state-of-the-art accuracy. We open-sourced code and checkpoint.^55^5
