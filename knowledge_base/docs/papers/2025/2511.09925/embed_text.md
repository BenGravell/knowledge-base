<!-- arxiv-full-text:v1 {"arxiv_id": "2511.09925", "source": "arxiv-html"} -->

## Introduction

This paper investigates matrix factorization, a fundamental non-convex optimization problem, which in its canonical form seeks to optimize the following objective: where $W_{j}\in\mathbb{F}^{d\times d}$ denotes the $j^{\text{th}}$ layer weight matrix, $\Sigma\in\mathbb{F}^{d\times d}$ denotes the target matrix and $\mathcal{L}_{\rm reg}$ is a (optional) regularizer. Here $\mathbb{F}\in\{\mathbb{C},\mathbb{R}\}$ as we consider both real and complex matrices in this paper. Following a long line of works (arora2019convergenceanalysisgradientdescent; jiang2023algorithmic; ye2021globalconvergencegradientdescent; chou2024gradient), we aim to understand the dynamics of gradient descent (GD) on this problem: where $\eta\in\mathbb{R}^{+}$ is the learning rate.

While global convergence guarantee for the case of two-layer matrix factorization ($N=2$) is well studied (du2018algorithmicregularizationlearningdeep; ye2021globalconvergencegradientdescent; jiang2023algorithmic), the deep matrix factorization problem, $i.e.$, the $N>2$ case is less explored. While the model representation power is independent of depth $N$, the deep matrix factorization problem is naturally motivated by the goal of understanding benefits of depth in deep learning (see, $e.g.$, arora2019implicitregularizationdeepmatrix). A long line of previous works (hardt2016identity; arora2019implicitregularizationdeepmatrix; arora2019convergenceanalysisgradientdescent; wang2023implicit) studies this regime as it directly captures Deep Linear Networks (DLN), the simplest type of deep neural networks. However, a general global convergence guarantee is still missing. Therefore, the following open research question can be naturally asked: *Can we prove global convergence of GD for matrix factorization problem with $N>2$ layers?* In this paper, we provide a positive answer to the question above. Specifically, we consider $4$-layer matrix factorization $(N=4)$ with the standard balancing regularization term (see park2017non; ge2017spuriouslocalminimanonconvex; zheng2016convergence) as where $W_{j}^{H}$ denotes the Hermitian transpose of $W_{j}$ and $a\in\mathrm{R}^{+}$ is a hyperparameter. We consider both real $(\mathbb{F}=\mathbb{R})$ and complex $(\mathbb{F}=\mathbb{C})$ setting with random Gaussian initialization and prove global convergence of gradient descent. Our main result can be summarized as follows:

### Theorem 1 (Main theorem, informal)

Consider four-layer matrix factorization under gradient descent, random Gaussian initialization with scaling factor $\epsilon\leq\sigma_{1}^{1/4}(\Sigma)/{\rm poly}(1/\delta,d)$, regularization factor $a\geq\sigma_{1}(\Sigma)\cdot{\rm poly}\left(1/\delta,d,\ln\left(\sigma_{1}^{1/4}(\Sigma)/\epsilon\right)\right)$, where $\sigma_{1}(\Sigma)$ denotes the largest singular value of target matrix $\Sigma$. Then for $\Sigma$ with identical singular values, there exists learning rate $\eta=O\left(1/\left[\sigma_{1}^{3/2}(\Sigma)\cdot{\rm poly}\left(a/\sigma_{1}(\Sigma),1/\delta,d,\sigma_{1}^{1/4}(\Sigma)/\epsilon\right)\right]\right)$ and convergence time $T(\epsilon_{\rm conv},\eta)=\eta^{-1}\sigma_{1}^{-3/2}(\Sigma)\cdot{\rm poly}\left(1/\delta,d,\sigma_{1}^{1/4}(\Sigma)/\epsilon,\ln\left(d\sigma_{1}^{2}(\Sigma)/\epsilon_{\rm conv}\right)\right)$, such that for any $\epsilon_{\rm conv}>0$, with high probability $1-\delta$ over the complex initialization, or with probability close to $\frac{1}{2}(1-\delta)$ over the real initialization, when $t>T(\epsilon_{\rm conv},\eta)$, $\mathcal{L}(t)<\epsilon_{\rm conv}$.

The formal version of Theorem 1. ‣ 1 Introduction ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization") is stated in Theorem 49 in Appendix.

### Remark 1

A natural question is why the convergence guarantee in the real case holds only with probability close to $\frac{1}{2}$, but not $1$. For the other $\frac{1}{2}$ probability, Theorem 2 presents a special case - considering gradient flow under the strict balance condition (which can be viewed as the limit as $a\to+\infty$), showing that the optimization process does not converge to a global minimum in finite time (and hence converges to a saddle point).

Main contributions. Our major contributions can summarized as follows: We prove global convergence of GD for $4$-layer matrix factorization under random Gaussian initialization. To the best of our knowledge, this is the first global convergence result for general deep linear networks under random initialization beyond the NTK regime in du2019width. This result helps provide new insights towards understanding the training dynamics of general deep neural networks.

We construct a novel three-stage convergence analysis of gradient descent dynamics, consisting of an alignment stage, a saddle-avoidance stage, and a local convergence stage. We also develop new techniques to show GD dynamics avoids saddle points and to characterize layer matrix eigenvalue changes, which we believe are of independent interest for deep linear networks analysis.

Challenges and techniques. Our analysis employs the following key techniques: Initialization analysis. To guarantee that gradient descent makes progress, it is necessary to establish a monotonically increasing lower bound for the singular values of the weight matrices. This, in turn, requires analyzing the smallest singular value of a newly introduced term (namely $W+WW^{H}$, where $W=W_{4}W_{3}W_{2}W_{1}$), at initialization. This analysis utilizes tools from random matrix theory, particularly the concept of Circular Ensembles. The detailed proof is given in Appendix B.

Regularity condition of each layer. To bridge the initialization with the subsequent training dynamics, we need to ensure that key matrix properties evolve in a controlled manner even during the rapid changes in the alignment stage. We prove that despite significant updates, the weight matrices retain certain spectral properties from their initial state. A delicate analysis of the smooth evolution of the extreme singular values and the limiting behavior of the Hermitian term after the regularization term converges is provided in Section 5.2.1 and 5.2.2.

Saddle avoidance. To avoid convergence to a saddle point, it is essential to prevent the smallest singular values of the weight matrices from decaying to zero, as such decay would cause the gradient norm to vanish. To this end, we construct a hermitian term providing lower-bounds for these singular values, along with a skew-hermitian error. During the optimization, the skew-hermitian error is approximately non-increasing, which in turn ensures that the minimum singular value of the hermitian term is non-decreasing. This mechanism provides a persistent lower bound, thereby effectively avoiding saddle points.

Bound of eigenvalue change. Finally, to translate the continuous-time intuition into rigorous guarantees for the discrete gradient descent algorithm, we develop new perturbation bounds for eigenvalues. In continuous time, the time derivatives of eigenvalues are directly characterized by the derivatives of the matrix. In discrete time, however, eigenvalue changes depend on the spectral gap in general, requiring a fine-grained, problem-specific analysis. Similar challenge are noted in Lemma 3.2 of ye2021globalconvergencegradientdescent. We address this issue in Lemma 29 and 30 in Appendix C.4.

These techniques form a cohesive proof strategy: the initialization analysis provides a favorable starting point; the regularity analysis ensures controlled dynamics throughout training; the saddle avoidance mechanism guarantees persistent progress; and the discrete-time perturbation bounds rigorously translate these insights into a full global convergence proof.

## Related works

For two-layer matrix factorization, the global convergence of symmetric case has been established under various settings (jain2017globalconvergencenonconvexgradient; li2019algorithmicregularizationoverparameterizedmatrix; Chen_2019). For asymmetric matrix factorization case with objective $\mathcal{L}=\frac{1}{2}\|UV^{\top}-\Sigma\|_{F}^{2}$, the following homogeneity issue occurs: the prediction result remains the same if one layer is multiplied by a positive constant while the other is divided by the same, introducing significant challenges in convergence analyzing (lee2016gradientdescentconvergesminimizers, Proposition 4.11). tu2016lowranksolutionslinearmatrix and ge2017spuriouslocalminimanonconvex tackles this problem by manually adding a regularization term on the objective function. du2018algorithmicregularizationlearningdeep discovers that gradient descent automatically balances the magnitudes of layers under small initialization, providing analysis of global convergence with polynomial time under decayed learning rate, while removing the regularization term. ye2021globalconvergencegradientdescent extends the convergence analysis to constant learning rate. kawaguchi2016deeplearningpoorlocal analyzes landscape for general DLN, showing there exists saddle points with no negative eigenvalues of Hessian for depth over three. bartlett2018gradientdescentidentityinitialization analyzes the dynamic under identity initialization, proving polynomial convergence with target matrix near initialization or symmetric positive definite, but such initialization fails to converge when target matrix is symmetric and has a negative eigenvalue. arora2019convergenceanalysisgradientdescent provides global convergence proof under specific deep linear neural network structures and initialization scheme, requiring the initial loss to be smaller than the loss of any rank-deficient solution. ji2019gradientdescentalignslayers conducted the proof of convergence on general deep neural networks with similar requirements on the initial loss. arora2019implicitregularizationdeepmatrix simplifies the training dynamics of deep linear neural network into the dynamic of singular values and singular vectors of product matrix under balanced initialization, providing theoretical illustration of local convergence when singular vectors are stationary. du2019width proves global convergence for wide linear networks under the neural tangent kernel (NTK) regime. More recent works focus on GD dynamics under (approximately) balanced initialization schemes (min2023convergence) or the $2$-layer case (min2021explicit; xiong2023over; tarmoun2021understanding). chizat2024infinite studies the infinite-width limit of DLN in the mean field regime. However, none of these results imply a global convergence guarantee for general DLN with $N>2$ under random initialization.

## Preliminaries

Notation. Denote the complex conjugate of $M$ as $\bar{M}$ and adjoint of $M$ as $M^{H}$, $\mathbb{N}$ as the set of non-negative integers, and $\mathbb{N}^{*}$ as the set of positive integers. For $k_{1}<k_{2}\in\mathbb{N}$, $\prod_{j=k_{2}}^{k_{1}}M_{j}=M_{k_{2}}M_{k_{2}-1}\cdots M_{k_{1}}$. $x\sim\mathcal{N}_{\mathbb{C}}$ means that the real and imaginary parts are independently sampled from Gaussian distribution with variance $\frac{1}{2}$: $\Re x,\Im x\overset{\text{i.i.d.}}{\sim}\mathcal{N}(0,1/2)$. $Q\sim U(d,\mathbb{C})$ or $O(d,\mathbb{R})$ means $Q$ is drawn from the unique uniform distribution (Haar measure) on the unitary or orthogonal group, implying its distribution is unitarily/orthogonally invariant. Consider general $N$-layer matrix factorization, for simplicity we define the following notations: $W$ is referred to as product matrix. The loss is written by $\mathcal{L}(W_{1},\cdots,W_{N})=\mathcal{L}_{\rm ori}+\mathcal{L}_{\rm reg}$, where $\mathcal{L}_{\rm ori}=\frac{1}{2}\left\|\Sigma-W\right\|_{F}^{2}$, $\mathcal{L}_{\rm reg}=\frac{1}{4}a\left(\sum_{j=1}^{N-1}\left\|\Delta_{j,j+1}\right\|_{F}^{2}\right)$.

Algorithmic setup. For the real case $(W_{j}\in\mathbb{R}^{d\times d})$, GD dynamics is canonical and described by equation 2. Under complex field $(W_{j}\in\mathbb{C}^{d\times d})$, for simplicity and coherence we define $\nabla_{M}=\frac{\partial}{\partial\Re M}+i\frac{\partial}{\partial\Im M}$, which is two times of Wirtinger derivative with $\bar{M}$: $\frac{\partial}{\partial\bar{M}}=\frac{1}{2}\left(\frac{\partial}{\partial\Re M}+i\frac{\partial}{\partial\Im M}\right)$. By following the updating rule of complex neural networks (see guberman2016complexvaluedconvolutionalneural), the gradient can be uniformly represented by | | $\displaystyle\nabla_{W_{j}}\mathcal{L}$ | $\displaystyle=\nabla_{W_{j}}\mathcal{L}_{\rm ori}+\nabla_{W_{j}}\mathcal{L}_{\rm reg}$ | | \(4\) | | | $\displaystyle\nabla_{W_{j}}\mathcal{L}_{\rm ori}$ | $\displaystyle=-W_{\prod_{L},j+1}^{H}\left(\Sigma-W\right)W_{\prod_{R},j-1}^{H},\,\nabla_{W_{j}}\mathcal{L}_{\rm reg}=-aW_{j}\Delta_{j-1,j}+a\Delta_{j,j+1}W_{j},$ | | | Under gradient flow, $\frac{\mathrm{d}W_{j}}{\mathrm{d}t}=-\nabla_{W_{j}}\mathcal{L}$; under gradient descent, $W_{j}(t+1)=W_{j}(t)-\eta\nabla_{W_{j}}\mathcal{L}(t)$.

Reduction to diagonal target. Following the simplification process of Section 2.1 in ye2021globalconvergencegradientdescent, suppose the singular value decomposition of $\Sigma$ is $\Sigma=U_{\Sigma}\Sigma^{\prime}V_{\Sigma}^{H}$, by applying the following transformation $W_{1}\leftarrow W_{1}V_{\Sigma}$ and $W_{N}\leftarrow U_{\Sigma}^{H}W_{N}$, the dynamics remain the same form, while the distributions of $W_{j}$ under our initialization schemes remain the same. Hence without loss of generality, we assume the target matrix is diagonal with real and non-negative entries throughout our analysis. Detailed analysis is presented in Appendix A Target ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization").

For some of the results, we further require target matrix to be an identity matrix scaled by a positive constant $\Sigma=\sigma_{1}(\Sigma)I$, which is equivalent to requiring the singular values of target matrix are identical.

Balancedness. Following a long line of works (arora2019convergenceanalysisgradientdescent; arora2019implicitregularizationdeepmatrix; du2018algorithmicregularizationlearningdeep), we define the balance error between layer $j$ and $j+1$ as As discussed in Definition 1 of arora2019convergenceanalysisgradientdescent, the weights are approximately balanced (namely $\|\Delta_{j,j+1}\|_{F}$ are small) throughout the iterations of gradient descent under approximate balancedness at initialization and small learning rate. Notice that approximate balancedness holds for small initialization near origin (small variance for Gaussian initialization).

Specifically, under gradient flow the balanced condition (defined as $\|\Delta_{j,j+1}\|_{F}\equiv 0$ or equivalently $\Delta_{j,j+1}\equiv O$, $\forall j\in[1,N-1]\cap\mathbb{N}^{*}$) holds strictly at arbitrary time under balanced initialization, which is defined as $\Delta_{j,j+1}(t=0)\equiv O$, $\forall j\in[1,N-1]\cap\mathbb{N}^{*}$.

### Remark 2

As previously discussed, balance condition holds approximately under small initialization, so such regularization's affect on the training process is relatively weak, especially when weight matrices grow larger and be away from origin.

## Training Dynamics under Balanced Gaussian Initialization

To exhibit the convergence dynamics clearly, we present the global convergence under the simplified scenario of balanced Gaussian initialization (formally defined in Section 4.1) and gradient flow. Notice that the adjacent matrices remain balanced due to the non-increasing property of regularization term (Lemma 26).

### Theorem 2

(Informal) Global convergence bound under balanced Gaussian initialization, gradient flow. For four-layer matrix factorization under gradient flow, balanced Gaussian initialization with scaling factor $\epsilon\leq\sigma_{1}^{1/4}(\Sigma)/{\rm poly}(1/\delta,d)$, then for target matrix with identical singular values, 1\. For $\mathbb{F}=\mathbb{R}$, with probability at least $\frac{1}{2}$ the loss does not converge to zero.

2\. For $\mathbb{F}=\mathbb{C}$ with high probability at least $1-\delta$ and for $\mathbb{F}=\mathbb{R}$ with probability at least $\frac{1}{2}(1-\delta)$, there exists $T(\epsilon_{\rm conv})=\sigma_{1}^{-3/2}(\Sigma)\cdot{\rm poly}\left(1/\delta,d,\sigma_{1}^{1/4}(\Sigma)/\epsilon,\ln\left(d\sigma_{1}^{2}(\Sigma)/\epsilon_{\rm conv}\right)\right)$, such that for any $\epsilon_{\rm conv}>0$, when $t>T(\epsilon_{\rm conv})$, $\mathcal{L}(t)<\epsilon_{\rm conv}$.

The formal version is stated in Theorem 37 in the Appendix.

### Balanced Gaussian Initialization

Generally, random Gaussian initialization does not satisfy strict balancedness. To adapt the random Gaussian initialization to ensure balanced condition, we introduce a balanced Gaussian initialization scheme for the analysis below. The procedure is defined as follows: \(1\) Sample $G$ with entries $G_{ij}\overset{\text{i.i.d.}}{\sim}\mathcal{N}_{\mathbb{F}}$, $Q_{k,k+1;k\in[0,N]\cap\mathbb{N}}\overset{\text{i.i.d.}}{\sim}\mathrm{Haar}$ on $U(d,\mathbb{C})$ for $\mathbb{F}=\mathbb{C}$ (or $O(d,\mathbb{R})$ for $\mathbb{F}=\mathbb{R}$). $s_{j,j\in[1,N]\cap\mathbb{N}^{*}}\in\mathbb{F}$ are arbitrary constants with modulus/absolute value $1$.

\(2\) For scaling factor $\epsilon\in\mathbb{R}^{+}$, which is a small positive constant, set the weight matrices: Intuitively, $Q_{k,k+1;k\in[0,N]\cap\mathbb{N}}$ are i.i.d. uniformly distributed unitary/orthogonal matrices. By Corollary 15 in the Appendix, each matrix is a $\epsilon$-scaled Gaussian random matrix ensemble (but not independent of the others), while satisfying balanced condition $\Delta_{j,j+1}=O$, $\forall j\in[1,N-1]\cap\mathbb{N}^{*}$.

### Theorem 3

Under $\epsilon$-scaled balanced Gaussian initialization with even number of depth $2\mid N$, suppose $W$ is $W=U\Sigma_{w}^{N}V^{H}$, where $U$, $V$ are unitary/orthogonal matrices, $\Sigma_{w}$ is positive semi-definite and diagonal, denote $s\coloneqq\prod_{j=1}^{N}s_{j}$, then for some $f_{1}=O\left(\frac{1}{\delta}\right)$, $f_{2}^{\prime}=O\left(\frac{1}{\delta^{2}}\right)$: 1\. If $\mathbb{F}=\mathbb{C}$, with probability $1-\delta$ such that | | $\displaystyle\|\Sigma_{w}\|_{op}\leq f_{1}(\delta)\sqrt{d}\epsilon$ | $\displaystyle,\,\|(U-V)\Sigma_{w}\|_{F}|_{t=0}\leq 2f_{1}(\delta)d\epsilon$ | | \(7\) | | | $\displaystyle\sigma_{\min}((U+V)\Sigma_{w})|_{t=0}$ | $\displaystyle\geq f_{2}^{\prime}(\delta)^{-1}d^{-3/2}\epsilon.$ | | | 2\. If $\mathbb{F}=\mathbb{R}$, $\Pr(s\det(Q_{N,N+1})\det(Q_{01})=1)=\Pr(s\det(Q_{N,N+1})\det(Q_{01})=-1)=\frac{1}{2}$. Under $\Pr(s\det(Q_{N,N+1})\det(Q_{01})=-1)$, $\sigma_{\min}((U+V)\Sigma_{w})|_{t=0}$; under $\Pr(s\det(Q_{N,N+1})\det(Q_{01})=1)$, with probability $1-\delta$ such that | | $\displaystyle\|\Sigma_{w}\|_{op}\leq f_{1}(\delta)\sqrt{d}\epsilon$ | $\displaystyle,\,\|(U-V)\Sigma_{w}\|_{F}|_{t=0}\leq 2f_{1}(\delta)d\epsilon$ | | \(8\) | | | $\displaystyle\sigma_{\min}((U+V)\Sigma_{w})|_{t=0}$ | $\displaystyle\geq f_{2}^{\prime}(\delta)^{-1}d^{-3/2}\epsilon.$ | | | Proof is presented in Appendix B.3.

### Non-increasing Skew-Hermitian Error

As presented in Lemma 24 in the Appendix, the product matrix can be factorized in to the form of $W(t)=U(t)\Sigma_{w}(t)^{N}V(t)^{H}$, where $\Sigma_{w}(t)$ is positive semi-definite and diagonal (consequently real-valued), $U$ and $V$ are unitary/orthogonal matrices, $U$, $V$ and $\Sigma_{w}$ are analytic. For simplicity, we denote $\sigma_{w,j}$ as the $j^{th}$ diagonal entry of $\Sigma_{w}$, and $u_{j}$, $v_{j}$ as the $j^{th}$ column of $U$, $V$. Under this representation of product matrix, we obtain a non-increasing skew-hermitian/symmetric term:

### Theorem 4

(Informal) Skew-hermitian error term is non-increasing.

Under balanced initialization with product matrix $W(t)=U(t)\Sigma_{w}(t)^{N}V(t)^{H}$, for depth $N\geq 2$, if the singular values of the product matrix at initial $W$ are non-zero and distinct, then the following skew-hermitian error $\left\|\Sigma^{1/2}(U-V)\Sigma_{w}\right\|_{F}^{2}$ is non-increasing: Proof sketch. Proof of the Theorem 4 involves technical and lengthy calculations. The formal version is stated in Theorem 33, while a special version for even $N$ is separately discussed in Theorem 34. For the proof of Theorem 33, the idea is to decompose the derivative of this term into the derivative of $\sigma_{w,j}$ and $u_{j}$, $v_{j}$, which have been characterized by Theorem 3 and Lemma 2 in arora2019implicitregularizationdeepmatrix respectively. This method is hard to generalize into unbalanced setting. For Theorem 34, this term is directly derived from derivative of $W_{N}W_{N}^{H}$, $W_{1}^{H}W_{1}$ and $W$. This approach is straight forward and can be extended to unbalanced initialization, but encounters difficulty under odd depth $2\nmid N$.

### Remark 3

This result is under the reduction of target matrix. For general target matrix, suppose its SVD is $\Sigma=U_{\Sigma}\Sigma^{\prime}V_{\Sigma}^{H}$, then Theorem 4 becomes: Explanation of the result. This theorem provides an intrinsic non-increasing term (under initialization close to origin, this term is already small at initial) of the system. Though the result is accurately derived under strictly balanced initialization and gradient flow, one may expect similar property to hold under small initialization and gradient descent.

Moreover, this theorem characterizes when $U$ and $V$ become aligned. The product matrix can be expressed as $W=\sum_{i=1}^{d}\sigma_{w,j}^{N}u_{j}v_{j}^{H}$, while the error can be rewritten as $\sum_{j=1}^{d}\sigma_{w,j}^{2}\left\|\Sigma^{1/2}(u_{j}-v_{j})\right\|_{F}^{2}$. Each term $\sigma_{w,j}^{N}u_{j}v_{j}^{H}$ of the product matrix can be interpreted as a "feature" of the linear neural network, containing one "value" $\sigma_{w,j}^{N}$ and two "directions" $u_{j}$, $v_{j}$. When the loss converges, each feature converges to $\sigma_{j}u_{\Sigma,j}u_{\Sigma,j}^{H}$, where $\Sigma=\sum_{j=1}^{d}\sigma_{j}u_{\Sigma,j}u_{\Sigma,j}^{H}$ is a SVD of $\Sigma$. This shows that under initialization near origin, once a "value" of the $j^{th}$ feature increases to a relatively large value (comparing to initialization), the directions of this feature automatically align with each other (i.e. $\langle u_{j},v_{j}\rangle\approx 1$). Followed by Theoretical illustration part of arora2019implicitregularizationdeepmatrix, Section 3, generally the alignment of $U$, $V$ leads to convergence.

As shown in the proof sketch, the analysis for odd $N$ encounters difficulty when generalized to the unbalanced case, thus this intrinsic non-increasing term becomes considerably more challenging to characterize. This is why we have developed the convergence proof for the four-layer case rather than the three-layer architecture.

### Non-Decreasing Hermitian Main Term

This section shows the dynamics of the minimum singular value of hermitian main term $(U+V)\Sigma_{w}$.

The motivation of studying this specific term is that it provides a bound for $\sigma_{k}(\Sigma_{w})$, $k\in[1,N-1]\cap\mathbb{N}^{*}$, especially a tight bound for $\sigma_{\min}(\Sigma_{w})$ (refer to Lemma 20): | | $\displaystyle\frac{1}{2}\sigma_{k}\left((U+V)\Sigma_{w}\right)$ | $\displaystyle\leq\sigma_{k}(\Sigma_{w})\leq\frac{\sqrt{2}}{2}\sqrt{\sigma_{k}^{2}\left((U+V)\Sigma_{w}\right)+\left\|\left(U-V\right)\Sigma_{w}\right\|_{op}^{2}}$ | | \(11\) | | | $\displaystyle\frac{1}{2}\sigma_{\min}\left((U+V)\Sigma_{w}\right)$ | $\displaystyle\leq\sigma_{\min}(\Sigma_{w})\leq\frac{1}{2}\sqrt{\sigma_{\min}^{2}\left((U+V)\Sigma_{w}\right)+\left\|\left(U-V\right)\Sigma_{w}\right\|_{op}^{2}}.$ | | | Notice that the extra term in the upper bound is bounded by the skew-hermitian error term discussed in the previous section.

Although the evolution of $\sigma_{k}((U+V)\Sigma_{w})$ is generally difficult to characterize, we find that in the special case of $\Sigma=\sigma_{1}(\Sigma)I$ and $N=4$, it exhibits a monotonically increasing pattern before local convergence:

### Theorem 5

Dynamics of minimum singular value of hermitian term.

Under balanced initialization with product matrix $W(t)=U(t)\Sigma_{w}(t)^{N}V(t)^{H}$, for target matrix with identical singular values (reduces to $\Sigma=\sigma_{1}(\Sigma)I$) and depth $N=4$, the time derivative of the $k^{th}$ singular value of the hermitian term $x_{k}\coloneqq\frac{1}{2}\sigma_{k}((U+V)\Sigma_{w})$ is bounded: | | $\displaystyle\leq\frac{\mathrm{d}}{\mathrm{d}t}x_{k}^{2}\leq\sigma_{1}(\Sigma)\left(2\|\Sigma_{w}\|_{op}^{2}+\|((U-V)\Sigma_{w})|_{t=0}\|_{F}^{2}\right)x_{k}^{2}.$ | | | Detailed proof is presented in D.2.

This theorem implies that under small initialization, if all singular values $\sigma_{k}((U+V)\Sigma_{w})$ are initially non-zero, they increase monotonically to relatively large values, leading to subsequent local convergence. However, if any singular value is initialized to zero (which occurs with probability at least $1/2$ for $\mathbb{F}=\mathbb{R}$, as shown in Theorem 3), it remains zero throughout the optimization (see Corollary 36), thereby explaining the $1/2$ convergence probability in Theorem 2. Numerical simulations under the identity target setting are provided in Figure 1, with additional results and discussions for non-identity targets shown in Figure 2.

## Convergence under Random Gaussian Initialization

This section presents the proof sketch for Theorem 1. ‣ 1 Introduction ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization"), extending our analytical framework in the previous section to accommodate random Gaussian initialization.

For random Gaussian Initialization with balance regularization term, the balanced condition holds approximately. Following the methodology in balanced initialization scheme, Section 4, we then characterize the skew-hermitian error term and hermitian main term by $\|W_{1}-W_{2}^{-1}W_{3}^{H}W_{4}^{H}\|_{F}^{2}$ and $\lambda_{\min}\left(\left(W_{1}+W_{2}^{-1}W_{3}^{H}W_{4}^{H}\right)^{H}\left(W_{1}+W_{2}^{-1}W_{3}^{H}W_{4}^{H}\right)\right)$ respectively.

### random Gaussian Initialization

We consider the canonical setting of random Gaussian initialization near origin: Specifically, we apply Gaussian distribution to generate $W_{1,2,\cdots,N}\in\mathbb{F}^{d\times d}$, $F=\mathbb{R}$ or $\mathbb{C}$ element-wisely and independently. Then the initialization is scaled by a small positive constant $\epsilon\in\mathbb{R}^{+}$. The scale of $\epsilon$ is determined in the main convergence Theorem 1. ‣ 1 Introduction ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization").

### Theorem 6

For $\epsilon$-scaled random Gaussian initialization on $W_{k,k=[1,N]\cap\mathbb{N}^{*}}$ over $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$, $N\in\mathbb{N}^{*}$, the initial product matrix $W=\prod_{k=N}^{1}W_{k}$ satisfy the following properties: 1\. If $\mathbb{F}=\mathbb{C}$, with probability at least $1-\delta$, | | $\displaystyle\max_{j,k}\sigma_{k}(W_{j})\leq f_{1}(\delta,N)\sqrt{d}\epsilon$ | $\displaystyle,\,\min_{j,k}\sigma_{k}(W_{j})\leq\frac{\epsilon}{f_{1}(\delta,N)\sqrt{d}}$ | | \(14\) | | | $\displaystyle\sigma_{\min}\left(W+\left(WW^{H}\right)^{1/2}\right)$ | $\displaystyle\geq f_{2}(\delta,N)^{-1}\cdot d^{-(N/2+1)}\epsilon^{N}.$ | | | 2\. If $\mathbb{F}=\mathbb{R}$, the determinants $\det(W)>0$ and $\det(W)<0$ occur each with probability $1/2$. If $\det(W)<0$, then $\sigma_{\min}\left(W+\left(WW^{\top}\right)^{1/2}\right)=0$; if $\det(W)>0$, then with conditional probability at least $1-\delta$, | | $\displaystyle\max_{j,k}\sigma_{k}(W_{j})\leq f_{1}(\delta,N)\sqrt{d}\epsilon$ | $\displaystyle,\,\min_{j,k}\sigma_{k}(W_{j})\leq\frac{\epsilon}{f_{1}(\delta,N)\sqrt{d}}$ | | \(15\) | | | $\displaystyle\sigma_{\min}\left(W+\left(WW^{\top}\right)^{1/2}\right)$ | $\displaystyle\geq f_{2}(\delta,N)^{-1}\cdot d^{-(N/2+1)}\epsilon^{N},$ | | | where $f_{1}(\delta,N)=O\left(\frac{N}{\delta}\right)$, $f_{2}(\delta,N)=O\left(\frac{N^{N}}{\delta^{N+1}}\right)$.

Proof is provided in Appendix B.2. For $N=4$, $f_{1}=O\left(\frac{1}{\delta}\right)$, $f_{2}=O\left(\frac{1}{\delta^{5}}\right)$.

In the convergence proof below, we consider the initialization where and holds. We divide the training dynamics into three stages consisting of an alignment stage $t\in[0,T_{1}]$, a saddle-avoidance stage $t\in[T_{1},T_{1}+T_{2}]$, and a local convergence stage $t\inT_{2},+\infty)$, to analyze the convergence process clearly. Here $T_{1}=O\left(\frac{1}{\eta\sigma_{1}^{3/2}(\Sigma)\cdot{\rm poly}\left(f_{1},f_{2},d,\epsilon/\sigma_{1}^{1/4}(\Sigma)\right)}\right)$, $T_{2}=O\left(\frac{1}{\eta\sigma_{1}^{3/2}(\Sigma)}\cdot{\rm poly}\left(f_{1},f_{2},d,\sigma_{1}^{1/4}/\epsilon\right)\right)$, refer to Theorem [50 and 54 respectively.

### Stage 1: Alignment Stage

During this stage, the weight matrices align with each other under the convergence of the regularization term, while the hermitian main term stays away from origin at the end of this stage.

### Convergence of Regularization term

The convergence rate of the regularization term is related to the smallest singular value of weight matrices:

### Theorem 7

(Informal) Convergence rate of the regularization term.

For four-layer matrix factorization, suppose the maximum and minimum singular values of the weight matrices are bounded by $M$ and $\delta$ respectively, then the regularization term decays by The formal version can be found in Theorem 31. A $N$-layer version of this Theorem, along with a generalized loss function under gradient flow is provided in Theorem 27. This shows the importance of bounding the extreme singular values of $W_{j}$, otherwise the linear convergence of the regularization term (along with the balancedness) might not be guaranteed.

### Theorem 8

(Informal) Under a small learning rate, the change in the maximum and minimum singular values is approximately independent of the regularization term: | | $\displaystyle\max_{j,k}\sigma_{k}^{2}(W_{j}(t+1))-\max_{j,k}\sigma_{k}^{2}(W_{j}(t))$ | $\displaystyle\leq 2\eta\max_{j,k}\sigma_{k}(W_{j}(t))\max_{j}\left\|\nabla_{W_{j}}\mathcal{L}_{\rm ori}(t)\right\|_{op}+O(\eta^{2}a^{2})$ | | \(17\) | | | $\displaystyle\min_{j,k}\sigma_{k}^{2}(W_{j}(t+1))-\min_{j,k}\sigma_{k}^{2}(W_{j}(t))$ | $\displaystyle\geq-2\eta\min_{j,k}\sigma_{k}(W_{j}(t))\max_{j}\left\|\nabla_{W_{j}}\mathcal{L}_{\rm ori}(t)\right\|_{op}+O(\eta^{2}a^{2}).$ | | | Here $a$ is the coefficient of the regularization term.

This Theorem ensures the smooth change of the extreme singular values over short time intervals. Although the regularization term can induce significant fluctuations in individual singular values due to its potentially large coefficient, the largest and smallest singular values remain stable. This theoretical conclusion is corroborated by numerical simulations, as shown in Figure 3. The complete formal statement can be found in Theorem 32 (and Theorem 28 for the continuous-time case) in the Appendix.

### The Limit Behavior of the Hermitian main term

Typically, the dynamics of the smallest singular value of the hermitian main term $W_{1}+W_{2}^{-1}W_{3}^{H}W_{4}^{H}$ is involved and does not obtain a non-trivial lower bound during this stage. However its limit behavior after the convergence of regularization term can be characterized.

To simplify the analysis, ignore the original square loss $\mathcal{L}_{\rm ori}$ and consider gradient flow. For $t\to+\infty$, regularization term is exactly zero and thus the adjacent matrices are strictly balanced. Moreover, the product matrix does not change through the optimization: $W(+\infty)=W$. Then under this scenario, the limit behavior of the hermitian main term is $\left.\left(W_{1}+W_{2}^{-1}W_{3}^{H}W_{4}^{H}\right)\right|_{t\to+\infty}=\left.\left(W_{2}^{-1}W_{3}^{-1}W_{4}^{-1}\right)\right|_{t\to+\infty}\left(W+\left(WW^{H}\right)^{1/2}\right)$.

This explains the reason of studying $\sigma_{\min}\left(W+\left(WW^{H}\right)^{1/2}\right)$ in the initialization section. Detailed analysis considering error terms is presented in Corollary 53.

### Remark 4

Note that $\sigma_{\min}\left(W_{1}+W_{2}^{-1}W_{3}^{H}W_{4}^{H}\right)$ is not necessarily lower-bounded by the above expression minus some error terms during the alignment stage. Instead, it may exhibit oscillations or a transient decrease, achieving stability only upon convergence of the regularization term. This behavior is illustrated in Figure 4 in the Appendix.

### Stage 2: Saddle Avoidance stage

Intuitively, this section focuses on generalizing Theorem 4 and 5 into unbalanced case by bounding the error terms introduced by unbalanceness.

The main technical challenge is to bound the operator norm of the inverse of $W_{2}$ below infinity, since both the skew-hermitian term and hermitian main term are characterized by $W_{2}^{-1}$ and hence need to be well-defined. Under small balance error (equivalently small regularization term) which is guaranteed by the previous stage, $W_{2}^{-1}$, which is rigorously proved in Lemma 57.

### Lemma 9

Skew-hermitian error in saddle avoidance stage, gradient descent. For $t\in[T_{1},T_{1}+T_{2}]$,

### Lemma 10

The minimum eigenvalue of Hermitian term. For $t=T_{1}+T_{2}$, Proofs are presented in H.2 in the Appendix.

### Stage 3: Local Convergence Stage

Since both the balanced error and skew-Hermitian error remain small, the minimal singular values of the weight matrices, after growing to the scale of the target matrix's, are prevented from decaying. This guarantees the local convergence.

### Theorem 11

(Informal) Local convergence. After the second stage ($t\geq T_{1}+T_{2}$), | | $\displaystyle\mathcal{L}(t)\leq\mathcal{L}_{\rm ori}(T_{1}+T_{2})\exp\left(-\eta\sigma_{1}^{3/2}(\Sigma)(t-T_{1}-T_{2})\right)$ | | \(20\) | | | $\displaystyle\sigma_{\min}\left(W_{1}(t)+W_{2}(t)^{-1}W_{3}(t)^{H}W_{4}(t)^{H}\right)\geq 2^{3/4}\sigma_{1}^{1/4}(\Sigma)$ | | | | | $\displaystyle\left\|W_{1}(t)-W_{2}(t)^{-1}W_{3}(t)^{H}W_{4}(t)^{H}\right\|_{F}\leq 3f_{1}d\epsilon.$ | | | Proof is presented in H.3 in the Appendix.

## Conclusions, Limitations and Future work

In this work, we establish a polynomial-time global convergence guarantee for gradient descent applied to four-layer matrix decomposition, under the setting of a target matrix with identical singular values and small random Gaussian initialization beyond the NTK regime. For complex random Gaussian initialization, global convergence is ensured with high probability, whereas for real random Gaussian initialization, it is guaranteed with a probability close to $\frac{1}{2}$.

The analysis developed in this work reveals intrinsic properties of the training dynamics, such as the effective behavior of the regularization term, the monotonically increasing lower bound for the minimum singular value, and the non-increasing nature of the skew-Hermitian error. These findings might provide deeper insight into the training process of Deep Linear Networks.

We anticipate that this work will stimulate further research on global convergence proofs under general random initialization for matrix factorization with arbitrary depth and arbitrary - possibly low-rank - target matrices.

The observed divergence in convergence behavior between real and complex initializations also reveals a subtle disparity, suggesting that complex initializations may circumvent certain saddle points that real initializations cannot. This insight might motivate more detailed analysis of the performance gap between complex and real neural networks.

## Reproducibility Statement

All theoretical results stated in this paper are proved in full detail in the Appendix, from Section A Target ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization") to H, including the proofs of all main-text theorems as well as intermediate lemmas and derivations, so that a reader can verify each step independently. The numerical illustration in Appendix I, where we specify the hyper-parameters in that section. Because the experiments are straightforward, we have not released an implementation.
