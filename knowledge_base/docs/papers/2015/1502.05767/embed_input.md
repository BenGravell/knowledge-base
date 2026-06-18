<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Automatic Differentiation in Machine Learning: A Survey

Topics include Graphs, Optimization, Learning, Automatic differentiation, Differentiable programming, Machine learning, CLARITY.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Derivatives, mostly in the form of gradients and Hessians, are ubiquitous in machine learning. Automatic differentiation (AD), also called algorithmic differentiation or simply "autodiff", is a family of techniques similar to but more general than backpropagation for efficiently and accurately evaluating derivatives of numeric functions expressed as computer programs. AD is a small but established field with applications in areas including computational fluid dynamics, atmospheric sciences, and engineering design optimization. Until very recently, the fields of machine learning and AD have largely been unaware of each other and, in some cases, have independently discovered each other's results. Despite its relevance, general-purpose AD has been missing from the machine learning toolbox, a situation slowly changing with its ongoing adoption under the names "dynamic computational graphs" and "differentiable programming". We survey the intersection of AD and machine learning, cover applications where AD has direct relevance, and address the main implementation techniques. By precisely defining the main differentiation techniques and their interrelationships, we aim to bring clarity to the usage of the terms "autodiff", "automatic differentiation", and "symbolic differentiation" as these are encountered more and more in machine learning settings.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Methods for the computation of derivatives in computer programs can be classified into four categories: manually working out derivatives and coding them; *numerical differentiation*using finite difference approximations; *symbolic differentiation*using expression manipulation in computer algebra systems such as Mathematica, Maxima, and Maple; and *automatic differentiation*, also called *algorithmic differentiation*, which is the subject matter of this paper.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Conventionally, many methods in machine learning have required the evaluation of derivatives and most of the traditional learning algorithms have relied on the computation of gradients and Hessians of an objective function. When introducing new models, machine learning researchers have spent considerable effort on the manual derivation of analytical derivatives to subsequently plug these into standard optimization procedures such as L-BFGS or stochastic gradient descent. Manual differentiation is time consuming and prone to error. Of the other alternatives, numerical differentiation is simple to implement but can be highly inaccurate due to round-off and truncation errors; more importantly, it scales poorly for gradients, rendering it inappropriate for machine learning where gradients with respect to millions of parameters are commonly needed. Symbolic differentiation addresses the weaknesses of both the manual and numerical methods, but often results in complex and cryptic expressions plagued with the problem of "expression swell". Furthermore, manual and symbolic methods require models to be defined as closed-form expressions, ruling out or severely limiting algorithmic control flow and expressivity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are concerned with the powerful fourth technique, automatic differentiation (AD). AD performs a non-standard interpretation of a given computer program by replacing the domain of the variables to incorporate derivative values and redefining the semantics of the operators to propagate derivatives per the chain rule of differential calculus. Despite its widespread use in other fields, general-purpose AD has been underused by the machine learning community until very recently.^11^1See, e.g., [ Following the emergence of deep learning as the state-of-the-art in many machine learning tasks and the modern workflow based on rapid prototyping and code reuse in frameworks such as Theano, Torch, and TensorFlow, the situation is slowly changing where projects such as autograd^22^2 Chainer^33^3 and PyTorch^44^4 are leading the way in bringing general-purpose AD to the mainstream.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The term "automatic" in AD can be a source of confusion, causing machine learning practitioners to put the label "automatic differentiation", or just "autodiff", on any method or tool that does not involve manual differentiation, without giving due attention to the underlying mechanism. We would like to stress that AD as a technical term refers to a specific family of techniques that compute derivatives through accumulation of values during code execution to generate numerical derivative evaluations rather than derivative expressions. This allows accurate evaluation of derivatives at machine precision with only a small constant factor of overhead and ideal asymptotic efficiency. In contrast with the effort involved in arranging code as closed-form expressions under the syntactic and semantic constraints of symbolic differentiation, AD can be applied to regular code with minimal change, allowing branching, loops, and recursion. Because of this generality, AD has been applied to computer simulations in industry and academia and found applications in fields including engineering design optimization, computational fluid dynamics, physical modeling, optimal control, structural mechanics, atmospheric sciences, and computational finance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In machine learning, a specialized counterpart of AD known as the backpropagation algorithm has been the mainstay for training neural networks, with a colorful history of having been reinvented at various times by independent researchers. It has been one of the most studied and used training algorithms since the day it became popular mainly through the work of Rumelhart et al.. In simplest terms, backpropagation models learning as gradient descent in neural network weight space, looking for the minima of an objective function. The required gradient is obtained by the backward propagation of the sensitivity of the objective value at the output (Figure 1), utilizing the chain rule to compute partial derivatives of the objective with respect to each weight. The resulting algorithm is essentially equivalent to transforming the network evaluation function composed with the objective function under reverse mode AD, which, as we shall see, actually generalizes the backpropagation idea. Thus, a modest understanding of the mathematics underlying backpropagation provides one with sufficient background for grasping AD techniques.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we review AD from a machine learning perspective, covering its origins, applications in machine learning, and methods of implementation. Along the way, we also aim to dispel some misconceptions that we believe have impeded wider recognition of AD by the machine learning community. In Section 2 we start by explicating how AD differs from numerical and symbolic differentiation. Section 3 gives an introduction to the AD technique and its forward and reverse accumulation modes. Section 4 discusses the role of derivatives in machine learning and examines cases where AD has relevance. Section 5 covers various implementation approaches and general-purpose AD tools, followed by Section 6 where we discuss future directions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "What AD Is Not", "weight": 1.0} -->

Without proper introduction, one might assume that AD is either a type of numerical or symbolic differentiation. Confusion can arise because AD does in fact provide numerical values of derivatives (as opposed to derivative expressions) and it does so by using symbolic rules of differentiation (but keeping track of derivative values as opposed to the resulting expressions), giving it a two-sided nature that is partly symbolic and partly numerical. We start by emphasizing how AD is different, and in several aspects superior to, these two commonly encountered techniques of computing derivatives.

<!-- chunk {"id": "body-0010", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

Numerical differentiation is the finite difference approximation of derivatives using values of the original function evaluated at some sample points (Figure 2, lower right). In its simplest form, it is based on the limit definition of a derivative. For example, for a multivariate function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, one can approximate the gradient ${\nabla f} = \left( \frac{\partial f}{\partial x_{1}},\ldots,\frac{\partial f}{\partial x_{n}} \right)$ using

<!-- chunk {"id": "body-0011", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

where $\mathbf{e}_{i}$ is the $i$-th unit vector and $h > 0$ is a small step size. This has the advantage of being uncomplicated to implement, but the disadvantages of performing $O{(n)}$ evaluations of $f$ for a gradient in $n$ dimensions and requiring careful consideration in selecting the step size $h$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

Numerical approximations of derivatives are inherently ill-conditioned and unstable,^55^5Using the limit definition of the derivative for finite difference approximation commits both cardinal sins of numerical analysis: *"thou shalt not add small numbers to big numbers"*, and *"thou shalt not subtract numbers which are approximately equal"*. with the exception of complex variable methods that are applicable to a limited set of holomorphic functions. This is due to the introduction of truncation^66^6Truncation error is the error of approximation, or inaccuracy, one gets from $h$ not actually being zero. It is proportional to a power of $h$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

and round-off^77^7Round-off error is the inaccuracy one gets from valuable low-order bits of the final answer having to compete for machine-word space with high-order bits of $f{({\mathbf{x} + {h\mathbf{e}_{i}}})}$ and $f{(\mathbf{x})}$ (Eq. 1), which the computer has to store just until they cancel in the subtraction at the end. Round-off error is inversely proportional to a power of $h$. errors inflicted by the limited precision of computations and the chosen value of the step size $h$. Truncation error tends to zero as $h\rightarrow 0$. However, as $h$ is decreased, round-off error increases and becomes dominant (Figure 3).

<!-- chunk {"id": "body-0014", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

Various techniques have been developed to mitigate approximation errors in numerical differentiation, such as using a center difference approximation

<!-- chunk {"id": "body-0015", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

where the first-order errors cancel and one effectively moves the truncation error from first-order to second-order in $h$.^88^8This does not avoid either of the cardinal sins, and is still highly inaccurate due to truncation. For the one-dimensional case, it is just as costly to compute the forward difference (Eq. 1) and the center difference (Eq. 2), requiring only two evaluations of $f$. However, with increasing dimensionality, a trade-off between accuracy and performance is faced, where computing a Jacobian matrix of a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ requires $2mn$ evaluations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

Other techniques for improving numerical differentiation, including higher-order finite differences, Richardson extrapolation to the limit, and differential quadrature methods using weighted sums, have increased computational complexity, do not completely eliminate approximation errors, and remain highly susceptible to floating point truncation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "AD Is Not Numerical Differentiation", "weight": 1.0} -->

The $O{(n)}$ complexity of numerical differentiation for a gradient in $n$ dimensions is the main obstacle to its usefulness in machine learning, where $n$ can be as large as millions or billions in state-of-the-art deep learning models. In contrast, approximation errors would be tolerated in a deep learning setting thanks to the well-documented error resiliency of neural network architectures.

<!-- chunk {"id": "body-0018", "role": "body", "section": "AD Is Not Symbolic Differentiation", "weight": 1.0} -->

Symbolic differentiation is the automatic manipulation of expressions for obtaining derivative expressions (Figure 2, center right), carried out by applying transformations representing rules of differentiation such as

<!-- chunk {"id": "body-0019", "role": "body", "section": "AD Is Not Symbolic Differentiation", "weight": 1.0} -->

When formulae are represented as data structures, symbolically differentiating an expression tree is a perfectly mechanistic process, considered subject to mechanical automation even at the very inception of calculus (Leibniz, 1685). This is realized in modern computer algebra systems such as Mathematica, Maxima, and Maple and machine learning frameworks such as Theano.

<!-- chunk {"id": "body-0020", "role": "body", "section": "AD Is Not Symbolic Differentiation", "weight": 1.0} -->

In optimization, symbolic derivatives can give valuable insight into the structure of the problem domain and, in some cases, produce analytical solutions of extrema (e.g., solving for ${\frac{d}{dx}f{(x)}} = 0$) that can eliminate the need for derivative calculation altogether. On the other hand, symbolic derivatives do not lend themselves to efficient runtime calculation of derivative values, as they can get exponentially larger than the expression whose derivative they represent.

<!-- chunk {"id": "body-0021", "role": "body", "section": "AD Is Not Symbolic Differentiation", "weight": 1.0} -->

Consider a function ${h{(x)}} = {f{(x)}g{(x)}}$ and the multiplication rule in Eq. 3. Since $h$ is a product, $h{(x)}$ and $\frac{d}{dx}h{(x)}$ have some common components, namely $f{(x)}$ and $g{(x)}$. Note also that on the right hand side, $f{(x)}$ and $\frac{d}{dx}f{(x)}$ appear separately. If we just proceeded to symbolically differentiate $f{(x)}$ and plugged its derivative into the appropriate place, we would have nested duplications of any computation that appears in common between $f{(x)}$ and $\frac{d}{dx}f{(x)}$. Hence, careless symbolic differentiation can easily produce exponentially large symbolic expressions which take correspondingly long to evaluate. This problem is known as *expression swell* (Table 1).

<!-- chunk {"id": "body-0022", "role": "body", "section": "AD Is Not Symbolic Differentiation", "weight": 1.0} -->

When we are concerned with the accurate numerical evaluation of derivatives and not so much with their actual symbolic form, it is in principle possible to significantly simplify computations by storing only the values of intermediate sub-expressions in memory. Moreover, for further efficiency, we can interleave as much as possible the differentiation and simplification steps. This interleaving idea forms the basis of AD and provides an account of its simplest form: *apply symbolic differentiation at the elementary operation level and keep intermediate numerical results, in lockstep with the evaluation of the main function.* This is AD in the forward accumulation mode, which we shall introduce in the following section.

<!-- chunk {"id": "body-0023", "role": "body", "section": "AD and Its Main Modes", "weight": 1.0} -->

AD can be thought of as performing a non-standard interpretation of a computer program where this interpretation involves augmenting the standard computation with the calculation of various derivatives. All numerical computations are ultimately compositions of a finite set of elementary operations for which derivatives are known, and combining the derivatives of the constituent operations through the chain rule gives the derivative of the overall composition. Usually these elementary operations include the binary arithmetic operations, the unary sign switch, and transcendental functions such as the exponential, the logarithm, and the trigonometric functions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "AD and Its Main Modes", "weight": 1.0} -->

On the left hand side of Table 2 we see the representation of the computation $y = {f{(x_{1},x_{2})}} = {{{\ln{(x_{1})}} + {x_{1}x_{2}}} - {\sin{(x_{2})}}}$ as an *evaluation trace* of elementary operations---also called a Wengert list. We adopt the three-part notation used by Griewank and Walther, where a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ is constructed using intermediate variables $v_{i}$ such that

<!-- chunk {"id": "body-0025", "role": "body", "section": "AD and Its Main Modes", "weight": 1.0} -->

variables ${v_{i}i} = {1,\ldots,l}$ are the working (intermediate) variables, and

<!-- chunk {"id": "body-0026", "role": "body", "section": "AD and Its Main Modes", "weight": 1.0} -->

Evaluation traces form the basis of the AD techniques. An important point to note here is that AD can differentiate not only closed-form expressions in the classical sense, but also algorithms making use of control flow such as branching, loops, recursion, and procedure calls, giving it an important advantage over symbolic differentiation which severely limits such expressivity. This is thanks to the fact that any numeric code will eventually result in a numeric evaluation trace with particular values of the input, intermediate, and output variables, which are the only things one needs to know for computing derivatives using chain rule composition, regardless of the specific control flow path that was taken during execution. Another way of expressing this is that AD is blind with respect to any operation, including control flow statements, which do not directly alter numeric values.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

AD in forward accumulation mode^99^9Also called *tangent linear* mode. is the conceptually most simple type. Consider the evaluation trace of the function ${f{(x_{1},x_{2})}} = {{{\ln{(x_{1})}} + {x_{1}x_{2}}} - {\sin{(x_{2})}}}$ given on the left-hand side in Table 2 and in graph form in Figure 4. For computing the derivative of $f$ with respect to $x_{1}$, we start by associating with each intermediate variable $v_{i}$ a derivative

<!-- chunk {"id": "body-0028", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

Applying the chain rule to each elementary operation in the forward primal trace, we generate the corresponding tangent (derivative) trace, given on the right-hand side in Table 2. Evaluating the primals $v_{i}$ in lockstep with their corresponding tangents ${\overset{˙}{v}}_{i}$ gives us the required derivative in the final variable ${\overset{˙}{v}}_{5} = \frac{\partial y}{\partial x_{1}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

This generalizes naturally to computing the Jacobian of a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ with $n$ independent (input) variables $x_{i}$ and $m$ dependent (output) variables $y_{j}$. In this case, each forward pass of AD is initialized by setting only one of the variables ${\overset{˙}{x}}_{i} = 1$ and setting the rest to zero (in other words, setting $\overset{˙}{\mathbf{x}} = \mathbf{e}_{i}$, where $\mathbf{e}_{i}$ is the $i$-th unit vector). A run of the code with specific input values $\mathbf{x} = \mathbf{a}$ then computes

<!-- chunk {"id": "body-0030", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

giving us one column of the Jacobian matrix

<!-- chunk {"id": "body-0031", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

evaluated at point $\mathbf{a}$. Thus, the full Jacobian can be computed in $n$ evaluations.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

Furthermore, forward mode AD provides a very efficient and matrix-free way of computing Jacobian--vector products

<!-- chunk {"id": "body-0033", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

simply by initializing with $\overset{˙}{\mathbf{x}} = \mathbf{r}$. Thus, we can compute the Jacobian--vector product in just one forward pass. As a special case, when $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, we can obtain the directional derivative along a given vector $\mathbf{r}$ as a linear combination of the partial derivatives

<!-- chunk {"id": "body-0034", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

by starting the AD computation with the values $\overset{˙}{\mathbf{x}} = \mathbf{r}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

Forward mode AD is efficient and straightforward for functions $f:{{\mathbb{R}}\rightarrow{\mathbb{R}}^{m}}$, as all the derivatives $\frac{dy_{i}}{dx}$ can be computed with just one forward pass. Conversely, in the other extreme of $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, forward mode AD requires $n$ evaluations to compute the gradient

<!-- chunk {"id": "body-0036", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

which also corresponds to a $1 \times n$ Jacobian matrix that is built one column at a time with the forward mode in $n$ evaluations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Forward Mode", "weight": 1.0} -->

In general, for cases $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ where $n \gg m$, a different technique is often preferred. We will describe AD in *reverse accumulation mode* in Section 3.2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

Mathematically, forward mode AD (represented by the left- and right-hand sides in Table 2) can be viewed as evaluating a function using dual numbers,^1010^10First introduced by Clifford, with important uses in linear algebra and physics. which can be defined as truncated Taylor series of the form

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

where ${v,\overset{˙}{v}} \in {\mathbb{R}}$ and $\epsilon$ is a nilpotent number such that $\epsilon^{2} = 0$ and $\epsilon \neq 0$. Observe, for example, that

<!-- chunk {"id": "body-0040", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

in which the coefficients of $\epsilon$ conveniently mirror symbolic differentiation rules (e.g., Eq. 3). We can utilize this by setting up a regime where

<!-- chunk {"id": "body-0041", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

and using dual numbers as data structures for carrying the tangent value together with the primal.^1111^11Just as the complex number written $x + {yi}$ is represented in the computer as a pair in memory $(x,y)$ whose two slots are reals, the dual number written $x + {\overset{˙}{x}\epsilon}$ is represented as the pair $(x,\overset{˙}{x})$. Such pairs are sometimes called Argand pairs (Hamilton, 1837, p107 Eqs. and ). The chain rule works as expected on this representation: two applications of Eq. 5 give

<!-- chunk {"id": "body-0042", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

The coefficient of $\epsilon$ on the right-hand side is exactly the derivative of the composition of $f$ and $g$. This means that since we implement elementary operations to respect the invariant Eq. 5, all compositions of them will also do so.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

This also extends to arbitrary program constructs, since dual numbers, as data types, can be contained in any data structure. As long as a dual number remains in a data structure with no arithmetic operations being performed on it, it will just remain a dual number; and if it is taken out of the data structure and operated on again, then the differentiation will continue.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Dual Numbers", "weight": 1.0} -->

In practice, a function $f$ coded in a programming language of choice would be fed into an AD tool, which would then augment it with corresponding extra code to handle the dual operations so that the function and its derivative are simultaneously computed. This can be implemented through calls to a specific library, in the form of source code transformation where a given source code will be automatically modified, or through operator overloading, making the process transparent to the user. We discuss these implementation techniques in Section 5.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

AD in the reverse accumulation mode^1212^12Also called *adjoint* or *cotangent linear* mode. corresponds to a generalized backpropagation algorithm, in that it propagates derivatives backward from a given output. This is done by complementing each intermediate variable $v_{i}$ with an adjoint

<!-- chunk {"id": "body-0046", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

which represents the sensitivity of a considered output $y_{j}$ with respect to changes in $v_{i}$. In the case of backpropagation, $y$ would be a scalar corresponding to the error $E$ (Figure 1).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

In reverse mode AD, derivatives are computed in the second phase of a two-phase process. In the first phase, the original function code is run *forward*, populating intermediate variables $v_{i}$ and recording the dependencies in the computational graph through a bookkeeping procedure. In the second phase, derivatives are calculated by propagating adjoints ${\overline{v}}_{i}$ in *reverse*, from the outputs to the inputs.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

Returning to the example $y = {f{(x_{1},x_{2})}} = {{{\ln{(x_{1})}} + {x_{1}x_{2}}} - {\sin{(x_{2})}}}$, in Table 3 we see the adjoint statements on the right-hand side, corresponding to each original elementary operation on the left-hand side. In simple terms, we are interested in computing the contribution ${\overline{v}}_{i} = \frac{\partial y}{\partial v_{i}}$ of the change in each variable $v_{i}$ to the change in the output $y$. Taking the variable $v_{0}$ as an example, we see in Figure 4 that the only way it can affect $y$ is through affecting $v_{2}$ and $v_{3}$, so its contribution to the change in $y$ is given by

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

In Table 3, this contribution is computed in two incremental steps

<!-- chunk {"id": "body-0050", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

lined up with the lines in the forward trace from which these expressions originate.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

After the forward pass on the left-hand side, we run the reverse pass of the adjoints on the right-hand side, starting with ${\overline{v}}_{5} = \overline{y} = \frac{\partial y}{\partial y} = 1$. In the end we get the derivatives $\frac{\partial y}{\partial x_{1}} = {\overline{x}}_{1}$ and $\frac{\partial y}{\partial x_{2}} = {\overline{x}}_{2}$ in just one reverse pass.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

Compared with the straightforwardness of forward accumulation mode, reverse mode AD can, at first, appear somewhat "mysterious". Griewank and Walther argue that this is in part because of the common acquaintance with the chain rule as a mechanistic procedure propagating derivatives forward.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

An important advantage of the reverse mode is that it is significantly less costly to evaluate (in terms of operation count) than the forward mode for functions with a large number of inputs. In the extreme case of $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, only one application of the reverse mode is sufficient to compute the full gradient ${\nabla f} = \left( \frac{\partial y}{\partial x_{1}},\ldots,\frac{\partial y}{\partial x_{n}} \right)$, compared with the $n$ passes of the forward mode needed for populating the same. Because machine learning practice principally involves the gradient of a scalar-valued objective with respect to a large number of parameters, this establishes the reverse mode, as opposed to the forward mode, as the mainstay technique in the form of the backpropagation algorithm.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

In general, for a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$, if we denote the operation count to evaluate the original function by $\text{ops}{(f)}$, the time it takes to calculate the $m \times n$ Jacobian by the forward mode is $nc\text{ops}{(f)}$, whereas the same computation can be done via reverse mode in $mc\text{ops}{(f)}$, where $c$ is a constant guaranteed to be $c < 6$ and typically $c \sim {\lbrack 2,3\rbrack}$. That is to say, reverse mode AD performs better when $m \ll n$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

Similar to the matrix-free computation of Jacobian--vector products with forward mode (Eq. 4), reverse mode can be used for computing the transposed Jacobian--vector product

<!-- chunk {"id": "body-0056", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

by initializing the reverse phase with $\overline{\mathbf{y}} = \mathbf{r}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Reverse Mode", "weight": 1.0} -->

The advantages of reverse mode AD, however, come with the cost of increased storage requirements growing (in the worst case) in proportion to the number of operations in the evaluated function. It is an active area of research to improve storage requirements in implementations by using advanced methods such as checkpointing strategies and data-flow analysis.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Origins of AD and Backpropagation", "weight": 1.0} -->

Ideas underlying AD date back to the 1950s. Forward mode AD as a general method for evaluating partial derivatives was essentially discovered by Wengert. It was followed by a period of relatively low activity, until interest in the field was revived in the 1980s mostly through the work of Griewank, also supported by improvements in modern programming languages and the feasibility of an efficient reverse mode AD.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Origins of AD and Backpropagation", "weight": 1.0} -->

Reverse mode AD and backpropagation have an intertwined history. The essence of the reverse mode, cast in a continuous-time formalism, is the Pontryagin maximum principle. This method was understood in the control theory community and cast in more formal terms with discrete-time variables topologically sorted in terms of dependency by Werbos. Prior to Werbos, the work by Linnainmaa is often cited as the first published description of the reverse mode. Speelpenning subsequently introduced reverse mode AD as we know it, in the sense that he gave the first implementation that was actually automatic, accepting a specification of a computational process written in a general-purpose programming language and automatically performing the reverse mode transformation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Origins of AD and Backpropagation", "weight": 1.0} -->

Incidentally, Hecht-Nielsen cites the work of Bryson and Ho and Werbos as the two earliest known instances of backpropagation. Within the machine learning community, the method has been reinvented several times, such as by Parker, until it was eventually brought to fame by Rumelhart et al. and the Parallel Distributed Processing (PDP) group. The PDP group became aware of Parker's work only after their own discovery; similarly, Werbos' work was not appreciated until it was found by Parker. This tells us an interesting story of two highly interconnected research communities that have somehow also managed to stay detached during this foundational period.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Origins of AD and Backpropagation", "weight": 1.0} -->

For a thorough review of the development of AD, we advise readers to refer to Rall. Interested readers are highly recommended to read Griewank for an investigation of the origins of the reverse mode and Schmidhuber for the same for backpropagation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "AD and Machine Learning", "weight": 1.0} -->

In the following, we examine the main uses of derivatives in machine learning and report on a selection of works where general-purpose AD, as opposed to just backpropagation, has been successfully applied in a machine learning context. Areas where AD has seen use include optimization, neural networks, computer vision, natural language processing, and probabilistic inference.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

Gradient-based optimization is one of the pillars of machine learning. Given an objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, classical gradient descent has the goal of finding (local) minima $\mathbf{w}^{\ast} = {{{\arg\min}_{\mathbf{w}}f}{(\mathbf{w})}}$ via updates of the form ${\Delta\mathbf{w}} = {- {\eta{\nabla f}}}$, where $\eta > 0$ is a step size. Gradient-based methods make use of the fact that $f$ decreases steepest if one goes in the direction of the negative gradient. The convergence rate of gradient-based methods is usually improved by adaptive step-size techniques that adjust the step size $\eta$ on every iteration.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

As we have seen, for large $n$, reverse mode AD provides a highly efficient method for computing gradients.^1313^13See for an example of a general-purpose AD-based gradient descent routine using DiffSharp. Figure 5 and Table 4 demonstrate how gradient computation scales differently for forward and reverse mode AD and numerical differentiation, looking at the Helmholtz free energy function that has been used in AD literature for benchmarking gradient calculations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

Second-order methods based on Newton's method make use of both the gradient $\nabla f$ and the Hessian $\mathbf{H}_{f}$, working via updates of the form ${\Delta\mathbf{w}} = {- {\eta\mathbf{H}_{f}^{- 1}{\nabla f}}}$ and providing significantly faster convergence. AD provides a way of automatically computing the exact Hessian, enabling succinct and convenient general-purpose implementations.^1414^14See for an implementation of Newton's method with the full Hessian. Newton's method converges in fewer iterations, but this comes at the cost of having to compute $\mathbf{H}_{f}$ in each iteration. In large-scale problems, the Hessian is usually replaced by a numerical approximation using first-order updates from gradient evaluations, giving rise to quasi-Newton methods. A highly popular such method is the BFGS^1515^15After Broyden--Fletcher--Goldfarb--Shanno, who independently discovered the method in the 1970s.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

algorithm, together with its limited-memory variant L-BFGS. On the other hand, Hessians arising in large-scale applications are typically sparse. This sparsity along with symmetry can be readily exploited by AD techniques such as computational graph elimination, partial separability, and matrix coloring and compression.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

In many cases one does not need the full Hessian but only a Hessian--vector product $\mathbf{H}\mathbf{v}$, which can be computed efficiently using a reverse-on-forward configuration of AD by applying the reverse mode to take the gradient of code produced by the forward mode.^1616^16Christianson demonstrates that the second derivative can be computed with the same arithmetic operation sequence using forward-on-reverse, reverse-on-forward, and reverse-on-reverse. The taping overheads of these methods may differ in implementation-dependent ways.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

Given the function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, the evaluation point $\mathbf{x}$, and the vector $\mathbf{v}$, one can accomplish this by first computing the directional derivative $\nabla{f \cdot \mathbf{v}}$ through the forward mode via setting $\overset{˙}{\mathbf{x}} = \mathbf{v}$ and then applying the reverse mode on this result to get ${\nabla^{2}{f \cdot \mathbf{v}}} = {\mathbf{H}_{f}\mathbf{v}}$. This computes $\mathbf{H}\mathbf{v}$ with $O{(n)}$ complexity, even though $\mathbf{H}$ is a $n \times n$ matrix. Availability of robust AD tools may make more sophisticated optimization methods applicable to large-scale machine-learning problems.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

For instance, when fast stochastic Hessian--vector products are available, these can be used as the basis of stochastic Newton's methods, which have the potential to endow stochastic optimization with quadratic convergence.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Gradient-Based Optimization", "weight": 1.0} -->

Another approach for improving the rate of convergence of gradient-based methods is to use gain adaptation methods such as stochastic meta-descent (SMD), where stochastic sampling is introduced to avoid local minima and reduce the computational expense. An example using SMD with AD Hessian--vector products is given by Vishwanathan et al. on conditional random fields (CRF). Similarly, Schraudolph and Graepel use Hessian--vector products in their model combining conjugate gradient techniques with stochastic gradient descent.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

Training of a neural network is an optimization problem with respect to its set of weights, which can in principle be addressed by using any method ranging from evolutionary algorithms to gradient-based methods such as BFGS or the mainstay stochastic gradient descent and its many variants. As we have seen, the backpropagation algorithm is only a special case of AD: by applying reverse mode AD to an objective function evaluating a network's error as a function of its weights, we can readily compute the partial derivatives needed for performing weight updates.^1717^17See for an implementation of backpropagation with reverse mode AD.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

The LUSH system, and its predecessor SN, were the first production systems that targeted efficient neural network simulation while incorporating both a general-purpose programming language and AD. Modern deep learning frameworks provide differentiation capability in one way or another, but the underlying mechanism is not always made clear and confusion abounds regarding the use of the terms "autodiff", "automatic differentiation", and "symbolic differentiation", which are sometimes even used interchangeably. In mainstream frameworks including Theano^1818^18Theano is a computational graph optimizer and compiler with GPU support and it currently handles derivatives in a highly optimized form of symbolic differentiation. The result can be interpreted as a hybrid of symbolic differentiation and reverse mode AD, but Theano does not use the general-purpose reverse accumulation as we describe in this paper. (Personal communication with the authors.), TensorFlow, Caffe, and CNTK the user first constructs a model as a computational graph using a domain-specific mini language, which then gets interpreted by the framework during execution.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

This approach has the advantage of enabling optimizations of the computational graph structure (e.g., as in Theano), but the disadvantages of having limited and unintuitive control flow and being difficult to debug. In contrast, the lineage of recent frameworks led by autograd, Chainer, and PyTorch provide truly general-purpose reverse mode AD of the type we outline in Section 3, where the user directly uses the host programming language to define the model as a regular program of the forward computation. This eliminates the need for an interpreter, allows arbitrary control flow statements, and makes debugging simple and intuitive.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

Simultaneously with the ongoing adoption of general-purpose AD in machine learning, we are witnessing a modeling-centric terminology emerge within the deep learning community. The terms *define-and-run* and *static computational graph* refer to Theano-like systems where a model is constructed, before execution, as a computational graph structure, which later gets executed with different inputs while remaining fixed. In contrast, the terms *define-by-run* and *dynamic computational graph* refer to the general-purpose AD capability available in newer PyTorch-like systems where a model is a regular program in the host programming language, whose execution dynamically constructs a computational graph on-the-fly that can freely change in each iteration.^1919^19Note that the terms "static" and "dynamic" here are used in the sense of having a fixed versus non-fixed computational graph topology and not in the sense of data flow architectures.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

*Differentiable programming*^2020^20A term advocated by Christopher Olah, David Dalrymple, and Yann LeCun from a deep learning point of view. Note the difference from *differential* dynamic programming in optimal control. is another emerging term referring to the realization that deep learning practice essentially amounts to writing program templates of potential solutions to a problem, which are constructed as differentiable directed graphs assembled from functional blocks whose parameters are learned from examples using gradient-based optimization. Expressed in this paradigm, neural networks are just a class of parameterized differentiable programs composed of building blocks such as feed-forward, convolutional, and recurrent elements. We are increasingly seeing these traditional building blocks freely composed in arbitrary algorithmic structures using control flow, as well as the introduction of novel differentiable architectures such as the neural Turing machine, a range of controller--interface abstractions, and differentiable versions of data structures such as stacks, queues, deques. Availability of general-purpose AD greatly simplifies the implementation of such architectures by enabling their expression as regular programs that rely on the differentiation infrastructure.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

Although the differentiable programming perspective on deep learning is new, we note that programming with differentiable functions and having differentiation as a language infrastructure has been the main research subject of the AD community for many decades and realized in a wide range of systems and languages as we shall see in Section 5.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Neural Networks, Deep Learning, Differentiable Programming", "weight": 1.0} -->

There are instances in neural network literature---albeit few---where explicit reference has been made to AD for computing error gradients, such as Eriksson et al. using AD for large-scale feed-forward networks, and the work by Yang et al., where the authors use AD to train a neural-network-based proportional-integral-derivative (PID) controller. Similarly, Rollins uses reverse mode AD in conjunction with neural networks for the problem of optimal feedback control. Another example is given for continuous time recurrent neural networks (CTRNN) by Al Seyab and Cao, where the authors apply AD for the training of CTRNNs predicting dynamic behavior of nonlinear processes in real time and report significantly reduced training time compared with other methods.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Computer Vision", "weight": 1.0} -->

Since the influential work by Krizhevsky et al., computer vision has been dominated by deep learning, specifically, variations of convolutional neural networks. These models are trained end-to-end, meaning that a mapping from raw input data to corresponding outputs is learned, automatically discovering the representations needed for feature detection in a process called representation learning.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Computer Vision", "weight": 1.0} -->

Besides deep learning, an interesting area where AD can be applied to computer vision problems is inverse graphics ---or analysis-by-synthesis ---where vision is seen as the inference of parameters for a generative model of a scene. Using gradient-based optimization in inverse graphics requires propagating derivatives through whole image synthesis pipelines including the renderer. Eslami et al. use numerical differentiation for this purpose. Loper and Black implement the Open Differentiable Renderer (OpenDR), which is a scene renderer that also supplies derivatives of the image pixels with respect to scene parameters, and demonstrate it in the task of fitting an articulated and deformable 3D model of the human body to image and range data from a Kinect device. Similarly, Kulkarni et al. implement a differentiable approximate renderer for the task of inference in probabilistic programs describing scenes.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Computer Vision", "weight": 1.0} -->

Srajer et al. investigate the use of AD for three tasks in computer vision and machine learning, namely bundle adjustment, Gaussian mixture model fitting, and hand tracking, and provide a comprehensive benchmark of various AD tools for the computation of derivatives in these tasks.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Computer Vision", "weight": 1.0} -->

Pock et al. make use of AD in addressing the problems of denoising, segmentation, and recovery of information from stereoscopic image pairs, and note the usefulness of AD in identifying sparsity patterns in large Jacobian and Hessian matrices. In another study, Grabner et al. use reverse mode AD for GPU-accelerated medical 2D/3D registration, a task involving the alignment of data from different sources such as X-ray images or computed tomography. The authors report a six-fold increase in speed compared with numerical differentiation using center difference (cf. our benchmark with the Helmholtz function, Figure 5 and Table 4).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Computer Vision", "weight": 1.0} -->

Barrett and Siskind present a use of general-purpose AD for the task of video event detection using hidden Markov models (HMMs) and Dalal and Triggs object detectors, performing training on a corpus of pre-tracked video using an adaptive step size gradient descent with reverse mode AD. Initially implemented with the R6RS-AD package^2121^21 which provides forward and reverse mode AD in Scheme, the resulting gradient code was later ported to C and highly optimized.^2222^22Personal communication.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Natural Language Processing", "weight": 1.0} -->

Natural language processing (NLP) constitutes one of the areas where rapid progress is being made by applying deep learning techniques, with applications in tasks including machine translation, language modeling, dependency parsing, and question answering. Besides deep learning approaches, statistical models in NLP are commonly trained using general purpose or specialized gradient-based methods and mostly remain expensive to train. Improvements in training time can be realized by using online or distributed training algorithms. An example using stochastic gradient descent for NLP is given by Finkel et al. optimizing conditional random field parsers through an objective function. Related with the work on video event detection in the previous section, Yu and Siskind report their work on sentence tracking, representing an instance of grounded language learning paired with computer vision, where the system learns word meanings from short video clips paired with descriptive sentences. The method uses HMMs to represent changes in video frames and meanings of different parts of speech. This work is implemented in C and computes the required gradients using AD through the ADOL-C tool.^2323^23An

<!-- chunk {"id": "body-0084", "role": "body", "section": "Probabilistic Modeling and Inference", "weight": 1.0} -->

Inference in probabilistic models can be static, such as compiling a given model to Bayesian networks and using algorithms such as belief propagation for inference; or they can be dynamic, executing a model forward many times and computing statistics on observed values to infer posterior distributions. Markov chain Monte Carlo (MCMC) methods are often used for dynamic inference, such as the Metropolis--Hastings algorithm based on random sampling. Meyer et al. give an example of how AD can be used to speed up Bayesian posterior inference in MCMC, with an application in stochastic volatility. Amortized inference techniques based on deep learning work by training neural networks for performing approximate inference in generative models defined as probabilistic programs.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Probabilistic Modeling and Inference", "weight": 1.0} -->

When model parameters are continuous, the Hamiltonian---or, hybrid---Monte Carlo (HMC) algorithm provides improved convergence characteristics avoiding the slow exploration of random sampling, by simulating Hamiltonian dynamics through auxiliary "momentum variables". The advantages of HMC come at the cost of requiring gradient evaluations of complicated probability models. AD is highly suitable here for complementing probabilistic modeling, because it relieves the user from the manual derivation of gradients for each model.^2424^24See for an implementation of HMC with reverse mode AD. For instance, the probabilistic programming language Stan implements automatic Bayesian inference based on HMC and the No-U-Turn sampler (NUTS) and uses reverse mode AD for the calculation of gradients for both HMC and NUTS. Similarly, Wingate et al. demonstrate the use of AD as a non-standard interpretation of probabilistic programs enabling efficient inference algorithms. Kucukelbir et al. present an AD-based method for deriving variational inference (VI) algorithms.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Probabilistic Modeling and Inference", "weight": 1.0} -->

PyMC3 allows fitting of Bayesian models using MCMC and VI, for which it uses gradients supplied by Theano. Edward is a library for deep probabilistic modeling, inference, and criticism that supports VI using TensorFlow. Availability of general-purpose AD in this area has enabled new libraries such as Pyro^2525^25 and ProbTorch for deep *universal* probabilistic programming with support for recursion and control flow, relying, in both instances, on VI using gradients supplied by PyTorch's reverse mode AD infrastructure.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Probabilistic Modeling and Inference", "weight": 1.0} -->

When working with probabilistic models, one often needs to backpropagate derivatives through sampling operations of random variables in order to achieve stochastic optimization of model parameters. The score-function estimator, or REINFORCE, method provides a generally applicable unbiased gradient estimate, albeit with high variance. When working with continuous random variables, one can substitute a random variable by a deterministic and differentiable transformation of a simpler random variable, a method known as the "reparameterization trick". For discrete variables, the REBAR method provides a lower-variance unbiased gradient estimator by using continuous relaxation. A generalization of REBAR called RELAX works by learning a free-form control variate parameterized by a neural network and is applicable in both discrete and continuous settings.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Implementations", "weight": 1.0} -->

It is useful to have an understanding of the different ways in which AD can be implemented. Here we cover major implementation strategies and provide a survey of existing tools.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Implementations", "weight": 1.0} -->

A principal consideration in any AD implementation is the performance overhead introduced by the AD arithmetic and bookkeeping. In terms of computational complexity, AD guarantees that the amount of arithmetic goes up by no more than a small constant factor. On the other hand, managing this arithmetic can introduce a significant overhead if done carelessly. For instance, naïvely allocating data structures for holding dual numbers will involve memory access and allocation for every arithmetic operation, which are usually more expensive than arithmetic operations on modern computers.^2626^26The implementation of forward mode in Julia attempts to avoid this, and some current compilers can avoid this expense by unboxing dual numbers. This method is also used to reduce the memory-access overhead in the implementations of forward mode in Stalingrad and the Haskell *ad* library. Likewise, using operator overloading may introduce method dispatches with attendant costs, which, compared to raw numerical computation of the original function, can easily amount to a slowdown of an order of magnitude.^2727^27Flow analysis and/or partial evaluation, together with tag stripping, can remove this method dispatch.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Implementations", "weight": 1.0} -->

These, together with unboxing, can often make it possible to completely eliminate the memory access, memory allocation, memory reclamation, and method dispatch overhead of dual numbers.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Implementations", "weight": 1.0} -->

Another major issue is the risk of hitting a class of bugs called "perturbation confusion". This essentially means that if two ongoing differentiations affect the same piece of code, the two formal epsilons they introduce (Section 3.1.1) need to be kept distinct. It is very easy to have bugs---particularly in performance-oriented AD implementations---that confuse these in various ways. Such situations can also arise when AD is nested, that is, derivatives are computed for functions that internally compute derivatives.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Implementations", "weight": 1.0} -->

Translation of mathematics into computer code often requires attention to numeric issues. For instance, the mathematical expressions $\log{({1 + x})}$ or $\sqrt{x^{2} + y^{2} + z^{2}}$ or $\tan^{- 1}{({y/x})}$ should not be naïvely translated, but rather expressed as log1p(x), hypot(x,hypot(y,z)), and atan2(y,x). In machine learning, the most prominent example of this is probably the so-called log-sum-exp trick to improve the numerics of calculations of the form $\log{\sum_{i}{\exp x_{i}}}$. AD is not immune to such numeric considerations. For example, code calculating $E = {\sum_{i}E_{i}}$, processed by AD, will calculate ${\nabla_{w}E} = {\sum_{i}{\nabla_{w}E_{i}}}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Implementations", "weight": 1.0} -->

If the system is seeking a local minimum of $E$ then ${\nabla_{w}E} = {\sum_{i}{\nabla_{w}E_{i}}}\rightarrow_{t}0$, and naïvely adding a set of large numbers whose sum is near zero is numerically fraught. This is to say that AD is not immune to the perils of floating point arithmetic, and can sometimes introduce numeric issues which were not present in the primal calculation. Issues of numeric analysis are outside our present scope, but there is a robust literature on the numerics of AD (e.g., Griewank et al. ) involving using subgradients to allow optimization to proceed despite non-differentiability of the objective, appropriate subgradients and approximations for functions like $| \cdot |$ and ${\parallel \cdot \parallel}_{2}$ and $\sqrt{\cdot}$ near zero, and a spate of related issues.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Implementations", "weight": 1.0} -->

One should also be cautious about approximated functions and AD. In this case, if one has a procedure *approximating* an ideal function, AD always gives the derivative of the procedure that was actually programmed, which may not be a good approximation of the derivative of the ideal function that the procedure was approximating. For instance, consider $e^{x}$ computed by a piecewise-rational approximation routine. Using AD on this routine would produce an approximated derivative in which each piece of the piecewise formula will get differentiated. Even if this would remain an approximation of the derivative of $e^{x}$, we know that $\frac{de^{x}}{dx} = e^{x}$ and the original approximation itself was already a better approximation for the derivative of $e^{x}$.^2828^28In modern systems this is not an issue, because $e^{x}$ is a primitive implemented in hardware. Users of AD implementations must be therefore cautious to *approximate the derivative, not differentiate the approximation*. This would require explicitly approximating a known derivative, in cases where a mathematical function can only be computed approximately but has a well-defined mathematical derivative.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Implementations", "weight": 1.0} -->

We note that there are similarities as well as differences between machine learning workloads and those studied in the traditional AD literature. Deep learning systems are generally compute-bound and spend a considerable amount of computation time in highly-optimized numerical kernels for matrix operations. This is a situation which is arguably amenable to operator-overloading-based AD implementations on high-level operations, as is commonly found in current machine learning frameworks. In contrast, numerical simulation workloads in traditional AD applications can be bandwidth-bound, making source code transformation and compiler optimization approaches more relevant. Another difference worth noting is that whereas high numerical precision is desirable in traditional application domains of AD such as computational fluid dynamics, in deep learning lower-precision is sufficient and even desirable in improving computational efficiency, thanks to the error resiliency of neural networks.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Implementations", "weight": 1.0} -->

There are instances in recent literature where implementation-related experience from the AD field has been put to use in machine learning settings. One particular area of recent interest is implicit and iterative AD techniques, which has found use in work incorporating constrained optimization within deep learning and probabilistic graphical models and neural networks. Another example is checkpointing strategies, which allow balancing of application-specific trade-offs between time and space complexities of reverse mode AD by not storing the full tape of intermediate variables in memory and reconstructing these as needed by re-running parts of the forward computation from intermediate checkpoints. This is highly relevant in deep learning workloads running on GPUs with limited memory budgets. A recent example in this area is the work by Gruslys et al., where the authors construct a checkpointing variety of the backpropagation through time (BPTT) algorithm for recurrent neural networks and demonstrate it saving up to 95% memory usage at the cost of a 33% increase in computation time in one instance.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Implementations", "weight": 1.0} -->

In Table 5 we present a review of notable general-purpose AD implementations.^2929^29Also see the website for a list of tools maintained by the AD community. A thorough taxonomy of implementation techniques was introduced by Juedes, which was later revisited by Bischof et al. and simplified into *elemental*, *operator overloading*, *compiler-based*, and *hybrid* methods. We adopt a similar classification for the following part of this section.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Implementations", "weight": 1.0} -->

Computational Infrastructure for Operations Research
Walther and Griewank

<!-- chunk {"id": "body-0099", "role": "body", "section": "Implementations", "weight": 1.0} -->

Computational Infrastructure for Operations Research
Bell and Burke

<!-- chunk {"id": "body-0100", "role": "body", "section": "Implementations", "weight": 1.0} -->

Technical University of Denmark
Bendtsen and Stauning

<!-- chunk {"id": "body-0101", "role": "body", "section": "Implementations", "weight": 1.0} -->

Fermi National Accelerator Laboratory
Ostiguy and Michelotti

<!-- chunk {"id": "body-0102", "role": "body", "section": "Implementations", "weight": 1.0} -->

George Mason Univ., Dept. of Computer Science

<!-- chunk {"id": "body-0103", "role": "body", "section": "Implementations", "weight": 1.0} -->

Maynooth University, Microsoft Research Cambridge

<!-- chunk {"id": "body-0104", "role": "body", "section": "Implementations", "weight": 1.0} -->

Numerical Algorithms Group
Naumann and Riehme

<!-- chunk {"id": "body-0105", "role": "body", "section": "Implementations", "weight": 1.0} -->

Max Planck Institute for Meteorology
Giering and Kaminski

<!-- chunk {"id": "body-0106", "role": "body", "section": "Implementations", "weight": 1.0} -->

Michigan State Univ., Biomedical and Physical Sci.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Implementations", "weight": 1.0} -->

University Politehnica of Bucharest
Slusanschi and Dumitrel

<!-- chunk {"id": "body-0108", "role": "body", "section": "Implementations", "weight": 1.0} -->

Technical University of Darmstadt, Scientific Comp.
Willkomm and Vehreschild

<!-- chunk {"id": "body-0109", "role": "body", "section": "Implementations", "weight": 1.0} -->

Hamburg Univ. of Technology, Inst. for Reliable Comp.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Implementations", "weight": 1.0} -->

Cranfield University &amp; Tomlab Optimization Inc.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Implementations", "weight": 1.0} -->

Harvard Intelligent Probabilistic Systems Group

<!-- chunk {"id": "body-0112", "role": "body", "section": "Implementations", "weight": 1.0} -->

Purdue Univ., School of Electrical and Computer Eng.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Implementations", "weight": 1.0} -->

MIT Computer Science and Artificial Intelligence Lab.
Sussman and Wisdom

<!-- chunk {"id": "body-0114", "role": "body", "section": "Implementations", "weight": 1.0} -->

Purdue Univ., School of Electrical and Computer Eng.
Pearlmutter and Siskind

<!-- chunk {"id": "body-0115", "role": "body", "section": "Implementations", "weight": 1.0} -->

F: Forward, R: Reverse; COM: Compiler, INT: Interpreter, LIB: Library, OO: Operator overloading, ST: Source transformation

<!-- chunk {"id": "body-0116", "role": "body", "section": "Elemental Libraries", "weight": 1.0} -->

These implementations form the most basic category and work by replacing mathematical operations with calls to an AD-enabled library. Methods exposed by the library are then used in function definitions, meaning that the decomposition of any function into elementary operations is done manually when writing the code.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Elemental Libraries", "weight": 1.0} -->

The approach has been utilized since the early days of AD, with prototypical examples being the WCOMP and UCOMP packages of Lawson, the APL package of Neidinger, and the work by Hinkins. Likewise, Rich and Hill formulate their implementation of AD in MATLAB using elemental methods.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Elemental Libraries", "weight": 1.0} -->

Elemental libraries still constitute the simplest strategy to implement AD for languages without operator overloading.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Compilers and Source Code Transformation", "weight": 1.0} -->

These implementations provide extensions to programming languages that automate the decomposition of algorithms into AD-enabled elementary operations. They are typically executed as preprocessors^3030^30Preprocessors transform program source code before it is given as an input to a compiler. to transform the input in the extended language into the original language.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Compilers and Source Code Transformation", "weight": 1.0} -->

Classical instances of source code transformation include the Fortran preprocessors GRESS and PADRE2, which transform AD-enabled variants of Fortran into standard Fortran 77 before compiling. Similarly, the ADIFOR tool, given a Fortran source code, generates an augmented code in which all specified partial derivatives are computed in addition to the original result. For procedures coded in ANSI C, the ADIC tool implements AD as a source code transformation after the specification of dependent and independent variables. A recent and popular tool also utilizing this approach is Tapenade, implementing forward and reverse mode AD for Fortran and C programs. Tapenade itself is implemented in Java and can be run locally or as an online service.^3131^31

<!-- chunk {"id": "body-0121", "role": "body", "section": "Compilers and Source Code Transformation", "weight": 1.0} -->

In addition to language extensions through source code transformation, there are implementations introducing new languages with tightly integrated AD capabilities through special-purpose compilers or interpreters. Some of the earliest AD tools such as SLANG and PROSE belong to this category. The NAGWare Fortran 95 compiler is a more recent example, where the use of AD-related extensions triggers automatic generation of derivative code at compile time.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Compilers and Source Code Transformation", "weight": 1.0} -->

As an example of interpreter-based implementation, the algebraic modeling language AMPL enables objectives and constraints to be expressed in mathematical notation, from which the system deduces active variables and arranges the necessary AD computations. Other examples in this category include the FM/FAD package, based on the Algol-like DIFALG language, and the object-oriented COSY language similar to Pascal.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Compilers and Source Code Transformation", "weight": 1.0} -->

The Stalingrad compiler, working on the Scheme-based AD-aware VLAD language, also falls under this category. The newer DVL compiler^3232^32 is based on Stalingrad and uses a reimplementation of portions of the VLAD language.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Compilers and Source Code Transformation", "weight": 1.0} -->

Motivated by machine learning applications, the Tangent library implements AD using source code transformation, and accepts numeric functions written in a syntactic subset of Python and Numpy.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Operator Overloading", "weight": 1.0} -->

In modern programming languages with polymorphic features, operator overloading provides the most straightforward way of implementing AD, exploiting the capability of redefining elementary operation semantics.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Operator Overloading", "weight": 1.0} -->

A popular tool implemented with operator overloading in C++ is ADOL-C. ADOL-C requires the use of AD-enabled types for variables, and records arithmetic operations on variables in tape data structures, which can subsequently be "played back" during reverse mode AD computations. The Mxyzptlk package is another example for C++ capable of computing arbitrary-order partial derivatives via forward propagation. The FADBAD++ library implements AD for C++ using templates and operator overloading. For Python, the *ad* package^3333^33 uses operator overloading to compute first- and second-order derivatives, while the newer autograd package^3434^34 provides forward and reverse mode AD with support for higher-order derivatives.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Operator Overloading", "weight": 1.0} -->

For functional languages, examples include R6RS-AD^3535^35 and the AD routines within the Scmutils library^3636^36 for Scheme, the *ad* library^3737^37 for Haskell, and DiffSharp^3838^38 for F# and C#.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Backpropagation and gradient-based optimization are behind virtually all recent successes in machine learning, yielding state-of-the-art results in computer vision, speech recognition and synthesis, and machine translation. We expect these techniques to remain at the core of machine learning for the foreseeable future. Research in the field involves a rapid prototyping and development cycle for testing new models and ideas, using a collection of increasingly higher-quality machine learning frameworks. These frameworks are in the process of transition from coarse-grained (module level) backpropagation towards fine-grained, general-purpose AD, allowing models to be implemented as regular programs in general-purpose programming languages with differentiation as an integral part of the infrastructure. We strongly believe that general-purpose AD is the future of gradient-based machine learning and we expect it to become an indispensable tool in the machine learning toolbox.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Conclusions", "weight": 1.0} -->

It is an exciting time for working at the intersection of AD and machine learning, and there are many opportunities for bringing advanced techniques and expertise from AD literature to bear on machine learning problems. Techniques that have been developed by the AD community such as tape reduction and elimination, fixed-point iterations, utilizing sparsity by matrix coloring, and reverse AD checkpointing are just a few examples that can find potential use in machine learning for increasing performance, improving convergence of optimization, using hardware more efficiently, and even enabling new types of machine learning models to be implemented. Similarly, exciting new AD modes like direct propagation of the inverse Jacobian have emerged from the machine learning community, but have yet to be examined and formalized by the AD community.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conclusions", "weight": 1.0} -->

An important direction for future work is to make use of nested AD techniques in machine learning, allowing differentiation to be nested arbitrarily deep with referential transparency. Nested AD is highly relevant in hyperparameter optimization as it can effortlessly provide exact hypergradients, that is, derivatives of a training objective with respect to the hyperparameters of an optimization routine. Potential applications include Bayesian model selection and gradient-based tuning of Hamiltonian Monte Carlo step sizes and mass matrices. Besides hyperparameters, models internally using higher-order derivatives constitute a straightforward usage case for nested AD. The Riemannian manifold Langevin and Hamiltonian Monte Carlo methods use higher-order derivative information to more closely track the information geometry of the sampled distribution for faster convergence and exploration. In neural networks, it is very natural to use nested derivatives in defining objective functions that take input transformations into account, such as the Tangent Prop method for imposing invariance under a set of chosen transformations.
