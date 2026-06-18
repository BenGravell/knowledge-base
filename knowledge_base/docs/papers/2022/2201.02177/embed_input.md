<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Grokking: Generalization beyond Overfitting on Small Algorithmic Datasets

Topics include Neural networks, Deep learning, Datasets, Generalization, Optimization, Learning, Grokking.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we propose to study generalization of neural networks on small algorithmically generated datasets. In this setting, questions about data efficiency, memorization, generalization, and speed of learning can be studied in great detail. In some situations we show that neural networks learn through a process of "grokking" a pattern in the data, improving generalization performance from random chance level to perfect generalization, and that this improvement in generalization can happen well past the point of overfitting. We also study generalization as a function of dataset size and find that smaller datasets require increasing amounts of optimization for generalization. We argue that these datasets provide a fertile ground for studying a poorly understood aspect of deep learning: generalization of overparametrized neural networks beyond memorization of the finite training dataset.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The generalization of overparameterized neural networks has long been a source of interest to the machine learning community since it defies intuitions derived from classical learning theory. In this paper we show that training networks on small algorithmically generated datasets can reliably exhibit unusual generalization patterns, clearly decoupled from performance on the training set, in a significantly more pronounced way than such effects manifest on datasets derived from natural data (see Figure 1, left, for an example). Such experiments can be quickly reproduced on a single GPU, and this makes them convenient testbeds for theories of generalization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The datasets we consider are binary operation tables of the form ${a \circ b} = c$ where $a,b,c$ are discrete symbols with no internal structure, and $\circ$ is a binary operation. Examples of binary operations include addition, composition of permutations, and bivariate polynomials. Training a neural network on a proper subset of all possible equations then amounts to filling in the blanks of the binary op table, much like solving a Sudoku puzzle. An example is shown on the right in Figure 1. Since we use distinct abstract symbols for all distinct elements $a,b,c$ involved in the equations, the network is not made aware of any internal structure of the elements, and has to learn about their properties only from their interactions with other elements. For example the network doesn't see numbers in decimal notation, or permutations in line notation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that neural networks are capable of generalizing to the empty slots in a variety of binary op tables.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that, long after severely overfitting, validation accuracy sometimes suddenly begins to increase from chance level toward perfect generalization. We call this phenomenon 'grokking'. An example is shown in Figure 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present the data efficiency curves for a variety of binary operations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show empirically that the amount of optimization required for generalization quickly increases as the dataset size decreases.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We compare various optimization details to measure their impact on data efficiency. We find that weight decay is particularly effective at improving generalization on the tasks we study.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We visualize the symbol embeddings learned by these networks and find that they sometimes uncover recognizable structure of the mathematical objects represented by the symbols.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

All of our experiments used a small transformer trained on datasets of equations of the form ${a \circ b} = c$, where each of "$a$", "$\circ$", "$b$", "$=$", and "$c$" is a separate token. Details of the operations studied, the architecture, training hyperparameters and tokenization can be found in Appendix A.1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Generalization beyond overfitting", "weight": 1.0} -->

Deep learning practitioners are used to seeing small improvements in validation accuracy after validation loss stops decreasing. A double descent of validation loss has been documented in some circumstances, but is considered unusual among practitioners Nakkiran et al.; Belkin et al.; d'Ascoli et al.. On the small algorithmic datasets that we study, improved generalization after initial overfitting occurs for a range of models, optimizers, and dataset sizes, and in some cases these effects are extremely pronounced. A typical example is shown for modular division in Figure 1. There we see that validation accuracy starts increasing beyond chance level only after 1000 times more optimization steps than are required for training accuracy to get close to optimal. In Figure 4 the training/validation losses are also plotted and we see the double descent of the validation loss.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Generalization beyond overfitting", "weight": 1.0} -->

We found these behaviors to be typical for all the binary operations for dataset sizes that were close to the minimal dataset size for which the network generalized within the allotted optimization budget. For larger dataset sizes, the training and validation curves tend to track each other more closely.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning time curves", "weight": 1.0} -->

In a typical supervised learning problem, decreasing the amount of training data decreases the converged generalization performance of the model when the optimization procedure is capable of interpolating the training data. In our setting, we observe a different phenomenon: while the converged performance stays constant at 100% within a range of training dataset sizes, the optimization time required to achieve that performance grows quicky as the dataset size is decreased.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Grokking on a variety of problems", "weight": 1.0} -->

We've measured the mean accuracy across three runs for training datasets consisting of different fractions of all available equations for a variety of binary operations listed in Appendix A.1.1. The results are presented in Figure 2 (right).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Grokking on a variety of problems", "weight": 1.0} -->

Since the operands are presented to the neural network as unrelated abstract symbols, the operations ${x + y}\mspace{17mu}{({\operatorname{mod}{p - 1}})}$ and ${x \ast y}\mspace{17mu}{({\operatorname{mod}p})}$ with a prime number $p$ and non-zero $x,y$ are indistinguishable from the neural network's perspective (and similarly ${x - y}\mspace{17mu}{({\operatorname{mod}{p - 1}})}$ and ${x/y}\mspace{17mu}{({\operatorname{mod}p})}$). This is because every nonzero residue modulo a prime can be represented as a power of a primitive root. This representation shows the equivalence (up to renaming of symbols) of modular addition modulo $p - 1$ and modular multiplication modulo $p$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Grokking on a variety of problems", "weight": 1.0} -->

We see in Figure 2 (right) that $x - y$ and $x/y$ indeed take about the same amount of data for generalization to occur.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Grokking on a variety of problems", "weight": 1.0} -->

Some of the operations listed in Figure 2 (right) are symmetric with respect to the order of the operands ($x + y$, $x \ast y$, $x^{2} + y^{2}$ and $x^{2} + {xy} + y^{2}$). Such operations tend to require less data for generalization than closely related non-symmetrical counterparts ($x - y$, $x/y$, $x^{2} + {xy} + y^{2} + x$). We believe this effect might be partially architecture-dependent, since it's easy for a transformer to learn a symmetric function of the operands by ignoring positional embedding.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Grokking on a variety of problems", "weight": 1.0} -->

Some operations (for example ${x^{3} + {xy^{2}} + y}\mspace{17mu}{({\operatorname{mod}97})}$) didn't lead to generalization within the allowed optimization budget at any percentage of data up to 95%. The converged models effectively just memorized the training dataset without finding any real patterns in the data. To such a model, the data is effectively random.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Grokking on a variety of problems", "weight": 1.0} -->

The operation $\lbrack x/y{({\operatorname{mod}p})}\text{~if~}y\text{~is odd, otherwise~}x - y{({\operatorname{mod}p})}\rbrack$ requires the network to learn a mix of several simple operations - in particular the role of $x$ has to be interpreted as a residue in the additive group when it's paired with an even $y$, and as a residue in the multiplicative group when it's paired with an odd $y$. This shows that generalization can happen even for operations that are not cleanly interpretable via group or ring operations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Ablations and Tricks", "weight": 1.0} -->

We've tried various forms of regularization to see what can induce networks to generalize better on our datasets. Here we present the data efficiency curves on a particular dataset $S_{5}$ for a variety of interventions: full-batch gradient descent, stochastic gradient descent, large or small learning rates, residual dropout Srivastava et al., weight decay Loshchilov & Hutter and gradient noise Neelakantan et al.. The results are shown in Figure 2 (left).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Ablations and Tricks", "weight": 1.0} -->

We find that adding weight decay has a very large effect on data efficiency, more than halving the amount of samples needed compared to most other interventions. We found that weight decay towards the initialization of the network is also effective, but not quite as effective as weight decay towards the origin. This makes us believe that the prior, that approximately zero weights are suitable for small algorithmic tasks, explains part, but not all of the superior performance of weight decay. Adding some noise to the optimization process (e.g. gradient noise from using minibatches, Gaussian noise applied to weights before or after computing the gradients) is beneficial for generalization, consistent with the idea that such noise might induce the optimization to find flatter minima that generalize better. We found that learning rate had to be tuned in a relatively narrow window for the generalization to happen (within 1 order of magnitude).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Qualitative Visualization of Embeddings", "weight": 1.0} -->

In order to gain some insight into networks that generalize, we visualized the matrix of the output layer for the case of modular addition and $S_{5}$. In Figure 3 we show t-SNE plots of the row vectors. For some networks we find clear reflections of the structure of the underlying mathematical objects in the plots. For example the circular topology of modular addition is shown with a 'number line' formed by adding 8 to each element. The structure is more apparent in networks that were optimized with weight decay.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have seen that in the datasets we studied, small algorithmic binary operation tables, effects such as double descent or late generalization, and improvements to generalization from interventions like weight decay can be striking. This suggests that these datasets could be a good place to investigate aspects of generalization. For example, we plan to test whether various proposed measures of minima flatness correlate with generalization in our setting.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have also seen that visualizing the embedding spaces of these neural networks can show natural kinds of structure, for example in problems of modular arithmetic the topology of the embeddings tends to be circles or cylinders. We also see that the network tends to idiosyncratically organize the embeddings by various residues. Whilst the properties of these mathematical objects are familiar to us, we speculate that such visualizations could one day be a useful way to gain intuitions about novel mathematical objects.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Discussion", "weight": 1.5} -->

In addition, we document an interesting phenomenon, where the number of optimization steps needed to reach a given level of performance increases quickly as we reduce the size of the training dataset. Since this represents a way trade compute for performance on smaller amounts of data, it would be useful to investigate in future work whether the effect is also present for other datasets.
