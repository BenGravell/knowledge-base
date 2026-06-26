<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Smoother Way to Train Structured Prediction Models

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a framework to train a structured prediction model by performing smoothing on the inference algorithm it builds upon. Smoothing overcomes the non-smoothness inherent to the maximum margin structured prediction objective, and paves the way for the use of fast primal gradient-based optimization algorithms. We illustrate the proposed framework by developing a novel primal incremental optimization algorithm for the structural support vector machine. The proposed algorithm blends an extrapolation scheme for acceleration and an adaptive smoothing scheme and builds upon the stochastic variance-reduced gradient algorithm. We establish its worst-case global complexity bound and study several practical variants, including extensions to deep structured prediction. We present experimental results on two real-world problems, namely named entity recognition and visual object localization. The experimental results show that the proposed framework allows us to build upon efficient inference algorithms to develop large-scale optimization algorithms for structured prediction which can achieve competitive performance on the two real-world problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider the optimization problem arising when training maximum margin structured prediction models: where each $f^{(i)}$ is the structural hinge loss. Max-margin structured prediction was designed to forecast discrete data structures such as sequences and trees.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Batch non-smooth optimization algorithms such as cutting plane methods are appropriate for problems with small or moderate sample sizes. Stochastic non-smooth optimization algorithms such as stochastic subgradient methods can tackle problems with large sample sizes. However, both families of methods achieve the typical worst-case complexity bounds of non-smooth optimization algorithms and cannot easily leverage a possible hidden smoothness of the objective.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, as significant progress is being made on incremental smooth optimization algorithms for training unstructured prediction models, we would like to transfer such advances and design faster optimization algorithms to train structured prediction models. Indeed if each term in the finite-sum were $L$-smooth, incremental optimization algorithms such as MISO, SAG, SAGA, SDCA, and SVRG could leverage the finite-sum structure of the objective and achieve faster convergence than batch algorithms on large-scale problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Incremental optimization algorithms can be further accelerated, either on a case-by-case basis or using the Catalyst acceleration scheme, to achieve near-optimal convergence rates. Accelerated incremental optimization algorithms demonstrate stable and fast convergence behavior on a wide range of problems, in particular for ill-conditioned ones.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a general framework that allows us to bring the power of accelerated incremental optimization algorithms to the realm of structured prediction problems. To illustrate our framework, we focus on the problem of training a structural support vector machine (SSVM), and extend the developed algorithms to deep structured prediction models with nonlinear mappings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We seek primal optimization algorithms, as opposed to saddle-point or primal-dual optimization algorithms, in order to be able to tackle structured prediction models with affine mappings such as SSVM as well as deep structured prediction models with nonlinear mappings. We show how to shade off the inherent non-smoothness of the objective while still being able to rely on efficient inference algorithms.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Smooth Inference Oracles.: We introduce a notion of smooth inference oracles that gracefully fits the framework of black-box first-order optimization. While the exp inference oracle reveals the relationship between max-margin and probabilistic structured prediction models, the top-$K$ inference oracle can be efficiently computed using simple modifications of efficient inference algorithms in many cases of interest.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Incremental Optimization Algorithms.: We present a new algorithm built on top of SVRG, blending an extrapolation scheme for acceleration and an adaptive smoothing scheme. We establish the worst-case complexity bounds of the proposed algorithm and extend it to the case of non-linear mappings. Finally, we demonstrate its effectiveness compared to competing algorithms on two tasks, namely named entity recognition and visual object localization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The code is publicly available as a software library called Casimir^11^1 The outline of the paper is as follows: Sec. 1.1 reviews related work. Sec. 2 discusses smoothing for structured prediction followed by Sec. 3, which defines and studies the properties of inference oracles and Sec. 4, which describes the concrete implementation of these inference oracles in several settings of interest. Then, we switch gears to study accelerated incremental algorithms in convex case (Sec. 5) and their extensions to deep structured prediction (Sec. 6). Finally, we evaluate the proposed algorithms on two tasks, namely named entity recognition and visual object localization in Sec. 7.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimization for Structural Support Vector Machines", "weight": 1.0} -->

Table 1 gives an overview of different optimization algorithms designed for structural support vector machines. Early works considered batch dual quadratic optimization (QP) algorithms. The stochastic subgradient method operated directly on the non-smooth primal formulation. More recently, Lacoste-Julien et al. proposed a block coordinate Frank-Wolfe (BCFW) algorithm to optimize the dual formulation of structural support vector machines; see also Osokin et al. for variants and extensions. Saddle-point or primal-dual approaches include the mirror-prox algorithm. Palaniappan and Bach propose an incremental optimization algorithm for saddle-point problems. However, it is unclear how to extend it to the structured prediction problems considered here. Incremental optimization algorithms for conditional random fields were proposed by Schmidt et al.. We focus here on primal optimization algorithms in order to be able to train structured prediction models with affine or nonlinear mappings with a unified approach, and on incremental optimization algorithms which can scale to large datasets.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Inference", "weight": 1.0} -->

The ideas of dynamic programming inference in tree structured graphical models have been around since the pioneering works of Pearl and Dawid. Other techniques emerged based on graph cuts, bipartite matchings and search algorithms. For graphical models that admit no such a discrete structure, techniques based on loopy belief propagation, linear programming (LP), dual decomposition and variational inference gained popularity.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Top-$K$ Inference", "weight": 1.0} -->

Smooth inference oracles with $\ell_{2}^{2}$ smoothing echo older heuristics in speech and language processing. Combinatorial algorithms for top-$K$ inference have been studied extensively by the graphical models community under the name "$M$-best MAP". Seroussi and Golmard and Nilsson first considered the problem of finding the $K$ most probable configurations in a tree structured graphical model. Later, Yanover and Weiss presented the Best Max-Marginal First algorithm which solves this problem with access only to an oracle that computes max-marginals. We also use this algorithm in Sec. 4.2. Fromer and Globerson study top-$K$ inference for LP relaxation, while Batra considers the dual problem to exploit graph structure. Flerova et al. study top-$K$ extensions of the popular $\text{A}^{\star}$ and branch and bound search algorithms in the context of graphical models. Other related approaches include diverse $K$-best solutions and finding $K$-most probable modes.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Smoothing Inference", "weight": 1.0} -->

Smoothing for inference was used to speed up iterative algorithms for continuous relaxations. Johnson considered smoothing dual decomposition inference using the entropy smoother, followed by Jojic et al. and Savchynskyy et al. who studied its theoretical properties. Meshi et al. expand on this study to include $\ell_{2}^{2}$ smoothing. Explicitly smoothing discrete inference algorithms in order to smooth the learning problem was considered by Zhang et al. and Song et al. using the entropy and $\ell_{2}^{2}$ smoothers respectively. The $\ell_{2}^{2}$ smoother was also used by Martins and Astudillo. Hazan et al. consider the approach of blending learning and inference, instead of using inference algorithms as black-box procedures.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Smoothing Inference", "weight": 1.0} -->

Related ideas to ours appear in the independent works. These works partially overlap with ours, but the papers choose different perspectives, making them complementary to each other. Mensch and Blondel proceed differently when, e.g., smoothing inference based on dynamic programming. Moreover, they do not establish complexity bounds for optimization algorithms making calls to the resulting smooth inference oracles. We define smooth inference oracles in the context of black-box first-order optimization and establish worst-case complexity bounds for incremental optimization algorithms making calls to these oracles. Indeed we relate the amount of smoothing controlled by $\mu$ to the resulting complexity of the optimization algorithms relying on smooth inference oracles.

<!-- chunk {"id": "body-0017", "role": "body", "section": "End-to-end Training of Structured Prediction", "weight": 1.0} -->

The general framework for global training of structured prediction models was introduced by Bottou and Gallinari and applied to handwriting recognition by Bengio et al. and to document processing by Bottou et al.. This approach, now called "deep structured prediction", was used, e.g., by Collobert et al. and Belanger and McCallum.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Smooth Structured Prediction", "weight": 1.0} -->

Structured prediction aims to search for score functions $\phi$ parameterized by ${\mathbf{w}} \in {\mathbb{R}}^{d}$ that model the compatibility of input ${\mathbf{x}} \in \mathcal{X}$ and output ${\mathbf{y}} \in \mathcal{Y}$ as $\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}$ through a graphical model. Given a score function $\phi{(\cdot, \cdot;{\mathbf{w}})}$, predictions are made using an inference procedure which, when given an input $\mathbf{x}$, produces the best output We shall return to the score functions and the inference procedures in Sec. 3. First, given such a score function $\phi$, we define the structural hinge loss and describe how it can be smoothed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Structural Hinge Loss", "weight": 1.0} -->

On a given input-output pair $({\mathbf{x}},{\mathbf{y}})$, the error of prediction of $\mathbf{y}$ by the inference procedure with a score function $\phi{(\cdot, \cdot;{\mathbf{w}})}$, is measured by a task loss $\ell\left({\mathbf{y}},{{\mathbf{y}}^{\ast}{({\mathbf{x}};{\mathbf{w}})}} \right)$ such as the Hamming loss. The learning procedure would then aim to find the best parameter $\mathbf{w}$ that minimizes the loss on a given dataset of input-output training examples. However, the resulting problem is piecewise constant and hard to optimize.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Structural Hinge Loss", "weight": 1.0} -->

This approach, known as max-margin structured prediction, builds upon binary and multi-class support vector machines, where the term $\ell{({\mathbf{y}}^{(i)},{\mathbf{y}})}$ inside the maximization in generalizes the notion of margin. The task loss $\ell$ is assumed to possess appropriate structure so that the maximization inside, known as loss augmented inference, is no harder than the inference problem. When considering a fixed input-output pair $({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)}$), we drop the index with respect to the sample $i$ and consider the structural hinge loss as When the map ${\mathbf{w}}\mapsto{\psi{({\mathbf{y}};{\mathbf{w}})}}$ is affine, the structural hinge loss $f$ and the objective $F$ from are both convex - we refer to this case as the structural support vector machine.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Structural Hinge Loss", "weight": 1.0} -->

When ${\mathbf{w}}\mapsto{\psi{({\mathbf{y}};{\mathbf{w}})}}$ is a nonlinear but smooth map, then the structural hinge loss $f$ and the objective $F$ are nonconvex.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Smoothing Strategy", "weight": 1.0} -->

A convex, non-smooth function $h$ can be smoothed by taking its infimal convolution with a smooth function. We now recall its dual representation, which Nesterov first used to relate the amount of smoothing to optimal complexity bounds.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Smoothing the Structural Hinge Loss", "weight": 1.0} -->

We rewrite the structural hinge loss as a composition where $m = {|\mathcal{Y}|}$ so that the structural hinge loss reads We smooth the structural hinge loss by simply smoothing the non-smooth max function $h$ as When $\mathbf{g}$ is smooth and Lipschitz continuous, $f_{\mu\omega}$ is a smooth approximation of the structural hinge loss, whose gradient is readily given by the chain-rule. In particular, when $\mathbf{g}$ is an affine map ${{\mathbf{g}}{({\mathbf{w}})}} = {{{\mathbf{A}}{\mathbf{w}}} + {\mathbf{b}}}$, if follows that $f_{\mu\omega}$ is $({{\|{\mathbf{A}}\|}_{\beta,\alpha}^{2}/\mu})$-smooth with respect to $\parallel \cdot \parallel_{\beta}$ (cf. Lemma 40 in Appendix A).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Smoothing Variants", "weight": 1.0} -->

In the context of smoothing the max function, we now describe two popular choices for the smoothing function $\omega$, followed by computational considerations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Entropy and $\\ell_{2}^{2}$ smoothing", "weight": 1.0} -->

When $h$ is the max function, the smoothing operation can be computed analytically for the *entropy* smoother and the $\ell_{2}^{2}$ smoother, denoted respectively as These lead respectively to the log-sum-exp function and an orthogonal projection onto the simplex, Furthermore, the following holds for all $\mu_{1} \geq \mu_{2} \geq 0$ from Prop.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Top-$K$ Strategy", "weight": 1.0} -->

Though the gradient of the composition $f_{\mu\omega} = {h_{\mu\omega} \circ {\mathbf{g}}}$ can be written using the chain rule, its actual computation for structured prediction problems involves computing $\nabla{\mathbf{g}}$ over all $m = {|\mathcal{Y}|}$ of its components, which may be intractable. However, in the case of $\ell_{2}^{2}$ smoothing, projections onto the simplex are sparse, as pointed out by the following proposition.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Inference Oracles", "weight": 1.0} -->

This section studies first order oracles used in standard and smoothed structured prediction. We first describe the parameterization of the score functions through graphical models.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Score Functions", "weight": 1.0} -->

Structured prediction is defined by the structure of the output $\mathbf{y}$, while input ${\mathbf{x}} \in \mathcal{X}$ can be arbitrary. Each output ${\mathbf{y}} \in \mathcal{Y}$ is composed of $p$ components $y_{1},\ldots,y_{p}$ that are linked through a graphical model $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$ - the nodes $\mathcal{V} = {\{ 1,\cdots,p\}}$ represent the components of the output $\mathbf{y}$ while the edges $\mathcal{E}$ define the dependencies between various components. The value of each component $y_{v}$ for $v \in \mathcal{V}$ represents the state of the node $v$ and takes values from a finite set $\mathcal{Y}_{v}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Score Functions", "weight": 1.0} -->

The set of all output structures $\mathcal{Y} = {\mathcal{Y}_{1} \times \cdots \times \mathcal{Y}_{p}}$ is then finite yet potentially intractably large.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Score Functions", "weight": 1.0} -->

The structure of the graph (i.e., its edge structure) depends on the task. For the task of sequence labeling, the graph is a chain, while for the task of parsing, the graph is a tree. On the other hand, the graph used in image segmentation is a grid.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Score Functions", "weight": 1.0} -->

For a given input $\mathbf{x}$ and a score function $\phi{(\cdot, \cdot;{\mathbf{w}})}$, the value $\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}$ measures the compatibility of the output $\mathbf{y}$ for the input $\mathbf{x}$. The essential characteristic of the score function is that it decomposes over the nodes and edges of the graph as For a fixed $\mathbf{w}$, each input $\mathbf{x}$ defines a specific compatibility function $\phi{({\mathbf{x}}, \cdot;{\mathbf{w}})}$. The nature of the problem and the optimization algorithms we consider hinge upon whether $\phi$ is an affine function of $\mathbf{w}$ or not. The two settings studied here are the following:: Pre-defined Feature Map.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Score Functions", "weight": 1.0} -->

In this structured prediction framework, a pre-specified feature map $\Phi:{{\mathcal{X} \times \mathcal{Y}}\rightarrow{\mathbb{R}}^{d}}$ is employed and the score $\phi$ is then defined as the linear function: Learning the Feature Map. We also consider the setting where the feature map $\Phi$ is parameterized by ${\mathbf{w}}_{0}$, for example, using a neural network, and is learned from the data. The score function can then be written as where ${\mathbf{w}} = {({\mathbf{w}}_{0},{\mathbf{w}}_{1})}$ and the scalar product decomposes into nodes and edges as above.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Score Functions", "weight": 1.0} -->

Note that we only need the decomposition of the score function over nodes and edges of the $\mathcal{G}$ as in Eq.. In particular, while Eq. is helpful to understand the use of neural networks in structured prediction, the optimization algorithms developed in Sec. 6 apply to general nonlinear but smooth score functions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Score Functions", "weight": 1.0} -->

This framework captures both generative probabilistic models such as Hidden Markov Models (HMMs) that model the joint distribution between $\mathbf{x}$ and $\mathbf{y}$ as well as discriminative probabilistic models, such as conditional random fields where dependencies among the input variables $\mathbf{x}$ do not need to be explicitly represented. In these cases, the log joint and conditional probabilities respectively play the role of the score $\phi$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 5 (Sequence Tagging)", "weight": 1.0} -->

Consider the task of sequence tagging in natural language processing where each $\mathbf{x} = {(x_{1},\cdots,x_{p})} \in \mathcal{X}$ is a sequence of words and $\mathbf{y} = {(y_{1},\cdots,y_{p})} \in \mathcal{Y}$ is a sequence of labels, both of length $p$. Common examples include part of speech tagging and named entity recognition. Each word $x_{v}$ in the sequence $\mathbf{x}$ comes from a finite dictionary $\mathcal{D}$, and each tag $y_{v}$ in $\mathbf{y}$ takes values from a finite set $\mathcal{Y}_{v} = \mathcal{Y}_{tag}$. The corresponding graph is simply a linear chain.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Inference Oracles", "weight": 1.0} -->

We define now inference oracles as first order oracles in structured prediction. These are used later to understand the information-based complexity of optimization algorithms.

<!-- chunk {"id": "body-0037", "role": "body", "section": "First Order Oracles in Structured Prediction", "weight": 1.0} -->

A first order oracle for a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is a routine which, given a point ${\mathbf{w}} \in {\mathbb{R}}^{d}$, returns on output a value $f{({\mathbf{w}})}$ and a (sub)gradient ${\mathbf{v}} \in {\partial{f{({\mathbf{w}})}}}$, where $\partial f$ is the Fréchet (or regular) subdifferential. We now define inference oracles as first order oracles for the structural hinge loss $f$ and its smoothed variants $f_{\mu\omega}$. Note that these definitions are independent of the graphical structure. However, as we shall see, the graphical structure plays a crucial role in the implementation of the inference oracles.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 8", "weight": 1.0} -->

Consider the task of sequence tagging from Example 5. ‣ 3.1 Score Functions ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"). The inference problem is a search over all ${|\mathcal{Y}|} = {|\mathcal{Y}_{tag}|}^{p}$ label sequences. For chain graphs, this is equivalent to searching for the shortest path in the associated trellis, shown in Fig. 1. An efficient dynamic programming approach called the Viterbi algorithm can solve this problem in space and time polynomial in $p$ and $|\mathcal{Y}_{tag}|$. The structural hinge loss is non-smooth because a small change in $\mathbf{w}$ might lead to a radical change in the best scoring path shown in Fig. 1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 8", "weight": 1.0} -->

When smoothing $f$ with $\omega = \ell_{2}^{2}$, the smoothed function $f_{\mu\ell_{2}^{2}}$ is given by a projection onto the simplex, which picks out some number $K_{\psi/\mu}$ of the highest scoring outputs $\mathbf{y} \in \mathcal{Y}$ or equivalently, $K_{\psi/\mu}$ shortest paths in the Viterbi trellis (Fig. 1(b)). The top-$K$ oracle then uses the top-$K$ strategy to approximate $f_{\mu\ell_{2}^{2}}$ with $f_{\mu,K}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 8", "weight": 1.0} -->

On the other hand, with entropy smoothing $\omega = {- H}$, we get the log-sum-exp function and its gradient is obtained by averaging over paths with weights such that shorter paths have a larger weight (cf. Lemma 7(ii) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models")). This is visualized in Fig. 1(c).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Exp Oracles and Conditional Random Fields", "weight": 1.0} -->

Recall that a Conditional Random Field (CRF) with augmented score function $\psi$ and parameters ${\mathbf{w}} \in {\mathbb{R}}^{d}$ is a probabilistic model that assigns to output ${\mathbf{y}} \in \mathcal{Y}$ the probability where $A_{\psi}{({\mathbf{w}})}$ is known as the log-partition function, a normalizer so that the probabilities sum to one. Gradient-based maximum likelihood learning algorithms for CRFs require computation of the log-partition function $A_{\psi}{({\mathbf{w}})}$ and its gradient ${\nabla A_{\psi}}{({\mathbf{w}})}$. Next proposition relates the computational costs of the exp oracle and the log-partition function.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation of Inference Oracles", "weight": 1.0} -->

We now turn to the concrete implementation of the inference oracles. This depends crucially on the structure of the graph $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$. If the graph $\mathcal{G}$ is a tree, then the inference oracles can be computed exactly with efficient procedures, as we shall see in in the Sec. 4.1. When the graph $\mathcal{G}$ is not a tree, we study special cases when specific discrete structure can be exploited to efficiently implement some of the inference oracles in Sec. 4.2. The results of this section are summarized in Table 2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Inference Oracles in Trees", "weight": 1.0} -->

We first consider algorithms implementing the inference algorithms in trees and examine their computational complexity.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Max Oracle", "weight": 1.0} -->

In tree structured graphical models, the inference problem, and thus the max oracle (cf. Lemma 7(i) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models")) can always be solved exactly in polynomial time by the max-product algorithm, which uses the technique of dynamic programming. The Viterbi algorithm (Algo. 1) for chain graphs from Example 8 is a special case. See Algo. 7 in Appendix B for the max-product algorithm in full generality.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Top-$K$ Oracle", "weight": 1.0} -->

The top-$K$ oracle uses a generalization of the max-product algorithm that we name top-$K$ max-product algorithm. Following the work of Seroussi and Golmard, it keeps track of the $K$-best intermediate structures while the max-product algorithm just tracks the single best intermediate structure. Formally, the $k$th largest element from a discrete set $S$ is defined as We present the algorithm in the simple case of chain structured graphical models in Algo. 2. The top-$K$ max-product algorithm for general trees is given in Algo. 8 in Appendix B. Note that it requires $\overset{\sim}{\mathcal{O}}{(K)}$ times the time and space of the max oracle.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Exp oracle", "weight": 1.0} -->

The relationship of the exp oracle with CRFs (Prop. 9) leads directly to Algo. 3, which is based on marginal computations from the sum-product algorithm.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Exp oracle", "weight": 1.0} -->

1: Input: Augmented score function ψ (⋅, ⋅; w) defined on a chain graph 𝒢. 2: Set π1 (y1) ← ψ1 (y1) for all y1 ∈ 𝒴1. 4: For all yv ∈ 𝒴v, set 5: Assign to δv (yv) the yv − 1 that attains the max above for each yv ∈ 𝒴v. 7: Set ψ* ← maxyp ∈ 𝒴pπp (yp) and store the maximizing assignments of yp in yp*.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 10", "weight": 1.0} -->

We note that clique trees allow the generalization of the algorithms of this section to general graphs with cycles. However, the construction of a clique tree requires time and space exponential in the treewidth of the graph.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 11", "weight": 1.0} -->

Consider the task of sequence tagging from Example 5. ‣ 3.1 Score Functions ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"). The Viterbi algorithm (Algo. 1) maintains a table $\pi_{v}{(y_{v})}$, which stores the best length-$v$ prefix ending in label $y_{v}$. One the other hand, the top-$K$ Viterbi algorithm (Algo. 2) must store in $\pi_{v}^{(k)}{(y_{v})}$ the score of $k$th best length-$v$ prefix that ends in $y_{v}$ for each $k \in {\lbrack K\rbrack}$. In the vanilla Viterbi algorithm, the entry $\pi_{v}{(y_{v})}$ is updated by looking the previous column $\pi_{v - 1}$ following. Compare this to update of the top-$K$ Viterbi algorithm.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 11", "weight": 1.0} -->

In this case, the exp oracle is implemented by the forward-backward algorithm, a specialization of the sum-product algorithm to chain graphs.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Complexity of Inference Oracles", "weight": 1.0} -->

The next proposition presents the correctness guarantee and complexity of each of the aforementioned algorithms. Its proof has been placed in Appendix B.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Inference Oracles in Loopy Graphs", "weight": 1.0} -->

For general loopy graphs with high tree-width, the inference problem is NP-hard. In particular cases, graph cut, matching or search algorithms can be used for exact inference in dense loopy graphs, and therefore, to implement the max oracle as well (cf. Lemma 7(i) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models")). In each of these cases, we find that the top-$K$ oracle can be implemented, but the exp oracle is intractable. Appendix C contains a review of the algorithms and guarantees referenced in this section.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Inference Oracles using Max-Marginals", "weight": 1.0} -->

We now define a max-marginal, which is a constrained maximum of the augmented score $\psi$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Graph Cut and Matching Inference", "weight": 1.0} -->

Kolmogorov and Zabin showed that submodular energy functions over binary variables can be efficiently minimized exactly via a minimum cut algorithm. For a class of alignment problems, e.g., Taskar et al., inference amounts to finding the best bipartite matching. In both these cases, max-marginals can be computed exactly and efficiently by combinatorial algorithms. This gives us a way to implement the max and top-$K$ oracles. However, in both settings, computing the log-partition function $A_{\psi}{({\mathbf{w}})}$ of a CRF with score $\psi$ is known to be #P-complete. Prop. 9 immediately extends this result to the exp oracle. This discussion is summarized by the following proposition, whose proof is provided in Appendix C.4.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Branch and Bound Search", "weight": 1.0} -->

Max oracles implemented via search algorithms can often be extended to implement the top-$K$ oracle. We restrict our attention to best-first branch and bound search such as the celebrated Efficient Subwindow Search.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Branch and Bound Search", "weight": 1.0} -->

Branch and bound methods partition the search space into disjoint subsets, while keeping an upper bound $\hat{\psi}:{{\mathcal{X} \times 2^{\mathcal{Y}}}\rightarrow{\mathbb{R}}}$, on the maximal augmented score for each of the subsets $\hat{\mathcal{Y}} \subseteq \mathcal{Y}$. Using a best-first strategy, promising parts of the search space are explored first. Parts of the search space whose upper bound indicates that they cannot contain the maximum do not have to be examined further.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Branch and Bound Search", "weight": 1.0} -->

The top-$K$ oracle is implemented by simply continuing the search procedure until $K$ outputs have been produced - see Algo. 13 in Appendix C.5. Both the max oracle and the top-$K$ oracle can degenerate to an exhaustive search in the worst case, so we do not have sharp running time guarantees. However, we have the following correctness guarantee.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Casimir Algorithm", "weight": 1.0} -->

We come back to the optimization problem with $f^{(i)}$ defined. We assume in this section that the mappings ${\mathbf{g}}^{(i)}$ defined in are affine. Problem now reads For a single input ($n = 1$), the problem reads where $h$ is a simple non-smooth convex function and $\lambda \geq 0$. Nesterov first analyzed such setting: while the problem suffers from its non-smoothness, fast methods can be developed by considering smooth approximations of the objectives. We combine this idea with the Catalyst acceleration scheme to accelerate a linearly convergent smooth optimization algorithm resulting in a scheme called Casimir.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Casimir: Catalyst with Smoothing", "weight": 1.0} -->

The Catalyst approach minimizes regularized objectives centered around the current iterate. The algorithm proceeds by computing approximate proximal point steps instead of the classical (sub)-gradient steps. A proximal point step from a point $\mathbf{w}$ with step-size $\kappa^{- 1}$ is defined as the minimizer of which can also be seen as a gradient step on the Moreau envelope of $F$ - see Lin et al. for a detailed discussion. While solving the subproblem might be as hard as the original problem we only require an approximate solution returned by a given optimization method $\mathcal{M}$. The Catalyst approach is then an inexact accelerated proximal point algorithm that carefully mixes approximate proximal point steps with the extrapolation scheme of Nesterov. The Casimir scheme extends this approach to non-smooth optimization.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Casimir: Catalyst with Smoothing", "weight": 1.0} -->

For the overall method to be efficient, subproblems must have a low complexity. That is, there must exist an optimization algorithm $\mathcal{M}$ that solves them linearly. For the Casimir approach to be able to handle non-smooth objectives, it means that we need not only to regularize the objective but also to smooth it. To this end we define as a smooth approximation of the objective $F$, and, a smooth and regularized approximation of the objective centered around a given point ${\mathbf{z}} \in {\mathbb{R}}^{d}$. While the original Catalyst algorithm considered a fixed regularization term $\kappa$, we vary $\kappa$ and $\mu$ along the iterations. This enables us to get adaptive smoothing strategies.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Casimir: Catalyst with Smoothing", "weight": 1.0} -->

The overall method is presented in Algo. 4. We first analyze in Sec. 5.2 its complexity for a generic linearly convergent algorithm $\mathcal{M}$. Thereafter, in Sec. 5.3, we compute the total complexity with SVRG as $\mathcal{M}$. Before that, we specify two practical aspects of the implementation: a proper stopping criterion and a good initialization of subproblems (Line 4).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Stopping Criterion", "weight": 1.0} -->

A practical alternate stopping criterion proposed by Lin et al. is to fix an iteration budget $T_{budget}$ and run the inner solver $\mathcal{M}$ for exactly $T_{budget}$ steps. We do not have a theoretical analysis for this scheme but find that it works well in experiments.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Warm Start of Subproblems", "weight": 1.0} -->

Rate of convergence of first order optimization algorithms depends on the initialization and we must warm start $\mathcal{M}$ at an appropriate initial point in order to obtain the best convergence of subproblem in Line 4 of Algo. 4. We advocate the use of the prox center ${\mathbf{z}}_{k - 1}$ in iteration $k$ as the warm start strategy. We also experiment with other warm start strategies in Section 7.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Convergence Analysis of Casimir", "weight": 1.0} -->

We first state the outer loop complexity results of Algo. 4 for any generic linearly convergent algorithm $\mathcal{M}$ in Sec. 5.2.1, prove it in Sec. 5.2.2. Then, we consider the complexity of each inner optimization problem in Sec. 5.2.3 based on properties of $\mathcal{M}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Outer Loop Convergence Analysis", "weight": 1.0} -->

We now prove Thm. 16. The proof technique largely follows that of Lin et al., with the added challenges of accounting for smoothing and varying Moreau-Yosida regularization. We first analyze the sequence ${(\alpha_{k})}_{k \geq 0}$. The proof follows from the algebra of Eq. and has been given in Appendix D.1_{𝑘≥0} ‣ Appendix D The Casimir Algorithm and Non-Convex Extensions: Missing Proofs ‣ A Smoother Way to Train Structured Prediction Models").

<!-- chunk {"id": "body-0066", "role": "body", "section": "Claim 23", "weight": 1.0} -->

For the sequences defined in -, we have,

<!-- chunk {"id": "body-0067", "role": "body", "section": "Inner Loop Complexity", "weight": 1.0} -->

Consider a class $\mathcal{F}_{L,\lambda}$ of functions defined as We now formally define a linearly convergent algorithm on this class of functions.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Casimir with SVRG", "weight": 1.0} -->

We now choose SVRG to be the linearly convergent algorithm $\mathcal{M}$, resulting in an algorithm called Casimir-SVRG. The rest of this section analyzes the total iteration complexity of Casimir-SVRG to solve Problem. The proofs of the results from this section are calculations stemming from combining the outer loop complexity from Cor. 17 to 20 with the inner loop complexity from Prop. 27, and are relegated to Appendix D.4. Table 4 summarizes the results of this section.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 28", "weight": 1.0} -->

We start with the strongly convex case with constant smoothing.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Extension to Non-Convex Optimization", "weight": 1.0} -->

Let us now turn to the optimization problem in full generality where the mappings ${\mathbf{g}}^{(i)}$ defined in are not constrained to be affine: where $h$ is a simple, non-smooth, convex function, and each ${\mathbf{g}}^{(i)}$ is a continuously differentiable nonlinear map and $\lambda \geq 0$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Extension to Non-Convex Optimization", "weight": 1.0} -->

We describe the prox-linear algorithm in Sec. 6.1, followed by the convergence guarantee in Sec. 6.2 and the total complexity of using Casimir-SVRG together with the prox-linear algorithm in Sec. 6.3.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The Prox-Linear Algorithm", "weight": 1.0} -->

The exact prox-linear algorithm of Burke generalizes the proximal gradient algorithm (see e.g., Nesterov) to compositions of convex functions with smooth mappings such as.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The Prox-Linear Algorithm", "weight": 1.0} -->

$F{(\cdot;{\mathbf{w}}_{k})}$ of $F$ about ${\mathbf{w}}_{k}$ as Given a step length $\eta > 0$, each iteration of the exact prox-linear algorithm then minimizes the local convex model plus a proximal term as 1: Input: Smoothable objective F of the form with h simple, step length η, tolerances (ϵk)k ≥ 1, initial point w0, non-smooth convex optimization algorithm, ℳ, time horizon K 3: Using ℳ with wk − 1 as the starting point, find ${\hat{\mathbf{w}}}_{k} \approx \underset{\mathbf{w}}{\arg\min}\left\lbrack F_{\eta}{({\mathbf{w}};{\mathbf{w}}_{k - 1})}:=\frac{1}{n}\sum\limits_{i = 1}^{n} \right.$ $\left.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The Prox-Linear Algorithm", "weight": 1.0} -->

${F{({\hat{\mathbf{w}}}_{k})}} \leq {F{({\mathbf{w}}_{k - 1})}}$, else set wk = wk − 1. Algorithm 5 (Inexact) Prox-linear algorithm: outer loop Following Drusvyatskiy and Paquette, we consider an inexact prox-linear algorithm, which approximately solves using an iterative algorithm.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The Prox-Linear Algorithm", "weight": 1.0} -->

In particular, since the function to be minimized in is precisely of the form, we employ the fast convex solvers developed in the previous section as subroutines. Concretely, the prox-linear outer loop is displayed in Algo. 5. We now delve into details about the algorithm and convergence guarantees.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Inexactness Criterion", "weight": 1.0} -->

As in Section 5, we must be prudent in choosing when to terminate the inner optimization (Line 3 of Algo. 5). Function value suboptimality is used as the inexactness criterion here. In particular, for some specified tolerance $\epsilon_{k} > 0$, iteration $k$ of the prox-linear algorithm accepts a solution $\hat{\mathbf{w}}$ that satisfies ${{F_{\eta}{({\hat{\mathbf{w}}}_{k};{\mathbf{w}}_{k - 1})}} - {{\min_{\mathbf{w}}F_{\eta}}{({\mathbf{w}};{\mathbf{w}}_{k - 1})}}} \leq \epsilon_{k}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Fixed Iteration Budget", "weight": 1.0} -->

As in the convex case, we consider as a practical alternative a fixed iteration budget $T_{budget}$ and optimize $F_{\eta}{( \cdot;{\mathbf{w}}_{k})}$ for exactly $T_{budget}$ iterations of $\mathcal{M}$. Again, we do not have a theoretical analysis for this scheme but find it to be effective in practice.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Warm Start of Subproblems", "weight": 1.0} -->

As in the convex case, we advocate the use of the prox center ${\mathbf{w}}_{k - 1}$ to warm start the inner optimization problem in iteration $k$ (Line 3 of Algo. 5).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Convergence analysis of the prox-linear algorithm", "weight": 1.0} -->

We now state the assumptions and the convergence guarantee of the prox-linear algorithm.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Assumptions", "weight": 1.0} -->

For the prox-linear algorithm to work, the only requirement is that we minimize an upper model. The assumption below makes this concrete.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Assumption 33", "weight": 1.0} -->

The map $\mathbf{g}^{(i)}$ is continuously differentiable everywhere for each $i \in {\lbrack n\rbrack}$. Moreover, there exists a constant $L > 0$ such that for all ${\mathbf{w},\mathbf{w}'} \in {\mathbb{R}}^{d}$ and $i \in {\lbrack n\rbrack}$, it holds that When $h$ is $G$-Lipschitz and each ${\mathbf{g}}^{(i)}$ is $\overset{\sim}{L}$-smooth, both with respect to $\parallel \cdot \parallel_{2}$, then Assumption 33 holds with $L = {G\overset{\sim}{L}}$. In the case of structured prediction, Assumption 33 holds when the augmented score $\psi$ as a function of $\mathbf{w}$ is $L$-smooth. The next lemma makes this precise and its proof is in Appendix D.5.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Convergence Guarantee", "weight": 1.0} -->

Convergence is measured via the norm of the prox-gradient $\mathbf{\varrho}_{\eta}{(\cdot)}$, also known as the gradient mapping, defined as The measure of stationarity $\|{\mathbf{\varrho}_{\eta}{({\mathbf{w}})}}\|$ turns out to be related to the norm of the gradient of the Moreau envelope of $F$ under certain conditions - see Drusvyatskiy and Paquette for a discussion.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Convergence Guarantee", "weight": 1.0} -->

The prox-linear outer loop shown in Algo. 5 has the following convergence guarantee.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 36", "weight": 1.0} -->

Algo. 5 accepts an update only if it improves the function value (Line 4). A variant of Algo. 5 which always accepts the update has a guarantee identical to that of Thm. 35, but the sequence ${({F{(\mathbf{w}_{k})}})}_{k \geq 0}$ would not guaranteed to be non-increasing.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Prox-Linear with Casimir-SVRG", "weight": 1.0} -->

We now analyze the total complexity of minimizing the finite sum problem with Casimir-SVRG to approximately solve the subproblems of Algo. 5.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Prox-Linear with Casimir-SVRG", "weight": 1.0} -->

We choose the tolerance $\epsilon_{k}$ to decrease as $1/k$. When using the Casimir-SVRG algorithm with constant smoothing (Prop. 29) as the inner solver, this method effectively smooths the $k$th prox-linear subproblem as $1/k$. We have the following rate of convergence for this method, which is proved in Appendix D.6.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Remark 38", "weight": 1.0} -->

When an estimate or an upper bound $B$ on ${F{(\mathbf{w}_{0})}} - F^{\ast}$, one could set $\epsilon_{0} = {\mathcal{O}{(B)}}$. This is true, for instance, in the structured prediction task where $F^{\ast} \geq 0$ whenever the task loss $\ell$ is non-negative (cf. ).

<!-- chunk {"id": "body-0088", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we study the experimental behavior of the proposed algorithms on two structured prediction tasks, namely named entity recognition and visual object localization. Recall that given training examples ${\{{({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)})}\}}_{i = 1}^{n}$, we wish to solve the problem: Note that we now allow the output space $\mathcal{Y}{({\mathbf{x}})}$ to depend on the instance $\mathbf{x}$ - the analysis from the previous sections applies to this setting as well. In all the plots, the shaded region represents one standard deviation over ten random runs.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare the performance of various optimization algorithms based on the number of calls to a smooth inference oracle. Moreover, following literature for algorithms based on SVRG, we exclude the cost of computing the full gradients.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Experiments", "weight": 1.0} -->

The results must be interpreted keeping in mind that the running time of all inference oracles is not the same. These choices were motivated by the following reasons, which may not be appropriate in all contexts. The ultimate yardstick to benchmark the performance of optimization algorithms is wall clock time. However, this depends heavily on implementation, system and ambient system conditions. With regards to the differing running times of different oracles, we find that a small value of $K$, e.g., 5 suffices, so that our highly optimized implementations of the top-$K$ oracle incurs negligible running time penalties over the max oracle. Moreover, the computations of the batch gradient have been neglected as they are embarrassingly parallel.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experiments", "weight": 1.0} -->

The outline of the rest of this section is as follows. First, we describe the datasets and task description in Sec. 7.1, followed by methods compared in Sec. 7.2 and their hyperparameter settings in Sec. 7.3. Lastly, Sec. 7.4 presents the experimental studies.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Dataset and Task Description", "weight": 1.0} -->

For each of the tasks, we specify below the following: (a) the dataset ${\{{({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)})}\}}_{i = 1}^{n}$, (b) the output structure $\mathcal{Y}$, (c) the loss function $\ell$, (d) the score function $\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}$, (e) implementation of inference oracles, and lastly, (f) the evaluation metric used to assess the quality of predictions.

<!-- chunk {"id": "body-0093", "role": "body", "section": "CoNLL 2003: Named Entity Recognition", "weight": 1.0} -->

Named entities are phrases that contain the names of persons, organization, locations, etc, and the task is to predict the label (tag) of each entity. Named entity recognition can be formulated as a sequence tagging problem where the set $\mathcal{Y}_{tag}$ of individual tags is of size 7.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Score Function", "weight": 1.0} -->

We use a chain graph to represent this task. In other words, the observation-label dependencies are encoded as a Markov chain of order 1 to enable efficient inference using the Viterbi algorithm. We only consider the case of linear score ${\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}} = {\langle{\mathbf{w}},{\Phi{({\mathbf{x}},{\mathbf{y}})}}\rangle}$ for this task. The feature map $\Phi$ here is very similar to that given in Example 5. ‣ 3.1 Score Functions ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"). Following Tkachenko and Simanovsky, we use local context $\Psi_{i}{({\mathbf{x}})}$ around $i$^th^ word $x_{i}$ of $\mathbf{x}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Score Function", "weight": 1.0} -->

In particular, define ${\Psi_{i}{({\mathbf{x}})}} = {{\mathbf{e}}_{x_{i - 2}} \otimes \cdots \otimes {\mathbf{e}}_{x_{i + 2}}}$, where $\otimes$ denotes the Kronecker product between column vectors, and ${\mathbf{e}}_{x_{i}}$ denotes a one hot encoding of word $x_{i}$, concatenated with the one hot encoding of its the part of speech tag and syntactic chunk tag which are provided with the input. Now, we can define the feature map $\Phi$ as where ${\mathbf{e}}_{y} \in {\mathbb{R}}^{|\mathcal{Y}_{tag}|}$ is a one hot-encoding of $y \in \mathcal{Y}_{tag}$, and $\oplus$ denotes vector concatenation.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Inference", "weight": 1.0} -->

We use the Viterbi algorithm as the max oracle (Algo. 1) and top-$K$ Viterbi algorithm (Algo. 2) for the top-$K$ oracle.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Dataset", "weight": 1.0} -->

The dataset used was CoNLL 2003, which contains about $\sim {20K}$ sentences.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Evaluation Metric", "weight": 1.0} -->

We follow the official CoNLL metric: the $F_{1}$ measure excluding the 'O' tags. In addition, we report the objective function value measured on the training set ("train loss").

<!-- chunk {"id": "body-0099", "role": "body", "section": "Other Implementation Details", "weight": 1.0} -->

The sparse feature vectors obtained above are hashed onto $2^{16} - 1$ dimensions for efficiency.

<!-- chunk {"id": "body-0100", "role": "body", "section": "PASCAL VOC 2007: Visual Object Localization", "weight": 1.0} -->

Given an image and an object of interest, the task is to localize the object in the given image, i.e., determine the best bounding box around the object. A related, but harder task is object detection, which requires identifying and localizing any number of objects of interest, if any, in the image. Here, we restrict ourselves to pure localization with a single instance of each object. Given an image ${\mathbf{x}} \in \mathcal{X}$ of size $n_{1} \times n_{2}$, the label ${\mathbf{y}} \in {\mathcal{Y}{({\mathbf{x}})}}$ is a bounding box, where $\mathcal{Y}{({\mathbf{x}})}$ is the set of all bounding boxes in an image of size $n_{1} \times n_{2}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Loss Function", "weight": 1.0} -->

The PASCAL IoU metric is used to measure the quality of localization. Given bounding boxes ${\mathbf{y}},{\mathbf{y}}'$, the IoU is defined as the ratio of the intersection of the bounding boxes to the union: We then use the $1 - {IoU}$ loss defined as ${\ell{({\mathbf{y}},{\mathbf{y}}')}} = {1 - {{IoU}{({\mathbf{y}},{\mathbf{y}}')}}}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Score Function", "weight": 1.0} -->

The formulation we use is based on the popular R-CNN approach. We consider two cases: linear score and non-linear score $\phi$, both of which are based on the following definition of the feature map $\Phi{({\mathbf{x}},{\mathbf{y}})}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Score Function", "weight": 1.0} -->

Consider a convolutional neural network known as AlexNet pre-trained on ImageNet and pass $\Pi{({{\mathbf{x}}|}_{\mathbf{y}})}$ through it. Take the output of conv4, the penultimate convolutional layer as the feature map $\Phi{({\mathbf{x}},{\mathbf{y}})}$. It is of size $3 \times 3 \times 256$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Inference", "weight": 1.0} -->

For a given input image $\mathbf{x}$, we follow the R-CNN approach and use selective search to prune the search space. In particular, for an image $\mathbf{x}$, we use the selective search implementation provided by OpenCV and take the top 1000 candidates returned to be the set $\hat{\mathcal{Y}}{({\mathbf{x}})}$, which we use as a proxy for $\mathcal{Y}{({\mathbf{x}})}$. The max oracle and the top-$K$ oracle are then implemented as exhaustive searches over this reduced set $\hat{\mathcal{Y}}{({\mathbf{x}})}$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Dataset", "weight": 1.0} -->

We use the PASCAL VOC 2007 dataset, which contains $\sim {5K}$ annotated consumer (real world) images shared on the photo-sharing site Flickr from 20 different object categories. For each class, we consider all images with only a single occurrence of the object, and train an independent model for each class.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Evaluation Metric", "weight": 1.0} -->

We keep track of two metrics. The first is the localization accuracy, also known as CorLoc (for correct localization), following Deselaers et al.. A bounding box with IoU $> 0.5$ with the ground truth is considered correct and the localization accuracy is the fraction of images labeled correctly. The second metric is average precision (AP), which requires a confidence score for each prediction. We use $\phi{({\mathbf{x}},{\mathbf{y}}';{\mathbf{w}})}$ as the confidence score of ${\mathbf{y}}'$. As previously, we also plot the objective function value measured on the training examples.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

The experiments compare various convex stochastic and incremental optimization methods for structured prediction.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

SGD: Stochastic subgradient method with a learning rate $\gamma_{t} = {\gamma_{0}/{({1 + {\lfloor{t/t_{0}}\rfloor}})}}$, where $\eta_{0},t_{0}$ are tuning parameters. Note that this scheme of learning rates does not have a theoretical analysis. However, the averaged iterate ${\overline{\mathbf{w}}}_{t} = {{2/{({t^{2} + t})}}{\sum_{\tau = 1}^{t}{\tau{\mathbf{w}}_{\tau}}}}$ obtained from the related scheme $\gamma_{t} = {1/{({\lambdat})}}$ was shown to have a convergence rate of $\mathcal{O}{({({\lambda\epsilon})}^{- 1})}$. It works on the non-smooth formulation directly.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

BCFW: The block coordinate Frank-Wolfe algorithm of Lacoste-Julien et al.. We use the version that was found to work best in practice, namely, one that uses the weighted averaged iterate ${\overline{\mathbf{w}}}_{t} = {{2/{({t^{2} + t})}}{\sum_{\tau = 1}^{t}{\tau{\mathbf{w}}_{\tau}}}}$ (called bcfw-wavg by the authors) with optimal tuning of learning rates. This algorithm also works on the non-smooth formulation and does not require any tuning.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

SVRG: The SVRG algorithm proposed by Johnson and Zhang, with each epoch making one pass through the dataset and using the averaged iterate to compute the full gradient and restart the next epoch. This algorithm requires smoothing.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

Casimir-SVRG-const: Algo. 4 with SVRG as the inner optimization algorithm. The parameters $\mu_{k}$ and $\kappa_{k}$ as chosen in Prop. 29, where $\mu$ and $\kappa$ are hyperparameters. This algorithm requires smoothing.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

Casimir-SVRG-adapt: Algo. 4 with SVRG as the inner optimization algorithm. The parameters $\mu_{k}$ and $\kappa_{k}$ as chosen in Prop. 30, where $\mu$ and $\kappa$ are hyperparameters. This algorithm requires smoothing.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

On the other hand, for non-convex structured prediction, we only have two methods: SGD: The stochastic subgradient method, which we call as SGD. This algorithm works directly on the non-smooth formulation. We try learning rates $\gamma_{t} = \gamma_{0}$, $\gamma_{t} = {\gamma_{0}/\sqrt{t}}$ and $\gamma_{t} = {\gamma_{0}/t}$, where $\gamma_{0}$ is found by grid search in each of these cases. We use the names SGD-const, SGD-$t^{- {1/2}}$ and SGD-$t^{- 1}$ respectively for these variants. We note that SGD-$t^{- 1}$ does not have any theoretical analysis in the non-convex case.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Methods Compared", "weight": 1.0} -->

PL-Casimir-SVRG: Algo. 5 with Casimir-SVRG-const as the inner solver using the settings of Prop. 37. This algorithm requires smoothing the inner subproblem.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Regularization", "weight": 1.0} -->

The regularization coefficient $\lambda$ is chosen as $c/n$, where $c$ is varied in $\{ 0.01,0.1,1,10\}$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Choice of $K$", "weight": 1.0} -->

The experiments use $K = 5$ for named entity recognition where the performance of the top-$K$ oracle is $K$ times slower, and $K = 10$ for visual object localization, where the running time of the top-$K$ oracle is independent of $K$. We also present results for other values of $K$ in Fig. 5(d) and find that the performance of the tested algorithms is robust to the value of $K$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Tuning Criteria", "weight": 1.0} -->

Some algorithms require tuning one or more hyperparameters such as the learning rate. We use grid search to find the best choice of the hyperparameters using the following criteria: For the named entity recognition experiments, the train function value and the validation $F_{1}$ metric were only weakly correlated. For instance, the 3 best learning rates in the grid in terms of $F_{1}$ score, the best $F_{1}$ score attained the worst train function value and vice versa. Therefore, we choose the value of the tuning parameter that attained the best objective function value within 1% of the best validation $F_{1}$ score in order to measure the optimization performance while still remaining relevant to the named entity recognition task. For the visual object localization task, a wide range of hyperparameter values achieved nearly equal performance in terms of the best CorLoc over the given time horizon, so we choose the value of the hyperparameter that achieves the best objective function value within a given iteration budget.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Hyperparameters for Convex Optimization", "weight": 1.0} -->

This corresponds to the setting of Section 5.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Learning Rate", "weight": 1.0} -->

The algorithms SVRG and Casimir-SVRG-adapt require tuning of a learning rate, while SGD requires $\eta_{0},t_{0}$ and Casimir-SVRG-const requires tuning of the Lipschitz constant $L$ of $\nabla F_{\mu\omega}$, which determines the learning rate $\gamma = {1/{({L + \lambda + \kappa})}}$. Therefore, tuning the Lipschitz parameter is similar to tuning the learning rate. For both the learning rate and Lipschitz parameter, we use grid search on a logarithmic grid, with consecutive entries chosen a factor of two apart.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Choice of $\\kappa$", "weight": 1.0} -->

For Casimir-SVRG-const, with the Lipschitz constant in hand, the parameter $\kappa$ is chosen to minimize the overall complexity as in Prop. 29. For Casimir-SVRG-adapt, we use $\kappa = \lambda$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Stopping Criteria", "weight": 1.0} -->

Following the discussion of Sec. 5, we use an iteration budget of $T_{budget} = n$.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Warm Start", "weight": 1.0} -->

The warm start criterion determines the starting iterate of an epoch of the inner optimization algorithm. Recall that we solve the following subproblem using SVRG for the $k$th iterate (cf.): Here, we consider the following warm start strategy to choose the initial iterate ${\hat{\mathbf{w}}}_{0}$ for this subproblem: Prox-center: ${\hat{\mathbf{w}}}_{0} = {\mathbf{z}}_{k - 1}$.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Warm Start", "weight": 1.0} -->

We use the Prox-center strategy unless mentioned otherwise.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Level of Smoothing and Decay Strategy", "weight": 1.0} -->

For SVRG and Casimir-SVRG-const with constant smoothing, we try various values of the smoothing parameter in a logarithmic grid. On the other hand, Casimir-SVRG-adapt is more robust to the choice of the smoothing parameter (Fig. 5(a)). We use the defaults of $\mu = 2$ for named entity recognition and $\mu = 10$ for visual object localization.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Hyperparameters for Non-Convex Optimization", "weight": 1.0} -->

This corresponds to the setting of Section 6.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Prox-Linear Learning Rate $\\eta$", "weight": 1.0} -->

We perform grid search in powers of 10 to find the best prox-linear learning rate $\eta$. We find that the performance of the algorithm is robust to the choice of $\eta$ (Fig. 7(a)).

<!-- chunk {"id": "body-0127", "role": "body", "section": "Stopping Criteria", "weight": 1.0} -->

We used a fixed budget of 5 iterations of Casimir-SVRG-const. In Fig. 7(b), we experiment with different iteration budgets.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Level of Smoothing and Decay Strategy", "weight": 1.0} -->

In order to solve the $k$th prox-linear subproblem with Casimir-SVRG-const, we must specify the level of smoothing $\mu_{k}$. We experiment with two schemes, (a) constant smoothing $\mu_{k} = \mu$, and (b) adaptive smoothing $\mu_{k} = {\mu/k}$. Here, $\mu$ is a tuning parameters, and the adaptive smoothing scheme is designed based on Prop. 37 and Remark 38. We use the adaptive smoothing strategy as a default, but compare the two in Fig. 6.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Gradient Lipschitz Parameter for Inner Optimization", "weight": 1.0} -->

The inner optimization algorithm Casimir-SVRG-const still requires a hyperparameter $L_{k}$ to serve as an estimate to the Lipschitz parameter of the gradient ${\nabla F_{\eta,{\mu_{k}\omega}}}{( \cdot;{\mathbf{w}}_{k})}$. We set this parameter as follows, based on the smoothing strategy: (a) $L_{k} = L_{0}$ with the constant smoothing strategy, and (b) $L_{k} = {kL_{0}}$ with the adaptive smoothing strategy (cf. Prop. 2). We note that the latter choice has the effect of decaying the learning rate as $1/k$ in the $k$th outer iteration.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Convex Optimization", "weight": 1.0} -->

For the named entity recognition task, Fig. 2 plots the performance of various methods on CoNLL 2003. On the other hand, Fig. 3 presents plots for various classes of PASCAL VOC 2007 for visual object localization.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Convex Optimization", "weight": 1.0} -->

The plots reveal that smoothing-based methods converge faster in terms of training error while achieving a competitive performance in terms of the performance metric on a held-out set. Furthermore, BCFW and SGD make twice as many actual passes as SVRG based algorithms.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Non-Convex Optimization", "weight": 1.0} -->

Fig. 4 plots the performance of various algorithms on the task of visual object localization on PASCAL VOC.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Experimental Study of Effect of Hyperparameters: Convex Optimization", "weight": 1.0} -->

We now study the effects of various hyperparameter choices.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

Fig. 5(a) plots the effect of the level of smoothing for Casimir-SVRG-const and Casimir-SVRG-adapt. The plots reveal that, in general, small values of the smoothing parameter lead to better optimization performance for Casimir-SVRG-const. Casimir-SVRG-adapt is robust to the choice of $\mu$. Fig. 5(b) shows how the smooth optimization algorithms work when used heuristically on the non-smooth problem.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(b) Effect of smoothing: use of smooth optimization with smoothing (labeled “smooth”) versus the heuristic use of these algorithms without smoothing (labeled “non-smooth”) for λ = 0.01/n.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(c) Effect of warm start strategies for λ = 0.01/n (first row) and λ = 1/n (second row).

<!-- chunk {"id": "body-0137", "role": "body", "section": "Effect of Warm Start Strategies", "weight": 1.0} -->

Fig. 5(c) plots different warm start strategies for Casimir-SVRG-const and Casimir-SVRG-adapt. We find that Casimir-SVRG-adapt is robust to the choice of the warm start strategy while Casimir-SVRG-const is not. For the latter, we observe that Extrapolation is less stable (i.e., tends to diverge more) than Prox-center, which is in turn less stable than Prev-iterate, which always works (cf. Fig. 5(c)). However, when they do work, Extrapolation and Prox-center provide greater acceleration than Prev-iterate. We use Prox-center as the default choice to trade-off between acceleration and applicability.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Effect of $K$", "weight": 1.0} -->

Fig. 5(d) illustrates the robustness of the method to choice of $K$: we observe that the results are all within one standard deviation of each other.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Experimental Study of Effect of Hyperparameters: Non-Convex Optimization", "weight": 1.0} -->

We now study the effect of various hyperparameters for the non-convex optimization algorithms. All of these comparisons have been made for $\lambda = {1/n}$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

Fig. 6(a) compares the adaptive and constant smoothing strategies. Fig. 6(b) and Fig. 6(c) compare the effect of the level of smoothing on the the both of these. As previously, the adaptive smoothing strategy is more robust to the choice of the smoothing parameter.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(a) Comparison of adaptive and constant smoothing strategies.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(b) Effect of μ of the adaptive smoothing strategy.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(c) Effect of μ of the constant smoothing strategy.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(b) Effect of the iteration budget of the inner solver.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Effect of Smoothing", "weight": 1.0} -->

(c) Effect of the warm start strategy of the inner Casimir-SVRG-const algorithm.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Effect of Prox-Linear Learning Rate $\\eta$", "weight": 1.0} -->

Fig. 7(a) shows the robustness of the proposed method to the choice of $\eta$.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Effect of Iteration Budget", "weight": 1.0} -->

Fig. 7(b) also shows the robustness of the proposed method to the choice of iteration budget of the inner solver, Casimir-SVRG-const.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Effect of Warm Start of the Inner Solver", "weight": 1.0} -->

Fig. 7(c) studies the effect of the warm start strategy used within the inner solver Casimir-SVRG-const in each inner prox-linear iteration. The results are similar to those obtained in the convex case, with Prox-center choice being the best compromise between acceleration and compatibility.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Future Directions", "weight": 1.0} -->

We introduced a general notion of smooth inference oracles in the context of black-box first-order optimization. This allows us to set the scene to extend the scope of fast incremental optimization algorithms to structured prediction problems owing to a careful blend of a smoothing strategy and an acceleration scheme. We illustrated the potential of our framework by proposing a new incremental optimization algorithm to train structural support vector machines both enjoying worst-case complexity bounds and demonstrating competitive performance on two real-world problems. This work paves also the way to faster incremental primal optimization algorithms for deep structured prediction models.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Future Directions", "weight": 1.0} -->

There are several potential venues for future work. When there is no discrete structure that admits efficient inference algorithms, it could be beneficial to not treat inference as a black-box numerical procedure. Instance-level improved algorithms along the lines of Hazan et al. could also be interesting to explore.
