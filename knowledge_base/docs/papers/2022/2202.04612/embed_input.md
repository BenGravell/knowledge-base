<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Zeroth-Order Randomized Subspace Newton Methods

Topics include ZO-RSN.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Zeroth-order methods have become important tools for solving problems where we have access only to function evaluations. However, the zeroth-order methods only using gradient approximations are n times slower than classical first-order methods for solving n-dimensional problems. To accelerate the convergence rate, this paper proposes the zeroth order randomized subspace Newton (ZO-RSN) method, which estimates projections of the gradient and Hessian by random sketching and finite differences. This allows us to compute the Newton step in a lower dimensional subspace, with small computational costs. We prove that ZO-RSN can attain lower iteration complexity than existing zeroth order methods for strongly convex problems. Our numerical experiments show that ZO-RSN can perform black-box attacks under a more restrictive limit on the number of function queries than the state-of-the-art Hessian-aware zeroth-order method.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several applications in machine learning, signal processing and communication networks can often be cast into optimization problems, where gradients are difficult or even infeasible to compute. Popular application examples include optimal hyper-parameter tuning for learning models, black-box adversarial attacks on neural network models and sensor selection problems in smart grids or wireless networks. This motivates the study of the zeroth-order methods. A prominent type of zeroth order methods uses function value differences to estimate the gradients \[10, Section 3.4\]. However, these methods are much slower than classical gradient descent, and also suffers from poor performance particularly for ill-conditioned problems. An alternative way to improve their performance is to incorporate the second order information into zeroth-order methods. However, computing the full Hessian matrix can heavily increase the number of function evaluations and make the Newton step hard to compute, especially for high-dimensional problems. This necessitates us to approximate the Hessian matrix in a lower-dimensional subspace.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ye *et al.* developed the Hessian-aware zeroth order (ZOHA) methods, which integrate Hessian information into zeroth-order methods. The power-iteration based method ZOHA-PW has a lower query complexity than the gradient-estimating method by when the eigenvalues of the Hessian decay sufficiently quickly. However, the power iteration method requires $O{(n)}$ function queries per iteration for $n$-dimensional problems, which is expensive when $n$ is large. To decrease the query cost, they proposed the heuristic methods ZOHA-Gauss-DC and ZOHA-Diag-DC, which estimate the Hessian based on a limited number of random directions. However, no complexity bounds are provided for them.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another approach to reduce the times of computing Hessian information for high-dimensional problems is to use randomized sketching techniques. These sketching techniques construct lower dimensional sub-problems, which can be solved within small computation times, and enable classical optimization algorithms to have better scalability. For instance, a randomized subspace newton (RSN) method exploits the sketching techniques on the Newton method to solve the problems with very large dimension and to achieve accelerated convergence rate.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose Hessian-based zeroth-order algorithms using sketching techniques for huge-dimensional problems, called zeroth-order RSN (ZO-RSN). The methods exploit finite differences and sketching to approximate projections of the gradient and Hessian. We provide complexity bounds and prove that under certain conditions ZO-RSN attains lower query complexity than existing zeroth-order algorithms for strongly convex problems. Finally, our experiments with black-box attack problems on a convolutional neural network show that ZO-RSN has an overall competitive performance and higher success rate, compared to the ZOHA-Gauss-DC method.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the unconstrained optimization problem

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where the dimension $n$ could be very large. Here, $f{(x)}$ is a three times differentiable and $\mu$-strongly convex function, which is bounded from below and has its minimum value $f^{\ast}$ at the point $x^{\ast}$. $g{(x)}$ and $H{(x)}$ are also $L_{1}$- and $L_{2}$-Lipschitz continuous. To facilitate the analysis, we further make the following standard assumption on $f{(x)}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1. ‣ 2 Problem Formulation ‣ Zeroth-Order Randomized Subspace Newton Methods") states the smoothness and strong convexity of $f{(x)}$ under the norm weighted by its Hessian $\parallel \cdot \parallel_{H{(x)}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "RSN Methods", "weight": 1.0} -->

The randomized subspace Newton (RSN) method is a popular inexact Newton method for solving huge-dimensional problems. This method solves an exact Newton system restricted to a random subspace.

<!-- chunk {"id": "body-0011", "role": "body", "section": "RSN Methods", "weight": 1.0} -->

where $S_{k} \in {\mathbb{R}}^{n \times m}$ stores $m$ vectors that span the randomly selected subspace of ${\mathbb{R}}^{n}$. The next lemma characterizes the decrease in the function value from the ZO-RSN method.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Zeroth-order RSN Methods", "weight": 1.0} -->

In this section, we introduce the zeroth-order randomized subspace Newton (ZO-RSN) method, which builds on the RSN method.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Zeroth-order RSN Methods", "weight": 1.0} -->

This ensures function value improvement in Eq. if $\alpha$ is sufficiently small and ${\overset{\sim}{H}}_{S_{k}}{(x_{k})}$ is positive definite. In fact, we can ensure that positive definiteness of ${\overset{\sim}{H}}_{S_{k}}{(x_{k})}$ follows from $\alpha$ being small enough if we choose $S_{k}$ appropriately.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Theoretical results", "weight": 1.0} -->

We now provide a complexity bound for ZO-RSN methods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We compare the performance of ZO-RSN against the existing Hessian-aware zeroth methods called ZOHA-Gauss-DC that uses a descent-checking procedure to increase an attack success rate, and approximates Hessian according to

<!-- chunk {"id": "body-0016", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

where $\lambda$ is a positive constant and $u_{1},\ldots,u_{b}$ are the vectors generated from the Gaussian distribution with zero mean and unit variance. In particular, we evaluate both methods on training un-targeted black box adversarial attacks over the MNIST data set. These attacks are carried out against the trained convolutional neural network (CNN) model described in \[Section 5.2\]. For each example $x_{i}^{nat}$ in the test set, the optimizer aims to generate an adversarial example $x_{i}$ which differs from $x_{i}^{nat}$ by at most $\epsilon$ in $\ell_{\infty}$ norm, while being classified differently with sufficient confidence.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Here, ${\lbrack{Z{(x)}}\rbrack}_{i}$ represents the probability of an input $x$ belonging to class $i$ according to the trained neural network.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Since the problem is constrained and does not have guarantees for $\mu$-strong convexity or $L_{1}$-smoothness, we need to modify the ZO-RSN algorithm. Firstly, we artificially ensure positive definiteness and boundedness of ${\overset{\sim}{H}}_{S_{k}}{(x_{k})}$ by applying the operator $\Pi_{\lbrack\lambda_{\min},\lambda_{\max}\rbrack}{( \cdot )}$ that projects its eigenvalues onto an interval $\lbrack\lambda_{\min},\lambda_{\max}\rbrack$ to get a modified matrix ${\hat{H}}_{S_{k}}{(x_{k})}$. Secondly, we consider $\ell_{\infty}$-norm constraints by determining ${\overset{\sim}{\lambda}}_{k}$ that solves the following minimization problem

<!-- chunk {"id": "body-0019", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

This approach corresponds to using sequential quadratic programming (SQP) for nonlinear problems with linear constraints, but with the step to the next iterate being restricted to lie in a specific subspace. To solve the auxiliary problem quickly with a standard cvxopt solver, we generate $S_{k}$ by choosing its columns to be unit coordinate vectors. This enables us to formulate the problem with only $m$ constraints. This adapted ZO-RSN algorithm is called ZO-RSN-SQP. Finally, we use the descent-checking technique corresponding to that for ZOHA-Gauss-DC. The full description of ZO-RSN-SQP is given in Algorithm 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We trained the network model until its accuracy reached $98.84\%$, and also set ${\alpha = 0.1},{{\gamma = 1},{m = 3}}$ and $m_{\max} = 20$ for ZO-RSN-SQP and the same parameters for ZOHA-Gauss-DC for the un-targeted black box attacks described in \[. In the experiments, we either ended a test run if the algorithm managed to find a point with function value at $\omega = {- 1}$, or if the algorithm called queried the neural network for a prediction 50000 times. We labelled the former result as a success and the latter result as a failure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

The results of our black box attack experiments were summarized in Table 1. Firstly, ZO-RSN-SQP has a more stable performance than ZOHA-Gauss-DC. Even though both algorithms implement the same decent checking technique, only ZO-RSN-SQP succeeds in the attacks for all cases. Secondly, the mean number of queries for ZO-RSN-SQP is lower than that for ZOHA-Gauss-DC. This results from a minority of the problems, where ZOHA-Gauss-DC requires a large number of queries to solve. In contrast, ZOHA-Gauss-DC has a lower median value than ZO-RSN-SQP. As ZO-RSN requires more function queries per iteration and subspace dimension than ZOHA-Gauss-DC, one can hypothesize this extra effort is worthwhile mainly for the harder-to-attack test examples.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

To investigate the speed of convergence, we also ran a separate experiment where we made estimates of the average objective value after 2000, 4000 and 6000 queries, $f_{est2000}$, $f_{est4000}$, $f_{est6000}$, using the first 100 MNIST examples. The suboptimalities based on these results are also shown in Table 1. As we can see, ZOHA-Gauss-DC is initially faster, but ZO-RSN-SQP becomes more accurate towards the end.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have proposed the ZO-RSN method, a Hessian-based zeroth-order method that approximates sketched gradients and Hessians by finite differences. Our results display a lower iteration complexity of the ZO-RSN method than existing zeroth-order methods for strongly convex problems. The experiments with un-targeted adversarial attacks on a CNN model illustrate that the modified ZO-RSN method named ZO-RSN-SQP attains an overall competitive performance and a higher stability, compared to ZOHA-Gauss-DC.
