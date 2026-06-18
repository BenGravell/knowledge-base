Flat Minima Generalize for Low-rank Matrix Recovery

Empirical evidence suggests that for a variety of overparameterized nonlinear models, most notably in neural network training, the growth of the loss around a minimizer strongly impacts its performance. Flat minima - those around which the loss grows slowly - appear to generalize well. This work takes a step towards understanding this phenomenon by focusing on the simplest class of overparameterized nonlinear models: those arising in low-rank matrix recovery. We analyze overparameterized matrix and bilinear sensing, robust PCA, covariance matrix estimation, and single hidden layer neural networks with quadratic activation functions. In all cases, we show that flat minima, measured by the trace of the Hessian, exactly recover the ground truth under standard statistical assumptions. For matrix completion, we establish weak recovery, although empirical evidence suggests exact recovery holds here as well. We conclude with synthetic experiments that illustrate our findings and discuss the effect of depth on flat solutions.

## Introduction

Recent advances in machine learning and artificial intelligence have relied on fitting highly overparameterized models, notably deep neural networks, to observed data tan2019efficientnet; kolesnikov2020big; huang2019gpipe; zhang2021understanding. In such settings, the number of parameters of the model is much greater than the number of data samples, thereby resulting in models that achieve near-zero training error....

Existing literature highlights two intriguing properties---small norm and flat landscape---that correlate with generalization neyshabur2017exploring; dziugaite2017computing; dinh2017sharp. Indeed, it has long been known that the magnitude of the weights plays an important role for neural network training. As a result, one typically incorporates a squared $\ell_{2}$-penalty on the weights---called weight decay---when applying iterative methods....

For any integer $k \in {\mathbb{N}}$, Lemma 4.5. ‣ 4 Flat minima under RIP conditions: matrix and bilinear sensing ‣ Flat minima generalize for low-rank matrix recovery") ensures that there exist numerical constants ${\delta_{1},\delta_{2}} > 0$ and constants ${c_{0},C_{0}} > 0$ depending only on $l$ such that in the regime $m \geq {c_{0}r{({d_{1} + d_{2}})}}$, with probability at least $1 - {\exp{({- {C_{0}m}})}}$, the measurement map $\mathcal{A}$ satisfies $\ell_{1}/\ell_{2}$ RIP with parameters $({lr_{\natural}},\delta_{1},\delta_{2})$. Lemma 4.9....

Therefore in this regime, we may upper bound the condition number $\kappa$ of $D_{1}$ and $D_{2}$ by $\frac{1 + \delta}{1 - \delta}$. In light of Lemma 4.7, in order to ensure exact recovery, it remains to simply choose a large enough $l$ such that the inequality ${\frac{\delta_{2}}{\delta_{1}} \cdot {(\frac{1 + \delta}{1 - \delta})}^{2}} \leq \sqrt{l}$ holds (recall $\delta_{1},\delta_{2}$ are numerical constants). An application of Lemma 4.7 and Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") completes the proof. ∎

Therefore, a natural convex relaxation for finding the flattest solution drops the rank constraint:

Consequently, the scaled trace is simply

We next verify (23. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix...
