<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimizing with Low Budgets: A Comparison on the Black-Box Optimization Benchmarking Suite and OpenAI Gym

Topics include Black-box optimization, Low-budget optimization, Bayesian optimization, Derivative-free optimization, BBOB, COCO, OpenAI Gym, Benchmarking, Reinforcement learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Compares Bayesian-optimization-oriented ML tools with classical derivative-free optimizers under limited evaluation budgets. The study updates earlier benchmarking work by testing both COCO/BBOB functions and direct policy search in OpenAI Gym, showing that BO methods are strong at small budgets but can be overtaken by other black-box optimizers as budgets grow.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The growing ubiquity of machine learning (ML) has led it to enter various areas of computer science, including black-box optimization (BBO). Recent research is particularly concerned with Bayesian optimization (BO). BO-based algorithms are popular in the ML community, as they are used for hyperparameter optimization and more generally for algorithm configuration. However, their efficiency decreases as the dimensionality of the problem and the budget of evaluations increase. Meanwhile, derivative-free optimization methods have evolved independently in the optimization community. Therefore, we urge to understand whether cross-fertilization is possible between the two communities, ML and BBO, i.e., whether algorithms that are heavily used in ML also work well in BBO and vice versa. Comparative experiments often involve rather small benchmarks and show visible problems in the experimental setup, such as poor initialization of baselines, overfitting due to problem-specific setting of hyperparameters, and low statistical significance.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With this paper, we update and extend a comparative study presented by Hutter et al. in 2013. We compare BBO tools for ML with more classical heuristics, first on the well-known BBOB benchmark suite from the COCO environment and then on Direct Policy Search for OpenAI Gym, a reinforcement learning benchmark. Our results confirm that BO-based optimizers perform well on both benchmarks when budgets are limited, albeit with a higher computational cost, while they are often outperformed by algorithms from other families when the evaluation budget becomes larger. We also show that some algorithms from the BBO community perform surprisingly well on ML tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Black-Box Optimization (BBO) is an affirmed and rapidly growing field of optimization and a topic of critical importance in many application areas including complex systems engineering, energy and environment, materials design, drug discovery, chemical process synthesis, and computational biology. As in other classical optimization contexts, BBO assumes that we are facing an objective function $f$ for which we aim to provide a solution $x$ with $f{(x)}$ as good as possible using as little computational effort as possible. The key distinguishing property of BBO is that the algorithms learn about the problem instance $f$ only by querying the quality $f{(x)}$ of possible solution candidates $x$. This may be because we indeed lack an explicit representation of $f$ (e.g., if simulations or experiments are required for assessing the quality of a possible solution) or when we lack efficient approaches to make use of the instance information (e.g., many real-world scheduling and routing problems are solved with heuristic approaches).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simplifying the complexity measurement, in BBO we typically only account for the number of function evaluations, and hence aim for identifying high-quality solutions $x$ using as few function evaluations as possible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because of its high practical relevance, people with many different backgrounds are drawn into BBO, leading to a multitude of approaches in the area, ranging from simple heuristics such as local search to local/global modeling approaches. To understand the strengths and weaknesses of these different methods, fair performance comparisons are needed. Several platforms and benchmark suites (i.e., collections of benchmark problems) address this empirical comparison. Some examples are the Black-Box Optimization Benchmarking (BBOB) collection of the COCO environment, Large-Scale Global Optimization (LSGO), Nevergrad, Pseudo-Boolean Optimization (PBO), and Machine Learning and Data Analysis (MLDA). Apart from these more general benchmarking suites, there are also problem collections for evaluating and comparing algorithms for specific BBO tasks such as algorithm configuration and selection, neural architecture search, and expensive global optimization; see \[13, Section 3\] for a more exhaustive summary.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An approach commonly used for expensive optimization problems (for which the available number of function evaluations can be very small) uses surrogates to approximate the problem instance $f$, with the idea that the approximation $\hat{f}$ can be used to locate interesting solution candidates without requiring evaluations of the true problem $f$. Recently, Machine Learning (ML) has gone down this road and proposed several tools for BBO along these lines. In particular, a large field of research is Bayesian Optimization (BO), which is based on the Efficient Global Optimization (EGO) algorithm. Despite its success, BO is stated to be limited to less than 15 parameters and a few thousand evaluations according to the literature. To overcome this issue, recent research started to explore space partitioning and local modeling. In fact, learning a classifier that locates the samples on a promising subregion of the domain with high probability might be more effective than learning a regressor on the whole domain. Among other partitioning strategies, the Latent Action Monte Carlo Tree Search (LA-MCTS) recursively learns space partition in a hierarchical manner using Monte Carlo Tree Search (MCTS).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, in addition to BO, MCTS has also been adapted from control and games to BBO. However, both the BO and MCTS tools for BBO have rarely been compared to existing BBO methods in a systematic and satisfactory manner. For example, the comparisons in the LA-MCTS paper depend heavily on poor initialization of competitors, and the baselines used in the paper are not made available in the provided code, while the comparisons in consider only the simple $({1 + 1})$ sampling method and not the more sophisticated (and often better performing) BBO methods provided by the Nevergrad platform, although they refer to the comparison as 'Nevergrad'. However, we note some efforts to make neutral and comprehensive comparisons. Extensive comparisons in Nevergrad tend to favor more classical methods such as tools from mathematical programming like Cobyla and others or evolution strategies like CMA-ES, possibly equipped with surrogate models. Hutter et al. ran SMAC-BBOB, a well-known BO framework, on the BBOB benchmark suite and got positive results for BO when the budget of admissible function evaluations is fairly small.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, their investigation on expensive black-box functions only assesses SMAC against CMA-ES, yielding a rather limited benchmarking study.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, there is widespread utilization of black-box optimization algorithms in the ML field, yet there exists a deficiency in conducting comprehensive comparisons between the algorithms favored in ML domains and those favored by evolutionary computation researchers. Recent papers raised doubts on the reproducibility of some results in the ML community. In this work, we update and extend the comparison made in by adding several state-of-the-art solvers and by comparing not only on the BBOB benchmark suite but also -- as it is closer to ML -- on direct policy search for OpenAI Gym problems. We evaluate the performance of various BBO algorithms, considering solvers commonly associated with the ML community as well as more classical heuristics, and testing over a range of budgets that allow us to draw fair and unbiased conclusions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Black-box Optimization Algorithms", "weight": 1.0} -->

We briefly summarize the algorithms included in our comparison, along with a brief description of two main classes of interest, BO and LA-MCTS.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Bayesian Optimization", "weight": 1.0} -->

BO is a sequential design strategy targeting global optimization of black-box functions that do not assume any functional forms. It is particularly advantageous for problems where the objective function is difficult to evaluate, is a black box with some known structure, relies upon less than 20 dimensions, and where no information about sensitivity and derivatives is available. Since the objective function does not have an explicit mathematical formulation, BO treats it as a random function and places a prior over it. A Kriging model, also known as *Gaussian Process Regression* (GPR), can be used as a prior probability distribution over functions in BO.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Bayesian Optimization", "weight": 1.0} -->

Often, a Gaussian likelihood is taken, leading to a conjugate posterior process, i.e., $\left. f \middle| \mathbf{y} \right. \sim {gp{({\hat{f}{( \cdot )}},{K^{\prime}{( \cdot, \cdot )}})}}$, where $\hat{f}$ and $K^{\prime}$ are the posterior mean and covariance function, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Bayesian Optimization", "weight": 1.0} -->

On an unknown point $\mathbf{x}$, $\hat{f}{(\mathbf{x})}$ yields the maximum *a posteriori* estimate of $f{(\mathbf{x})}$ whereas ${{\hat{s}}^{2}{(\mathbf{x})}} ≔ {K^{\prime}{(\mathbf{x},\mathbf{x})}}$ quantifies the uncertainty of this estimation. The posterior process is, again, a GPR. Based on the posterior process, promising points are identified via the so-called infill-criterion, i.e., by optimizing an acquisition function that balances $\hat{f}$ with ${\hat{s}}^{2}$ (exploitation vs. exploration). A variety of infill-criteria has been proposed in the literature, e.g., Probability of Improvement, Expected Improvement, and the Upper Confidence Bound.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Bayesian Optimization", "weight": 1.0} -->

When a new candidate point is selected by the infill criterion, it is evaluated and added to the BO data set, which is used to update the GPR posterior. This process is repeated until a stopping condition is met, i.e., a good enough result is located or the computational budget is exhausted.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Monte Carlo Tree Search", "weight": 1.0} -->

Monte Carlo Tree Search (MCTS) is a solver that migrated from trees of bandits for games and control, including alpha-zero, to applications in BBO. Its evolved version, LA-MCTS, progressively learns and generalizes promising regions in the problem space by recursively partitioning so that solvers like BO can access these regions to improve their performance. At any iteration $t$ of the algorithm, a training dataset $\mathbf{D}_{t} = {(\mathbf{X},\mathbf{Y})}$ of all the points evaluated so far is available. A tree node $A$ represents a subregion of the search space $\Omega_{A}$. Therefore, $\mathbf{D}_{t} \cap \Omega_{A}$ is the set of all the samples falling in the subregion $\Omega_{A}$. MCTS uses the Monte Carlo simulation to accumulate value estimates that lead to highly rewarding trajectories in the search tree.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Monte Carlo Tree Search", "weight": 1.0} -->

In other words, MCTS pays more attention to promising nodes (i.e., subregions of the search space), in order to avoid the need to brute force all possibilities. This is done by using an Upper Confidence Bound (UCB) policy. More specifically, each node has an associated UCB value and, during selection, the child node with the highest UCB value is considered. The statistics used to compute the UCB are $n_{A}$, which is the number of samples in $\mathbf{D}_{t} \cap \Omega_{A}$, and the node value $v_{A}:={{({\sum_{{\mathbf{x}}_{i} \in \mathbf{D}_{t}} \cap {\Omega_{A}f{({\mathbf{x}}_{i})}}})}/n_{A}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Monte Carlo Tree Search", "weight": 1.0} -->

Therefore, in LA-MCTS, which is the MCTS-based optimizer that we include in the comparisons of this study, promising regions are found by recursively partitioning the search space based on latent actions. In one iteration, LA-MCTS starts building the tree by partitioning and then selects a region based on UCB. Finally, sampling is performed in the selected region using BO. In this way, BO avoids over-exploring the search space, and its performance improves, especially for high-dimensional problems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

BO: the Bayesian Optimization algorithm implemented in Nevergrad. The python class is a wrapper over the bayes_opt package.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

LA-MCTS: as described above, LA-MTCS is an MCTS-based derivative-free meta-solver that recursively learns space partition in a hierarchical manner. Sampling is then performed in the selected region using BO.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

Turbo: a trust-region-inspired algorithm using Thompson sampling rather than the optimization of an acquisition function to find new candidate solutions in each subregion. denotes the multi-trust-regions counterpart of Turbo.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

AX: a modular BO framework that uses BoTorch primitives for optimization over continuous spaces. It automates the selection of optimization routines, reducing the amount of fine-tuning required.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

SMAC: a sequential model-based algorithm for algorithm configuration to optimize the parameters of arbitrary algorithms. It scales well to high dimensions and is particularly suitable for hyperparameter optimization of ML algorithms. The main core consists of BO. SMAC2 refers to SMAC-HPO, i.e., SMAC with hyperparameter optimization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

HyperOpt: library for serial and parallel hyperparameter optimization, designed to accommodate BO algorithms based on Gaussian processes and regression trees. We use the version based on Parzen estimates.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Selection of BO-based Algorithms", "weight": 1.0} -->

Optuna: automatic hyperparameter optimization software framework which uses state-of-the-art algorithms for sampling hyperparameters and pruning unpromising trials. By default, Optuna implements a BO algorithm (Tree-structured Parzen Estimator).

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-D Classical Black-box Optimization Algorithms", "weight": 1.0} -->

As baselines commonly used in the broader BBO context we consider CMA, which stands for CMA-ES, a well-known evolution strategy, Cobyla, a tool from mathematical programming, particle swarm optimization (PSO ), and NGOpt from Nevergrad, a wizard that combines many classical algorithms in various ways. In the use cases considered in this work (sequential, low-dimensional, noise-free problems), NGOpt mainly uses CMA, Cobyla, and (1+1)-type sampling equipped with metamodels.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-D Classical Black-box Optimization Algorithms", "weight": 1.0} -->

We also include DefaultCMA, a version of CMA without the BBOB-specific initialization used for the experiments of CMA on BBOB. We do this to show that ad hoc initialization of CMA-ES does not lead to significant improvement over DefaultCMA.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

Extensive comparisons have already been proposed in Nevergrad, focusing on reproducibility, real-world, and different problem sizes. We propose here additional experiments in the well-known BBOB framework, chosen for its simplicity/canonicity, and for OpenAI Gym^11^1 commonly used in the reinforcement learning (RL) environment.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

BBOB: The BBOB collection contains 24 functions, with known difficulty (e.g., non-separability, ill-conditioning, different levels of multimodality, adequate or weak global structure, etc.). Although all functions are defined and can be evaluated over ${\mathbb{R}}^{D}$, the default search domain is ${\lbrack{- 5},5\rbrack}^{D}$; that is, in contrast to Nevergrad's experiments, the BBOB suite has a focus on bounded domains.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

BBOB offers a possibility to randomize both the position of the optimal solution (that is, test functions are randomly shifted in the domain) and the function value of the optimum (test functions are randomly shifted in the co-domain). To reduce bias with respect to problem encoding, we run the algorithms on 15 randomly chosen instances per test function and dimension. We consider six different dimensions (2, 3, 5, 10, 20, and 40).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

As suggested, we focus on a relatively small budget of $10D$ or $100D$ function evaluations (the default setting for BBOB experiments is $1000D$). When a method crashes, we rerun it with the remaining budget.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

For the BBOB experiments, our key performance measure is the empirical cumulative distribution function (ECDF) of the runtimes needed to reach the optimal objective value with a given precision $\Delta t$, i.e., the runtime depends on a given target function value ($f_{t} = {f_{\text{opt}} + {\Delta t}}$) and is computed across all runs of an optimizer on a function, as the total number of function evaluations before reaching $f_{t}$ divided by the number of trials that actually reached $f_{t}$. Informally, the ECDF shows the proportion of problems solved within a given budget, with the budget indicated on the x-axis.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

OpenAI Gym with Direct Policy Search: Firstly, we work on a multi-deterministic Open AI Gym with tiny neural nets. Indeed, we analyze a small version (small number of neurons, low budget) to fit the low-budget context of the present work. *Multi-deterministic* here means that for a given algorithm, a different seed is drawn at random for each repetition, and this list of seeds is used for all algorithms. There are different seeds so that we avoid overfitting, and the list of seeds is the same over the different algorithms so that we have statistical pairing. This means that parameters are not tuned based on specific landscapes (e.g., bounded/unbounded domains, prescribed optimal regions, and multimodality of the objective function). This is somewhat analogous to random perturbation of the optimum in classical BBO benchmarks in the sense that the objective function is deterministic but drawn randomly.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

Within the gym library, we select a few environments to compare algorithms based on average loss (i.e. average negated reward) and average winning rates (i.e., the frequencies at which one method outperforms another): MountainCar-v0 ($D = 12$), Pendulum-v0 ($D = 15$), GuessingGame-v0 ($D = 24$), HotterColer-v0 ($D = 24$), CartPole-v0 ($D = 28$). CartPole-v1 ($D = 28$), NChain-v0 ($D = 40$), and MountainCarContinuous-v0 ($D = 8$). We chose these problems with $D < 50$ because they are sufficiently challenging and are not too hard in our context of tiny networks and minimal budget, i.e., not all algorithms perform equally.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

Here we use a *neural factor* (i.e., the scaling coefficient used in the benchmarking suite to choose the size of neural networks) of 1. The dimension, i.e., the total number of weights, is a consequence of the number of neurons, which in turn is based on the scaling factor (the number of neurons per hidden layer is the neural factor multiplied by the input dimension).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

In a second set of experiments we include problems with dimensions $D \leq 264$ for larger networks defined by setting the neural factor to $3$, which parameterizes the size of the hidden layer. This bound on the dimension and the different neural factor lead to a different subset of OpenAI Gym problems: LunarLanderContinuous-v2, Blackjack-v0, Pendulum-v0, HotterColder-v0, MountainCarContinuous-v0, CartPole-v0, Acrobot-v1, NChain-v0, GuessingGame-v0, CartPole-v1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Benchmark Problems", "weight": 1.0} -->

Winning percentage rates are evaluated at fixed budgets of 25, 50, 100, 200, and 400 function evaluations for both settings (neural factor $1$ and $3$), while bigger budgets are also considered for the bigger networks (see Sections IV and V in the Supplementary Material).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Results for BBOB: Figs. 1 and 2 present results with budget equal to $10D$ and $100D$, respectively, in dimension $D$. The x-axis is the budget divided by the dimension, in logarithmic scale, while the y-axis shows the frequency of problems solved, i.e., the higher, the better. The plots are built by using the COCO/BBOB post-processing tool. It aggregates problems with different target precision values and displays the runtime distributions with simulated restarts. The default target precision values are 51 evenly log-spaced values between $10^{2}$ and $10^{- 8}$. The complete data set is archived on Zenodo and allows further comparison with other BBOB data sets through the original COCO platform or the IOHanalyzer web-interface.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Our experiments for a budget of $10D$ reproduce the results, where SMAC outperforms CMA. However, SMAC performance decreases with increasing dimension. Similar to all BO-based algorithms, its computational complexity increases significantly with increasing dimension and with increasing budget.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Although we tested fewer optimizers for the $D = 20$ and $D = 40$ cases due to the high computational cost, it is interesting to note that Cobyla, which is simply based on linear interpolation, often performs better than all other solvers. Although there is no tuning for our present results from Cobyla on BBOB, it outperformed all BO-based algorithms. Cobyla is also the algorithm selected by the NGOpt wizard for the test cases considered, which explains their similar performance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Fig. 2 shows that both versions of CMA -- defaultcma and cmafmin2 (and, which uses CMA as a component) -- perform better than all other solvers when a larger budget of function evaluations is available.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

The LinearSlope function, which has optima in the corners, is difficult for methods that assume that the optimum is supposed to be inside.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

The precision parameter, ranging from ${1e} - 8$ to $100$ by default, has a significant impact on results. Since our budget is much smaller than the default setting, the percentage of the problems that are successfully solved is smaller than the typically reported ones.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

In an additional set of experiments, we verified that removing LinearSlope or changing the precision parameter does not change the overall picture of our results.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Table I and Table II list the total execution time in seconds for 15 runs on the 24 BBOB functions for budget 10D and 100D, respectively. Note that NGOpt sometimes, in particular when the budget is sufficiently large compared to the dimension, spends a significant time learning a meta-model and checking in cross-validation whether this meta-model could be applied. NGOpt can hence be unexpectedly more expensive in lower dimensions, which in our experiments leads to the non-monotonic behavior of the running time with respect to the dimension. DefaultCMA and SMAC2 have comparable execution times to CMAFmin2, Turbo, and SMAC, respectively. AX, BO, LAMCTS, and SMAC showed a total time of more than 20 000 seconds in dimension 10. As their computational cost became unmanageable for dimension 20, we stopped the runs after 3-day wall-clock time. We therefore do not report results for these algorithms for the 20- and 40-dimensional BBOB functions with 10D budget. The same algorithms, with the exception of SMAC, plus Optuna, are excluded from the experiments with a higher total evaluation budget (100D) due to their excessive computational cost for that budget.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Results for the Direct Policy Search on OpenAI Gym: In Fig. 3, we provide an independent comparison of black-box solvers applied to the Ng-Full-Gym benchmark, which is Nevergrad's direct policy search applied to OpenAI Gym. More precisely, is the optimization of a neural network as a controller for OpenAI Gym problems. We plot the unscaled loss, defined as the opposite of the reward the agent accumulates over time. Here, the lower the curve, the better the performance. The non-monotonic trend of the curves with respect to the elapsed budget is due to the fact that, for a given problem and algorithm, we perform new runs each time the total budget of the evaluations is updated. As a consequence, the algorithm may choose a different parametrization depending on the total budget or the ratio between the budget and the dimension of the specific benchmark, leading to a statistically significant difference in performance. In addition, since we perform independent runs for different budgets and average over the repetitions, some variability in performance is to be expected.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

We add the following algorithms to our comparison: QORandomSearch, MetaTuneRecentering, and MetaRecentering are variants of random search that are fully parallel and reduce redundancies compared to random search. We also add NGOpt16RL and SpecialRL from Nevergrad: NGOpt16RL is Nevergrad's wizard NGOpt optimized specifically for RL problems; SpecialRL runs the base NGOpt16RL for half of the budget and then uses test-based population size adaptation (TBPSA) in the second half. Moreover, since the OpenAI Gym suite contains problems that are unbounded with optima at a small scale, we add algorithms that can adjust the scale of the search. GeneticDE and RotatedTwoPointsDE, for example, are designed to extrapolate the scale from some variables to others and find the right scale before running the classic DE algorithm. MetaTuneRecentering performs a DoE entirely designed to choose the right scale depending on the relationship between budget and dimension. MultiCMA is a tentative robustification of CMA that runs three copies of CMA.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

We also consider a (1+1) evolutionary algorithm, which is a simple and fast state-of-the-art heuristic for adjusting the scale, Diagonal CMA, which uses a diagonal covariance matrix, and its scaled version, Scaled Diagonal CMA. Finally, we add to our portfolio Lamcts-Turbo, an improved version of vanilla LA-MCTS coupled with Turbo to draw new samples in the selected node of the Monte Carlo search tree at each iteration. For a complete list of all algorithms compared, see Section VI in the Supplementary Material.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Although we cannot derive comprehensive recommendations from Fig. 3 because of the high variability of results across different benchmarks and dimensions, some conclusions can be drawn from the observation of similar patterns. First, we note that Fig. 3b, 3c, and 3d corresponding to problems of intermediate dimension $(D = 15$ and $D = 24)$ show no significant differences in solver performance. On the contrary, for the low-dimensional test cases in Fig. 3a and 3g, we observe a very clear superiority of the BO-based solvers (BO and AX), HyperOpt, PSO, and the wizard NgOpt16RL, all consistently belonging to the 5-best group. On the other hand, Fig. 3e, 3f, and 3h show that the quality of the performance of the 5-best group deteriorates as the dimension of the problem increases. Indeed, we observe the lowest loss values at the end of the total evaluation budget for population-based algorithms like DE and CMA, which are known to be powerful heuristics to address difficult black-box problems when a large number of function evaluations are available.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

However, for lower budgets of up to 100 function evaluations, the best-performing algorithms are still BO, AX, HyperOpt, PSO, and NgOpt16RL. On the contrary, Lamcts-Turbo consistently performs poorly on OpenAI Gym benchmarks, regardless of problem budget and dimension, in sharp contrast to the results shown, where LA-MCTS was reported to perform well on some OpenAI Gym problems. We suspect that this discrepancy is caused by a poor initialization of the competitors.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

For an in-depth comparison, we also present aggregate plots based on average winning rates (e.g., Fig. 4), where we observe good results for the BO-based methods: BO is the most powerful solver for the lowest budget, while AX, NGOpt16RL and PSO turn out to be the best algorithms (within the confidence intervals) when aggregating results across all budgets (Fig. 4f). This means that vanilla BO is actually good for fast low-precision approximations on difficult problems, whereas AX, NGOpt16RL and PSO can be recommended when optimizing low-dimensional problems with low to medium budgets. Furthermore, Fig. 4 confirms, on the one hand, the good performance of NGOpt16RL, PSO, and HyperOpt for benchmarks with tiny neural networks, and, on the other hand, the poor search capabilities of Lamcts-Turbo, regardless of the available budget. For higher dimensions, Fig. 5 shows that BO-based solvers become less competitive, although they still perform among the best for the smallest budgets (25 and 50 evaluations). For larger budgets, we see that CMA and DE start becoming more competitive, which is in line.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

However, Fig. 5f shows a supremacy of HyperOpt, which is designed for large-scale optimization for models with hundreds of parameters, and PSO, which performs surprisingly well considering that it is a classical heuristic originating from the BBO field and rarely used in ML applications. It can also be noted that Cobyla does not perform as well as for BBOB, while PSO performs constantly well for intermediate budgets from 50 to 400 total evaluations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

Fig. 1 in the Supplementary Material extends the present results to budgets 800, 1600, and 3200 for both tiny and big neural nets. Here, as the total budget increases, a smaller set of algorithms are compared: AX is affordable for runs on tiny neural nets up to a budget of 800 evaluations, and BO and Lamcts-Turbo become too expensive when exceeding a total budget of 1600 evaluations for big neural nets. The RL-specific algorithms, SpecialRL, and NGOpt16RL achieve the best performance for the largest budgets, followed by the various CMA and DE versions, leaving PSO and HyperOpt behind.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results of the Empirical Comparison", "weight": 1.0} -->

All in all, our results on OpenAI Gym show the competitiveness of BO-based methods for small dimensions and evaluation budgets (up to 100 evaluations), comparably to other solvers, while solvers from other families perform better as the budget increases. We note that this is different behavior from the BBOB benchmarks, where BO-based methods never rank first and show only average performance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our results provide insight into the comparison between different state-of-the-art BO methods, commonly used in ML, and more classical BBO heuristics. We compared the solvers on the BBOB benchmark suite from the COCO environment, which is well-known in the BBO community, and on OpenAI Gym problems, which are from the RL domain. On the BBOB comparison, we noted that Cobyla and the Nevergrad wizard perform best for any tested dimensionality from 2D to 40D with a total budget of 10D. They were consistently better than SMAC and Turbo, which was highlighted as a strong BO method. It is worth noting that Turbo and HyperOpt have the advantage of being computationally cheaper than other BO methods. Moreover, HyperOpt performed among the best on OpenAI Gym, with the exception of the largest considered budget for big neural nets. Good performance was also observed for PSO, which is commonly considered a classical heuristic and hardly ever used for ML tasks. For the larger budget of 100D, CMA or the Nevergrad wizard perform best regardless of the considered dimension of the problem.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In general, we found that the OpenAI Gym benchmark is very sensitive to variable scaling. While BBOB focuses on translations of optima and might therefore favor algorithms tuned for this setting, direct policy search for OpenAI Gym has an unbounded domain and depends differently on the initialization scaling and the ability of the algorithm to change scaling as needed. We optimized the scaling to Bayesian Optimization methods for obtaining results in Fig. 4, and then we ran the experiments to get the (possibly more neutral) results in Fig. 5 without any change.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Overall, tools based on heavy use of machine learning are computationally more expensive and perform roughly equivalently to mathematical programming or evolutionary techniques. In future work, we plan to compare BO and other methods in discrete settings as well. Our results also indicate a high relevance of initializing the solvers with the right scaling. Identifying suitable methods for a dynamic control policy is therefore another topic that we aim to investigate in future works. Of course, it remains interesting to periodically update our comparisons with new state-of-the-art solvers. Since all our experiments are performed with Nevergrad, such an ongoing benchmarking is largely facilitated: users can simply add their favorite method and compare their results to the ones reported above.
