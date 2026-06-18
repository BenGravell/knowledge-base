Optimizing Static Linear Feedback: Gradient Method

Topics include Optimal control, Optimization, Control, Linear quadratic regulator, Optimization problem, Stationary point, Gradient method, Output feedback.

The linear quadratic regulator is the fundamental problem of optimal control. The abstract also notes that its state feedback version was set and solved in the early 1960s.

The linear quadratic regulator is the fundamental problem of optimal control. Its state feedback version was set and solved in the early 1960s. However the static output feedback problem has no explicit-form solution. It is suggested to look at both of them from another point of view as matrix optimization problems, where the variable is a feedback matrix gain. The properties of such a function are investigated, it turns out to be smooth, but not convex, with possible non-connected domain. Nevertheless, the gradient method for it with the special step-size choice converges to the optimal solution in the state feedback case and to a stationary point in the output feedback case. The results can be extended for the general framework of unconstrained optimization and for reduced gradient method for minimization with equality-type constraints.

## Introduction

The linear quadratic regulator (LQR) problem is formulated as an optimization problem of minimizing a quadratic integral cost with respect to control function. It has been extensively analyzed in the last century since the seminal works of Kalman in 1960. The main result claims that for an infinite-horizon LTI system the optimal control can be expressed as linear static state feedback. The optimal gain can be found by solving the algebraic matrix Riccati equation (ARE). The results became classical and were immediately included in textbooks on control....

The nearest relative of LQR is output feedback --- the same LTI system with quadratic performance in the case when full state is not measured but some output (a linear function of the state) is available. The attempts to apply static output feedback (SOF) met numerous difficulties. The problem was first addressed by Levine and Athans, but it was discovered that such stabilizing control may be lacking and there are no simple optimality certificates if it does exist. Serious theoretical efforts were directed on the formulation of existence conditions, see, but the problem remains open....

## Conclusion

The results can be extended in several directions. First, more efficient computational schemes are of interest. Gradient method is the simplest method for unconstrained smooth optimization. Accelerated algorithms - such as conjugate gradient, heavy ball, Nesterov acceleration - are developed for strongly convex functions. But we have proved (Corollary 3.15 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020....

### Second derivative of $f{(K)}$

For $C = I$ equation becomes ${{{({A - {BK}})}^{\top}X} + {X{({A - {BK}})}} + {K^{\top}RK} + Q} = 0$. It is proved in that equality here can be replaced with inequality and after change of variables $P = X^{- 1}$ definition of stabilizing controllers becomes

As we have seen, $f{(K)}$ can be noncovex even for state feedback case (SLQR). However there is a useful property which replaces convexity in validation of minimization methods. This property is referred to in the optimization literature as gradient domination or Ležanski-Polyak-Lojasiewicz (LPL) condition.

A promising tool for solving both state and output feedback control is the direct gradient method....
