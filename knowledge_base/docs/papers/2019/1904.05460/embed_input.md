Least Squares Auto-Tuning

Least squares is by far the simplest and most commonly applied computational method in many fields. In almost all applications, the least squares objective is rarely the true objective. We account for this discrepancy by parametrizing the least squares problem and automatically adjusting these parameters using an optimization algorithm. We apply our method, which we call least squares auto-tuning, to data fitting.

## Introduction

Since its introduction over 200 years ago by Legendre and Gauss, the method of least squares has been one of the most widely employed computational techniques in many fields, including machine learning and statistics, signal processing, control, robotics, and finance. Its wide application primarily comes from the fact that it has a simple analytical solution, it is easy to understand, and very efficient and stable algorithms for computing its solution have been developed.

To account for the discrepancy between the least squares objective and the true objective, it is common practice to modify (or tune) the least squares problem that is solved to obtain a good solution in terms of the true objective. Typical tricks here include modifying the data, adding additional (regularization) terms to the cost function, or varying hyper-parameters or weights in the least squares problem to be solved.

Our focus in this paper is on automating the process of least squares tuning, for a variety of data fitting applications. We parametrize the least squares problem to be solved by hyper-parameters, and then automatically adjust these hyper-parameters using a gradient-based optimization algorithm, to obtain the best (or at least better) true performance. This lets us automatically search the hyper-parameter design space, which can lead us to better designs than could be found manually, or help us find good values of the hyper-parameters more quickly than if the adjustments were done manually.

One of our main contributions in this paper is the observation that least squares auto-tuning is very effective for a wide variety of data fitting problems that are usually handled using more complex and advanced methods, such as non-quadratic loss functions or regularizers in regression, or special loss functions for classification problems. In addition, it can simultaneously adjust hyper-parameters in the feature generation chain. Through several examples, we show that ordinary least squares, used for over 200 years, coupled with automated hyper-parameter tuning, can be very effective as a method for data fitting.

## Conclusion

The authors are currently writing a second paper, *Least Squares Auto-Tuning Examples*, which will detail many more applications of the methods described in this paper to data fitting, control, and estimation.
