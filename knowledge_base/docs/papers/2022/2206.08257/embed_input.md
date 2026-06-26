<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient Descent for Low-Rank Functions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Several recent empirical studies demonstrate that important machine learning tasks, e.g., training deep neural networks, exhibit low-rank structure, where the loss function varies significantly in only a few directions of the input space. In this paper, we leverage such low-rank structure to reduce the high computational cost of canonical gradient-based methods such as gradient descent (GD). Our proposed Low-Rank Gradient Descent (LRGD) algorithm finds an epsilon-approximate stationary point of a p-dimensional function by first identifying r <= p significant directions, and then estimating the true p-dimensional gradient at every iteration by computing directional derivatives only along those r directions. We establish that the "directional oracle complexities" of LRGD for strongly convex and non-convex objective functions are O(r log(1/epsilon) + rp) and O(r/epsilon^ + rp), respectively. When r ll p, these complexities are smaller than the known complexities of O(p log(1/epsilon)) and O(p/epsilon^) of {\gd} in the strongly convex and non-convex settings, respectively.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Thus, LRGD significantly reduces the computational cost of gradient-based methods for sufficiently low-rank functions. In the course of our analysis, we also formally define and characterize the classes of exact and approximately low-rank functions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

First order optimization methods such as Gradient Descent (GD) and its variants have become the cornerstone of training modern machine learning models. Hence, reducing the running times of first order methods has been an important problem in the optimization literature, cf.. The running times of GD methods is known to grow linearly with the dimension of the model parameters, which can be very large, e.g., in deep neural networks. However, it has recently been observed that many empirical risk minimization problems have objective functions (i.e., real-valued losses) with *low-rank structure* in their gradients. In what follows, we will refer to such objects as low-rank functions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Roughly speaking, a low-rank function is a differentiable real-valued function whose gradients live *close* to a low-dimensional subspace. Such low-rank structure has been exploited to theoretically improve the running times of federated optimization algorithms. Yet, canonical GD methods do not exploit this additional structure. Hence, the goal of this work is to address the following question: We consider solving the optimization problem ${\min_{\theta \in {\mathbb{R}}^{p}}f}{(\theta)}$, with objective function $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}}$, using gradient-based methods. In particular, we characterize the computational cost of an iterative routine to solve this minimization problem, namely *oracle complexity*, as the number of evaluations of *directional derivatives* of $f$ to achieve a certain accuracy level $\epsilon > 0$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under this definition, the vanilla GD algorithm requires an oracle complexity of $\mathcal{O}{({p{\log{({1/\epsilon})}}})}$ to find an $\epsilon$-minimizer of a strongly convex objective $f$, which grows linearly with parameter dimension $p$. Note that each iteration of GD costs $p$ directional derivatives as it requires a full gradient computation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To ameliorate the oracle complexity of such methods, we propose to leverage the existing low-rank structure in the objective. As briefly pointed out above, low-rank functions demonstrate significant variation in only a few directions of the parameter space, e.g., in $r$ directions where $r \ll p$. As a result, its gradient vectors live entirely (or approximately) in a low-dimensional subspace. To minimize such low-rank objective functions, we restrict the function to the low-rank subspace defined by the significant directions -- the *active subspace* -- and perform descent iterations only along these directions. This is the main idea behind our proposed method *Low-Rank Gradient Descent* (LRGD). More precisely, LRGD first identifies a fairly accurate proxy for the active subspace. Then, in each descent iteration, it approximates the true gradient vector on the current iterate by computing only $r$ directional derivatives of the objective along the active subspace. This approximate gradient is then used to update the model parameters. Note that each iteration of LRGD costs only $r$ directional derivative computations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intuitively, this is far less than canonical methods such as GD, which has iteration cost growing linearly with $p$, as noted earlier.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Low-rank structures have been observed in several contexts which further highlights the potential utility of the proposed LRGD method. We briefly describe some such motivating examples below.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivation 1: Low-rank Hessians. Low-rank structures have been found in large-scale deep learning scenarios irrespective of the architecture, training methods, and tasks, where the Hessians exhibit a sharp decay in their eigenvalues. For instance, in classification tasks with $k$ classes, during the course of training a deep neural network model, the gradient lives in the subspace spanned by the $k$ eigenvectors of the Hessian matrix with largest eigenvalues. As another example, empirically demonstrates that some layers of a deep neural network model (VGG-19) trained on the CIFAR-10 dataset shows *exponential* decay in the eigenvalues of the gradient covariance matrix. These practical scenarios further suggest that the LRGD method may be able to leverage such low-rank structures to mitigate training computation cost. This connection is further detailed in Appendix F. Furthermore, a simple simulation based on the the MNIST database that illustrates low-rank structure in gradients of neural networks is provided in Appendix G.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivation 2: Relation to line search. Line search is an iterative strategy to find the optimum stepsize in GD-type methods. More precisely, given a current position $\theta$, the line search algorithm minimizes the objective $f$ restricted to the rank-$1$ subspace (i.e., a line) passing through $\theta$ in the direction of ${\nabla f}{(\theta)}$, that is, $\theta\leftarrow{{\underset{\theta' \in {\{{\theta + {\alpha{\nabla f}{(\theta)}}}:{\alpha \in {\mathbb{R}}}\}}}{\arg\min}f}{(\theta')}}$. Now consider a similar search problem where the objective $f$ is to be minimized restricted to a rank-$r$ subspace rather than a line. We refer to this subspace search method as *iterated LRGD* (see Algorithm 2).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed LRGD method can be viewed as solving the intermediate minimization problems in such subspace search.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivation 3: Ridge functions. Ridge functions are generally defined as functions that only vary on a given low-dimensional subspace of the ambient space. There are many standard examples of ridge function losses in machine learning, e.g., least-squares regression, logistic regression, one hidden layer neural networks, etc.. Moreover, they have been exploited in the development of projection pursuit methods in statistics, cf. and the references therein. In the next section we will show that the LRGD method is particularly well-suited for optimization of such functions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivation 4: Constrained optimization. The general idea of solving an optimization problem on a smaller dimensional subspace is connected to *constrained optimization*. In fact, one of the primary steps of LRGD can be perceived as *learning* (through sampling) "hidden" linear constraints under which it is efficient to solve an a priori unconstrained optimization problem. Classically, when such constraints are known, e.g., when optimizing $f{(\theta)}$ under a constraint of the form ${A\theta} = b$, a change-of-variables allows us to reduce the dimension of the optimization problem.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Main contributions. We next list our main contributions: Table 1: Oracle complexities for both exactly and approximately low-rank settings. (The difference between these settings is in constants that are hidden by the 𝒪 notation.)

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We identify the class of low-rank functions and propose LRGD in Algorithm 1 to mitigate gradient computation cost of GD-type methods to minimize such objectives.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide theoretical guarantees for the proposed LRGD method and characterize its oracle complexity in optimizing both exactly and approximately low-rank strongly convex and non-convex functions in Theorems 3.1. ‣ 3.2 Oracle complexity analysis for strongly convex setting ‣ 3 Algorithms and theoretical guarantees ‣ Gradient Descent for Low-Rank Functions"), 3.2. ‣ 3.2 Oracle complexity analysis for strongly convex setting ‣ 3 Algorithms and theoretical guarantees ‣ Gradient Descent for Low-Rank Functions"), 3.3. ‣ 3.3 Oracle complexity analysis for non-convex setting ‣ 3 Algorithms and theoretical guarantees ‣ Gradient Descent for Low-Rank Functions"), and 3.4. ‣ 3.3 Oracle complexity analysis for non-convex setting ‣ 3 Algorithms and theoretical guarantees ‣ Gradient Descent for Low-Rank Functions"). As demonstrated in Table 1, for low-rank objectives (with sufficient approximation accuracy), LRGD is able to reduce the dependency of the dominant term in GD from $p$ to $r$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive several auxiliary results characterizing exactly and approximately low-rank functions, e.g., Propositions 2.1. ‣ 2.2 Exactly low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions"), 2.3. ‣ 2.3 Approximately low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions"), and C.1. ‣ C.1 Algebra of low-rank functions ‣ Appendix C Calculus of low-rank functions ‣ Gradient Descent for Low-Rank Functions").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose several algorithms that can optimize general (possibly high-rank) functions using LRGD as a building block, e.g., *iterated LRGD* (Algorithm 2) and *adaptive LRGD* (Algorithm 3). While LRGD is provably efficient on (approximately) low-rank functions, its variants are *applicable to broader classes of functions that may not possess low-rank structure* on the full space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate the performance of LRGD on different objectives and demonstrate its usefulness in restricted but insightful setups.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work. Low-rank structures have been exploited extensively in various disciplines. For example, in machine learning, matrix estimation (or completion) methods typically rely on low-rank assumptions to recover missing entries. In classical statistics, projection pursuit methods rely on approximating functions using ridge functions, which are precisely low-rank functions (see Proposition 2.1. ‣ 2.2 Exactly low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions")). In a similar vein, in scientific computing, approximation methods have been developed to identify influential input directions of a function for uncertainty quantification.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to these settings, we seek to exploit low-rank structure in optimization algorithms. Recently, the authors of developed a local polynomial interpolation based GD algorithm for empirical risk minimization that learns gradients at every iteration using smoothness of loss functions in data. The work in extended these developments to a federated learning context (cf., and the references therein), where low-rank matrix estimation ideas were used to exploit such smoothness of loss functions. Following this line of reasoning, this paper utilizes the structure of low-rank objective functions to improve iterative gradient-based algorithms in the canonical optimization setting. (In a very different direction, low-rank structure has also been used to solve semidefinite programs.)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several works have recently highlighted different forms of low-rank structure in large-scale training problems. For example, deep neural networks seem to have loss functions with low-rank Hessians, which partly motivates our work here (also see Appendix G). Moreover, deep neural networks have been shown to exhibit low-rank weight matrices and neural collapse, and low-rank approximations of gradient weight matrices have been used for their training.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work falls within the broader effort of speeding up first order optimization algorithms, which has been widely studied in the literature. In this literature, the running time is measured using first order oracle complexity (i.e., the number of full gradient evaluations until convergence). The first order oracle complexity of GD, e.g., strongly convex functions, is analyzed in the standard text. Similar analyses for stochastic versions of GD that are popular in large-scale empirical risk minimization problems, such as (mini-batch) stochastic GD, can be found. There are several standard approaches to theoretically or practically improving the running times of these basic algorithms, e.g., momentum, acceleration, variance reduction, and adaptive learning rates. More related to our problem, random coordinate descent-type methods such as stochastic subspace descent have been studied. In addition, various other results pertaining to GD with inexact oracles (see and the references therein), fundamental lower bounds on oracle complexity, etc. have also been established in the literature. We refer readers to the surveys in for details and related references.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions in this paper are complementary to the aforementioned approaches to speed up first order optimization methods, which do not use low-rank structure in objective functions. Indeed, ideas like acceleration, variance reduction, and adaptive learning rates could potentially be used in conjunction with our proposed LRGD algorithm, although we leave such developments for future work. Furthermore, we only consider GD-like methods rather than more prevalent stochastic GD methods in this work, because our current focus is to show simple theoretical improvements in running time by exploiting low-rank structure. Hence, we also leave the development of stochastic optimization algorithms that exploit low-rank structure for future work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outline. We briefly outline the remainder of the paper. We state our assumptions, the computational model, and definitions of low-rank functions in Section 2. We describe the LRGD algorithm and its theoretical guarantees in Section 3. Finally, illustrative simulations are given in Section 4.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2.1 ($L$-smoothness)", "weight": 1.0} -->

Non-convex setting. Under no further assumption on the function $f$, the general goal we will pursue is to find an $\epsilon$-stationary point, that is, for a given accuracy $\epsilon$, we aim to find $\theta \in \Theta$ such that, Note that a solution to exists as soon as $f$ is lower-bounded by some $f^{\ast} = {\inf_{\theta \in \Theta}{f{(\theta)}}} \in {\mathbb{R}}$ which is assumed throughout this paper.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2.1 ($L$-smoothness)", "weight": 1.0} -->

Strongly convex setting. We also study a similar problem under the additional assumption that $f$ is strongly convex.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2.2 (Strong convexity)", "weight": 1.0} -->

Under this particular setting, a solution of can be interpreted as an approximate minimizer of $f$ through the *Polyak-Łojasiewicz inequality* (see, e.g.,): ${{f{(\theta)}} - f^{\ast}} \leq {\frac{1}{2\mu}{\|{{\nabla f}{(\theta)}}\|}^{2}}$. The goal we will pursue will be to find an $\epsilon$-minimizer for $f$, which is defined as $\theta \in \Theta$ satisfying where $\epsilon > 0$ is the predefined accuracy. Note that it suffices to find an $\epsilon'$-stationary point of $f$ with $\epsilon' = \sqrt{2\mu\epsilon}$ to get an $\epsilon$-minimizer of $f$, which explains the relation between both settings.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 2.2 (Strong convexity)", "weight": 1.0} -->

In this paper, we focus on gradient descent methods and zoom-in on their computational complexity which we concretely measure through the following computation model.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 2.2 (Strong convexity)", "weight": 1.0} -->

Computation model. To characterize the running time of a GD-type algorithm for solving the problem and, we employ a variant of the well-established notion of *oracle complexity*. In particular, we tailor this notion to count the number of calls to *directional* derivatives of the objective where the directional derivative of $f$ along a unit-norm vector $u \in {\mathbb{R}}^{p}$ is a scalar defined as, This computation model -- which differs from most of the literature on first order methods that typically assumes the existence of a full-gradient oracle ${\nabla f}{(\theta)}$ -- will allow us to showcase the utility of a low-rank optimization method.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Exactly low-rank functions", "weight": 1.0} -->

In this paragraph, we formally define the notion of low-rank function (Definition 2.2. ‣ 2.2 Exactly low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions")). We then immediately observe that such functions have already widely been studied in the literature under different equivalent forms (Proposition 2.1. ‣ 2.2 Exactly low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions")). We make the simple observation that the class of such functions is fairly restricted, e.g., it contains no strongly convex function, thereby requiring the more general notion of approximately low-rank functions that will come later.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Approximately low-rank functions", "weight": 1.0} -->

The discussion above calls for a relaxation of the notion of low rank functions. In this section, we provide a definition for *approximately low-rank* functions where we no longer require that the gradients all belong to a given low-dimensional subspace $H$ but instead are inside a cone supported by this subspace, this is made explicit in Definition 2.3. ‣ 2.3 Approximately low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions"). In the rest of this section, more precisely through Proposition 2.2. ‣ 2.3 Approximately low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions") and Proposition 2.3. ‣ 2.3 Approximately low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions") we give more details about the desired properties of the approximation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithms and theoretical guarantees", "weight": 1.0} -->

In this section, we state the precise description of the proposed LRGD algorithm, we provide its computational complexity guarantees and conclude with a discussion on practical considerations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "LRGD algorithm", "weight": 1.0} -->

The proposed algorithm, LRGD, is an iterative gradient-based method. It starts by identifying a subspace $H$ of rank $r \leq p$ that is a good candidate to match our definition of approximately low-rank function for the objective $f$, i.e., Definition 2.3. ‣ 2.3 Approximately low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions"). More precisely, we pick $r$ random models $\theta^{1},\cdots,\theta^{r}$ and construct the matrix $G = {\lbrack{g_{1}/{\| g_{1}\|}},\cdots,{g_{r}/{\| g_{r}\|}}\rbrack}$ where we denote $g_{j} ≔ {{\nabla f}{(\theta^{j})}}$ for $j \in {\lbrack r\rbrack}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "LRGD algorithm", "weight": 1.0} -->

Then, assuming that $G$ is full-rank, the active subspace $H$ will be the space induced by the $r$ dominant left singular vectors of $G$. In other words, if we denote $G = {U\SigmaV^{\top}}$ the singular value decomposition (SVD) for $G$, we pick $H = {{span}{(U)}} = {{span}{(u_{1},\cdots,u_{r})}}$. Having set the active subspace $H$, LRGD updates the model parameters $\theta_{t}$ in each iteration $t$ by $\theta_{t + 1} = {\theta_{t} - {\alpha\hat{\nabla}f{(\theta_{t})}}}$ for a proper stepsize $\alpha$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "LRGD algorithm", "weight": 1.0} -->

Note that $\hat{\nabla}f{(\theta_{t})}$ here denotes the projection of the true gradient ${\nabla f}{(\theta_{t})}$ on the active subspace $H$ which LRGD uses as a low-rank proxy to ${\nabla f}{(\theta_{t})}$. Computing each approximate gradient $\hat{\nabla}f$ requires only $r$ (and not $p$) calls to the directional gradient oracle as we have ${\hat{\nabla}f{(\theta_{t})}} = {\sum_{j = 1}^{r}{\partial_{u_{j}}{f{(\theta_{t})}u_{j}}}}$. Algorithm 1 provides the details of LRGD.

<!-- chunk {"id": "body-0038", "role": "body", "section": "LRGD algorithm", "weight": 1.0} -->

1 Require: rank r ≤ p, stepsize α 2pick r points θ1, ⋯, θr and evaluate gradients gj = ∇f (θj) for j ∈ [r] 4compute SVD for G: G = U Σ V⊤ with U = [u1, ⋯, ur] (Gram-Schmidt or QR is also possible) 9 compute gradient approximation ${\hat{\nabla}f{(\theta_{t})}} = {\Pi_{H}{({{\nabla f}{(\theta_{t})}})}} = {\sum_{j = 1}^{r}{\partial_{u_{j}}{f{(\theta_{t})}u_{j}}}}$ 10 update $\theta_{t + 1} = {\theta_{t} - {\alpha\hat{\nabla}f{(\theta_{t})}}}$ Algorithm 1 Low-Rank Gradient Descent (LRGD)

<!-- chunk {"id": "body-0039", "role": "body", "section": "Oracle complexity analysis for strongly convex setting", "weight": 1.0} -->

Next, we characterize the oracle complexity of the proposed LRGD method for strongly convex objectives and discuss its improvement over other benchmarks. Let us start from a fairly simple case. As elaborated in Section 2 and in Proposition 2.1. ‣ 2.2 Exactly low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions"), strongly convex functions cannot be exactly low-rank. However, an exactly low-rank function may be strongly convex when restricted to its active subspace. Next theorem characterizes the oracle complexity for LRGD in such scenario.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Oracle complexity analysis for non-convex setting", "weight": 1.0} -->

Next, we turn our focus to non-convex and smooth objectives and discuss the benefits of LRGD on the overall coracle complexity for such functions. Let us begin with exactly low-rank objectives.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Variants of LRGD", "weight": 1.0} -->

Algorithm 1 (LRGD) can be extended to broader settings, especially in order to make it less sensitive to assumptions on the function $f$, since such assumptions are rarely known a priori before the optimization task is defined. In this section, we present two such extensions: Algorithm 2 (in Appendix B) provides a variant of LRGD where the active subspace is updated as soon as the low-rank descent converges. Note that this guarantees the termination of the optimization algorithm on any function -- and not just on functions satisfying the assumptions of the theoretical results. This algorithm is particularly adapted to situations where the function is *locally* approximately rank $r$ as the active subspace is updated through a local sampling (that is also used to accelerate the descent with $r$ iterations of GD). This algorithm still takes the parameter $r$ as an input. It is used for empirical tests in Section 4.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Variants of LRGD", "weight": 1.0} -->

Algorithm 3 (in Appendix B) provides a variant of LRGD that is adapted to situations where the rank $r$ is unknown. In this algorithm, the active subspace is made larger as when the algorithm reaches convergence on the corresponding subspace. As a result the rank $r$ goes from $1$ to $p$. If the function is rank $r^{\ast}$ all iterations where the rank $r$ goes from $r^{\ast}$ to $p$ will be cost-less. Note that in some circumstances, the arithmetic progression of the rank ${{update}{(r)}} = {r + 1}$ can be can be advantageously replaced by a geometric progression ${{update}{(r)}} = {2r}$. The empirical evaluation of this variant is left for future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

In this section we attempt to demonstrate the utility of the LRGD method (specifically, the iterative version in Algorithm 2 in Appendix B) through numerical simulations. We start in Figure 1 by a simple two-dimensional example ($p = 2$ and $r = 1$) to help building intuition about the method. In this experiment we observe that even when the LRGD method makes a more important number of iterations than the vanilla GD methods (left), it may be as efficient in terms of oracle calls (right). We then argue with Tables 2, 3, 4 (Tables 3, 4 are in Appendix H) that the LRGD method significantly outperforms the vanilla GD method in ill-conditioned setups.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

A close observation of Figure 1 and of the subsequent tables allows to make the following observations about situations where the LRGD method outperforms GD.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

Even for functions that are not approximately low-rank -- as in the example from Figure 1 -- using LRGD instead of GD does not seem to hurt in terms of number of oracle calls.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

In the results of Table 2, LRGD outperforms GD by a factor at most ${p/r} = 2$ that this factor is nearly attained in some cases (bottom-right of the table). This is in coherence with the theoretical results from Section 3 and the motivation from the introduction stating that the benefits of the LRGD method are indeed particularly visible when the ratio $p/r$ is higher.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

As observed in Figure 1, the LRGD method converges after a series of phases that end with the convergence of the descent on a given subspace. We can distinctly see two phases (iteration 1 to 7 and iteration 7 to 17) and can roughly guess two others (iteration 17 to 19 and iteration 19 to 21). These phases traduce in a series of waterfalls (Figure 1, right) that each tend to be sharper than the single waterfall of GD.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

The LRGD method is particularly efficient when consecutive gradient evaluations are very correlated. This typically because when the step-size $\alpha$ is too small with respect to the local variations of the function. The step-size is determined to satisfy $\alpha < {1/L}$. It is therefore smaller for ill-conditioned functions -- i.e., examples on the right of Table 2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

Conclusion. This work proposes an optimization approach that leverages low-rank structure to reduce the number of directional derivative queries. We believe that other optimization methods could benefit from incorporating such an approach.
