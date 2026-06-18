<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMAP, and PaCMAP for Data Visualization

Topics include Datasets, Control, Dimension reduction, DR.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dimension reduction (DR) techniques such as t-SNE, UMAP, and TriMAP have demonstrated impressive visualization performance on many real world datasets. One tension that has always faced these methods is the trade-off between preservation of global structure and preservation of local structure: these methods can either handle one or the other, but not both. In this work, our main goal is to understand what aspects of DR methods are important for preserving both local and global structure: it is difficult to design a better method without a true understanding of the choices we make in our algorithms and their empirical impact on the lower-dimensional embeddings they produce. Towards the goal of local structure preservation, we provide several useful design principles for DR loss functions based on our new understanding of the mechanisms behind successful DR methods. Towards the goal of global structure preservation, our analysis illuminates that the choice of which components to preserve is important. We leverage these insights to design a new algorithm for DR, called Pairwise Controlled Manifold Approximation Projection (PaCMAP), which preserves both local and global structure. Our work provides several unexpected insights into what design choices both to make and avoid when constructing DR algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dimension reduction (DR) tools for data visualization can act as either a blessing or a curse in understanding the geometric and neighborhood structures of datasets. Being able to visualize the data can provide an understanding of cluster structure or provide an intuition of distributional characteristics. On the other hand, it is well-known that DR results can be misleading, displaying cluster structures that are simply not present in the original data, or showing observations to be far from each other in the projected space when they are actually close in the original space. Thus, if we were to run several DR algorithms and receive different results, it is not clear how we would determine which of these results, if any, yield trustworthy representations of the original data distribution.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of this work is to decipher these algorithms, and why they work or don't work. We study and compare several leading algorithms, in particular, t-SNE, UMAP, and TriMap. Each of these algorithms is subject to different limitations. For instance, t-SNE can be very sensitive to the perplexity parameter and creates spurious clusters; both t-SNE and UMAP perform beautifully in preserving local structure but struggle to preserve global structure. TriMap, which (to date) is the only triplet model to approach the performance levels of UMAP and t-SNE, handles global structure well; however, as we shall see, TriMap's success with global structure preservation is not due to reasons we expect, based on its derivation. TriMap also struggles with local structure sometimes. Interestingly, none of t-SNE, UMAP, or TriMap can be adjusted smoothly from local to global structure preservation through any obvious adjustment of parameters. Even basic comparisons of these algorithms can be tricky: each one has a different loss function with many parameters, and it is not clear which parameters matter, and how parameters correspond to each other across algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For instance, even comparing the heavily related algorithms t-SNE and UMAP is non-trivial; their repulsive forces between points arise from two different mechanisms. In fact, several papers have been published that navigate the challenges of tuning parameters and applying these methods in practice.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Without an understanding of the algorithms' loss functions and what aspects of them have an impact on the embedding, it is difficult to substantially improve upon them. Similarly, without an understanding of other choices made within these algorithms, it becomes hard to navigate adjustments of their parameters. Hence, we ask: What aspects of the various loss functions for different algorithms are important? Is there a not-very-complicated loss function that allows us to handle both local and global structure in a unified way? Can we tune an algorithm to migrate smoothly between local and global structure preservation in a way we can understand? Can we preserve both local and global structure within the same algorithm? Can we determine what components of the high-dimensional data to preserve when reducing to a low-dimensional space? We have found that addressing these questions requires looking at two primary design choices: the loss function, and the choice of graph components involved in the loss function.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The loss function controls the attractive and repulsive forces between each pair of data points. In Section 4, we focus on deciphering general principles of a good loss function. We show how UMAP and other algorithms obey these principles, and show empirically why deviating from these principles ruins the DR performance. We also introduce a simple loss function obeying our principles. This new loss function is used in an algorithm called Pairwise Controlled Manifold Approximation Projection (PaCMAP) introduced in this work. Only by visualizing the loss function in a specific way (what we call a "rainbow figure") were we able to see why this new loss function works to preserve local structure.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The choice of graph components determines which subset of pairs are to be attracted and repulsed. This is the focus of Section 5. Generally, we try to pull neighbors from the high-dimensional space closer together in the low-dimensional space, while pushing further points in the original space away in the low-dimensional space. We find that the choices of which points to attract and which points to repulse are important in the preservation of local versus global structure. We provide some understanding of how to navigate these choices in practice. Specifically, we illustrate the importance of having forces on non-neighbors. One mechanism to do this is to introduce "mid-near" pairs to attract, which provide a contrast to the repulsion of further points. Mid-near pairs are leveraged in PaCMAP to preserve global structure.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Throughout, we also discuss other aspects of DR algorithms. For example, in Section 6, we show that initialization and scaling can be important, in fact, we show that TriMap's ability to preserve global structure comes from an unexpected source, namely its initialization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

From these few figures, we already gain some intuition about the different behavior of these algorithms and where their weaknesses might be. One major benefit of working on dimension-reduction methods is that the results can be visualized and assessed qualitatively. As we show experimentally within this paper, the qualitative observations we make about the algorithms' performance correlate directly with quantitative local-and-global structure preservation metrics: in many cases, qualitative analysis, similar to what we show in Figure 1, is sufficient to assess performance qualities. In other words, with these algorithms, what you see is actually what you get.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contributions are: An understanding of key elements of dimension reduction algorithms: the loss function, and the set of graph components. A set of principles that good loss functions for successful algorithms have obeyed, unified in the rainbow figure, which visualizes the mechanisms behind different DR methods. A new loss function (PaCMAP's loss) that obeys the principles and is easy to work. Guidelines for the choice of graph components (neighbors, mid-near pairs, and further points). An insight that initialization has a surprising impact on several DR algorithms that influences their ability to preserve global structure. A new algorithm, PaCMAP, that obeys the principles outlined above. PaCMAP preserves both local and global structure, owing to a dynamic choice of graph components over the course of the algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "t-SNE, UMAP, TriMap, and PaCMAP", "weight": 1.0} -->

For completeness, we review the algorithms t-SNE, UMAP, TriMap in common notation in Sections 3.1, 3.2, and 3.3; readers familiar with these methods can skip these subsections. We also place a short description of PaCMAP in Section 3.4, though the full explanation of the decisions we made in PaCMAP follows in later sections, with a full statement of the algorithm in Section 7.

<!-- chunk {"id": "body-0013", "role": "body", "section": "t-SNE", "weight": 1.0} -->

The user-defined parameter $Perplexity$ is monotonically increasing in $\sigma_{i}$. Intuitively, as $Perplexity$ becomes larger, the probabilities become uniform. When $Perplexity$ becomes smaller, the probabilities concentrate heavily on the nearest points.

<!-- chunk {"id": "body-0014", "role": "body", "section": "t-SNE", "weight": 1.0} -->

Define the symmetric probability $p_{ij} = \frac{p_{i|j} + p_{j|i}}{2n}$. Observe that this probability does not depend on the decision variables $\mathbf{Y}$ and is derived from $\mathbf{X}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "t-SNE", "weight": 1.0} -->

Initialization: initialize $\mathbf{Y}$ using the multivariate Normal distribution $\mathcal{N}{(0,{10^{- 4}I})}$, with $I$ denoting the two-dimensional identity matrix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "t-SNE", "weight": 1.0} -->

Optimization: apply gradient descent with momentum. The momentum term is set to 0.5 for the first 250 iterations, and to 0.8 for the following 750 iterations. The learning rate is initially set to 100 and updated adaptively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "t-SNE", "weight": 1.0} -->

Intuitively, for every observation $i$, t-SNE defines a relative distance metric $p_{ij}$ and tries to find a low-dimensional embedding in which the relative distances $q_{ij}$ in the low-dimensional space match those of the high-dimensional distances (according to Kullback--Leibler divergence). See van der Maaten and Hinton for additional details and modifications that were made to the basic algorithm to improve its performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "UMAP", "weight": 1.0} -->

The algorithm consists of two primary phases: graph construction for the high-dimensional space, and optimization of the low-dimensional graph layout. The algorithm was derived using simplicial geometry, but this derivation is not necessary to understand the algorithm's steps or general behavior.

<!-- chunk {"id": "body-0019", "role": "body", "section": "UMAP", "weight": 1.0} -->

For each observation, find the $k$ nearest neighbors for a given distance metric ${Distance}_{i,j}$ (typically Euclidean).

<!-- chunk {"id": "body-0020", "role": "body", "section": "UMAP", "weight": 1.0} -->

For each observation, compute $\rho_{i}$, the minimal positive distance from observation $i$ to a neighbor.

<!-- chunk {"id": "body-0021", "role": "body", "section": "UMAP", "weight": 1.0} -->

Intuitively, $\sigma_{i}$ is used to normalize the distances between every observation and its neighbors to preserve the relative high-dimensional proximities.

<!-- chunk {"id": "body-0022", "role": "body", "section": "UMAP", "weight": 1.0} -->

Define a weighted graph $G$ whose vertices are observations and where for each edge $(i,j)$ it holds that $\mathbf{x}_{i}$ is a nearest neighbor of $\mathbf{x}_{j}$, or vice versa. The (symmetric) weight of an edge $(i,j)$ is equal to

<!-- chunk {"id": "body-0023", "role": "body", "section": "UMAP", "weight": 1.0} -->

Initialization: initialize $Y$ using spectral embedding.

<!-- chunk {"id": "body-0024", "role": "body", "section": "UMAP", "weight": 1.0} -->

The hyperparameters $a$ and $b$ are tuned using the data by fitting the function $\left( {1 + {a\left( {\|{\mathbf{y}_{i} - \mathbf{y}_{j}}\|}_{2}^{2} \right)^{b}}} \right)^{- 1}$ to the non-normalized weight function $\exp\left( {- {\max{\{ 0,{{Distance}_{i,j} - \rho_{i}}\}}}} \right)$ with the goal of creating a smooth approximation. The hyperparameter $\alpha$ indicates the learning rate.

<!-- chunk {"id": "body-0025", "role": "body", "section": "UMAP", "weight": 1.0} -->

Apply a repulsive force to observation $i$, pushing it away from observation $k$. Here, $k$ is chosen by randomly sampling non-neighboring vertices, that is, an edge $(i,k)$ that is not in $G$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "UMAP", "weight": 1.0} -->

Intuitively, the algorithm first constructs a weighted graph of nearest neighbors, where weights represent probability distributions. The optimization phase can be viewed as a stochastic gradient descent on individual observations, or as a force-directed graph layout algorithm. The latter refers a family of algorithms for visualizing graphs by iteratively moving points in the low-dimensional space closer that are close to each other in the high-dimensional space, and pushing apart points in the low-dimensional space that are further away from each other in the high-dimensional space.

<!-- chunk {"id": "body-0027", "role": "body", "section": "UMAP", "weight": 1.0} -->

In the UMAP paper, the authors discuss several variants of the algorithm, as well as finer details and additional hyperparameters. The description provided here mostly adheres to Section 3 of McInnes et al. with minor modifications to the denominators based on the implementation of UMAP. We also note that in the actual implementation, the edges are sampled sequentially with probability $\overline{w}{(\mathbf{x}_{i},\mathbf{x}_{j})}$ rather than selected uniformly, and the repulsive force sets ${\overline{w}{(\mathbf{x}_{i},\mathbf{x}_{k})}} = 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "TriMap", "weight": 1.0} -->

For each observation $i$, find its 10 nearest neighbors ("n_inliers") according to the distance metric $Distance$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "TriMap", "weight": 1.0} -->

For every observation $i$ and one of its neighbors $j$, randomly sample 5 observations $k$ that are not neighbors ("n_outliers") to create 50 triplets per observation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "TriMap", "weight": 1.0} -->

For each observation $i$ randomly sample 2 additional observations to create a triplet. Repeat this step 5 times ("n_random").

<!-- chunk {"id": "body-0031", "role": "body", "section": "TriMap", "weight": 1.0} -->

where $d_{i,j}^{2} = {{{Distance}_{i,j}^{2}/\sigma_{i}}\sigma_{j}}$, and $\sigma_{i}$ is the average distance between $\mathbf{x}_{i}$ and the set of its 4--6 nearest neighbors. With a slight abuse of notation, later in the work we define $d_{i,j}^{2}$ in a close but slightly different way.

<!-- chunk {"id": "body-0032", "role": "body", "section": "TriMap", "weight": 1.0} -->

Intuitively, $\omega_{i,j,k}$ is larger when the distances in the tuple are more significant, suggesting that it is more important to preserve this relation in the low-dimensional space.

<!-- chunk {"id": "body-0033", "role": "body", "section": "TriMap", "weight": 1.0} -->

This construction, which is similar to expressions used in t-SNE and UMAP, approaches 1 when observations $i$ and $j$ are placed closer, and approaches 0 when the observations are placed further away. This implies that the fraction in the triplet loss function would approach the maximal value of 1 when $i$ is placed close to $k$ and far away from $j$ (which contradicts the definition of a triplet $(i,j,k)$ where $i$ should be closer to $j$ than to $k$). Otherwise, as $k$ moves further away, the loss approaches 0.

<!-- chunk {"id": "body-0034", "role": "body", "section": "TriMap", "weight": 1.0} -->

Initialization: initialize $\mathbf{Y}$ using PCA.

<!-- chunk {"id": "body-0035", "role": "body", "section": "TriMap", "weight": 1.0} -->

Optimization method: apply full batch gradient descent with momentum using the delta-bar-delta method (400 iterations with the value of momentum parameter equal to 0.5 during the first 250 iterations and 0.8 thereafter).

<!-- chunk {"id": "body-0036", "role": "body", "section": "TriMap", "weight": 1.0} -->

Intuitively, the algorithm tries to find an embedding that preserves the ordering of distances within a subset of triplets that mostly consist of a k-nearest neighbor and a further observation with respect to a focal observation, and a few additional randomized triplets which consist of two non-neighbors. As can be seen in the description above, the algorithm contains many design choices that work empirically, but it is not evident which of these choices are essential to creating good visualizations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "PaCMAP", "weight": 1.0} -->

PaCMAP will be officially introduced in Section 7. In this section we will provide a short description, leaving the derivation for later.

<!-- chunk {"id": "body-0038", "role": "body", "section": "PaCMAP", "weight": 1.0} -->

First, define the scaled distances between pairs of observations $i$ and $j$: $d_{ij}^{2,\text{select}} = {\frac{{\|{\mathbf{x}_{i} - \mathbf{x}_{j}}\|}^{2}}{\sigma_{ij}}\text{~and~}\sigma_{ij}} = {\sigma_{i}\sigma_{j}}$, where $\sigma_{i}$ is the average distance between $i$ and its Euclidean nearest fourth to sixth neighbors. Do not precompute these distances, as we will select only a small subset of them and can compute the distances after selecting.

<!-- chunk {"id": "body-0039", "role": "body", "section": "PaCMAP", "weight": 1.0} -->

Near pairs: Pair $i$ with its nearest $n_{NB}$ neighbors defined by the scaled distance $d_{ij}^{2,\text{select}}$. To take advantage of existing implementations of k-NN algorithms, for each sample we first select the $\min{({n_{NB} + 50},N)}$ nearest neighbors according to the Euclidean distance and from this subset we calculate scaled distances and pick the $n_{NB}$ nearest neighbors according to the scaled distance $d_{ij}^{2,\text{select}}$ (recall that $N$ is the total number of observations).

<!-- chunk {"id": "body-0040", "role": "body", "section": "PaCMAP", "weight": 1.0} -->

Mid-near pairs: For each $i$, sample 6 observations, and choose the second closest of the 6, and pair it with $i$. The number of mid-near pairs to compute is $n_{MN} = {\lfloor{{n_{NB} \times M}N\_}\rfloor}$. Default $MN\_$ is 0.5.

<!-- chunk {"id": "body-0041", "role": "body", "section": "PaCMAP", "weight": 1.0} -->

Further pairs: Sample non-neighbors. The number of such pairs is $n_{FP} = {\lfloor{{n_{NB} \times F}P\_}\rfloor}$, where default ${FP\_} = 2$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Principles of a Good Objective Function for Dimension Reduction, Part I: The Loss Function", "weight": 1.0} -->

In this section, we discuss the principles of good objective functions for DR algorithms based on two criteria: local structure: the low-dimensional representation preserves each observation's neighborhood from the high-dimensional space; and global structure: the low-dimensional representation preserves the relative positions of neighborhoods from the high-dimensional space. Note that a high-quality local structure is sometimes necessary for high-quality global structure, for instance to avoid overlapping non-compact clusters of different classes.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Principles of a Good Objective Function for Dimension Reduction, Part I: The Loss Function", "weight": 1.0} -->

We use different datasets (shown in Figure 3) to demonstrate performance on these two criteria. For the local structure criterion, we use the MNIST and COIL-20 datasets, using the labels as representing the ground truth about cluster formation (the labels are not given as input to the DR algorithms). The qualitative evaluation criteria we use for assessing the preservation of local structure is whether clusters are preserved despite the fact DR takes place without labels. (Later in Section 8 we use quantitative metrics; the qualitative measures directly reflect quantitative outcomes.) For global structure, we use the 3D datasets S-curve and Mammoth in which the relative positions of different neighborhoods contain important information (additional information about these datasets can be found in Section 8).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Principles of a Good Objective Function for Dimension Reduction, Part I: The Loss Function", "weight": 1.0} -->

In Section 4.1, we provide a generic unified objective for DR. In Section 4.2, we will introduce the rainbow figure, which can be used to directly compare loss functions from different algorithms to understand whether they are likely to preserve local structure. Section 4.3 provides the principles of loss functions for local structure preservation. Section 4.4 provides sufficient conditions for obeying the principles, namely when the loss is separable into a sum of additive and repulsive forces obeying specific technical conditions. Finally, in Section 4.5 we present PaCMAP's loss.

<!-- chunk {"id": "body-0045", "role": "body", "section": "A unified DR objective", "weight": 1.0} -->

All of the algorithms for DR that we discuss can be viewed as graph-based algorithms where a weighted graph is initially constructed based on the high-dimensional data (in particular, the distances in the high-dimension). In such graphs, nodes correspond to observations and edges signify a certain similarity between nodes which is further detailed by edge weights. Thereafter, a loss function based on the graph structure is defined and optimized to find the low-dimensional representation. If we respectively denote by $\mathcal{C}_{i}^{H}$ and $\mathcal{C}_{i}^{L}$ two corresponding graph components (e.g.,

<!-- chunk {"id": "body-0046", "role": "body", "section": "A unified DR objective", "weight": 1.0} -->

Table 1 lists several DR algorithms, and breaks their objectives down in terms of which graph components they use and what their loss functions are. Note that the definition of the loss functions in the considered algorithms is intertwined with the graph weights (e.g., weights of graph components can be thought of as either a property of the loss or the graph components).

<!-- chunk {"id": "body-0047", "role": "body", "section": "A unified DR objective", "weight": 1.0} -->

Graph components and Loss function

<!-- chunk {"id": "body-0048", "role": "body", "section": "A unified DR objective", "weight": 1.0} -->

When gradient methods are used on the objective functions, the loss function induces forces (attraction or repulsion) on the positions of the observations in the low-dimensional space. It is therefore insightful to consider how the algorithms define these forces (direction and magnitude) and apply them to different observations, which we do in more depth in Section 5. The objectives for the DR methods we consider (e.g., t-SNE, UMAP and TriMap), define for each point a set of other points to attract, and a set of further points to repulse. To illustrate the differences between the various methods, we consider triplets of points $(i,j,k)$, where $i$ is attracting $j$ and repulsing $k$. Notation $d_{ij}\overset{def}{=}\left. \parallel{\mathbf{y}_{i} - \mathbf{y}_{j}}\parallel \right._{2}$ indicates the distance between two points in the low-dimensional space.

<!-- chunk {"id": "body-0049", "role": "body", "section": "A unified DR objective", "weight": 1.0} -->

The specific choices of which observations are attracted and repulsed are complicated, but at its core, the loss governs the balance between attraction and repulsion; each algorithm aims to preserve the structure of the high-dimensional graph and reduce the crowding problem in different ways.

<!-- chunk {"id": "body-0050", "role": "body", "section": "A unified DR objective", "weight": 1.0} -->

We find these losses difficult to compare directly: they each have a different functional form. The key instrument that we will use to compare the algorithms is a plot that we refer to as the "rainbow figure," discussed next.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

The rainbow figure is a visualization of the loss and its gradients for $(i,j,k)$ triplets, where $i$ and $j$ should be attracted to each other (typically they are neighbors in the high-dimension), and $i$ and $k$ are to be repulsed (typically further points in the high-dimension). While the edges $(i,j)$ and $(i,k)$ need not be neighbors and further points, to build intuition and for ease of presentation, we refer to them as such. Note that this plot applies to local structure preservation, because it handles mainly a group of nearest neighbors and further points.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

(We note that t-SNE considers a group of nearest neighbors to keep close, although whether to attract or repulse them also depends on the comparison of distributions in low- and high- dimensional space; UMAP explicitly attracts only a group of nearest neighbors; TriMap mainly considers triplets that contain a k-nearest neighbor, and we will show in Figure 11 that the rest of the triplets actually have little effect on the final results; PaCMAP has both a group of nearest neighbors and a group of mid-near points to attract, but here in the rainbow figures we only consider attraction on the group of nearest neighbors, just as what PaCMAP does in the last phase of optimization--discussed below--where it focuses on refining local structure, in order to be consistent with other algorithms we discuss here.)

<!-- chunk {"id": "body-0053", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

Since plotting the rainbow figures requires loss functions for $(i,j,k)$ triplets, we include such losses for each of t-SNE, UMAP, TriMap, and PaCMAP (which we call "good" losses as the first 3 methods are widely considered to be very effective methods) in Table 1. We ignore weights in t-SNE, UMAP, TriMap for simplicity. PaCMAP uses uniform weights. We also note that while UMAP is motivated by the loss shown in Table 1, in practice it applies an approximation to the gradient of that loss (see Section 3.2). In what follows, we numerically compute and present the actual loss that UMAP implicitly uses.

<!-- chunk {"id": "body-0054", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

Note that even though the rainbow figure visualizes triplets, it is not necessarily the case that the loss is computed using triplets. In fact, TriMap is the only algorithm we consider that uses a loss explicitly based on triplets. Also note that t-SNE does not fix pairs of points on which to apply attractive and repulsive forces in advance. It determines these over the course of the algorithm. The other methods choose points in advance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

In addition to the "good" losses, we show rainbow figures for four "bad" losses, that we (admittedly) had constructed in aiming to construct good losses. These bad losses correspond to four DR algorithms that fail badly in experiments; these bad losses will allow us to see what properties are valuable when considering the losses of triplets for DR algorithms.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

Each of the bad losses fits some of the principles of good loss functions (considered in the next subsection), but not all of them. The choice of the particular loss functions was guided by exploring additive and multiplicative relations between the attractive and repulsive forces, as well as applying the logarithm and exponential functions to moderate the impact of large penalties.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

The upper row of figures within Figures 4 and 5 show the outcome of each DR algorithm on the MNIST dataset. The middle figures of Figures 4 and 5 show rainbow figures for the loss functions. The magnitudes of the gradients are shown in the lower figures. Directions of forces are shown in arrows (which are the same in both middle and lower figures). The attractive pair $(i,j)$ of the triplet is shown on the horizontal axis, whereas the repulsive pair $(i,k)$ is shown on the vertical axis. Each point on the plot thus represents a triplet, with forces acting on it, depending on how far the points are placed away from each other: if $i$'s neighbor $j$ is far away, there is a large loss contribution for this pair (more yellow or red on the right). Similarly, if repulsion point $k$ is too close to $i$, the loss is large (more red near the bottom of the plot, sometimes the red stripe is too thin to be clearly seen).

<!-- chunk {"id": "body-0058", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

For each triplet, $d_{ij}$ and $d_{ik}$ are (stochastically) optimized following the gradient curves on the rainbow figure; $j$ is pulled closer to $i$, while $k$ is pushed away.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The rainbow figure for loss functions", "weight": 1.0} -->

The rainbow figures are useful for helping us understand the tradeoffs made during optimization between attraction and repulsion among different neighbors or triplets. In particular, the rainbow figures of the good losses share many similarities, and differ from those of the bad losses. Several properties that induce good performance, which we have found to be common to the good losses, have been formalized as principles in the next section.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

The rainbow figures provide the following insights about what constitutes a good loss function.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Monotonicity. As expected, the loss functions are monotonically decreasing in $d_{ik}$ and are monotonically increasing in $d_{ij}$. That is, as a far point (to which repulsive forces are typically applied) becomes further away, the loss should become lower, and as a neighbor (to which attractive forces are typically applied) becomes further, the loss should become higher.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

There should be asymmetry in handling the preservation of near and far edges. We have different concerns and requirements for neighbors and further points. The following three principles deal with asymmetry.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Except in the bottom area of the rainbow figures (where $d_{ik}$ is small), the gradient of the loss should go mainly to the left. If $d_{ik}$ is not too small (assuming that the further point $k$ is sufficiently far from $i$), we no longer encourage it to be even larger, and focus on minimizing $d_{ij}$. That is, the main concern for further points is to separate them from neighbors, which avoids the crowding problem and enables clusters to be separated (if clusters exist). There should be only small gains possible even if we push further points very far away. After $d_{ik}$ is sufficiently large, we focus our attention on minimizing $d_{ij}$ (i.e., pulling nearer points closer). Formally,

<!-- chunk {"id": "body-0064", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

The advantage of this formulation of the principle (as well as the following ones) is that they are scale-invariant, and thus do not require quantification of "large" or "small" gradients. This means that they do not capture absolute magnitudes. For example, we observe empirically that when projecting the gradients on each axis, the mode of the repulsive force is smaller and has a higher peak, compared to the analogous plot of the attractive force (see, for example, Figures 9 and 10).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

In the bottom area of rainbow figures, the gradient of the loss should mainly go up, which increases $d_{ik}$. (When $d_{ik}$ is very small, the further point is too close -- it should have been further away.)

<!-- chunk {"id": "body-0066", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Along the vertical axis (when $d_{ij}$ is very small), the magnitude of the gradient should be small. That is, when $d_{ij}$ is small enough (when the near point is sufficiently close), there is little gain in further decreasing it, thus we should turn our attention to optimizing other points. This is not easy to see on the magnitude plot in Figure 4; it appears as a very thin stripe to the left of a thicker vertical stripe. Formally,

<!-- chunk {"id": "body-0067", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Along the horizontal axis (observed in 3 out of 4 methods when $d_{ik}$ is small), the magnitude of the gradient should be large. When $d_{ik}$ is too small (the further point is too close), it is pushed hard to become further away. Formally,

<!-- chunk {"id": "body-0068", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Gradients should be larger when $d_{ij}$ is moderately small, and become smaller when $d_{ij}$ is large. This reflects the fact that not all nearest neighbors can be preserved in the lower dimension and therefore the penalty for the respective violation should be limited. In a sense, we are essentially giving up on neighbors that we cannot preserve, suffering a fixed penalty for not preserving them. Formally,

<!-- chunk {"id": "body-0069", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

An illustration of the principles is given in Figure 6. As we can see from the figure (and as we can conclude from the principles), the only large gradients allowed can be along the bottom axis, also in a region slightly to the right of the vertical axis.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Principles 2-6 arise from the inherently limited capacity of any low-dimensional representation. We cannot simply always pull neighbors closer and push further points away; not all of this information can be preserved. The algorithms instead prioritize what information should be preserved, in terms of which points to consider, and how to preserve their relative distances (and which relative distances to focus on). We will consider the choice of points in Section 5.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Note that the rainbow figure of TriMap seems to violate one of our principles, namely Principle 5, that the gradient along the horizontal axis should be large. This means that two points that should be far from each other may not actually be pushed away from each other when constructing the low-dimensional representation. Interestingly, the algorithm's initialization may prevent this from causing a problem; if there are no triplets that include further points that are initialized close to each other, and neighbors that are initialized to be far away, then the forces on such triplets are irrelevant. We further discuss how TriMap obeys the principles in Section 5.1.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

Let us look at the bad loss functions, and find out what happens when the principles are violated. Recall that these bad loss functions were unsuccessful attempts to create good losses, so they each (inadvertently) obey some of the principles. All loss functions aim to minimize $d_{ij}$ and maximize $d_{ik}$ (thus obeying the first principle about monotonicity). One might think that monotonicity is enough, since it encourages attraction of neighbors and repulsion of far points, but it is not: the tradeoffs made by these loss functions are important.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

BadLoss 1: This loss cannot separate the clusters that exist in the data. This could potentially stem, first, from a violation of Principle 3, where if further points are close (when they should not be), the loss effectively ignores them and focuses instead on pulling neighbors closer (see Figure 5). Second, in a violation of Principle 2, the gradient is essentially zero in the upper left of the rainbow figure, rather than going toward the left. This means there are almost no forces on pairs for which $d_{ij}$ is relatively small and $d_{ik}$ is fairly large; the loss essentially ignores many of the triplets that could help fine-tune the structure.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

BadLoss 2: This loss preserves more of the cluster structure than BadLoss 1, but still allows different clusters to overlap. This loss works better than BadLoss 1 because it does abide by Principles 3, 4, and 5, so that far points in the high-dimensional space are well separated and neighbors are pulled closer. However, due to the violation of Principle 6, the gradient does not sufficiently preserve local structure. In fact, we can see in Figure 5 that the gradient increases with $d_{ij}$, which is visible particularly along the bottom axis. This means it tends to focus on fixing large $d_{ij}$ (global structure) at the expense of small $d_{ij}$ (local structure), where the gradient is small.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

BadLoss 3: While this loss is seemingly similar to BadLoss 2 (it is equal to the inverse and negation of that loss), the performance of this loss is significantly worse, exhibiting a severe crowding problem. We believe this failure is the result of a violation of Principle 5: This loss has larger gradient for larger $d_{ik}$ values than for smaller $d_{ik}$ values. That is, the algorithm makes little effort to repulse further points when $d_{ik}$ is small, so the points stick together. There is simply not enough force to separate points that should be distant from each other. One can see this from looking at the gradient magnitude plot of BadLoss 3 in Figure 5, showing small gradient magnitudes along the whole bottom of the plot. Consequently, although the direction of the gradient is almost the same as that of BadLoss 2, the quality of the visualization result drops significantly.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Principles of good loss functions", "weight": 1.0} -->

BadLoss 4: This loss is the most successful one in the four bad losses we presented here. Most of the clusters are well separated with a few exceptions of overlapping. The successful preservation of local structure could be credited to the obedience to Principles 2 and 4. These principles pull the neighbors together, but not too close. However, the violation of Principle 6 causes a bad trade-off among different neighbors. This loss makes great efforts to pull neighbors closer that are far away (large gradient when $d_{ij}$ is large), at the expense of ignoring the neighbors that are closer; if these nearer neighbors were optimized, they would better define the fine-grained structure of the clusters. Less attention to these closer neighbors yields non-compact clusters that sometimes overlap. Additional problems are caused by violations of Principles 3 and 5, implying that further points are not encouraged to be well-separated, which is another reason that clusters are overlapping.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Sufficient conditions for obeying the principles", "weight": 1.0} -->

There are simpler ways to check whether our principles hold than to check them each separately.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

PaCMAP uses a simple objective consisting of three types of pairwise loss terms, each corresponding to a different kind of graph component: nearest neighbor edges (denoted neighbor edges), mid-near edges (MN edges) and repulsion edges with further points (FP edges). We synonymously use the terms "edges" and "pairs."

<!-- chunk {"id": "body-0079", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

and ${\overset{\sim}{d}}_{ab} = {d_{ab}^{2} + 1} = {{\|{\mathbf{y}_{a} - \mathbf{y}_{b}}\|}^{2} + 1}$. The term $\overset{\sim}{d}$ was first used in the t-SNE algorithm, and inspired similar choices for UMAP and TriMap, which we also adopt here. The weights $w_{NB}$, $w_{MN}$, and $w_{FP}$ are weights on the different terms that we discuss in depth later, as they are important. The first two loss functions (for neighbor and mid-near edges) induce attractive forces while the latter induces a repulsive force. While the definition and role of mid-near edges are discussed in detail in Section 5, we briefly note that mid-near pairs are used to improve global structure optimization in the early part of training.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

The exact functions we have used in the losses (simple fractions) could potentially be replaced with many other functions with similar characteristics: the important elements are that they are easy to work, the attractive and repulsive forces obey the six principles, and that there is an attractive force on mid-near pairs that is separate from the other two forces.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

In what follows, we discuss how the above loss functions relate to the principles of good loss functions. For better illustration, in Figure 7 we visualize PaCMAP's losses on neighbors and further points (subplot a) and their gradients (subplot b) which can be seen as forces when optimizing the low-dim embedding. We see in Figure 7a that monotonicity holds for PaCMAP's loss, so Principle 1 is met. For a neighbor $j$, $\text{Loss}_{NB}$ changes rapidly (large gradient/forces) when $d_{ij}$ is moderately small (Principle 6), and the magnitude of the gradient is small for extreme values of $d_{ij}$ (Principle 4).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

This is a result of the slow growth of the square function ${\overset{\sim}{d}}_{ab} = {d_{ab}^{2} + 1}$ that is used in the loss of PaCMAP, when $d_{ab}$ is very small (which encourages small gradients for very small $d_{ij}$ values), and the fact that $\text{Loss}_{NB}$ saturates for large $d_{ij}$ (encourages slow growth for large $d_{ij}$ values). This can be seen in Figure 7b. These nice properties of $\text{Loss}_{NB}$ enable PaCMAP to meet Principles 4 and 6. For further points, $\text{Loss}_{FP}$ induces strong repulsive force for very small $d_{ik}$, but the force dramatically decreases to almost zero when $d_{ik}$ increases.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

In this way, PaCMAP's loss meets the requirements of Principles 3 and 5. Compared to $\text{Loss}_{FP}$ where the gradient (force) is almost zero for $d_{ik}$ values that are not too small, $\text{Loss}_{NB}$ induces an effective gradient (force) for a much wider range of $d_{ij}$. As a result of this trade-off, $\text{Loss}_{NB}$ is dominant when $d_{ik}$ is not too small, implying that Principle 2 is obeyed.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Applying the principles of a good loss function and introducing PaCMAP's loss", "weight": 1.0} -->

While the principles of good loss functions are important, they are not the only key ingredient. We will discuss the other key ingredient below: the construction of the graph components that we sum over in the loss function.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Principles of a Good Objective Function for Dimension Reduction, Part II: Graph Construction and Attractive and Repulsive Forces", "weight": 1.0} -->

Given that we cannot preserve all graph components, which ones should we preserve, and does it matter? In this section, we point out that the choice of graph components is critical to preservation of global and local structure, and the balance between them. Which points we choose to attract and repulse, and how we attract and repulse them, matter. If we choose only to attract neighbors, and if we repulse far points only when they get too close, we will lose global structure.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Principles of a Good Objective Function for Dimension Reduction, Part II: Graph Construction and Attractive and Repulsive Forces", "weight": 1.0} -->

Interestingly, most of the DR algorithms in the literature have made choices that force them to be "near-sighted." In particular, as we show in Section 5.1, most DR algorithms leave out graph components that preserve global structure. In Section 5.2, we provide mechanisms to better balance between local and global structure through the choice of graph components.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

The triplets in $\mathcal{T}$ are the graph components. Also consider a simple triplet loss such as $l_{i,j,k} = 1$ if $j$ is further away than $k$, and 0 otherwise (we call this the 0-1 triplet loss). Now, what would happen if every triplet in $\mathcal{T}$ contained at least one point very close to $i$, to serve as $j$ in the triplet? In other words, $\mathcal{T}$ omits all triplets where $j$ and $k$ are both far from $i$. In this case, we argue that the algorithm would completely lose its ability to preserve global structure. To see this, note that the 0-1 triplet loss is zero whenever all further points are further away than all neighbors. But this loss can be zero without preserving global structure. While maintaining zero loss, even simple topological structures may not be preserved.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Figure 8 (right) shows an example of a curve generated from the data on Figure 8 (left) with an algorithm that focuses only on local structure by choosing triplets as we discussed (with at least two points near each other per triplet). Here the triplet loss is approximately zero, but global structure would not be preserved. Thus, although the loss is optimized to make all neighbors close and all further points far, this can be accomplished amidst a complete sacrifice of global structure.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Similarly, consider any algorithm that uses attractive forces and/or repulsive forces (e.g.,

<!-- chunk {"id": "body-0090", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

where $\mathcal{T}_{NB}$ consists of neighbor pairs where attractive forces are applied and $\mathcal{T}_{\text{further}}$ consists of further-point pairs where repulsive forces are applied. Again, consider a simple 0-1 loss where $l^{\text{attract}}{(i,j)}$ is 0 if $i$ is close to $j$ in the low-dimensional space, and that $l^{\text{repulse}}{(i,k)}$ is 0 if $i$ and $k$ are far. Again, even when the total loss is zero, global structure need not be preserved, by the same logic as in the above example.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

From these two examples, we see that in order to preserve global structure, we must have forces on non-neighbors. If this requirement is not met, the relative distances between further points do not impact the loss, which, in turn, sacrifices global structure. Given this insight, let us consider what DR algorithms actually do.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Graph structure and repulsive forces for t-SNE: t-SNE attracts or repulses points by varying amounts, depending on the perplexity. The calculation below, however, shows that t-SNE's repulsive force has the issues we pinpointed: further points have little attractive or repulsive forces on them unless they are too close, meaning that t-SNE is "near-sighted."

<!-- chunk {"id": "body-0093", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

where $j$ is one of the other points. For simplicity, we denote $\|{\mathbf{y}_{i} - \mathbf{y}_{j}}\|$ as $d_{ij}$, and the unit vector in the direction of $i$ to $j$ as $\mathbf{e}_{ij}$. Recall that

<!-- chunk {"id": "body-0094", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

For a point $j$, we denote its force on $i$ (the $j$th term in the gradient above) as $\text{Force}_{ij}$. Following the separation of gradient given by van der Maaten,

<!-- chunk {"id": "body-0095", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Since $p_{ij}$, $q_{ij}$ and $d_{ij}$ are always non-negative, the two forces $F_{\text{attraction}}$ and $F_{\text{repulsion}}$ are always non-negative, pointing in directions opposite to each other along the unit vector $\mathbf{e}_{ij}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Both of these forces decay rapidly to 0 when $i$ and $j$ are non-neighbors in the original space, and when $d_{ij}$ is sufficiently large. Let us show this.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Attractive forces decay: The attractive term depends on $p_{ij}$, which is inversely proportional to the squared distance in the original space. Since we have assumed this distance to be large (i.e., $i$ and $j$ were assumed to be non-neighbors in the original space), its inverse is small. Thus the attractive force on non-neighbors is small.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

For most of the modern t-SNE implementations, $p_{ij}$ for most pairs is set to 0 within the code. In particular, if the perplexity is set to $Perplexity$, the algorithm considers 3$\cdot {Perplexity}$ nearest neighbors of each point. For points beyond these 3$\cdot {Perplexity}$, the attractive force will be set to 0. This operation directly implies that there are no attractive forces on non-neighbors.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Repulsive forces decay: The repulsive force does not depend on distances in the original space, yet also decays rapidly to 0. To see this, temporarily define $a_{ij}:=\frac{1}{1 + d_{ij}^{2}}$, and define $B_{ij}$ as $\sum_{{k \neq l},{{kl} \neq {ij}}}{({1 + d_{kl}^{2}})}^{- 1}$. Simplifying the second term of (5.1)

<!-- chunk {"id": "body-0100", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Further, the derivative of the forces smoothly decays to 0 as $d_{ij}$ grows.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

When $d_{ij}$ is large, the quartic term $B_{ij}d_{ij}^{4}$ will dominate the numerator, and the term $B_{ij}^{2}d_{ij}^{8}$ will dominate the denominator. Hence, when $d_{ij}$ is large, the force stays near 0.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Now that we have asymptotically shown that t-SNE has minimal forces on non-neighbors, we also want to check what happens empirically. Figure 9 provides a visualization of t-SNE's pairwise forces on the COIL-20 dataset. We can see that for different further pairs, the force applied on them is almost the same, and is vanishingly small. This means, in a similar way as discussed above, t-SNE cannot distinguish between further points, which explains why t-SNE loses its ability to preserve global structure.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Despite t-SNE favoring local structure, in its original implementation, it still calculates and uses distances between all pairs of points, most of which are far from each other and exert little force between them. The use of all pairwise distances causes t-SNE to run slowly. This limitation was improved in subsequent papers. Overall, it seems that we are better off selecting a subset of edges to work, rather than aiming to work with all of them simultaneously.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Graph structure and repulsive forces for UMAP: UMAP's forces exhibit tendencies similar to those of t-SNE's. Its attractive forces on neighbors and its repulsive forces decay rapidly with distance. As long as a further point is sufficiently far from point $i$ in the low-dimensional space, the force is minimal. Figure 10 (left) shows that most points are far enough away from each other that little pairwise force is exerted between them, either attractive or repulsive. UMAP has weights that scale these curves, however, the scaling does not change the shapes of these curves. Thus again, we can conclude that since UMAP does not aim to distinguish between further points, it will not necessarily preserve global structure.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Graph structure and repulsive forces for TriMap: In the thought experiment considered above, if no triplets are considered such that $j$ and $k$ are both far from $i$, the algorithm fails to distinguish the relative distances of further points and loses global structure.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Approximately 90% (55 triplets for each point, 50 of which involve a neighbor) of TriMap's triplets have $j$ as a neighbor of $i$. One would thus think its global structure preservation would arise from the 10% of random triplets--which are likely comprised of points that are all far from each other--but its global structure preservation does not arise from these random triplets. Instead, its global structure preservation seems to arise from its use of PCA initialization. Without PCA initialization, TriMap's global structure is ruined, as shown in Figure 11, where TriMap is run with and without the random triplets and PCA initialization. (More details are discussed in Section 6). Given that the small number of TriMap's random triplets have little effect on the final layouts, in the discussion below, we consider triplets that contain a neighbor for analyzing how TriMap optimizes on neighbors and further points.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Even though TriMap's rainbow figure does not look like that of the other loss functions, it still follows our technical principles, which are based on asymptotic properties. However, as discussed above, in spirit, Principle 5 should be concerned with pushing farther points away from each other that are very close, which corresponds to triplets that lie along the horizontal axis of the rainbow plot. Interestingly, TriMap's initialization causes Principle 5 to be somewhat unnecessary. After the PCA initialization (discussed above), there typically are no triplets on the bottom of the rainbow plot. This is because the PCA initialization tends to keep farther points separated from each other. In that way, TriMap manages to obey all of the principles, but only when the initialization allows it to avoid dealing with Principle 5.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

We can determine whether our principles are obeyed empirically by examining the forces on each neighbor $j$ and each further point $k$. We considered a moment during training of MNIST, at iteration 150 out of (a default of) 400 iterations. We first visualize the distribution of $d_{ij}$ and $d_{ik}$, shown in Figure 12a. From this figure, we observe that if we randomly draw a neighbor $j$ then $d_{ij}$ is small. Conversely, if we randomly draw a further point, $d_{ik}$ has a wide variance, but is not often small. The implication of Figure 12a is that most of TriMap's triplets will consist of a neighbor $j$ and a further point (that is far from both $i$ and $j$). This has implications for the forces on each neighbor $j$ and each further point $k$ as we will show in the next two paragraphs.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Let us calculate the forces on $i$'s neighbor $j$ that arise from the triplets associated with it. For neighbor $j$, TriMap's graph structure includes 5 triplets for it, each with a further point, denoted $(k_{1},k_{2},k_{3},k_{4},k_{5})$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

We now consider the loss $Loss_{ij}$ as a function of $d_{ij}$, viewing all other distances as fixed for this particular moment during training (when we calculate the gradients, we do not update the embedding). To estimate these forces during our single chosen iteration of MNIST, for each neighbor $j$, we randomly selected 5 $d_{ik}$ values among $d_{ik}$'s distribution and visualized their resulting attractive forces for $i$'s neighbor $j$. In Figure 12b, we visualize the results of 10 draws of the $d_{ik}$'s. This figure directly shows that Principles 4 and 6 seem to be obeyed.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

Again let us view $d_{ij}$ as a fixed number for this moment during training. Note from Figure 12a that $d_{ij}$ takes values mainly from $0$ to $3$, which means the set of values $0.3$, $1$, $2$, and $3$ are representative of the typical $d_{ij}$ values we would see in practice. We visualize the repulsive forces received by $k$ corresponding to these 4 typical values of $d_{ij}$, shown in Figure 12c. From this figure we see directly that violations of Principle 5 are avoided (as discussed above) since there are almost no points along the horizontal axis.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

The other important principles, namely Principles 2 and 3, require consideration of the forces relative to each other, which can be achieved by a balance between attractive and repulsive forces that cannot be shown in Figure 12.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Graph component selection and loss terms in most methods mainly favors preservation of local structure", "weight": 1.0} -->

What we have shown is that TriMap's loss approximately obeys our principles in practice, at least midway through its convergence, after the (very helpful) PCA initialization. However, the principles are necessary for local structure preservation but not sufficient for global structure preservation -- because TriMap attracts mainly its neighbors in the high-dimensional space (that is, because the attractive forces in Figure 12b apply only to neighbors), and because repulsion is again restricted to points that are very close, global structure need not be preserved.

<!-- chunk {"id": "body-0114", "role": "body", "section": "PaCMAP's graph structure using mid-near edges and dynamic choice of graph elements", "weight": 1.0} -->

As discussed above, if no forces are exerted on further points, global structure may not be preserved. This suggests that to preserve global structure, an algorithm should generally be able to distinguish between further points at different distances; it should not fail to distinguish between a point that is moderately distant and a point that is really far away. That is, if $j$ is much further than $k$, we should consider repulsing $k$ more than $j$, or attracting $j$ more than $k$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "PaCMAP's graph structure using mid-near edges and dynamic choice of graph elements", "weight": 1.0} -->

Let us discuss two defining elements of PaCMAP: its use of mid-near pairs, and its dynamic choice of graph elements for preservation of global structure. In early iterations, PaCMAP exerts strong attractive forces on mid-near pairs to create global structure, whereas in later iterations, it resorts to local neighborhood preservation through attraction of neighbors.

<!-- chunk {"id": "body-0116", "role": "body", "section": "PaCMAP's graph structure using mid-near edges and dynamic choice of graph elements", "weight": 1.0} -->

Mid-near pair construction: Mid-near points are weakly attracted. To construct a mid-near point for point $i$, PaCMAP randomly samples six other points (uniformly), and chooses the second nearest of these points to be a mid-near point. Here, the random sampling approach allows us to avoid computing a full ranked list of all points, which would be computationally expensive, but sampling still permits an approximate representation of the distribution of pairwise distances that suffices for choosing mid-near pairs.

<!-- chunk {"id": "body-0117", "role": "body", "section": "PaCMAP's graph structure using mid-near edges and dynamic choice of graph elements", "weight": 1.0} -->

Dynamic choice of graph elements: As we will discuss in more depth later, PaCMAP gradually reduces the attractive force on the mid-near pairs. Thus, in early iterations, the algorithm focuses on global structure: both neighbors and mid-near pairs are attracted, and the further points are repulsed. Over time, once the global structure is in place, the attractive force on the mid-near pairs decreases, then stabilizes and eventually disappears, leaving the algorithm to refine details of the local structure.

<!-- chunk {"id": "body-0118", "role": "body", "section": "PaCMAP's graph structure using mid-near edges and dynamic choice of graph elements", "weight": 1.0} -->

Recall that the rainbow figure conveys information only about local structure since it considers only neighbors and further points, and not mid-near points. From the rainbow figures, we note that strong attractive forces on neighbors and strong repulsive forces on further points operate in narrow ranges of the distance; if $i$ and $j$ are far from each other, there is little force placed on them. Because of this, the global structure created in the first stages of the algorithm tends to stay stable as the local structure is tuned later. In other words, the global structure is constructed early from the relatively strong attraction of mid-near pairs and gentle repulsion of further points; when those forces are relaxed, the algorithm concentrates on local attraction and repulsion.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Assigning weights for graph components is not always helpful", "weight": 1.0} -->

Besides the choice of graph components, some DR algorithms also assign weights for graph components based on the distance information in high-dimensional space. For example, a higher weight for a neighbor pair $(i,j)$ implies that neighbor $j$ is closer to $i$ in the high-dimensional space. The weights can be viewed as a softer choice of graph component selection (the weight is 0 if the component is not selected).

<!-- chunk {"id": "body-0120", "role": "body", "section": "Assigning weights for graph components is not always helpful", "weight": 1.0} -->

For TriMap, the weight computation is complicated, and yet the weights do not seem to have much of an effect on the final output; other factors (such as initialization and choice of graph components) seem to play a much larger role. In Figure 15, we showed what happens when we remove the weights (i.e., we assign all graph components to uniform weights) and the resulting performance turns out to be very similar on several datasets.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Assigning weights for graph components is not always helpful", "weight": 1.0} -->

In contrast to TriMap, we have elected not to use complicated formulas for weights in PaCMAP. All neighbors, mid-near points, and further points receive the same weights. These three weights change in a simple way over iterations.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Initialization Can Really Matter", "weight": 1.0} -->

Though issues with robustness of some algorithms are well known, in what follows, we present some insight into why they are not robust.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Some algorithms are not robust to random initialization", "weight": 1.0} -->

The various methods approach initialization differently: t-SNE uses random values, UMAP applies spectral embedding, and TriMap first runs PCA. According to the original papers, both UMAP and TriMap can be initialized randomly, but the specific initializations provided were argued to provide faster convergence and improve stability. However, just as much recent research has discovered, we found that the initialization has a much larger influence on the success rate than simply faster convergence and stability. When we used UMAP and TriMap with random initialization, which is shown in Figures 16 and 17, the results were substantially worse, even after convergence, and these poor results were robust across runs (that is, robustness was not impacted by initialization, the results were consistently poor). Even after tuning hyper-parameters, we were still unable to observe similar performance with random initialization as for careful initialization. In other words, the initialization seems to be a key driver of performance for both UMAP and TriMap. We briefly note that this point is further illustrated in Figures A.1 and A.2 where we apply MDS and spectral embedding.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Some algorithms are not robust to random initialization", "weight": 1.0} -->

An important reason why initialization matters so much for those algorithms is the limited "working zone" of attractive and repulsive forces induced by the loss, which was discussed in relation to Figure 7. Once a point is pushed outside of its neighbors' attractive forces, it is almost impossible to regain that neighbor, as there is little force (either attractive or repulsive) placed on it. This tends to cause false clusters, since clusters that should be attracted to each other are not. In other words, the fact that these algorithms are not robust to random initialization is a side-effect of the "near-sightedness" we discussed at length in the previous sections.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Some algorithms are not robust to random initialization", "weight": 1.0} -->

As discussed earlier, PaCMAP is fairly robust (but not completely robust) to the choice of initialization due to its mid-near points and dynamic graph structure.

<!-- chunk {"id": "body-0126", "role": "body", "section": "DR algorithms are often sensitive to the scale of initialization", "weight": 1.0} -->

Interestingly, DR algorithms are not scale invariant. Figure 18 shows this for the 2D curve dataset, where both the original and embedded space are 2D. Here we took the distances from the original data, and scaled them by a constant to initialize the algorithms, only to find that even this seemingly-innocuous transformation had a large impact on the result.

<!-- chunk {"id": "body-0127", "role": "body", "section": "DR algorithms are often sensitive to the scale of initialization", "weight": 1.0} -->

The middle row of Figure 18 is particularly interesting--the dataset is a 2D dataset, so one might presume that using the correct answer as the starting point would give the algorithms an advantage, since the algorithm simply needs to converge at the first iteration to achieve the correct result. However, even in this case, attractive and repulsive forces can exist, disintegrating global structure.

<!-- chunk {"id": "body-0128", "role": "body", "section": "DR algorithms are often sensitive to the scale of initialization", "weight": 1.0} -->

In the third row, all points start out far from each other because of the scaling, which multiplies all dimensions by 1000. As we know from our earlier analysis, repulsion forces fade as distances fade, explaining why the algorithms all achieved perfect results; however, scaling by 1000 will not work in general, instead it will generally lead the algorithm to stop at the first iteration. The warning here is always to initialize the low-dimensional embedding so that the forces are not all zero.

<!-- chunk {"id": "body-0129", "role": "body", "section": "DR algorithms are often sensitive to the scale of initialization", "weight": 1.0} -->

Hence, because DR methods are not generally scale-invariant, if the scale of the initialization is too large or too small relative to the distance range where attractive and repulsive forces are effective, this could lead to poor DR outcomes.

<!-- chunk {"id": "body-0130", "role": "body", "section": "The PaCMAP Algorithm", "weight": 1.0} -->

We now formally introduce the Pairwise Controlled Manifold Approximation Projection (PaCMAP) method. Algorithm 1 outlines the implementation of PaCMAP. Its key steps are graph construction, initialization of the solution, and iterative optimization using a custom gradient descent algorithm. In what follows we discuss its finer details and the reasoning behind the design choices.

<!-- chunk {"id": "body-0131", "role": "body", "section": "The PaCMAP Algorithm", "weight": 1.0} -->

0: • X - high-dimensional data matrix. • nN B - the number of neighbor pairs (default values: nN B = 10). • M N _, F P _ - the ratio between the number of mid-near pairs and further pairs with to the number of neighbor pairs (default values: M N _ = 0.5, F P _ = 2). • niterations - the number of gradient steps (default value: niterations = 450). • i n i t - initialization procedure for the lower dim. embedding (default i n i t= PCA, alternatively, i n i t = r a n d o m, which initializes Y using the multivariate Normal distribution 𝒩 (0,10−4 I), with I denoting the two-dimensional identity matrix; alternatively, ). • τ1, τ2, τ3 - beginning of the three optimization phases, satisfying τ1 = 1 ≤ τ2 ≤ τ3 ≤ niterations (default values: τ1 = 1, τ2 = 101, τ3 = 201).

<!-- chunk {"id": "body-0132", "role": "body", "section": "The PaCMAP Algorithm", "weight": 1.0} -->

• wN B, wM N, wF P – the weights associated with neighbor, mid-near, and further pairs at iteration t. The default values are: - for t ∈ [τ1, τ2): ${w_{NB} = 2},{{{w_{MN}{(t)}} = {{1000 \cdot \left( {1 - \frac{t - 1}{\tau_{2} - 1}} \right)} + {3 \cdot \frac{t - 1}{\tau_{2} - 1}}}},{w_{FP} = 1}}$; - for t ∈ [τ2, τ3): wN B = 3, wM N = 3, wF P = 1; - for t ∈ [τ3, niterations]: wN B = 1, wM N = 0, wF P = 1. 0: • Y - low-dimensional data matrix. • construct nN B neighbor edges by computing the nN B nearest neighbors of xi using scaled distances di j2, select.

<!-- chunk {"id": "body-0133", "role": "body", "section": "The PaCMAP Algorithm", "weight": 1.0} -->

To take advantage of existing implementations of k-NN algorithms, for each sample we first select the min (nN B + 50,N) nearest neighbors according to the Euclidean distance and from this subset we pick the nN B nearest neighbors according to the scaled distance di j2, select (recall that N is the total number of observations). • construct nM N = ⌊nN B × M N _⌋ mid-near pairs. For each pair, construct it by sampling 6 observations, using xi and the 2nd nearest observation to xi as the mid-near pair. • construct nF P = ⌊nN B × F P _⌋ further pairs by sampling non-neighbor points. • apply the initialization procedure i n i t to set the initial values of Y.
• run AdamOptimizer niterations iterations to optimize the loss function LossPaCMAP while simultaneously adjusting the weights according to the above scheme.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Graph construction", "weight": 1.0} -->

PaCMAP uses edges as graph components. As discussed earlier, PaCMAP distinguishes between three types of edges: neighbor pairs, mid-near pairs, and further pairs. The first group consists of the $n_{NB}$ nearest neighbors from each observation in the high-dimensional space.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Graph construction", "weight": 1.0} -->

where $\sigma_{i}$ is the average distance between $i$ and its Euclidean nearest fourth to sixth neighbors. These are used to construct the neighbor pairs ${{{(i,j_{t})},t} = 1},{2,\ldots,n_{NB}}$. The scaling is performed to account for the fact that neighborhoods in different parts of the feature space could be of significantly different magnitudes. Here, the scaled distances $d_{ij}^{2,\text{select}}$ are used only for selecting neighbors; they are not used during optimization.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Graph construction", "weight": 1.0} -->

As discussed in Section 5.2, the second group consists of $N \cdot n_{MN}$ mid-near pairs selected by randomly sampling from each observation 6 additional observations and using the second smallest of them for the mid-near pair. Finally, the third group consists of a random selection of $n_{FP}$ further points from each observation. For convenience, the number of mid-near and further point pairs is determined by the parameters $MN\_$ and $FP\_$ that specify the ratio of these quantities to the number of nearest neighbors, that is, $n_{MN} = {{MN\_} \cdot n_{NB}}$ and $n_{FP} = {{FP\_} \cdot n_{NB}}$. Since the number of neighbors $n_{NB}$ is typically an order of magnitude smaller than the total number of observations, random sampling effectively chooses non-nearest neighbors as mid-near and further pairs. We note that the decision to choose pairs randomly rather than deterministically (e.g., certain fixed quantiles) is aimed at reducing the computational burden.

<!-- chunk {"id": "body-0137", "role": "body", "section": "The loss function", "weight": 1.0} -->

Where ${\overset{\sim}{d}}_{ab} = {{\|{\mathbf{y}_{a} - \mathbf{y}_{b}}\|}^{2} + 1}$. The pairs are further weighted by the coefficients $w_{NB}$, $w_{MN}$, and $w_{FP}$, which altogether account for the total loss. The weights are updated dynamically during the algorithm according to a scheme we describe as part of the optimization process. The particular choice of using the transformed distance $\overset{\sim}{d}$ is motivated by the Student's t-distribution used in the similarity functions of t-SNE and TriMap. The choice of loss terms could be thought of as related to TriMap's triplet loss, but where the triplet has been decoupled and the third point is fixed. This loss was also motivated by the principles for good loss functions, discussed further in Section 4.5.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Initialization of PaCMAP", "weight": 1.0} -->

While PaCMAP's outcomes are fairly insensitive to the initialization method, we can still use PCA to improve the running time. See Section 6 for additional details.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Dynamic Optimization", "weight": 1.0} -->

The optimization process consists of three phases, which are designed to avoid local optima. In the first phase (iterations $\tau_{1} = 1$ to $\tau_{2} - 1$), the goal is to improve the initial placement of embedded points to one that preserves, to a certain degree, both the global and local structures, but mainly the global structure. This is achieved by heavily weighing the mid-near pairs. Over the course of the first phase, we gradually decrease the weights on the mid-near pairs, which allows the algorithm to gradually refocus from global structure to local structure. In the second phase (iterations $\tau_{2}$ to $\tau_{3} - 1$), the goal is to improve the local structure while maintaining the global structure captured during the first phase by assigning a small (but not zero) weight for mid-near pairs.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Dynamic Optimization", "weight": 1.0} -->

Together, the first two phases try to avoid local optima using a process that bares similarities with simulated annealing and the "early exaggeration" technique used by t-SNE. However, early exaggeration places more emphasis on neighbors, rather than mid-near points, whereas PaCMAP focuses on mid-near pairs first and neighbors later. The key hurdles that these phases try to avoid are: first, neglecting to place forces on non-near further points, which ignores global structure; and second, placing neighbors in the low-dimensional space too far away from each other in early iterations, causing the derivatives to saturate, which makes it difficult for these neighbors to become close again. This would lead to false clusters in the low-dimensional embedding. The effect of the three-stage dynamic optimization is demonstrated in Figures 19 and 20. In these two figures, PaCMAP is implemented with random initialization rather than PCA initialization which is the default choice.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Dynamic Optimization", "weight": 1.0} -->

(This figure shows that, although PCA initialization can help PaCMAP achieve more stable global structure, PaCMAP does not rely on PCA initialization to capture global structure.) With random initialization, these two figures can better demonstrate how PaCMAP actually works.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Dynamic Optimization", "weight": 1.0} -->

Finally, in the third phase (iterations $\tau_{3}$ to $n_{\text{iterations}}$), the focus is on improving the local structure by reducing the weight of mid-near pairs to zero and that of neighbors to a smaller value, emphasizing the role of the repulsive force to help separate possible clusters and make their boundary clearer. The third stage seems to have a larger effect on datasets with primarily local structure, like MNIST (Figure 20) as compared with datasets with global structure, such as Mammoth (Figure 19).

<!-- chunk {"id": "body-0143", "role": "body", "section": "Dynamic Optimization", "weight": 1.0} -->

The algorithm uses AdamOptimizer, a modern stochastic gradient descent algorithm. Section 3 reviews the specific algorithms used by the other DR methods.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Dynamic Optimization", "weight": 1.0} -->

As we will see in the experiments, PaCMAP has several characteristics worth noting: it tends to favor global structure when such structure exists, and also preserves local structure when such structure exists (the fact that its loss function obeys the principles above helps to ensure this). Its run time results give it a unique advantage, as well as the fact that its results are not nearly as sensitive to the choice of initialization procedure as other methods.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

In this section, we report on the results of a numerical study conducted to assess the quality of PaCMAP on a wide range of datasets, and compare it against leading DR methods. Although PaCMAP is able to reduce a dataset to an arbitrary number of dimensions, we only consider the two dimensional case for visualization purpose in this paper.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Overall, we find that PaCMAP achieves a good balance of local and global structure: for datasets that mainly consist of local structure, it performs as well as algorithms that specifically preserve local structure (e.g., UMAP), while for datasets that consist of mainly global structure, it performs comparably with global structure-preservation algorithms (e.g., TriMap). PaCMAP also seems to be fairly robust in its hyperparameter choices (within non-extreme ranges for those parameters). We find that PaCMAP is significantly faster than other algorithms in runtime experiments.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Algorithms", "weight": 1.0} -->

We compare PaCMAP against t-SNE, UMAP, TriMap (Section 3), as well as LargeVis. DR methods are known to be sensitive to the selection of hyperparameters and there is no single hyperparameter setting would be expected to fit all the datasets. Thus, we selected three different hyperparameters that fall into the suggested tuning ranges for each algorithm. We report the best of these three hyperparameter results on each metric. The specific hyperparameter values we chose for each algorithm are: t-SNE, perplexity $\in$ {10, 20, 40}; UMAP, $n_{NB}$ $\in$ {10, 20, 40}; TriMap, $n_{inlier}$ $\in$ {8, 10, 15}; LargeVis, perplexity $\in$ {30, 50, 80}; and PaCMAP, $n_{NB} \in$ {5, 10, 20}.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Datasets", "weight": 1.0} -->

Similarly to other studies of DR methods, we use the following datasets to evaluate and compare DR methods: Olivetti Faces, COIL-20, COIL-100, S-curve with hole dataset (synthesized by the authors), Mammoth, USPS, MNIST, FMNIST, Mouse scRNA-seq, 20 NewsGroups, Flow cytometry, and KDD Cup 99. Note that the S-curve with hole dataset, the Mouse scRNA-seq dataset and the Flow cytometry dataset do not possess class labels.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Metrics and methodology", "weight": 1.0} -->

Similarly to other works, we use labeled datasets to assess the quality of the various DR methods, where labels are only used for evaluation once the DR algorithms complete their execution. We consider various types of measures to capture the preservation of local and global structure.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Metrics and methodology", "weight": 1.0} -->

The quality of the preservation of local structure is measured in two ways. First by applying leave-one-out cross validation using the K-Nearest Neighbors (KNN) classifier. This has become a standard evaluation method for DR. The intuition behind this method is that labels tend to be similar in small neighborhoods and therefore the classification accuracy based on neighborhoods would remain close to that in the high-dimensional space. Moreover, one would expect the prediction accuracy of KNN to deteriorate if the DR method does not preserve neighborhoods. For each dataset and algorithm, we performed hyper-parameter tuning for the number of neighbors $k$. We denote this metric as KNN Accuracy.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Metrics and methodology", "weight": 1.0} -->

In addition, we measure the accuracy of nonlinear support vector machine (SVM) models with a radial basis function (RBF) kernel using 5-fold cross validation. Similarly to KNN, the SVM accuracy measures the cohesiveness of neighborhoods, but this is done in a potentially more flexible manner that is less impacted by the density of the data. Specifically, for each DR method we partition the embedding into 5 folds, each time using 4 folds as the training data for the SVM model and using the remaining fold for the evaluation of accuracy. To further reduce the running time, we used the Nyström method, which approximates the kernel matrix by a low rank matrix, using sklearn.kernel_approximation.Nystroem. Thereafter, we trained linear SVM models (using sklearn.svm.LinearSVC) on the non-linearly transformed features. We denote this metric as SVM Accuracy.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Metrics and methodology", "weight": 1.0} -->

To measure the preservation of global structure, that is the relative positioning of neighborhoods, we sample observations and compute the Random Triplet Accuracy, which is the percentage of triplets whose relative distance in the high- and low-dimensional spaces maintain their relative order. For numerical tractability, we use a sample of triplets rather than considering all triplets. Due to randomness, we apply this metric for five times and report the mean value and standard deviation. Note that random triplet accuracy does not require labels, so we can evaluate it on unlabeled datasets. In the same spirit, but at a lower resolution, for labeled datasets, we also measure global structure preservation by computing the centroids of each class in the high- and low-dimensional spaces, and construct triplets using the relative distances between centroids in the high-dimensional space. We report the percentage of preserved centroid triplets, denoted as Centroid Triplet Accuracy.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Computational environment", "weight": 1.0} -->

We implemented PaCMAP in Python by adapting code from TriMap and using the packages ANNOY and Numba. We used the following implementations for the other DR methods: t-SNE, LargeVis, UMAP, and TriMap. The algorithms were executed on a Dell R730 Server with 2 Intel Xeon E5-2640 v4 2.4GHz CPU. We limited the memory usage to 64 GB and runtime to 24 hours. The code for the numerical experiment is available online at

<!-- chunk {"id": "body-0154", "role": "body", "section": "Qualitative assessment", "weight": 1.0} -->

Figures 21 and 22 show the output of the various DR methods (rows correspond to datasets and columns to DR methods; additional results are presented in Appendix A). We observe that t-SNE tends to distribute data fairly uniformly around the space, which may potentially contribute to the preservation of local structure and hinder the preservation of the global structure. In the particular example of the MNIST dataset, we see that this actually results in creating false clusters (the yellow and red clusters are split into two parts). We also observe that UMAP and LargeVis tend to nicely preserve local structure (observed through cleaner separation of classes), while TriMap tends to focus on the global structure (as seen by its application to the S-curve dataset, and by better preservation of relative distances between clusters in the COIL-20, COIL-100 and MNIST datasets) at the cost of local structure. The figures suggest that PaCMAP balances between local and global, where for datasets that have mainly local structure, it tends to behave like UMAP (preserving local structure), whereas for datasets that have mainly global structure, it tends to behave more like TriMap (preserving global structure).

<!-- chunk {"id": "body-0155", "role": "body", "section": "Preservation of local structure", "weight": 1.0} -->

In terms of SVM accuracy, PaCMAP achieved the best performance for more of the datasets than other algorithms, demonstrating its ability to preserve manifold structures on complicated datasets. Again, not favoring local structure, TriMap (and LargeVis, which also favors local structure) performed poorly on this particular experiment.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Preservation of local structure", "weight": 1.0} -->

We also observe that there is a gap between the baseline prediction and the predictions made in lower dimensions. This indicates that the neighborhoods are not perfectly preserved, which could result from the limited capacity of the lower dimension space.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Preservation of local structure", "weight": 1.0} -->

To summarize, methods that favor preservation of local structure (UMAP, t-SNE) tend to perform better on local-preservation metrics, along with PaCMAP, which also preserves local structure and performs well.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Preservation of global structure", "weight": 1.0} -->

Tables 3 and 4 show the average and standard deviation of the random triplet accuracy and centroid triplet accuracy, respectively. These global structure metrics are where algorithms like PaCMAP and TriMap really shine. It is worth noting that unlike UMAP and TriMap, which gain their global structure through initialization (see Section 5.1), PaCMAP creates the global structure completely through its graph component selection and dynamic changes in the component selection, as we have shown in Sections 5.2 and 7. An additional comparison with random initialization is provided in Section 8.3.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Preservation of global structure", "weight": 1.0} -->

In short, PaCMAP preserves global structure, without sacrificing local structure or depending on initialization.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Preservation of global structure", "weight": 1.0} -->

We note that t-SNE, which performed well on the local structure metrics for F-MNIST, has one of the worst performance results with respect to global structure on F-MNIST.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Run time", "weight": 1.0} -->

Table 5 compares the running time of the different algorithms. PaCMAP is significantly faster than other algorithms, attaining a speedup of more than 1.5 times faster than other methods for most datasets. It can also run efficiently on large-scale datasets, such as the Flow Cytometry and KDD datasets, whereas multiple DR algorithm failed to converge under the time limit or ran out of memory. PaCMAP's speed can be attributed to the design of its loss function which reduces the number of pairs that need to be considered at each iteration, which reduces the usage of computing and memory resources.

<!-- chunk {"id": "body-0162", "role": "body", "section": "PaCMAP-specific considerations and sensitivity analysis", "weight": 1.0} -->

The most important parameters for controlling PaCMAP behavior are $n_{NB}$, $MN\_$, $FP\_$, and $init$. The meaning of each parameter can be found in Section 7. PaCMAP uses the following default parameters: $n_{NB} = 10$, ${MN\_} = 0.5$, ${FP\_} = 2$, and $init$ = PCA. In this subsection, we will perform sensitivity analyses for each of them and assess performance qualitatively.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Robustness to initialization", "weight": 1.0} -->

We discussed TriMap's heavy dependence on initialization in Section 6 and Figure 16.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In this study, our goal was to empirically dissect what approaches to dimension reduction work and what do not, using a selection of datasets for which local- and global-structure preservation needs are different, and where the algorithms could be visually evaluated after projecting to two dimensions.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

The observations from our studies turned out to yield valuable and unexpected results, particularly in showing what is not necessarily important for DR: while some of the loss functions and forces are motivated through probabilistic modeling (e.g., t-SNE) or mathematical constructs such as simplices (UMAP), these extra layers of statistics and mathematics may obscure a simple explanation of the how these methods are similar or different from each other, or what is important in general. We showed that the derivations for these other algorithms are modeling choices, rather than choices inherent to the problem: there is no inherent reason why neighbors should be probabilistically related to each other, nor that an understanding of simplices are necessary for deriving DR algorithms; TriMap's and PaCMAP's purely loss-based approaches are also equally feasible modeling choices.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

By seeing the results of these choices empirically, we showed that several seemingly important aspects of several DR algorithms do not drive performance, and can actually hurt it. In particular, we showed several reasons that t-SNE and UMAP's weighting choices and graph component selections do not preserve global structure. In particular, they leave out forces on further points, making these algorithms "near-sighted" in preserving only local structure. Even TriMap has this problem; we showed that a key driver of TriMap's excellent performance on global structure is a seemingly-innocent initialization choice.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In striving to compare algorithms, we found that the rainbow figures and their accompanying force plots provide insight into what principles a good loss function for DR should possess; straying from these principles destroys the DR result. These principles, in turn, led to the development of a simple loss, comprised of three simple fractional losses that, when combined with other insights, yield the powerful and robust PaCMAP algorithm.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Its choice of graph components ensures that further points have non-zero forces, which remedies a fault we found in other algorithms. This observation is a key to preservation of global structure that is not found in other methods.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Its dynamic graph component selection focuses on global structure in early iterations, fine-tuning local structure at later iterations, allowing the result to preserve both local and global structure. It behaves like UMAP for datasets that mainly have local structure characteristics, and behaves like TriMap for datasets whose important structure is global. Unlike TriMap, it does not rely on initialization to preserve global structure; its dynamic graph component selection ensures that it performs well even under random initialization.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Its loss function does not require triplets and does not use too many unnecessary graph components, leading to faster computation and convergence times.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Its performance is relatively robust within reasonable parameter choices.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

The qualitative performance results we examine for PaCMAP led directly to high-quality quantitative results measured on 12 datasets.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

There are many avenues for future work. First, one could consider the possibility of a continuum between local and global structure. While considering a simple dichotomy between local and global has been convenient, it is possible that the data contains multi-scale or hierarchical structure at many levels. We provide an analysis of a simple synthetic dataset with hierarchical structure in Appendix B, where all methods have difficulty displaying structure on all levels of the hierarchy (although PaCMAP slightly outperforms other methods). A second direction for future work is to study very large scale datasets, particularly in high dimensions. Large datasets pose problems for DR methods, both in scaling DR methods to handle data of such sizes, but also, parameters that have been tuned on smaller datasets often do not extend to good performance on larger datasets. Determining what adjustments need to be made for larger datasets is an important direction for future work. Third, there are open questions about the combination of distance metric learning in high dimensions and how it might couple with DR methods.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

If we do not know the distance metric perfectly, learning it so that DR behaves well might be useful; on the other hand, combining distance metric learning with DR risks luring the method towards distance metrics that may be unfaithful to the data just so that DR results look convincing. Fourth, the development of evaluation metrics is important for DR. We have introduced several evaluation metrics that we have found useful. It is possible that other evaluation metrics might also be useful, and it could be possible to develop specialized metrics for various application domains. Finally, one could use the general principles established in this work to design new DR methods. These new algorithms could have very different functional forms than PaCMAP while still obeying the principles we have established. The principles open the door to a wide variety of other algorithms and new ways to design them.
