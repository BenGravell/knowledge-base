Analysis of Thompson Sampling for the Multi-armed Bandit Problem

Topics include Thompson sampling, Multi-armed bandits, Bayesian algorithms, Regret analysis, Exploration exploitation, Stochastic bandits, Sequential decision making.

Provides one of the first logarithmic expected-regret analyses for Thompson sampling in stochastic multi-armed bandits. The paper helped move Thompson sampling from an empirically attractive Bayesian heuristic toward a theoretically grounded bandit algorithm, though with gap-dependent constants that later work refined.

The multi-armed bandit problem is a popular model for studying exploration/exploitation trade-off in sequential decision problems. Many algorithms are now available for this well-studied problem. One of the earliest algorithms, given by W. R. Thompson, dates back to 1933. This algorithm, referred to as Thompson Sampling, is a natural Bayesian algorithm. The basic idea is to choose an arm to play according to its probability of being the best arm. Thompson Sampling algorithm has experimentally been shown to be close to optimal. In addition, it is efficient to implement and exhibits several desirable properties such as small regret for delayed feedback. However, theoretical understanding of this algorithm was quite limited. In this paper, for the first time, we show that Thompson Sampling algorithm achieves logarithmic expected regret for the multi-armed bandit problem. More precisely, for the two-armed bandit problem, the expected regret in time T is O(fracln TDelta + 1/Delta^). And, for the N-armed bandit problem, the expected regret in time T is O([(sum_i = 2^(N) 1/Delta_i^)^] ln T). Our bounds are optimal but for the dependence on Delta_i and the constant factors in big-Oh.

## Introduction

Multi-armed bandit (MAB) problem models the exploration/exploitation trade-off inherent in sequential decision problems. Many versions and generalizations of the multi-armed bandit problem have been studied in the literature; in this paper we will consider a basic and well-studied version of this problem: the stochastic multi-armed bandit problem.

Recently, TS has attracted considerable attention. Several studies (e.g., ) have empirically demonstrated the efficacy of Thompson Sampling: provides a detailed discussion of probability matching techniques in many general settings along with favorable empirical comparisons with other techniques. demonstrate that empirically TS achieves regret comparable to the lower bound of; and in applications like display advertising and news article recommendation, it is competitive to or better than popular methods such as UCB.

It has been suggested that despite being easy to implement and being competitive to the state of the art methods, the reason TS is not very popular in literature could be its lack of strong theoretical analysis. Existing theoretical analyses in provide weak guarantees, namely, a bound of $o{(T)}$ on expected regret in time $T$. In this paper, for the first time, we provide a logarithmic bound on expected regret of TS algorithm in time $T$ that is close to the lower bound of. Before stating our results, we describe the MAB problem and the TS algorithm formally.

## Conclusion

In this paper, we showed theoretical guarantees for Thompson Sampling close to other state of the art methods, like UCB. Our result is a first step in theoretical understanding of TS and there are several avenues to explore for the future work: There is a gap between our upper bounds and the lower bound of. While it may be easy to improve the constant factors in our upper bounds by making the analysis more careful (but more complicated), it seems harder to improve the dependence on the $\Delta$'s.
