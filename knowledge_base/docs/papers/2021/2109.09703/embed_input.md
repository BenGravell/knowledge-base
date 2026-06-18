Learning to Forecast Dynamical Systems from Streaming Data

Kernel analog forecasting (KAF) is a powerful methodology for data-driven, non-parametric forecasting of dynamically generated time series data. This approach has a rigorous foundation in Koopman operator theory and it produces good forecasts in practice, but it suffers from the heavy computational costs common to kernel methods. This paper proposes a streaming algorithm for KAF that only requires a single pass over the training data. This algorithm dramatically reduces the costs of training and prediction without sacrificing forecasting skill. Computational experiments demonstrate that the streaming KAF method can successfully forecast several classes of dynamical systems (periodic, quasi-periodic, and chaotic) in both data-scarce and data-rich regimes. The overall methodology may have wider interest as a new template for streaming kernel regression.

## Introduction

Forecasting problems are ubiquitous in physical science and engineering applications, including climate prediction, navigation, and medicine. In these settings, we do not possess complete information about the state of the system, and we may not have full knowledge of the equations of motion. Owing to our lack of omniscience, it is not possible to make predictions by integrating the current state forward in time. Instead, we may acquire training data by observing some aspect of the system's evolution. The goal is to build a compact model of the dynamics of this observable....

Kernel analog forecasting (KAF) offers a promising approach to this problem. KAF is a data-driven, non-parametric forecasting technique that is best understood as a type of regularized kernel regression (Section 2). KAF emerged from recent efforts to translate Koopman operator theory into effective computational methodologies for forecasting (Section 2.7). The approach belongs to a rapidly expanding literature on operator-theoretic techniques for low-order modeling of dynamical systems, including methods based on kernels.

## Conclusions

Kernel analog forecasting is a regression-based approach to forecasting dynamical systems that offers a theoretical guarantee of asymptotically optimal predictions (in the $L_{2}$ or RMSE sense) in the large-data limit. By incorporating two randomized approximation techniques from numerical linear algebra---random Fourier features and the randomized Nyström method---we developed a streaming implementation of kernel analog forecasting. This approach makes it possible to build forecasting models from large data sets where the KAF methodology is theoretically justified....

The randomized Nyström approximation ${\check{\mathbf{C}}}_{xx}$ provides a good low-rank approximation of the covariance ${\mathbf{C}}_{xx}$; see \[78, Thms. 4.1--4.2\]. Our ultimate formula for the weight matrix becomes

The simple idea behind RFF is to approximate the kernel using a Monte Carlo estimate of the integral. Let the parameter $s \in {\mathbb{N}}$ designate the number of random features. Once and for all, draw and fix independent random vectors ${{\mathbf{z}}_{1},\ldots,{\mathbf{z}}_{s}} \in {\mathbb{R}}^{d}$ that are distributed according to the probability measure $\nu$....
