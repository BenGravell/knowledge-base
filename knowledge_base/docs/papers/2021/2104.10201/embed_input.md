<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bayesian Optimization Is Superior to Random Search for Machine Learning Hyperparameter Tuning: Analysis of the Black-Box Optimization Challenge 2020

Topics include Bayesian optimization, Random search, Hyperparameter optimization, Black-box optimization, Derivative-free optimization, Machine learning benchmarks, NeurIPS challenge, Competition analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes the NeurIPS black-box optimization challenge for machine-learning hyperparameter tuning and finds that Bayesian optimization and related black-box optimizers substantially outperform default-package baselines and random search on held-out objectives. The paper is valuable less for a new optimizer than for its benchmark design and empirical evidence about optimizer selection under realistic tuning constraints.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents the results and insights from the black-box optimization (BBO) challenge at NeurIPS 2020 which ran from July-October, 2020. The challenge emphasized the importance of evaluating derivative-free optimizers for tuning the hyperparameters of machine learning models. This was the first black-box optimization challenge with a machine learning emphasis. It was based on tuning (validation set) performance of standard machine learning models on real datasets. This competition has widespread impact as black-box optimization (e.g., Bayesian optimization) is relevant for hyperparameter tuning in almost every machine learning project as well as many applications outside of machine learning. The final leaderboard was determined using the optimization performance on held-out (hidden) objective functions, where the optimizers ran without human intervention. Baselines were set using the default settings of several open-source black-box optimization packages as well as random search.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In black-box optimization we aim to solve the problem ${\min_{x \in \Omega}f}{(x)}$, where $f$ is a computationally expensive black-box function and the domain $\Omega$ is commonly a hyper-rectangle. The fact that evaluations are computationally expensive typically limits the number of evaluations of $f$ to a few hundred. In the black-box setting, no additional information is known about $f$ and we observe no first- or second-order information when evaluating $f$. This is commonly referred to as derivative-free optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Black-box optimization problems of this form appear everywhere. Most machine learning (ML) models have hyperparameters that require tuning via black-box (i.e., derivative-free) optimization. Likewise, black-box optimization has wide applications in closely related areas such as signal processing. These black-box optimization problems are often solved using Bayesian optimization (BO) methods. BO methods rely on a (probabilistic) surrogate model for the objective function that provides a measure of uncertainty. This model is often a Gaussian process (GP), but other models such as Bayesian neural networks are also commonly used as long as they provide a measure of uncertainty. Using this surrogate model, an acquisition function is used to determine the most promising point to evaluate next, where popular options include expected improvement (EI), knowledge gradient (KG), and entropy search (ES). There are also other surrogate optimization methods that rely on deterministic surrogate models such as radial basis functions, see Forrester et al. for an overview. The choice of surrogate model and acquisition function are both problem-dependent and the goal of this challenge is to compare different approaches over a large number of different problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This was the first challenge aiming to find the best black box optimizers specially for ML-related problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, many non-ML problems also benefit from the use of BO. For example, chemical engineering, materials discovery, manufacturing design, control systems and drug discovery are also effective uses of BO. Even real-world experiments, such as optimal web interfaces evaluated using A/B tests, have been optimized using BO. Hyperparameter tuning is such a demanded tool that all the major cloud platforms offer parameter tuning tools. Additionally, there are small businesses (e.g., SigOpt) offering hyperparameter optimization as a service (OPTaaS).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evolutionary algorithms (EAs) are another popular approach to black-box is optimization; they include methods such as differential evolution (DE), genetic algorithms (GAs), and the covariance matrix adaptation evolution strategy (CMA-ES). However, EAs generally require thousands of evaluations to be competitive with more sample-efficient methods such as BO, which may not be feasible when $f$ is computationally expensive. Other possible options for solving black-box optimization problems include the Nelder-Mead algorithm and the popular quasi-Newton method BFGS with gradients obtained via finite differences.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While BO has gained a lot of traction over the last few years and open-source packages have become very mature and robust, the study by Bouthillier and Varoquaux shows that there is still work to do to convince ML practitioners to use it to tune their algorithms. Surveying authors of papers published at NeurIPS 2019 and ICLR 2020 they found that while 80% of the NeurIPS papers and 88% of the ICLR papers tuned their hyperparameters, the vast majority used manual tuning, random search, or grid search (GS). In fact, only 7% of the NeurIPS papers and 6% of the ICLR papers used a different method such as BO. Motivated by the original NeurIPS 2019 survey we decided to submit a proposal for a competition with the goal of decisively showing that BO and similar methods are superior choices over random search and grid search for tuning hyperparameters of ML models. This competition showed this advantage decisively and also provided guidance on how to select the best performing black-box optimization method.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Competition Setup", "weight": 1.0} -->

This is a new competition as there have been no ML-oriented black-box optimization competitions in the past.^33^3 The most similar competition, the previously mentioned AutoML series, maintains key differences (endemic between any black-box optimization competition and any AutoML competition). In AutoML, the algorithm gets to pick the search space while in black-box optimization, it is assigned to the algorithm by the user. The user often has intuition for reasonable hyperparameter ranges in ML problems, which makes it possible to frame it as a black-box optimization problem. While the survey by Bouthillier and Varoquaux showed that most ML researchers tune their hyperparameters, they do so using simple methods such as random search, grid search, and manual tuning. In addition, there are a large number of possible algorithms from BO and EAs, so concluding which method is preferable on real-world problems is a clear technical advance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Competition Setup", "weight": 1.0} -->

There were three different sets of problems where the participants' algorithms were evaluated: 1) The *local practice problems*; these problems were included in Bayesmark and run locally on the participants' machines with full visibility into the models and data. 2) The *feedback leaderboard problems*; these problems were used to calculate the leaderboard score on the website during the three month feedback phase of the challenge. These problems were run in a cloud environment and completely hidden from the participant. 3) The *final leaderboard problems*; these problems were used to calculate the final leaderboard score, which was posted on the website after the closing of submissions and used to determine prizes. These problems were also hidden like the feedback problems. To prevent overfitting, the participants' algorithms were only evaluated a single time on the final leaderboard problems. Problems were randomly split between feedback and final. The set of problems is discussed in more detail in Section 3.2.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Competition Setup", "weight": 1.0} -->

However, the local practice problems were made from tuning ML models on public scikit-learn datasets, and therefore, not a random split of the other problems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Competition Setup", "weight": 1.0} -->

We provided a *starter kit*^44^4 to allow the participants to: 1) Locally score their submissions on the local practice problems with a single shell command; and 2) package their submissions into a compliant zip file for submission with a single shell command. All baseline and evaluation code runs on CPU without the need for a GPU.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Baselines", "weight": 1.0} -->

The starter kit provided examples using the default configurations of several different optimization packages: Hyperopt, Nevergrad, OpenTuner, pySOT, Scikit-Optimize, and TuRBO, which serve as baselines. However, the most natural single reference point is the performance of (included) random search.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Baselines", "weight": 1.0} -->

These baselines were meant to give participants a good starting point, but there are many other possible packages such as Ax/BoTorch, Cornell-MOE, Dragonfly, Emukit, GPFlowOpt, GPyOpt, pycma, RBFOpt, RoBO, ProBO, and Spearmint.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

The "dataset" for this competition was a collection of optimization problems. Therefore, we followed the same protocols that were followed in the AutoML competition for a "dataset of datasets". A collection of public scikit-learn datasets^55^5The example scikit-learn datasets were: digits, iris, wine, breast, boston, and diabetes. were provided to the participants in local practice problems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

We obtain novel optimization problems via the Cartesian product of datasets, ML models, and evaluation metrics. For example, the following are all examples of optimization problems,

<!-- chunk {"id": "body-0018", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

Tune a GBDT on MNIST evaluated on accuracy on the validation set.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

Tune logistic regression on MNIST evaluated on log loss on the validation set.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

Tune an MLP on Boston housing evaluated on RMSE on the validation set.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

The Cartesian product is violated slightly as different loss functions are used for classification and regression problems. Keeping many of these datasets completely hidden allows us to have test (optimization) problems unknown to the participants for both the feedback and final leaderboards. The search space varied by ML model and was provided to the algorithm by the benchmark. We summarize this space of problems across phases in Table 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Optimization Problems", "weight": 1.0} -->

This structure was chosen because in industrial settings we are often more concerned with *wall clock time* than raw CPU time. To keep this wall clock time reasonable, each submission was allowed a budget of 30 minutes per optimization run. Therefore, algorithms that perform well when making parallel suggestions are highly desirable. Much of the BO literature is focused on limiting the number function evaluations rather than iterations. The limitation of 16 rounds of guesses (iterations) is very small in the broader world of optimization.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

In this challenge we use the open-source package Bayesmark to execute all the experiments inside the docker and for scoring. The Bayesmark package has routines designed to deal with the subtleties of scoring black-box optimization algorithms. Scoring an optimization algorithm on a single problem is easy; simply take the minimum found by the optimizer after $n$ function evaluations. Averaging over repeated trials can be done in noisy settings. Each repeated trial of a particular problem is known as a *study*.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

However, averaging over many different problems becomes more subtle. We cannot simply average scores because they are all on different scales (units); such an approach builds in an arbitrary implicit weighting across problems. The Bayesmark package has a scoring system designed to deal with this problem. First, we normalize the performance on each problem so that a single RS suggestion has an average score of 1, and the global optimum has a score of 0. Then, we can average the performance across multiple problems because the units are all the same.
