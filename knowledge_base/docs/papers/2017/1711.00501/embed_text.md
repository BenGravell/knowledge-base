## Introduction

Scalable optimization has been playing crucial roles in the success of deep learning, which has immense applications in artificial intelligence. Remarkably, optimization issues are often addressed through designing new models that make the resulting training objective functions easier to be optimized. For example, over-parameterization, batch-normalization, and residual networks \[, \] are often considered as ways to improve the optimization landscape of the resulting objective functions.

How do we design models and objective functions that allow efficient optimization with guarantees? Towards understanding this question in a principled way, this paper studies learning neural networks with one hidden layer. Roughly speaking, we will show that when the input is from Gaussian distribution and under certain simplifying assumptions on the weights, we can design an objective function $G{(\cdot)}$, such that\\[a\] all local minima of $G{(\cdot)}$ are global minima\\[b\] all the global minima are the desired solutions, namely, the ground-truth parameters (up to permutation and some fixed transformation).

We note that designing such objective functions is challenging because 1) the natural $\ell_{2}$ loss objective does have bad local minimum, and 2) due to the permutation invariance^11^1Permuting the rows of $B^{\star}$ and the coordinates of $a^{\star}$ correspondingly preserves the functionality of the network., the objective function inherently has to contain an exponential number of isolated local minima.

### Setup and known issues with proper learning

We aim to learn a neural network with a one-hidden-layer using a non-convex objective function. We assume input $x$ comes from Gaussian distribution and the label $y$ comes from the model where ${a^{\star} \in {\mathbb{R}}^{d}},{B^{\star} \sim {\mathbb{R}}^{m \times d}}$ are the ground-truth parameters, $\sigma{(\cdot)}$ is a element-wise non-linear function, and $\xi$ is a noise vector with zero mean. Here we can without loss of generality assume $x$ comes from spherical Gaussian distribution $\mathcal{N}{(0,\text{Id}_{d \times d})}$. ^22^2This is because if $x \sim {N{(0,\Sigma)}}$, then we can whiten the data by taking $x' = {\Sigma^{- {1/2}}x}$ and define $B_{}^{\star '} = {B\Sigma^{1/2}}$. We note that ${B_{}^{\star '}x'} = {Bx}$ and therefore we main the functionality of the model.

For technical reasons, we will further assume $m \leq d$ and that $a^{\star}$ has non-negative entries.

The most natural learning objective is perhaps the $\ell_{2}$ loss function, given the additive noise. Concretely, we can parameterize with training parameters ${a \in {\mathbb{R}}^{d}},{B \sim {\mathbb{R}}^{m \times d}}$ of the same dimension as $a^{\star}$ and $B^{\star}$ correspondingly, and then use stochastic gradient descent to optimize the $\ell_{2}$ loss function. When we have enough training examples, we are effectively minimizing the following population risk with stochastic updates, However, empirically stochastic gradient descent cannot converge to the ground-truth parameters in the synthetic setting above when ${\sigma{(x)}} = {\text{ReLU}{(x)}} = {\max{\{ x,0\}}}$, even if we have access to an infinite number of samples, and $B^{\star}$ is a orthogonal matrix. Such empirical results have been reported previously, and we also provide our version in Figure 1 of Section 6. This is consistent with observations and theory that over-parameterization is crucial for training neural networks successfully \[\].

These empirical findings suggest that the population risk $f{(a,B)}$ has spurious local minima with inferior error compared to that of the global minimum. This phenomenon occurs even if we assume we know $a^{\star}$ or $a^{\star} = \mathbf{1}$ is merely just the all one's vector. Empirically, such landscape issues seem to be alleviated by over-parameterization. By contrast, our method described in the next section does not require over-parameterization and might be suitable for applications that demand the recovery of the true parameters.

### Our contributions

Towards learning with the same number of training parameters as the ground-truth model, we first study the landscape of the population risk $f{( \cdot )}$ and give an analytic formula for it --- as an explicit function of the ground-truth parameter and training parameter with the randomness of the data being marginalized out. The formula in equation (2.3) shows that $f{( \cdot )}$ is implicitly attempting to solve simultaneously a finite number of low-rank tensor decomposition problems with commonly shared components.

Inspired by the formula, we design a new training model whose associated loss function --- named $f'$ and formally defined in equation (2.6) --- corresponds to the loss function for decomposing a matrix (2-nd order tensor) and a 4-th order tensor (Theorem 2.2). Empirically, stochastic gradient descent on $f'$ learns the network as shown in experiment section (Section 6).

Despite the empirical success of $f'$, we still lack a provable guarantee on the landscape of $f'$. The second contribution of the paper is to design a more sophisticated objective function $G{( \cdot )}$ whose landscape is provably nice --- all the local minima of $G{( \cdot )}$ are proven to be global, and they correspond to the permutation of the true parameters. See Theorem 2.3.

Moreover, the value and the gradient of $G$ can be estimated using samples, and there are no constraints in the optimization. These allow us to use straightforward stochastic gradient descent (see guarantees in \[, JGN^+^17\]) to optimize $G{( \cdot )}$ and converge to a local minimum, which is also a global minimum (Corollary 2.4).

Finally, we also prove a finite-sample complexity result. We will show that with a polynomial number of samples, the empirical version of $G$ share almost the same landscape properties as $G$ itself (Theorem 2.7). Therefore, we can also use an empirical version of $G$ as a surrogate in the optimization.

### Related work

The work of Arora et al. is one of the early results on provable algorithms for learning deep neural networks, where the authors give an algorithm for learning deep generative models with sparse weights. Livni et al., Zhang et al. \[, \], and Daniely et al. study the learnability of special cases of neural networks using ideas from kernel methods. Janzamin et al. give a polynomial-time algorithm for learning one-hidden-layer neural networks with twice-differential activation function and known input distributions, using the ideas from tensor decompositions.

A series of recent papers study the theoretical properties of non-convex optimization algorithms for one-hidden-layer neural networks. Brutzkus and Globerson and Tian analyze the landscape of the population risk for one-hidden-layer neural networks with Gaussian inputs under the assumption that the weights vector associated to each hidden variable (that is, the filters) have disjoint supports. Li and Yuan prove that stochastic gradient descent recovers the ground-truth parameters when the parameters are known to be close to the identity matrix. Zhang et al. studies the optimization landscape of learning one-hidden-layer neural networks with a specific activation function, and they design a specific objective function that can recover a single column of the weight matrix. Zhong et al. \[ZSJ^+^17\] studies the convergence of non-convex optimization from a good initializer that is produced by tensor methods. Our algorithm works for a large family of activation functions (including ReLU) and any full-rank weight matrix. To our best knowledge, we give the first global convergence result for gradient-based methods for our general setting.^33^3The work of \[, ZSJ^+^17\] are closely related, but they require tensor decomposition as the algorithm/initialization.

The optimization landscape properties have also been investigated on simplified neural networks models. Kawaguchi shows that the landscape of deep neural nets does not have bad local minima but has degenerate saddle points. Hardt and Ma show that re-parametrization using identity connection as in residual networks can remove the degenerate saddle points in the optimization landscape of deep linear residual networks. Soudry and Carmon showed that an over-parameterized neural network does not have bad differentiable local minimum. Hardt et al. analyze the power of over-parameterization in a linear recurrent network (which is equivalent to a linear dynamical system.)

The optimization landscape has also been analyzed for other machine learning problems, including SVD/PCA phase retrieval/synchronization, orthogonal tensor decomposition, dictionary learning, matrix completion, matrix sensing \[ \]. Our analysis techniques build upon that for tensor decomposition --- we add two additional regularization terms to deal with spurious local minimum caused by the weights $a^{\star}$ and to remove the constraints.

### Notations

We use ${\mathbb{N}},{\mathbb{R}}$ to denote the set of natural numbers and real numbers respectively. We use $\parallel \cdot \parallel$ to denote the Euclidean norm of a vector and spectral norm of a matrix. We use ${\parallel \cdot \parallel}_{F}$ to denote the Frobenius/Euclidean norm of a matrix or high-order tensor. For a vector $x$, let ${\parallel x\parallel}_{0}$ denotes its infinity norm and for a matrix $A$, let ${|A|}_{0}$ be a shorthand for ${\parallel{\text{vec}{(A)}}\parallel}_{0}$ where $\text{vec}{(A)}$ is the vectorization of $A$. For a vector $x$, let $|x|_{\text{2nd}}$ denotes the second largest absolute values of the entries for $x$. We note that $| \cdot |_{\text{2nd}}$ is not a norm.

We use $A \otimes B$ to denote the Kronecker product of $A$ and $B$, and $A^{\otimes k}$ is a shorthand for $A \otimes \cdots \otimes A$ where $A$ appears $k$ times. For vectors $a \otimes b$ and $a^{\otimes k}$ denote the tensor product. We use ${\lambda_{\max}{( \cdot )}},{\lambda_{\min}{( \cdot )}}$ to denote the largest and smallest eigenvalues of a square matrix. Similarly, $\sigma_{\max}{( \cdot )}$ and $\sigma_{\min}{( \cdot )}$ are used to denote the largest and smallest singular values. We denote the identity matrix in dimension $d \times d$ by $\text{Id}_{d \times d}$, or Id when the dimension is clear from the context.

In the analysis, we rely on many properties of Hermite polynomials. We use $h_{j}$ to denote the $j$-th normalized Hermite polynomial. These polynomials form an orthonormal basis. See Section 4.1 for an introduction of Hermite polynomials.

We will define other notations when we first use them.

## Main Results

### Connecting $\ell_{2}$ Population Risk with Tensor Decomposition

We first show that a natural $\ell_{2}$ loss for the one-hidden-layer neural network can be interpreted as simultaneously decomposing tensors of different orders.

A straightforward approach of learning the model (1.1) is to parameterize the prediction by where ${a \in {\mathbb{R}}^{d}},{B \sim {\mathbb{R}}^{m \times d}}$ are the training parameters. Naturally, we can use $\ell_{2}$ as the empirical loss, which means the population risk is Throughout the paper, we use $b_{1}^{\star \top},\ldots,b_{m}^{\star \top}$ to denote the row vectors of $B^{\star}$ and similarly for $B$. That is, we have $B = \begin{bmatrix} \end{bmatrix}$ and $B^{\star} = \begin{bmatrix} \end{bmatrix}$. Let $a_{i}$ and $a_{i}^{\star}$'s be the coordinates of $a$ and $a^{\star}$ respectively.

We give the following analytic formula for the population risk defined above.

### Theorem 2.1

Assume vectors $b_{i},b_{i}^{\star}$'s are unit vectors. Then, the population risk $f$ defined in equation (2.2) satisfies that where ${\hat{\sigma}}_{k}$ is the $k$-th Hermite coefficient of the function $\sigma$. See section 4.1 for a short introduction of Hermite polynomial basis. ^44^4 When $\sigma = {ReLU}$, we have that ${\hat{\sigma}}_{0} = \frac{1}{\sqrt{2\pi}}$, ${\hat{\sigma}}_{1} = \frac{1}{2}$. For $n \geq 2$ and even, ${\hat{\sigma}}_{n} = \frac{{({{({n - 3})}!!})}^{2}}{\sqrt{2\pi{n!}}}$. For $n \geq 2$ and odd, ${\hat{\sigma}}_{n} = 0$.

Connection to tensor decomposition: We see from equation (2.3) that the population risk of $f$ is essentially an average of infinite number of loss functions for tensor decomposition. For a fixed $k \in {\mathbb{N}}$, we have that the $k$-th summand in equation (2.3) is equal to (up to the scaling factor ${\hat{\sigma}}_{k}^{2}$) where $T_{k} = {\sum_{i \in {\lbrack m\rbrack}}{a_{i}^{\star}b_{i}^{\star {\otimes k}}}}$ is a $k$-th order tensor in ${({\mathbb{R}}^{d})}^{\otimes k}$. We note that the objective $f_{k}$ naturally attempts to decompose the $k$-order rank-$m$ tensor $T_{k}$ into $m$ rank-1 components ${a_{1}b_{i}^{\otimes k}},\ldots,{a_{m}b_{m}^{\otimes k}}$.

The proof of Theorem 2.1 follows from using techniques in Hermite Fourier analysis, which is deferred to Section 4.2.

### Issues with optimizing $f$

It turns out that optimizing the population risk using stochastic gradient descent is empirically difficult. Figure 1 shows that in a synthetic setting where the noise is zero, the test error empirically doesn't converge to zero for sufficiently long time with various learning rate schemes, even if we are using fresh samples in iteration. This suggests that the landscape of the population risk has some spurious local minimum that is not a global minimum. See Section 6 for more details on the experiment setup.

### An empirical fix

Inspired by the connection to tensor decomposition objective described earlier in the subsection, we can design a new objective function that takes exactly the same form as the tensor decomposition objective function $f_{2} + f_{4}$. Concretely, let's define where $\gamma = {{\hat{\sigma_{2}}h_{2}} + {{\hat{\sigma}}_{4}h_{4}}}$ and ${h_{2}{(t)}} = {\frac{1}{\sqrt{2}}{({t^{2} - 1})}}$ and ${h_{4}{(t)}} = {\frac{1}{\sqrt{24}}{({{t^{4} - {6t^{2}}} + 3})}}$ are the 2nd and 4th normalized probabilists' Hermite polynomials. We abuse the notation slightly by using the same notation to denote the its element-wise application on a vector. Now for each example we use ${\parallel{{\hat{y}}' - y}\parallel}^{2}$ as loss function. The corresponding population risk is Now by an extension of Theorem 2.1, we have that the new population risk is equal to the ${{\hat{\sigma}}_{2}^{2}f_{2}} + {{\hat{\sigma}}_{4}^{2}f_{4}}$.

### Theorem 2.2

Let $f'$ be defined as in equation (2.6) and $f_{2}$ and $f_{4}$ be defined in equation (2.4). Assume $b_{i},b_{i}^{\star}$'s are unit vectors. Then, we have It turns out stochastic gradient descent on the objective $f'{(a,B)}$ (with projection to the set of matrices $B$ with row norm 1) converges empirically to the ground truth $(a^{\star},B^{\star})$ or one of its equivalent permutations. (See Figure 2.) However, we don't know of any existing work for analyzing the landscape of the objective $f'$ (or $f_{k}$ for any $k \geq 3$). We conjecture that the landscape of $f'$ doesn't have any spurious local minimum under certain mild assumptions on $(a^{\star},B^{\star})$. Despite recent attempts on other loss functions for tensor decomposition, we believe that analyzing $f'$ is technically challenging and its resolution will be potentially enlightening for the understanding landscape of loss function with permutation invariance. See Section 6 for more experimental results.

### Landscape design for orthogonal $B^{\star}$

The population risk defined in equation (2.6) --- though works empirically for randomly generated ground-truth $(a^{\star},B^{\star})$ --- doesn't have any theoretical guarantees. It's also possible that when $(a^{\star},B^{\star})$ are chosen adversarially or from a different distribution, SGD no longer converges to the ground-truth.

To solve this problem, we design another objective function $G{( \cdot )}$, such that the optimizer of $G{( \cdot )}$ still corresponds to the ground-truth, and $G{}$ has provably nice landscape --- all local minima of $G{}$ are global minima.

In this subsection, for simplicity, we work with the case when $B^{\star}$ is an orthogonal matrix and state our main result. The discussion of the general case is deferred to the end of this Section and Section A.

We define our objective function $G{(B)}$ as where $\varphi{(\cdot, \cdot)}$ is defined as and $\phi{(\cdot, \cdot, \cdot)}$ is defined as The rationale behind of the choices of $\phi$ and $\varphi$ will only be clearer and relevant in later sections. For now, the only relevant property of them is that both are smooth functions whose derivatives are easily computable.

We remark that we can sample $G{( \cdot )}$ using the samples straightforwardly --- it's defined as an average of functions of examples and the parameters. We also note that only parameter $B$ appears in the loss function. We will infer the value of $a^{\star}$ using straightforward linear regression after we get the (approximately) accurate value of $B^{\star}$.

Due to technical reasons, our method only works for the case when $a_{i}^{\star} > 0$ for every $i$. We will assume this throughout the rest of the paper. The general case is left for future work. Let $a_{\max}^{\star} = {\max a_{i}^{\star}}$, $a_{\min}^{\star} = {\min a_{i}^{\star}}$, and $\kappa^{\star} = {\max{a_{i}^{\star}/{\min a_{i}^{\star}}}}$. Our result will depend on the value of $\kappa^{\star}.$ Essentially we treat $\kappa^{\star}$ as an absolute constant that doesn't scale in dimension. The following theorem characterizes the properties of the landscape of $G{( \cdot )}$.

### Theorem 2.3

Let $c$ be a sufficiently small universal constant (e.g. $c = 0.01$ suffices) and suppose the activation function $\sigma$ satisfies ${\hat{\sigma}}_{4} \neq 0$. Assume $\mu \leq {c/\kappa^{\star}}$, $\lambda \geq {c^{- 1}a_{\max}^{\star}}$, and $B^{\star}$ is an orthogonal matrix. The function $G{(\cdot)}$ defined as in equation (2.8) satisfies that A matrix $B$ is a local minimum of $G$ if and only if $B$ can be written as $B = {DPB^{\star}}$ where $P$ is a permutation matrix and $D$ is a diagonal matrix with $D_{ii} \in \left\{ {{\pm 1} \pm {O{({{\mua_{\max}^{\star}}/\lambda})}}} \right\}$.^55^5More precisely, ${|D_{ii}|} = \sqrt{\frac{1}{1 - {{\mu{|{\hat{\sigma}}_{4}|}a_{i}^{\star}}/{({\sqrt{6}\lambda})}}}}$ Furthermore, this means that all local minima of $G$ are also global.

Any saddle point $B$ has a strictly negative curvature in the sense that ${\lambda_{\min}{({{\nabla^{2}G}{(B)}})}} \geq {- \tau_{0}}$ where $\tau_{0} = {c{\min{\{{{\mua_{\min}^{\star}}/{({\kappa^{\star}d})}},\lambda\}}}}$ Suppose $B$ is an approximate local minimum in the sense that $B$ satisfies Then $B$ can be written as $B = {{PDB^{\star}} + {EB^{\star}}}$ where $P$ is a permutation matrix, $D$ is a diagonal matrix satisfying the same bound as in bullet 1, and ${|E|}_{\infty} \leq {O{({\varepsilon/{({{\hat{\sigma}}_{4}a_{\min}^{\star}})}})}}$.

As a direct consequence, $B$ is $O_{d}{(\varepsilon)}$-close to a global minimum in Euclidean distance, where $O_{d}{( \cdot )}$ hides polynomial dependency on $d$ and other parameters.

The theorem above implies that we can learn $B^{\star}$ (up to permutation of rows and sign-flip) if we take $\lambda$ to be sufficiently large and optimize $G{( \cdot )}$ using stochastic gradient descent. In this case, the diagonal matrix $D$ in bullet 1 is sufficiently close to identity (up to sign flip) and therefore a local minimum $B$ is close to $B^{\star}$ up to permutation of rows and sign flip. The sign of each $b_{i}^{\star}$ can be recovered easily after we recover $a$ (see Lemma 2.5 below.)

Stochastic gradient descent converges to a local minimum (under the additional property as established in bullet 2 above), which is also a global minimum for the function $G{( \cdot )}$. We will prove the theorem in Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") as a direct corollary of Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). The technical bullet 2 and 3 of the theorem is to ensure that we can use stochastic gradient descent to converge to a local minimum as stated below.^66^6In the most general setting, converging to a local minimum of a non-convex function is NP-hard.

### Corollary 2.4

In the setting of Theorem 2.3, we can use stochastic gradient descent to optimize function $G{( \cdot )}$ (with fresh samples at each iteration) and converge to an approximate global minimum $B$ that is $\varepsilon$-close to a global minimum in time ${poly}{(d,{1/\varepsilon})}$.

After approximately recovering the matrix $B^{\star}$, we can also recover the coefficient $a^{\star}$ easily. Note that fixing $B$, we can fit $a$ using simply linear regression. For the ease of analysis, we analyze a slightly different algorithm. The lemma below is proved in Section B.

### Lemma 2.5

Given a matrix $B$ whose rows have unit norm, and are $\delta$-close to $B^{\star}$ in Euclidean distance up to permutation and sign flip with $\delta \leq {1/{({2\kappa^{\star}})}}$. Then, we can give estimates $a,B'$ (using e.g., Algorithm 1) such that there exists a permutation $P$ where ${\|{a - {Pa^{\star}}}\|}_{\infty} \leq {\deltaa_{\max}^{\star}}$ and $B'$ is row-wise $\delta$-close to $PB^{\star}$.

The key step towards analyzing objective function $G{(B)}$ is the following theorem that gives an analytic formula for $G{( \cdot )}$.

### Theorem 2.6

The function $G{(\cdot)}$ satisfies Theorem 2.6 is proved in Section 4. We will motivate our design choices with a brief overview in Section 3 and formally analyze the landscape of $G$ in Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") (see Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")).

### Finite sample complexity bounds

: Extending Theorem 2.3, we can characterize the landscape of the empirical risk $\hat{G}$, which implies that stochastic gradient on $\hat{G}$ also converges approximately to the ground-truth parameters with polynomial number of samples.

### Theorem 2.7

In the setting of Theorem 2.3, suppose we use $N$ empirical samples to approximate $G$ and obtain empirical risk $\hat{G}$. There exists a fixed polynomial $\text{poly}{(d,{1/\varepsilon})}$ such that if $N \geq {\text{poly}{(d,{1/\varepsilon})}}$, then with high probability the landscape of $\hat{G}$ very similar properties to that of $G$.

Precisely, if $B$ is an approximate local minimum in the sense that ${\lambda_{min}{({{\nabla^{2}\hat{G}}{(B)}})}} \geq {- {\tau_{0}/2}}$ and ${\|{{\nabla\hat{G}}{(B)}}\|} \leq {\varepsilon/2}$, then $B$ can be written as $B = {{DPB^{\star}} + {EB^{\star}}}$ where $P$ is a permutation matrix, $D$ is a diagonal matrix and ${|E|}_{\infty} \leq {O{({\varepsilon/{({{\hat{\sigma}}_{4}a_{\min}^{\star}})}})}}$.

All of the results above assume that $B^{\star}$ is orthogonal. Since the local minimum are preserved by linear transformation of the input space, these results can be extended to the general case when $B^{\star}$ is not orthogonal but full rank (with some additional technicality) or the case when the dimension is larger than the number of neurons ($m < d$). See Section A for details.

## Overview: Landscape Design and Analysis

In this section, we present a general overview of ideas behind the design of objective function $G{( \cdot )}$. Inspired by the formula (2.3), in Section 3.1, we envision a family of possible objective functions for which we have unbiased estimators via samples. In Section 3.2, we pick a specific function that feeds our needs: a) it has no spurious local minimum; b) the global minimum corresponds to the ground-truth parameters.

### Which objective can be estimated by samples?

Recall that in equation (2.2) of Theorem 2.1 we give an analytic formula for the straightforward population risk $f$. Although the population risk $f$ doesn't perform well empirically, the lesson that we learn from it help us design better objective functions. One of the key fact that leads to the proof of Theorem 2.1 is that for any continuous and bounded function $\gamma$, we have that Here ${\hat{\sigma}}_{k}$ and ${\hat{\gamma}}_{k}$ are the $k$-th Hermite coefficient of the function $\sigma$ and $\gamma$. That is, letting $h_{k}$ the $k$-th normalized probabilists' Hermite polynomials and $\langle \cdot, \cdot \rangle$ be the standard inner product between functions, we have ${\hat{\sigma}}_{k} = {\langle h_{k},\sigma\rangle}$.

Note that $\gamma$ can be chosen arbitrarily to extract different terms. For example, by choosing $\gamma = h_{k}$, we obtain that That is, we can always access functions forms that involves weighted sum of the powers of $\langle b_{i}^{\star},b_{i}\rangle$, as in RHS of equation (3.1).

Using a bit more technical tools in Fourier analysis (see details in Section 4), we claim that most of the symmetric polynomials over variables $\langle b_{i}^{\star},b_{j}\rangle$ can be estimated by samples:

### Claim 3.1 (informal)

For an arbitrary polynomial $p{}$ over a single variable, there exits a corresponding function $\phi^{p}$ such that Moreover, for an any polynomial $q{(\cdot, \cdot)}$ over two variables, there exists corresponding $\phi^{q}$ such that We will not prove these two general claims. Instead, we only focus on the formulas in Theorem 4.5 and Theorem 4.6, which are two special cases of the claims above.

Motivated by Claim 4.3, in the next subsection, we will pick an objective function which has no spurious local minimum among those functional forms on the right-hand sides of equation (3.2. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) and (3.3. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")).

### Which objective has no spurious local minima?

As discussed briefly in the introduction, one of the technical difficulties to design and analyze objective functions for neural networks comes from the permutation invariance --- if a matrix $B$ is a good solution, then any permutation of the rows of $B$ still gives an equally good solution (if we also permute the coefficients in $a$ accordingly). We only know of a very limited number of objective functions that guarantee to enjoy permutation invariance and have no spurious local minima.

We start by considering the objective function used, Note that here we overload the notation by using $b_{i}^{\star}$'s to denote a set of fixed vectors that we wanted to recover and using $b_{i}$'s to denote the variables. Careful readers may notice that $P{(B)}$ doesn't fall into the family of functions that we described in the previous section (that is, RHS equation of (3.2. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) and (3.3. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design"))), because it lacks the weighting $a_{i}^{\star}$'s. We will fix this issue later in the subsection. Before that we first summarize the nice properties of the landscape of $P{(B)}$.

For the simplicity of the discussion, let's assume $B^{\star} = \begin{bmatrix} \end{bmatrix}$ forms an orthonormal matrix in the rest of the subsection. Then, any permutation and sign-flip of the rows of $B^{\star}$ leads to a global minimum of $P{(\cdot)}$ --- when $B = {SQB^{\star}}$ with a permutation matrix $Q$ and a sign matrix $S$ (diagonal with $\pm 1$), we have that ${P{(B)}} = 0$ because one of ${\langle b_{i}^{\star},b_{j}\rangle}^{2}$ and ${\langle b_{i}^{\star},b_{k}\rangle}^{2}$ has to be zero for all $i,j,k$^77^7Note that $B^{\star}$ is orthogonal, and $j \neq k$).

It turns out that these permutations/sign-flips of $B^{\star}$ are also the only local minima^88^8We note that since there are constraints here, by local minimum we mean the local minimum on the manifold defined by the constraints. of function $P{( \cdot )}$. To see this, notice that $P{(B)}$ is a degree-2 polynomial of $B$. Thus if we pick an index $s$ and fix every row except for $b_{s}$, then $P{(B)}$ is a quadratic function over unit vector $b_{s}$ -- reduces to an smallest eigenvector problem. Eigenvector problems are known to have no spurious local minimum. Thus the corresponding function (w.r.t $b_{s}$) has no spurious local minimum. It turns out the same property still holds when we treat all the rows as variables and add the row-wise norm constraints (see proof ).

However, there are two issues with using objective function $P{(B)}$. The obvious one is that it doesn't involve the coefficients $a_{i}^{\star}$'s and thus doesn't fall into the forms of equation (3.3. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")). Optimistically, we would hope that for nonnegative $a_{i}^{\star}$'s the weighted version of $P$ below would also enjoy the similar landscape property When $a_{i}^{\star}$'s are positive, indeed the global minimum of $P'$ are still just all the permutations of the $B^{\star}$.^99^9This is the main reason why we require $a^{\star} \geq 0$. However, when ${\max a_{i}^{\star}} > {2{\min a_{i}^{\star}}}$, we found that $P'$ starts to have spurious local minima. It seems that spurious local minimum often occurs when a row of $B$ is a linear combination of a smaller number of rows of $B^{\star}$. See Section D for a concrete example.

To remove such spurious local minima, we add a regularization term below that pushes each row of $B$ to be close to one of the rows of $B^{\star}$, We see that for each fixed $j$, the part in $R{(B)}$ that involves $b_{j}$ has the form This is commonly used objective function for decomposing tensor $\sum_{i}{a_{i}^{\star}b_{i}^{\star {\otimes 4}}}$. It's known that for orthogonal $b_{i}^{\star}$'s, the only local minima are ${\pm b_{1}^{\star}},\ldots,{\pm b_{d}^{\star}}$. Therefore, intuitively $R{(B)}$ pushes each of the $b_{i}$'s towards one of the $b_{i}^{\star}$'s. ^1010^10However, note that $R{(B)}$ by itself doesn't work because it does not prevent the solutions where all the $b_{i}$'s are equal to the same $b_{j}^{\star}$. Choosing $\mu$ to be small enough, it turns out that ${P'{(B)}} + {R{(B)}}$ doesn't have any spurious local minimum as we will show in Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

Another issue with the choice of ${P'{(B)}} + {R{(B)}}$ is that we are still having a constraint minimization problem. Such row-wise norm constraints only make sense when the ground-truth $B^{\star}$ is orthogonal and thus has unit row norm. A straightforward generalization of $P{(B)}$ to non-orthogonal case requires some special constraints that also depend on the covariance matrix $B^{\star}B_{}^{\star \top}$, which in turn requires a specialized procedure to estimate. Instead, we move the constraints into the objective function by considering adding another regularization term that approximately enforces the constraints.

It turns out the following regularizer suffices for the orthogonal case, Moreover, we can extend this easily to the non-orthogonal case (see Section A) without estimating any statistics of $B^{\star}$ in advance. We note that $S{(B)}$ is not the Lagrangian multiplier and it does change the global minima slightly. We will take $\lambda$ to be large enough so that $\parallel b_{i}\parallel$ has to be close to 1. As a summary, we finally use the unconstrained objective Since $R{(B)}$ and $S{(B)}$ are degree-4 polynomials of $B$, the analysis of $G{(B)}$ is much more delicate, and we cannot use much linear algebra as we could for $P'{(B)}$. See Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") for details.

Finally we note that a feature of this objective $G{( \cdot )}$ is that it only takes $B$ as variables. We will estimate the value of $a^{\star}$ after we recover the value of $B$. (see Section B). ·

## Analytic Formula for Population Risks

### Basics on Hermite Polynomials

In this section, we briefly review Hermite polynomials and Fourier analysis on Gaussian space. Let $H_{j}$ be the probabilists' Hermite polynomial, and let $h_{j} = {\frac{1}{\sqrt{j!}}H_{j}}$ be the normalized Hermite polynomials. The normalized Hermite polynomial forms a complete orthonormal basis in the function space $L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}$ in the following sense^1111^11We denote by $L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}$ the weighted $L_{2}$ space, namely, ${L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}} \triangleq \left\{ f:{{\int_{- \infty}^{\infty}{f{(x)}^{2}e^{- {x^{2}/2}}{dx}}} < \infty} \right\}$. For two functions $f,g$ that map $\mathbb{R}$ to $\mathbb{R}$, define the inner product $\langle f,g\rangle$ with respect to the Gaussian measure as The polynomials $h_{0},\ldots,h_{m},\ldots$ are orthogonal to each other under this inner product: Here $\delta_{ij} = 1$ if $i = j$ and otherwise $\delta_{ij} = 0$. Given a function $\sigma \in {L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}}$, let the $k$-th Hermite coefficient of $\sigma$ be defined as Since ${h_{0},\ldots,h_{m},\ldots},$ forms a complete orthonormal basis, we have the expansion that We will leverage several other nice properties of the Hermite polynomials in our proofs. The following claim connects the Hermite polynomial to the coefficients of Taylor expansion of a certain exponential function. It can also serve as a definition of Hermite polynomials.

### Claim 4.1 (\[O'D14, Equation 11.8\])

We have that for ${t,z} \in {\mathbb{R}}$, The following Claims shows that the expectation $\mathbb{E}\left\lbrack {h_{n}{(x)}h_{m}{(y)}} \right\rbrack$ can be computed easily when $x,y$ are (correlated) Gaussian random variables.

### Claim 4.2 (\[O'D14, Section 11.2\])

Let $(x,y)$ be $\rho$-correlated standard normal variables (that is, both $x$,$y$ have marginal distribution $\mathcal{N}{}$ and ${\mathbb{E}{\lbrack{xy}\rbrack}} = \rho$). Then, As a direct corollary, we can compute $\mathbb{E}_{x \sim {\mathcal{N}{(0,\text{Id}_{d \times d})}}}\left\lbrack {\sigma{({u^{\top}x})}\gamma{({v^{\top}x})}} \right\rbrack$ by expanding in the Hermite basis and applying the Claim above.

### Claim 4.3

Let $\sigma,\gamma$ be two functions from $\mathbb{R}$ to $\mathbb{R}$ such that ${\sigma^{2},\gamma^{2}} \in {L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}}$. Then, for any unit vectors ${u,v} \in {\mathbb{R}}^{d}$, we have that

### Proof of Claim 4.3

Let $s = {u^{\top}x}$ and $t = {v^{\top}x}$. Then $s,t$ are two spherical standard normal random variables that are $\langle u,v\rangle$-correlated, and we have that We expand $\sigma{(s)}$ and $\gamma{(t)}$ in the Fourier basis and obtain that

### Analytic Formula for population risk $f$ and $f'$

In this section we prove Theorem 2.1 and Theorem 2.2, which both follow from the following more general Theorem.

### Theorem 4.4

Let ${\gamma,\sigma} \in {L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}}$, and $\hat{y} = {a^{\top}\gamma{({Bx})}}$ with parameter $a \in {\mathbb{R}}^{\ell}$ and $B \in {\mathbb{R}}^{\ell \times d}$. Define the population risk $f_{\gamma}$ as Suppose $B = \begin{bmatrix} \end{bmatrix}$ and $B^{\star} = \begin{bmatrix} \end{bmatrix}$ and $b_{i}$'s and $b_{i}^{\star}$'s have unit $\ell_{2}$ norm. Then, where ${\hat{\sigma}}_{k},{\hat{\gamma}}_{k}$ are the $k$-th Hermite coefficients of the function $\sigma$ and $\gamma$ respectively.

We can see that Theorem 2.1 follows from choosing $\gamma = \sigma$ and Theorem 2.2 follows from choosing $\gamma = {{{\hat{\sigma}}_{2}h_{2}} + {{\hat{\sigma}}_{4}h_{4}}}$. The key intuition here is that we can decompose $\sigma$ into a weighted combination of Hermite polynomials, and each Hermite polynomial influence the population risk more or less independently (because they are orthogonal polynomials with respect to the Gaussian measure).

### Proof of Theorem 4.4

### Analytic Formula for population risk $G$

In this section we show that the population risk $G{(\cdot)}$ (defined as in equation (2.8)) has the following analytical formula: The formula will be crucial for the analysis of the landscape of $G{(\cdot)}$ in Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). The formula follows straightforwardly from the following two theorems and the definition (2.8).

### Theorem 4.5

Let $\phi{( \cdot, \cdot, \cdot )}$ be defined as in equation (2.10), we have that

### Theorem 4.6

Let $\varphi{(\cdot, \cdot)}$ be defined as in equation (2.9), then we have that In the rest of the section we prove Theorem 4.5 and 4.6.

We start with a simple but fundamental lemma. Essentially all the result in this section follows from expanding the two sides of equation (4.1) below.

### Lemma 4.7

Let ${u,v} \in {\mathbb{R}}^{d}$ be two fixed vectors and $x \sim {\mathcal{N}{(0,\text{Id}_{d \times d})}}$. Then, for any ${s,t} \in {\mathbb{R}}$,

### Proof

Using the fact that ${\mathbb{E}\left\lbrack {\exp{({v^{\top}x})}} \right\rbrack} = {\exp{({\frac{1}{2}{\parallel v\parallel}^{2}})}}$, we have that, Next we extend some of the results in the previous section to the setting with different scaling (such as when $v$ in Claim 4.3 is no longer a unit vector.)

### Lemma 4.8

Let $u$ be a fixed unit vector and $v$ be an arbitrary vector in ${\mathbb{R}}^{d}$. Let ${\varphi{(v,x)}} = {{{\frac{1}{8}{\parallel v\parallel}^{4}} - {\frac{1}{4}{({v^{\top}x})}^{2}{\parallel v\parallel}^{2}}} + {\frac{1}{24}{({v^{\top}x})}^{4}}}$.

As a sanity check, we can verify that when $v$ is a unit vector, ${\varphi{(v,x)}} = {\sqrt{24}h_{4}{({v^{\top}x})}}$ and th Lemma reduces to a special case of Claim 4.2. ‣ 4.1 Basics on Hermite Polynomials ‣ 4 Analytic Formula for Population Risks ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

### Proof

Let $A,B$ be formal power series in variable $s,t$ defined as $A = {\exp{({{\langle u,v\rangle}st})}}$ and $B = {\mathbb{E}\left\lbrack {{\exp{({{u^{\top}xt} - {\frac{1}{2}{\parallel u\parallel}^{2}t^{2}}})}}{\exp{({{v^{\top}xs} - {\frac{1}{2}{\parallel v\parallel}^{2}s^{2}}})}}} \right\rbrack}$. We refer the readers to for more backgrounds of power series. For casual readers, one can just think of $A$ as $B$ as two power series obtained by expanding the $exp{(\cdot)}$ via Taylor expansion. For a formal power series $A$ in variable $x$, let ${\lbrack x^{\alpha}\rbrack}A$ to denote coefficient in front of the monomial $x^{\alpha}$. By Lemma 4.7, we have that $A = B$, and thus which implies that where the last line is by the fact that ${\varphi{(v,x)}} = {{\lbrack s^{4}\rbrack}{\exp{({{v^{\top}xs} - {\frac{1}{2}{\parallel v\parallel}^{2}s^{2}}})}}}$. This can be verified by applying Claim 4.1. ‣ 4.1 Basics on Hermite Polynomials ‣ 4 Analytic Formula for Population Risks ‣ Learning One-hidden-layer Neural Networks with Landscape Design") with $t = {s{\parallel v\parallel}}$ and $z = \frac{v^{T}x}{\parallel v\parallel}$, and noting that ${H_{4}{(x)}} = {{x^{4} - {6x^{2}}} + 3}$. ∎ Now we are ready prove Theorem 4.6 using Lemma 4.8.

### Proof of Theorem 4.6

Using the fact that ${\sigma{({v^{\top}x})}} = {\sum_{k = 0}^{\infty}{{\hat{\sigma}}_{k}h_{k}{({v^{\top}x})}}}$, we have that Towards proving Theorem 4.5, we start with the following Lemma. Inspired by the proofs above, we design a function $\phi{(v,w,x)}$ such that we can estimate ${\langle u,v\rangle}^{2}{\langle u,w\rangle}^{2}$ by taking expectation of $\mathbb{E}\left\lbrack {\sigma{({u^{\top}x})}\phi{(v,w,x)}} \right\rbrack$.

### Lemma 4.9

Let $a$ be a fixed unit vector in ${\mathbb{R}}^{d}$ and $v,w$ two fixed vectors in ${\mathbb{R}}^{d}$. Let $\varphi{(\cdot, \cdot)}$ be defined as in Lemma 4.8. Define $\phi{(v,w,x)}$ as Then, we have that

### Proof

Using the fact that ${{{\langle u,{v + w}\rangle}^{2} + {\langle u,{v - w}\rangle}^{4}} - {2{\langle u,v\rangle}^{2}} - {2{\langle u,w\rangle}^{4}}} = {12{\langle u,v\rangle}^{2}{\langle u,w\rangle}^{2}}$ and Lemma 4.8, we have that Using the fact that ${\sigma{({u^{\top}x})}} = {\sum_{k = 0}^{\infty}{{\hat{\sigma}}_{k}h_{k}{({u^{\top}x})}}}$, we conclude that Now we are ready to prove Theorem 4.5 by using Lemma 4.9 for every summand.

### Proof of Theorem 4.5

## Landscape of Population Risk $G{( \cdot )}$

In this section we prove Theorem 2.3. Since the landscape property is invariant with respect to rotations of parameters, without loss of generality we assume $B^{\star}$ is the identity matrix Id throughout this section. (See Section A for a precise statement for the invariance.) Recall that by Theorem 2.6, the population risk $G{(\cdot)}$ in the case of $B^{\star} = \text{Id}$ is equal to In the rest of section we work with the formula above for $G{(\cdot)}$ instead of the original definition. In fact, for future reference, we study a more general version of the function $G$. For nonnegative vectors $\alpha,\beta$ and nonnegative number $\mu$, let $G_{\alpha,\beta,\mu}$ be defined as Here $e_{i}$ denotes the $i$-th natural basis vector. We see that $G$ is sub-case of $G_{\alpha,\beta,\mu}$ and we prove the following extension of Theorem 2.3. Let $\alpha_{\max} = {\max_{i}\alpha_{i}}$ and $\alpha_{\min} = {\min_{i}\alpha_{i}}$.

### Theorem 5.1

Let $\kappa_{\alpha} = {\alpha_{\max}/\alpha_{\min}}$ and $c$ be a sufficiently small universal constant (e.g. $c = 10^{- 2}$ suffices). Suppose $\mu \leq {{c\alpha_{\min}}/\beta_{\max}}$ and $\lambda \geq {4{\max{({\mu\beta_{\max}},\alpha_{\max})}}}$. Then, the function $G_{\alpha,\beta,\mu}{(B)}$ defined as in equation (5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) satisfies that A matrix $B$ is a local minimum of $G_{\alpha,\beta,\mu}$ if and only if $B$ can be written as $B = {DP}$ where $P$ is a permutation matrix and $D$ is a diagonal matrix with $D_{ii} \in \left\{ {\pm \sqrt{\frac{1}{1 - {{\mu\beta_{i}}/\lambda}}}} \right\}$.

Any saddle point $B$ has strictly negative curvature in the sense that ${\lambda_{\min}{({{\nabla^{2}G_{\alpha,\beta,\mu}}{(B)}})}} \leq {- \tau_{0}}$ where $\tau_{0} = {c{\min{\{{{\mu\beta_{\min}}/{({\kappa_{\alpha}d})}},{{\mu\beta_{\min}^{2}}/\beta_{\max}},\lambda\}}}}$ Suppose $B$ is an approximate local minimum in the sense that $B$ satisfies Then $B$ can be written as $B = {{DP} + E}$ where $P$ is a permutation matrix, $D$ is a diagonal matrix with the entries satisfying and $E$ is an error matrix satisfying As a direct consequence, $B$ is $O_{d}{(\varepsilon)}$-close to a global minimum in Euclidean distance, where $O_{d}{(\cdot)}$ hides polynomial dependency on $d$ and other parameters.

Here we recall that ${|E|}_{\infty}$ denotes the largest entries in the matrix $E$. Theorem 2.3 follows straightforwardly from Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") by setting $\alpha = {2\sqrt{6}{|{\hat{\sigma}}_{4}|}a^{\star}}$ and $\beta = {{{|{\hat{\sigma}}_{4}|}a^{\star}}/\sqrt{6}}$. In the rest of the section we prove Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

Note that our variable $B$ is a matrix of dimension $d \times d$ and we use $b_{i}$ to denote the rows of $B$, that is, $B = \begin{bmatrix} \end{bmatrix}$. Naturally, towards analyzing the properties of a local minimum $B$, the first step is that we pick a row $b_{s}$ of $B$ and treat only $b_{s}$ as variables and others rows as fixed. We will show that local optimality of $b_{s}$ will imply that $b_{s}$ is equal to one of the basis vector $e_{j}$ up to some scaling factor. This step is done in Section 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). Then in Section 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") we show that the local optimality of all the variables in $B$ implies that each of the rows of $B$ corresponds to different basis vector, which implies that $B$ is a permutation matrix (up to scaling of the rows).

### Step 1: Analysis of Local Optimality of a Single Row

Suppose we fix $b_{1},\cdots,b_{s - 1},b_{s + 1},\cdots,b_{d}$, and optimize only over $b_{s}$, we obtain the objective $h$ of the following form: We can see that setting ${\alpha_{i} = {a_{i}^{\star}{\sum_{k \neq s}{({b_{k}^{\top}e_{i}})}^{2}}}},{{\beta_{i} = a_{i}^{\star}},{{\text{~and~}x} = b_{s}}}$ gives us the original objective $G{(B)}$. In this subsection, we will work with $h{(\cdot)}$ and analyze the properties of the local minima of $h{(\cdot)}$.

The following lemma shows that a local minimum $x$ of the objective $h{( \cdot )}$ must be a scaling of a basis vector. Recall that $|x|_{\text{2nd}}$ denotes the second largest absolute value of the entries of $x$. The lemma deals generally an approximate local minimum, though we suggest casual readers simply think of ${\varepsilon,\tau} = 0$ in the lemma.

### Lemma 5.2

Let $h{( \cdot )}$ be defined in equation (5.3 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) with non-negative vectors $\alpha$ and $\beta$ in ${\mathbb{R}}^{d}$. Suppose parameters ${\varepsilon,\tau} \geq 0$ satisfy that $\varepsilon \leq \sqrt{\tau^{3}/\beta_{\min}}$. If some point $x$ satisfies ${\parallel{{\nabla h}{(x)}}\parallel} \leq \varepsilon$ and ${\lambda_{\min}{({{\nabla^{2}h}{(x)}})}} \geq {- \tau}$, then we have

### Proof

Without loss of generality, we can take $\varepsilon = \sqrt{\tau^{3}/\beta_{\min}}$ which means $\tau = {\varepsilon^{2/3}\beta_{\min}^{1/3}}$. The gradient and Hessian of function $h{(\cdot)}$ are where $\gamma \triangleq {4\lambda{({{\parallel x\parallel}^{2} - 1})}}$.

Let $S = {\{ i:{{|x_{i}|} \geq \delta}\}}$ be the indices of the coordinates that are significantly away from zero, where $\delta = \left(\frac{\varepsilon}{\beta_{\min}} \right)^{1/3}$. Since ${\parallel{{\nabla h}{(x)}}\parallel} \leq \varepsilon$, we have that ${|{{\nabla h}{(x)}_{i}}|} \leq \varepsilon$ for every $i \in {\lbrack d\rbrack}$, which implies that which further implies that If ${|S|} = 1$, then we are done because $|x|_{\text{2nd}} \leq \delta$. Next we prove that ${|S|} \geq 2$. For the sake of contradiction, we assume that ${|S|} \geq 2$. Moreover, WLOG, we assume that ${|x|}_{1} \geq {|x|}_{2}$ are the two largest entries of $|x|$ in absolute values.

We take $v \in {\mathbb{R}}^{d}$ such that $v_{1} = {- {x_{2}/\sqrt{x_{1}^{2} + x_{2}^{2}}}}$, and $v_{2} = {x_{1}/\sqrt{x_{1}^{2} + x_{2}^{2}}}$, and $v_{j} = 0$ for $j \geq 2$. Then we have that ${v^{\top}x} = 0$ and ${\parallel v\parallel} = 1$. We evaluate the quadratic form and have that Recall that $\delta = \left(\frac{\varepsilon}{\beta_{\min}} \right)^{1/3}$. Then we conclude that This contradicts with the assumption that ${\lambda_{\min}{({{\nabla^{2}h}{(x)}})}} \geq {- {\beta_{\min}^{1/3}\varepsilon^{2/3}}} = \tau$ and that ${\parallel v\parallel} = 1$. Therefore we have ${|S|} = 1$ and For future reference, we can also show that for a sufficiently strong regularization term (sufficiently large $\lambda$), the norm of a local minimum $x$ should be bounded from below and above by $1/2$ and $2$. This are rather coarse bounds that suffice for our purpose in this subsection. In Section 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") we will show that all the rows of a local minimum $B$ of $G$ have norm close to 1.

### Lemma 5.3

In the setting of Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), Suppose in addition that $\lambda \geq {4{\max{(\beta_{\max},\tau)}}}$ and $\varepsilon \leq {0.1\beta_{\min}d^{- {3/2}}}$, then Let $i^{\star} = {\arg{\max_{i}{|x_{i}|}}}$. In addition to the previous conditions in bullet 1, assume that $\lambda \geq {4\alpha_{i^{\star}}}$. Then, We remark that we have to state the conditions for the upperbounds and lowerbounds separately since they will be used with these different conditions.

### Proof

Let $S = {\{ i:{{|x_{i}|} \geq \delta}\}}$ be the indices of the coordinates that are significantly away from zero, where $\delta = \left(\frac{\varepsilon}{\beta_{\min}} \right)^{1/3}$. We first show that ${\parallel x\parallel}^{2} \leq 2$. We divide into two cases: $S$ is empty. Since $\varepsilon \leq {0.1\beta_{\min}d^{- {3/2}}}$, then $\delta \leq \frac{\sqrt{2}}{\sqrt{d}}$. We conclude that ${\parallel x\parallel}^{2} \leq 2$. $S$ is non-empty. For $i \in S$, recall equation (5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) which implies that Since $\lambda \geq {4\beta_{\max}}$, so $\lambda \geq {\beta_{\min}^{1/3}\varepsilon^{2/3}} \geq \frac{3\varepsilon}{4\delta}$, and thus from the display above we have that ${\parallel x\parallel}^{2} \leq 2$.

Next we show that ${\parallel x\parallel}^{2} \geq \frac{1}{2}$. Again we divide into two cases: $S$ is empty. For the sake of contradiction, assume that ${\parallel x\parallel}^{2} \leq \frac{1}{2}$, then $\gamma \leq {- {2\lambda}}$. We show that there is sufficient negative curvature. Recall that Choose index $j^{\star}$ so that $\alpha_{j^{\star}} = \alpha_{\min}$, then This contradicts with the fact that ${\lambda_{\min}{({{\nabla^{2}h}{(x)}})}} \geq {- \tau}$. Thus when $S$ is empty, ${\parallel x\parallel}^{2} \geq \frac{1}{2}$. $S$ is non-empty. Recall that $i^{\star} = {\arg{\max_{i}{|x_{i}|}}}$, and by definition $i^{\star} \in S$. Using Equation (5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) which implies that Since $\lambda \geq {4\alpha_{i^{\star}}}$, and $\lambda \geq {\beta_{\min}^{1/3}\varepsilon^{2/3}} \geq \frac{\varepsilon}{\delta}$, we conclude that ${\parallel x\parallel}^{2} \geq {1/2}$.

We have shown that a local minimum $x$ of $h$ should be a scaling of the basis vector $e_{i^{\star}}$. The following lemma strengthens the result by demonstrating that not all basis vector can be a local minimum --- the corresponding coefficient $\alpha_{i^{\star}}$ has to be reasonably small for $e_{i^{\star}}$ being a local minimum. The key intuition here is that if $\alpha_{i^{\star}}$ is very large compared to other entries of $\alpha$, then if we move locally the mass of $e_{i^{\star}}$ from entry $i^{\star}$ to some other index $j$, the objective function will be likely to decrease because $\alpha_{j}x_{j}^{2}$ is likely to be smaller than $\alpha_{i^{\star}}x_{i^{\star}}^{2}$. (Indeed, we will show that such movement will cause a second-order decrease of the objective function in the proof.)

### Lemma 5.4

In the setting of Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), let $i^{\star} = {\arg{\max_{i}{|x_{i}|}}}$. If ${\parallel{{\nabla h}{(x)}}\parallel} \leq \varepsilon$, and ${\lambda_{\min}{({{\nabla^{2}h}{(x)}})}} > {- \tau}$ for $0 \leq \tau \leq {{0.1\beta_{\min}}/d}$ and $\varepsilon \leq \sqrt{\tau^{3}/\beta_{\min}}$, then

### Proof

For the ease of notation, assume WLOG that $i^{\star} = 1$. Let $\delta = {({\tau/\beta_{\min}})}^{1/2}$. By the assumptions, we have that $\delta \leq \frac{1}{\sqrt{6d}}$. By Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we have ${\parallel x\parallel}^{2} \geq \frac{1}{2}$, which implies that Define $v = {{- {\left(\frac{x_{k}}{x_{1}} \right)e_{1}}} + e_{k}}$. Since $x_{1}$ is the largest entry of $x$, we can verify that $1 \leq {\parallel v\parallel}^{2} = {1 + \frac{x_{k}^{2}}{x_{1}^{2}}} \leq 2$. By the assumption, we have that On the other hand, recall the form of Hessian (equation (5.4 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"))), by straightforward algebraic manipulation, we have that Combining equation (5.8 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) and the equation above gives Since $k$ is arbitrary we complete the proof. ∎ The previous lemma implies that it's very likely that the local minimum $x$ can be written as $x = {x_{i^{\star}}e_{i^{\star}}}$ and the index $i^{\star}$ is also likely to be the argmin of $\alpha$. The following technical lemma shows that when this indeed happens, then we can strengthen Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") in terms of the error bound's dependency on $\varepsilon$ and $\tau$. In Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we have that $|x|_{\text{2nd}}$ is bounded by a function of $\tau$. Here we strengthen the bound to be a function that only depends on $\varepsilon$. Thus as long as $\tau$ be small enough so that we can apply Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") and Lemma 5.4 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") to meet the condition of the lemma below, then we get an error bound that goes to zero as $\varepsilon$ goes to zero. This translates to the error bound in bullet 3 of Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") where the bound on $E$ only depends on $\varepsilon$. For casual readers we suggest to skip this Lemma since its precise functionality will only be clearer in the proof of Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

### Lemma 5.5

In the setting of Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), in addition we assume that $i = {\text{argmin}_{k}{|\alpha_{k}|}}$ and that $x$ can be written as $x = {{x_{i}e_{i}} + x_{- i}}$ satisfying Then, we can strengthen the bound to

### Proof

WLOG, let $i = 1$. Let $x_{j}$ be the second largest entry of $x$ in absolute value. Define $v_{1} = {{4\beta_{1}x_{1}^{2}} - {2\alpha_{1}} - \gamma}$, and similarly $v_{j} = {{4\beta_{j}x_{j}^{2}} - {2\alpha_{j}} - \gamma}$. Since ${\parallel{{\nabla h}{(x)}}\parallel} \leq \varepsilon$, by equation (5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")), we have that ${|v_{1}|} \leq \frac{\varepsilon}{|x_{1}|}$ and ${|v_{2}|} = \frac{\varepsilon}{|x_{j}|}$. Subtracting ${4\beta_{1}x_{1}^{2}} = {{2\alpha_{1}} + \gamma + v_{1}}$ and ${4\beta_{j}x_{j}^{2}} = {{2\alpha_{j}} + \gamma + v_{j}}$, we obtain, Since ${\parallel x\parallel}^{2} \geq \frac{1}{2}$, then $x_{1}^{2} \geq {\frac{1}{2} - {d\delta^{2}}} \geq \frac{1}{3}$. Since ${|x_{j}|} \leq \delta$, Combining the above two displays, Since ${|v_{1}|} \leq \frac{\varepsilon}{|x_{1}|}$ and ${|v_{2}|} = \frac{\varepsilon}{|x_{2}|}$, and re-arranging gives ${|x_{j}|} \leq {3\frac{\varepsilon}{\beta_{\min}}}$. ∎

### Local Optimality of All the Variables

In this section we prove Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). Results in Subsection 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") have established that if $B$ is a local minimum, then each row $b_{s}$ of $B$ has to be a scaling of a basis vector. In this section we show that these basis vectors need to be distinct from each other. The following proposition summaries such a claim (with a weak error analysis).

### Proposition 5.6

In the setting of Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), suppose $B$ satisfies for parameters $\tau,\varepsilon$ satisfying $0 \leq \tau \leq {c{\min{\{{{\mu\beta_{\min}}/{({\kappa_{\alpha}d})}},\lambda\}}}}$ and $\varepsilon \leq {c{\min{\{\alpha_{\min},\sqrt{\tau^{3}/\beta_{\min}}\}}}}$. Then, the matrix $B$ can be written as where $D$ is diagonal such that ${{\forall i},{|D_{ii}|}} \in {\lbrack{1/4},2\rbrack}$, and $P$ is a permutation matrix, and ${|E|}_{\infty} \leq \delta$ with $\delta = \left(\frac{\tau}{\mu\beta_{\min}} \right)^{1/2}$.

As alluded before, in the proof we will first apply the results in Section 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") to show that when $B$ is a local minimum, each row $b_{s}$ has a unique large entry. Then we will show that the largest entries of each row sit on different columns. The key intuition behind the proof is that if two rows, say row $s,t$, have their large entries on the same column, then it means that there exists a column--- say column $k$ --- that doesn't contain largest entry of any row. Then either row $s$ or $t$ will violate Lemma 5.4 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). Or in other words, either row $s$ or $t$ can move their mass into the column $k$ to decrease the function value. This contradicts the assumption that $B$ is a local minimum.

### Proof

As pointed in the paragraph below equation (5.3 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")), when we restrict our attention to a particular row of $B$ and fix the rest of the rows the function $G_{\alpha,\beta,\mu}$ reduces to the function $h{( \cdot )}$ in equation (5.3 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) so that we can apply lemmas in Section 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

Concretely, fix an index $s \in {\lbrack d\rbrack}$ and let $x = b_{s}$. For all $i \in {\lbrack d\rbrack}$, let ${\overline{\alpha}}_{i} = {\alpha_{i}{\sum_{j \neq s}{({b_{j}^{\top}e_{i}})}^{2}}}$, and ${\overline{\beta}}_{i} = {\mu\beta_{i}}$. Then we have that We view the function above as $h{(x)}$. Now we apply Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") (by replacing $\alpha,\beta$ in Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") by $\overline{\alpha},\overline{\beta}$). The assumption that ${\lambda_{\min}{({{\nabla^{2}g_{\alpha,\beta,\mu}}{(B)}})}} \geq {- \tau}$ implies that ${\lambda_{\min}{({{\nabla^{2}h}{(x)}})}} \geq {- \tau}$ since ${\nabla^{2}h}{(x)}$ is a submatrix of ${\nabla^{2}g}{(B)}$. Moreover, ${\parallel{{\nabla h}{(x)}}\parallel} \leq {\parallel{{\nabla G}{(B)}}\parallel} \leq \varepsilon \leq \sqrt{\tau^{3}/{({\mu\beta_{\min}})}}$ Hence by Lemma 5.2 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we have that the second largest entry of $|b_{s}|$ satisfies where $\delta \triangleq \left(\frac{\tau}{\mu\beta_{\min}} \right)^{1/2}$ for the ease of notation. We can check that $\delta \leq \frac{1}{4\sqrt{\kappa_{\alpha}d}}$ by the assumption. Therefore, we have essentially shown that each row of $B$ has only one single large entry, since the second largest entry is at most $\delta$.

Next we show that each row of $B$ has largest entries on distinct columns. For each row $j \in {\lbrack d\rbrack}$, let $i_{j} = {\arg{\max_{i}{|{e_{i}^{\top}b_{j}}|}}}$ be the index of the largest entry of $b_{j}$. We will show that $i_{1},\ldots,i_{d}$ are distinct.

For the sake of contradiction, suppose they are not distinct, that is, there are two distinct rows $s,t$ that have the same largest entries on column $l$, that is, we assume that $i_{s} = i_{t} = l$. This implies that ${\{ i_{1},\ldots,i_{d}\}} \neq {\lbrack d\rbrack}$ and let $k \in {\lbrack d\rbrack}$ be the index such that $k \notin {\{ i_{1},\ldots,i_{d}\}}$. We note that by the assumption $\delta = \left(\frac{\tau}{\mu\beta_{\min}} \right)^{1/2} \leq \frac{1}{4\sqrt{\kappa_{\alpha}d}} \leq \frac{1}{4\sqrt{d}}$. We first bound from above ${\overline{\alpha}}_{k}$ Assume in addition without loss of generality that ${|{b_{s}^{\top}e_{l}}|} \leq {|{b_{t}^{\top}e_{l}}|}$. Let be the sum of squares of the entries on the column $l$ without entry $b_{j}^{\top}e_{l}$, and that ${\overline{\alpha}}_{l} = {\alpha_{l}z_{l}}$. We first prove that $z_{l} \geq {1/3}$.

For the sake of contradiction, assume ${z_{l} < {1/3}}.$ Then we have that ${{\overline{\alpha}}_{l} = {\alpha_{l}z} \leq {\frac{1}{3}\alpha_{l}}}.$ This implies that $\lambda \geq {4{\max{\{{\overline{\alpha}}_{l},\tau\}}}}$, and since $l$ is the index of the largest column of $b_{s}$ we can invoke Lemma 5.3 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") and conclude that ${\parallel b_{s}\parallel}^{2} \geq {1/2}$. This further implies that Since we have assumed that ${|{b_{s}^{\top}e_{l}}|} \leq {|{b_{t}^{\top}e_{l}}|}$. Then we obtain that which contradicts the assumption. Therefore, we conclude that $z_{l} \geq {1/3}$. Then we are ready to bound ${\overline{\alpha}}_{l}$ from below: The display above and Equation (5.13 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) implies that Note that $l$ is the largest entry in absolute value in the vector $b_{s}$. We will apply Lemma 5.4 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). We fix every row of $B$ except $b_{s}$ and consider the objective as a function of $b_{s}$ only. Again let ${\overline{\alpha}}_{i} = {\alpha_{i}{\sum_{j \neq s}{({b_{j}^{\top}e_{i}})}^{2}}}$, and ${\overline{\beta}}_{i} = {\mu\beta_{i}}$ and we have the equation (5.11 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")). (Note that now $\overline{\alpha}$ depends on the choice of $s$ which we fixed.) Lemma 5.4 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") gives us that Since $\varepsilon \leq {\frac{1}{50}\alpha_{\min}}$, $\tau \leq {\frac{1}{50}\alpha_{\min}}$ and ${\overline{\beta}}_{l} = {\mu\beta_{l}} \leq {\frac{1}{50}\alpha_{\min}}$, we obtain that which contradicts equation (5.14 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")). Thus we have established that $i_{1},\ldots,i_{d}$ are distinct.

Finally, let $Q$ be the matrix that only contain the largest entries (in absolute value) of each columns of $B$. Since $i_{1},\ldots,i_{d}$ are distinct, we have that $Q$ contains exactly one entry per row and per column. Therefore $Q$ can be written as $DP$ where $P$ is a permutation matrix and $D$ is a diagonal matrix. Moreover, we have that ${\parallel b_{s}\parallel}_{\infty}^{2} \geq {{\parallel b_{s}\parallel}^{2} - {d\left| b_{s} \right|_{\text{2nd}}^{2}}} \geq {1/4}$ and ${\parallel b_{s}\parallel}^{2} \leq 2$. Therefore, the largest entry of each row has absolute value between $1/4$ and $2$. Therefore ${|D|}_{ii} \in {\lbrack{1/4},2\rbrack}$. Let $E = {B - {PD}}$. Then we have that ${|E|}_{\infty} \leq {\max_{s}\left| b_{s} \right|_{\text{2nd}}} \leq \delta$,which completes the proof.

Applying Lemma 5.5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we can further strengthen Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") with better error bounds and better control of the largest entries of each column.

### Proposition 5.7 (Strengthen of Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"))

In the setting of Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). Suppose in addition that $\tau$ satisfies $\tau \leq {{c\mu\beta_{\min}^{2}}/\beta_{\max}}$. Then, the matrix $B$ can be written as where $P$ is a permutation matrix, $D$ is diagonal such that

### Proof

By Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we know that ${|E|}_{\infty} \leq \delta = \left( \frac{\tau}{\mu\beta_{\min}} \right)^{1/2}$. Now we use Lemma 5.5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") to strength the error bound.

As we have done in the proof of Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we again fix an arbitrary $s \in {\lbrack d\rbrack}$ and all the rows except $b_{s}$ and view $G_{\alpha,\beta,\mu}$ as a function of $b_{s}$. For all $i \in {\lbrack d\rbrack}$, let ${\overline{\alpha}}_{i} = {\alpha_{i}{\sum_{j \neq s}{({b_{j}^{\top}e_{i}})}^{2}}}$, and ${\overline{\beta}}_{i} = {\mu\beta_{i}}$ and view $G_{\alpha,\beta,\mu}$ as a function of the form $h{(x)}$ with $\alpha,\beta$ replaced by $\overline{\alpha},\overline{\beta}$, namely, We will verify the condition of Lemma 5.5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). Let $i$ be the index of the largest entry in absolute value of the vector $b_{s}$. Since we have shown that the largest entry in each row sits on different columns, and the second largest entry is always less than $\delta$, we have that, For any $k \neq i$, we know that the column $k$ contains some entry $(k,j_{k})$ which is the largest entry of some row, and we also have that $j_{k} \neq s$ since the largest entry of row $s$ is on column $i$. Therefore, we have that Therefore, $\overline{\alpha_{k}} \geq \overline{\alpha_{i}}$ for any $k \neq i$ and thus $i = {\text{argmin}_{k}{|{\overline{\alpha}}_{k}|}}$. By the fact that ${|E|}_{\infty} \leq \delta$, we have that ${\parallel x_{- i}\parallel}_{\infty} \leq \delta \leq {0.1{\min{\{{1/\sqrt{d}},\sqrt{\beta_{\min}/{(\beta_{\max})}}\}}}}$. Now we are ready to apply Lemma 5.5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") and obtain that $\left| b_{s} \right|_{\text{2nd}} \leq \frac{3\varepsilon}{\beta_{\min}}$. Applying the argument for every row $s$ gives ${|E|}_{\infty} \leq \frac{3\varepsilon}{\beta_{\min}}$.

Finally, we give the bound for the entires in $D$. Let $v$ be a short hand for ${\nabla h}{(b_{s})}$ which is equal to the $s$-th column of ${\nabla G}{(B)}$. Since $B$ is an $\varepsilon$-approximate stationary point, then we have that ${\parallel v\parallel} \leq \varepsilon$ and by straightforward calculation of the gradient, we have Since $x_{i} \neq 0$, dividing by $x_{i}$ gives, Rearranging the equation above gives, To upper bound $x_{i}^{2}$, we note that ${|v_{i}|} < \varepsilon$, ${\overline{\alpha}}_{i} > 0$, and ${\sum_{j \neq i}x_{j}^{2}} > 0$, so For the lower bound of $x_{i}^{2}$, we note that ${|E|}_{\infty} \leq \delta = \frac{3\varepsilon}{\beta_{\min}}$ implies ${\sum_{j \neq i}x_{j}^{2}} \leq {d\delta^{2}}$. Moreover, we have proved that each rows has largest entry at different columns. Also note that the largest entry of row $b_{s}$ is on column $i$. Therefore, we have ${\overline{\alpha}}_{i} = {\alpha_{i}{\sum_{j \neq s}{({b_{j}^{T}e_{i}})}^{2}}} \leq {\alpha_{\max}d\delta^{2}}$. Using these two estimates and $\delta = \frac{3\varepsilon}{\beta_{\min}}$, we have Finally we are ready to prove Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") by applying Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

### Proof of Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design")

By setting ${\varepsilon = 0},{\tau = 0}$ in Proposition 5.6 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we have that any local minimum $B$ satisfies that $B = {DP}$ where $P$ is a permutation matrix and $D$ is a diagonal and the precise diagonal entries of $D$. It can be verified that all these points have the same function value, so that they are all global minimizers.

Towards proving the second bullet, we note that a saddle point $B$ satisfies that ${{\nabla G}{(B)}} = 0$. We will prove that ${\lambda_{\min}{({{\nabla^{2}G}{(B)}})}} \leq {- \tau_{0}}$. For the sake of contradiction, suppose ${\lambda_{\min}{({{\nabla^{2}G}{(B)}})}} \geq {- \tau_{0}}$. Then setting $\varepsilon = 0$ and $\tau = \tau_{0}$ in Propostion 5.7. ‣ 5.2 Local Optimality of All the Variables ‣ 5 Landscape of Population Risk 𝐺⁢(⋅) ‣ Learning One-hidden-layer Neural Networks with Landscape Design"), we have that $B = {DP}$ and $D_{ii} = \left\{ {\pm \sqrt{\frac{1}{1 - {{\mu\beta_{i}}/\lambda}}}} \right\}$, which by bullet 1 implies that $B$ is a local minimum. This contradicts the assumption that $B$ is a saddle point.

The 3rd bullet is a just a rephrasing of Proposition 5.7. ‣ 5.2 Local Optimality of All the Variables ‣ 5 Landscape of Population Risk 𝐺⁢(⋅) ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). ∎

## Simulation

Figure 1: Data are generated by a network with ReLU activation without noise. The training model uses the same architecture. Left: the estimated population risk doesn’t converge to zero. Right: the parameter error using the surrogate in equation (6.1).

In this section, we provide simple simulation results that verify that minimizing $G{(B)}$ with SGD recovers a permutation of $B^{\star}$; however, minimizing Equation (2.2) with SGD results in finding spurious local minima. Based on the formula for the population risk in Equation (2.3), we also verified empirically the conjecture that SGD would successfully recover $B^{\star}$ using the activation functions ${\gamma{(z)}} = {{{\hat{\sigma}}_{2}h_{2}{(z)}} + {{\hat{\sigma}}_{4}h_{4}{(z)}}}$,^1212^12We also observed that using ${\gamma{(z)}} = {\frac{1}{2}{|z|}}$ also works but due to the space limitation we don't report the experimental results here. even if the data were generated via a model with ReLU activation. (See Section 2.1 for the rationale behind such conjectures.)

For all of our experiments, we chose $B^{\star} = \text{Id}_{d \times d}$ with dimension $d = 50$ and $a^{\star} = \mathbf{1}$ for simplicity, and the data is generated from a one-hidden-layer network with ReLU activation without noise. We use stochastic gradient descent with fresh samples at each iteration, and we plot the (expected) population error (that is, the error on a fresh batch of examples).

Figure 2: The labels are generated from a network with ReLU activation. We learn with σ̂2 h2 + σ̂4 h4 activation. Left: the test loss subtracted by the theoretical global minimum value. Right: the error in parameter space measured by equation (6.1) Figure 3: Learning with objective function G (⋅). Left: the test loss. Right: the error in parameter space measured by equation (6.1).

To test whether SGD converges to a matrix $B$ which is equivalent to $B^{\star}$ up to permutation of rows, we use a surrogate error metric to evaluate whether $B_{}^{\star {- 1}}B$ is close to a permutation matrix. Given a matrix $Q$ with row norm 1, let Then we have that if ${e{(Q)}} \leq \varepsilon$ for some $\varepsilon < {1/3}$, then it implies that $Q$ is $\sqrt{2\varepsilon}$-close to a permutation matrix in infinity norm. On the other direction, we know that if ${e{(Q)}} > \varepsilon$, then $Q$ is not $\varepsilon$-close to any permutation matrix in infinity norm. The latter statement also holds when $Q$ doesn't have row norm $1$.

Figure 1 shows that without over-parameterization, using ReLU as an activation function, SGD doesn't converge to zero test error and the ground-truth parameters. We decreased step-size by a factor of $4$ every $5000$ number of iterations after the error plateaus at $10000$ iterations. For the final $5000$ iterations, the step-size is less than $10^{- 9}$, so we can be confident that the non-zero objective value is not due to the variance of SGD. We see that none of the five runs of SGD converged to a global minimum.

Figure 2 shows that using ${{\hat{\sigma}}_{2}h_{2}} + {{\hat{\sigma}}_{4}h_{4}}$ as the activation function, SGD with projection to the set of matrices $B$ with row norm 1 converges to the ground-truth parameters. We also plot the loss function which converges the value of a global minimum. (We subtracted the constant term in equation (2.7) so that the global minimum has loss 0.)

Figure 3 shows that using our objective function $G{(B)}$, the iterate converges to the ground truth matrix $B^{\star}$. The fact that the parameter error goes up and down is not surprising, because the algorithm first gets close to a saddle point and then breaks ties and converges to a one of the global minima.

Finally we note that using the loss function $G{( \cdot )}$ seems to require significantly larger batch (and sample complexity) to reduce the variance in the gradients estimation. We used batch size 262144 in the experiment for $G{( \cdot )}$. However, in contrast, for the ${{\hat{\sigma}}_{2}h_{2}} + {\hat{\sigma_{4}}h_{4}}$ we used batch size 8192 and for relu we used batch size 256.

## Conclusion

In this paper we first give an analytic formula for the population risk of the standard $\ell_{2}$ loss, which empirically may converge to a spurious local minimum. We then design a novel population loss that is guaranteed to have no spurious local minimum.

Designing objective functions with well-behaved landscape is an intriguing and fruitful direction. We hope that our techniques can be useful for characterizing and designing the optimization landscape for other settings.

We conjecture that the objective ${\alphaf_{2}} + {\betaf_{4}}$ has no spurious local minimum when $\alpha,\beta$ are reasonable constants and the ground-truth parameters are in general position^1313^13See equation (2.4) for the definition of $f_{k}$ and Theorem 2.2 for how to access ${\alphaf_{2}} + {\betaf_{4}}$ in the setting of one-hidden-layer neural nets.. We provided empirical evidence to support the conjecture.

Our results assume that the input distribution is Gaussian. Extending them to other input distributions is a very interesting open problem.
