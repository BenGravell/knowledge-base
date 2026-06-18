Universal Off-Policy Evaluation

Topics include Partial observability.

When faced with sequential decision-making problems, it is often useful to be able to predict what would happen if decisions were made using a new policy. Those predictions must often be based on data collected under some previously used decision-making rule. Many previous methods enable such off-policy (or counterfactual) estimation of the expected value of a performance measure called the return. In this paper, we take the first steps towards a universal off-policy estimator (UnO) - one that provides off-policy estimates and high-confidence bounds for any parameter of the return distribution. We use UnO for estimating and simultaneously bounding the mean, variance, quantiles/median, inter-quantile range, CVaR, and the entire cumulative distribution of returns. Finally, we also discuss Uno's applicability in various settings, including fully observable, partially observable (i.e., with unobserved confounders), Markovian, non-Markovian, stationary, smoothly non-stationary, and discrete distribution shifts.

## Introduction

Problems requiring sequential decision-making are ubiquitous. When online experimentation is costly or dangerous, it is essential to conduct off-policy evaluation before deploying a new policy; that is, one must leverage existing data collected using some policy $\beta$ (called a behavior policy) to evaluate a performance metric of another policy $\pi$ (called the evaluation policy). For problems with high stakes, such as in terms of health or financial assets, it is also crucial to provide high-confidence bounds on the desired performance metric to ensure reliability and safety.

This raises the main question of interest: How do we develop a universal off-policy method---one that can estimate any desired performance metrics and can also provide finite-sample confidence bounds that hold simultaneously with high probability for those metrics?

A. For any distributional parameter (mean, variance, quantiles, entropy, CVaR, CDF, etc.), we provide an off-policy method to obtain (A.1) model-free estimators; (A.2) high-confidence bounds that have guaranteed coverage simultaneously for all parameters and that, perhaps surprisingly, often nearly match or outperform prior bounds specifically designed for the mean and the variance; and (A.3) approximate bounds using statistical bootstrapping that can often be significantly tighter.

Our method uses importance sampling and thus Requires knowledge of action probabilities under the behavior policy $\beta$, Any outcome under the evaluation policy should have a sufficient probability of occurring under $\beta$, and Variance of our estimators scales exponentially with the horizon length, which may be unavoidable in non-Markovian domains.

## Conclusion

We have taken the first steps towards developing a *universal off-policy estimator* (UnO), closing the open question of whether it is possible to estimate and provide finite-sample bounds (that hold with high probability) for any parameter of the return distribution in the off-policy setting, with minimal assumptions on the domain. Now, without being restricted to the most common and basic parameters, researchers and practitioners can fully characterize the (potentially dangerous or costly) behavior of a policy without having to deploy it.
