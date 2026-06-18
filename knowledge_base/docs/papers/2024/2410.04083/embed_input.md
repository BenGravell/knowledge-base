<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OPTAMI: Global Superlinear Convergence of High-order Methods

Topics include Convex optimization, Optimization, OPTAMI.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Second-order methods for convex optimization outperform first-order methods in terms of theoretical iteration convergence, achieving rates up to O(k^(-5)) for highly-smooth functions. However, their practical performance and applications are limited due to their multi-level structure and implementation complexity. In this paper, we present new results on high-order optimization methods, supported by their practical performance. First, we show that the basic high-order methods, such as the Cubic Regularized Newton Method, exhibit global superlinear convergence for mu-strongly star-convex functions, a class that includes mu-strongly convex functions and some non-convex functions. Theoretical convergence results are both inspired and supported by the practical performance of these methods. Secondly, we propose a practical version of the Nesterov Accelerated Tensor method, called NATA. It significantly outperforms the classical variant and other high-order acceleration techniques in practice. The convergence of NATA is also supported by theoretical results. Finally, we introduce an open-source computational library for high-order methods, called OPTAMI.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This library includes various methods, acceleration techniques, and subproblem solvers, all implemented as PyTorch optimizers, thereby facilitating the practical application of high-order methods to a wide range of optimization problems. We hope this library will simplify research and practical comparison of methods beyond first-order.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Basic Methods", "weight": 1.0} -->

where, for $p = 1$, we simplify notation to $\Phi_{x}{(y)}$. From, we can get the next upper-bound of the function $f{(x)}$

<!-- chunk {"id": "body-0005", "role": "body", "section": "Basic Methods", "weight": 1.0} -->

which leads us to the high-order model

<!-- chunk {"id": "body-0006", "role": "body", "section": "Basic Methods", "weight": 1.0} -->

Now, we can formulate the Basic Tensor method

<!-- chunk {"id": "body-0007", "role": "body", "section": "Basic Methods", "weight": 1.0} -->

with the convergence rate $O\left( \frac{M_{1}R^{2}}{T} \right)$ for convex functions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Basic Methods", "weight": 1.0} -->

with the convergence rate $O\left( \frac{M_{3}D^{4}}{T^{3}} \right)$. The step can be performed with almost the same computational complexity (up to a logarithmic factor) by using the Bregman Distance Gradient Method as a subsolver. The details are written in the Appendix C.1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Global Superlinear Convergence of High-order Methods for Strongly Star-Convex Functions", "weight": 1.0} -->

In this section, we establish the global superlinear convergence of high-order methods for uniformly star-convex functions. We begin by defining global superlinear convergence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Nesterov Accelerated Tensor Method with $A_{t}$-Adaptation (NATA)", "weight": 1.0} -->

In this section, we focus on Nesterov Acceleration for tensor methods proposed. Theoretically, the Nesterov Accelerated Tensor Method (NATM), with a covergence rate $O\left( T^{- {({p + 1})}} \right)$, dominates Basic Tensor Method with the rate $O\left( T^{- p} \right)$. However, in practice, it is often observed that the NATM method is slower, particularly in the initial stages (Scieur Carmon et al. Antonakopoulos et al., ). To illustrate this, we present a practical example using the logistic regression problem with $\mu = 0$. In Figure 3(a) ‣ OPTAMI: Global Superlinear Convergence of High-order Methods"), the accelerated versions appear slower, which contradicts the theoretical expectations. In this section, we investigate the causes of this underperformance and propose a solution. We begin by revisiting the classical Nesterov Accelerated method, with further details provided in Appendix C.2.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Nesterov Accelerated Tensor Method with $A_{t}$-Adaptation (NATA)", "weight": 1.0} -->

Theoretically, $A_{t}$ should be defined as ${A_{t} = {\frac{\nu_{p}}{L_{p}}t^{p + 1}}},$ where $\nu_{2} = \frac{1}{24}$ for $M_{2} = L_{2}$ and $\nu_{3} = \frac{5}{3024}$ for $M_{3} = {6L_{3}}$. However, the values of $\nu_{p}$ appear to be quite small, which limits the speed of convergence. Can these values be increased? The answer is yes. We propose the Nesterov Accelerated Tensor Method with $A_{t}$-Adaptation, which selects these parameters more aggressively, leading to faster convergence.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Computational Comparison of Acceleration Methods", "weight": 1.0} -->

In this section, we present the practical comparison of different acceleration techniques for tensor methods for convex optimization. We choose five main variants: Nesterov Accelerated Tensor Method ) with a rate $O{(T^{- {({p + 1})}})}$; Near-Optimal Tensor Acceleration with a rate $\overset{\sim}{O}{(T^{- {{({{3p} + 1})}/2}})}$; Near-Optimal Proximal-Point Acceleration Method with Segment Search with the rate $\overset{\sim}{O}{(T^{- {{({{3p} + 1})}/2}})}$; and Optimal Acceleration with a rate $O{(T^{- {{({{3p} + 1})}/2}})}$, where $\overset{\sim}{O}{( \cdot )}$ means up to a logarithmic factor. Next, we present experiments for logistic regression on the a9a dataset in Figure and on the w8a dataset in Figure.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Computational Comparison of Acceleration Methods", "weight": 1.0} -->

Let us now discuss the performance of the methods. The new NATA acceleration outperforms all other methods. We attribute this to NATA's strategy of maximizing ${\overset{\sim}{a}}_{t}$ and ${\overset{\sim}{A}}_{t}$, which enables even faster convergence in the later stages. The second-best performer is the Near-Optimal Tensor Acceleration method. Although it struggles initially due to a large number of line-search iterations per step, it gradually requires fewer line-search iterations---less than two per step on average---as parameters from previous line-search steps become well-suited for the current iteration. With fewer line-search iterations, the method accelerates and outpaces the remaining competitors. A promising direction for improving this method would be to refine the line-search process through an advanced line-search strategy. Next, the classical Accelerated method starts off slower than the basic method without acceleration. Eventually, the method accelerates and overtakes the basic version. Near-Optimal Proximal-Point Acceleration Method with Segment Search performs very similarly to Basic Methods.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Computational Comparison of Acceleration Methods", "weight": 1.0} -->

It has much fewer iterations, but it does a safe segment search with an average of 3 Basic steps per search. Lastly, the Optimal Acceleration method performs the worst in practice. We believe the main issue lies in the internal parameters, which need tuning and adaptation, as we used the theoretical parameters in our implementation. This leads to many inner iterations without significant global progress. Improving these parameters presents an open question for future research. More details can be found in the Appendix D.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations. This paper primarily focuses on high-order methods which come with certain limitations. First of all, they have computational and memory limitations in high-dimensional spaces, due to the need for Hessian calculations. There are, however, approaches to overcome this, such as using first-order subsolvers, or inexact Hessian approximations like Quasi-Newton approximations (BFGS, L-SR1). In this paper, we focus on the exact Hessian to analyze methods' peak performance.\
Another limitation arises from the specific function classes and the theoretical results considered. Nonetheless, many of the proposed methods can be practically applied to a broader set of problems. For instance, the CRN performs competitively from general non-convex to strongly convex functions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Conclusion and Future work. In the paper, we demonstrated that the basic high-order methods exhibit global superlinear convergence for $\mu$-strongly star-convex functions. This result is significant because it shows that high-order methods accelerate with each iteration, in stark contrast to first-order methods, which typically have a steady linear convergence rate. This raises intriguing questions: Can superlinear convergence rates be established for accelerated high-order methods as well? What is the best possible global per-iteration decrease that we can theoretically guarantee?\
In the second part of the paper, we proposed NATA, a practical acceleration technique. NATA employs a more aggressive schedule adaptation for $A_{t}$, enabling faster convergence. Our experimental results show that NATA significantly outperforms both basic and accelerated methods, including near-optimal and optimal methods. This opens up another interesting question: Could other high-order methods be optimized by addressing practical issues that arise due to overly conservative theoretical guarantees?\
Finally, we introduced OPTAMI, an open-source library designed to make high-order optimization methods more accessible and easier to experiment. We plan to expand this library to cover a wider range of settings and incorporate more optimization methods in the future.
