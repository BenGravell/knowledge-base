Least Squares Auto-Tuning

Least squares is by far the simplest and most commonly applied computational method in many fields. In almost all applications, the least squares objective is rarely the true objective. We account for this discrepancy by parametrizing the least squares problem and automatically adjusting these parameters using an optimization algorithm. We apply our method, which we call least squares auto-tuning, to data fitting.

## Introduction

Since its introduction over 200 years ago by Legendre and Gauss, the method of least squares has been one of the most widely employed computational techniques in many fields, including machine learning and statistics, signal processing, control, robotics, and finance \[\]. Its wide application primarily comes from the fact that it has a simple analytical solution, it is easy to understand, and very efficient and stable algorithms for computing its solution have been developed.

In essentially all applications, the least squares objective is not the true objective; rather it is a surrogate for the real goal. For example, in least squares data fitting, the objective is not to solve a least squares problem involving the training data set, but rather to find a model or predictor that generalizes, i.e., achieves small error on new unseen data. In control, the least squares objective is only a surrogate for keeping the state near some target or desired value, while keeping the control or actuator input small.

## Conclusion

The authors are currently writing a second paper, *Least Squares Auto-Tuning Examples*, which will detail many more applications of the methods described in this paper to data fitting, control, and estimation.

In a data fitting problem, we have *training data* consisting of *inputs* ${u_{1},\ldots,u_{N}} \in \mathcal{U}$ and *outputs* ${y_{1},\ldots,y_{N}} \in \text{R}^{m}$. In *least squares data fitting*, we fit the parameters of a predictor

It can be shown (see Appendix A) that the gradients of $\psi$ with respect to $A$ and $B$ are given by

The next hyper-parameter subvector that we consider is the regularization hyper-parameter $\omega^{reg}$. The regularization hyper-parameter affects the

To account for the discrepancy between the least squares objective and the true objective, it is common practice to modify (or tune) the least squares problem that is solved to obtain a good solution in terms of the true objective. Typical tricks here include modifying the data, adding additional (regularization) terms to the cost function, or varying hyper-parameters or weights in the least squares problem to be solved.

The art of using least squares in applications is generally in how to carry out these modifications or choose these additional terms, and how to choose the hyper-parameters....
