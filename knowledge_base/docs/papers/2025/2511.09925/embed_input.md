<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Convergence of Four-Layer Matrix Factorization under Random Initialization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Gradient descent dynamics on the deep matrix factorization problem is extensively studied as a simplified theoretical model for deep neural networks. Although the convergence theory for two-layer matrix factorization is well-established, no global convergence guarantee for general deep matrix factorization under random initialization has been established to date. To address this gap, we provide a polynomial-time global convergence guarantee for randomly initialized gradient descent on four-layer matrix factorization, given certain conditions on the target matrix and a standard balanced regularization term. Our analysis employs new techniques to show saddle-avoidance properties of gradient decent dynamics, and extends previous theories to characterize the change in eigenvalues of layer weights.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

While global convergence guarantee for the case of two-layer matrix factorization ($N = 2$) is well studied (du2018algorithmicregularizationlearningdeep; ye2021globalconvergencegradientdescent; jiang2023algorithmic), the deep matrix factorization problem, ${i.e}.$, the $N > 2$ case is less explored. While the model representation power is independent of depth $N$, the deep matrix factorization problem is naturally motivated by the goal of understanding benefits of depth in deep learning (see, ${e.g}.$, arora2019implicitregularizationdeepmatrix). A long line of previous works (hardt2016identity; arora2019implicitregularizationdeepmatrix; arora2019convergenceanalysisgradientdescent; wang2023implicit) studies this regime as it directly captures Deep Linear Networks (DLN), the simplest type of deep neural networks. However, a general global convergence guarantee is still missing.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Can we prove global convergence of GD for matrix factorization problem with $N > 2$ layers?*

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we provide a positive answer to the question above. Specifically, we consider $4$-layer matrix factorization $({N = 4})$ with the standard balancing regularization term (see park2017non; ge2017spuriouslocalminimanonconvex; zheng2016convergence) as

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $W_{j}^{H}$ denotes the Hermitian transpose of $W_{j}$ and $a \in R^{+}$ is a hyperparameter. We consider both real $({{\mathbb{F}} = {\mathbb{R}}})$ and complex $({{\mathbb{F}} = {\mathbb{C}}})$ setting with random Gaussian initialization and prove global convergence of gradient descent.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Remark 1", "weight": 1.0} -->

A natural question is why the convergence guarantee in the real case holds only with probability close to $\frac{1}{2}$, but not $1$. For the other $\frac{1}{2}$ probability, Theorem 2 presents a special case - considering gradient flow under the strict balance condition (which can be viewed as the limit as $a\rightarrow{+ \infty}$), showing that the optimization process does not converge to a global minimum in finite time (and hence converges to a saddle point).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We prove global convergence of GD for $4$-layer matrix factorization under random Gaussian initialization. To the best of our knowledge, this is the first global convergence result for general deep linear networks under random initialization beyond the NTK regime in du2019width. This result helps provide new insights towards understanding the training dynamics of general deep neural networks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We construct a novel three-stage convergence analysis of gradient descent dynamics, consisting of an alignment stage, a saddle-avoidance stage, and a local convergence stage. We also develop new techniques to show GD dynamics avoids saddle points and to characterize layer matrix eigenvalue changes, which we believe are of independent interest for deep linear networks analysis.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Initialization analysis. To guarantee that gradient descent makes progress, it is necessary to establish a monotonically increasing lower bound for the singular values of the weight matrices. This, in turn, requires analyzing the smallest singular value of a newly introduced term (namely $W + {WW^{H}}$, where $W = {W_{4}W_{3}W_{2}W_{1}}$), at initialization. This analysis utilizes tools from random matrix theory, particularly the concept of Circular Ensembles. The detailed proof is given in Appendix B.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Regularity condition of each layer. To bridge the initialization with the subsequent training dynamics, we need to ensure that key matrix properties evolve in a controlled manner even during the rapid changes in the alignment stage. We prove that despite significant updates, the weight matrices retain certain spectral properties from their initial state. A delicate analysis of the smooth evolution of the extreme singular values and the limiting behavior of the Hermitian term after the regularization term converges is provided in Section 5.2.1 and 5.2.2.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Saddle avoidance. To avoid convergence to a saddle point, it is essential to prevent the smallest singular values of the weight matrices from decaying to zero, as such decay would cause the gradient norm to vanish. To this end, we construct a hermitian term providing lower-bounds for these singular values, along with a skew-hermitian error. During the optimization, the skew-hermitian error is approximately non-increasing, which in turn ensures that the minimum singular value of the hermitian term is non-decreasing. This mechanism provides a persistent lower bound, thereby effectively avoiding saddle points.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Bound of eigenvalue change. Finally, to translate the continuous-time intuition into rigorous guarantees for the discrete gradient descent algorithm, we develop new perturbation bounds for eigenvalues. In continuous time, the time derivatives of eigenvalues are directly characterized by the derivatives of the matrix. In discrete time, however, eigenvalue changes depend on the spectral gap in general, requiring a fine-grained, problem-specific analysis. Similar challenge are noted in Lemma 3.2 of ye2021globalconvergencegradientdescent. We address this issue in Lemma 29 and 30 in Appendix C.4.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1", "weight": 1.0} -->

These techniques form a cohesive proof strategy: the initialization analysis provides a favorable starting point; the regularity analysis ensures controlled dynamics throughout training; the saddle avoidance mechanism guarantees persistent progress; and the discrete-time perturbation bounds rigorously translate these insights into a full global convergence proof.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related works", "weight": 1.0} -->

For two-layer matrix factorization, the global convergence of symmetric case has been established under various settings (jain2017globalconvergencenonconvexgradient; li2019algorithmicregularizationoverparameterizedmatrix; Chen_2019). For asymmetric matrix factorization case with objective $\mathcal{L} = {\frac{1}{2}{\|{{UV^{\top}} - \Sigma}\|}_{F}^{2}}$, the following homogeneity issue occurs: the prediction result remains the same if one layer is multiplied by a positive constant while the other is divided by the same, introducing significant challenges in convergence analyzing (lee2016gradientdescentconvergesminimizers, Proposition 4.11). tu2016lowranksolutionslinearmatrix and ge2017spuriouslocalminimanonconvex tackles this problem by manually adding a regularization term on the objective function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related works", "weight": 1.0} -->

du2018algorithmicregularizationlearningdeep discovers that gradient descent automatically balances the magnitudes of layers under small initialization, providing analysis of global convergence with polynomial time under decayed learning rate, while removing the regularization term. ye2021globalconvergencegradientdescent extends the convergence analysis to constant learning rate.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related works", "weight": 1.0} -->

kawaguchi2016deeplearningpoorlocal analyzes landscape for general DLN, showing there exists saddle points with no negative eigenvalues of Hessian for depth over three. bartlett2018gradientdescentidentityinitialization analyzes the dynamic under identity initialization, proving polynomial convergence with target matrix near initialization or symmetric positive definite, but such initialization fails to converge when target matrix is symmetric and has a negative eigenvalue. arora2019convergenceanalysisgradientdescent provides global convergence proof under specific deep linear neural network structures and initialization scheme, requiring the initial loss to be smaller than the loss of any rank-deficient solution. ji2019gradientdescentalignslayers conducted the proof of convergence on general deep neural networks with similar requirements on the initial loss. arora2019implicitregularizationdeepmatrix simplifies the training dynamics of deep linear neural network into the dynamic of singular values and singular vectors of product matrix under balanced initialization, providing theoretical illustration of local convergence when singular vectors are stationary. du2019width proves global convergence for wide linear networks under the neural tangent kernel (NTK) regime.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related works", "weight": 1.0} -->

More recent works focus on GD dynamics under (approximately) balanced initialization schemes (min2023convergence) or the $2$-layer case (min2021explicit; xiong2023over; tarmoun2021understanding). chizat2024infinite studies the infinite-width limit of DLN in the mean field regime. However, none of these results imply a global convergence guarantee for general DLN with $N > 2$ under random initialization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2", "weight": 1.0} -->

As previously discussed, balance condition holds approximately under small initialization, so such regularization's affect on the training process is relatively weak, especially when weight matrices grow larger and be away from origin.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training Dynamics under Balanced Gaussian Initialization", "weight": 1.0} -->

To exhibit the convergence dynamics clearly, we present the global convergence under the simplified scenario of balanced Gaussian initialization (formally defined in Section 4.1) and gradient flow. Notice that the adjacent matrices remain balanced due to the non-increasing property of regularization term (Lemma 26).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Balanced Gaussian Initialization", "weight": 1.0} -->

Generally, random Gaussian initialization does not satisfy strict balancedness. To adapt the random Gaussian initialization to ensure balanced condition, we introduce a balanced Gaussian initialization scheme for the analysis below.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Balanced Gaussian Initialization", "weight": 1.0} -->

Intuitively, $Q_{{k,{k + 1};k} \in {{\lbrack 0,N\rbrack} \cap {\mathbb{N}}}}$ are i.i.d. uniformly distributed unitary/orthogonal matrices. By Corollary 15 in the Appendix, each matrix is a $\epsilon$-scaled Gaussian random matrix ensemble (but not independent of the others), while satisfying balanced condition ${\Delta_{j,{j + 1}}{}} = O$, ${\forall j} \in {{\lbrack 1,{N - 1}\rbrack} \cap {\mathbb{N}}^{\ast}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Non-increasing Skew-Hermitian Error", "weight": 1.0} -->

As presented in Lemma 24 in the Appendix, the product matrix can be factorized in to the form of ${W{(t)}} = {U{(t)}\Sigma_{w}{(t)}^{N}V{(t)}^{H}}$, where $\Sigma_{w}{(t)}$ is positive semi-definite and diagonal (consequently real-valued), $U$ and $V$ are unitary/orthogonal matrices, $U$, $V$ and $\Sigma_{w}$ are analytic. For simplicity, we denote $\sigma_{w,j}$ as the $j^{th}$ diagonal entry of $\Sigma_{w}$, and $u_{j}$, $v_{j}$ as the $j^{th}$ column of $U$, $V$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3", "weight": 1.0} -->

This result is under the reduction of target matrix.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Explanation of the result. This theorem provides an intrinsic non-increasing term (under initialization close to origin, this term is already small at initial) of the system. Though the result is accurately derived under strictly balanced initialization and gradient flow, one may expect similar property to hold under small initialization and gradient descent.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3", "weight": 1.0} -->

When the loss converges, each feature converges to $\sigma_{j}u_{\Sigma,j}u_{\Sigma,j}^{H}$, where $\Sigma = {\sum_{j = 1}^{d}{\sigma_{j}u_{\Sigma,j}u_{\Sigma,j}^{H}}}$ is a SVD of $\Sigma$. This shows that under initialization near origin, once a "value" of the $j^{th}$ feature increases to a relatively large value (comparing to initialization), the directions of this feature automatically align with each other (i.e. ${\langle u_{j},v_{j}\rangle} \approx 1$). Followed by Theoretical illustration part of arora2019implicitregularizationdeepmatrix, Section 3, generally the alignment of $U$, $V$ leads to convergence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3", "weight": 1.0} -->

As shown in the proof sketch, the analysis for odd $N$ encounters difficulty when generalized to the unbalanced case, thus this intrinsic non-increasing term becomes considerably more challenging to characterize. This is why we have developed the convergence proof for the four-layer case rather than the three-layer architecture.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Non-Decreasing Hermitian Main Term", "weight": 1.0} -->

This section shows the dynamics of the minimum singular value of hermitian main term ${({U + V})}\Sigma_{w}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Non-Decreasing Hermitian Main Term", "weight": 1.0} -->

Notice that the extra term in the upper bound is bounded by the skew-hermitian error term discussed in the previous section.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence under Random Gaussian Initialization", "weight": 1.0} -->

This section presents the proof sketch for Theorem 1. ‣ 1 Introduction ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization"), extending our analytical framework in the previous section to accommodate random Gaussian initialization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "random Gaussian Initialization", "weight": 1.0} -->

Specifically, we apply Gaussian distribution to generate $W_{1,2,\cdots,N} \in {\mathbb{F}}^{d \times d}$, $F = {\mathbb{R}}$ or $\mathbb{C}$ element-wisely and independently. Then the initialization is scaled by a small positive constant $\epsilon \in {\mathbb{R}}^{+}$. The scale of $\epsilon$ is determined in the main convergence Theorem 1. ‣ 1 Introduction ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization").

<!-- chunk {"id": "body-0032", "role": "body", "section": "Stage 1: Alignment Stage", "weight": 1.0} -->

During this stage, the weight matrices align with each other under the convergence of the regularization term, while the hermitian main term stays away from origin at the end of this stage.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Limit Behavior of the Hermitian main term", "weight": 1.0} -->

Typically, the dynamics of the smallest singular value of the hermitian main term $W_{1} + {W_{2}^{- 1}W_{3}^{H}W_{4}^{H}}$ is involved and does not obtain a non-trivial lower bound during this stage. However its limit behavior after the convergence of regularization term can be characterized.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Limit Behavior of the Hermitian main term", "weight": 1.0} -->

To simplify the analysis, ignore the original square loss $\mathcal{L}_{ori}$ and consider gradient flow. For $t\rightarrow{+ \infty}$, regularization term is exactly zero and thus the adjacent matrices are strictly balanced. Moreover, the product matrix does not change through the optimization: ${W{({+ \infty})}} = {W{}}$. Then under this scenario, the limit behavior of the hermitian main term is $\left. \left( {W_{1} + {W_{2}^{- 1}W_{3}^{H}W_{4}^{H}}} \right) \right|_{t\rightarrow{+ \infty}} = {\left.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Limit Behavior of the Hermitian main term", "weight": 1.0} -->

This explains the reason of studying $\sigma_{\min}\left( {{W{}} + \left( {W{}W{}^{H}} \right)^{1/2}} \right)$ in the initialization section. Detailed analysis considering error terms is presented in Corollary 53.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Note that $\sigma_{\min}\left( {W_{1} + {W_{2}^{- 1}W_{3}^{H}W_{4}^{H}}} \right)$ is not necessarily lower-bounded by the above expression minus some error terms during the alignment stage. Instead, it may exhibit oscillations or a transient decrease, achieving stability only upon convergence of the regularization term. This behavior is illustrated in Figure 4 in the Appendix.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Stage 2: Saddle Avoidance stage", "weight": 1.0} -->

Intuitively, this section focuses on generalizing Theorem 4 and 5 into unbalanced case by bounding the error terms introduced by unbalanceness.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Stage 2: Saddle Avoidance stage", "weight": 1.0} -->

The main technical challenge is to bound the operator norm of the inverse of $W_{2}$ below infinity, since both the skew-hermitian term and hermitian main term are characterized by $W_{2}^{- 1}$ and hence need to be well-defined. Under small balance error (equivalently small regularization term) which is guaranteed by the previous stage, $W_{2}^{- 1}$, which is rigorously proved in Lemma 57.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Stage 3: Local Convergence Stage", "weight": 1.0} -->

Since both the balanced error and skew-Hermitian error remain small, the minimal singular values of the weight matrices, after growing to the scale of the target matrix's, are prevented from decaying. This guarantees the local convergence.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusions, Limitations and Future work", "weight": 1.0} -->

In this work, we establish a polynomial-time global convergence guarantee for gradient descent applied to four-layer matrix decomposition, under the setting of a target matrix with identical singular values and small random Gaussian initialization beyond the NTK regime. For complex random Gaussian initialization, global convergence is ensured with high probability, whereas for real random Gaussian initialization, it is guaranteed with a probability close to $\frac{1}{2}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusions, Limitations and Future work", "weight": 1.0} -->

The analysis developed in this work reveals intrinsic properties of the training dynamics, such as the effective behavior of the regularization term, the monotonically increasing lower bound for the minimum singular value, and the non-increasing nature of the skew-Hermitian error. These findings might provide deeper insight into the training process of Deep Linear Networks.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions, Limitations and Future work", "weight": 1.0} -->

We anticipate that this work will stimulate further research on global convergence proofs under general random initialization for matrix factorization with arbitrary depth and arbitrary - possibly low-rank - target matrices.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusions, Limitations and Future work", "weight": 1.0} -->

The observed divergence in convergence behavior between real and complex initializations also reveals a subtle disparity, suggesting that complex initializations may circumvent certain saddle points that real initializations cannot. This insight might motivate more detailed analysis of the performance gap between complex and real neural networks.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reproducibility Statement", "weight": 1.0} -->

All theoretical results stated in this paper are proved in full detail in the Appendix, from Section A Target ‣ Global Convergence of Four-Layer Matrix Factorization under Random Initialization") to H, including the proofs of all main-text theorems as well as intermediate lemmas and derivations, so that a reader can verify each step independently. The numerical illustration in Appendix I, where we specify the hyper-parameters in that section. Because the experiments are straightforward, we have not released an implementation.
