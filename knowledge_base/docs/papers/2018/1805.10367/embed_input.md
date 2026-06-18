<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization

Topics include Convex optimization, Nonconvex optimization, Stochastic optimization, Neural networks, Classification, Optimization, ZO-SVRG, ZO, Variance reduction, Black box.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As application demands for zeroth-order (gradient-free) optimization accelerate, the need for variance reduced and faster converging approaches is also intensifying. This paper addresses these challenges by presenting: a) a comprehensive theoretical analysis of variance reduced zeroth-order (ZO) optimization, b) a novel variance reduced ZO algorithm, called ZO-SVRG, and c) an experimental evaluation of our approach in the context of two compelling applications, black-box chemical material classification and generation of adversarial examples from black-box deep neural network models. Our theoretical analysis uncovers an essential difficulty in the analysis of ZO-SVRG: the unbiased assumption on gradient estimates no longer holds. We prove that compared to its first-order counterpart, ZO-SVRG with a two-point random gradient estimator could suffer an additional error of order O(1/b), where b is the mini-batch size. To mitigate this error, we propose two accelerated versions of ZO-SVRG utilizing variance reduced gradient estimators, which achieve the best rate known for ZO stochastic optimization (in terms of iterations).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our extensive experimental results show that our approaches outperform other state-of-the-art ZO algorithms, and strike a balance between the convergence rate and the function query complexity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zeroth-order (gradient-free) optimization is increasingly embraced for solving machine learning problems where explicit expressions of the gradients are difficult or infeasible to obtain. Recent examples have shown zeroth-order (ZO) based generation of prediction-evasive, black-box adversarial attacks on deep neural networks (DNNs) as effective as state-of-the-art white-box attacks, despite leveraging only the inputs and outputs of the targeted DNN. Additional classes of applications include network control and management with time-varying constraints and limited computation capacity, and parameter inference of black-box systems. ZO algorithms achieve gradient-free optimization by approximating the full gradient via gradient estimators based on only the function values.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although many ZO algorithms have recently been developed and analyzed, they often suffer from the high variances of ZO gradient estimates, and in turn, hampered convergence rates. In addition, these algorithms are mainly designed for convex settings, which limits their applicability in a wide range of (non-convex) machine learning problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the problem of design and analysis of variance reduced and faster converging nonconvex ZO optimization methods. To reduce the variance of ZO gradient estimates, one can draw motivations from similar ideas in the first-order regime. The stochastic variance reduced gradient (SVRG) is a commonly-used, effective first-order approach to reduce the variance. Due to the variance reduction, it improves the convergence rate of stochastic gradient descent (SGD) from $O{({1/\sqrt{T}})}$^11^1In the big $O$ notation, the constant numbers are ignored, and the dominant factors are kept. to $O{({1/T})}$, where $T$ is the total number of iterations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although SVRG has shown a great promise, applying similar ideas to ZO optimization is not a trivial task. The main challenge arises due to the fact that SVRG relies upon the assumption that a stochastic gradient is an unbiased estimate of the true batch/full gradient, which unfortunately does not hold in the ZO case. Therefore, it is an open question whether the ZO stochastic variance reduced gradient could enable faster convergence of ZO algorithms. In this paper, we attempt to fill the gap between ZO optimization and SVRG.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions We propose and evaluate a novel ZO algorithm for nonconvex stochastic optimization, ZO-SVRG, which integrates SVRG with ZO gradient estimators. We show that compared to SVRG, ZO-SVRG achieves a similar convergence rate that decays linearly with $O{({1/T})}$ but up to an additional error correction term of order $1/b$, where $b$ is the mini-batch size. Without a careful treatment, this correction term (e.g., when $b$ is small) could be a critical factor affecting the optimization performance. To mitigate this error term, we propose two accelerated ZO-SVRG variants, utilizing reduced variance gradient estimators. These yield a faster convergence rate towards $O{({d/T})}$, the best known iteration complexity bound for ZO stochastic optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work offers a comprehensive study on how ZO gradient estimators affect SVRG on both iteration complexity (i.e., convergence rate) and function query complexity. Compared to the existing ZO algorithms, our methods can strike a balance between iteration complexity and function query complexity. To demonstrate the flexibility of our approach in managing this trade-off, we conduct an empirical evaluation of our proposed algorithms and other state-of-the-art algorithms on two diverse applications: black-box chemical material classification and generation of universal adversarial perturbations from black-box deep neural network models. Extensive experimental results and theoretical analysis validate the effectiveness of our approaches.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumptions", "weight": 1.0} -->

Both A1 and A2 are the standard assumptions used in nonconvex optimization literature. Note that A2 is milder than the assumption of bounded gradients. For example, if ${\|{{\nabla f_{i}}{(\mathbf{x})}}\|}_{2} \leq \overset{\sim}{\sigma}$, then A2 is satisfied with $\sigma = {2\overset{\sim}{\sigma}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "ZO gradient estimation", "weight": 1.0} -->

Given an individual cost function $f_{i}$ (or an arbitrary function under A1 and A2), a two-point random gradient estimator $\hat{\nabla}f_{i}{(\mathbf{x})}$ is defined by

<!-- chunk {"id": "body-0012", "role": "body", "section": "ZO gradient estimation", "weight": 1.0} -->

where recall that $d$ is the number of optimization variables, $\mu > 0$ is a smoothing parameter^22^2The parameter $\mu$ can be generalized to $\mu_{i}$ for $i \in {\lbrack n\rbrack}$. Here we assume $\mu_{i} = \mu$ for ease of representation., and $\{\mathbf{u}_{i}\}$ are i.i.d. random directions drawn from a uniform distribution over a unit sphere. In general, RandGradEst is a biased approximation to the true gradient ${\nabla f_{i}}{(\mathbf{x})}$, and its bias reduces as $\mu$ approaches zero. However, in a practical system, if $\mu$ is too small, then the function difference could be dominated by the system noise and fails to represent the function differential.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Instead of using a single sample $\mathbf{u}_{i}$ in RandGradEst, the average of $q$ i.i.d. samples ${\{\mathbf{u}_{i,j}\}}_{j = 1}^{q}$ can also be used for gradient estimation,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1", "weight": 1.0} -->

which we call an average random gradient estimator.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In addition to RandGradEst and Avg-RandGradEst, the work considered a coordinate-wise gradient estimator. Here every partial derivative is estimated via the two-point querying scheme under fixed direction vectors,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1", "weight": 1.0} -->

where $\mu_{\ell} > 0$ is a coordinate-wise smoothing parameter, and $\mathbf{e}_{\ell} \in {\mathbb{R}}^{d}$ is a standard basis vector with $1$ at its $\ell$th coordinate, and $0$s elsewhere. Compared to RandGradEst, CoordGradEst is deterministic and requires $d$ times more function queries. However, as will be evident later, it yields an improved iteration complexity (i.e., convergence rate). More details on ZO gradient estimation can be found in Appendix A.1 gradient estimators ‣ Appendix A Supplementary material ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization").

<!-- chunk {"id": "body-0017", "role": "body", "section": "SVRG: from first-order to zeroth-order", "weight": 1.0} -->

It has been shown in that the first-order SVRG achieves the convergence rate $O{({1/T})}$, yielding $O{(\sqrt{T})}$ less iterations than the ordinary SGD for solving finite sum problems. The key step of SVRG^33^3Different from the standard SVRG, we consider its mini-batch variant. (Algorithm 1) is to generate an auxiliary sequence $\hat{\mathbf{x}}$ at which the full gradient is used as a reference in building a modified stochastic gradient estimate

<!-- chunk {"id": "body-0018", "role": "body", "section": "SVRG: from first-order to zeroth-order", "weight": 1.0} -->

where $\hat{\mathbf{g}}$ denotes the gradient estimate at $\mathbf{x}$, $\mathcal{I} \subseteq {\lbrack n\rbrack}$ is a mini-batch of size $b$ (chosen uniformly randomly^44^4For mini-batch $\mathcal{I}$, SVRG assumes i.i.d. samples with replacement, while a variant of SVRG (called SCSG) assumes samples without replacement. This paper considers both sampling strategies.), and ${{\nabla f}{(\mathbf{x})}} = {{\nabla f_{\lbrack n\rbrack}}{(\mathbf{x})}}$. The key property of (2 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization")) is that $\hat{\mathbf{g}}$ is an unbiased gradient estimate of ${\nabla f}{(\mathbf{x})}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SVRG: from first-order to zeroth-order", "weight": 1.0} -->

The gradient blending (2 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization")) is also motivated by a variance reduced technique known as control variate. The link between SVRG and control variate is discussed in Appendix A.2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "SVRG: from first-order to zeroth-order", "weight": 1.0} -->

In the ZO setting, the gradient blending (2 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization")) is approximated using only function values,

<!-- chunk {"id": "body-0021", "role": "body", "section": "SVRG: from first-order to zeroth-order", "weight": 1.0} -->

where ${\hat{\nabla}f{(\mathbf{x})}} = {\hat{\nabla}f_{\lbrack n\rbrack}{(\mathbf{x})}}$, and $\hat{\nabla}f_{i}$ is a ZO gradient estimate specified by RandGradEst, Avg-RandGradEst or CoordGradEst. Replacing (2 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization")) with (3 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization")) in SVRG (Algorithm 1) leads to a new ZO algorithm, which we call ZO-SVRG (Algorithm 2). We highlight that although ZO-SVRG is similar to SVRG except the use of ZO gradient estimators to estimate batch, mini-batch, as well as blended gradients, this seemingly minor difference yields an essential difficulty in the analysis of ZO-SVRG. That is, the unbiased assumption on gradient estimates used in SVRG no longer holds.

<!-- chunk {"id": "body-0022", "role": "body", "section": "SVRG: from first-order to zeroth-order", "weight": 1.0} -->

Thus, a careful analysis of ZO-SVRG is much needed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "ZO-SVRG and convergence analysis", "weight": 1.0} -->

In what follows, we focus on the analysis of ZO-SVRG using RandGradEst. Later, we will study ZO-SVRG with Avg-RandGradEst and CoordGradEst. We start by investigating the second-order moment of the blended ZO gradient estimate ${\hat{\mathbf{v}}}_{k}^{s}$ in the form of (3 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization")); see Proposition 1 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization").

<!-- chunk {"id": "body-0024", "role": "body", "section": "Acceleration of ZO-SVRG", "weight": 1.0} -->

In this section, we improve the iteration complexity of ZO-SVRG (Algorithm 2) by using Avg-RandGradEst and CoordGradEst, respectively. We start by comparing the squared errors of different gradient estimates to the true gradient $\nabla f$, as formalized in Proposition 2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Applications and experiments", "weight": 1.0} -->

We evaluate the performance of our proposed algorithms on two applications: black-box classification and generating adversarial examples from black-box DNNs. The first application is motivated by a real-world material science problem, where a material is classified to either be a conductor or an insulator from a density function theory (DFT) based black-box simulator. The second application arises in testing the robustness of a deployed DNN via iterative model queries.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

We consider a non-linear least square problem \[32, Sec. 3.2\], i.e., problem with ${f_{i}{(\mathbf{x})}} = \left( {y_{i} - {\phi{(\mathbf{x};\mathbf{a}_{i})}}} \right)^{2}$ for $i \in {\lbrack n\rbrack}$. Here $(\mathbf{a}_{i},y_{i})$ is the $i$th data sample containing feature vector $\mathbf{a}_{i} \in {\mathbb{R}}^{d}$ and label $y_{i} \in {\{ 0,1\}}$, and $\phi{(\mathbf{x};\mathbf{a}_{i})}$ is a black-box function that only returns the function value given an input. The used dataset consists of $N = 1000$ crystalline materials/compounds extracted from Open Quantum Materials Database.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

Each compound has $d = 145$ chemical features, and its label ($0$ is conductor and $1$ is insulator) is determined by a DFT simulator. Due to the black-box nature of DFT, the true $\phi$ is unknown^66^6 One can mimic DFT simulator using a logistic function once the parameter $\mathbf{x}$ is learned from ZO algorithms.. We split the dataset into two equal parts, leading to $n = 500$ training samples and $({N - n})$ testing samples. We refer readers to Appendix A.10 for more details on our dataset and the setting of experiments.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

(a) Training loss versus iterations (b) Training loss versus function queries
Figure 2: Comparison of different ZO algorithms for the task of chemical material classification.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

Method ZO-SGD ZO-SVRC ZO-SVRG ZO-SVRG-Coord ZO-SVRG-Ave # of epochs 14600 100 2920 50 365 Error (%) 12.56% 23.70% 11.18% 20.67% 15.26%
Table 2: Testing error for chemical material classification using 7.3 × 106 function queries.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

In Fig. 2, we present the training loss against the number of epochs (i.e., iterations divided by the epoch length $m = 50$) and function queries. We compare our proposed algorithms ZO-SVRG, ZO-SVRG-Coord and ZO-SVRG-Ave with ZO-SGD and ZO-SVRC. Fig. 2-(a) presents the convergence trajectories of ZO algorithms as functions of the number of epochs, where ZO-SVRG is evaluated under different mini-batch sizes $b \in {\{ 1,10,40\}}$. We observe that the convergence error of ZO-SVRG decreases as $b$ increases, and for a small mini-batch size $b \leq 10$, ZO-SVRG likely converges to a neighborhood of a critical point as shown by Corollary 1 ‣ Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization").

<!-- chunk {"id": "body-0031", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

We also note that our proposed algorithms ZO-SVRG ($b = 40$), ZO-SVRG-Coord and ZO-SVRG-Ave have faster convergence speeds (i.e., less iteration complexity) than the existing algorithms ZO-SGD and ZO-SVRC. Particularly, the use of multiple random direction samples in Avg-RandGradEst significantly accelerates ZO-SVRG since the error of order $O{({1/b})}$ is reduced to $O{({1/{({bq})}})}$ (see Table 1), leading to a non-dominant factor versus $O{({d/T})}$ in the convergence rate of ZO-SVRG-Ave. Fig. 2-(b) presents the training loss against the number of function queries. For the same experiment, Table 2 shows the number of iterations and the testing error of algorithms studied in Fig. 2-(b) using $7.3 \times 10^{6}$ function queries.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Black-box binary classification", "weight": 1.0} -->

We observe that the performance of CoordGradEst based algorithms (i.e., ZO-SVRC and ZO-SVRG-Coord) degrade due to the need of large number of function queries to construct coordinate-wise gradient estimates. By contrast, algorithms based on random gradient estimators (i.e., ZO-SGD, ZO-SVRG and ZO-SVRG-Ave) yield better both training and testing results, while ZO-SGD consumes an extremely large number of iterations ($14600$ epochs). As a result, ZO-SVRG ($b = 40$) and ZO-SVRG-Ave achieve better tradeoffs between the iteration and the function query complexity.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Generation of adversarial examples from black-box DNNs", "weight": 1.0} -->

In image classification, adversarial examples refer to carefully crafted perturbations such that, when added to the natural images, are visually imperceptible but will lead the target model to misclassify. In the setting of 'zeroth order' attacks, the model parameters are hidden and acquiring its gradient is inadmissible. Only the model evaluations are accessible. We can then regard the task of generating a universal adversarial perturbation (to $n$ natural images) as an ZO optimization problem of the form. We elaborate on the problem formulation for generating adversarial examples in Appendix A.11.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Generation of adversarial examples from black-box DNNs", "weight": 1.0} -->

We use a well-trained DNN^77^7 on the MNIST handwritten digit classification task as the target black-box model, which achieves 99.4% test accuracy on natural examples. Two ZO optimization methods, ZO-SGD and ZO-SVRG-Ave, are performed in our experiment. Note that ZO-SVRG-Ave reduces to ZO-SVRG when $q = 1$. We choose $n = 10$ images from the same class, and set the same parameters $b = 5$ and constant step size $30/d$ for both ZO methods, where $d = {28 \times 28}$ is the image dimension. For ZO-SVRG-Ave, we set $m = 10$ and vary the number of random direction samples $q \in {\{ 10,20,30\}}$. In Fig. 3, we show the black-box attack loss (against the number of epochs) as well as the least $\ell_{2}$ distortion of the successful (universal) adversarial perturbations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Generation of adversarial examples from black-box DNNs", "weight": 1.0} -->

To reach the same attack loss (e.g., $7$ in our example), ZO-SVRG-Ave requires roughly $30 \times$ ($q = 10$), $77 \times$ ($q = 20$) and $380 \times$ ($q = 30$) more function evaluations than ZO-SGD. The sharp drop of attack loss in each method could be caused by the hinge-like loss as part of the total loss function, which turns to $0$ only if the attack becomes successful. Compared to ZO-SGD, ZO-SVRG-Ave offers a faster convergence to a more accurate solution, and its convergence trajectory is more stable as $q$ becomes larger (due to the reduced variance of Avg-RandGradEst). In addition, ZO-SVRG-Ave improves the $\ell_{2}$ distortion of adversarial examples compared to ZO-SGD (e.g., $30\%$ improvement when $q = 30$). We present the corresponding adversarial examples in Appendix A.11.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we studied ZO-SVRG, a new ZO nonconvex optimization method. We presented new convergence results beyond the existing work on ZO nonconvex optimization. We show that ZO-SVRG improves the convergence rate of ZO-SGD from $O{({1/\sqrt{T}})}$ to $O{({1/T})}$ but suffers a new correction term of order $O{({1/b})}$. The is the side effect of combining a two-point random gradient estimators with SVRG. We then propose two accelerated variants of ZO-SVRG based on improved gradient estimators of reduced variances. We show an illuminating trade-off between the iteration and the function query complexity. Experimental results and theoretical analysis validate the effectiveness of our approaches compared to other state-of-the-art algorithms.
