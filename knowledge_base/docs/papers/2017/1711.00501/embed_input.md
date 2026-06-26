<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning One-hidden-layer Neural Networks with Landscape Design

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of learning a one-hidden-layer neural network: we assume the input xin R^(d) is from Gaussian distribution and the label y = a^(top) sigma(Bx) + xi, where a is a nonnegative vector in R^(m) with m <= d, Bin R^(mx) d is a full-rank weight matrix, and xi is a noise vector. We first give an analytic formula for the population risk of the standard squared loss and demonstrate that it implicitly attempts to decompose a sequence of low-rank tensors simultaneously. Inspired by the formula, we design a non-convex objective function G(*) whose landscape is guaranteed to have the following properties: 1. All local minima of G are also global minima. 2. All global minima of G correspond to the ground truth parameters. 3. The value and gradient of G can be estimated using samples. With these properties, stochastic gradient descent on G provably converges to the global minimum and learn the ground-truth parameters. We also prove finite sample complexity result and validate the results by simulations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scalable optimization has been playing crucial roles in the success of deep learning, which has immense applications in artificial intelligence. Remarkably, optimization issues are often addressed through designing new models that make the resulting training objective functions easier to be optimized. For example, over-parameterization, batch-normalization, and residual networks are often considered as ways to improve the optimization landscape of the resulting objective functions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

How do we design models and objective functions that allow efficient optimization with guarantees? Towards understanding this question in a principled way, this paper studies learning neural networks with one hidden layer. Roughly speaking, we will show that when the input is from Gaussian distribution and under certain simplifying assumptions on the weights, we can design an objective function $G{(\cdot)}$, such that\\[a\] all local minima of $G{(\cdot)}$ are global minima\\[b\] all the global minima are the desired solutions, namely, the ground-truth parameters (up to permutation and some fixed transformation).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We note that designing such objective functions is challenging because 1) the natural $\ell_{2}$ loss objective does have bad local minimum, and 2) due to the permutation invariance^11^1Permuting the rows of $B^{\star}$ and the coordinates of $a^{\star}$ correspondingly preserves the functionality of the network., the objective function inherently has to contain an exponential number of isolated local minima.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Setup and known issues with proper learning", "weight": 1.0} -->

We aim to learn a neural network with a one-hidden-layer using a non-convex objective function. We assume input $x$ comes from Gaussian distribution and the label $y$ comes from the model where ${a^{\star} \in {\mathbb{R}}^{d}},{B^{\star} \sim {\mathbb{R}}^{m \times d}}$ are the ground-truth parameters, $\sigma{(\cdot)}$ is a element-wise non-linear function, and $\xi$ is a noise vector with zero mean. Here we can without loss of generality assume $x$ comes from spherical Gaussian distribution $\mathcal{N}{(0,\text{Id}_{d \times d})}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Setup and known issues with proper learning", "weight": 1.0} -->

^22^2This is because if $x \sim {N{(0,\Sigma)}}$, then we can whiten the data by taking $x' = {\Sigma^{- {1/2}}x}$ and define $B_{}^{\star '} = {B\Sigma^{1/2}}$. We note that ${B_{}^{\star '}x'} = {Bx}$ and therefore we main the functionality of the model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Setup and known issues with proper learning", "weight": 1.0} -->

For technical reasons, we will further assume $m \leq d$ and that $a^{\star}$ has non-negative entries.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Setup and known issues with proper learning", "weight": 1.0} -->

The most natural learning objective is perhaps the $\ell_{2}$ loss function, given the additive noise. Concretely, we can parameterize with training parameters ${a \in {\mathbb{R}}^{d}},{B \sim {\mathbb{R}}^{m \times d}}$ of the same dimension as $a^{\star}$ and $B^{\star}$ correspondingly, and then use stochastic gradient descent to optimize the $\ell_{2}$ loss function. When we have enough training examples, we are effectively minimizing the following population risk with stochastic updates, However, empirically stochastic gradient descent cannot converge to the ground-truth parameters in the synthetic setting above when ${\sigma{(x)}} = {\text{ReLU}{(x)}} = {\max{\{ x,0\}}}$, even if we have access to an infinite number of samples, and $B^{\star}$ is a orthogonal matrix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Setup and known issues with proper learning", "weight": 1.0} -->

Such empirical results have been reported previously, and we also provide our version in Figure 1 of Section 6. This is consistent with observations and theory that over-parameterization is crucial for training neural networks successfully.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Setup and known issues with proper learning", "weight": 1.0} -->

These empirical findings suggest that the population risk $f{(a,B)}$ has spurious local minima with inferior error compared to that of the global minimum. This phenomenon occurs even if we assume we know $a^{\star}$ or $a^{\star} = \mathbf{1}$ is merely just the all one's vector. Empirically, such landscape issues seem to be alleviated by over-parameterization. By contrast, our method described in the next section does not require over-parameterization and might be suitable for applications that demand the recovery of the true parameters.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Towards learning with the same number of training parameters as the ground-truth model, we first study the landscape of the population risk $f{( \cdot )}$ and give an analytic formula for it --- as an explicit function of the ground-truth parameter and training parameter with the randomness of the data being marginalized out. The formula in equation (2.3) shows that $f{( \cdot )}$ is implicitly attempting to solve simultaneously a finite number of low-rank tensor decomposition problems with commonly shared components.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Inspired by the formula, we design a new training model whose associated loss function --- named $f'$ and formally defined in equation (2.6) --- corresponds to the loss function for decomposing a matrix (2-nd order tensor) and a 4-th order tensor (Theorem 2.2). Empirically, stochastic gradient descent on $f'$ learns the network as shown in experiment section (Section 6).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Despite the empirical success of $f'$, we still lack a provable guarantee on the landscape of $f'$. The second contribution of the paper is to design a more sophisticated objective function $G{( \cdot )}$ whose landscape is provably nice --- all the local minima of $G{( \cdot )}$ are proven to be global, and they correspond to the permutation of the true parameters. See Theorem 2.3.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Moreover, the value and the gradient of $G$ can be estimated using samples, and there are no constraints in the optimization. These allow us to use straightforward stochastic gradient descent (see guarantees in \[, JGN^+^17\]) to optimize $G{( \cdot )}$ and converge to a local minimum, which is also a global minimum (Corollary 2.4).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Finally, we also prove a finite-sample complexity result. We will show that with a polynomial number of samples, the empirical version of $G$ share almost the same landscape properties as $G$ itself (Theorem 2.7). Therefore, we can also use an empirical version of $G$ as a surrogate in the optimization.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations", "weight": 1.0} -->

In the analysis, we rely on many properties of Hermite polynomials. We use $h_{j}$ to denote the $j$-th normalized Hermite polynomial. These polynomials form an orthonormal basis. See Section 4.1 for an introduction of Hermite polynomials.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations", "weight": 1.0} -->

We will define other notations when we first use them.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Connecting $\\ell_{2}$ Population Risk with Tensor Decomposition", "weight": 1.0} -->

We first show that a natural $\ell_{2}$ loss for the one-hidden-layer neural network can be interpreted as simultaneously decomposing tensors of different orders.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Connecting $\\ell_{2}$ Population Risk with Tensor Decomposition", "weight": 1.0} -->

A straightforward approach of learning the model (1.1) is to parameterize the prediction by where ${a \in {\mathbb{R}}^{d}},{B \sim {\mathbb{R}}^{m \times d}}$ are the training parameters. Naturally, we can use $\ell_{2}$ as the empirical loss, which means the population risk is Throughout the paper, we use $b_{1}^{\star \top},\ldots,b_{m}^{\star \top}$ to denote the row vectors of $B^{\star}$ and similarly for $B$. That is, we have $B = \begin{bmatrix} \end{bmatrix}$ and $B^{\star} = \begin{bmatrix} \end{bmatrix}$. Let $a_{i}$ and $a_{i}^{\star}$'s be the coordinates of $a$ and $a^{\star}$ respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Connecting $\\ell_{2}$ Population Risk with Tensor Decomposition", "weight": 1.0} -->

We give the following analytic formula for the population risk defined above.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Issues with optimizing $f$", "weight": 1.0} -->

It turns out that optimizing the population risk using stochastic gradient descent is empirically difficult. Figure 1 shows that in a synthetic setting where the noise is zero, the test error empirically doesn't converge to zero for sufficiently long time with various learning rate schemes, even if we are using fresh samples in iteration. This suggests that the landscape of the population risk has some spurious local minimum that is not a global minimum. See Section 6 for more details on the experiment setup.

<!-- chunk {"id": "body-0023", "role": "body", "section": "An empirical fix", "weight": 1.0} -->

Inspired by the connection to tensor decomposition objective described earlier in the subsection, we can design a new objective function that takes exactly the same form as the tensor decomposition objective function $f_{2} + f_{4}$. Concretely, let's define where $\gamma = {{\hat{\sigma_{2}}h_{2}} + {{\hat{\sigma}}_{4}h_{4}}}$ and ${h_{2}{(t)}} = {\frac{1}{\sqrt{2}}{({t^{2} - 1})}}$ and ${h_{4}{(t)}} = {\frac{1}{\sqrt{24}}{({{t^{4} - {6t^{2}}} + 3})}}$ are the 2nd and 4th normalized probabilists' Hermite polynomials. We abuse the notation slightly by using the same notation to denote the its element-wise application on a vector.

<!-- chunk {"id": "body-0024", "role": "body", "section": "An empirical fix", "weight": 1.0} -->

Now for each example we use ${\parallel{{\hat{y}}' - y}\parallel}^{2}$ as loss function. The corresponding population risk is Now by an extension of Theorem 2.1, we have that the new population risk is equal to the ${{\hat{\sigma}}_{2}^{2}f_{2}} + {{\hat{\sigma}}_{4}^{2}f_{4}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Landscape design for orthogonal $B^{\\star}$", "weight": 1.0} -->

The population risk defined in equation (2.6) --- though works empirically for randomly generated ground-truth $(a^{\star},B^{\star})$ --- doesn't have any theoretical guarantees. It's also possible that when $(a^{\star},B^{\star})$ are chosen adversarially or from a different distribution, SGD no longer converges to the ground-truth.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Landscape design for orthogonal $B^{\\star}$", "weight": 1.0} -->

To solve this problem, we design another objective function $G{( \cdot )}$, such that the optimizer of $G{( \cdot )}$ still corresponds to the ground-truth, and $G{}$ has provably nice landscape --- all local minima of $G{}$ are global minima.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Landscape design for orthogonal $B^{\\star}$", "weight": 1.0} -->

In this subsection, for simplicity, we work with the case when $B^{\star}$ is an orthogonal matrix and state our main result. The discussion of the general case is deferred to the end of this Section and Section A.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Landscape design for orthogonal $B^{\\star}$", "weight": 1.0} -->

We define our objective function $G{(B)}$ as where $\varphi{(\cdot, \cdot)}$ is defined as and $\phi{(\cdot, \cdot, \cdot)}$ is defined as The rationale behind of the choices of $\phi$ and $\varphi$ will only be clearer and relevant in later sections. For now, the only relevant property of them is that both are smooth functions whose derivatives are easily computable.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Landscape design for orthogonal $B^{\\star}$", "weight": 1.0} -->

We remark that we can sample $G{( \cdot )}$ using the samples straightforwardly --- it's defined as an average of functions of examples and the parameters. We also note that only parameter $B$ appears in the loss function. We will infer the value of $a^{\star}$ using straightforward linear regression after we get the (approximately) accurate value of $B^{\star}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Landscape design for orthogonal $B^{\\star}$", "weight": 1.0} -->

Due to technical reasons, our method only works for the case when $a_{i}^{\star} > 0$ for every $i$. We will assume this throughout the rest of the paper. The general case is left for future work. Let $a_{\max}^{\star} = {\max a_{i}^{\star}}$, $a_{\min}^{\star} = {\min a_{i}^{\star}}$, and $\kappa^{\star} = {\max{a_{i}^{\star}/{\min a_{i}^{\star}}}}$. Our result will depend on the value of $\kappa^{\star}.$ Essentially we treat $\kappa^{\star}$ as an absolute constant that doesn't scale in dimension. The following theorem characterizes the properties of the landscape of $G{( \cdot )}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Finite sample complexity bounds", "weight": 1.0} -->

: Extending Theorem 2.3, we can characterize the landscape of the empirical risk $\hat{G}$, which implies that stochastic gradient on $\hat{G}$ also converges approximately to the ground-truth parameters with polynomial number of samples.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Overview: Landscape Design and Analysis", "weight": 1.0} -->

In this section, we present a general overview of ideas behind the design of objective function $G{( \cdot )}$. Inspired by the formula (2.3), in Section 3.1, we envision a family of possible objective functions for which we have unbiased estimators via samples. In Section 3.2, we pick a specific function that feeds our needs: a) it has no spurious local minimum; b) the global minimum corresponds to the ground-truth parameters.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Which objective can be estimated by samples?", "weight": 1.0} -->

Recall that in equation (2.2) of Theorem 2.1 we give an analytic formula for the straightforward population risk $f$. Although the population risk $f$ doesn't perform well empirically, the lesson that we learn from it help us design better objective functions. One of the key fact that leads to the proof of Theorem 2.1 is that for any continuous and bounded function $\gamma$, we have that Here ${\hat{\sigma}}_{k}$ and ${\hat{\gamma}}_{k}$ are the $k$-th Hermite coefficient of the function $\sigma$ and $\gamma$. That is, letting $h_{k}$ the $k$-th normalized probabilists' Hermite polynomials and $\langle \cdot, \cdot \rangle$ be the standard inner product between functions, we have ${\hat{\sigma}}_{k} = {\langle h_{k},\sigma\rangle}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Which objective can be estimated by samples?", "weight": 1.0} -->

Note that $\gamma$ can be chosen arbitrarily to extract different terms. For example, by choosing $\gamma = h_{k}$, we obtain that That is, we can always access functions forms that involves weighted sum of the powers of $\langle b_{i}^{\star},b_{i}\rangle$, as in RHS of equation (3.1).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Claim 3.1 (informal)", "weight": 1.0} -->

For an arbitrary polynomial $p{}$ over a single variable, there exits a corresponding function $\phi^{p}$ such that Moreover, for an any polynomial $q{(\cdot, \cdot)}$ over two variables, there exists corresponding $\phi^{q}$ such that We will not prove these two general claims. Instead, we only focus on the formulas in Theorem 4.5 and Theorem 4.6, which are two special cases of the claims above.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Claim 3.1 (informal)", "weight": 1.0} -->

Motivated by Claim 4.3, in the next subsection, we will pick an objective function which has no spurious local minimum among those functional forms on the right-hand sides of equation (3.2. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) and (3.3. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

As discussed briefly in the introduction, one of the technical difficulties to design and analyze objective functions for neural networks comes from the permutation invariance --- if a matrix $B$ is a good solution, then any permutation of the rows of $B$ still gives an equally good solution (if we also permute the coefficients in $a$ accordingly). We only know of a very limited number of objective functions that guarantee to enjoy permutation invariance and have no spurious local minima.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

We start by considering the objective function used, Note that here we overload the notation by using $b_{i}^{\star}$'s to denote a set of fixed vectors that we wanted to recover and using $b_{i}$'s to denote the variables. Careful readers may notice that $P{(B)}$ doesn't fall into the family of functions that we described in the previous section (that is, RHS equation of (3.2. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")) and (3.3. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design"))), because it lacks the weighting $a_{i}^{\star}$'s. We will fix this issue later in the subsection. Before that we first summarize the nice properties of the landscape of $P{(B)}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

For the simplicity of the discussion, let's assume $B^{\star} = \begin{bmatrix} \end{bmatrix}$ forms an orthonormal matrix in the rest of the subsection. Then, any permutation and sign-flip of the rows of $B^{\star}$ leads to a global minimum of $P{(\cdot)}$ --- when $B = {SQB^{\star}}$ with a permutation matrix $Q$ and a sign matrix $S$ (diagonal with $\pm 1$), we have that ${P{(B)}} = 0$ because one of ${\langle b_{i}^{\star},b_{j}\rangle}^{2}$ and ${\langle b_{i}^{\star},b_{k}\rangle}^{2}$ has to be zero for all $i,j,k$^77^7Note that $B^{\star}$ is orthogonal, and $j \neq k$).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

It turns out that these permutations/sign-flips of $B^{\star}$ are also the only local minima^88^8We note that since there are constraints here, by local minimum we mean the local minimum on the manifold defined by the constraints. of function $P{( \cdot )}$. To see this, notice that $P{(B)}$ is a degree-2 polynomial of $B$. Thus if we pick an index $s$ and fix every row except for $b_{s}$, then $P{(B)}$ is a quadratic function over unit vector $b_{s}$ -- reduces to an smallest eigenvector problem. Eigenvector problems are known to have no spurious local minimum. Thus the corresponding function (w.r.t $b_{s}$) has no spurious local minimum. It turns out the same property still holds when we treat all the rows as variables and add the row-wise norm constraints (see proof ).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

However, there are two issues with using objective function $P{(B)}$. The obvious one is that it doesn't involve the coefficients $a_{i}^{\star}$'s and thus doesn't fall into the forms of equation (3.3. ‣ 3.1 Which objective can be estimated by samples? ‣ 3 Overview: Landscape Design and Analysis ‣ Learning One-hidden-layer Neural Networks with Landscape Design")). Optimistically, we would hope that for nonnegative $a_{i}^{\star}$'s the weighted version of $P$ below would also enjoy the similar landscape property When $a_{i}^{\star}$'s are positive, indeed the global minimum of $P'$ are still just all the permutations of the $B^{\star}$.^99^9This is the main reason why we require $a^{\star} \geq 0$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

However, when ${\max a_{i}^{\star}} > {2{\min a_{i}^{\star}}}$, we found that $P'$ starts to have spurious local minima. It seems that spurious local minimum often occurs when a row of $B$ is a linear combination of a smaller number of rows of $B^{\star}$. See Section D for a concrete example.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

To remove such spurious local minima, we add a regularization term below that pushes each row of $B$ to be close to one of the rows of $B^{\star}$, We see that for each fixed $j$, the part in $R{(B)}$ that involves $b_{j}$ has the form This is commonly used objective function for decomposing tensor $\sum_{i}{a_{i}^{\star}b_{i}^{\star {\otimes 4}}}$. It's known that for orthogonal $b_{i}^{\star}$'s, the only local minima are ${\pm b_{1}^{\star}},\ldots,{\pm b_{d}^{\star}}$. Therefore, intuitively $R{(B)}$ pushes each of the $b_{i}$'s towards one of the $b_{i}^{\star}$'s.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

^1010^10However, note that $R{(B)}$ by itself doesn't work because it does not prevent the solutions where all the $b_{i}$'s are equal to the same $b_{j}^{\star}$. Choosing $\mu$ to be small enough, it turns out that ${P'{(B)}} + {R{(B)}}$ doesn't have any spurious local minimum as we will show in Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design").

<!-- chunk {"id": "body-0045", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

Another issue with the choice of ${P'{(B)}} + {R{(B)}}$ is that we are still having a constraint minimization problem. Such row-wise norm constraints only make sense when the ground-truth $B^{\star}$ is orthogonal and thus has unit row norm. A straightforward generalization of $P{(B)}$ to non-orthogonal case requires some special constraints that also depend on the covariance matrix $B^{\star}B_{}^{\star \top}$, which in turn requires a specialized procedure to estimate. Instead, we move the constraints into the objective function by considering adding another regularization term that approximately enforces the constraints.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

It turns out the following regularizer suffices for the orthogonal case, Moreover, we can extend this easily to the non-orthogonal case (see Section A) without estimating any statistics of $B^{\star}$ in advance. We note that $S{(B)}$ is not the Lagrangian multiplier and it does change the global minima slightly. We will take $\lambda$ to be large enough so that $\parallel b_{i}\parallel$ has to be close to 1. As a summary, we finally use the unconstrained objective Since $R{(B)}$ and $S{(B)}$ are degree-4 polynomials of $B$, the analysis of $G{(B)}$ is much more delicate, and we cannot use much linear algebra as we could for $P'{(B)}$. See Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") for details.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Which objective has no spurious local minima?", "weight": 1.0} -->

Finally we note that a feature of this objective $G{( \cdot )}$ is that it only takes $B$ as variables. We will estimate the value of $a^{\star}$ after we recover the value of $B$. (see Section B). ·

<!-- chunk {"id": "body-0048", "role": "body", "section": "Basics on Hermite Polynomials", "weight": 1.0} -->

In this section, we briefly review Hermite polynomials and Fourier analysis on Gaussian space. Let $H_{j}$ be the probabilists' Hermite polynomial, and let $h_{j} = {\frac{1}{\sqrt{j!}}H_{j}}$ be the normalized Hermite polynomials.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Basics on Hermite Polynomials", "weight": 1.0} -->

For two functions $f,g$ that map $\mathbb{R}$ to $\mathbb{R}$, define the inner product $\langle f,g\rangle$ with respect to the Gaussian measure as The polynomials $h_{0},\ldots,h_{m},\ldots$ are orthogonal to each other under this inner product: Here $\delta_{ij} = 1$ if $i = j$ and otherwise $\delta_{ij} = 0$. Given a function $\sigma \in {L^{2}{({\mathbb{R}},e^{- {x^{2}/2}})}}$, let the $k$-th Hermite coefficient of $\sigma$ be defined as Since ${h_{0},\ldots,h_{m},\ldots},$ forms a complete orthonormal basis, we have the expansion that We will leverage several other nice properties of the Hermite polynomials in our proofs.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Basics on Hermite Polynomials", "weight": 1.0} -->

The following claim connects the Hermite polynomial to the coefficients of Taylor expansion of a certain exponential function. It can also serve as a definition of Hermite polynomials.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Claim 4.1 (\\[O'D14, Equation 11.8\\])", "weight": 1.0} -->

We have that for ${t,z} \in {\mathbb{R}}$, The following Claims shows that the expectation $\mathbb{E}\left\lbrack {h_{n}{(x)}h_{m}{(y)}} \right\rbrack$ can be computed easily when $x,y$ are (correlated) Gaussian random variables.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Claim 4.2 (\\[O'D14, Section 11.2\\])", "weight": 1.0} -->

Let $(x,y)$ be $\rho$-correlated standard normal variables (that is, both $x$,$y$ have marginal distribution $\mathcal{N}{}$ and ${\mathbb{E}{\lbrack{xy}\rbrack}} = \rho$). Then, As a direct corollary, we can compute $\mathbb{E}_{x \sim {\mathcal{N}{(0,\text{Id}_{d \times d})}}}\left\lbrack {\sigma{({u^{\top}x})}\gamma{({v^{\top}x})}} \right\rbrack$ by expanding in the Hermite basis and applying the Claim above.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Analytic Formula for population risk $f$ and $f'$", "weight": 1.0} -->

In this section we prove Theorem 2.1 and Theorem 2.2, which both follow from the following more general Theorem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Analytic Formula for population risk $G$", "weight": 1.0} -->

In this section we show that the population risk $G{(\cdot)}$ (defined as in equation (2.8)) has the following analytical formula: The formula will be crucial for the analysis of the landscape of $G{(\cdot)}$ in Section 5 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). The formula follows straightforwardly from the following two theorems and the definition (2.8).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Landscape of Population Risk $G{( \\cdot )}$", "weight": 1.0} -->

In this section we prove Theorem 2.3. Since the landscape property is invariant with respect to rotations of parameters, without loss of generality we assume $B^{\star}$ is the identity matrix Id throughout this section. (See Section A for a precise statement for the invariance.) Recall that by Theorem 2.6, the population risk $G{(\cdot)}$ in the case of $B^{\star} = \text{Id}$ is equal to In the rest of section we work with the formula above for $G{(\cdot)}$ instead of the original definition. In fact, for future reference, we study a more general version of the function $G$. For nonnegative vectors $\alpha,\beta$ and nonnegative number $\mu$, let $G_{\alpha,\beta,\mu}$ be defined as Here $e_{i}$ denotes the $i$-th natural basis vector.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Step 1: Analysis of Local Optimality of a Single Row", "weight": 1.0} -->

The following lemma shows that a local minimum $x$ of the objective $h{( \cdot )}$ must be a scaling of a basis vector. Recall that $|x|_{\text{2nd}}$ denotes the second largest absolute value of the entries of $x$. The lemma deals generally an approximate local minimum, though we suggest casual readers simply think of ${\varepsilon,\tau} = 0$ in the lemma.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Local Optimality of All the Variables", "weight": 1.0} -->

In this section we prove Theorem 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design"). Results in Subsection 5.1 ‣ Learning One-hidden-layer Neural Networks with Landscape Design") have established that if $B$ is a local minimum, then each row $b_{s}$ of $B$ has to be a scaling of a basis vector. In this section we show that these basis vectors need to be distinct from each other. The following proposition summaries such a claim (with a weak error analysis).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulation", "weight": 1.0} -->

In this section, we provide simple simulation results that verify that minimizing $G{(B)}$ with SGD recovers a permutation of $B^{\star}$; however, minimizing Equation (2.2) with SGD results in finding spurious local minima. Based on the formula for the population risk in Equation (2.3), we also verified empirically the conjecture that SGD would successfully recover $B^{\star}$ using the activation functions ${\gamma{(z)}} = {{{\hat{\sigma}}_{2}h_{2}{(z)}} + {{\hat{\sigma}}_{4}h_{4}{(z)}}}$,^1212^12We also observed that using ${\gamma{(z)}} = {\frac{1}{2}{|z|}}$ also works but due to the space limitation we don't report the experimental results here. even if the data were generated via a model with ReLU activation.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Simulation", "weight": 1.0} -->

(See Section 2.1 for the rationale behind such conjectures.)

<!-- chunk {"id": "body-0060", "role": "body", "section": "Simulation", "weight": 1.0} -->

For all of our experiments, we chose $B^{\star} = \text{Id}_{d \times d}$ with dimension $d = 50$ and $a^{\star} = \mathbf{1}$ for simplicity, and the data is generated from a one-hidden-layer network with ReLU activation without noise. We use stochastic gradient descent with fresh samples at each iteration, and we plot the (expected) population error (that is, the error on a fresh batch of examples).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Simulation", "weight": 1.0} -->

To test whether SGD converges to a matrix $B$ which is equivalent to $B^{\star}$ up to permutation of rows, we use a surrogate error metric to evaluate whether $B_{}^{\star {- 1}}B$ is close to a permutation matrix. Given a matrix $Q$ with row norm 1, let Then we have that if ${e{(Q)}} \leq \varepsilon$ for some $\varepsilon < {1/3}$, then it implies that $Q$ is $\sqrt{2\varepsilon}$-close to a permutation matrix in infinity norm. On the other direction, we know that if ${e{(Q)}} > \varepsilon$, then $Q$ is not $\varepsilon$-close to any permutation matrix in infinity norm. The latter statement also holds when $Q$ doesn't have row norm $1$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Simulation", "weight": 1.0} -->

Finally we note that using the loss function $G{( \cdot )}$ seems to require significantly larger batch (and sample complexity) to reduce the variance in the gradients estimation. We used batch size 262144 in the experiment for $G{( \cdot )}$. However, in contrast, for the ${{\hat{\sigma}}_{2}h_{2}} + {\hat{\sigma_{4}}h_{4}}$ we used batch size 8192 and for relu we used batch size 256.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we first give an analytic formula for the population risk of the standard $\ell_{2}$ loss, which empirically may converge to a spurious local minimum. We then design a novel population loss that is guaranteed to have no spurious local minimum.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Designing objective functions with well-behaved landscape is an intriguing and fruitful direction. We hope that our techniques can be useful for characterizing and designing the optimization landscape for other settings.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conjecture that the objective ${\alphaf_{2}} + {\betaf_{4}}$ has no spurious local minimum when $\alpha,\beta$ are reasonable constants and the ground-truth parameters are in general position^1313^13See equation (2.4) for the definition of $f_{k}$ and Theorem 2.2 for how to access ${\alphaf_{2}} + {\betaf_{4}}$ in the setting of one-hidden-layer neural nets.. We provided empirical evidence to support the conjecture.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our results assume that the input distribution is Gaussian. Extending them to other input distributions is a very interesting open problem.
