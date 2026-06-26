<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Hessian of Tall-skinny Networks Is Easy to Invert

Topics include Linear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe an exact algorithm to solve linear systems of the form Hx = b where H is the Hessian of a deep net. The method computes Hessian-inverse-vector products without storing the Hessian or its inverse. It requires time and storage that scale linearly in the number of layers. This is in contrast to the naive approach of first computing the Hessian, then solving the linear system, which takes storage and time that are respectively quadratic and cubic in the number of layers. The Hessian-inverse-vector product method scales roughly like Pearlmutter's algorithm for computing Hessian-vector products.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Hessian of a deep net is the matrix of second-order mixed partial derivatives of its loss with respect to its parameters. Decades ago, when deep nets had only hundreds or thousands of parameters, the Hessian matrix could be inverted to implement optimizers that converged much faster than gradient descent. But for large modern deep nets, relying on the Hessian has become impractical: The Hessian of a model with a billion parameters would have a quintillion entries, which is far larger than can be stored, multiplied, or inverted even in the largest data centers. A common workaround is to approximate the Hessian as a low-rank matrix or as a diagonal matrix. Such approximations make it easier to apply the inverse of the Hessian to a vector. This article shows how to compute and apply the inverse of the Hessian exactly without storing the Hessian or its inverse. The Hessian-inverse-vector product can be computed in time and storage that scale linearly with the number of layers in the model, and cubically in the number of parameters and activations in each layer.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pearlmutter showed how to compute the product of the Hessian with a fixed vector (the so-called Hessian-vector product) in time and storage that scale linearly with the number of layers in the network. This is much faster than the cubic scaling of the naive algorithm that first computes the Hessian matrix and then multiplies it by the vector. His method transforms the original network into a new network whose gradient is the desired Hessian-vector product. To compute the Hessian-vector product, one then just applies backpropagation to the new network. Given a way to compute the Hessian-vector product, one can indirectly compute the Hessian-inverse-vector product via, say Krylov iterations like Conjugate Gradient as proposed by Pearlmutter and more recently re-investigated. However, the quality of the result would then depend on the conditioning of the Hessian, which is notoriously poor for deep nets. Unfortunately, there seems to exist no variant of Pearlmutter's trick to compute the Hessian-inverse-vector products directly.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed Hessian-inverse-vector product algorithm takes advantage of a deep net's layerwise structure. Regardless of the specific operations in each layer, the Hessian is a second order matrix polynomial that involves the first order and second order mixed derivatives of each layer, and the inverse of a block bi-diagonal operator that represents the backpropagation algorithm. Multiplying a vector by this structure computes the Hessian-vector product using exactly the same operations as Pearlmutter's algorithm (see Appendix B is Pearlmutter’s Hessian-vector multiplication algorithm ‣ The Hessian of tall-skinny networks is easy to invert")). It also leads to a way to compute Hessian-inverse-vector product that does not require forming or storing the full Hessian. To formally characterize the storage and running time of the algorithm, assume an oracle that offers the first order and second order mixed derivatives of each layer.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For an $L$-layer deep net where each layer has at most $p$ parameters and generates at most $a$ activations, naively storing the Hessian would require $O(L^{2}p^{2})$ memory, and solving a linear system would require $O\left(L^{3}p^{3}\right)$ operations in addition to the oracle queries. In contrast, we will show how to perform these operations using only $O(L\max(a,p)^{2})$ storage and $O(L\max(a,p)^{3})$ computation in addition to the oracle queries. The dependence on the number of activations and parameters in each layer remains cubic, but the dependence on the number of layers is only linear. This makes operating on the Hessian of tall and skinny networks more efficient than the Hessian of short and fat networks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although modern networks are typically short and wide, our method runs faster than the naive Hessian-inverse-vector product algorithm on tall and skinny networks, since it ameliorates the naive algorithm's cubic dependence on depth to a mild linear dependence on depth. A follow-up article will explore training tall-skinny networks using the Hessian-inverse-vector product as a preconditioner. We expect that a significant training speedup will motivate a return to deeper network designs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Overview", "weight": 1.0} -->

Our objective is to efficiently solve linear systems of the form $Hx=b$, where $H$ is the Hessian of a deep neural network, without forming $H$ explicitly. To do this, we employ the following strategy: Write down the gradient of the deep net in matrix form, as a block bi-diagonal system of linear equations. Solving this system uses back-substitution, which in this case coincides exactly with the computations carried out by backpropagation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Overview", "weight": 1.0} -->

Differentiate this matrix form to obtain an expression for the Hessian. This expression involves a second-order polynomial in the inverse of the aforementioned block bi-diagonal matrix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Overview", "weight": 1.0} -->

Refactor the expression wit hthe help of auxiliarry variables. These lift the polynomial into a higher-dimensional linear form. After pivoting, this linear form becomes block tri-diagonal.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Overview", "weight": 1.0} -->

Factorize the resulting block-tri-diagonal into a lower block bi-diagonal matrix, a block diagonal matrix, and an upper block diagonal matrix using the LDU factorization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overview", "weight": 1.0} -->

Solve the resulting system using forward and backward substitution. This is similar to running backpropagation on a modified version of the original network that's designed to compute the Hessian-inverse-vector product.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview", "weight": 1.0} -->

Un-pivot the result, and report the un-lifted solution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview", "weight": 1.0} -->

Algorithm 1 summarizes the steps above.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview", "weight": 1.0} -->

1:A vector b, damping constant ϵ. 3:Define the sparse block matrix 𝒦 and the augmented system as in Equation 13. 4:Pivot into permuted system 𝒦′x′ = b′ where 𝒦′ = Π𝒦Π⊤ is block-tri-diagonal following Equation. 5:Solve 𝒦′x′ = b′ using block-LDU decomposition. 6:Recover the solution x from the permuted vector $\Pi\left[\begin{smallmatrix}x\\z\end{smallmatrix}^{\prime}\right]$. Algorithm 1 Compute the hessian-inverse-vector product by solving (H + ϵI)x = b.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overview", "weight": 1.0} -->

The algorithm is straightforward to implement with a suitable library of block matrix operations.^11^1

<!-- chunk {"id": "body-0017", "role": "body", "section": "Backpropagation, the matrix way", "weight": 1.0} -->

We would like to fit the vector of parameters $x=(x_{1},\ldots,x_{L})$ given a training dataset, which we represent by a stochastic input $z_{0}$ to the pipeline. Training the model proceeds by gradient descent steps along the stochastic gradient $\partial z_{L}(z_{0};x)/\partial x$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Backpropagation, the matrix way", "weight": 1.0} -->

The components of this direction can be computed by the chain rule with a backward recursion: The identification $b_{\ell}\equiv\frac{\partial z_{L}}{\partial z_{\ell}}$, $\nabla_{x}f_{\ell}\equiv\frac{\partial z_{\ell}}{\partial x_{\ell}}$, and $\nabla_{z}f_{\ell}\equiv\frac{\partial z_{\ell}}{\partial z_{\ell-1}}$ turns this recurrence into with the base case $b_{L}=1$, a scalar. These two equations can be written in vector form as Solving for $b$ and substituting back gives The matrix $M$ is block bi-diagonal. Its diagonal entries are identity matrices, and its off-diagonal matrices are the gradient of the intermediate activations with respect to the layer's parameters.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Backpropagation, the matrix way", "weight": 1.0} -->

The matrix $D_{x}$ is block diagonal, with the block as the derivative of each layer's activations with respect to its inputs. $M$ is invertible because the spectrum of a triangular matrix can be read off its diagonal, which in this case is all ones.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Hessian", "weight": 1.0} -->

To obtain the Hessian, we use similar techniques to compute the gradient of Equation with respect to $x$. The gradient we computed in Equation is the unique vector $g$ such that $dz_{L}\equiv z_{L}(x+dx)-z_{L}(dx)\to g(x)^{\top}dx$ as $dx\to 0$. Similarly, the Hessian $H$ of $z_{L}$ with respect to the parameters is the unique matrix $H(x)$ such that $dg\equiv g(x+dx)-g(x)\to H(x)\;dx$ as $dx\to 0$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Claim 1", "weight": 1.0} -->

The Hessian of the loss $z_{L}$ with respect to the vector of parameters $x$ is given by with the following matrices: Given a vector $x\in\mathop{\mathbb{R}}^{Lp}$, the formula above allows us to compute $Hx$ in $O\left(Lap^{2}+La^{2}p+La^{3}\right)$ operations without forming $H$. This cost is dominated by multiplying by the $D_{xx}$, $D_{zx}$, and $D_{zz}$ matrices. Appendix B is Pearlmutter’s Hessian-vector multiplication algorithm ‣ The Hessian of tall-skinny networks is easy to invert") shows that these operations are exactly the operations performed in Pearlmutter's trick to compute the Hessian-vector product.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Claim 1", "weight": 1.0} -->

To solve systems of the form $Hx=b$, one could use Krylov methods to repeatedly multiply by $H$ without forming $H$ (a possibility Pearlmutter considered ). This would require applying $H$ some number of times that depends on the condition number of $H$. However, the next section shows how to solve systems of the form $H^{-1}x=b$ with only $\max(a,p)$ times more operations than are needed to compute $Hx$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Applying the inverse of the Hessian", "weight": 1.0} -->

The above shows that the Hessian is a second order matrix polynomial in $M^{-1}$. While $M$ itself is block-bidiagonal, $M^{-1}$ is dense, so $H$ is dense. Nevertheless, this polynomial can be lifted into a higher order object whose inverse is easy to compute: In general, $H$ is singular. We wish to solve the system $(H+\epsilon I)x=g$ for $x$. We can convert this dense system involving inverses into a larger, sparse system by introducing auxiliary variables. Define which implies $My-D_{x}x=0$. Define a second auxiliary variable which implies $M^{\top}z-P^{\top}D_{M}D_{xz}x-P^{\top}D_{M}D_{zz}Py=0$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Applying the inverse of the Hessian", "weight": 1.0} -->

With these substitutions, $(H+\epsilon I)x=g$ becomes Collecting these three linear equations gives us a unified system Finding $x=\left(H+\epsilon I\right)^{-1}g$ is equivalent to solving this block-linear system and reporting the resulting $x$. The benefit of doing this is that this system can be pivoted into a block-tri-diagonal system, which can be solved more efficiently than Gaussian elimination on $\mathcal{K}$ or $H$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Applying the inverse of the Hessian", "weight": 1.0} -->

The pivoting we'll apply reorders the blocks of the variables $x,y,z$ from $x_{1},\ldots,x_{L},y_{1},\ldots,y_{L},z_{1},\ldots,z_{L}$ to $x_{1},y_{1},z_{1},\dots,x_{L},y_{L},z_{L}$. This pivoting operation acts as a kind of transpose operation on block matrices (its generalization is called a "commutation matrix" in ). When applied to $\mathcal{K}$, it turns it into a block-tri-diagonal matrix. To get a better feel for this operation, denote the $ij$th block of $\mathcal{K}$ by $\mathcal{K}_{ij}$ and the $uv$th sub-block of this block by $\mathcal{K}_{ij,uv}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Applying the inverse of the Hessian", "weight": 1.0} -->

Similarly, $x$ denote a vector conformant with $\mathcal{K}$, with $x_{j}$ denoting the column vector that multiplies each block $\mathcal{K}_{\cdot j}$ and denote the $v$th sub-block of $x_{j}$ by $x_{jv}$, which multiplies $\mathcal{K}_{\cdot j,\cdot v}$. We say that $x$ is $j$-major because as we traverse the entries of $x$ from top to bottom, the index $j$ increments more slowly than the $v$ index.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Applying the inverse of the Hessian", "weight": 1.0} -->

Denote by $\Pi$ the permutation that transposes the blocks with the sub-blocks. Applying this permutation matrix $\Pi$ to $x$ reorders it from $j$-major to $d$-major. Applying it to the rows and columns of $\mathcal{K}$ results in a block matrix $\mathcal{K}^{\prime}\equiv\Pi\mathcal{K}\Pi^{\top}$ that satisfies $\mathcal{K}_{ij,uv}=\mathcal{K}^{\prime}_{uv,ij}$. Section C illustrates this operator with some examples.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Observation 2", "weight": 1.0} -->

When the blocks of $\mathcal{K}$ are banded with bandwidth $w$, $\mathcal{K}^{\prime}$ is block-banded with bandwidth $w$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Observation 2", "weight": 1.0} -->

The blocks in $\mathcal{K}$ are either block-diagonal, block-upper-bi-diagonal, or block-lower-bi-diagonal, so $\mathcal{K}^{\prime}$ is at most block-tri-diagonal.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Observation 2", "weight": 1.0} -->

Denote the $ij$th block of $\mathcal{K}^{\prime}$ as $B_{ij}$: Then $\mathcal{K}^{\prime}$ can be written as the block-tri-diagonal matrix That means we can solve the system $\mathcal{K}^{\prime}x^{\prime}=b^{\prime}$ by first decomposing $\mathcal{K}^{\prime}$ via block LDU decomposition into the product of a lower-block-bi-diagonal matrix, a block-diagonal matrix, and an upper-block-bi-diagonal matrix as $LDUx^{\prime}=b^{\prime}$, then solve for $Ly=b^{\prime}$ using back substitution, and finally solve for $DUx^{\prime}=y$ using forward substitution. Because these systems are block-bi-diagonal, solving them looks like forward and backward propagation on a chain. The running time for these solvers is linear in the depth of the network and cubic in the dimension of each block $B_{ij}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Observation 2", "weight": 1.0} -->

Depending on the block, the dimension of each of these blocks is either in the number of parameters or the number of activations in the corresponding layer. In all,assuming $a$ and $p$ are the largest activation and parameter count for a layer, the running time for solving this system is $O\left(L\max(a,p)^{3}\right)$ operations.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have described a method to compute the product of the inverse Hessian of a deep neural network with a vector. Compared to the naive method, which stores the Hessian and requires computation cubic in the depth of the network, this method does not store the Hessian and requires computation linear in the depth of the network.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In its final stage, the method relies on a forward and backward substitution to solve a block tridiagonal system. This step bears a similarity to Pearlmutter's method for computing the Hessian-vector product: It can be interpreted as running backpropagation on a modified version of the original network whose gradient is the desired Hessian-inverse-vector product. The downside of this similarity is that solving large linear systems with LDU factorization is prone to numerical instability. An improvement on the proposal is to solve the block tridiagonal system with an off-the-shelf banded solver.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our hope is to use this technique as a preconditioner to speed up stochastic gradient descent. Since the method's speedup is greatest when the network is tall and skinny, we hope it might rekindle interest in extremely deep architectures.
