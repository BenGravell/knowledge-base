<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient Boosting Performs Gaussian Process Inference

Topics include Uncertainty, Regression, Gradient boosting, Gaussian processes.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper shows that gradient boosting based on symmetric decision trees can be equivalently reformulated as a kernel method that converges to the solution of a certain Kernel Ridge Regression problem. Thus, we obtain the convergence to a Gaussian Process' posterior mean, which, in turn, allows us to easily transform gradient boosting into a sampler from the posterior to provide better knowledge uncertainty estimates through Monte-Carlo estimation of the posterior variance. We show that the proposed sampler allows for better knowledge uncertainty estimates leading to improved out-of-domain detection.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient boosting is a classic machine learning algorithm successfully used for web search, recommendation systems, weather forecasting, and other problems. In a nutshell, gradient boosting methods iteratively combine simple models (usually decision trees), minimizing a given loss function. Despite the recent success of neural approaches in various areas, gradient-boosted decision trees (GBDT) are still state-of-the-art algorithms for *tabular* datasets containing heterogeneous features.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper aims at a better theoretical understanding of GBDT methods for regression problems assuming the widely used RMSE loss function. First, we show that the gradient boosting with regularization can be reformulated as an optimization problem in some Reproducing Kernel Hilbert Space (RKHS) with implicitly defined kernel structure. After obtaining that connection between GBDT and kernel methods, we introduce a technique for sampling from prior Gaussian process distribution with the same kernel that defines RKHS so that the final output would converge to a sample from the Gaussian process posterior. Without this technique, we can view the output of GBDT as the mean function of the Gaussian process.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Importantly, our theoretical analysis assumes the regularized gradient boosting procedure (Algorithm 2) without any simplifications --- we only need decision trees to be symmetric (oblivious) and properly randomized (Algorithm 1). These assumptions are non-restrictive and are satisfied in some popular gradient boosting implementations, e.g., CatBoost.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments confirm that the proposed sampler from the Gaussian process posterior outperforms the previous approaches and gives better knowledge uncertainty estimates and improved out-of-domain detection.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Gradient boosted decision trees", "weight": 1.0} -->

Given a loss function $L:{{\mathbb{R}}^{2}\rightarrow{\mathbb{R}}}$, a classic gradient boosting algorithm iteratively combines weak learners (usually decision trees) to reduce the average loss over the train set $\mathbf{z}$: ${\mathcal{L}{(f)}} = {{\mathbb{E}}_{\mathbf{z}}{\lbrack{L{({f{(x)}},y)}}\rbrack}}$. At each iteration $\tau$, the model is updated as: ${f_{\tau}{(x)}} = {{f_{\tau - 1}{(x)}} + {\epsilonw_{\tau}{(x)}}}$, where ${w_{\tau}{(\cdot)}} \in \mathcal{W}$ is a weak learner chosen from some family of functions $\mathcal{W}$, and $\epsilon$ is a learning rate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Gradient boosted decision trees", "weight": 1.0} -->

The weak learner $w_{\tau}$ is usually chosen to approximate the negative gradient of the loss function ${- {g_{\tau}{(x,y)}}}:={- \left. \frac{\partial{L{(s,y)}}}{\partial s} \right|_{s = {f_{\tau - 1}{(x)}}}}$: The family $\mathcal{W}$ usually consists of decision trees. In this case, the algorithm is called GBDT (Gradient Boosted Decision Trees). A decision tree is a model that recursively partitions the feature space into disjoint regions called leaves. Each leaf $R_{j}$ of the tree is assigned to a value, which is the estimated response $y$ in the corresponding region.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Gradient boosted decision trees", "weight": 1.0} -->

A recent paper Ustimenko & Prokhorenkova proposes a modification of classic stochastic gradient boosting (SGB) called *Stochastic Gradient Langevin Boosting* (SGLB). SGLB combines gradient boosting with stochastic gradient Langevin dynamics to achieve global convergence even for non-convex loss functions. As a result, the obtained algorithm provably converges to some stationary distribution (invariant measure) concentrated near the global optimum of the loss function. We mention this method because it samples from similar distribution as our method but with a different kernel.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Estimating uncertainty", "weight": 1.0} -->

In addition to the predictive quality, it is often important to detect when the system is uncertain and can be mistaken. For this, different measures of *uncertainty* can be used. There are two main sources of uncertainty: *data uncertainty* (a.k.a. aleatoric uncertainty) and *knowledge uncertainty* (a.k.a. epistemic uncertainty). Data uncertainty arises due to the inherent complexity of the data, such as additive noise or overlapping classes. For instance, if the target is distributed as $\left. y \middle| x \right. \sim {\mathcal{N}{({f{(x)}},{\sigma^{2}{(x)}})}}$, then $\sigma{(x)}$ reflects the level of data uncertainty. This uncertainty can be assessed if the model is probabilistic.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Estimating uncertainty", "weight": 1.0} -->

Knowledge uncertainty arises when the model gets input from a region either sparsely covered by or far from the training data. Since the model does not have enough data in this region, it will likely make a mistake. A standard approach to estimating knowledge uncertainty is based on *ensembles*. Assume that we have trained an ensemble of several independent models. If all the models understand an input (low knowledge uncertainty), they will give similar predictions. However, for out-of-domain examples (high knowledge uncertainty), the models are likely to provide diverse predictions. For regression tasks, one can obtain knowledge uncertainty by measuring the variance of the predictions provided by multiple models.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Estimating uncertainty", "weight": 1.0} -->

Such ensemble-based approaches are standard for neural networks. Recently, ensembles were also tested for GBDT models. The authors consider two ways of generating ensembles: ensembles of independent SGB models and ensembles of independent SGLB models. While empirically methods are very similar, SGLB has better theoretical properties: the convergence of parameters to the stationary distribution allows one to sample models from a particular posterior distribution. One drawback of SGLB is that its convergence rate is unknown, as the proof is asymptotic. However, the convergence rate can be upper bounded by that of Stochastic Gradient Langevin Dynamics for log-concave functions, e.g., Zou et al., which is not dimension-free. In contrast, our rate is dimension-free and scales linearly with inverse precision.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Gaussian process inference", "weight": 1.0} -->

To solve the KRR problem, one can apply the gradient descent (GD) method in the functional space: where $\epsilon > 0$ is a learning rate.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Gaussian process inference", "weight": 1.0} -->

Since this objective is strongly convex due to the regularization, the gradient descent rapidly converges to the unique optimum: see Appendices C and E for the details.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gaussian process inference", "weight": 1.0} -->

Gradient descent guides $f_{\tau}$ to the posterior mean $f_{\ast}^{\lambda}$ of the Gaussian Process with kernel ${\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}$. To obtain the posterior variance estimate $\overset{\sim}{\mathcal{K}}{(x,x)}$ for any $x$, one can use sampling and introduce a source of randomness in the above iterative scheme as follows: This method is known as Sample-then-Optimize and is widely adopted for Bayesian inference. As $\tau\rightarrow\infty$, we get $f^{init} + f_{\infty}$ distributed as a Gaussian Process posterior with the desired mean and variance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

Our theoretical analysis holds for classic GBDT algorithms discussed in Section 2.1 equipped with regularization from Ustimenko & Prokhorenkova. The only requirement we need is that the procedure of choosing each new tree has to be properly randomized. Let us discuss a tree selection algorithm that we assume in our analysis.

<!-- chunk {"id": "body-0017", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

Each new tree approximates the gradients of the loss function with respect to the current predictions of the model. Since we consider the RMSE loss function, the gradients are proportional to the residuals $r_{j} = {y_{j} - {f{(x_{j})}}}$, where $f$ is the currently built model. The tree structure is defined by the features and the corresponding thresholds used to split the space. The analysis in this paper assumes the *SampleTree* procedure (see Algorithm 1), which is a classic approach equipped with proper randomization. *SampleTree* builds an *oblivious* decision tree, i.e., all nodes at a given level share the same splitting criterion (feature and threshold).^33^3In fact, the procedure can be extended to arbitrary trees, but this would over-complicate formulation of the algorithm and would not change the space of tree ensembles as any non-symmetric tree can be represented as a sum of symmetric ones. To limit the number of candidate splits, each feature is quantized into $n + 1$ bins.

<!-- chunk {"id": "body-0018", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

In other words, for each feature, we have $n$ thresholds that can be chosen arbitrarily.^44^4A standard approach is to quantize the feature such that all $n + 1$ buckets have approximately the same number of training samples. The maximum tree depth is limited by $m$. Recall that we denote the set of all possible tree structures by $\mathcal{V}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

We build the tree in a top-down greedy manner. At each step, we choose one split among all the remaining candidates based on the following *score* defined for $\nu \in \mathcal{V}$ and residuals $r$: output: oblivious tree structure ν ∈ 𝒱 hyper-parameters: number of feature splits n, max.

<!-- chunk {"id": "body-0020", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

tree depth m, random strength β ∈ [0, ∞) 𝒮 = {(j, k)|j ∈ {1, …, d}, k ∈ {1, …, n}} — indices of all possible splits choose next split as ${\{ s_{i + 1}\}} = {\underset{s\in\mathcal{S}^{(i)}}{\arg\max}\left({{D\left({(\nu_{i},s)},r \right)} - {\beta{\log{({- {{\log u_{i}}{(s)}}})}}}} \right)}$ update candidate splits: 𝒮(i + 1) = 𝒮(i) ∖ {si + 1} hyper-parameters: learning rate ϵ > 0, regularization λ > 0, iterations of boosting T, parameters of SampleTree m, n, β ντ = SampleTree (rτ; m, n, β) — construct a tree $\theta_{\tau} = \left(\frac{\sum_{i =

<!-- chunk {"id": "body-0021", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

boosting, one builds a tree recursively by choosing such split $s$ that maximizes the score $D{({(\nu_{i},s)},r)}$.^55^5Maximizing is equivalent to minimizing the squared error between the residuals and the mean values in the leaves.

<!-- chunk {"id": "body-0022", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

Random noise is often added to the scores to improve generalization. In *SampleTree*, we choose a split that maximizes Here $\beta$ is random strength: $\beta = 0$ gives the standard greedy approach, while $\beta\rightarrow\infty$ gives the uniform distribution among all possible split candidates.

<!-- chunk {"id": "body-0023", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

To sum up, *SampleTree* is a classic oblivious tree construction but with added random noise. We do this to make the distribution of trees regular in a certain sense: roughly speaking, the distributions should stabilize with iterations by converging to some fixed distribution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "GBDT algorithm under consideration", "weight": 1.0} -->

Given the algorithm *SampleTree*, we describe the gradient boosting procedure assumed in our analysis in Algorithm 2. It is a classic GBDT algorithm but with the update rule ${f_{\tau + 1}{( \cdot )}} = {{\left( {1 - {{\lambda\epsilon}/N}} \right)f_{\tau}{( \cdot )}} + {\epsilonw_{\tau}{(x)}}}$. In other words, we shrink the model at each iteration, which serves as regularization. Such shrinkage is available, e.g., in the CatBoost library.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

The following lemma describes the distribution $p{(\left. {d\nu} \middle| {f,\beta} \right.)}$, see Appendix F for the proof.

<!-- chunk {"id": "body-0026", "role": "body", "section": "RKHS structure", "weight": 1.0} -->

In this section, we describe the evolution of GBDT in a certain Reproducing Kernel Hilbert Space (RKHS). Even though the problem is finite dimensional, treating it as functional regression is more beneficial as dimension of the ensembles space grows rapidly and therefore we want to obtain dimension-free constants which is impossible if we treat it as finite dimensional optimization problem. Let us start with defining necessary kernels. For convenience, we also provide a diagram illustrating the introduced kernels and relations between them in Appendix A.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Kernel Gradient Boosting convergence to KRR", "weight": 1.0} -->

Consider the sequence ${\{ f_{\tau}\}}_{\tau \in {\mathbb{N}}}$ generated by the gradient boosting algorithm. Its evolution is described by Lemma 3.7. The following theorem estimates the expected (w.r.t. the randomness of tree selection) empirical error of $f_{T}$ relative to the best possible ensemble. The full statement of the theorem and its proof can be found in Appendix G.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Gaussian inference", "weight": 1.0} -->

So far, the main result of the paper proved in Section 3.5 shows that Algorithm 2 solves the Kernel Ridge Regression problem, which can be interpreted as learning Gaussian Process posterior mean $f_{\ast}^{\lambda}$ under the assumption that $f \sim {\mathcal{G}\mathcal{P}{(0,{{\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}})}}$ where $\lambda = \frac{\sigma^{2}}{\delta^{2}}$. I.e., Algorithm 2 does not give us the posterior variance. Still, as mentioned earlier, we can estimate the posterior variance through Monte-Carlo sampling in a sample-then-optimize way.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Prior sampling", "weight": 1.0} -->

We introduce Algorithm 3 for sampling from the prior distribution. *SamplePrior* generates an ensemble of random trees (with random splits and random values in leaves). Note that while being random, the tree structure depends on the dataset features $\mathbf{x}_{N}$ since candidate splits are based on $\mathbf{x}_{N}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Posterior sampling", "weight": 1.0} -->

We further refer to this procedure as *SamplePosterior* or *KGB* (Kernel Gradient Boosting) for brevity. Denote | | {{{h_{\infty} = {\lim\limits_{T_{0}\rightarrow\infty}h_{T_{0}}}},{f_{\infty} = {\lim f_{T_{1}}}}},} | | where the first limit is with respect to the point-wise convergence of stochastic processes and the second one with respect to $L_{2}{(\rho)}$ convergence.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Posterior sampling", "weight": 1.0} -->

The following theorem shows that KGB indeed samples from the desired posterior. The proof directly follows from Lemmas 4.1 and 2.1. hyper-parameters: learning rate ϵ > 0, boosting iteration T1, SamplePrior iterations T0, parameters of SampleTree m, n, β, kernel scale σ > 0 (default σ = 1), noise scale δ > 0 (default: δ = 0.01) ${f_{T_{1}}{(\cdot)}} = {{TrainGBDT}\left({(\mathbf{x}_{N},\mathbf{y}_{N}^{new})};\epsilon,T_{1},m,n,\beta,\frac{\delta^{2}}{\sigma^{2}} \right)}$

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section empirically evaluates the proposed KGB algorithm and shows that it indeed allows for better knowledge uncertainty estimates.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Synthetic experiment", "weight": 1.0} -->

We sample 10K points from $U{({\lbrack 0,1\rbrack}^{2})}$ and take into the train set only those that fall into $D$. The target is defined as ${f{(x,y)}} = {x + y}$. Figure 1(a) illustrates the training dataset colored with the target values. For evaluation, we take the same 10K points without restricting them to $D$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Synthetic experiment", "weight": 1.0} -->

For KGB, we fix $\epsilon = 0.3$, $T_{0} = 100$, $T_{1} = 900$, $\sigma = 10^{- 2}$, $\delta = 10^{- 4}$ $\beta = 0.1$, $m = 4$, $n = 64$, and sampled $100$ KGB models. Figure 1(b) shows the estimated by Monte-Carlo posterior mean $\overset{\sim}{\mu}$. On Figure 1(c), we show $\log\overset{\sim}{\sigma}$, where ${\overset{\sim}{\sigma}}^{2}$ is the posterior variance estimated by Monte-Carlo. One can see that the posterior variance is small in-domain and grows when we move outside the dataset $D$, as desired.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Synthetic experiment", "weight": 1.0} -->

(c) $\log\overset{\sim}{\sigma}$ Figure 1: KGB on a synthetic dataset.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment on real datasets", "weight": 1.0} -->

Uncertainty estimates for GBDTs have been previously analyzed by Malinin et al.. Our experiments on real datasets closely follow their setup, and we compare the proposed KGB with SGB, SGLB, and their ensembles. For the experiments, we use several standard regression datasets. The implementation details can be found in Appendix H. The code of our experiments can be found on GitHub.^77^7 Table 1: Predictive performance, RMSE Table 2: Error and OOD detection We note that in our setup, we cannot compute likelihoods as kernel $\mathcal{K}$ is defined implicitly, and its evaluation requires summing up among all possible trees structures number of which grows as ${({nd})}^{m}$ which is unfeasible, not to mention the requirement to inverse the kernel which requires $\mathcal{O}{(N^{2 + \omega})}$ operations which additionally rules out the applicability of classical Gaussian Processes methods with our kernel. Therefore, a typical Bayesian setup is not applicable, and we resort to the uncertainty estimation setup described in Malinin et al..

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment on real datasets", "weight": 1.0} -->

Also, the intractability of the kernel does not allow us to treat $\sigma,\delta$ in a fully Bayesian way, as it will require estimating the likelihood. Therefore, we fix them as constants, but we note that this will not affect the evaluation metrics for our setup as they are scale and translation invariant.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiment on real datasets", "weight": 1.0} -->

First, we compare KGB with SGLB since they both sample from similar posterior distributions. Thus, this comparison allows us to find out which of the algorithms does a better sampling from the posterior and thus provides us with more reliable estimates of knowledge uncertainty. Moreover, we consider the SGB approach as the most "straightforward" way to generate an ensemble of models.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiment on real datasets", "weight": 1.0} -->

In Table 5, we compare the predictive performance of the methods. Interestingly, we obtain improvements on almost all the datasets. Here we perform cross-validation to estimate statistical significance with paired $t$-test and highlight the approaches that are insignificantly different from the best one ($\text{p-value} > 0.05$). Then, we check whether uncertainty measured as the variance of the model's predictions can be used to detect errors and out-of-domain inputs. Detecting errors can be evaluated via the Prediction-Rejection Ratio (PRR). PRR measures how well uncertainty estimates correlate with errors and rank-order them. Out-of-domain (OOD) detection is usually assessed via the area under the ROC curve (AUC-ROC) for the binary task of detecting whether a sample is OOD. For this, one needs an OOD test set. We use the same OOD test sets (sampled from other datasets) as Malinin et al.. The results of this experiment are given in Table 5. We can see that the proposed method significantly outperforms the baselines for out-of-domain detection.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiment on real datasets", "weight": 1.0} -->

These improvements can be explained by the theoretical soundness of KGB: convergence properties are theoretically grounded and non-asymptotic. In contrast, for SGB, there are no general results applicable in our setting, while for SGLB the guarantees are asymptotic. In summary, these results show that our approach is superior to SGB and SGLB, achieving smaller values of RMSE and having better knowledge uncertainty estimates.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper theoretically analyses the classic gradient boosting algorithm. In particular, we show that GBDT converges to the solution of a certain Kernel Ridge Regression problem. We also introduce a simple modification of the classic algorithm allowing one to sample from the Gaussian posterior. The proposed method gives much better knowledge uncertainty estimates than the existing approaches.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We highlight the following important directions for future research. First, to explore how one can control the kernel and use it for better knowledge uncertainty estimates. Also, we do not analyze generalization in the current work, which is another important research topic. Finally, we need to establish universal approximation property which further justifies need for functional formalism.
