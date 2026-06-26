<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Discovering the Elite Hypervolume by Leveraging Interspecies Correlation

Topics include Robotics.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Evolution has produced an astonishing diversity of species, each filling a different niche. Algorithms like MAP-Elites mimic this divergent evolutionary process to find a set of behaviorally diverse but high-performing solutions, called the elites. Our key insight is that species in nature often share a surprisingly large part of their genome, in spite of occupying very different niches; similarly, the elites are likely to be concentrated in a specific "elite hypervolume" whose shape is defined by their common features. In this paper, we first introduce the elite hypervolume concept and propose two metrics to characterize it: the genotypic spread and the genotypic similarity. We then introduce a new variation operator, called "directional variation", that exploits interspecies (or inter-elites) correlations to accelerate the MAP-Elites algorithm. We demonstrate the effectiveness of this operator in three problems (a toy function, a redundant robotic arm, and a hexapod robot).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The astonishing diversity and elegance of life forms has long been an inspiration for creative algorithms that attempt to mimic the evolutionary process. Nevertheless, current evolutionary algorithms primarily view evolution as an optimization process, that is, they aim at performance, not diversity. It is therefore no wonder that most experiments in evolutionary computation do not show an explosion of diverse and surprising designs, but show instead a convergence to a single, rarely surprising "solution".

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This view of artificial evolution has recently been challenged by a new family of algorithms that focus more on diversification than on optimization. This does not mean that performance --- fitness --- does not play any role: inside an ecological niche, individuals compete and optimize their fitness; but two species in two different niches are not competing directly. These algorithms are called "illumination algorithms", because they "illuminate the search space", or "quality diversity algorithms", because they search for a set of diverse, but high-performing solutions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current illumination algorithms essentially differ in the way they define niches and in how they bias the selection of individuals to reproduce. We are here interested in the Multi-dimensional Archive of Phenotypic Elites (MAP-Elites) algorithm, because it produces high-quality results, while being conceptually simple and straightforward to implement. MAP-Elites explicitly divides the behavior space in niches using a regular grid or a centroidal Voronoi tessellation (CVT) and each niche stores the best individual found so far, called the elite. MAP-Elites was successfully used to create high-performing behavioral repertoires for robots, design airfoils and soft robots, evolve images that "fool" deep neural networks, "innovation engines" able to generate images that resemble natural objects, and 3D-printable objects by leveraging feedback from neural networks trained on 2D images.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While being effective at generating a diverse set of high-performing solutions, MAP-Elites requires numerous fitness evaluations to do so. For instance, a few million evaluations are typically used when evolving behavioral repertoires for robots. The objective of this paper is to propose an updated MAP-Elites that uses fewer evaluations for similar or better results.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main insight is that the high-performing solutions in different niches often share many traits, even when they look very different. In nature, a tiny worm like C. Elegans uses neurons and cells that are similar to those used by humans, insects, and all the other animal life forms. Similarly, all the bird species have a beak, two wings, a heart, and two lungs, but they occupy widely diverse niches, from the sea to tropical forests. Modern genomic analyses confirm this idea: species that occupy very different niches often share a surprisingly large part of their genome. For example, fruit flies and humans share about 60 percent of their genes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

If we translate the concept that "high-performing species have many things in common" to evolutionary computation, we conclude that all the elites of the search space, as found by MAP-Elites, are likely to be concentrated in a sub-part of the genotypic space (Fig. 1). We propose to call this sub-part of the genotypic space the "elite hypervolume". Describing this sub-part would correspond to writing the "recipe" for high-performing solutions. For instance, all the high-speed walking controllers might need to use the same high-frequency oscillator, in spite of very different gait patterns. This idea might be counter-intuitive at first, because we would expect that a well spread set of behaviors would correspond to a well spread set of genotypes, but this is the case only when there exists a linear mapping between genotypes and behaviors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the more general case, many genotypes can lead to the same behavior (e.g., there are many ways of not moving for a walking robot), and we should expect that competition between solutions will make it likely that survivors share some traits (e.g., a good balancing controller is useful for any gait).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first objective of the present paper is to empirically show that elites are often concentrated in a small elite hypervolume whose shape reflects the common features of high-performing solutions. The second objective is to introduce a variation operator that exploits the correlations between the elites, that is, the "interspecies" similarities that define the elite hypervolume.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Illumination / Quality Diversity", "weight": 1.0} -->

Illumination algorithms originated in the field of evolutionary robotics with the purpose of encouraging diversity in a space known as the behavior space. This space describes the possible behaviors of individuals over their lifetimes: for example, a point in this space, i.e., a behavior descriptor, could be the final positions of simulated robots whose controllers are evolved. In contrast, the genotype space is the space in which the evolutionary algorithm operates (e.g., a space of bit strings) and the phenotype space encodes the possible controllers (e.g., neural networks) that are derived from the genotype space.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Illumination / Quality Diversity", "weight": 1.0} -->

Current illumination algorithms define niches and bias selection in different ways. The two main algorithms are currently MAP-Elites, which defines niches with a grid and selects uniformly among the elites, and Novelty Search with Local Competition, which defines niches using a neighborhood based on a behavioral distance and selects using a multi-objective ranking between density in behavior space and performance. Depending on the task, selection biases can be introduced in all the algorithms. For instance, MAP-Elites can be modified to bias selection towards sparse regions, which can be facilitated using a tree structure.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Illumination / Quality Diversity", "weight": 1.0} -->

To our knowledge, there is no explicit consideration for variation operators in the current algorithms: they use the variation operators that were designed for previous work with objective-based evolutionary algorithms (e.g., real-valued genetic algorithms (GAs) or the NEAT operators for neural networks ).

<!-- chunk {"id": "body-0014", "role": "body", "section": "The CVT-MAP-Elites Algorithm", "weight": 1.0} -->

2: 𝒞← CVT(k) ⊳ Run CVT and get the centroids 3: (𝒳, 𝒫)← create_empty_archive(k) 4: for i = 1 → G do ⊳ Initialization: G random x 7: for i = 1 → I do ⊳ Main loop, I iterations 12:procedure add_to_archive(x, 𝒳, 𝒫) 14: c← get_index_of_closest_centroid(b, 𝒞) Algorithm 1 CVT-MAP-Elites algorithm We here use the CVT-MAP-Elites algorithm with uniform selection, which generalizes MAP-Elites to arbitrary dimensions and provides explicit control over the desired number of niches.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The CVT-MAP-Elites Algorithm", "weight": 1.0} -->

CVT-Map-Elites first partitions the behavior space into $k$ well-spread centroids (niches) using a CVT (Alg. 1, line 2). It then creates an empty archive with capacity $k$ ($\mathcal{X}$ and $\mathcal{P}$ store the genotypes and performances, respectively). At the first generation, the algorithm samples a set of random genotypes (line 5) and evaluates them by recording their performance and behavior descriptor (line 13); it calculates the centroid closest to each behavior descriptor (line 14) and stores the individual in the archive only if the corresponding region is empty or has a less fit solution (lines 15,16). The main loop of the algorithm corresponds to selecting a random parent (line 8), varying the parent to create the offspring (line 9) and attempting to insert it in the archive as above. Note that there is no specific strategy for variation, which we address in this paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Exploiting Correlations in Evolutionary Algorithms", "weight": 1.0} -->

In evolution strategies (ES), correlations between variables can be exploited by allowing each population member to maintain a multivariate Gaussian distribution (in the form of different mutation strengths and rotation angles). Modern variants of ES (such as or ) and other estimation of distribution algorithms (EDAs), exploit such correlations by building probabilistic models (that act as search distributions) from which they sample the next population. EDAs have been augmented with niching mechanisms to address multimodal optimization problems; however, they have never been used for illumination^11^1A combination of ES and techniques from illumination algorithms have been proposed recently, but not for the purpose of illumination..

<!-- chunk {"id": "body-0017", "role": "body", "section": "Exploiting Correlations in Evolutionary Algorithms", "weight": 1.0} -->

In GAs, commonalities between solutions can be exploited by the recombination operator. In real-coded GAs, parent-centric operators, i.e., ones that create solutions near the parent with more probability, can be more beneficial than mean-centric ones (e.g., ), especially when the population has not surrounded the optimum. One of the most successful parent-centric operators is the simulated binary crossover (SBX), which creates two offspring from two randomly selected parents using a polynomial distribution. By spreading the offspring in proportion to the spread of the parents, SBX endows GAs with self-adaptive properties similar to ES. A variant of SBX produces the offspring along a line that joins two parents, thus, being able to exploit linear correlations between them. To our knowledge, there has not been any study about exploiting correlations with a crossover operator when niching is performed either in phenotype or in behavior space.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Tasks", "weight": 1.0} -->

We perform our experiments in the following tasks, where $\mathbf{x} \in {\lbrack 0,1\rbrack}^{n}$ is the genotype, $\mathbf{y}$ is the phenotype, and the genotype-phenotype map is a linear scaling to the range described below.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Schwefel's Function 1.2", "weight": 1.0} -->

This is a classic function used when benchmarking optimization algorithms. The objective is to maximize ${f{(\mathbf{y})}} = {- {\sum_{i = 1}^{n}\left( {\sum_{j = 1}^{i}y_{j}} \right)^{2}}}$. We use a 100-dimensional genotype space ($\mathbf{y} \in {\lbrack{- 5},5\rbrack}^{100}$) and set the behavior descriptor to be the first 2 phenotypic dimensions (${\mathbf{b}{(\mathbf{y})}} \in {\lbrack{- 5},5\rbrack}^{2}$).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Arm Repertoire", "weight": 1.0} -->

The purpose of this experiment is to create a repertoire of joint angles for a redundant robotic arm for which the resulting end effector positions cover its reachable space. After convergence, each filled niche will contain a solution to its corresponding inverse kinematics (IK) problem, i.e., a joint configuration that takes the end effector inside the region; the goal of the illumination algorithm is, thus, to collect solutions for thousands of IK problems (one per region) in a single run.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Arm Repertoire", "weight": 1.0} -->

We use a 12-degree of freedom (DOF) arm in 2D space, where each joint is a revolute one (no joint limit), and we find the end effector position using the forward kinematics equations: where $n = 12$, each link length $l_{i} = {1/n}$, $y_{i}$ is a joint angle (thus, the phenotype space is the joint space, $\mathbf{y} \in {\lbrack{- \pi},\pi\rbrack}^{12}$), and ${\mathbf{b}{(\mathbf{y})}} \in {\lbrack{- 1},1\rbrack}^{2}$ is the behavior descriptor.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hexapod Locomotion", "weight": 1.0} -->

The final experiment is the hexapod locomotion task of ^22^2We implemented this task using the Dynamic Animation and Robotics Toolkit.. The objective is to maximize the distance covered by the hexapod robot in 5 seconds. The controller is an open-loop oscillator that actuates each motor by a periodic signal of frequency $1Hz$ parameterized by the amplitude, its phase shift and its duty cycle (i.e., the fraction of each period that the joint angle is positive). Each leg has 3 joints, however, only the movement of the first 2 is defined in the genotype (as the control signal of the third motor of each leg is the opposite of the second one). This results in a 36D genotype space ($\mathbf{y} \in {\lbrack 0,1\rbrack}^{36}$), as there are 6 parameters for each of the 6 legs of the robot.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Hexapod Locomotion", "weight": 1.0} -->

The behavior descriptor ${\mathbf{b}{(\mathbf{y})}} \in {\lbrack 0,1\rbrack}^{6}$ is defined as the proportion of time each leg is in contact with the ground (${dt} = {15ms}$, thus, the number of simulation steps $T = {{{5sec}/15}ms} = 333$).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Metrics", "weight": 1.0} -->

We study each elite hypervolume, $E{(t)}$, using the archives provided by CVT-MAP-Elites at a given time $t$ (number of evaluations), with the following metrics: Figure 3. Example with a 2-DOF robotic arm that needs to reach thousands of points in 2D space (upper row; task/behavior space, where niching is performed). Each white region in task space is an empty niche, whereas each colored region corresponds to a genotype, i.e., 2 joint angles (bottom row; genotype/parameter space). The number of points in genotype space show the archive size at a given generation, since only one, elite genotype can occupy a niche. The fitness is the negative variance of the joints, thus, solutions along the diagonal (bottom row) have higher fitness. The color reflects the fitness value. The elites of each generation are noisy samples from the volume we are interested in finding (gen. 5000, bottom row).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Metrics", "weight": 1.0} -->

Spread can be interpreted as the mean distance to the nearest neighbor normalized by the maximum possible distance (in the bounding volume of the genotype space ${\lbrack 0,1\rbrack}^{n}$), and similarity is the mean of the average pairwise distances normalized by the maximum possible distance, thus, representing a fraction, and subtracted from 1 so that a higher value means more similar in terms of percentage.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Metrics", "weight": 1.0} -->

When taken together, these two metrics^55^5Other metrics can be considered, such as number of clusters, correlation of solutions in each cluster, volume, geometric span, or others based on manifold learning algorithms, however, the ones we present here are representative for our objective in this paper. can roughly characterize three different situations: a uniformly spaced set of points has high spread and low similarity (Fig. 2, left); a single cluster of points has low spread and high similarity (Fig. 2, middle); and multiple clusters of points have low spread and low similarity (Fig. 2, right).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Elite Hypervolume for each task", "weight": 1.0} -->

We run the CVT-MAP-Elites algorithm in each task to study the corresponding elite hypervolume. Any other illumination/quality diversity algorithm could be used instead of CVT-MAP-Elites.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Elite Hypervolume for each task", "weight": 1.0} -->

We first run the kinematic arm task with a 2-DOF arm (Fig. 3), which allows us to visualize the elite hypervolume in 2D. The initial, randomly generated elites are evenly spread in the genotypic space (generation 0); however, once CVT-MAP-Elites has converged (here after 5000 generations), the elites are concentrated in a very particular (non-convex) volume in the genotype space (Fig. 3, last panel). The highest performing solutions are on a diagonal line (they correspond to a fitness of $0$, for which the two joint angles are equal), but occupying the other behavioral niches requires to have a lower fitness.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Elite Hypervolume for each task", "weight": 1.0} -->

We then move on with the tasks described in Section 3. For the experiments with the Schwefel function and the robotic arm, we use 30 replicates of 100k evaluations. The hexapod experiment is a more difficult task, therefore, we use 500k evaluations; since it is computationally more expensive, we use 20 replicates.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Elite Hypervolume for each task", "weight": 1.0} -->

In all tasks, the spread of the solutions becomes lower as we increase the number of evaluations (Fig.4; the differences between pairs are highly significant, $p < 10^{- 7}$ Mann-Whitney U test). On the other hand, the similarity of the elites (Fig.5) increases with the number of evaluations in the Schwefel function and the arm task ($p < 10^{- 11}$), but not in the hexapod task ($p = 0.64$ between 250k and 500k, $p < 10^{- 7}$ for the other pairs). This shows that in the Schwefel function and the arm task, the elites become more concentrated into an elite hypervolume, thus, it should be possible to easily exploit their similarities and accelerate illumination. In the hexapod task, however, we should not expect to be able to do so, as the solutions seem to be split into several hypervolumes (clusters).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

When elites share a large part of their genome (here in the first two tasks), it becomes possible to bias the variation operator (the mutation) to make it more likely to generate new candidates in the elite hypervolume. To exploit these inter-species similarities, a simple approach is to extract genotypic correlations and sample new candidates accordingly. In evolutionary computation, this is typically achieved by sampling from a multivariate Gaussian distribution $\mathcal{N}{(\mu,\mathbf{\Sigma})}$, where the covariance matrix $\mathbf{\Sigma}$ models the correlations.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

A first idea is to estimate the distribution of all the elites at each generation, that is, to attempt to capture "global correlations". However, if we except purely artificial tasks, it is unlikely that all the elites follow the same correlation (this would mean that all the elites lie on a single line in the genotypic space). An alternative is to estimate a multivariate Gaussian distribution from a neighborhood around a parent $\mathbf{x}_{i}^{(t)}$ (i.e., the objective vector of the elite stored in the $i$th niche), thus, centering the distribution on $\mathbf{x}_{i}^{(t)}$. Nevertheless, this approach would require to select the appropriate neighborhood, which is likely to be specific to the task and the generation number.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

We propose a third approach that exploits the existence of a hypervolume without constructing it, and which is inspired by the success of crossover in extracting the common features of successful individuals (see Sec. 2.3).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

Once a parent is selected (here we select uniformly among the elites), it is mutated according to the following principles: the direction of correlation $\mathbf{d}_{ji}^{(t)}$ is defined by a randomly chosen elite $\mathbf{x}_{j}^{(t)}$: $\mathbf{d}_{ji}^{(t)} = {{({\mathbf{x}_{j}^{(t)} - \mathbf{x}_{i}^{(t)}})}/{\|{\mathbf{x}_{j}^{(t)} - \mathbf{x}_{i}^{(t)}}\|}}$; the variance along $\mathbf{d}_{ji}^{(t)}$ depends on the distance $\|\mathbf{d}_{ji}^{(t)}\|$, so that the mutation is self-adjusting (when the volume shrinks, the variance decreases); this follows from the literature on crossover in

<!-- chunk {"id": "body-0035", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

real-valued GAs; to mitigate premature convergence, exploration is performed not only along $\mathbf{d}_{ji}^{(t)}$, but also in all other directions; when $\|\mathbf{d}_{ji}^{(t)}\|$ is small, the variance does not decrease to zero, to ensure continual exploration in the spirit of illumination algorithms which are inherently exploratory.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

We can implement these four principles by convolving two Gaussian distributions (since the result is still a Gaussian distribution). The first distribution is an isotropic one, which has small variance in all directions (satisfying principles and); the second distribution is a directional one, which adds a Gaussian elongation (satisfying principles and). Under this operator, the offspring is sampled as follows: where $\sigma_{1}$ and $\sigma_{2}$ are user-defined parameters. Note that when $\sigma_{2} = 0$ the effect of the directional distribution disappears and the distribution becomes isotropic (Fig. 6A). Conversely, when $\sigma_{1} = 0$ the effect of the isotropic distribution disappears and the distribution takes a directional form (Fig. 6B). When $\sigma_{1} > 0$ and $\sigma_{2} > 0$ the distribution becomes correlated (Fig. 6C), and as $\|\mathbf{d}_{ji}^{(t)}\|$ goes to zero, the distribution becomes more and more isotropic.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Principle and motivation", "weight": 1.0} -->

Alternatively, Eq. 3 can be interpreted as the combination of an isotropic Gaussian mutation and a mutation similar to differential evolution whose scaling factor follows a Gaussian distribution.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In all our experiments, we use the CVT-MAP-Elites algorithm with 10000 niches. We suspect that similar results would be obtained with other quality-diversity algorithms and variants of MAP-Elites because our main assumption is that the elites are located in a specific elite hypervolume (and not evenly spread), which does not depend on the way niches are defined.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In addition, we select $\mathbf{x}_{i}^{(t)}$ and $\mathbf{x}_{j}^{(t)}$ uniformly at random. It is, however, very likely that directional variation can be combined with biases for novelty or curiosity when selecting parents. Since we care about illumination and not merely finding a single optimal solution, we define three performance metrics, which should all be maximized: archive size (with a maximum capacity of 10000), which corresponds to the number of filled niches, the mean fitness of the solutions that exist in the archive, and the maximum fitness found.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In our experiments, we abbreviate our new variation operator as "Iso+LineDD", as it incorporates an isotropic Gaussian (Iso) with a fixed variance and a directional Gaussian (Line) with a distance-dependent (DD) variance. It corresponds to the case where $\sigma_{1} > 0$ and $\sigma_{2} > 0$. In our experiments, we set $\sigma_{1} = 0.01$ and $\sigma_{2} = 0.2$. We evaluate it against the baselines of the next section^66^6All the parameters settings are found after preliminary experimentation..

<!-- chunk {"id": "body-0041", "role": "body", "section": "Gaussian Line with Distance Dependent Variance (LineDD)", "weight": 1.0} -->

This variant of our operator corresponds to the case where $\sigma_{1} = 0$ and $\sigma_{2} = 0.2$ (Fig. 6B).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Isotropic Gaussian (Iso)", "weight": 1.0} -->

This is the standard isotropic Gaussian mutation (Fig. 6A), for which we set $\sigma = 0.1$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Iso Self-Adaptation (IsoSA)", "weight": 1.0} -->

Our new operator uses a DD variance along the direction of correlation between elites. This can be seen as a type of self-adaptation, thus, it is natural to ask whether the type of self-adaptation found in ES confers any similar benefits. We thus extend each individual to additionally contain a single mutation strength $\sigma$ that is updated using a log-normal distribution: $\sigma_{i}^{({t + 1})} = {\sigma_{i}^{(t)}exp{({\tau\mathcal{N}{}})}}$, where $\tau = {({2n})}^{- {1/2}}$ and $\sigma_{i}^{} = 0.1$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Global Correlation (GC)", "weight": 1.0} -->

At every generation, we estimate the direction of global correlation by fitting a multivariate Gaussian distribution on all the points of the archive, i.e., $\mathcal{N}{(\mu_{global},\Sigma_{global})}$. Then we sample the offspring for each selected parent, by centering the distribution on the parent and scaling the covariance by some factor $\alpha$: $\mathbf{x}_{i}^{({t + 1})} = {\mathbf{x}_{i}^{(t)} + {\alpha\mathcal{N}{(\mathbf{0},\Sigma_{global})}}}$^77^7Our experiments have shown that it is always better, not to sample from the mean of the distribution, but to use this parent-centric approach.. We set $\alpha = 0.1$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Simulated Binary Crossover with One Offspring (SBX)", "weight": 1.0} -->

Since our variation operator resembles a crossover operator for real-coded GAs, we compare it with SBX, which is also parent-centric, and self-adjusting according to the distance between the two parents.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Simulated Binary Crossover with One Offspring (SBX)", "weight": 1.0} -->

To have a fairer comparison, instead of creating two offspring (each one near its corresponding parent), we generate only one as follows: $x_{ik}^{({t + 1})} = {0.5\left\lbrack {{{({1 + \beta_{k}})}x_{ik}^{(t)}} + {{({1 - \beta_{k}})}x_{jk}^{(t)}}} \right\rbrack}$, where $x_{ik}^{(t)}$ is the $k$th element of solution $\mathbf{x}_{i}^{(t)}$ ($k = {1,2,\ldots,n}$), and where $\eta \geq 0$ is the distribution index and $u_{k}$ is a random number generated from a uniform distribution in $\lbrack 0,1)$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Simulated Binary Crossover with One Offspring (SBX)", "weight": 1.0} -->

In addition, each variable has a $0.5$ chance of not being recombined in which case $x_{ik}^{({t + 1})} = x_{ik}^{(t)}$. In our experiments, we set $\eta = 10$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

As in Sec. 3, we use 30 replicates of 100k evaluations for the Schwefel function and the arm task and 20 replicates of 500k evaluations for the hexapod task. All the reported results are medians over these runs. The results (Fig. 7) confirm our conclusions when measuring the spread (Fig. 4) and similarity (Fig.5) of the corresponding elite hypervolume (Sec. 4.3). In particular, Iso+LineDD and LineDD accelerate illumination in Schwefel's function (in terms of mean and max performance; Fig. 7, left column, 2nd and 3rd panel) and the arm task (in all metrics; Fig. 7, middle column), while for the hexapod task they only provide marginal benefits (slightly better progress in archive size; Fig. 7, right column, 1st panel).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

More specifically, in Schwefel's function, Iso+LineDD and LineDD, reach a level of maximum performance at 10k evaluations (-416.5 and -419.7 respectively) that is only reached at 60k evaluations with Line (-439.7) and never reached by any other operator at 100k evaluations. This demonstrates an order of magnitude faster improvement. It also shows that DD variance is beneficial when coupled with the line operators, since IsoDD has the worst overall performance. The archive size increases at the same rate with all operators (1st panel); however, this is expected since the behavior space is just a subset (rather than a function) of the genotype space.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

In the arm task, all line operators have the best progress rates in all 3 metrics, followed by SBX. Self-adaptation (SA) helps the Iso operator in attaining better progress rates for archive size and mean fitness, and DD helps to accelerate its progress even more in contrast to the previous task. While GC always surpasses Iso in terms of mean fitness, Iso has better overall max fitness and reaches the archive size of GC at 100k evaluations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

Finally, in the hexapod task, Iso+LineDD and LineDD have the lead in terms of archive size (7274 and 7169 at 500k evaluations respectively), significantly outperforming the Iso operators which come second (6710-6725; $p < 10^{- 4}$ Mann Whitney U test); Line does not perform as well (5483.5) and displays high variance, while SBX and GC come last (4173.5 and 3977 respectively). However, in terms of mean fitness, the Line operator starts off faster than the other operators, however, at 500k evaluations Iso+LineDD manages to reach a similar level, with their difference not being statistically significant (Line: 0.412, Iso+LineDD: 0.402, $p = 0.18$ Mann-Whitney U test). Although this shows that making smaller steps along the direction of correlation helps in improving the solutions in Line's archive, note that the archive size of Line at 500k evaluations (5483.5) is even lower than the one of Iso+LineDD at 150k evaluations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

SA does not significantly affect the performance of Iso, whereas, DD negatively impacts it both in terms of mean and max fitness. In all three metrics, GC is consistently worse than the other operators.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

When plotting the final solutions found by the operators in terms of median of the mean fitness against the median of the archive size (Pareto plot; Fig. 7, bottom row), we observe that Iso+LineDD is never Pareto dominated in all three tasks.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

In this paper, we demonstrated that when using illumination algorithms in certain tasks (here the Schwefel function and the arm experiment), the set of solutions returned by the algorithms form an elite hypervolume in genotype space. We introduced two metrics, the genotypic spread and the genotypic similarity, to empirically characterize this hypervolume, as well as a variation operator that can exploit correlations between solutions. We then showed that in case the elite solutions display high genotypic similarity, the operator can significantly increase the progress rate of MAP-Elites in terms of performance (without reducing diversity, e.g., in the Schwefel function) or both performance and diversity (e.g., in the arm task); in case the elite solutions display low genotypic similarity, the operator can significantly increase the diversity (without reducing performance, e.g., in the hexapod task).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

The variation operator we introduced here resembles a parent-centric crossover for real-coded GAs. It plays a significant role in illumination algorithms because it provides them with a better balance between exploration and exploitation. In other words, the niching scheme provides the exploration, while this operator provides the exploitation because it has the "right" bias. Thus, we expect it to be more useful in cases where there is a good diversity of solutions. To our knowledge, such results are lacking in the field of real-coded GAs.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

It is likely that selective biases for illumination algorithms, will complement the variation biases we introduced here, thus, further accelerating illumination. For instance, we could minimize the chances of sampling the regions outside the elite hypervolume by restricting the selection of the second elite which would define the direction of correlation. Such an approach bears similarities to the restricted tournament selection method from multimodal optimization. Taking more inspiration from the multimodal optimization literature, we could select the second elite to be the nearest better neighbor of the first, in which case we would bias for performance.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

One might wonder whether the findings of this work apply for variable-sized genotypes, such as the ones used by the NeuroEvolution of Augmenting Topologies (NEAT) algorithm. While the crossover operator of NEAT is effective in recombining variable-sized neural networks, or compositional pattern producing networks, it resembles a disruptive, mean-centric approach to recombination (e.g., see ), rather than a parent-centric one (e.g., ). Thus, an interesting research direction would be to study how correlations between graphs can be modeled and exploited. Model-building approaches for genetic programming could provide a fruitful inspiration for such an endeavor.
