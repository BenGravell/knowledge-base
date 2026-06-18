Certainty Equivalence Is Efficient for Linear Quadratic Control

Topics include Control, Linear quadratic regulator, Linear quadratic, Linear quadratic Gaussian, Fully observed, Riccati equation.

We study the performance of the certainty equivalent controller on Linear Quadratic (LQ) control problems with unknown transition dynamics. We show that for both the fully and partially observed settings, the sub-optimality gap between the cost incurred by playing the certainty equivalent controller on the true system and the cost incurred by using the optimal LQ controller enjoys a fast statistical rate, scaling as the square of the parameter error. To the best of our knowledge, our result is the first sub-optimality guarantee in the partially observed Linear Quadratic Gaussian (LQG) setting. Furthermore, in the fully observed Linear Quadratic Regulator (LQR), our result improves upon recent work by Dean et al., who present an algorithm achieving a sub-optimality gap linear in the parameter error. A key part of our analysis relies on perturbation bounds for discrete Riccati equations. We provide two new perturbation bounds, one that expands on an existing result from Konstantinov et al., and another based on a new elementary proof strategy.

## Introduction

One of the most straightforward methods for controlling a dynamical system with unknown transitions is based on the *certainty equivalence principle*: a model of the system is fit by observing its time evolution, and a control policy is then designed by treating the fitted model as the truth. Despite the simplicity of this method, it is challenging to guarantee its efficiency because small modeling errors may propagate to large, undesirable behaviors on long time horizons. As a result, most work on controlling systems with unknown dynamics has explicitly incorporated robustness against model uncertainty.

In this work, we show that for the standard baseline of controlling an unknown linear dynamical system with a quadratic objective function known as Linear Quadratic (LQ) control, certainty equivalent control synthesis achieves *better* cost than prior methods that account for model uncertainty. Our results hold for both the fully observed Linear Quadratic Regulator (LQR) and the partially observed Linear Quadratic Gaussian (LQG) setting....

## Conclusion

Though a naïve Taylor expansion suggests that the fast rates we derive here must be achievable, precisely computing such rates has been open since the 80s. All of the pieces we used here have existed in the literature for some time, and perhaps it has just required a bit of time to align contemporary rate-analyses in learning theory with earlier operator theoretic work in optimal control. There remain many possible extensions to this work. The robust control approach of Dean et al. applies to many different objective functions besides quadratic costs, such as $\mathcal{H}_{\infty}$ and $\mathcal{L}_{1}$ control....

where we used Proposition 1 and the assumption on $f{(\varepsilon)}$.

Our result explains the behavior observed in Figure 4 of Dean et al.. The authors propose two procedures for synthesizing robust controllers for LQR with unknown transitions: one which guarantees robustness of the performance gap $\hat{J} - J_{\star}$, and one which only guarantees the stability of the closed loop system. Dean et al. observed that the latter performs better in the small estimation error regime, which happens because the robustness constraint of the synthesis procedure becomes inactive when the estimation error is small enough....
