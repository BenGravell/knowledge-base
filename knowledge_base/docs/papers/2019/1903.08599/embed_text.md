<!-- arxiv-full-text:v1 {"arxiv_id": "1903.08599", "source": "ar5iv"} -->

### Introduction

Linear matrix inequalities (LMIs) commonly appear in systems, stability, and control applications. Many analysis and synthesis problems in these areas can be solved as feasibility or optimization problems subject to LMI constraints. Although most well-known LMI properties and manipulation tricks (e.g., Schur complement, congruence transformation) can be found in standard references, many useful LMI properties are scattered throughout the literature. The purpose of this document is to collect and organize properties, tricks, and applications related to LMIs from a number of references together in a single document. Proofs of the properties presented in this document are not included when they can be found in the cited references in the interest of brevity. Illustrative examples are included whenever necessary to fully explain a certain property. Multiple equivalent forms of LMIs are often presented to give the reader a choice of which form may be best suited for a particular problem at hand. The equivalency of some of the LMIs in this document may be straightforward to more experienced readers, but the authors believe that some readers may benefit from the presentation of multiple equivalent LMIs.

The document is organized as follows. In the remaining portions of Section 1, the notation used throughout the document is presented and some fundamental LMI properties are discussed. Section 2 features a collection of LMI properties and tricks that are interesting and potentially useful. The LMI properties and tricks in this section are grouped together based on similarities when possible. Applications involving LMIs in systems and stability theory are included in Section 3. Section 4 presents a number of LMI-based optimal controller synthesis methods, while Section 5 includes LMI-based optimal estimation synthesis methods.

The authors would like to thank the following individuals for alerting us of errors, and providing useful comments and suggestions for improvement: Leila Bridgeman, Jyot Buch, Manash Chakraborty, Steven Dahdah, William Elke, Robyn Fortune, Peter Seiler.

Please note that this document is a work in progress. If you notice any errors or inaccuracies, or have any suggestions of content that should be included in this document, please email either of the authors at rcaverly@umn.edu or james.richard.forbes@mcgill.ca so that changes to future versions can be made.

### Notation

In this document, matrices are denoted by boldface letters (e.g., $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$), column matrices are denoted by lowercase boldface letters (e.g., $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$), scalars are denoted by simple letters (e.g., $\gamma \in {\mathbb{R}}$), and operators are denoted by script letters (e.g., ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$). The set of $n$ by $m$ real matrices is denoted as ${\mathbb{R}}^{n \times m}$, the set of $n$ by $m$ complex matrices is denoted as ${\mathbb{C}}^{n \times m}$, and the set of $n$ by $n$ symmetric matrices is denoted as ${\mathbb{S}}^{n}$. The identity matrix is written as $\mathbf{1}$ and a matrix filled with zeros is written as $\mathbf{0}$. The dimensions of $\mathbf{1}$ and $\mathbf{0}$ are specified when necessary. Repeated blocks within symmetric matrices are replaced by $\ast$ for brevity and clarity. The conjugate transpose or Hermitian transpose of the matrix $\mathbf{V} \in {\mathbb{C}}^{\mathbf{n} \times \mathbf{m}}$ is denoted by $\mathbf{V}^{\mathsf{H}}$. The notation $\text{He}{\{ \cdot \}}$ is used as a shorthand in situations with limited space, where ${\text{He}{\{ \cdot \}}} = {( \cdot ) + ( \cdot )^{\mathsf{H}}}$. The real and imaginary parts of the complex number $z \in {\mathbb{C}}$ are denoted as $\text{Re}{(z)}$ and $\text{Im}{(z)}$, respectively. The Kroenecker product of two matrices is denoted by $\otimes$.

Consider the square matrix $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The eigenvalues of $\mathbf{A}$ are denoted by $\lambda_{i}{(\mathbf{A})}$, $i = {1,2,\ldots,n}$. The matrix $\mathbf{A}$ is Hurwitz if all of its eigenvalues are in the open left-half complex plane (i.e., ${\text{Re}\left( {\lambda_{i}{(\mathbf{A})}} \right)} < 0$, $i = {1,\ldots,n}$). A matrix is Schur if all of its eigenvalues are strictly within a unit disk centered at the origin of the complex plane (i.e., $\left| {\lambda_{i}{(\mathbf{A})}} \right| < 1$, $i = {1,\ldots,n}$). If $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, then the minimum eigenvalue of $\mathbf{A}$ is denoted by $\underset{¯}{\lambda}{(\mathbf{A})}$ and its maximum eigenvalue is denoted by $\overline{\lambda}{(\mathbf{A})}$.

Consider the matrix $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$. The minimum singular value of $\mathbf{B}$ is denoted by $\underset{¯}{\sigma}{(\mathbf{B})}$ and its maximum singular value is denoted by $\overline{\sigma}{(\mathbf{B})}$. The range and nullspace of $\mathbf{B}$ are denoted by $\mathcal{R}{(\mathbf{B})}$ and $\mathcal{N}{(\mathbf{B})}$, respectively.

A state-space realization of the continuous-time linear time-invariant (LTI) system is often written compactly as $(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D})$ in this document. The argument of time is often omitted in continuous-time state-space realizations, unless needed to prevent ambiguity.

A state-space realization of the discrete-time LTI system is often written compactly as $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$.

The inner product spaces $\mathcal{L}_{2}$ and $\mathcal{L}_{2e}$ for continuous-time signals are defined as follows.

The inner product sequence spaces $\ell_{2}$ and $\ell_{2e}$ for discrete-time signals are defined as follows.

### Definitions and Fundamental LMI Properties

### Definiteness of a Matrix

### Definition 1.1

\[6, pp. 429--430\] Consider the symmetric matrix $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$. The matrix $\mathbf{A}$ is *positive definite* if ${\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}} > \mathbf{0}$, ${\forall\mathbf{x}} \neq \mathbf{0} \in {\mathbb{R}}^{\mathbf{n}}$, *positive semi-definite* if ${\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}} \geq \mathbf{0}$, ${\forall\mathbf{x}} \in {\mathbb{R}}^{\mathbf{n}}$, *negative definite* if ${\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}} < \mathbf{0}$, ${\forall\mathbf{x}} \neq \mathbf{0} \in {\mathbb{R}}^{\mathbf{n}}$, *negative semi-definite* if ${\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}} \leq \mathbf{0}$, ${\forall\mathbf{x}} \in {\mathbb{R}}^{\mathbf{n}}$, and indefinite if $\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}$ is neither positive nor negative.

### Theorem 1.2

\[6, pp. 430--431\], \[7, p. 703\] Consider the symmetric matrix $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$. The matrix $\mathbf{A}$ is *positive definite* if and only if ${\underset{¯}{\lambda}{(\mathbf{A})}} > \mathbf{0}$, *positive semi-definite* if and only if ${\underset{¯}{\lambda}{(\mathbf{A})}} \geq \mathbf{0}$, *negative definite* if and only if ${\overline{\lambda}{(\mathbf{A})}} < \mathbf{0}$, *negative semi-definite* if and only if ${\overline{\lambda}{(\mathbf{A})}} \leq \mathbf{0}$, and indefinite if and only if ${\underset{¯}{\lambda}{(\mathbf{A})}} < \mathbf{0}$ and ${\overline{\lambda}{(\mathbf{A})}} > \mathbf{0}$.

### Proof

To see why the sign of $\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}$ is dictated by the eigenvalues of $\mathbf{A}$, let $\mathbf{A} = {\mathbf{V}\mathbf{\Lambda}\mathbf{V}^{- \mathbf{1}}}$, where $\mathbf{V}^{- \mathbf{1}} = \mathbf{V}^{\mathsf{T}}$ because $\mathbf{A}$ is symmetric. Notice that where $\mathbf{z} = {\mathbf{V}^{\mathsf{T}}\mathbf{x}} = \begin{bmatrix} \mathbf{z}_{\mathbf{1}} & \mathbf{z}_{\mathbf{2}} & \cdots & \mathbf{z}_{\mathbf{n}} \end{bmatrix}^{\mathsf{T}}$. ∎ When evaluating the sign of the quadratic form $\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}$, there is no loss of generality in restricting $\mathbf{A}$ to be symmetric. This is seen through the next two examples.

### Example 1.1

Consider the skew-symmetric matrix $\mathbf{A} = {- \mathbf{A}^{\mathsf{T}}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. Evaluating the quadratic form $\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}$ yields Therefore, ${\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}} = \mathbf{0}$ for all skew-symmetic matrices.

### Example 1.2

Consider the matrix $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, which can be decomposed as where $\mathbf{A}_{\text{sym}} = \mathbf{A}_{\text{sym}}^{\mathsf{T}} = {\frac{1}{2}\left({\mathbf{A} + \mathbf{A}^{\mathsf{T}}} \right)}$ is the symmetric part of $\mathbf{A}$ and $\mathbf{A}_{\text{skew}} = {- \mathbf{A}_{\text{skew}}^{\mathsf{T}}} = {\frac{1}{2}\left({\mathbf{A} - \mathbf{A}^{\mathsf{T}}} \right)}$ is the skew-symmetric part of $\mathbf{A}$. Evaluating the quadratic form $\mathbf{x}^{\mathsf{T}}{\mathbf{A}\mathbf{x}}$ yields This confirms that when determining the definiteness of a matrix there is no loss of generality in restricting the matrix to be symmetric.

The positive definiteness and positive semidefiniteness of a matrix are denoted by $> 0$ and $\geq 0$, respectively (e.g., $\mathbf{A} = \mathbf{A}^{\mathsf{T}} > \mathbf{0}$ is positive definite and $\mathbf{B} = \mathbf{B}^{\mathsf{T}} \geq \mathbf{0}$ is positive semidefinite). Similarly, the negative definiteness and negative semidefiniteness of a matrix are denoted by $< 0$ and $\leq 0$, respectively (e.g., $\mathbf{C} = \mathbf{C}^{\mathsf{T}} < \mathbf{0}$ is negative definite and $\mathbf{D} = \mathbf{D}^{\mathsf{T}} \leq \mathbf{0}$ is negative semidefinite). For brevity, the transpose component of a definiteness statement is omitted in this document, for example, $\mathbf{A} = \mathbf{A}^{\mathsf{T}} > \mathbf{0}$ is simply written as $\mathbf{A} > \mathbf{0}$.

### Matrix Inequalities and LMIs

### Definition 1.3

A matrix inequality, $\mathbf{G}:{{\mathbb{R}}^{\mathbf{m}}\rightarrow{\mathbb{S}}^{\mathbf{n}}}$, in the variable $\mathbf{x} \in {\mathbb{R}}^{\mathbf{m}}$ is an expression of the form where $\mathbf{x}^{\mathsf{T}} = \begin{bmatrix} {\mathbf{x}_{\mathbf{1}}\cdots\mathbf{x}_{\mathbf{m}}} \end{bmatrix}$, $\mathbf{G}_{\mathbf{0}} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{G}_{\mathbf{i}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $i = {1,\ldots,p}$.

### Definition 1.4

\[8, p. 34\], A bilinear matrix inequality (BMI), $\mathbf{H}:{{\mathbb{R}}^{\mathbf{m}}\rightarrow{\mathbb{S}}^{\mathbf{n}}}$, in the variable $\mathbf{x} \in {\mathbb{R}}^{\mathbf{m}}$ is an expression of the form where $\mathbf{x}^{\mathsf{T}} = \begin{bmatrix} {\mathbf{x}_{\mathbf{1}}\cdots\mathbf{x}_{\mathbf{m}}} \end{bmatrix}$, and $\mathbf{H}_{\mathbf{i}}$, $\mathbf{H}_{\mathbf{i},\mathbf{j}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {0,\ldots,m}$, $j = {0,\ldots,m}$.

### Definition 1.5

\[1, p. 7\],\[3, pp. 15--16\] An LMI, $\mathbf{F}:{{\mathbb{R}}^{\mathbf{m}}\rightarrow{\mathbb{S}}^{\mathbf{n}}}$, in the variable $\mathbf{x} \in {\mathbb{R}}^{\mathbf{m}}$ is an expression of the form where $\mathbf{x}^{\mathsf{T}} = \begin{bmatrix} {\mathbf{x}_{\mathbf{1}}\cdots\mathbf{x}_{\mathbf{m}}} \end{bmatrix}$ and $\mathbf{F}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {0,\ldots,m}$.

LMIs can alternatively be defined in terms of matrix variables as follows.

### Definition 1.6

\[10, p. 125\] An LMI, $\mathbf{F}:{{{\mathbb{R}}^{\mathbf{p}_{\mathbf{1}} \times \mathbf{q}_{\mathbf{1}}} \times \cdots \times {\mathbb{R}}^{\mathbf{p}_{\mathbf{r}} \times \mathbf{q}_{\mathbf{r}}}}\rightarrow{\mathbb{S}}^{\mathbf{n}}}$, in the matrix variables $\mathbf{X}_{\mathbf{i}} \in {\mathbb{R}}^{\mathbf{p}_{\mathbf{i}} \times \mathbf{q}_{\mathbf{i}}}$, $i = {1,\ldots,r}$, where $m = {\sum_{i = 1}^{r}{p_{i}q_{i}}}$, is an expression of the form where $\mathbf{F}_{\mathbf{0}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{G}_{\mathbf{i}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}_{\mathbf{i}}}$, and $\mathbf{H}_{\mathbf{i}} \in {\mathbb{R}}^{\mathbf{q}_{\mathbf{i}} \times \mathbf{n}}$, $i = {1,\ldots,r}$.

### Example 1.3

\[1, pp. 8--9\] Consider the matrices $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$. It is desired to find a symmetric matrix $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ satisfying the matrix inequality where $\mathbf{P} > \mathbf{0}$. The matrix $\mathbf{P}$ is the design variable in this problem, and this LMI can be directly related to the definition in (1.2) by setting $\mathbf{F}_{\mathbf{0}} = \mathbf{Q}$, $\mathbf{G}_{\mathbf{1}} = \mathbf{1}$, $\mathbf{H}_{\mathbf{1}} = \mathbf{A}$, $\mathbf{X}_{\mathbf{1}} = \mathbf{P}$, and enforcing the constraint $\mathbf{X}_{\mathbf{1}} = \mathbf{X}_{\mathbf{1}}^{\mathsf{T}}$. This LMI can be reformulated in the form of (1.1) by defining the scalar entries of the matrix variable $\mathbf{P}$ as the design variables. To illustrate this, let us consider the case of $n = 2$ so that each matrix is of dimension $2 \times 2$, and $\mathbf{x} = \begin{bmatrix} \mathbf{p}_{\mathbf{1}} & \mathbf{p}_{\mathbf{2}} & \mathbf{p}_{\mathbf{3}} \end{bmatrix}^{\mathsf{T}}$. Writing the matrix $\mathbf{P}$ in terms of a basis $\mathbf{E}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{2}}$, $i = {1,2,3}$, yields Note that the matrices $\mathbf{E}_{\mathbf{i}}$ are linearly independent and symmetric, thus forming a basis for the symmetric matrix $\mathbf{P}$. The matrix inequality in (1.3) can be written as Defining $\mathbf{F}_{\mathbf{0}} = \mathbf{Q}$ and $\mathbf{F}_{\mathbf{i}} = \mathbf{F}_{\mathbf{i}}^{\mathsf{T}} = {{\mathbf{E}_{\mathbf{i}}\mathbf{A}} + {\mathbf{A}^{\mathsf{T}}\mathbf{E}_{\mathbf{i}}}}$, $i = {1,2,3}$, yields which now resembles the definition of an LMI in (1.1). Throughout this document, LMIs are typically written in the matrix form of (1.2), rather than the scalar form of (1.1).

### Relative Definiteness of a Matrix

The definiteness of a matrix can be found relative to another matrix. For example, consider the matrices $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{B} \in {\mathbb{S}}^{\mathbf{n}}$. The matrix inequality $\mathbf{A} < \mathbf{B}$ is equivalent to ${\mathbf{A} - \mathbf{B}} < \mathbf{0}$ or ${\mathbf{B} - \mathbf{A}} > \mathbf{0}$.

Knowing the relative definiteness of matrices can be useful. For example, if in the previous example we have $\mathbf{A} < \mathbf{B}$ and also know that $\mathbf{A} > \mathbf{0}$, then we know that $\mathbf{B} > \mathbf{0}$. This follows from $0 < \mathbf{A} < \mathbf{B}$. For more facts involving the relative definiteness of matrices, see \[7, pp. 703--704\].

### Strict and Nonstrict Matrix Inequalities

A strict matrix inequality can be converted to a nonstrict matrix inequality. For example, $\mathbf{A} > \mathbf{0}$ is implied by $\mathbf{A} \geq {\epsilon\mathbf{1}}$, where $\epsilon \in {\mathbb{R}}_{> 0}$. Similarly, $\mathbf{B} < \mathbf{0}$ is implied by $\mathbf{B} \leq {- {\epsilon\mathbf{1}}}$, where $\epsilon \in {\mathbb{R}}_{> 0}$.

Converting a strict matrix inequality into a nonstrict matrix inequality is useful when working with LMI solvers that cannot handle strict constraints.

### Concatenation of LMIs

A useful property of LMIs is that multiple LMIs can be concatenated together to form a single LMI. For example, satisfying the LMIs $\mathbf{A} < \mathbf{0}$ and $\mathbf{B} < \mathbf{0}$ is equivalent to satisfying the concatenated LMI More generally, satisfying the LMIs $\mathbf{A}_{\mathbf{i}} < \mathbf{0}$, $i = {1,\ldots,n}$ is equivalent to satisfying the concatenated LMI ${{diag}{\{\mathbf{A}_{\mathbf{1}},\ldots,\mathbf{A}_{\mathbf{n}}\}}} < \mathbf{0}$.

### Convexity of LMIs

### Definition 1.7

\[11, p. 138\] A set, $\mathcal{S}$, in a real inner product space is convex if for all ${\mathbf{x},\mathbf{y}} \in \mathcal{S}$ and $\alpha \in {\mathbb{R}}$, where $0 \leq \alpha \leq 1$, it holds that ${{\alpha\mathbf{x}} + {{({\mathbf{1} - \alpha})}\mathbf{y}}} \in \mathcal{S}$.

### Lemma 1.1

The set of solutions to an LMI is convex. That is, the set $\mathcal{S} = \left. \{{\mathbf{x} \in {\mathbb{R}}^{\mathbf{m}}} \middle| {{\mathbf{F}{(\mathbf{x})}} \leq \mathbf{0}}\} \right.$ is a convex set, where $\mathbf{F}:{{\mathbb{R}}^{\mathbf{m}}\rightarrow{\mathbb{S}}^{\mathbf{n}}}$ is an LMI.

### Proof

Consider ${\mathbf{x},\mathbf{y}} \in {\mathbb{R}}^{\mathbf{m}}$ and $\alpha \in {\lbrack 0,1\rbrack}$, and suppose that $\mathbf{x}$ and $\mathbf{y}$ satisfy (1.1). The LMI $\mathbf{F}:{{\mathbb{R}}^{\mathbf{m}}\rightarrow{\mathbb{S}}^{\mathbf{n}}}$ is convex, since

### Semidefinite Programs (SDPs)

A semidefinite program (SDP) is a convex optimization problem of the form \[12, p. 168\] where $\mathbf{x}^{\mathsf{T}} = \begin{bmatrix} {\mathbf{x}_{\mathbf{1}}\cdots\mathbf{x}_{\mathbf{m}}} \end{bmatrix}$, $\mathbf{c} \in {\mathbb{R}}^{\mathbf{m}}$, $\mathbf{F}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {0,\ldots,m}$, and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is an LMI in the variable $\mathbf{x}$. As shown in Example 1.3, the LMI constraint in (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) can be written in matrix form, rather than the standard form.

The dual problem of the SDP described by (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is given by \[12, pp. 168--169\] where $\mathbf{c}^{\mathsf{T}} = \begin{bmatrix} \mathbf{c}_{\mathbf{1}} & {\cdots\mathbf{c}_{\mathbf{m}}} \end{bmatrix}$. Within the context of duality, the SDP outlined in (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is denoted as the primal problem. Further details on the use of SDP duality within the context of LTI systems can be found.

When using matrix variables to describe an SDP's LMI constraints, it may be inconvenient to rewrite the objective function in the form of (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). SDP parsers, which will be discussed in Section 1.5, are capable of converting LMIs and linear objective functions in matrix form to the standard form required by most SDP solvers. An example of a linear objective function in matrix form is where $\mathbf{X}$, $\mathbf{Q}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$.

More generally, a number of convex objective functions involving matrix variables that are not explicitly written in the standard SDP form can be reformulated as SDPs. Some SDP parsers are capable of performing this conversion for the user. Two examples of such objective functions are given, with a brief explanation of how they can be reformulated in the standard SDP form.

### Example 1.4

\[12, p. 71\] Consider ${\mathcal{J}{(\mathbf{x})}} = {{\frac{1}{2}\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}} + {\mathbf{q}^{\mathsf{T}}\mathbf{x}} + \mathbf{r}}$, where $\mathbf{x}$, $\mathbf{q} \in {\mathbb{R}}^{\mathbf{n}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P} > \mathbf{0}$, and $r \in {\mathbb{R}}$. Two special cases of this objective function are listed below.

Special case when $\mathbf{q} = \mathbf{0}$ and $r = 0$: ${\mathcal{J}{(\mathbf{x})}} = {\frac{1}{2}\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}}$, where $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{P} > \mathbf{0}$.

Special case when $\mathbf{P} = {\mathbf{2} \cdot \mathbf{1}}$, $\mathbf{q} = \mathbf{0}$, and $r = 0$: ${\mathcal{J}{(\mathbf{x})}} = {\mathbf{x}^{\mathsf{T}}\mathbf{x}} = \left\| \mathbf{x} \right\|_{\mathbf{2}}^{\mathbf{2}}$, where $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$.

The optimization problem is equivalent to the optimization problem where the Schur complement (see Section 2.3) is used to reformulate the quadratic objective function into an LMI constraint.

### Example 1.5

Consider ${\mathcal{J}{(\mathbf{X})}} = {{tr}\left( {{\mathbf{X}^{\mathsf{T}}{\mathbf{P}\mathbf{X}}} + {\mathbf{Q}^{\mathsf{T}}\mathbf{X}} + {\mathbf{X}^{\mathsf{T}}\mathbf{R}} + \mathbf{S}} \right)}$, where $\mathbf{X}$, $\mathbf{Q}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathbf{P} \geq \mathbf{0}$. Four special cases of this objective function are listed below.

Special case when $\mathbf{Q} = \mathbf{R} = \mathbf{0}$ and $\mathbf{S} = \mathbf{0}$: ${\mathcal{J}{(\mathbf{X})}} = {{tr}\left( {\mathbf{X}^{\mathsf{T}}{\mathbf{P}\mathbf{X}}} \right)}$, where $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{P} > \mathbf{0}$.

Special case when $\mathbf{P} = \mathbf{1}$, $\mathbf{Q} = \mathbf{R} = \mathbf{0}$, and $\mathbf{S} = \mathbf{0}$: ${\mathcal{J}{(\mathbf{X})}} = {{tr}\left( {\mathbf{X}^{\mathsf{T}}\mathbf{X}} \right)} = \left\| \mathbf{X} \right\|_{\text{F}}^{\mathbf{2}}$, where $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$.

\[1, p. 88\] Special case when $\mathbf{P} = \mathbf{0}$, $\mathbf{R} = \mathbf{0}$ and $\mathbf{S} = \mathbf{0}$: ${\mathcal{J}{(\mathbf{X})}} = {{tr}{({\mathbf{Q}^{\mathsf{T}}\mathbf{X}})}}$, where $\mathbf{X}$, $\mathbf{Q} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$.

\[7, p. 718\] Special case when $\mathbf{P} = \mathbf{1}$, $\mathbf{Q} = \mathbf{R} = \mathbf{0}$, $\mathbf{S} = \mathbf{0}$, and $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$: ${\mathcal{J}{(\mathbf{X})}} = {{tr}{(\mathbf{X}^{\mathbf{2}})}}$, where $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$.

The optimization problem is equivalent to the optimization problem where a property involving the trace of a symmetric matrix (see Section 2.15) and the Schur complement (see Section 2.3) are used to reformulate the quadratic objective function into an LMI constraint.

Another useful convex objective function is given by ${\mathcal{J}{(\mathbf{X})}} = {\log\left( {\det{(\mathbf{X}^{- \mathbf{1}})}} \right)} = {- {\log\left( {\det{(\mathbf{X})}} \right)}}$, where $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{X} > \mathbf{0}$ \[1, p. 14\],. This objective function cannot be readily converted into the standard SDP form, but can be implemented with most SDP solvers and parsers. In particular, SDPT3 is capable of directly minimizing SDPs with objective functions of the form $- {\log\left( {\det{(\mathbf{X})}} \right)}$.

### Numerical Tools to Solve SDPs

There are many semidefinite program solvers that accept LMI constraints. Most solvers require that LMI constraints be written in the standard form shown in (1.1). This is often not convenient, as it is typical to derive LMI constraints in matrix form, such as the LMI in (1.3). LMI parsers convert LMIs in matrix form to the standard form in (1.1), allowing for a smoother transition from mathematical derivation to numerical implementation. A non-exhaustive list of SDP solvers and LMI parsers are included for reference.

### SDP Solvers

There are a number of SDP solvers available. The authors have experience with SeDuMi, SDPT3, and Mosek, though other solvers are available, such as CSDP, CVXOPT, DDS, DSDP, LMILab, PENLAB, SCS, SDPA, SMCP, and SDPNAL. There are advantages and disadvantages to each of these solvers, and sometimes one solver may give a solution to a given problem when others do not. For this reason, it is useful to have multiple solvers available. Comparisons of various LMI solvers and benchmark problems are found .

Many solvers, including SeDuMi, SDPT3, are available for free, while Mosek is a commercial software package. A free academic license of Mosek can be requested for research in academic institutions or educational purposes.

### LMI Parsers

LMI parsers allow the user to define the SDP to be solved within standard software environments, and often in a more convenient matrix form. A number of openly-distributed LMI parsers are available for use within different software environments. The following is a non-exhaustive list of LMI parsers and the solvers they are known to be compatible , sorted by software environment.

Yalmip. Solvers: CSDP, DSDP, LMILab, Mosek, PENLAB, SCS, SDPA, SDPT3, SDPNAL, and SeDuMi.

CVX. Solvers: Mosek, SDPT3, and SeDuMi.

LMILab. Features an internal solver.

CVXPY. Solvers: SCS. Other solvers can be installed separately.

PICOS. Solvers: CVXOPT, Mosek, and SMCP.

Irene. Solvers: CSDP, CVXOPT, DSDP, and SDPA.

PyLMI-SDP. Solvers: CVXOPT and SDPA.

Convex.jl. Solvers: Mosek and SCS.

JuMP. Solvers: Mosek and SCS.

SciYalmip. Solvers: CSDP and SDPA. Also features the internal solver LMISOLVER.

NSPYalmip. Solvers: CSDP and SeDuMi.

## LMI Properties and Tricks

This section presents a compilation of LMI properties and tricks from the literature. Many of these properties are used in subsequent sections to reformulate LMIs or transform matrix inequalities into LMIs.

### Change of Variables \[1, pp. 100--101\], \[4, Sec. 12.3.1\]

A BMI can sometimes be converted into an LMI using a change of variables.

### Example 2.1

\[4, Example 12.5, Sec. 12.3.1\] Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$. The matrix inequality given by is bilinear in the variables $\mathbf{Q}$ and $\mathbf{K}$. Define a change of variable as $\mathbf{F} = {\mathbf{K}\mathbf{Q}}$ to obtain which is an LMI in the variables $\mathbf{Q}$ and $\mathbf{F}$. Once this LMI is solved, the original variable can be recovered by $\mathbf{K} = {\mathbf{F}\mathbf{Q}}^{- \mathbf{1}}$.

It is important that a change of variables is chosen to be a one-to-one mapping in order for the new matrix inequality to be equivalent to the original matrix inequality. In Example 2.1 the change of variable $\mathbf{F} = {\mathbf{K}\mathbf{Q}}$ is a one-to-one mapping since $\mathbf{Q}^{- \mathbf{1}}$ is invertible, which gives a unique solution for the reverse change of variable $\mathbf{K} = {\mathbf{F}\mathbf{Q}}^{- \mathbf{1}}$.

### Congruence Transformation \[1, p. 15\], \[4, Sec. 12.3.2\]

Consider $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where ${\text{rank}{(\mathbf{W})}} = \mathbf{n}$. The matrix inequality $\mathbf{Q} < \mathbf{0}$ is satisfied if and only if ${\mathbf{W}\mathbf{Q}\mathbf{W}}^{\mathsf{T}} < \mathbf{0}$ or equivalently ${\mathbf{W}^{\mathsf{T}}{\mathbf{Q}\mathbf{W}}} < \mathbf{0}$.

### Example 2.2

\[4, Example 12.6, Sec. 12.3.2\] Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{C}^{\mathsf{T}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{V} \in {\mathbb{S}}^{\mathbf{p}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{V} > \mathbf{0}$. The matrix inequality given by is linear in the variable $\mathbf{V}$ and bilinear in the variable pair $(\mathbf{P},\mathbf{K})$. Choose the matrix $\mathbf{W} = {\text{diag}{\{\mathbf{P}^{- \mathbf{1}},\mathbf{V}^{- \mathbf{1}}\}}}$ to obtain an equivalent BMI given by Using a change of variable $\mathbf{X} = \mathbf{P}^{- \mathbf{1}}$, $\mathbf{U} = \mathbf{V}^{- \mathbf{1}}$, and $\mathbf{F} = {\mathbf{K}\mathbf{V}}^{- \mathbf{1}}$, (2.1) becomes which is an LMI in the variables $\mathbf{X}$, $\mathbf{U}$, and $\mathbf{F}$. Once (2.2) is solved, the original variable $\mathbf{K}$ is recovered by the reverse change of variable $\mathbf{K} = {\mathbf{F}\mathbf{U}}^{- \mathbf{1}}$.

A congruence transformation preserves the definiteness of a matrix by ensuring that $\mathbf{Q} < \mathbf{0}$ and ${\mathbf{W}\mathbf{Q}\mathbf{W}}^{\mathsf{T}} < \mathbf{0}$ are equivalent. A congruence transformation is related, but not equivalent to a similarity transformation ${\mathbf{T}\mathbf{Q}\mathbf{T}}^{- \mathbf{1}}$, which preserves not only the definiteness, but also the eigenvalues of a matrix. A congruence transformation is equivalent to a similarity transformation in the special case when $\mathbf{W}^{\mathsf{T}} = \mathbf{W}^{- \mathbf{1}}$.

### Schur Complement

### Strict Schur Complement \[1, pp. 7--8\], \[4, Sec. 12.3.3\]

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C} \in {\mathbb{S}}^{\mathbf{m}}$. The following statements are equivalent.

\mathbf{B}^{\mathsf{T}} & \mathbf{C} ${\mathbf{A} - {{\mathbf{B}\mathbf{C}}^{- \mathbf{1}}\mathbf{B}^{\mathsf{T}}}} < \mathbf{0}$, $\mathbf{C} < \mathbf{0}$. ${\mathbf{C} - {\mathbf{B}^{\mathsf{T}}\mathbf{A}^{- \mathbf{1}}\mathbf{B}}} < \mathbf{0}$, $\mathbf{A} < \mathbf{0}$.

### Nonstrict Schur Complement \[1, p. 28\]

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C} \in {\mathbb{S}}^{\mathbf{m}}$. The following statements are equivalent.

\mathbf{B}^{\mathsf{T}} & \mathbf{C} \end{bmatrix} \leq 0$. ${\mathbf{A} - {{\mathbf{B}\mathbf{C}}^{+}\mathbf{B}^{\mathsf{T}}}} < \mathbf{0}$, $\mathbf{C} \leq \mathbf{0}$, ${\mathbf{B}{({\mathbf{1} - {\mathbf{C}\mathbf{C}}^{+}})}} = \mathbf{0}$, where $\mathbf{C}^{+}$ is the Moore-Penrose inverse of $\mathbf{C}$. ${\mathbf{C} - {\mathbf{B}^{\mathsf{T}}\mathbf{A}^{+}\mathbf{B}}} < \mathbf{0}$, $\mathbf{A} \leq \mathbf{0}$, ${\mathbf{B}^{\mathsf{T}}{({\mathbf{1} - {\mathbf{A}\mathbf{A}}^{+}})}} = \mathbf{0}$, where $\mathbf{A}^{+}$ is the Moore-Penrose inverse of $\mathbf{A}$.

### Schur Complement Lemma-Based Properties

\[3, p. 108\],\[61, p. 100\] Consider $\mathbf{P}_{\mathbf{1}\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{2}}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{P}_{\mathbf{1}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{P}_{\mathbf{2}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, and $\mathbf{P}_{\mathbf{3}\mathbf{3}} \in {\mathbb{S}}^{\mathbf{p}}$. There exists $\mathbf{X}$ such that Any matrix $\mathbf{X} \in {\mathbb{S}}^{\mathbf{m}}$ satisfying is a solution to (2.3). That is, (2.4)$\Longrightarrow$ (2.3).

\[3, pp. 108--109\],\[61, p. 101\] Consider $\mathbf{P}_{\mathbf{1}\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{1}\mathbf{2}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{P}_{\mathbf{1}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{P}_{\mathbf{2}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, and $\mathbf{P}_{\mathbf{3}\mathbf{3}} \in {\mathbb{S}}^{\mathbf{p}}$. There exists $\mathbf{X}$ such that If the two matrix inequalities in (2.6) hold, then a solution to (2.5) is given by

### Proof

Necessity ((2.5) $\Longrightarrow$ (2.6)) comes from the requirement that the submatrices corresponding to the principle minors of (2.5) are negative definite. Sufficiency ((2.6) $\Longrightarrow$ (2.5)) is shown by rewriting the matrix inequalities of (2.6) in the equivalent form Concatenating the two matrix inequalities in (2.7) and choosing $\mathbf{X} = {{\mathbf{P}_{\mathbf{2}\mathbf{3}}\mathbf{P}_{\mathbf{3}\mathbf{3}}^{- \mathbf{1}}\mathbf{P}_{\mathbf{1}\mathbf{3}}^{\mathsf{T}}} - \mathbf{P}_{\mathbf{1}\mathbf{2}}^{\mathsf{T}}}$ gives the equivalent matrix inequality which is equivalent to (2.5) using the Schur complement lemma. ∎ Permutation of the columns and rows of (2.5) yields the following equivalent result.

\[5, pp. 41--42\] Consider $\mathbf{P}_{\mathbf{1}\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{1}\mathbf{2}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{P}_{\mathbf{1}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{P}_{\mathbf{2}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, and $\mathbf{P}_{\mathbf{3}\mathbf{3}} \in {\mathbb{S}}^{\mathbf{p}}$. There exists $\mathbf{X}$ such that If the matrix inequalities in (2.9) hold, then a solution to (2.8) is given by \[5, p. 41\] Consider $\mathbf{P}_{\mathbf{1}\mathbf{1}}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{P}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{X} > \mathbf{0}$. There exists $\mathbf{X}$ such that

### Proof

The matrix inequality in (2.10) can be rewritten using the Schur complement lemma as, \[63, p. 319--320\] Consider $\mathbf{P}_{\mathbf{1}\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{P}_{\mathbf{3}\mathbf{3}} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$. There exists $\mathbf{X}$ such that

### Proof

The proof is found. ∎ \[63, p. 320\] Consider $\mathbf{P}_{\mathbf{1}\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{P}_{\mathbf{2}\mathbf{3}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{P}_{\mathbf{3}\mathbf{3}} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$. There exists $\mathbf{X}$ such that

### Proof

The proof is found. ∎ Consider $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{H} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$. The matrix inequality given by For $\mathbf{G} = \mathbf{P}$, this relationship becomes the Schur complement lemma.

### Proof

Using the Schur complement lemma on (2.12) gives Using the property ${{\mathbf{G} + \mathbf{G}^{\mathsf{T}}} - \mathbf{P}} \leq {\mathbf{G}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{G}}$ (see the special case of Young's relation in Section 2.4.3 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), or equivalently $\left({{\mathbf{G} + \mathbf{G}^{\mathsf{T}}} - \mathbf{P}} \right)^{- 1} \geq {\mathbf{G}^{- \mathbf{1}}{\mathbf{P}\mathbf{G}}^{- \mathsf{T}}}$ gives Variations of this property are listed as follows.

Consider $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{H} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$. The matrix inequality given by Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{m}}$, and $\beta \in {\mathbb{R}}$. The matrix inequality given by implies the matrix inequality ${\mathbf{A} + {\mathbf{B}\mathbf{P}\mathbf{B}}^{\mathsf{T}}} < \mathbf{0}$., \[63, p. 321\] Consider $\mathbf{P}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{2}}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{q}}$, $\mathbf{Q}_{\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{Q}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{p}}$, $\mathbf{R}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{R}_{\mathbf{2}} \in {\mathbb{S}}^{\mathbf{p}}$. The matrix inequalities given by are satisfied if and only if

### Proof

The proof is found in and is very similar to the proof of Property 2. ∎ Consider $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{Q} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, and $\mathbf{E} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The matrix inequalities given by are satisfied if and only if

### Proof

The proof is found in and is very similar to the proof of Property 2. ∎, \[2, p. 229\] Consider $\mathbf{P}_{\mathbf{1}}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{P}_{\mathbf{2}}$, $\mathbf{Q}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{P}_{\mathbf{3}}$, $\mathbf{Q}_{\mathbf{3}} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{P}_{\mathbf{3}} > \mathbf{0}$, $\mathbf{Q}_{\mathbf{1}} > \mathbf{0}$, and $\mathbf{Q}_{\mathbf{3}} > \mathbf{0}$. There exist $\mathbf{P}_{\mathbf{2}}$, $\mathbf{P}_{\mathbf{3}}$, $\mathbf{Q}_{\mathbf{2}}$, and $\mathbf{Q}_{\mathbf{3}}$ such that Provided $\mathbf{P}_{\mathbf{1}}$ and $\mathbf{Q}_{\mathbf{1}}$ satisfy (2.20), a solution to (2.19) is given by $\mathbf{P}_{\mathbf{3}} = \mathbf{1}$, $\mathbf{Q}_{\mathbf{2}} = {- {\mathbf{Q}_{\mathbf{1}}\mathbf{P}_{\mathbf{2}}}}$, $\mathbf{Q}_{\mathbf{3}} = {{\mathbf{P}_{\mathbf{2}}^{\mathsf{T}}\mathbf{Q}_{\mathbf{1}}\mathbf{P}_{\mathbf{2}}} + \mathbf{1}}$, and $\mathbf{P}_{\mathbf{2}}$ satisfies ${\mathbf{P}_{\mathbf{2}}\mathbf{P}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{P}_{\mathbf{1}} - \mathbf{Q}_{\mathbf{1}}^{- \mathbf{1}}}$.

\[68, pp. 13--14\] Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{Q} > \mathbf{0}$, and $\epsilon \geq 1$. The matrix inequality given by

### Proof

Since $\mathbf{P} > \mathbf{0}$, $\mathbf{Q} > \mathbf{0}$, and $\epsilon \geq 1$, it is known that ${{({\epsilon - 1})}\mathbf{X}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{X}} \geq \mathbf{0}$ and ${{({\epsilon - 1})}\mathbf{Y}^{\mathsf{T}}\mathbf{Q}^{- \mathbf{1}}\mathbf{Y}} \geq \mathbf{0}$. These inequalities are rewritten as Applying the Schur complement lemma to the expressions in (2.22) results in The matrix inequalities in (2.23) imply Applying the Schur complement lemma to (2.24) yields (Linearization Lemma \[3, p. 92\]) Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{T} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{q}}$, ${\mathbf{Y}{(\mathbf{v})}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, ${\mathbf{Q}{(\mathbf{v})}} \in {\mathbb{S}}^{\mathbf{n}}$, ${\mathbf{R}{(\mathbf{v})}} \in {\mathbb{S}}^{\mathbf{m}}$, and ${\mathbf{U}{(\mathbf{v})}} \in {\mathbb{S}}^{\mathbf{q}}$, where $\mathbf{Y}{(\mathbf{v})}$, $\mathbf{Q}{(\mathbf{v})}$, and $\mathbf{R}{(\mathbf{v})}$ depend affinely on the parameter $v$, and $\mathbf{R}{(\mathbf{v})}$ can be decomposed as ${\mathbf{R}{(\mathbf{v})}} = {{\mathbf{T}\mathbf{U}}^{- \mathbf{1}}{(\mathbf{v})}\mathbf{T}^{- \mathbf{1}}}$. The matrix inequalities ${\mathbf{U}{(\mathbf{v})}} > \mathbf{0}$ and

### Young's Relation (Completion of the Squares)

### Young's Relation

Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. The matrix inequality given by is known as Young's relation or Young's inequality.

Young's relation can be derived from a completion of the squares as follows. which is Young's relation.

### Reformulation of Young's Relation

Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. The matrix inequality given by is a reformulation of Young's relation.

### Special Cases of Young's Relation

Consider $\mathbf{X}$,$\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$. A special case of Young's relation with $\mathbf{S} = \mathbf{1}$ is given by Consider $\overline{\mathbf{X}}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\overline{\mathbf{X}} = {- \mathbf{X}}$ is given by Consider $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{G}$ and $\mathbf{Y} = \mathbf{1}$ is given by \[7, p. 737\] Consider $\mathbf{P}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{X}^{\mathsf{T}} = \mathbf{P}$ and $\mathbf{Y} = \mathbf{1}$ is given by \[7, p. 732\] Consider $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\alpha \in {\mathbb{R}}_{> 0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{G}$, $\mathbf{Y} = \mathbf{1}$, and $\mathbf{S} = {\alpha\mathbf{1}}$ is given by \[7, p. 732\] Consider $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\alpha \in {\mathbb{R}}_{> 0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{G}$, $\mathbf{Y} = \mathbf{G}^{\mathsf{T}}$, and $\mathbf{S} = {\alpha\mathbf{1}}$ is given by \[7, p. 732\] Consider $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{1}$, $\mathbf{Y} = \mathbf{1}$ is given by Consider $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$ and $\alpha \in {\mathbb{R}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{1}$, $\mathbf{Y} = {\alpha\mathbf{1}}$ is given by \[72, p. 38\], Consider the column matrices $\mathbf{x}$, $\mathbf{y} \in {\mathbb{R}}^{\mathbf{n}}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\mathbf{X} = \mathbf{x}$ and $\mathbf{Y} = \mathbf{y}$ is given by Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{q}}$, $\overline{\mathbf{Y}} \in {\mathbb{R}}^{q \times m}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of Young's relation with $\mathbf{Y} = {\mathbf{F}\overline{\mathbf{Y}}}$ is given by \[5, pp. 29--30\] Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\overline{\mathbf{Y}} \in {\mathbb{R}}^{n \times m}$, $\mathbf{F} \in {\mathbb{S}}^{\mathbf{n}}$, and $\delta \in {\mathbb{R}}_{> 0}$, where $\mathbf{F} > \mathbf{0}$. A special case of Young's relation with $\mathbf{Y} = {\mathbf{F}\overline{\mathbf{Y}}}$ and $\mathbf{S} = \left({\delta\mathbf{F}} \right)^{- \mathbf{1}}$ is given by Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{q}}$, $\overline{\mathbf{Y}} \in {\mathbb{R}}^{q \times m}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$. A special case of the matrix inequality (2.27 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) with $\mathbf{S} = {\epsilon\mathbf{1}}$ is given by Proof. Substituting $\mathbf{S} = {\epsilon\mathbf{1}}$ into (2.27 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) yields Premultiplying ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$ by ${\overline{\mathbf{Y}}}^{\mathsf{T}}$, postmultiplying by $\overline{\mathbf{Y}}$, and multiplying both sides by $\epsilon^{- 1}$ leads to Substituting (2.30 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) into (2.29 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) yields (2.28 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$ Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{q}}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{m}}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. Applying Young's relation gives the matrix inequality Proof. Expanding the left-hand side of (2.31 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) yields From Young's relation it can be shown that Substituting (2.33 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) into (2.32 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) gives (2.31 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$ Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of (2.31 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) with $\mathbf{F} = \mathbf{S}$ is given by \[72, p. 38\], Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{r}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{r} \times \mathbf{q}}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{m}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$, and ${\mathbf{P} - {\epsilon{\mathbf{D}\mathbf{D}}^{\mathsf{T}}}} > \mathbf{0}$. Then the matrix inequality given by where $\left({{\epsilon^{- 1}\mathbf{1}} - {\mathbf{D}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{D}}} \right)^{- {1/2}}$ exists due to the matrix inversion lemma \[7, p. 304\] since ${\mathbf{P} - {\epsilon{\mathbf{D}\mathbf{D}}^{\mathsf{T}}}} > \mathbf{0}$. Expanding the terms in ${\mathbf{W}^{\mathsf{T}}\mathbf{W}} \geq \mathbf{0}$ yields Adding $\mathbf{X}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{X}$ to both sides of the inequality and rearranging gives Using the matrix inversion lemma \[7, p. 304\], it is known that Substituting (2.36 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) into (2.35 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), factoring the left side of the inequality, and knowing ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$ gives (2.34 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$ Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{r}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{r} \times \mathbf{q}}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{m}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$, and ${{\epsilon\mathbf{1}} - {\mathbf{D}^{\mathsf{T}}{\mathbf{P}\mathbf{D}}}} > \mathbf{0}$. Then the matrix inequality given by where $\left({{\epsilon\mathbf{1}} - {\mathbf{D}^{\mathsf{T}}{\mathbf{P}\mathbf{D}}}} \right)^{- {1/2}}$ exists since ${{\epsilon\mathbf{1}} - {\mathbf{D}^{\mathsf{T}}{\mathbf{P}\mathbf{D}}}} > \mathbf{0}$. Expanding the terms in ${\mathbf{W}^{\mathsf{T}}\mathbf{W}} \geq \mathbf{0}$ yields Adding $\mathbf{X}^{\mathsf{T}}{\mathbf{P}\mathbf{X}}$ to both sides of the inequality and rearranging gives Factoring the left side of the inequality and knowing ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \geq \mathbf{1}$ gives (2.37 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$ \[76, p. 11\] Consider $\mathbf{N} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{H} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{J} \in {\mathbb{S}}^{\mathbf{n}}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where $\mathbf{J} > \mathbf{0}$ and ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$. With some manipulation, a special case of (2.27 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) with $\mathbf{X} = {\mathbf{H}^{\mathsf{T}}\mathbf{E}^{\mathsf{T}}\mathbf{N}^{\mathsf{T}}}$ and $\overline{\mathbf{Y}} = \mathbf{1}$ is given by \[76, p. 11\] Consider $\mathbf{N} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{H} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{J} \in {\mathbb{S}}^{\mathbf{n}}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where $\mathbf{J} > \mathbf{0}$ and ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$. With some manipulation, a special case of (2.27 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) with $\mathbf{X} = {\mathbf{N}\mathbf{H}\mathbf{E}}$ and $\overline{\mathbf{Y}} = \mathbf{1}$ is given by

### Young's Relation-Based Properties

Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$. The matrix inequality given by is satisfied if and only if there exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{G}_{\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{G}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{H} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{P} > \mathbf{0}$, such that Consider $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{W} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X}$ is full rank and $\mathbf{W} > \mathbf{0}$. The matrix inequality given by is satisfied if there exists $\lambda \in {\mathbb{R}}_{> 0}$ such that \[7, p. 737\] Consider $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Q} > \mathbf{0}$. The matrix inequality given by

### Iterative Convex Overbounding

Iterative convex overbounding is a technique based on Young's relation that is useful when solving an optimization problem with a BMI constraint.

Consider the matrices $\mathbf{Q} = \mathbf{Q}^{\mathsf{T}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{q}}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{r}}$, and $\mathbf{C} \in {\mathbb{R}}^{\mathbf{r} \times \mathbf{n}}$, where $\mathbf{S}$ and $\mathbf{R}$ are design variables in the BMI given by Suppose that $\mathbf{S}_{\mathbf{0}}$ and $\mathbf{R}_{\mathbf{0}}$ are known to satisfy (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). The BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where ${\mathbf{\phi}{(\mathbf{R},\mathbf{S})}} = {\mathbf{B}\left({{{\mathbf{R}\mathbf{D}\mathbf{S}}_{\mathbf{0}} + {\mathbf{R}_{\mathbf{0}}{\mathbf{D}\mathbf{S}}}} - {\mathbf{R}_{\mathbf{0}}{\mathbf{D}\mathbf{S}}_{\mathbf{0}}}} \right)\mathbf{C}}$, $\mathbf{W} > \mathbf{0}$ is an arbitrary matrix, $\mathbf{D} = {\mathbf{U}\mathbf{V}}$, and the matrices $\mathbf{U}$ and $\mathbf{V}^{\mathsf{T}}$ have full column rank. The LMI of (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is equivalent to the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, and is therefore non-conservative for values of $\mathbf{R}$ and $\mathbf{S}$ and are close to the previously known solutions $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$.

Alternatively, the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where $\mathbf{Z} > \mathbf{0}$ is an arbitrary matrix, $\mathbf{D} = {\mathbf{U}\mathbf{V}}$, and the matrices $\mathbf{U}$ and $\mathbf{V}^{\mathsf{T}}$ have full column rank. Again, the LMI of (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is equivalent to the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, and is therefore non-conservative for values of $\mathbf{R}$ and $\mathbf{S}$ and are close to the previously known solutions $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$.

A benefit of convex overbounding compared to a linearization approach, is that in addition to ensuring conservatism or error is reduced in the neighborhood of $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, the LMIs of (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) imply (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")).

Iterative convex overbounding is particularly useful when used to solve an optimization problem with BMI constraints. For example, choose $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$ that are initial feasible solutions to (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). Then solve for $\mathbf{R}$ and $\mathbf{S}$ that minimize a specified objective function and satisfy (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) or (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), which imply (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) without conservatism when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$. Set $\mathbf{R}_{\mathbf{0}} = \mathbf{R}$ and $\mathbf{S}_{\mathbf{0}} = \mathbf{S}$, and repeat until the objective function meets a specified stopping criteria. The benefits of this procedure are that its individual steps are convex optimization problems with very little conservatism in the neighborhood of the solution from the previous iteration, and that it tends to converge quickly to a solution. However, there is no guarantee that the method will converge to even a local solution.

### Example 2.3

Consider a special case of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) given by where $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{S} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. The BMI of (2.41 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where $\mathbf{W} > \mathbf{0}$ is an arbitrary matrix. Alternatively, the BMI of (2.41 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where $\mathbf{Z} > \mathbf{0}$ is an arbitrary matrix.

### Projection Lemma (Matrix Elimination Lemma)

### Strict Projection Lemma, \[1, pp. 22--23\], \[3, pp. 109--110\], \[4, Sec. 12.3.5\]

Consider $\mathbf{\Psi} \in {\mathbb{S}}^{n}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{\Lambda} \in {\mathbb{R}}^{m \times p}$, and $\mathbf{H} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$. There exists $\mathbf{\Lambda}$ such that where ${\mathcal{R}{(\mathbf{N}_{\mathbf{G}})}} = {\mathcal{N}{(\mathbf{G}^{\mathsf{T}})}}$ and ${\mathcal{R}{(\mathbf{N}_{\mathbf{H}})}} = {\mathcal{N}{(\mathbf{H}^{\mathsf{T}})}}$.

### Nonstrict Projection Lemma \[80, p. 93\]

Consider $\mathbf{\Psi} \in {\mathbb{S}}^{n}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{\Lambda} \in {\mathbb{R}}^{m \times p}$, and $\mathbf{H} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, where $\mathcal{R}{(\mathbf{G})}$ and $\mathcal{R}{(\mathbf{H})}$ are linearly independent. There exists $\mathbf{\Lambda}$ such that where ${\mathcal{R}{(\mathbf{N}_{\mathbf{G}})}} = {\mathcal{N}{(\mathbf{G}^{\mathsf{T}})}}$ and ${\mathcal{R}{(\mathbf{N}_{\mathbf{H}})}} = {\mathcal{N}{(\mathbf{H}^{\mathsf{T}})}}$.

### Reciprocal Projection Lemma

Consider $\mathbf{P}$, $\mathbf{\Psi} \in {\mathbb{S}}^{n}$ and $\mathbf{W}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. There exists $\mathbf{W}$ such that if and only if ${\mathbf{\Psi} + \mathbf{S} + \mathbf{S}^{\mathsf{T}}} < \mathbf{0}$.

### Projection Lemma-Based Properties

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B}$, $\mathbf{J} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{m}}$. The matrix inequality given by implies the matrix inequality If the matrices $\mathbf{J}$ and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.43 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.44 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

Consider $\mathbf{T} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{A}$, $\mathbf{J}$, $\mathbf{G}$, $\mathbf{P} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The matrix inequality given by implies the matrix inequality If the matrices $\mathbf{J}$ and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.45 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.46 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

Consider $\mathbf{T}_{\mathbf{1}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{A}$, $\mathbf{J}_{\mathbf{1}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{T}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{J}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{T}_{\mathbf{3}} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{T}_{\mathbf{3}} < \mathbf{0}$. The matrix inequality given by implies the matrix inequality If the matrices $\mathbf{J}_{\mathbf{1}}$, $\mathbf{J}_{\mathbf{2}}$, and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.47 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.48 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

\[76, p. 9\] Consider $\mathbf{T} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{A}$, $\mathbf{G}$, $\mathbf{P} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\beta \in {\mathbb{R}}$, where $\mathbf{T} < \mathbf{0}$. The matrix inequality given by implies the matrix inequality ${\mathbf{T} + {\mathbf{A}^{\mathsf{T}}\mathbf{P}^{\mathsf{T}}} + {\mathbf{P}\mathbf{A}}} < \mathbf{0}$.

### Finsler's Lemma

### Finsler's Lemma \[1, pp. 22--23\], \[4, Sec. 12.3.5\],

Consider $\mathbf{\Psi} \in {\mathbb{S}}^{n}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{\Lambda} \in {\mathbb{R}}^{m \times p}$, $\mathbf{H} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, and $\sigma \in {\mathbb{R}}$. There exists $\mathbf{\Lambda}$ such that if and only if there exists $\sigma$ such that

### Alternative Form of Finsler's Lemma, \[87, pp. 90--97\], \[88, pp. 41--48\]

Consider $\mathbf{\Psi} \in {\mathbb{S}}^{n}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$, where ${\text{rank}{(\mathbf{Z})}} < \mathbf{n}$. The following statements are equivalent. is satisfied for all $\mathbf{x}$ satisfying ${\mathbf{Z}\mathbf{x}} = \mathbf{0}$, where $\mathbf{x} \neq \mathbf{0}$.

The matrix inequality is satisfied, where ${\mathcal{R}{(\mathbf{N}_{\mathbf{Z}})}} = {\mathcal{N}{(\mathbf{Z})}}$.

There exists $\sigma \in {\mathbb{R}}$ such that There exists $\mathbf{X} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$ such that

### Modified Finsler's Lemma \[72, p. 37\],

Consider $\mathbf{\Psi} \in {\mathbb{S}}^{n}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{\Lambda} \in {\mathbb{R}}^{m \times p}$, $\mathbf{H} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, and $\epsilon \in {\mathbb{R}}_{> 0}$, where ${\mathbf{\Lambda}^{\mathsf{T}}\mathbf{\Lambda}} \leq \mathbf{R}$ and $\mathbf{R} > \mathbf{0}$. There exists $\mathbf{\Lambda}$ such that if and only if there exists $\epsilon$ such that

### Proof

The proof of (2.50) $\Longrightarrow$ (2.49) follows from a completion of the squares argument. The authors are not aware of a complete proof of (2.49) $\Longrightarrow$ (2.50), so use this identity with caution. ∎

### Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma

The Schur complement, Young's relation, and the projection lemma are three of the most common tools used to transform a BMI into an LMI. The sign of the BMI determines which one is suitable to transform the BMI into an LMI. For example, consider the case of a BMI in the variable $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$ of the form where $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{S} > \mathbf{0}$. The Schur complement is used to obtain an equivalent LMI given by This LMI can also be written as Applying the Projection Lemma, it is known that there exists $\mathbf{Y}$ satisfying (2.52) if and only if $\mathbf{P} < \mathbf{0}$ and $\mathbf{S}^{- \mathbf{1}} > \mathbf{0}$, since ${\mathcal{N}\left(\begin{bmatrix} \end{bmatrix} \right)} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, ${\mathcal{N}\left(\begin{bmatrix} \end{bmatrix} \right)} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, and Notice that the Projection Lemma gives two matrix inequalities that do not depend on the variable $\mathbf{Y}$. This is why the Projection Lemma is also known as the Matrix Elimination Lemma.

Alternatively, consider the BMI where $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{S} > \mathbf{0}$. Young's relation is used to obtain an LMI in $\mathbf{Y}$ given by which implies the BMI of (2.53). Notice that (2.54) involves a new variable $\mathbf{X} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. Using the Schur complement on (2.54) yields which is an LMI in $\mathbf{Y}$ for a fixed $\mathbf{X}$.

It is desirable to use the Schur complement of the Projection Lemma over Young's relation whenever possible, as they provides an LMI or LMIs that are equivalent to the original BMI. When using Young's relation, the resulting LMI implies the original BMI, but is not equivalent. This introduces conservatism into an optimization problem.

If a previously-known solution $\mathbf{Y}_{\mathbf{0}}$ to (2.53) is available, then convex overbounding can be used to reduce conservatism in the neighborhood of $\mathbf{Y}_{\mathbf{0}}$. The BMI of (2.53) is equivalent to the BMI Since the term $\left({\mathbf{Y} - \mathbf{Y}_{\mathbf{0}}} \right)^{\mathsf{T}}\mathbf{S}\left({\mathbf{Y} - \mathbf{Y}_{\mathbf{0}}} \right)$ is positive definite, (2.55) is implied by the LMI The LMI of (2.56) is in general conservative, but this conservatism disappears when $\mathbf{Y} = \mathbf{Y}_{\mathbf{0}}$ and is reduced when $\mathbf{Y}$ is close to $\mathbf{Y}_{\mathbf{0}}$.

### Dilation

Matrix inequalities can be dilated to obtain a larger matrix inequality, often with additional design variables. This can be a useful technique to separate design variables in a BMI.

A common technique to dilate an LMI involves the use the projection lemma in reverse or the reciprocal projection lemma. For instance, consider the following example taken from and inspired by the dilated bounded real lemma matrix inequality in \[5, pp. 153--155\] involving the matrices $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$. The matrix inequality Since $\mathbf{P} > \mathbf{0}$, it is also known that which can be rewritten as The matrix inequalities in (2.58) and (2.59) are in the form of the strict projection lemma. Specifically, (2.58) is in the form of ${\mathbf{N}_{\mathbf{G}}^{\mathsf{T}}{(\mathbf{A})}\mathbf{\Phi}{(\mathbf{P})}\mathbf{N}_{\mathbf{G}}{(\mathbf{A})}} < \mathbf{0}$, where The matrix inequality of (2.59) is in the form of ${\mathbf{N}_{\mathbf{H}}^{\mathsf{T}}\mathbf{\Phi}{(\mathbf{P})}\mathbf{N}_{\mathbf{H}}} < \mathbf{0}$, where The projection lemma states that (2.58) and (2.59) are equivalent to where ${\mathcal{N}{({\mathbf{G}^{\mathsf{T}}{(\mathbf{A})}})}} = {\mathcal{R}{({\mathbf{N}_{\mathbf{G}}{(\mathbf{A})}})}}$, ${\mathcal{N}{(\mathbf{H}^{\mathsf{T}})}} = {\mathcal{R}{(\mathbf{N}_{\mathbf{H}})}}$, and $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. Choosing the matrix inequality of (2.60) can be rewritten as Therefore, the matrix inequality of (2.58) with $\mathbf{P} > \mathbf{0}$ is equivalent to the dilated matrix inequality of (2.61).

### Examples of Dilated Matrix Inequalities

Examples of some useful dilated matrix inequalities are presented here, while dilated forms of a number of important matrix inequalities are included as equivalent matrix inequalities in their respective sections.

Consider the matrices $\mathbf{A}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{\Delta} \in {\mathbb{R}}^{m \times n}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\delta_{1}$, $\delta_{2}$, $a$, $b \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $b = a^{- 1}$. The matrix inequality is equivalent to the matrix inequality Moreover, for every solution $\mathbf{P} > \mathbf{0}$ of (2.62), $\mathbf{P}$ and $\mathbf{G} = {- {\mathbf{a}\left({\mathbf{A} - {\mathbf{a}\mathbf{1}}} \right)^{- \mathbf{1}}\mathbf{P}}}$ will be solutions of (2.63).

\[76, pp. 7--8\] Consider the matrices $\mathbf{A}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{P}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{p}}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{R} > \mathbf{0}$, $\mathbf{S} > \mathbf{0}$, and $\mathbf{X} > \mathbf{0}$. The matrix inequality given by implies the matrix inequality \[76, p. 9\] Consider the matrices $\mathbf{A}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{Q}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{p}}$, where $\mathbf{Q} > \mathbf{0}$, $\mathbf{R} > \mathbf{0}$, $\mathbf{S} > \mathbf{0}$, and $\mathbf{X} > \mathbf{0}$. The matrix inequality given by implies the matrix inequality

### The S-Procedure \[1, pp. 23--24\], \[4, Sec. 12.3.4\],

Consider $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$ and the quadratic functions ${F_{0}{(\mathbf{x})}}:{{\mathbb{R}}^{\mathbf{n}}\rightarrow{\mathbb{R}}}$, ${F_{i}{(\mathbf{x})}}:{{\mathbb{R}}^{\mathbf{n}}\rightarrow{\mathbb{R}}}$, where $i = {1,\ldots,m}$. The inequality ${F_{0}{(\mathbf{x})}} \leq \mathbf{0}$ is satisfied when ${F_{i}{(\mathbf{x})}} \geq \mathbf{0}$, $i = {1,\ldots,m}$, if there exist $\tau_{i} \in {\mathbb{R}}_{\geq 0}$, $i = {1,\ldots,m}$ such that If $m = 1$, then this becomes a necessary and sufficient condition, that is, ${F_{0}{(\mathbf{x})}} \leq \mathbf{0}$ is satisfied when ${F_{1}{(\mathbf{x})}} \geq \mathbf{0}$ if and only if there exists $\tau_{1} \in {\mathbb{R}}_{\geq 0}$ such that ${{F_{0}{(\mathbf{x})}} + {\tau_{\mathbf{1}}\mathbf{F}_{\mathbf{1}}{(\mathbf{x})}}} \leq \mathbf{0}$.

### Example 2.4

\[1, p. 24\], \[4, Example 12.8, Sec. 12.3.4\] Consider $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$, $\mathbf{u} \in {\mathbb{R}}^{\mathbf{m}}$, $\gamma \in {\mathbb{R}}_{> 0}$, and $\tau \in {\mathbb{R}}_{\geq 0}$. There exists $\mathbf{P} > \mathbf{0}$ such that when $\mathbf{x} \neq \mathbf{0}$ and $\mathbf{u}$ satisfy the constraint ${\mathbf{u}^{\mathsf{T}}\mathbf{u}} \leq {\gamma\mathbf{x}^{\mathsf{T}}\mathbf{C}^{\mathsf{T}}{\mathbf{C}\mathbf{x}}}$ if and only if there exist $\mathbf{P} > \mathbf{0}$ and $\tau \in {\mathbb{R}}_{\geq 0}$ such that

### Dualization Lemma \[3, pp. 105--106\]

Consider $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and the subspaces $\mathcal{U}$, $\mathcal{V}$, where $\mathbf{P}$ is invertible and ${\mathcal{U} + \mathcal{V}} = {\mathbb{R}}^{n}$. The following are equivalent. ${\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}} < \mathbf{0}$ for all $\mathbf{x} \in {\mathcal{U} \smallsetminus {\{\mathbf{0}\}}}$ and ${\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}} \geq \mathbf{0}$ for all $\mathbf{x} \in \mathcal{V}$. ${\mathbf{x}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{x}} > \mathbf{0}$ for all $\mathbf{x} \in {\mathcal{U}^{\perp} \smallsetminus {\{\mathbf{0}\}}}$ and ${\mathbf{x}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{x}} \leq \mathbf{0}$ for all $\mathbf{x} \in \mathcal{V}^{\perp}$.

### Example 2.5

\[3, pp. 105--106\] Consider the matrices $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{M} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, where $\mathbf{R} \geq \mathbf{0}$, which define the quadratic matrix inequality Define $\mathbf{P} = \begin{bmatrix} \mathbf{S}^{\mathsf{T}} & \mathbf{R} \end{bmatrix}$, $\mathcal{U} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, and $\mathcal{V} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, where ${\mathcal{U} + \mathcal{V}} = {\mathbb{R}}^{n + m}$. Notice that (2.64) is equivalent to ${\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}} < \mathbf{0}$ for all $\mathbf{x} \in {\mathcal{U} \smallsetminus {\{\mathbf{0}\}}}$. Additionally, ${\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}} \geq \mathbf{0}$ for all $\mathbf{x} \in \mathcal{V}$ is equivalent to which is satisfied based on the definition of $\mathbf{R}$. By the dualization lemma, (2.64) is satisfied with $\mathbf{R} \geq \mathbf{0}$ if and only if where $\begin{bmatrix} \overset{\sim}{\mathbf{Q}} & \overset{\sim}{\mathbf{S}} \\{\overset{\sim}{\mathbf{S}}}^{\mathsf{T}} & \overset{\sim}{\mathbf{R}} \end{bmatrix} = \begin{bmatrix} \mathbf{S}^{\mathsf{T}} & \mathbf{R} \end{bmatrix}^{- 1}$, $\mathcal{U}^{\perp} = {\mathcal{N}\left(\begin{bmatrix} \mathbf{1} & \mathbf{M}^{\mathsf{T}} \end{bmatrix} \right)} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, and $\mathcal{V}^{\perp} = {\mathcal{N}\left(\begin{bmatrix} \end{bmatrix} \right)} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$

### Singular Values

### Maximum Singular Value \[1, p. 8\],

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\gamma \in {\mathbb{R}}_{> 0}$. The maximum singular value of $\mathbf{A}$ is strictly less than $\gamma$ (i.e., ${\overline{\sigma}{(\mathbf{A})}} < \gamma$) if and only if ${\mathbf{A}\mathbf{A}}^{\mathsf{T}} < {\gamma^{\mathbf{2}}\mathbf{1}}$. Using the Schur complement, ${\mathbf{A}\mathbf{A}}^{\mathsf{T}} < {\gamma^{\mathbf{2}}\mathbf{1}}$ is equivalent to Equivalently, ${\overline{\sigma}{(\mathbf{A})}} < \gamma$ if and only if ${\mathbf{A}^{\mathsf{T}}\mathbf{A}} < {\gamma^{\mathbf{2}}\mathbf{1}}$ or

### Maximum Singular Value of a Complex Matrix

Consider $\mathbf{A} \in {\mathbb{C}}^{\mathbf{n} \times \mathbf{m}}$ and $\gamma \in {\mathbb{R}}_{> 0}$. The maximum singular value of $\mathbf{A}$ is strictly less than $\gamma$ (i.e., ${\overline{\sigma}{(\mathbf{A})}} < \gamma$) if and only if ${\mathbf{A}\mathbf{A}}^{\mathsf{H}} < {\gamma^{\mathbf{2}}\mathbf{1}}$. Using the Schur complement, ${\mathbf{A}\mathbf{A}}^{\mathsf{H}} < {\gamma^{\mathbf{2}}\mathbf{1}}$ is equivalent to Equivalently, ${\overline{\sigma}{(\mathbf{A})}} < \gamma$ if and only if ${\mathbf{A}^{\mathsf{H}}\mathbf{A}} < {\gamma^{\mathbf{2}}\mathbf{1}}$ or

### Minimum Singular Value

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$. If $n \leq m$, the minimum singular value of $\mathbf{A}$ is strictly greater than $\nu$ (i.e., ${\underset{¯}{\sigma}{(\mathbf{A})}} > \nu$) if and only if ${\mathbf{A}\mathbf{A}}^{\mathsf{T}} > {\nu^{\mathbf{2}}\mathbf{1}}$. If $m \leq n$, ${\underset{¯}{\sigma}{(\mathbf{A})}} > \nu$ if and only if ${\mathbf{A}^{\mathsf{T}}\mathbf{A}} > {\nu^{\mathbf{2}}\mathbf{1}}$.

### Minimum Singular Value of a Complex Matrix

Consider $\mathbf{A} \in {\mathbb{C}}^{\mathbf{n} \times \mathbf{m}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$. If $n \leq m$, the minimum singular value of $\mathbf{A}$ is strictly greater than $\nu$ (i.e., ${\underset{¯}{\sigma}{(\mathbf{A})}} > \nu$) if and only if ${\mathbf{A}\mathbf{A}}^{\mathsf{H}} > {\nu^{\mathbf{2}}\mathbf{1}}$. If $m \leq n$, ${\underset{¯}{\sigma}{(\mathbf{A})}} > \nu$ if and only if ${\mathbf{A}^{\mathsf{H}}\mathbf{A}} > {\nu^{\mathbf{2}}\mathbf{1}}$.

### Frobenius Norm

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\gamma \in {\mathbb{R}}_{> 0}$. The Frobenius norm of $\mathbf{A}$ is $\left\| \mathbf{A} \right\|_{\text{F}} = \sqrt{{tr}\left( {\mathbf{A}^{\mathsf{T}}\mathbf{A}} \right)} = \sqrt{{tr}\left( {\mathbf{A}\mathbf{A}}^{\mathsf{T}} \right)}$ \[6, pp. 341--342\]. The Frobenius norm is less than or equal to $\gamma$ if and only if any of the following equivalent conditions are satisfied.

There exists $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}}$ such that There exists $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$ such that

### Nuclear Norm

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\mu \in {\mathbb{R}}_{> 0}$. The nuclear norm of $\mathbf{A}$ is given by $\left\| \mathbf{A} \right\|_{\ast} = {\sum_{i = 1}^{p}{\sigma_{i}(\mathbf{A})}}$, where $p = {\min{(n,m)}}$ and $\sigma_{i}{(\mathbf{A})}$, $i = {1,\ldots,p}$ are the singular values of $\mathbf{A}$ \[6, p. 466\]. The nuclear norm of $\mathbf{A}$ is less than or equal to $\mu$ (i.e., $\left\| \mathbf{A} \right\|_{\ast} \leq \mu$) if and only if there exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{m}}$ such that

### Eigenvalues of Symmetric Matrices

### Maximum Eigenvalue \[1, p. 10\]

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}$. The maximum eigenvalue of $\mathbf{A}$ is strictly less than $\gamma$ (i.e., ${\overline{\lambda}{(\mathbf{A})}} < \gamma$) if and only if $\mathbf{A} < {\gamma\mathbf{1}}$.

### Minimum Eigenvalue

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}$. The minimum eigenvalue of $\mathbf{A}$ is strictly greater than $\gamma$ (i.e., ${\underset{¯}{\lambda}{(\mathbf{A})}} > \gamma$) if and only if $\mathbf{A} > {\gamma\mathbf{1}}$.

### Sum of Largest Eigenvalues

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n} \times \mathbf{n}}$, $\gamma \in {\mathbb{R}}$, and $k \in {\mathbb{Z}}_{> 0}$. The sum of the $k$ largest eigenvalues of $\mathbf{A}$, where $k \leq n$, is less than $\gamma$ (i.e., ${\sum_{i = 1}^{k}{\lambda_{i}{(\mathbf{A})}}} \leq \gamma$) if and only if there exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $z \in {\mathbb{R}}$, where $\mathbf{X} \geq \mathbf{0}$, such that

### Sum of Absolute Value Largest Eigenvalues

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n} \times \mathbf{n}}$, $\gamma \in {\mathbb{R}}$, and $k \in {\mathbb{Z}}_{> 0}$. The sum of the absolute value of the $k$ largest eigenvalues of $\mathbf{A}$, where $k \leq n$, is less than $\gamma$ (i.e., ${\sum_{i = 1}^{k}\left| {\lambda_{i}{(\mathbf{A})}} \right|} \leq \gamma$) if and only if there exist $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}}$ and $z \in {\mathbb{R}}$, where $\mathbf{X} \geq \mathbf{0}$ and $\mathbf{Y} \geq \mathbf{0}$, such that

### Weighted Sum of Largest Eigenvalues

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n} \times \mathbf{n}}$, $\gamma \in {\mathbb{R}}$, $k \in {\mathbb{Z}}_{> 0}$, and $w_{i} \in {\mathbb{R}}_{> 0}$, $i = {1,\ldots,n}$, where $0 < w_{1} \leq w_{2} \leq \cdots \leq w_{n}$. The weighted sum of the $k$ largest eigenvalues of $\mathbf{A}$, where $k \leq n$, is less than $\gamma$ (i.e., ${\sum_{i = 1}^{k}{w_{i}\lambda_{i}{(\mathbf{A})}}} \leq \gamma$) if and only if there exist $\mathbf{X}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$ and $z_{i} \in {\mathbb{R}}$, $i = {1,\ldots,k}$, where $\mathbf{X}_{\mathbf{i}} \geq \mathbf{0}$, such that

### Weighted Sum of Absolute Value of Largest Eigenvalues

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n} \times \mathbf{n}}$, $\gamma \in {\mathbb{R}}$, $k \in {\mathbb{Z}}_{> 0}$, and $w_{i} \in {\mathbb{R}}_{> 0}$, $i = {1,\ldots,n}$, where $0 < w_{1} \leq w_{2} \leq \cdots \leq w_{n}$. The weighted sum of the absolute value of the $k$ largest eigenvalues of $\mathbf{A}$, where $k \leq n$, is less than $\gamma$ (i.e., ${\sum_{i = 1}^{k}{w_{i}\left| {\lambda_{i}{(\mathbf{A})}} \right|}} \leq \gamma$) if and only if there exist $\mathbf{X}_{\mathbf{i}}$, $\mathbf{Y}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$ and $z_{i} \in {\mathbb{R}}$, $i = {1,\ldots,k}$, where $\mathbf{X}_{\mathbf{i}} \geq \mathbf{0}$ and $\mathbf{Y}_{\mathbf{i}} \geq \mathbf{0}$, such that

### Matrix Condition Number

### Condition Number of a Matrix \[1, pp. 37--38\]

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\gamma$, $\mu \in {\mathbb{R}}_{> 0}$, where the condition number of $\mathbf{A}$ is $\kappa{(\mathbf{A})}$. If $m \leq n$, the inequality ${\kappa{(\mathbf{A})}} \leq \gamma$ holds if there exists $\mu$ such that If $n \leq m$, the inequality ${\kappa{(\mathbf{A})}} \leq \gamma$ holds if there exists $\mu$ such that

### Condition Number of a Positive Definite Matrix \[1, p. 38\]

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma$, $\mu \in {\mathbb{R}}_{> 0}$, where the condition number of $\mathbf{A}$ is $\kappa{(\mathbf{A})}$. The inequality ${\kappa{(\mathbf{A})}} \leq \gamma$ holds if there exists $\mu$ such that

### Spectral Radius \[8, p. 17\]

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\delta \in {\mathbb{R}}_{> 0}$. The spectral radius of $\mathbf{A}$ is strictly less than $\delta$ (i.e., ${\rho{(\mathbf{A})}} < \delta$) under either of the following necessary and sufficient conditions.

There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that Also see Section 3.25 for a similar condition related to the structured singular value.

### Trace of a Symmetric Matrix

### Trace of a Matrix with a Slack Variable

\[5, pp. 46--47\] Consider $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$. The inequality given by is satisfied if and only if there exists $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}}$ such that \[1, p. 8\] Consider $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$. The matrix inequality given by is satisfied if and only if there exists $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$ such that

### Relative Trace of Two Matrices \[5, pp. 46--47\]

Consider $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$. The property ${{tr}{(\mathbf{P})}} < {{tr}{(\mathbf{Q})}}$ holds if the matrix inequality $\mathbf{P} < \mathbf{Q}$ is satisfied.

### Range of a Symmetric Matrix \[7, p. 714\]

Consider $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$. If $\mathbf{P} \leq \mathbf{Q}$, then ${\mathcal{R}{(\mathbf{P})}} \subseteq {\mathcal{R}{(\mathbf{Q})}}$.

### Logarithm of a Positive Definite Matrix \[7, p. 715\]

Consider $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\alpha \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} \geq \mathbf{0}$. The matrix logarithm of $\mathbf{P}$ satisfies the following matrix inequality

### Douglas-Fillmore-Williams Lemma \[7, p. 714\]

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and $\mathbf{Q} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$. The following statements are equivalent.

There exists $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$ such that $\mathbf{A} = {\mathbf{B}\mathbf{C}}$.

There exists $\alpha \in {\mathbb{R}}_{> 0}$ such that ${{\mathbf{A}\mathbf{A}}^{\mathsf{T}} - {\alpha{\mathbf{B}\mathbf{B}}^{\mathsf{T}}}} \leq \mathbf{0}$. ${\mathcal{R}{(\mathbf{A})}} \subseteq {\mathcal{R}{(\mathbf{B})}}$.

### Submatrix Determinants

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$. Let $\mathbf{A}_{\mathbf{k}} \in {\mathbb{S}}^{\mathbf{k}}$ be a submatrix of $\mathbf{A}$ consisting of its first $k$ rows and columns, where $k \leq n$. The matrix inequality $\mathbf{A} > \mathbf{0}$ is satisfied if and only if

### Imaginary and Real Parts \[4, Sec. 12.1.1\]

Consider $\mathbf{Q}_{\mathbf{R}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Q}_{\mathbf{I}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathbf{Q} = \mathbf{Q}^{\mathsf{H}} = {\mathbf{Q}_{\mathbf{R}} + {\mathbf{j}\mathbf{Q}}_{\mathbf{I}}} \in {\mathbb{C}}^{\mathbf{n} \times \mathbf{n}}$. The matrix inequality $\mathbf{Q} > \mathbf{0}$ is equivalent to the matrix inequality given by

### Quadratic Inequalities

### Weighted Norm

Consider $\mathbf{W} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{x}$, $\mathbf{y} \in {\mathbb{R}}^{\mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{W} > \mathbf{0}$. The inequality ${{({\mathbf{x} - \mathbf{y}})}^{\mathsf{T}}\mathbf{W}{({\mathbf{x} - \mathbf{y}})}} \leq \gamma$ is equivalent to the matrix inequality given by

### Quadratic Inequalities

Consider $\mathbf{W} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{x}$, $\mathbf{c} \in {\mathbb{R}}^{\mathbf{m}}$, $\mathbf{b} \in {\mathbb{R}}^{\mathbf{n}}$, and $d \in {\mathbb{R}}$, where $\mathbf{W} > \mathbf{0}$. The quadratic inequality ${{{({{\mathbf{A}\mathbf{x}} + \mathbf{b}})}^{\mathsf{T}}\mathbf{W}{({{\mathbf{A}\mathbf{x}} + \mathbf{b}})}} - {\mathbf{c}^{\mathsf{T}}\mathbf{x}} - \mathbf{d}} \leq \mathbf{0}$ with $\mathbf{W} > \mathbf{0}$ is equivalent to the matrix inequality given by \[7, p. 731\] Consider $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$. The matrix inequality given by

### Miscellaneous Properties and Results

Consider $\mathbf{P}$, $\mathbf{Q}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$, where $\mathbf{P} \geq \mathbf{0}$, $\mathbf{Q} \geq \mathbf{0}$, and $\mathbf{Z} > \mathbf{0}$. If the inequality holds for all $\mathbf{x} \neq \mathbf{0}$, then there exists $\lambda \in {\mathbb{R}}_{> 0}$ such that Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{W}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{W} > \mathbf{0}$. If there exists $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$, such that then for any $0 < \mathbf{W}_{\mathbf{1}} \leq \mathbf{W}$ and $\mathbf{Q}_{\mathbf{1}} \geq \mathbf{Q}$ there exists $\mathbf{S}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S}_{\mathbf{1}} \geq \mathbf{S}$ such that Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}}$ and $r \in {\mathbb{Z}}_{> 0}$. There exist $\mathbf{X}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{r}}$ and $\mathbf{X}_{\mathbf{3}}$, $\mathbf{Y}_{\mathbf{3}} \in {\mathbb{S}}^{\mathbf{r}}$, where $\mathbf{X}_{\mathbf{3}} > \mathbf{0}$ such that if and only if ${\mathbf{X} - \mathbf{Y}^{- \mathbf{1}}} \geq \mathbf{0}$ and ${\text{rank}\left({\mathbf{X} - \mathbf{Y}^{- \mathbf{1}}} \right)} \leq r$.

\[103, p. 19\] Consider $\mathbf{M}_{\mathbf{1}\mathbf{1}}$, $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{M}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{M}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{E}$, $\mathbf{F}_{\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathbf{F}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, where $\mathbf{M}_{\mathbf{1}\mathbf{1}} \geq \mathbf{0}$ and $\mathbf{E}$ is invertible. The matrix inequality holds if and only if there exist $\mathbf{F}_{\mathbf{1}}$ and $\mathbf{F}_{\mathbf{2}}$ such that Moreover, the following statements hold.

If (2.65) holds, then (2.66) holds with $\mathbf{F}_{\mathbf{1}} = {- {\left( {\mathbf{M}_{\mathbf{1}\mathbf{1}} + {\epsilon\mathbf{W}}} \right)\mathbf{E}^{- \mathbf{1}}}}$ and $\mathbf{F}_{\mathbf{2}} = {- {\mathbf{M}_{\mathbf{1}\mathbf{2}}^{\mathsf{T}}\mathbf{E}^{- \mathbf{1}}}}$, where $\epsilon \in {\mathbb{R}}_{> 0}$ is sufficiently small, $\mathbf{W} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{W} > \mathbf{0}$.

If (2.65) holds and $\mathbf{M}_{\mathbf{1}\mathbf{1}} > \mathbf{0}$, then (2.66) holds with $\mathbf{F}_{\mathbf{1}} = {\mathbf{M}_{\mathbf{1}\mathbf{1}}\mathbf{E}^{- \mathbf{1}}}$ and $\mathbf{F}_{\mathbf{2}} = {- {\mathbf{M}_{\mathbf{1}\mathbf{2}}^{\mathsf{T}}\mathbf{E}^{- \mathbf{1}}}}$.

## LMIs in Systems and Stability Theory

### Lyapunov Inequalities

### Lyapunov Stability \[7, pp. 1201--1203\], \[1, pp. 20--21\]

Consider the matrices $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} \geq \mathbf{0}$. There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, satisfying the Lyapunov equation if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If (3.1) holds, then ${\text{Re}{\{{\lambda_{i}{(\mathbf{A})}}\}}} \leq \mathbf{0}$, $i = {1,\ldots,n}$, and the equilibrium point $\overline{\mathbf{x}} = \mathbf{0}$ of the system $\overset{˙}{\mathbf{x}} = {\mathbf{A}\mathbf{x}}$ is Lyapunov stable.

The matrix inequality of (3.1) is satisfied under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that

### Proof

Identical to the proof of (3.5), except with the use of the Nonstrict Projection Lemma, where $\mathbf{G}^{\mathsf{T}} = \begin{bmatrix} {- \mathbf{1}} & \mathbf{A} & \mathbf{1} \end{bmatrix}$ and $\mathbf{H}^{\mathsf{T}} = \begin{bmatrix} \mathbf{1} & \mathbf{0} & \mathbf{0} \end{bmatrix}$, and therefore $\mathcal{R}{(\mathbf{G})}$ and $\mathcal{R}{(\mathbf{H})}$ are linearly independent. ∎ There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that

### Proof

Identical to the proof of (3.6), except with the use of the Nonstrict Projection Lemma, where $\mathbf{G}^{\mathsf{T}} = \begin{bmatrix} {- \mathbf{1}} & \mathbf{A}^{\mathsf{T}} & \mathbf{1} \end{bmatrix}$ and $\mathbf{H}^{\mathsf{T}} = \begin{bmatrix} \mathbf{1} & \mathbf{0} & \mathbf{0} \end{bmatrix}$, and therefore $\mathcal{R}{(\mathbf{G})}$ and $\mathcal{R}{(\mathbf{H})}$ are linearly independent. ∎ There does not exist $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Z} > \mathbf{0}$, such that

### Asymptotic Stability \[7, p. 1201--1203\], \[1, p. 2\]

Consider the matrices $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$. There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, satisfying the Lyapunov equation if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If (3.2) holds, then ${\text{Re}{\{{\lambda_{i}{(\mathbf{A})}}\}}} < \mathbf{0}$, $i = {1,\ldots,n}$, the matrix $\mathbf{A}$ is Hurwitz, and the equilibrium point $\overline{\mathbf{x}} = \mathbf{0}$ of the system $\overset{˙}{\mathbf{x}} = {\mathbf{A}\mathbf{x}}$ is asymptotically stable.

The matrix inequality of (3.2) is satisfied and the matrix $\mathbf{A}$ is Hurwitz under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that (The $S$-Variable Approach \[103, pp. 2--3\],) There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{Y} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

The proof follows the same steps as the proof of (3.7), beginning with (3.4) instead of (3.3). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There do not exist $\mathbf{Z}_{\mathbf{1}}$, $\mathbf{Z}_{\mathbf{2}} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Z}_{\mathbf{1}} \geq \mathbf{0}$, $\mathbf{Z}_{\mathbf{2}} \geq \mathbf{0}$, $\mathbf{Z}_{\mathbf{1}} \neq \mathbf{0}$, and $\mathbf{Z}_{\mathbf{2}} \neq \mathbf{0}$, such that

### Discrete-Time Lyapunov Stability \[7, pp. 1203--1204\]

Consider the matrices $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} \geq \mathbf{0}$. There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, satisfying the discrete-time Lyapunov equation if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If (3.8) holds, then $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| \leq 1$, $i = {1,\ldots,n}$, and the equilibrium point $\overline{\mathbf{x}} = \mathbf{0}$ of the system $\mathbf{x}_{\mathbf{k} + \mathbf{1}} = {\mathbf{A}_{d}\mathbf{x}_{\mathbf{k}}}$ is Lyapunov stable.

The matrix inequality of (3.8) is satisfied and the eigenvalues of $\mathbf{A}_{d}$ satisfy $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| \leq 1$, $i = {1,\ldots,n}$ under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Discrete-Time Asymptotic Stability \[7, pp. 1203--1204\], \[5, pp. 97--98\]

Consider the matrices $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$. There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, satisfying the discrete-time Lyapunov equation if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If (3.9) holds, then $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| < 1$, $i = {1,\ldots,n}$, the matrix $\mathbf{A}_{d}$ is Schur, and the equilibrium point $\overline{\mathbf{x}} = \mathbf{0}$ of the system $\mathbf{x}_{\mathbf{k} + \mathbf{1}} = {\mathbf{A}_{d}\mathbf{x}_{\mathbf{k}}}$ is asymptotically stable.

The matrix inequality of (3.9) is satisfied and the eigenvalues of $\mathbf{A}_{d}$ satisfy $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| < 1$, $i = {1,\ldots,n}$ under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that \[5, p. 97\] There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that \[5, p. 97\] There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that (The $S$-Variable Approach \[103, p. 3\],) There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that \[109, pp. 46--47\], There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that \[109, pp. 46--47\], There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Descriptor System Admissibility

Consider the descriptor system given by ${\mathbf{E}\overset{˙}{\mathbf{x}}} = {\mathbf{A}\mathbf{x}}$, where $\mathbf{E}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The descriptor system is admissible under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, satisfying ${\mathbf{E}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}} \geq \mathbf{0}$ and There exists $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, satisfying ${\mathbf{E}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}^{\mathsf{T}}} \geq \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, and $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E})}}$, and $\mathbf{P} > \mathbf{0}$, satisfying There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{F}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{F}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}\mathbf{Z}} = \mathbf{0}$ and

### Discrete-Time Descriptor System Admissibility

Consider the discrete-time descriptor system given by ${\mathbf{E}_{d}\mathbf{x}_{\mathbf{k} + \mathbf{1}}} = {\mathbf{A}_{d}\mathbf{x}_{\mathbf{k}}}$, where $\mathbf{E}_{d}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The discrete-time descriptor system is admissible under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, satisfying ${\mathbf{E}_{d}^{\mathsf{T}}{\mathbf{P}\mathbf{E}}_{d}} \geq \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}_{d}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}_{d}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, and $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}_{d}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E}_{d})}}$, and $\mathbf{P} > \mathbf{0}$, satisfying There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}_{d}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\alpha \in {\mathbb{R}}$, satisfying ${\mathbf{E}_{d}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}_{d}} \geq \mathbf{0}$ and where $\mathbf{E}_{d}^{\dagger}$ is the pseudoinverse of $\mathbf{E}_{d}$.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, $\mathbf{F}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}_{d}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, $\mathbf{F}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}_{d}\mathbf{Z}} = \mathbf{0}$ and

### Bounded Real Lemma and the $\mathcal{H}_{\infty}$ Norm

### Continuous-Time Bounded Real Lemma, \[121, pp. 85--86\]

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is The inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $r$, $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that \[123, pp. 46--47\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that \[123, pp. 46--47\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that \[123, pp. 46--47\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{V}_{\mathbf{1}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{V}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{V}_{\mathbf{2}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, $\mathbf{V}_{\mathbf{2}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that

### Proof

Identical to the proof of (3.12) in \[5, p. 156\], except with $\mathbf{\Omega} = \begin{bmatrix} \mathbf{V}_{\mathbf{1}\mathbf{1}} & \mathbf{V}_{\mathbf{1}\mathbf{2}} \\\mathbf{V}_{\mathbf{2}\mathbf{1}} & \mathbf{V}_{\mathbf{2}\mathbf{2}} There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{W}_{\mathbf{1}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{W}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{V}_{\mathbf{2}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{V}_{\mathbf{2}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{p}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Identical to the proof of (3.13), except with $\mathbf{\Omega} = \begin{bmatrix} \mathbf{W}_{\mathbf{1}\mathbf{1}} & \mathbf{W}_{\mathbf{1}\mathbf{2}} \\\mathbf{W}_{\mathbf{2}\mathbf{1}} & \mathbf{W}_{\mathbf{2}\mathbf{2}} The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is the minimum value of $\gamma \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions. If $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$ is a minimal realization, then the matrix inequalities can be nonstrict \[1, pp. 26--27\], \[124, pp. 308--311\],.

The inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ also holds under any of the following equivalent sufficient conditions.

\[5, p. 156\] There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{W} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Identical to the proof of (3.12) in \[5, p. 156\], except starting with the Bounded Real Lemma in the form which requires $\mathbf{\Phi} = \begin{bmatrix} {- \mathbf{1}} & \mathbf{A} & \mathbf{B} & \mathbf{1} & \mathbf{0} \\\mathbf{0} & \mathbf{C} & \mathbf{D} & \mathbf{0} & {- {\gamma\mathbf{1}}} When $\mathbf{D} = \mathbf{0}$, then the inequality $\left\| {\mathcal{G}} \right\|_{\infty} > \gamma$ holds if and only if there exist $\mathbf{Z}_{\mathbf{1}\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{Z}_{\mathbf{2}\mathbf{2}} \in {\mathbb{S}}^{\mathbf{m}}$ such that | | ${{{\mathbf{Z}_{\mathbf{1}\mathbf{1}}\mathbf{A}^{\mathsf{T}}} + {\mathbf{A}\mathbf{Z}}_{\mathbf{1}\mathbf{1}} + {\mathbf{Z}_{\mathbf{1}\mathbf{2}}\mathbf{B}^{\mathsf{T}}} + {\mathbf{B}\mathbf{Z}}_{\mathbf{1}\mathbf{2}}^{\mathsf{T}}} = \mathbf{0}},$ | | | | $\begin{bmatrix} | ${\geq 0},$ | | | | \mathbf{Z}_{\mathbf{1}\mathbf{1}} & \mathbf{Z}_{\mathbf{1}\mathbf{2}} \\ | | | | | \ast & \mathbf{Z}_{\mathbf{2}\mathbf{2}} | | | | | ${tr}\left(\mathbf{Z}_{\mathbf{2}\mathbf{2}} \right)$ | ${= 1},$ | | | | ${tr}\left({{\mathbf{C}\mathbf{Z}}_{\mathbf{1}\mathbf{1}}\mathbf{C}^{\mathsf{T}}} \right)$ | ${> \gamma}.$ | |

### Discrete-Time Bounded Real Lemma

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is The inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{X}$ has full rank, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{X}$ has full rank, such that

### Proof

Apply the congruence transformation $\mathbf{W} = {{diag}{\{\mathbf{X}^{\mathsf{T}},\mathbf{1},\mathbf{1},\mathbf{1}\}}}$ to (3.14), where $\mathbf{W}$ has full rank since $\mathbf{X}$ has full rank. ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that

### Proof

Same as the proof of (3.16), by which it is shown that (3.17) is equivalent to (3.15). ∎ \[131, pp. 48--49\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that \[131, pp. 48--49\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that \[131, pp. 48--49\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is the minimum value of $\gamma \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions. If $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$ is a minimal realization, then the matrix inequalities can be nonstrict,.

### Descriptor System Bounded Real Lemma

Consider a descriptor system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, described by where $\mathbf{E}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and it is assumed that the system is regular. The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, such that ${\mathbf{E}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}} \geq \mathbf{0}$ and There exist $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, such that ${\mathbf{Y}\mathbf{E}}^{\mathsf{T}} = {\mathbf{E}\mathbf{Y}}^{\mathsf{T}} \geq \mathbf{0}$ and There exist $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, such that ${\mathbf{E}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}} \geq \mathbf{0}$ and There exist $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, such that ${\mathbf{Y}\mathbf{E}}^{\mathsf{T}} = {\mathbf{E}\mathbf{Y}}^{\mathsf{T}} \geq \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E})}}$, and $\mathbf{P} > \mathbf{0}$, satisfying There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{m}})} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, $\mathbf{F}$, $\mathbf{G} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{m}})} \times {({\mathbf{n} + \mathbf{m}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${{\overline{\mathbf{E}}}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{p}})} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, $\mathbf{F}$, $\mathbf{G} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{p}})} \times {({\mathbf{n} + \mathbf{p}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\overline{\mathbf{E}}\mathbf{Z}} = \mathbf{0}$ and

### Discrete-Time Descriptor System Bounded Real Lemma

Consider a discrete-time descriptor system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, described by where $\mathbf{E}_{d}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that ${\mathbf{E}_{d}^{\mathsf{T}}{\mathbf{P}\mathbf{E}}_{d}} \geq \mathbf{0}$ and There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that ${\mathbf{E}_{d}{\mathbf{Q}\mathbf{E}}_{d}^{\mathsf{T}}} \geq \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}_{d}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, $\mathbf{Z} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{p}})} \times {({{\mathbf{n} + \mathbf{p}} - \mathbf{m} - \mathbf{n}_{\mathbf{e}}})}}$, $\mathbf{F} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{p}})} \times {({\mathbf{n} + \mathbf{p}})}}$, $\mathbf{G} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{m}})} \times {({\mathbf{n} + \mathbf{p}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $m \leq p$, $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, such that ${{\overline{\mathbf{E}}}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{S}}^{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}$, $\mathbf{Z} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{m}})} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, $\mathbf{F} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{m}})} \times {({\mathbf{n} + \mathbf{m}})}}$, $\mathbf{G} \in {\mathbb{R}}^{{({\mathbf{n} + \mathbf{p}})} \times {({\mathbf{n} + \mathbf{m}})}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $m \leq p$, $n_{e} = {\text{rank}{(\mathbf{E}_{d})}}$ and $\mathbf{P} > \mathbf{0}$, such that ${\overline{\mathbf{E}}\mathbf{Z}} = \mathbf{0}$ and

### $\mathcal{H}_{2}$ Norm

### Continuous-Time $\mathcal{H}_{2}$ Norm

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{0})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{A}$ is Hurwitz. The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is where $\mathbf{W}$, $\mathbf{M} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{W} > \mathbf{0}$, $\mathbf{M} > \mathbf{0}$, and The inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of the following equivalent necessary and sufficient conditions.

\[3, pp. 71--72\] There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$, such that \[3, pp. 71--72\] There exist $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Y} > \mathbf{0}$, such that \[3, pp. 71--72\], There exist $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Y} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[3, pp. 71--72\] There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{\Gamma} \in {\mathbb{R}}^{n \times n}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is the minimum value of $\mu \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions.

### Discrete-Time $\mathcal{H}_{2}$ Norm Without Feedthrough

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{0})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{A}_{d}$ is Schur. The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is where $\mathbf{W}$, $\mathbf{M} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{W} > \mathbf{0}$, $\mathbf{M} > \mathbf{0}$, and The inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of following equivalent necessary and sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that

### Proof

Apply the congruence transformation $\mathbf{W}_{\mathbf{1}} = {{diag}{\{\mathbf{Q},\mathbf{Q},\mathbf{1}\}}}$ to (3.20) and $\mathbf{W}_{\mathbf{2}} = {{diag}{\{\mathbf{1},\mathbf{Q}\}}}$ to (3.21), where $\mathbf{Q} = \mathbf{P}^{- \mathbf{1}}$. ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, and $\mathbf{X}$ has full rank, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, and $\mathbf{X}$ has full rank, such that

### Proof

Apply the congruence transformation $\mathbf{W}_{\mathbf{1}} = {\text{diag}{\{\mathbf{1},{\mathbf{X}^{\mathsf{T}}\mathbf{Q}^{- \mathbf{1}}},\mathbf{1}\}}}$ to (3.22) and the congruence transformation $\mathbf{W}_{\mathbf{2}} = {\text{diag}{\{\mathbf{1},{\mathbf{X}^{\mathsf{T}}\mathbf{Q}^{- \mathbf{1}}}\}}}$ to (3.23), where $\mathbf{W}_{\mathbf{1}}$ and $\mathbf{W}_{\mathbf{2}}$ have full rank since $\mathbf{X}$ has full rank.

There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, and $\mathbf{X}$ has full rank, such that

### Proof

Apply the congruence transformation $\mathbf{W} = {{diag}{\{{\mathbf{X}^{\mathsf{T}}\mathbf{Q}^{- \mathbf{1}}},\mathbf{1},\mathbf{1}\}}}$ to (3.24), where $\mathbf{W}$ has full rank since $\mathbf{X}$ has full rank. ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, and $\mathbf{X}$ has full rank, such that

### Proof

Apply the congruence transformation $\mathbf{W} = {{diag}{\{{\mathbf{X}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}},\mathbf{1},\mathbf{1}\}}}$ to (3.25), where $\mathbf{W}$ has full rank since $\mathbf{X}$ has full rank. ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, and $\mathbf{X}$ has full rank, such that

### Proof

Same as the proof of (3.28), (3.29), (3.30) .

There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that

### Proof

Same as the proof of (3.28), (3.29), (3.30), by which it is shown that (3.31) is equivalent to (3.26). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, and $\mathbf{X}$ has full rank, such that

### Proof

Same as the proof of (3.28), (3.29), (3.30), by which it is shown that (3.32) is equivalent to (3.27). ∎ \[131, pp. 53--54\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{F}_{\mathbf{5}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{F}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[131, pp. 53--54\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{F}_{\mathbf{5}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{5}}$, $\mathbf{X}_{\mathbf{6}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{F}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{X}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[131, pp. 53--54\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{Y}_{\mathbf{5}}$, $\mathbf{Y}_{\mathbf{6}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{5}}$, $\mathbf{X}_{\mathbf{6}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{Y}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{X}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is the minimum value of $\mu \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions.

### Discrete-Time $\mathcal{H}_{2}$ Norm With Feedthrough

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and $\mathbf{A}_{d}$ is Schur. The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is where $\mathbf{W}$, $\mathbf{M} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{W} > \mathbf{0}$, $\mathbf{M} > \mathbf{0}$, and The inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of following equivalent necessary and sufficient conditions.

There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that | | ${{{{\mathbf{A}_{d}^{\mathsf{T}}{\mathbf{Q}\mathbf{A}}_{d}} - \mathbf{Q}} + {\mathbf{C}_{d}^{\mathsf{T}}\mathbf{C}_{d}}} < \mathbf{0}},$ | | | | ${tr}\left({{\mathbf{B}_{d}^{\mathsf{T}}{\mathbf{Q}\mathbf{B}}_{d}} + {\mathbf{D}_{d}^{\mathsf{T}}\mathbf{D}_{d}}} \right)$ | ${< \mu^{2}}.$ | | There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that | | ${{{{\mathbf{A}_{d}{\mathbf{P}\mathbf{A}}_{d}^{\mathsf{T}}} - \mathbf{P}} + {\mathbf{B}_{d}\mathbf{B}_{d}^{\mathsf{T}}}} < \mathbf{0}},$ | | | | ${tr}\left({{\mathbf{C}_{d}{\mathbf{P}\mathbf{C}}_{d}^{\mathsf{T}}} + {\mathbf{D}_{d}\mathbf{D}_{d}^{\mathsf{T}}}} \right)$ | ${< \mu^{2}}.$ | | There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[137, p. 25\] There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that

### Proof

Applying the Schur complement to (3.33) and (3.34) yields (3.37) and (3.38). ∎ \[137, p. 26\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that

### Proof

Applying the Schur complement to (3.35) and (3.36) yields (3.40) and (3.41). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that

### Proof

Apply the congruence transformation $\mathbf{W}_{\mathbf{1}} = {{diag}{\{\mathbf{P},\mathbf{P},\mathbf{1}\}}}$ to (3.37) and $\mathbf{W}_{\mathbf{2}} = {{diag}{\{\mathbf{1},\mathbf{P},\mathbf{1}\}}}$ to (3.38), where $\mathbf{P} = \mathbf{Q}^{- \mathbf{1}}$. ∎ There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[137, pp. 26--27\] There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[131, pp. 53--54\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{F}_{\mathbf{5}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{F}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[131, pp. 53--54\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{F}_{\mathbf{1}}$, $\mathbf{F}_{\mathbf{2}}$, $\mathbf{F}_{\mathbf{5}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{5}}$, $\mathbf{X}_{\mathbf{6}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{F}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{X}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that \[131, pp. 53--54\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{Y}_{\mathbf{5}}$, $\mathbf{Y}_{\mathbf{6}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{5}}$, $\mathbf{X}_{\mathbf{6}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{Y}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, $\mathbf{X}_{\mathbf{4}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Z} > \mathbf{0}$, such that The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is the minimum value of $\mu \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions.

### Descriptor System $\mathcal{H}_{2}$ Norm

Consider a descriptor system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, described by where $\mathbf{E}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and it is assumed that the system is regular. The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is where $\hat{\mathbf{C}} \in {\mathbb{R}}^{p \times n}$, $\hat{\mathbf{B}} \in {\mathbb{R}}^{n \times m}$, $\mathbf{W}$, $\mathbf{M} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{C} = {\hat{\mathbf{C}}\mathbf{E}}$, $\mathbf{B} = {\mathbf{E}\hat{\mathbf{B}}}$, ${\mathbf{W}\mathbf{E}}^{\mathsf{T}} = {\mathbf{E}\mathbf{W}}^{\mathsf{T}} > \mathbf{0}$, ${\mathbf{E}^{\mathsf{T}}\mathbf{M}} = {\mathbf{M}^{\mathsf{T}}\mathbf{E}} > \mathbf{0}$, and The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of the following equivalent necessary and sufficient conditions.

The descriptor state-space matrices satisfy ${\mathcal{R}{(\mathbf{B})}} \subseteq {\mathcal{R}{(\mathbf{E})}}$ and there exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E})}}$, and $\mathbf{Q} > \mathbf{0}$, satisfying The descriptor state-space matrices satisfy ${\mathcal{N}{(\mathbf{E})}} \subseteq {\mathcal{N}{(\mathbf{C})}}$ and there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E})}}$, and $\mathbf{P} > \mathbf{0}$, satisfying The descriptor state-space matrices satisfy ${\mathcal{R}{(\mathbf{B})}} \subseteq {\mathcal{R}{(\mathbf{E})}}$ and there exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{Q} > \mathbf{0}$, satisfying ${\mathbf{E}^{\mathsf{T}}\mathbf{Z}} = \mathbf{0}$ and The descriptor state-space matrices satisfy ${\mathcal{N}{(\mathbf{E})}} \subseteq {\mathcal{N}{(\mathbf{C})}}$ and there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{X} \in {\mathbb{R}}^{{({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})} \times \mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$ and $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}\mathbf{Z}} = \mathbf{0}$ and

### Discrete-Time Descriptor System $\mathcal{H}_{2}$ Norm

Consider a discrete-time descriptor system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, described by where $\mathbf{E}_{d}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is \[143, pp. 87--88\], where $\mathbf{W}$, $\mathbf{M} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{W} > \mathbf{0}$, $\mathbf{M} > \mathbf{0}$, The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that ${\mathbf{E}_{d}^{\mathsf{T}}{\mathbf{Q}\mathbf{E}}_{d}} \geq \mathbf{0}$, Note that, (3.42) is missing the $- {\mathbf{E}_{d}^{\mathsf{T}}{\mathbf{P}\mathbf{E}}_{d}}$ term.

### Proof

The proof follows from the definition of the $\mathcal{H}_{2}$ norm using an approach similar to that in \[2, pp. 201-211, Proposition 6.13\], where ${{tr}\left({{\mathbf{B}_{d}^{\mathsf{T}}{\mathbf{Q}\mathbf{B}}_{d}} + {\mathbf{D}_{d}^{\mathsf{T}}\mathbf{D}_{d}}} \right)} < \mu^{2}$ is equivalent to ${{{\mathbf{B}_{d}^{\mathsf{T}}{\mathbf{Q}\mathbf{B}}_{d}} + {\mathbf{D}_{d}^{\mathsf{T}}\mathbf{D}_{d}}} - \mathbf{Z}} < \mathbf{0}$ and ${{tr}{(\mathbf{Z})}} < \mu^{\mathbf{2}}$. ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{p}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that ${\mathbf{E}_{d}{\mathbf{P}\mathbf{E}}_{d}^{\mathsf{T}}} \geq \mathbf{0}$,

### Proof

The proof follows from the definition of the $\mathcal{H}_{2}$ norm using an approach similar to that in \[2, pp. 201-211, Proposition 6.13\], where ${{tr}\left({{\mathbf{C}_{d}{\mathbf{P}\mathbf{C}}_{d}^{\mathsf{T}}} + {\mathbf{D}_{d}\mathbf{D}_{d}^{\mathsf{T}}}} \right)} < \mu^{2}$ is equivalent to ${{{\mathbf{C}_{d}{\mathbf{P}\mathbf{C}}_{d}^{\mathsf{T}}} + {\mathbf{D}_{d}\mathbf{D}_{d}^{\mathsf{T}}}} - \mathbf{Z}} < \mathbf{0}$ and ${{tr}{(\mathbf{Z})}} < \mu^{\mathbf{2}}$. ∎ There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that ${\mathbf{E}_{d}^{\mathsf{T}}{\mathbf{Q}\mathbf{E}}_{d}} \geq \mathbf{0}$,

### Proof

Applying the Schur complement to (3.42) and (3.43) yields (3.46) and (3.47). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{o}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that ${\mathbf{E}_{d}{\mathbf{P}\mathbf{E}}_{d}^{\mathsf{T}}} \geq \mathbf{0}$,

### Proof

Applying the Schur complement to (3.44) and (3.45) yields (3.48) and (3.49). ∎

### Generalized $\mathcal{H}_{2}$ Norm (Induced $\mathcal{L}_{2}$-$\mathcal{L}_{\infty}$ Norm)

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{0})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{A}$ is Hurwitz. The generalized $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is The inequality $\left\| {\mathcal{G}} \right\|_{2,\infty} < \mu$ holds under any of following equivalent necessary and sufficient conditions.

\[3, p. 73\], There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Identical to the proof in used to obtain the dilated matrix inequality in (3.18). ∎ The generalized $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is the minimum value of $\mu \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions.

### Peak-to-Peak Norm (Induced $\mathcal{L}_{\infty}$-$\mathcal{L}_{\infty}$ Norm) \[3, pp. 74--75\],

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and $\mathbf{A}$ is Hurwitz. The peak-to-peak norm of $\mathcal{G}$ is The inequality $\left\| {\mathcal{G}} \right\|_{\infty,\infty} < \mu$ holds under any of the following equivalent sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\lambda$, $\epsilon$, $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\lambda$, $\epsilon$, $\mu \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} > \mathbf{0}$, such that The peak-to-peak norm of $\mathcal{G}$ is smaller than any $\mu \in {\mathbb{R}}_{> 0}$ that satisfies either of the above conditions.

### Kalman-Yakubovich-Popov (KYP) Lemma

### KYP Lemma for QSR Dissipative Systems

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ is QSR dissipative if where $\mathbf{u}{(\mathbf{t})}$ is the input to $\mathcal{G}$, $\mathbf{y}{(\mathbf{t})}$ is the output of $\mathcal{G}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$. The system $\mathcal{G}$ is also QSR dissipative if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Note that the Bounded Real Lemma (Section 3.2.1) is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {- \mathbf{1}}$, $\mathbf{S} = \mathbf{0}$, and $\mathbf{R} = {\gamma^{\mathbf{2}}\mathbf{1}}$.

### Discrete-Time KYP Lemma for QSR Dissipative Systems, \[151, p. 495\]

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with minimal state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ is QSR dissipative if where $\mathbf{u}_{\mathbf{k}}$ is the input to $\mathcal{G}$, $\mathbf{y}_{\mathbf{k}}$ is the output of $\mathcal{G}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{p}}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$. The system $\mathcal{G}$ is also QSR dissipative if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Note that the Discrete-Time Bounded Real Lemma (Section 3.2.2) is a special case of the Discrete-Time KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {- \mathbf{1}}$, $\mathbf{S} = \mathbf{0}$, and $\mathbf{R} = {\gamma^{\mathbf{2}}\mathbf{1}}$.

### KYP (Positive Real) Lemma Without Feedthrough \[152, p. 219\] \[154, p. 14\]

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{0})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. The system $\mathcal{G}$ is positive real (PR) under either of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that This is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = \mathbf{0}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$.

The system $\mathcal{G}$ is strictly positive real (SPR) under either of the following necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that This is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {\epsilon \cdot \mathbf{1}}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$, where $\epsilon \in {\mathbb{R}}_{> 0}$.

### KYP (Positive Real) Lemma With Feedthrough \[1, p. 25\], \[152, p. 218\] \[155, pp. 79--80\]

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The system $\mathcal{G}$ is positive real (PR) under either of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that This is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = \mathbf{0}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$.

The system $\mathcal{G}$ is strictly positive real (SPR) under either of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that This is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {\epsilon\mathbf{1}}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$, where $\epsilon \in {\mathbb{R}}_{> 0}$.

### Discrete-Time KYP (Positive Real) Lemma With Feedthrough \[155, pp. 171--172\]

Consider a square, discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with minimal state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The system $\mathcal{G}$ is positive real (PR) under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that This is a special case of the Discrete-Time KYP Lemma for QSR dissipative systems with $\mathbf{Q} = \mathbf{0}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$.

The system $\mathcal{G}$ is strictly positive real (SPR) under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that This is a special case of the Discrete-Time KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {\epsilon\mathbf{1}}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$, where $\epsilon \in {\mathbb{R}}_{> 0}$.

### KYP Lemma for Descriptor Systems \[155, pp. 91--93\],

Consider a square, LTI descriptor system given by where $\mathbf{E}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The system is extended strictly positive real (ESPR) if and only if there exist $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ such that ${\mathbf{E}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}} \geq \mathbf{0}$, ${\mathbf{E}^{\mathsf{T}}\mathbf{W}} = \mathbf{0}$, and The system is also ESPR if there exists $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ such that ${\mathbf{E}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}} \geq \mathbf{0}$ and

### Discrete-Time KYP Lemma for Descriptor Systems

Consider a square, discrete-time LTI descriptor system given by where $\mathbf{E}_{d}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The system is extended strictly positive real (ESPR) if and only if there exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ such that ${\mathbf{E}^{\mathsf{T}}{\mathbf{X}\mathbf{E}}} \geq \mathbf{0}$ and

### QSR Dissipativity-Related Properties

Consider a QSR-dissipative continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The $\mathcal{H}_{\infty}$ norm of $\mathcal{G}$ is less than $\gamma$ (i.e., $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$) if there exist $\alpha$, $\gamma \in {\mathbb{R}}_{> 0}$ such that ${\mathbf{1} + {\alpha\mathbf{Q}}} < \mathbf{0}$ and

### Conic Sectors

### Conic Sector Lemma

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$.

The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$, where $a$, $b \in {\mathbb{R}}$, and $a < b$, under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Note that the matrix inequality of (3.50) does not allow for the case where the upper bound $b$ is infinite.

\[165, p. 28\] There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that The system $\mathcal{G}$ is inside the cone of radius $r$ centered at $c$, where $r \in {\mathbb{R}}_{> 0}$ and $b \in {\mathbb{R}}$, under any of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Note that the matrix inequality of (3.51) does not allow for the case where the upper bound $b$ is infinite.

The Conic Sector Lemma is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {- \mathbf{1}}$, $\mathbf{S} = {\frac{\mathbf{a} + \mathbf{b}}{\mathbf{2}}\mathbf{1}} = {\mathbf{c}\mathbf{1}}$, and $\mathbf{R} = {- {\mathbf{a}\mathbf{b}\mathbf{1}}} = {\left( {\mathbf{r}^{\mathbf{2}} - \mathbf{c}^{\mathbf{2}}} \right)\mathbf{1}}$.

### Exterior Conic Sector Lemma

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The system $\mathcal{G}$ is in the exterior cone of radius $r$ centered at $c$ (i.e., ${\mathcal{G}} \in {\text{excone}_{r}{(c)}}$), where $r \in {\mathbb{R}}_{> 0}$ and $c \in {\mathbb{R}}$, under either of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} \geq \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $r^{2}\mathbf{1}$ term in (3.52) gives (3.53). ∎

### Modified Exterior Conic Sector Lemma

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The system $\mathcal{G}$ is in the exterior cone of radius $r$ centered at $c$ (i.e., ${\mathcal{G}} \in {\text{excone}_{r}{(c)}}$), where $r \in {\mathbb{R}}_{> 0}$ and $c \in {\mathbb{R}}$, under either of the following equivalent sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

The term $- {\mathbf{C}^{\mathsf{T}}\mathbf{C}}$ in (3.52) makes the matrix inequality "more" negative definite. Therefore, There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $r^{2}\mathbf{1}$ term in (3.54) gives (3.55). ∎ A system satisfying the Modified Exterior Conic Sector Lemma is Lyapunov stable if the additional restriction $\mathbf{P} > \mathbf{0}$ is made, which is not necessarily true for a system satisfying the Exterior Conic Sector Lemma.

The system $\mathcal{G}$ is also in the exterior cone of radius $r$ centered at $c$, where $r \in {\mathbb{R}}_{> 0}$ and $c \in {\mathbb{R}}$, under either of the following equivalent sufficient conditions.

There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that

### Generalized KYP (GKYP) Lemma for Conic Sectors

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. Also consider ${\mathbf{\Pi}_{c}{(a,b)}} \in {\mathbb{S}}^{m}$, which is defined as where $a \in {\mathbb{R}}$, $b \in {\mathbb{R}}_{> 0}$, and $a < b$. The following generalized KYP Lemmas give conditions for $\mathcal{G}$ to be inside the cone $\lbrack a,b\rbrack$ within finite frequency bandwidths.

(Low Frequency Range) The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$ for all $\omega \in \left. \{{\omega \in {\mathbb{R}}} \middle| {{|\omega| < \omega_{1}},{{\det{({{j\omega\mathbf{1}} - \mathbf{A}})}} \neq \mathbf{0}}}\} \right.$, where $\omega_{1} \in {\mathbb{R}}_{> 0}$, $a \in {\mathbb{R}}$, $b \in {\mathbb{R}}_{> 0}$, and $a < b$, if there exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and ${\overline{\omega}}_{1} \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} \geq \mathbf{0}$, such that If $\omega_{1}\rightarrow\infty$, $\mathbf{P} > \mathbf{0}$, and $\mathbf{Q} = \mathbf{0}$, then the traditional Conic Sector Lemma is recovered.

The parameter ${\overline{\omega}}_{1}$ is included in (3.56 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) to effectively transform $|\omega| \leq {({\omega_{1} - {\overline{\omega}}_{1}})}$ into the strict inequality $|\omega| < \omega_{1}$.

(Intermediate Frequency Range) The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$ for all $\omega \in \left. \{{\omega \in {\mathbb{R}}} \middle| {{\omega_{1} \leq |\omega| < \omega_{2}},{{\det{({{j\omega\mathbf{1}} - \mathbf{A}})}} \neq \mathbf{0}}}\} \right.$, where $\omega_{1}$, $\omega_{2} \in {\mathbb{R}}_{> 0}$, $a \in {\mathbb{R}}$, $b \in {\mathbb{R}}_{> 0}$, and $a < b$, if there exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{C}}^{\mathbf{n}}$, ${\overline{\omega}}_{2} \in {\mathbb{R}}_{> 0}$, and ${\hat{\omega}}_{2} = {\left({\omega_{1} + {({\omega_{2} - {\overline{\omega}}_{2}})}} \right)/2}$, where $\mathbf{P}^{\mathsf{H}} = \mathbf{P}$, $\mathbf{Q}^{\mathsf{H}} = \mathbf{Q}$, and $\mathbf{Q} \geq \mathbf{0}$, such that The parameter ${\overline{\omega}}_{2}$ is included in (3.57 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) to effectively transform $\omega_{1} \leq |\omega| \leq {({\omega_{2} - {\overline{\omega}}_{2}})}$ into the strict inequality $\omega_{1} \leq |\omega| < \omega_{2}$.

(High Frequency Range) The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$ for all $\omega \in \left. \{{\omega \in {\mathbb{R}}} \middle| {{\omega_{2} \leq |\omega|},{{\det{({{j\omega\mathbf{1}} - \mathbf{A}})}} \neq \mathbf{0}}}\} \right.$, where $\omega_{2} \in {\mathbb{R}}_{> 0}$, $a \in {\mathbb{R}}$, $b \in {\mathbb{R}}_{> 0}$, and $a < b$, if there exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} \geq \mathbf{0}$, such that If $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$ is a minimal realization, then the matrix inequalities in (3.56 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), (3.57 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), and (3.58 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) can be nonstrict.

### Minimum Gain

### Minimum Gain Lemma

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ has minimum gain $\nu$ under any of the following equivalent sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that If $\mathcal{G}$ is a square system (i.e., $m = p$) or ${\text{span}{(\mathbf{C})}} \subseteq {\text{span}{(\mathbf{D})}}$, then the preceding conditions are necessary and sufficient for $\mathcal{G}$ to have minimum gain $\nu \in {\mathbb{R}}_{\geq 0}$. The minimum gain lemma is a special case of the exterior conic sector lemma with $a = {- \nu}$ and $b = \nu$.

The system $\mathcal{G}$ also has minimum gain $\nu$ under any of the following sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{V}_{\mathbf{1}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{V}_{\mathbf{1}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{V}_{\mathbf{2}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{V}_{\mathbf{2}\mathbf{2}} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

Applying the congruence transformation $\mathbf{W} = {\text{diag}{\{{\nu^{- {\mathbf{1}/\mathbf{2}}}\mathbf{1}},{\nu^{- {\mathbf{1}/\mathbf{2}}}\mathbf{1}}\}}}$ and defining $\overline{\mathbf{P}} = {\nu^{- 1}\mathbf{P}}$, the matrix inequality of can be rewritten as Using Property 3 from Section 2.3.3 and making the assumption that $\overline{\mathbf{P}}$ is invertible, (3.60) is equivalent to Since $\overline{\mathbf{P}} > 0$ and $\nu \in {\mathbb{R}}_{\geq 0}$, it is also known that which can be rewritten as The matrix inequalities in (3.61) and (3.62) are in the form of the nonstrict projection lemma. Specifically, (3.61) is in the form of ${\mathbf{N}_{\mathbf{G}}^{\mathsf{T}}\mathbf{\Phi}\mathbf{N}_{\mathbf{G}}} \leq \mathbf{0}$, where The matrix inequality of (3.62) is in the form of ${\mathbf{N}_{\mathbf{H}}^{\mathsf{T}}\mathbf{\Phi}\mathbf{N}_{\mathbf{H}}} < \mathbf{0}$, where The nonstrict projection lemma states that (3.61) and (3.62) are equivalent to where ${\mathcal{N}{(\mathbf{G}^{\mathsf{T}})}} = {\mathcal{R}{(\mathbf{N}_{\mathbf{G}})}}$, ${\mathcal{N}{(\mathbf{H}^{\mathsf{T}})}} = {\mathcal{R}{(\mathbf{N}_{\mathbf{H}})}}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathcal{R}{(\mathbf{G})}$, $\mathcal{R}{(\mathbf{H})}$ are linearly independent. Choosing where $\mathcal{R}{(\mathbf{G})}$ and $\mathcal{R}{(\mathbf{H})}$ are in fact linearly independent, the matrix inequality of (3.63) can be rewritten as Redefining $\mathbf{P} = \overline{\mathbf{P}}$, (3.64) is identical to (3.59). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{V}_{\mathbf{1}\mathbf{1}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

The matrix inequality of (3.65) is derived from (3.59) with $\mathbf{V}_{\mathbf{1}\mathbf{1}} = \mathbf{V}$, $\mathbf{V}_{\mathbf{1}\mathbf{2}} = \mathbf{0}$, $\mathbf{V}_{\mathbf{2}\mathbf{1}} = \mathbf{0}$, and $\mathbf{V}_{\mathbf{2}\mathbf{2}} = {- \mathbf{1}}$. The dilation in (3.59) relies on the projection lemma and becomes only a sufficient condition in this case due to the structure imposed on $\mathbf{V}_{\mathbf{1}\mathbf{1}}$, $\mathbf{V}_{\mathbf{1}\mathbf{2}}$, $\mathbf{V}_{\mathbf{2}\mathbf{1}}$, and $\mathbf{V}_{\mathbf{2}\mathbf{2}}$. ∎

### Modified Minimum Gain Lemma

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ has minimum gain $\nu$ under any of the following equivalent sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $\nu^{2}\mathbf{1}$ term in (3.66) gives (3.67). ∎ A system satisfying the Modified Minimum Gain Lemma is Lyapunov stable if the additional restriction $\mathbf{P} > \mathbf{0}$ is made, which is not necessarily true for a system satisfying the Minimum Gain Lemma.

The system $\mathcal{G}$ also has minimum gain $\nu$ under any of the following equivalent sufficient conditions.

There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{Q} > \mathbf{0}$, such that

### Discrete-Time Minimum Gain Lemma

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ has minimum gain $\nu$ under any of the following equivalent sufficient conditions.

\[175, p. 30\] There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $\nu^{2}\mathbf{1}$ term in (3.68) gives (3.69). ∎ The system $\mathcal{G}$ also has minimum gain $\nu$ under any of the following equivalent sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Under the assumption that $\mathbf{P} > \mathbf{0}$, the nonstrict Schur complement lemma is applied to (3.68) to yield (3.70). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $\nu^{2}\mathbf{1}$ term in (3.70) gives (3.71). ∎

### Discrete-Time Modified Minimum Gain Lemma

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ has minimum gain $\nu$ under any of the following equivalent sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} \geq \mathbf{0}$, such that

### Proof

The term $- {\mathbf{C}_{d}^{\mathsf{T}}\mathbf{C}_{d}}$ in (3.68) makes the matrix inequality "more" negative definite. Therefore, There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $\nu^{2}\mathbf{1}$ term in (3.72) gives (3.73). ∎ A system satisfying the Discrete-Time Modified Minimum Gain Lemma is Lyapunov stable if the additional restriction $\mathbf{P} > \mathbf{0}$ is made, which is not necessarily true for a system satisfying the Discrete-Time Minimum Gain Lemma.

The system $\mathcal{G}$ also has minimum gain $\nu$ under any of the following sufficient conditions.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Under the assumption that $\mathbf{P} > \mathbf{0}$, the nonstrict Schur complement lemma is applied to (3.72) to yield (3.74). ∎ There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Applying the Schur complement lemma to the $\nu^{2}\mathbf{1}$ term in (3.74) gives (3.75). ∎ There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and $\nu \in {\mathbb{R}}_{\geq 0}$, where $\mathbf{Q} > \mathbf{0}$, such that

### Negative Imaginary Systems

### Negative Imaginary Lemma

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{S}}^{\mathbf{m}}$. The system $\mathcal{G}$ is negative imaginary under either of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} \geq \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} \geq \mathbf{0}$, such that The system $\mathcal{G}$ is strictly negative imaginary if ${\det{(\mathbf{A})}} \neq \mathbf{0}$ and either (3.76) is satisfied with $\mathbf{P} > \mathbf{0}$ or (3.77) is satisfied with $\mathbf{Q} > \mathbf{0}$.

### Discrete-Time Negative Imaginary Lemma

Consider a square, discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, ${{\mathbf{C}_{d}\left( {{\mathbf{z}\mathbf{1}} - \mathbf{A}_{d}} \right)^{- \mathbf{1}}\mathbf{B}_{d}} + \mathbf{D}_{d}} = {{\mathbf{B}_{d}^{\mathsf{T}}\left( {{\mathbf{z}\mathbf{1}} - \mathbf{A}_{d}^{\mathsf{T}}} \right)^{- \mathbf{1}}\mathbf{C}_{d}^{\mathsf{T}}} + \mathbf{D}_{d}^{\mathsf{T}}}$, ${\text{det}\left( {\mathbf{1} + \mathbf{A}} \right)} \neq 0$, and ${\text{det}\left( {\mathbf{1} - \mathbf{A}} \right)} \neq 0$. The system $\mathcal{G}$ is negative imaginary under either of the following equivalent necessary and sufficient conditions.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that

### Generalized Negative Imaginary Lemma

Consider a square, continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{S}}^{\mathbf{m}}$. Also consider $\mathbf{\Pi}_{p} \in {\mathbb{S}}^{m}$, which is defined as The following generalized KYP Lemmas give conditions for $\mathcal{G}$ to be negative imaginary within finite frequency bandwidths.

(Low Frequency Range) The system $\mathcal{G}$ is negative imaginary for all $\omega \in \left. \{{\omega \in {\mathbb{R}}} \middle| {{|\omega| < \omega_{1}},{{\det{({{j\omega\mathbf{1}} - \mathbf{A}})}} \neq \mathbf{0}}}\} \right.$, where $\omega_{1} \in {\mathbb{R}}_{> 0}$, if $\mathbf{D} = \mathbf{D}^{\mathsf{T}}$ and there exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$ and ${\overline{\omega}}_{1} \in {\mathbb{R}}_{> 0}$, where $\mathbf{Q} \geq \mathbf{0}$, such that If $\omega_{1}\rightarrow\infty$, $\mathbf{P} > \mathbf{0}$, and $\mathbf{Q} = \mathbf{0}$, then the traditional Negative Imaginary Lemma is recovered.

The parameter ${\overline{\omega}}_{1}$ is included in (3.78) to effectively transform $|\omega| \leq {({\omega_{1} - {\overline{\omega}}_{1}})}$ into the strict inequality $|\omega| < \omega_{1}$.

(Intermediate Frequency Range) The system $\mathcal{G}$ is negative imaginary for all $\omega \in \left. \{{\omega \in {\mathbb{R}}} \middle| {{\omega_{1} \leq |\omega| < \omega_{2}},{{\det{({{j\omega\mathbf{1}} - \mathbf{A}})}} \neq \mathbf{0}}}\} \right.$, where $\omega_{1}$, $\omega_{2} \in {\mathbb{R}}_{> 0}$, if $\mathbf{D} = \mathbf{D}^{\mathsf{T}}$ and there exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{C}}^{\mathbf{n}}$, ${\overline{\omega}}_{2} \in {\mathbb{R}}_{> 0}$, and ${\hat{\omega}}_{2} = {\left({\omega_{1} + {({\omega_{2} - {\overline{\omega}}_{2}})}} \right)/2}$, where $\mathbf{P}^{\mathsf{H}} = \mathbf{P}$, $\mathbf{Q}^{\mathsf{H}} = \mathbf{Q}$, and $\mathbf{Q} \geq \mathbf{0}$, such that The parameter ${\overline{\omega}}_{2}$ is included in (3.79) to effectively transform $\omega_{1} \leq |\omega| \leq {({\omega_{2} - {\overline{\omega}}_{2}})}$ into the strict inequality $\omega_{1} \leq |\omega| < \omega_{2}$.

(High Frequency Range) The system $\mathcal{G}$ is negative imaginary for all $\omega \in \left. \{{\omega \in {\mathbb{R}}} \middle| {{\omega_{2} \leq |\omega|},{{\det{({{j\omega\mathbf{1}} - \mathbf{A}})}} \neq \mathbf{0}}}\} \right.$, where $\omega_{2} \in {\mathbb{R}}_{> 0}$, if $\mathbf{D} = \mathbf{D}^{\mathsf{T}}$ and there exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} \geq \mathbf{0}$, such that

### Negative Imaginary System DC Constraint, \[183, pp. 32--34\]

Consider an NI transfer matrix $\mathbf{G}_{\mathbf{1}}{(\mathbf{s})}$ and an SNI transfer matrix ${\mathbf{G}_{\mathbf{2}}{(\mathbf{s})}} = {{\mathbf{C}_{\mathbf{2}}\left({{\mathbf{s}\mathbf{1}} - \mathbf{A}_{\mathbf{2}}} \right)^{- \mathbf{1}}\mathbf{B}_{\mathbf{2}}} + \mathbf{D}_{\mathbf{2}}}$. The condition ${\overline{\lambda}{({\mathbf{G}_{\mathbf{1}}{(\mathbf{0})}\mathbf{G}_{\mathbf{2}}{(\mathbf{0})}})}} < \mathbf{1}$ is satisfied if and only if where ${\mathbf{S}\mathbf{S}}^{\mathsf{T}} = {\mathbf{G}_{\mathbf{1}}{(\mathbf{0})}}$.

### Algebraic Riccati Inequalities

### Algebraic Riccati Inequality

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{N} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{Q} \geq \mathbf{0}$, and $\mathbf{R} > \mathbf{0}$. The algebraic Riccati inequality given by can be rewritten using the Schur complement lemma as

### Discrete-Time Algebraic Riccati Inequality

Consider $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{Q} \geq \mathbf{0}$, and $\mathbf{R} > \mathbf{0}$. The discrete-time algebraic Riccati inequality given by can be rewritten using the Schur complement lemma as Equivalently, this discrete-time algebraic Riccati inequality is satisfied under any of the following necessary and sufficient conditions.

There exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{Q} \geq \mathbf{0}$, and $\mathbf{R} > \mathbf{0}$, such that There exist $\mathbf{X}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{X} > \mathbf{0}$, $\mathbf{Q} \geq \mathbf{0}$, and $\mathbf{R} > \mathbf{0}$, such that

### Stabilizability

### Continuous-Time Stabilizability \[5, pp. 166--168\]

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ is stabilizable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A} + {\mathbf{B}\mathbf{K}}$ is Hurwitz with $\mathbf{K} = {- {\frac{1}{2}\mathbf{B}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}}}$. Equivalently, $\mathcal{G}$ is stabilizable if and only if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A} + {\mathbf{B}\mathbf{K}}$ is Hurwitz with $\mathbf{K} = {\mathbf{W}\mathbf{P}}^{- \mathbf{1}}$.

### Discrete-Time Stabilizability \[5, pp. 172--176\]

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ is stabilizable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A}_{d} + {\mathbf{B}_{d}\mathbf{K}_{d}}$ is Schur with $\mathbf{K}_{d} = {- {\left({\mathbf{2}\mathbf{1} + {\mathbf{B}_{d}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{B}_{d}}} \right)^{- \mathbf{1}}\mathbf{B}_{d}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{A}_{d}}}$. Equivalently, $\mathcal{G}$ is stabilizable if and only if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A}_{d} + {\mathbf{B}_{d}\mathbf{K}_{d}}$ is Schur with $\mathbf{K}_{d} = {\mathbf{W}\mathbf{P}}^{- \mathbf{1}}$.

### Detectability

### Continuous-Time Detectability \[5, pp. 170--171\]

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ is detectable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A} + {\mathbf{L}\mathbf{C}}$ is Hurwitz with $\mathbf{L} = {- {\frac{1}{2}\mathbf{P}^{- \mathbf{1}}\mathbf{C}^{\mathsf{T}}}}$. Equivalently, $\mathcal{G}$ is detectable if and only if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A} + {\mathbf{L}\mathbf{C}}$ is Hurwitz with $\mathbf{L} = {- {\frac{1}{2}\mathbf{P}^{- \mathbf{1}}\mathbf{W}^{\mathsf{T}}}}$.

### Discrete-Time Detectability \[5, pp. 177--178\]

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The system $\mathcal{G}$ is detectable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A}_{d} + {\mathbf{L}\mathbf{C}}_{d}$ is Schur with $\mathbf{L} = {- {\mathbf{A}_{d}\mathbf{P}^{- \mathbf{1}}\mathbf{C}_{d}^{\mathsf{T}}\left({\mathbf{2}\mathbf{1} + {\mathbf{C}_{d}\mathbf{P}^{- \mathbf{1}}\mathbf{C}_{d}^{\mathsf{T}}}} \right)^{- \mathbf{1}}}}$. Equivalently, $\mathcal{G}$ is detectable if and only if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{W} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The matrix $\mathbf{A}_{d} + {\mathbf{L}\mathbf{C}}_{d}$ is Schur with $\mathbf{L} = {\mathbf{P}^{- \mathbf{1}}\mathbf{W}}$.

### Static Output Feedback Stabilizability

### Continuous-Time Static Output Feedback Stabilizability, \[93, p. 120\]

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{0})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. The system $\mathcal{G}$ is static output feedback stabilizable under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$, such that There exist $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$, $\mathbf{P}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{X} > \mathbf{0}$, such that There exist $\mathbf{K} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{Q}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{Q} > \mathbf{0}$ and $\mathbf{X} > \mathbf{0}$, such that

### Discrete-Time Static Output Feedback Stabilizability

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{0})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. The system $\mathcal{G}$ is static output feedback stabilizable under any of the following equivalent necessary and sufficient conditions.

There exist $\mathbf{K}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{K}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Applying the reverse Schur complement lemma to (3.81) yields Multiplying out this matrix inequality and adding $\mathbf{0} = {{\mathbf{A}_{d}{\mathbf{P}\mathbf{P}\mathbf{A}}_{d}} - {\mathbf{A}_{d}{\mathbf{P}\mathbf{P}\mathbf{A}}_{d}}}$ to the left-hand side gives Applying the Schur complement lemma twice gives (3.82). ∎ The system $\mathcal{G}$ is also static output feedback stabilizable if there exist $\mathbf{K}_{d} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{p}}$ and $\mathbf{P}$, $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{X} > \mathbf{0}$, such that

### Proof

Using completion of the squares, it can be shown that Substituting (3.84) into (3.82) and using the Schur complement lemma yields (3.83). The matrix inequality in (3.83) is only a sufficient condition for static output feedback stabilizability since (3.84) is an inequality. ∎

### Strong Stabilizability

### Continuous-Time Strong Stabilizability

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{0})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and it is assumed that $(\mathbf{A},\mathbf{B})$ is stabilizable, $(\mathbf{A},\mathbf{C})$ is detectable, and the transfer matrix ${\mathbf{G}{(\mathbf{s})}} = {\mathbf{C}\left({{\mathbf{s}\mathbf{1}} - \mathbf{A}} \right)^{- \mathbf{1}}\mathbf{B}}$ has no poles on the imaginary axis. The system $\mathcal{G}$ is strongly stabilizable if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that where $\mathbf{F} = {- {\mathbf{B}^{\mathsf{T}}\mathbf{X}}}$ and $\mathbf{X} \in {\mathbb{S}}_{\mathbf{n}}$, $\mathbf{X} \geq \mathbf{0}$ is the solution to the Lyapunov equation given by Moreover, a controller that strongly stabilizes $\mathcal{G}$ is given by the state-space realization

### Discrete-Time Strong Stabilizability

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{0})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and it is assumed that $(\mathbf{A}_{d},\mathbf{B}_{d})$ is stabilizable, $(\mathbf{A}_{d},\mathbf{C}_{d})$ is detectable, and the transfer matrix ${\mathbf{G}{(\mathbf{z})}} = {\mathbf{C}_{d}\left({{\mathbf{z}\mathbf{1}} - \mathbf{A}_{d}} \right)^{- \mathbf{1}}\mathbf{B}_{d}}$ has no poles on the unit circle. The system $\mathcal{G}$ is strongly stabilizable if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Z} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{p}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that where $\mathbf{N}_{\mathbf{1}\mathbf{1}} = {{{\left({\mathbf{A}_{d} + {\mathbf{B}_{d}\mathbf{F}}} \right)^{\mathsf{T}}\mathbf{P}\left({\mathbf{A}_{d} + {\mathbf{B}_{d}\mathbf{F}}} \right)} - \mathbf{P}} + {\left({\mathbf{A}_{d} + {\mathbf{B}_{d}\mathbf{F}}} \right)^{\mathsf{T}}{\mathbf{Z}\mathbf{C}}_{d}} + {\mathbf{C}_{d}^{\mathsf{T}}\mathbf{Z}^{\mathsf{T}}\left({\mathbf{A}_{d} + {\mathbf{B}_{d}\mathbf{F}}} \right)}}$, $\mathbf{F} = {- {\mathbf{B}_{d}^{\mathsf{T}}\mathbf{X}}}$, $\mathbf{X} = \mathbf{Y}$, and $\mathbf{Y} \in {\mathbb{S}}_{\mathbf{n}}$, $\mathbf{Y} \geq \mathbf{0}$ is the solution to the discrete-time Lyapunov equation given by Moreover, a discrete-time controller that strongly stabilizes $\mathcal{G}$ is given by the state-space realization

### Proof

The proof follows the same procedure as in for the continuous-time case, where (3.85) ensures that the feedback controller defined by (3.87) and (3.88) renders the closed-loop system asymptotically stable and (3.86) ensures that the feedback controller defined by (3.87) and (3.88) has a finite $\mathcal{H}_{\infty}$ norm, and thus is asymptotically stable. ∎

### System Zeros

### System Zeros without Feedthrough

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{0})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. The transmission zeros of ${\mathbf{G}{(\mathbf{s})}} = {\mathbf{C}\left( {{\mathbf{s}\mathbf{1}} - \mathbf{A}} \right)^{- \mathbf{1}}\mathbf{B}}$ are the eigenvalues of $\mathbf{N}\mathbf{A}\mathbf{M}$, where $\mathbf{N} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{n}}$, $\mathbf{M} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{q}}$, ${\mathbf{C}\mathbf{M}} = \mathbf{0}$, ${\mathbf{N}\mathbf{B}} = \mathbf{0}$, and ${\mathbf{N}\mathbf{M}} = \mathbf{1}$. Therefore, $\mathbf{G}{(\mathbf{s})}$ is minimum phase if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{q}}$, where $\mathbf{P} > \mathbf{0}$, such that

### System Zeros with Feedthrough

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with minimal state-space realization $(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D})$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, $m \leq p$, and $\mathbf{D}$ is full rank. The transmission zeros of ${\mathbf{G}{(\mathbf{s})}} = {{\mathbf{C}\left({{\mathbf{s}\mathbf{1}} - \mathbf{A}} \right)^{- \mathbf{1}}\mathbf{B}} + \mathbf{D}}$ are the eigenvalues of $\mathbf{A} - {\mathbf{B}\left({\mathbf{D}^{\mathsf{T}}\mathbf{D}} \right)^{- \mathbf{1}}\mathbf{D}^{\mathsf{T}}\mathbf{C}}$. $\mathbf{G}{(\mathbf{s})}$ is minimum phase if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If the system is square ($m = p$), then $\mathbf{D}$ full rank implies $\mathbf{D}^{- \mathbf{1}}$ exists and (3.89) simplifies to

### Proof

The system $\mathcal{G}$ can be written in state-space form as Left-multiplying (3.92) by $\mathbf{D}^{\mathsf{T}}$ and rearranging yields Since $\mathbf{D}$ is full rank, $\left({\mathbf{D}^{\mathsf{T}}\mathbf{D}} \right)^{- 1}$ exists. Therefore, left-multiplying (3.93) by $\left({\mathbf{D}^{\mathsf{T}}\mathbf{D}} \right)^{- 1}$ gives Substituting (3.94) into (3.91) gives the following state-space representation of the inverted transfer matrix from $\mathbf{y}$ to $\mathbf{u}$.

The transmission zeros of $\mathbf{G}{(\mathbf{s})}$ are the poles of the inverted transfer matrix from $\mathbf{y}$ to $\mathbf{u}$, which are the eigenvalues of $\left( {\mathbf{A} - {\mathbf{B}\left( {\mathbf{D}^{\mathsf{T}}\mathbf{D}} \right)^{- \mathbf{1}}\mathbf{D}^{\mathsf{T}}\mathbf{C}}} \right)$. Substituting this matrix into a Lyapunov inequality gives the desired inequality in (3.89).

If the system is square and $\mathbf{D}^{- \mathbf{1}}$ exists, then ${\left({\mathbf{D}^{\mathsf{T}}\mathbf{D}} \right)^{- 1}\mathbf{D}^{\mathsf{T}}} = \mathbf{D}^{- \mathbf{1}}$ and (3.89) simplifies to (3.90). ∎ The transfer matrix $\mathbf{G}{(\mathbf{s})}$ is also minimum phase if and only if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Q} = \mathbf{P}^{- \mathbf{1}}$, such that where $\mathbf{N} \in {\mathbb{R}}^{\mathbf{q} \times \mathbf{n}}$, $\mathbf{M} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{q}}$, ${\mathcal{R}{(\mathbf{N}^{\mathsf{T}})}} = {\mathcal{N}{(\mathbf{B}^{\mathsf{T}})}}$, and ${\mathcal{R}{(\mathbf{M})}} = {\mathcal{N}{(\mathbf{C})}}$.

### Proof

Applying the Strict Projection Lemma to (3.89) yields (3.97) and (3.98). ∎

### Discrete-Time System Zeros with Feedthrough

Consider a discrete-time LTI system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, with minimal state-space realization $(\mathbf{A}_{d},\mathbf{B}_{d},\mathbf{C}_{d},\mathbf{D}_{d})$, where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, $m \leq p$, and $\mathbf{D}_{d}$ is full rank. The transmission zeros of ${\mathbf{G}{(\mathbf{z})}} = {{\mathbf{C}_{d}\left({{\mathbf{z}\mathbf{1}} - \mathbf{A}_{d}} \right)^{- \mathbf{1}}\mathbf{B}_{d}} + \mathbf{D}_{d}}$ are the eigenvalues of $\mathbf{A}_{d} - {\mathbf{B}_{d}\left({\mathbf{D}_{d}^{\mathsf{T}}\mathbf{D}_{d}} \right)^{- \mathbf{1}}\mathbf{D}_{d}^{\mathsf{T}}\mathbf{C}_{d}}$. Therefore, $\mathbf{G}{(\mathbf{z})}$ is minimum phase if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If the system is square ($m = p$), then $\mathbf{D}_{d}$ full rank implies $\mathbf{D}_{d}^{- \mathbf{1}}$ exists and (3.99) simplifies to

### Proof

The proof follows the same procedure used in the proof of the continuous-time result in Section 3.15.2. ∎

### $\mathcal{D}$-Stability

### General LMI Region $\mathcal{D}$-Stability \[5, pp. 107--108\],

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The eigenvalues of a $\mathcal{D}$-stable matrix lie within the LMI region $\mathcal{D}$ of the complex plane, which is defined as $\mathcal{D} = {\{{z \in {\mathbb{C}}}:{{f_{\mathcal{D}}{(z)}} < 0}\}}$, where $\mathbf{\Lambda} \in {\mathbb{S}}^{m}$, $\mathbf{\Phi} \in {\mathbb{R}}^{m \times m}$, and $\overline{z}$ is the complex conjugate of $z$.

The matrix $\mathbf{A}$ is $\mathcal{D}$-stable if and only if any of the following equivalent conditions are satisfied.

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that where $\otimes$ is the Kroenecker product.

Alternatively, consider the LMI region $\mathcal{D}$ of the complex plane defined by \[3, p. 66\] where $\mathbf{Q}$, $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$ and $\mathbf{S} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The matrix $\mathbf{A}$ is $\mathcal{D}$-stable if and only if there exists $\mathbf{P}$ such that

### $\alpha$-Stability Region

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\alpha \in {\mathbb{R}}_{> 0}$. The matrix $\mathbf{A}$ satisfies ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\alpha)}}$, where ${\mathcal{D}{(\alpha)}}:={\{{z \in {\mathbb{C}}}:{{\text{Re}{(z)}} < {- \alpha}}\}}$ if and only if any of the following equivalent conditions are satisfied.

\[1, pp. 66-67\], \[5, p. 99\], There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

which is equivalent to (3.102) using the Schur complement. ∎ There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\epsilon \in {\mathbb{R}}_{> 0}$, and $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that Moreover, for every $\mathbf{X}$ that satisfies (3.101), $\mathbf{X}$ and $\mathbf{F} = {- {\epsilon^{- \mathbf{1}}\left({\mathbf{A} - {\epsilon^{- \mathbf{1}}\mathbf{1}}} \right)^{- \mathbf{1}}\mathbf{X}}}$ are solutions to (3.103).

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{Y}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{2}}$, $\mathbf{Y}_{\mathbf{3}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{X}_{\mathbf{2}}$, $\mathbf{X}_{\mathbf{3}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\alpha)}}$, then the solution to $\overset{˙}{\mathbf{x}} = {\mathbf{A}\mathbf{x}}$, ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$ satisfies $\left\| {\mathbf{x}{(\mathbf{t})}} \right\|_{2} \leq {\sqrt{\kappa{(\mathbf{P})}}\left\| \mathbf{x}_{\mathbf{0}} \right\|_{2}e^{- {\alphat}}}$, where $\kappa{(\mathbf{P})}$ is the condition number of $\mathbf{P}$. This system is exponentially stable with exponential decay rate $\alpha$.

### Vertical Band \[5, p. 99\],

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\alpha$, $\beta \in {\mathbb{R}}_{> 0}$. The matrix $\mathbf{A}$ satisfies ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\alpha,\beta)}}$, where ${\mathcal{D}{(\alpha,\beta)}}:={\{{z \in {\mathbb{C}}}:{{- \beta} < {\text{Re}{(z)}} < {- \alpha}}\}}$ if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that If ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\alpha,\beta)}}$, then the solution to $\overset{˙}{\mathbf{x}} = {\mathbf{A}\mathbf{x}}$, ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$ satisfies $\left\| {\mathbf{x}{(\mathbf{t})}} \right\|_{2} \leq {\sqrt{\kappa{(\mathbf{P})}}\left\| \mathbf{x}_{\mathbf{0}} \right\|_{2}e^{- {\alphat}}}$, where $\kappa{(\mathbf{P})}$ is the condition number of $\mathbf{P}$. This system is exponentially stable with exponential decay rate $\alpha$.

### Conic Sector Region

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\theta \in {\mathbb{R}}_{> 0}$. The matrix $\mathbf{A}$ satisfies ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\mathbf{k})}}$, where ${\mathcal{D}{(k)}}:={\{{z \in {\mathbb{C}}}:{{\left| {\text{Im}{(z)}} \right| < {- {{\tan{(\theta)}}\text{Re}{(z)}}}},{\, 0 < \theta < {\pi/2}}}\}}$, if and only if any of the following equivalent conditions are satisfied.

\[5, pp. 105--106\], There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that where $k = {\tan{(\theta)}}$.

There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\epsilon \in {\mathbb{R}}_{> 0}$, and $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that where $k = {\tan{(\theta)}}$. Moreover, for every $\mathbf{X}$ that satisfies (3.104), $\mathbf{X}$ and $\mathbf{F} = {- {\epsilon^{- \mathbf{1}}\left({\mathbf{A} - {\epsilon^{- \mathbf{1}}\mathbf{1}}} \right)^{- \mathbf{1}}\mathbf{X}}}$ are solutions to (3.105).

### Circular Region

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $r \in {\mathbb{R}}_{> 0}$, and $c \in {\mathbb{R}}_{< 0}$, where $c < {- r}$. The matrix $\mathbf{A}$ satisfies ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\mathbf{c},\mathbf{r})}}$, where ${\mathcal{D}{(c,r)}}:={\{{z \in {\mathbb{C}}}:{{\left( {{\text{Re}{(z)}} - c} \right)^{2} + \left( {\text{Im}{(z)}} \right)^{2}} < r^{2}}\}}$, if and only if any of the following equivalent conditions are satisfied.

\[5, p. 101\], There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that There exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, $\epsilon \in {\mathbb{R}}_{> 0}$, and $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that Moreover, for every $\mathbf{X}$ that satisfies (3.106), $\mathbf{X}$ and $\mathbf{F} = {- {\epsilon^{- \mathbf{1}}\left({\mathbf{A} - {\epsilon^{- \mathbf{1}}\mathbf{1}}} \right)^{- \mathbf{1}}\mathbf{X}}}$ are solutions to (3.107).

### Horizontal Band, \[192, p. 164\], \[193, p. 48\]

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$. The matrix $\mathbf{A}$ satisfies ${\lambda{(\mathbf{A})}} \subset {\mathcal{D}{(\gamma)}}$, where ${\mathcal{D}{(\gamma)}}:={\{{z \in {\mathbb{C}}}:{\left| {\text{Im}{(z)}} \right| < \gamma}\}}$ if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### $\mathcal{D}$-Admissibility

### General LMI Region $\mathcal{D}$-Admissibility

Consider $\mathbf{A}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The pair $(\mathbf{E},\mathbf{A})$ is $\mathcal{D}$-admissible if it is regular and causal, and the eigenvalues of $(\mathbf{E},\mathbf{A})$ lie within the LMI region $\mathcal{D}$ of the complex plane, which is defined as $\mathcal{D} = {\{{z \in {\mathbb{C}}}:{{f_{\mathcal{D}}{(z)}} < 0}\}}$, where $\mathbf{\Lambda} \in {\mathbb{S}}^{m}$, $\mathbf{\Phi} \in {\mathbb{R}}^{m \times m}$, and $\overline{z}$ is the complex conjugate of $z$.

The pair $(\mathbf{E},\mathbf{A})$ is $\mathcal{D}$-admissible if and only if any of the following equivalent conditions are satisfied.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, and $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E})}}$, and $\mathbf{P} > \mathbf{0}$, satisfying There exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}^{\mathsf{T}}{\mathbf{Q}\mathbf{E}}} \geq \mathbf{0}$ and There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, $\mathbf{U} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathbf{U}\mathbf{E}} = \mathbf{0}$, and $\mathbf{P} > \mathbf{0}$, satisfying There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, and $\mathbf{U}$, $\mathbf{V} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathcal{R}{(\mathbf{U})}} = {\mathcal{N}{(\mathbf{E}^{\mathsf{T}})}}$, ${\mathcal{R}{(\mathbf{V})}} = {\mathcal{N}{(\mathbf{E})}}$, and $\mathbf{P} > \mathbf{0}$, satisfying where $\otimes$ is the Kroenecker product and $\mathbf{1}_{\mathbf{m}\mathbf{m}}$ is an $m \times m$ matrix filled with ones.

There exist $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, satisfying ${\mathbf{E}^{\mathsf{T}}{\mathbf{Q}\mathbf{E}}} \geq \mathbf{0}$ and where $\otimes$ is the Kroenecker product and $\mathbf{1}_{\mathbf{m}\mathbf{m}}$ is an $m \times m$ matrix filled with ones.

There exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{R}}^{{(\mathbf{n} - \mathbf{n}_{\mathbf{e}})} \times {(\mathbf{n} - \mathbf{n}_{\mathbf{e}}}}$, $\mathbf{U} \in {\mathbb{R}}^{\mathbf{n} \times {({\mathbf{n} - \mathbf{n}_{\mathbf{e}}})}}$, where $n_{e} = {\text{rank}{(\mathbf{E})}}$, ${\mathbf{U}\mathbf{E}} = \mathbf{0}$, and $\mathbf{P} > \mathbf{0}$, satisfying where $\otimes$ is the Kroenecker product and $\mathbf{1}_{\mathbf{m}\mathbf{m}}$ is an $m \times m$ matrix filled with ones.

### Circular Region

Consider $\mathbf{A}$, $\mathbf{E} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $a$, $b \in {\mathbb{R}}$, and $d \in {\mathbb{R}}_{> 0}$, where $b \neq 0$. The pair $(\mathbf{E},\mathbf{A})$ is $\mathcal{D}$-admissible with $\mathcal{D} = {\{{z \in {\mathbb{C}}}:{{a + {2b\text{Re}{(z)}} + {d|z|^{2}}} < 0}\}}$ if and only if there exist $\mathbf{X} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\alpha \in {\mathbb{R}}$ such that ${\mathbf{E}^{\mathsf{T}}\mathbf{X}} = {\mathbf{X}^{\mathsf{T}}\mathbf{E}} \geq \mathbf{0}$ and where $\mathbf{E}^{\dagger}$ is the pseudoinverse of $\mathbf{E}$. The region $\mathcal{D}$ describes a circular region of the complex plane with radius $r = \sqrt{{- {a/d}} + {b^{2}/d^{2}}}$ centered at $(c,0)$, where $c = {- {b/d}}$.

### DC Gain of a Transfer Matrix

Consider $\gamma \in {\mathbb{R}}_{> 0}$ and a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with transfer matrix ${\mathbf{G}{(\mathbf{s})}} = {{\mathbf{C}\left( {{\mathbf{s}\mathbf{1}} - \mathbf{A}} \right)^{- \mathbf{1}}\mathbf{B}} + \mathbf{D}}$, where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The DC gain of $\mathcal{G}$ is strictly less than $\gamma$ (i.e., ${\overline{\sigma}{({\mathbf{G}{(\mathbf{0})}})}} < \gamma$) if and only if

### Proof

${\overline{\sigma}{({\mathbf{G}{(\mathbf{0})}})}} < \gamma$ if and only if ${\overline{\lambda}\left({\mathbf{G}{(\mathbf{0})}\mathbf{G}^{\mathsf{T}}{(\mathbf{0})}} \right)} < \gamma^{2}$, or equivalently Substituting ${\mathbf{G}{(\mathbf{0})}} = {{- {{\mathbf{C}\mathbf{A}}^{- \mathbf{1}}\mathbf{B}}} + \mathbf{D}}$ into (3.110) gives (3.108). Starting with ${{\overline{\sigma}{({\mathbf{G}{(\mathbf{0})}})}} < \gamma}\Leftrightarrow{{\overline{\lambda}\left({\mathbf{G}^{\mathsf{T}}{(\mathbf{0})}\mathbf{G}{(\mathbf{0})}} \right)} < \gamma^{\mathbf{2}}}$ in the first step of the proof and following the same steps yields (3.109). ∎

### Transient Bounds

### Transient State Bound for Autonomous LTI Systems \[1, p. 88\],

Consider the continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$. The Euclidean norm of the state satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Define $V = {\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}}$. Evaluating $\overset{˙}{V}$ and substituting in the matrix inequality from (3.113) results in $\overset{˙}{V} \leq 0$. Integrating both sides of this inequality from $t = 0$ to $t = T$, where $T \in {\mathbb{R}}_{\geq 0}$ gives Using the non-strict Schur complement, (3.112) can be rewritten as ${\gamma^{- 1}\mathbf{1}} \leq \mathbf{P}$. Substituting this and (3.111) into (3.114) yields

### Transient State Bound for Discrete-Time Autonomous LTI Systems

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The Euclidean norm of the state satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Define ${V{(k)}} = {\mathbf{x}_{\mathbf{k}}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}_{\mathbf{k}}}$. Evaluating ${V{({k + 1})}} - {V{(k)}}$ and substituting in the matrix inequality from (3.117) results in Using induction, this inequality implies Using the non-strict Schur complement, (3.116) can be rewritten as ${\gamma^{- 1}\mathbf{1}} \leq \mathbf{P}$. Substituting this and (3.115) into (3.118) yields

### Transient State Bound for Non-Autonomous LTI Systems \[1, p. 77--78\]

Consider the continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$ and ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$. The Euclidean norm of the state satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If $\mathbf{x}_{\mathbf{0}} = \mathbf{0}$ and $\mathbf{u}$ is a unit-energy input (i.e., $\left\| \mathbf{u} \right\|_{2T} \leq 1$, ${\forall T} \in {\mathbb{R}}_{\geq 0}$), then the preceding conditions ensure that $\left\| {\mathbf{x}{(\mathbf{T})}} \right\|_{2} \leq \gamma$, ${\forall T} \in {\mathbb{R}}_{\geq 0}$.

### Proof

Define $V = {\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}}$. Evaluating $\overset{˙}{V}$ results in Substituting (3.121) into (3.122) gives $\overset{˙}{V} \leq {\gamma\mathbf{u}^{\mathsf{T}}\mathbf{u}}$. Integrating both sides of this inequality from $t = 0$ to $t = T$, where $T \in {\mathbb{R}}_{\geq 0}$ yields Substituting (3.119) and (3.120) into (3.123) results in

### Transient State Bound for Discrete-Time Non-Autonomous LTI Systems

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$. The Euclidean norm of the state satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If $\mathbf{x}_{\mathbf{0}} = \mathbf{0}$ and $\mathbf{u}$ is a unit-energy input (i.e., $\left\| \mathbf{u} \right\|_{2k} \leq 1$, ${\forall k} \in {\mathbb{Z}}_{\geq 0}$), then the preceding conditions ensure that $\left\| \mathbf{x}_{\mathbf{k}} \right\|_{2} \leq \gamma$, ${\forall k} \in {\mathbb{Z}}_{\geq 0}$.

### Proof

Define ${V{(k)}} = {\mathbf{x}_{\mathbf{k}}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}_{\mathbf{k}}}$. Evaluating ${V{({k + 1})}} - {V{(k)}}$ results in Substituting in (3.126) and using induction gives Substituting (3.124) and (3.125) into (3.128) yields

### Transient Output Bound for Autonomous LTI Systems \[1, p. 88\],

Consider the continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$ and ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$. The Euclidean norm of the output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{p}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

The proof follows the same procedure as the proof in Section 3.19.1, except the inequalities in (3.129) and (3.130) are substituted in to the inequality of (3.114). ∎

### Transient Output Bound for Discrete-Time Autonomous LTI Systems

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. The Euclidean norm of the output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

The proof follows the same procedure as the proof in Section 3.19.2, except the inequalities in (3.131) and (3.132) are substituted in to the inequality of (3.118). ∎

### Transient Output Bound for Non-Autonomous LTI Systems

Consider the continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$. The Euclidean norm of the output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{p}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If $\mathbf{x}_{\mathbf{0}} = \mathbf{0}$ and $\mathbf{u}$ is a unit-energy input (i.e., $\left\| \mathbf{u} \right\|_{2T} \leq 1$, ${\forall T} \in {\mathbb{R}}_{\geq 0}$), then the preceding conditions ensure that $\left\| {\mathbf{y}{(\mathbf{T})}} \right\|_{2} \leq \gamma$, ${\forall T} \in {\mathbb{R}}_{\geq 0}$.

### Proof

The proof follows the same procedure as the proof in Section 3.19.3, except the inequalities in (3.133) and (3.134) are substituted in to the inequality of (3.123). ∎

### Transient Output Bound for Discrete-Time Non-Autonomous LTI Systems

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. The Euclidean norm of the output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If $\mathbf{x}_{\mathbf{0}} = \mathbf{0}$ and $\mathbf{u}$ is a unit-energy input (i.e., $\left\| \mathbf{u} \right\|_{2k} \leq 1$, ${\forall k} \in {\mathbb{Z}}_{\geq 0}$), then the preceding conditions ensure that $\left\| \mathbf{y}_{\mathbf{k}} \right\|_{2} \leq \gamma$, ${\forall k} \in {\mathbb{Z}}_{\geq 0}$.

### Proof

The proof follows the same procedure as the proof in Section 3.19.4, except the inequalities in (3.135) and (3.136) are substituted in to the inequality of (3.128). ∎

### Transient Impulse Response Bound

Consider the single-input multi-output continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{1}}$, and $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. Let ${\mathbf{z}{(\mathbf{t})}} = {{\mathbf{C}\mathbf{e}}^{\mathbf{A}\mathbf{t}}\mathbf{B}}$ be the unit impulse response of the system. The Euclidean norm of the impulse response satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{p}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

The proof follows the same procedure as the proof in Section 3.19.5, where the initial condition is chosen as $\mathbf{x}_{\mathbf{0}} = \mathbf{B}$. This yields the result Using the non-strict Schur complement, the matrix inequality in (3.137) is equivalent to ${\mathbf{B}^{\mathsf{T}}{\mathbf{P}\mathbf{B}}} \leq \gamma$. Substituting this and (3.138) into (3.139) gives the desired result. ∎

### Discrete-Time Transient Impulse Response Bound

Consider the single-input multi-output discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{1}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and it is assumed that $\mathbf{A}_{d}$ is invertible. Let $\mathbf{z}_{\mathbf{k}} = {\mathbf{C}_{d}\mathbf{A}_{d}^{\mathbf{k} - \mathbf{1}}\mathbf{B}_{d}}$ be the unit impulse response of the system. The Euclidean norm of the impulse response satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

The proof follows the same procedure as the proof in Section 3.19.6, where the initial condition is chosen as $\mathbf{x}_{\mathbf{0}} = {\mathbf{A}_{d}^{- \mathbf{1}}\mathbf{B}_{d}}$ so that the unit impulse response matching the free response $\mathbf{z}_{\mathbf{k}} = {\mathbf{C}_{d}\mathbf{A}_{d}^{\mathbf{k}}\mathbf{x}_{\mathbf{0}}}$. This yields the result Using the non-strict Schur complement, the matrix inequality in (3.140) is equivalent to the inequality ${\mathbf{B}_{d}^{\mathsf{T}}\mathbf{A}_{d}^{- \mathsf{T}}{\mathbf{P}\mathbf{A}}_{d}^{- \mathbf{1}}\mathbf{B}_{d}} \leq \gamma$. Substituting this and (3.141) into (3.142) gives the desired result. ∎

### Output Energy Bounds

### Output Energy Bound for Autonomous LTI Systems \[1, pp. 85--86\]

Consider the continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$ and ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$. The output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{p}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Define $V = {\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}}$. Evaluating $\overset{˙}{V}$ results in Using the Schur complement lemma and substituting (3.144) into (3.145) gives $\overset{˙}{V} \leq {- {\gamma^{- 1}\mathbf{y}^{\mathsf{T}}\mathbf{y}}}$. Integrating both sides of this inequality from $t = 0$ to $t = T$, where $T \in {\mathbb{R}}_{\geq 0}$ yields Substituting (3.143) into (3.146) results in

### Output Energy Bound for Discrete-Time Autonomous LTI Systems

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$. The output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

### Proof

Define ${V{(k)}} = {\mathbf{x}_{\mathbf{k}}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}_{\mathbf{k}}}$. Evaluating ${V{({k + 1})}} - {V{(k)}}$ results in Using the Schur complement lemma, substituting (3.148) into (3.149), and using induction gives Substituting (3.147) into (3.150) yields

### Output Energy Bound for Non-Autonomous LTI Systems

Consider the continuous-time LTI system with state-space realization where $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, $\mathbf{D} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$, and ${\mathbf{x}{(\mathbf{0})}} = \mathbf{x}_{\mathbf{0}}$. The output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{p}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If $\mathbf{x}_{\mathbf{0}} = \mathbf{0}$, then the preceding conditions match the Bounded Real Lemma and ensure that $\left\| \mathbf{y} \right\|_{2T} \leq {\gamma\left\| \mathbf{u} \right\|_{2T}}$, ${\forall T} \in {\mathbb{R}}_{\geq 0}$.

### Proof

Define $V = {\mathbf{x}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}}$. Evaluating $\overset{˙}{V}$ results in Using the Schur complement lemma and substituting (3.152) into (3.153) gives $\overset{˙}{V} \leq {{\gamma\mathbf{u}^{\mathsf{T}}\mathbf{u}} - {\gamma^{- \mathbf{1}}\mathbf{y}^{\mathsf{T}}\mathbf{y}}}$. Integrating both sides of this inequality from $t = 0$ to $t = T$, where $T \in {\mathbb{R}}_{\geq 0}$ yields Substituting (3.151) into (3.154) results in

### Output Energy Bound for Discrete-Time Non-Autonomous LTI Systems

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{C}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{n}}$, and $\mathbf{D}_{d} \in {\mathbb{R}}^{\mathbf{p} \times \mathbf{m}}$. The output satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that If $\mathbf{x}_{\mathbf{0}} = \mathbf{0}$, then the preceding conditions match the Bounded Real Lemma and ensure that $\left\| \mathbf{y} \right\|_{2k} \leq {\gamma\left\| \mathbf{u} \right\|_{2k}}$, ${\forall k} \in {\mathbb{Z}}_{\geq 0}$.

### Proof

Define ${V{(k)}} = {\mathbf{x}_{\mathbf{k}}^{\mathsf{T}}{\mathbf{P}\mathbf{x}}_{\mathbf{k}}}$. Evaluating ${V{({k + 1})}} - {V{(k)}}$ results in Using the Schur complement lemma, substituting (3.156) into (3.157), and using induction gives Substituting (3.155) into (3.158) yields

### Kharitonov-Bernstein-Haddad (KBH) Theorem

Consider the set of matrices Every matrix in the set $\mathcal{A}$ is Hurwitz if and only if there exist $\mathbf{P}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {1,2,3,4}$, where $\mathbf{P}_{\mathbf{i}} > \mathbf{0}$, $i = {1,2,3,4}$, such that Equivalently, every matrix in the set $\mathcal{A}$ is Hurwitz if and only if there exist $\mathbf{Q}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {1,2,3,4}$, where $\mathbf{Q}_{\mathbf{i}} > \mathbf{0}$, $i = {1,2,3,4}$, such that

### Stability of Discrete-Time System with Polytopic Uncertainty

### Open-Loop Robust Stability

Consider the set of matrices The discrete-time LTI system $\mathbf{x}_{\mathbf{k} + \mathbf{1}} = {\mathbf{A}_{d}{(\alpha)}\mathbf{x}_{\mathbf{k}}}$ is asymptotically stable for all ${\mathbf{A}_{d}{(\alpha)}} \in {\mathcal{A}}$ if there exist $\mathbf{P}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {1,\ldots,n}$, and $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P}_{\mathbf{i}} > \mathbf{0}$, $i = {1,\ldots,n}$, such that

### Closed-Loop Robust Stability

Consider the set of matrices The discrete-time LTI system $\mathbf{x}_{\mathbf{k} + \mathbf{1}} = {{\mathbf{A}_{d}{(\alpha)}\mathbf{x}_{\mathbf{k}}} + {\mathbf{B}_{d}{(\beta)}\mathbf{u}_{\mathbf{k}}}}$ is asymptotically stabilized by the state feedback control law $\mathbf{u}_{\mathbf{k}} = {- {{\mathbf{L}\mathbf{G}}^{- \mathbf{1}}\mathbf{u}_{\mathbf{k}}}}$ for all ${\mathbf{A}_{d}{(\alpha)}} \in {\mathcal{A}}$ and ${\mathbf{B}_{d}{(\alpha)}} \in {\mathcal{B}}$ if there exist $\mathbf{P}_{\mathbf{i}\mathbf{j}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {1,\ldots,n}$, $j = {1,\ldots,p}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, and $\mathbf{L} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, where $\mathbf{P}_{\mathbf{i}\mathbf{j}} > \mathbf{0}$, $i = {1,\ldots,n}$, $j = {1,\ldots,p}$ and $\mathbf{G}$ is invertible, such that

### Quadratic Stability

### Continuous-Time Quadratic Stability \[5, pp. 112--115\]

Consider the uncertain continuous-time linear system with state-space representation where $\mathbf{A}_{\mathbf{0}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, ${\Delta\mathbf{A}{({{\mathbf{δ}}{(\mathbf{t})}})}} = {\sum_{\mathbf{i} = \mathbf{1}}^{\mathbf{k}}{\delta_{\mathbf{i}}{(\mathbf{t})}\mathbf{A}_{\mathbf{i}}}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\delta_{i} \in {\mathbb{R}}$, $i = {1,\ldots,k}$, $\mathbf{A}_{\mathbf{i}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $i = {1,\ldots,k}$, ${{\mathbf{δ}}^{\mathsf{T}}{(t)}} = \begin{bmatrix} {\delta_{1}{(t)}} & {\delta_{2}{(t)}} & \cdots & {\delta_{k}{(t)}} \end{bmatrix} \in \mathbf{\Delta}$, and $\mathbf{\Delta}$ is the set of perturbation parameters. The uncertain system in (3.160) is quadratically stable if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The following statements can be made for particular sets of perturbations.

Consider the case where the set of perturbation parameters is defined by a regular polyhedron as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Consider the case where the set of perturbation parameters is defined by a polytope as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Discrete-Time Quadratic Stability \[5, pp. 116--118\]

Consider the uncertain discrete-time linear system with state-space representation where $\mathbf{A}_{d,\mathbf{0}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, ${\Delta\mathbf{A}_{d}{({{\mathbf{δ}}{(\mathbf{t})}})}} = {\sum_{\mathbf{i} = \mathbf{1}}^{\mathbf{k}}{\delta_{\mathbf{i}}{(\mathbf{t})}\mathbf{A}_{d,\mathbf{i}}}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\delta_{i} \in {\mathbb{R}}$, $i = {1,\ldots,k}$, $\mathbf{A}_{d,\mathbf{i}} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $i = {1,\ldots,k}$, ${{\mathbf{δ}}^{\mathsf{T}}{(t)}} = \begin{bmatrix} {\delta_{1}{(t)}} & {\delta_{2}{(t)}} & \cdots & {\delta_{k}{(t)}} \end{bmatrix} \in \mathbf{\Delta}$, and $\mathbf{\Delta}$ is the set of perturbation parameters. The uncertain system in (3.160) is quadratically stable if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that The following statements can be made for particular sets of perturbations.

Consider the case where the set of perturbation parameters is defined by a regular polyhedron as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Consider the case where the set of perturbation parameters is defined by a polytope as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

### Stability of Time-Delay Systems

Consider the continuous-time linear time-delay system with state-space representation where $\mathbf{A}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $d$, $\overline{d} \in {\mathbb{R}}_{> 0}$, and the initial condition is given by ${\mathbf{x}{(\mathbf{t})}} = {\mathbf{\phi}{(\mathbf{t})}}$, $t \in {\lbrack{- d},0\rbrack}$, where $\overline{d}$ is a known upper-bound on the time-delay (i.e., $0 < d \leq \overline{d}$).

### Delay-Independent Condition \[5, p. 126\]

The time-delay system in (3.162) is asymptotically stable if there exist $\mathbf{P}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{S} > \mathbf{0}$, such that

### Delay-Dependent Condition \[5, pp. 128--129\]

The time-delay system in (3.162) is uniformly asymptotically stable if there exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\beta \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\beta < 1$, such that

### $\mu$-Analysis \[1, p. 38--39\],

Consider the matrix $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and the invertible matrix $\mathbf{D} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The inequality ${\overline{\sigma}\left({\mathbf{D}\mathbf{A}\mathbf{D}}^{- \mathbf{1}} \right)} < \gamma$ holds if and only if there exist $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$, satisfying The inequality ${\overline{\sigma}\left({\mathbf{D}\mathbf{A}\mathbf{D}}^{- \mathbf{1}} \right)} < \gamma$ holds for $\mathbf{D} = \mathbf{X}^{\frac{1}{2}}$, where $\mathbf{X}$ satisfies (3.163).

### Static Output Feedback Algebraic Loop\[7, p. 1284\], \[175, pp. 39--40\]

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization where ${\mathbf{x}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}}}$ is the system state, ${\mathbf{z}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}}}$ is the performance signal, ${\mathbf{y}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{y}}}$ is the measurement signal, ${\mathbf{w}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{w}}}$ is the exogenous signal, ${\mathbf{u}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}}}$ is the control input signal, and the state-space matrices are real matrices with appropriate dimensions. Additionally, consider a static output feedback controller of the form $\mathbf{u} = {\mathbf{K}\mathbf{y}}$, where $\mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$ and it is assumed that the feedback interconnection is well-posed, that is, ${\det{({\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}})}} \neq \mathbf{0}$. The closed-loop system can be described by the following state-space realization. where $\overline{\mathbf{K}} = {\left({\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}} \right)^{- 1}\mathbf{K}}$.

The change of variable $\overline{\mathbf{K}} = {\left( {\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}} \right)^{- 1}\mathbf{K}}$ allows for the simplification of matrix inequalities involving the closed-loop system.

### Proof

Substituting the expression for $\mathbf{y}$ into $\mathbf{u} = {\mathbf{K}\mathbf{y}}$ gives Bringing the terms with $\mathbf{u}$ to the left-hand-side of the equation, left-multiplying by $\left({\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}} \right)^{- 1}$, and defining $\overline{\mathbf{K}} = {\left({\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}} \right)^{- 1}\mathbf{K}}$ yields Substituting (3.168) into (3.164) and (3.165) gives (3.166) and (3.167). ∎

## LMIs in Optimal Control

This section presents controller synthesis methods using LMIs for a number of well-known optimal control problems. The derivation of the LMIs used for controller synthesis is provided in some cases, while longer derivations can be found in the cited references.

### The Generalized Plant

### The Continuous-Time Generalized Plant

Figure 1: Block diagram of the generalized plant 𝒫 with the controller 𝒦.

Consider the generalized LTI plant ${\mathcal{P}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, shown in Figure 1, with a minimal state-space realization \[7, pp. 1291--1292\], \[4, Section 3.8\], \[200, p. 141\], \[201, pp. 14--16\], \[202, pp. 809--817\] where ${\mathbf{x}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}}}$ is the system state, ${\mathbf{z}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}}}$ is the performance signal, ${\mathbf{y}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{y}}}$ is the measurement signal, ${\mathbf{w}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{w}}}$ is the exogenous signal, ${\mathbf{u}{(\mathbf{t})}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}}}$ is the control input signal, and the state-space matrices are real matrices with appropriate dimensions. The generalized LTI plant can also be written in transfer matrix form as where the transfer matrix ${\mathbf{P}{(\mathbf{s})}} \in {\mathbb{C}}^{{({\mathbf{n}_{\mathbf{z}} + \mathbf{n}_{\mathbf{y}}})} \times {({\mathbf{n}_{\mathbf{w}} + \mathbf{n}_{\mathbf{u}}})}}$ is partitioned as The generalized plant, also known as the standard control problem in \[7, pp. 1291--1292\], \[201, pp. 14--16\] is useful, as it is possible to represent a number of LTI systems in this form, as shown in the following example.

### Example 4.1 (Basic Servo Loop Tracking \[175, p. 18\], \[201, p. 18\], )

Consider the basic servo loop shown in Figure 2 involving the LTI controller ${\mathbf{K}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{y}_{\mathbf{c}}} \times \mathbf{n}_{\mathbf{u}_{\mathbf{c}}}}$ and the plant ${\mathbf{G}_{\mathbf{p}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{y}_{\mathbf{p}}} \times \mathbf{n}_{\mathbf{u}_{\mathbf{p}}}}$, where the weighting transfer matrices are simply chosen as ${\mathbf{W}_{\mathbf{r}}{(\mathbf{s})}} = \mathbf{1}$, ${\mathbf{W}_{\mathbf{d}}{(\mathbf{s})}} = \mathbf{1}$, and ${\mathbf{W}_{\mathbf{n}}{(\mathbf{s})}} = \mathbf{1}$. The plant $\mathbf{G}_{\mathbf{p}}{(\mathbf{s})}$ has a minimal state-space realization $(\mathbf{A}_{\mathbf{p}},\mathbf{B}_{\mathbf{p}},\mathbf{C}_{\mathbf{p}},\mathbf{D}_{\mathbf{p}})$ and the state $\mathbf{x}_{\mathbf{p}}{(\mathbf{t})}$. The performance variables are the true tracking error ${\mathbf{z}_{\mathbf{1}}{(\mathbf{t})}} = {\mathbf{e}{(\mathbf{t})}} = {{\mathbf{r}{(\mathbf{t})}} - {\mathbf{y}_{\mathbf{p}}{(\mathbf{t})}}}$ and the control effort ${\mathbf{z}_{\mathbf{2}}{(\mathbf{t})}} = {\mathbf{u}_{\mathbf{c}}{(\mathbf{t})}}$, where ${\mathbf{z}^{\mathsf{T}}{(\mathbf{t})}} = \begin{bmatrix} {\mathbf{z}_{\mathbf{1}}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{z}_{\mathbf{2}}^{\mathsf{T}}{(\mathbf{t})}} \end{bmatrix}$. The generalized plant can be formulated with minimal state-space representation where ${\mathbf{x}{(\mathbf{t})}} = {\mathbf{x}_{\mathbf{p}}{(\mathbf{t})}}$, ${\mathbf{w}^{\mathsf{T}}{(\mathbf{t})}} = \begin{bmatrix} {\mathbf{r}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{d}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{n}^{\mathsf{T}}{(\mathbf{t})}} \end{bmatrix}$, ${\mathbf{u}{(\mathbf{t})}} = {\mathbf{u}_{\mathbf{c}}{(\mathbf{t})}}$, and ${\mathbf{y}{(\mathbf{t})}} = {{\mathbf{r}{(\mathbf{t})}} - {\mathbf{y}_{\mathbf{p}}{(\mathbf{t})}} - {\mathbf{n}{(\mathbf{t})}}}$.

Figure 2: Block diagram of the basic servo loop with plant Gp (s), controller K (s), and weighting transfer matrices Wr (s), Wd (s), and Wn (s).

### Example 4.2 (Basic Servo Loop Tracking with Weights \[4, Section 9.3.6\], \[175, p. 19\], \[204, pp. 169--170\])

Consider the same basic servo loop shown in Figure 2 involving the LTI controller ${\mathbf{K}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{y}_{\mathbf{c}}} \times \mathbf{n}_{\mathbf{u}_{\mathbf{c}}}}$, the plant ${\mathbf{G}_{\mathbf{p}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{y}_{\mathbf{p}}} \times \mathbf{n}_{\mathbf{u}_{\mathbf{p}}}}$, and the weighting transfer matrices ${\mathbf{W}_{\mathbf{r}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{r}} \times \mathbf{n}_{\mathbf{r}}}$, ${\mathbf{W}_{\mathbf{d}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{d}} \times \mathbf{n}_{\mathbf{d}}}$, and ${\mathbf{W}_{\mathbf{n}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{n}} \times \mathbf{n}_{\mathbf{n}}}$. The plant $\mathbf{G}_{\mathbf{p}}{(\mathbf{s})}$ has a minimal state-space realization $(\mathbf{A}_{\mathbf{p}},\mathbf{B}_{\mathbf{p}},\mathbf{C}_{\mathbf{p}},\mathbf{D}_{\mathbf{p}})$ and the weighting transfer matrices $\mathbf{W}_{\mathbf{r}}{(\mathbf{s})}$, $\mathbf{W}_{\mathbf{d}}{(\mathbf{s})}$, and $\mathbf{W}_{\mathbf{n}}{(\mathbf{s})}$ have minimal state-space realizations $(\mathbf{A}_{\mathbf{r}},\mathbf{B}_{\mathbf{r}},\mathbf{C}_{\mathbf{r}},\mathbf{D}_{\mathbf{r}})$, $(\mathbf{A}_{\mathbf{d}},\mathbf{B}_{\mathbf{d}},\mathbf{C}_{\mathbf{d}},\mathbf{D}_{\mathbf{d}})$, and $(\mathbf{A}_{\mathbf{n}},\mathbf{B}_{\mathbf{n}},\mathbf{C}_{\mathbf{n}},\mathbf{D}_{\mathbf{n}})$, respectively. The performance variable is defined as the weighted true tracking error ${\mathbf{z}_{\mathbf{1}}{(\mathbf{s})}} = {\mathbf{W}_{\mathbf{e}}{(\mathbf{s})}\mathbf{e}{(\mathbf{s})}} = {\mathbf{W}_{\mathbf{e}}{(\mathbf{s})}\left({{\mathbf{W}_{\mathbf{r}}{(\mathbf{s})}\mathbf{r}{(\mathbf{s})}} - {\mathbf{y}_{\mathbf{p}}{(\mathbf{s})}}} \right)}$ and the weighted control effort ${\mathbf{z}_{\mathbf{2}}{(\mathbf{s})}} = {\mathbf{W}_{\mathbf{u}}{(\mathbf{s})}\mathbf{u}_{\mathbf{c}}{(\mathbf{s})}}$, where ${\mathbf{z}^{\mathsf{T}}{(\mathbf{s})}} = \begin{bmatrix} {\mathbf{z}_{\mathbf{1}}^{\mathsf{T}}{(\mathbf{s})}} & {\mathbf{z}_{\mathbf{2}}^{\mathsf{T}}{(\mathbf{s})}} \end{bmatrix}$ and ${\mathbf{W}_{\mathbf{e}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{e}} \times \mathbf{n}_{\mathbf{e}}}$, ${\mathbf{W}_{\mathbf{u}}{(\mathbf{s})}} \in {\mathbb{C}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{u}}}$ are weighting transfer matrices with minimal state-space realizations $(\mathbf{A}_{\mathbf{e}},\mathbf{B}_{\mathbf{e}},\mathbf{C}_{\mathbf{e}},\mathbf{D}_{\mathbf{e}})$ and $(\mathbf{A}_{\mathbf{u}},\mathbf{B}_{\mathbf{u}},\mathbf{C}_{\mathbf{u}},\mathbf{D}_{\mathbf{u}})$, respectively. The generalized plant can be formulated with minimal state-space representation where ${\mathbf{x}^{\mathsf{T}}{(\mathbf{t})}} = \begin{bmatrix} {\mathbf{x}_{\mathbf{p}}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{x}_{\mathbf{r}}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{x}_{\mathbf{d}}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{x}_{\mathbf{n}}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{x}_{\mathbf{e}}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{x}_{\mathbf{u}}^{\mathsf{T}}{(\mathbf{t})}} \end{bmatrix}$, ${\mathbf{w}^{\mathsf{T}}{(\mathbf{t})}} = \begin{bmatrix} {\mathbf{r}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{d}^{\mathsf{T}}{(\mathbf{t})}} & {\mathbf{n}^{\mathsf{T}}{(\mathbf{t})}} \end{bmatrix}$, ${\mathbf{u}{(\mathbf{t})}} = {\mathbf{u}_{\mathbf{c}}{(\mathbf{t})}}$, ${\mathbf{y}{(\mathbf{s})}} = {{\mathbf{W}_{\mathbf{r}}{(\mathbf{s})}\mathbf{r}{(\mathbf{s})}} - {\mathbf{y}_{\mathbf{p}}{(\mathbf{s})}} - {\mathbf{W}_{\mathbf{n}}{(\mathbf{s})}\mathbf{n}{(\mathbf{s})}}}$, and $\mathbf{x}_{\mathbf{r}}{(\mathbf{t})}$, $\mathbf{x}_{\mathbf{d}}{(\mathbf{t})}$, $\mathbf{x}_{\mathbf{n}}{(\mathbf{t})}$, $\mathbf{x}_{\mathbf{e}}{(\mathbf{t})}$, and $\mathbf{x}_{\mathbf{u}}{(\mathbf{t})}$ are the states associated with the state-space realizations of the weighting transfer matrices $\mathbf{W}_{\mathbf{r}}{(\mathbf{s})}$, $\mathbf{W}_{\mathbf{d}}{(\mathbf{s})}$, $\mathbf{W}_{\mathbf{n}}{(\mathbf{s})}$, $\mathbf{W}_{\mathbf{e}}{(\mathbf{s})}$, and $\mathbf{W}_{\mathbf{u}}{(\mathbf{s})}$, respectively.

### The Discrete-Time Generalized Plant

The discrete-time generalized LTI plant ${\mathcal{P}}:{\ell_{2e}\rightarrow\ell_{2e}}$, shown in Figure 1, is described by the state-space realization where $\mathbf{x}_{\mathbf{k}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}}}$ is the system state at time step $k$, $\mathbf{z}_{\mathbf{k}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}}}$ is the performance signal at time step $k$, $\mathbf{y}_{\mathbf{k}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{y}}}$ is the measurement signal at time step $k$, $\mathbf{w}_{\mathbf{k}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{w}}}$ is the exogenous signal at time step $k$, $\mathbf{u}_{\mathbf{k}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}}}$ is the control input signal at time step $k$, and the state-space matrices have appropriate dimensions. The generalized LTI plant can also be written in discrete-time transfer matrix form as where the transfer matrix ${\mathbf{P}{(\mathbf{z})}} \in {\mathbb{C}}^{{({\mathbf{n}_{\mathbf{z}} + \mathbf{n}_{\mathbf{y}}})} \times {({\mathbf{n}_{\mathbf{w}} + \mathbf{n}_{\mathbf{u}}})}}$ is partitioned as

### $\mathcal{H}_{2}$-Optimal Control

The goal of $\mathcal{H}_{2}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

### $\mathcal{H}_{2}$-Optimal Full-State Feedback Control \[5, pp. 257--258\]

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{B}_{\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}$ to the performance output $\mathbf{z}$. Substituting the full-state feedback controller into (4.1) and (4.2) yields and a closed-loop transfer matrix Minimizing the $\mathcal{H}_{2}$ norm of the transfer matrix $\mathbf{T}{(\mathbf{s})}$ is equivalent to minimizing ${\mathcal{J}{(\mu)}} = \mu^{2}$ subject to where $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{w}}}$, $\mu \in {\mathbb{R}}_{> 0}$, $\mathbf{P} > \mathbf{0}$, and $\mathbf{Z} > \mathbf{0}$. A change of variables is performed with $\mathbf{F} = {\mathbf{K}\mathbf{P}}$ and $\nu = \mu^{2}$, which transforms (4.3) and (4.5) into LMIs in the variables $\mathbf{P}$, $\mathbf{F}$, $\mathbf{Z}$, and $\nu$ given by

### Synthesis Method 4.1

The $\mathcal{H}_{2}$-optimal full-state feedback controller is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{w}}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, (4.4), (4.6), and (4.7). The $\mathcal{H}_{2}$-optimal full-state feedback gain is recovered by $\mathbf{K} = {\mathbf{F}\mathbf{P}}^{- \mathbf{1}}$ and the $\mathcal{H}_{2}$ norm of $\mathbf{T}{(\mathbf{s})}$ is $\mu = \sqrt{\nu}$.

### Discrete-Time $\mathcal{H}_{2}$-Optimal Full-State Feedback Control

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{B}_{d\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u}_{\mathbf{k}} = {\mathbf{K}_{d}\mathbf{x}_{\mathbf{k}}}$) is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}_{\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{k}}$, given by

### Synthesis Method 4.2

The discrete-time $\mathcal{H}_{2}$-optimal full-state feedback controller is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, $\mathbf{F}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The $\mathcal{H}_{2}$-optimal full-state feedback gain is recovered by $\mathbf{K}_{d} = {\mathbf{F}_{d}\mathbf{P}^{- \mathbf{1}}}$ and the $\mathcal{H}_{2}$ norm of $\mathbf{T}{(\mathbf{z})}$ is $\mu = \sqrt{\nu}$.

### $\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by and $\overset{\sim}{\mathbf{D}} = {\mathbf{1} - {\mathbf{D}_{\mathbf{2}\mathbf{2}}\mathbf{D}_{\mathbf{c}}}}$.

### Synthesis Method 4.3

Solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. If $\mathbf{D}_{\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{\mathbf{c}} = \mathbf{A}_{_{\mathbf{K}}}$, $\mathbf{B}_{\mathbf{c}} = \mathbf{B}_{_{\mathbf{K}}}$, $\mathbf{C}_{\mathbf{c}} = \mathbf{C}_{_{\mathbf{K}}}$, and $\mathbf{D}_{\mathbf{c}} = \mathbf{D}_{_{\mathbf{K}}}$.

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

If $\mathbf{D}_{\mathbf{1}\mathbf{1}} = \mathbf{0}$, $\mathbf{D}_{\mathbf{1}\mathbf{2}} \neq \mathbf{0}$, and $\mathbf{D}_{\mathbf{2}\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{\mathbf{n}} = \mathbf{0}$ in order to satisfy the equality constraint of (4.8).

### Discrete-Time $\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization A discrete-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{d\mathbf{c}},\mathbf{B}_{d\mathbf{c}},\mathbf{C}_{d\mathbf{c}},\mathbf{D}_{d\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop system transfer matrix from $\mathbf{w}_{\mathbf{k}}$ to $\mathbf{z}_{\mathbf{k}}$, given by and ${\overset{\sim}{\mathbf{D}}}_{d} = {\mathbf{1} - {\mathbf{D}_{d\mathbf{2}\mathbf{2}}\mathbf{D}_{d\mathbf{c}}}}$.

### Synthesis Method 4.4

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{G}$, $\mathbf{H}$, $\mathbf{J}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{H}\mathbf{G}}}$. If $\mathbf{D}_{d\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{d\mathbf{c}} = \mathbf{A}_{d_{\mathbf{K}}}$, $\mathbf{B}_{d\mathbf{c}} = \mathbf{B}_{d_{\mathbf{K}}}$, $\mathbf{C}_{d\mathbf{c}} = \mathbf{C}_{d_{\mathbf{K}}}$, and $\mathbf{D}_{d\mathbf{c}} = \mathbf{D}_{d_{\mathbf{K}}}$.

Given $\mathbf{G}$ and $\mathbf{H}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

If $\mathbf{D}_{d\mathbf{1}\mathbf{1}} = \mathbf{0}$, $\mathbf{D}_{d\mathbf{1}\mathbf{2}} \neq \mathbf{0}$, and $\mathbf{D}_{d\mathbf{2}\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{d\mathbf{n}} = \mathbf{0}$ in order to satisfy the equality constraint of (4.11).

The LMI in (4.9) is derived from the LMI in Theorem 7 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix Similarly, the LMI in (4.10) is derived from the LMI in Theorem 7 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix

### Synthesis Method 4.5

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. If $\mathbf{D}_{d\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{d\mathbf{c}} = \mathbf{A}_{d_{\mathbf{K}}}$, $\mathbf{B}_{d\mathbf{c}} = \mathbf{B}_{d_{\mathbf{K}}}$, $\mathbf{C}_{d\mathbf{c}} = \mathbf{C}_{d_{\mathbf{K}}}$, and $\mathbf{D}_{d\mathbf{c}} = \mathbf{D}_{d_{\mathbf{K}}}$.

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

If $\mathbf{D}_{d\mathbf{1}\mathbf{1}} = \mathbf{0}$, $\mathbf{D}_{d\mathbf{1}\mathbf{2}} \neq \mathbf{0}$, and $\mathbf{D}_{d\mathbf{2}\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{d\mathbf{n}} = \mathbf{0}$ in order to satisfy the equality constraint of (4.13).

The LMIs in (4.12) and (4.13) are derived from (4.9) and (4.10) using the change of variables $\mathbf{S} = \mathbf{J} = \mathbf{1}$, $\mathbf{H} = \mathbf{X}_{\mathbf{1}}$, $\mathbf{G} = \mathbf{Y}_{\mathbf{1}}$. The LMI in (4.14) is added to ensure that ${\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}} \geq \mathbf{0}$ in a similar fashion to the approach used .

### $\mathcal{H}_{\infty}$-Optimal Control

The goal of $\mathcal{H}_{\infty}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

### $\mathcal{H}_{\infty}$-Optimal Full-State Feedback Control \[5, pp. 251--252\]

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{B}_{\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize $\mathcal{H}_{\infty}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}$ to the performance output $\mathbf{z}$. Substituting the full-state feedback controller into (4.15) and (4.16) yields and a closed-loop transfer matrix From the Bounded Real Lemma in Section 3.2.1, the $\mathcal{H}_{\infty}$ of the closed-loop system is the minimum value of $\gamma \in {\mathbb{R}}_{> 0}$ that satisfies where $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$ and $\mathbf{P} > \mathbf{0}$. A congruence transformation is performed on (4.17) with $\mathbf{W} = {\text{diag}{\{\mathbf{P}^{- \mathbf{1}},\mathbf{1},\mathbf{1}\}}}$ and a change of variables is made with $\mathbf{Q} = \mathbf{P}^{- \mathbf{1}}$ and $\mathbf{F} = {\mathbf{K}\mathbf{Q}}$. This yields an LMI in the design variables $\mathbf{Q}$, $\mathbf{F}$, and $\gamma$, given by

### Synthesis Method 4.6

The $\mathcal{H}_{\infty}$-optimal full-state feedback controller is synthesized by solving for $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$ and $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{Q} > \mathbf{0}$ and (4.18). The $\mathcal{H}_{\infty}$-optimal full-state feedback controller gain is recovered by $\mathbf{K} = {\mathbf{F}\mathbf{Q}}^{- \mathbf{1}}$ and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}{(\mathbf{s})}$ is $\gamma$.

### Discrete-Time $\mathcal{H}_{\infty}$-Optimal Full-State Feedback Control

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{B}_{d\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u}_{\mathbf{k}} = {\mathbf{K}_{d}\mathbf{x}_{\mathbf{k}}}$) is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}_{\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{k}}$, given by

### Synthesis Method 4.7

The discrete-time $\mathcal{H}_{\infty}$-optimal full-state feedback controller is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{F}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{P} > \mathbf{0}$, The $\mathcal{H}_{\infty}$-optimal full-state feedback gain is recovered by $\mathbf{K}_{d} = {\mathbf{F}_{d}\mathbf{P}^{- \mathbf{1}}}$ and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}{(\mathbf{z})}$ is $\gamma$.

### $\mathcal{H}_{\infty}$-Optimal Dynamic Output Feedback Control

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by and $\overset{\sim}{\mathbf{D}} = {\mathbf{1} - {\mathbf{D}_{\mathbf{2}\mathbf{2}}\mathbf{D}_{\mathbf{c}}}}$.

Two different synthesis methods for the $\mathcal{H}_{\infty}$-optimal dynamic output feedback control problem are presented as follows.

### Synthesis Method 4.8

Solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, where $\mathbf{N}_{\mathbf{1}\mathbf{1}} = {{\mathbf{A}\mathbf{Y}}_{\mathbf{1}} + {\mathbf{Y}_{\mathbf{1}}\mathbf{A}^{\mathsf{T}}} + {\mathbf{B}_{\mathbf{2}}\mathbf{C}_{\mathbf{n}}} + {\mathbf{C}_{\mathbf{n}}^{\mathsf{T}}\mathbf{B}_{\mathbf{2}}^{\mathsf{T}}}}$. The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. If $\mathbf{D}_{\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{\mathbf{c}} = \mathbf{A}_{_{\mathbf{K}}}$, $\mathbf{B}_{\mathbf{c}} = \mathbf{B}_{_{\mathbf{K}}}$, $\mathbf{C}_{\mathbf{c}} = \mathbf{C}_{_{\mathbf{K}}}$, and $\mathbf{D}_{\mathbf{c}} = \mathbf{D}_{_{\mathbf{K}}}$.

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

### Synthesis Method 4.9

,\[2, pp. 224--232\] The controller is solved for in the following two steps.

Solve for $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{Q} > \mathbf{0}$, that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to where ${\mathcal{R}\left(\mathbf{N}_{\mathbf{o}} \right)} = {\mathcal{N}\left(\begin{bmatrix} \mathbf{C}_{\mathbf{2}} & \mathbf{D}_{\mathbf{2}\mathbf{1}} \end{bmatrix} \right)}$ and ${\mathcal{R}\left(\mathbf{N}_{\mathbf{c}} \right)} = {\mathcal{N}\left(\begin{bmatrix} \mathbf{B}_{\mathbf{2}}^{\mathsf{T}} & \mathbf{D}_{\mathbf{1}\mathbf{2}}^{\mathsf{T}} \end{bmatrix} \right)}$. Define $\mathbf{P}_{_{CL}} = \begin{bmatrix} \mathbf{P} & \mathbf{P}_{\mathbf{2}}^{\mathsf{T}} \\\end{bmatrix}$, where ${\mathbf{P}_{\mathbf{2}}\mathbf{P}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{P} - \mathbf{Q}^{- \mathbf{1}}}$.

Fix $\mathbf{P}_{_{CL}}$ and solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to | | $\overline{\mathbf{A}}$ | ${= \begin{bmatrix} | $\overline{\mathbf{B}}$ | ${= \begin{bmatrix} | | | | | \mathbf{A} & \mathbf{0} \\ | | {\mathbf{B}_{\mathbf{1}} - {\mathbf{B}_{\mathbf{2}}{\overline{\mathbf{D}}}_{\mathbf{c}}\mathbf{D}_{\mathbf{2}\mathbf{1}}}} \\ | | | | | \mathbf{0} & \mathbf{0} | | \mathbf{0} | | | | | \end{bmatrix}},$ | | \end{bmatrix}},$ | | | | $\overline{\mathbf{C}}$ | ${= \begin{bmatrix} | $\underset{¯}{\mathbf{C}}$ | ${= \begin{bmatrix} | | | | | \mathbf{C}_{\mathbf{1}} & \mathbf{0} | | \mathbf{0} & \mathbf{1} \\ | | | | | \end{bmatrix}},$ | | \mathbf{C}_{\mathbf{2}} & \mathbf{0} | | | | $\underset{¯}{\mathbf{B}}$ | ${= \begin{bmatrix} | ${\underset{¯}{\mathbf{D}}}_{12}$ | ${= \begin{bmatrix} | | | | | \mathbf{0} & {- \mathbf{B}_{\mathbf{2}}} \\ | | \mathbf{0} & {- \mathbf{D}_{\mathbf{1}\mathbf{2}}} | | | | | \mathbf{1} & \mathbf{0} | | \end{bmatrix}},$ | | | | ${\underset{¯}{\mathbf{D}}}_{21}$ | ${= \begin{bmatrix} | | | | | \mathbf{D}_{\mathbf{2}\mathbf{1}} | | The controller is recovered by If $\mathbf{D}_{\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{\mathbf{c}} = \mathbf{A}_{\mathbf{n}}$, $\mathbf{B}_{\mathbf{c}} = \mathbf{B}_{\mathbf{n}}$, $\mathbf{C}_{\mathbf{c}} = \mathbf{C}_{\mathbf{n}}$, and $\mathbf{D}_{\mathbf{c}} = \mathbf{D}_{\mathbf{n}}$.

Note that the purpose of the matrix inequality $\begin{bmatrix} \end{bmatrix} \geq 0$ in (4.19) is to ensure that there exists $\mathbf{P}_{_{CL}} = \begin{bmatrix} \mathbf{P} & \mathbf{P}_{\mathbf{2}}^{\mathsf{T}} \\\end{bmatrix} > \mathbf{0}$ and $\mathbf{P}_{_{CL}}^{- \mathbf{1}} = \begin{bmatrix} \mathbf{Q} & {- {\mathbf{Q}\mathbf{P}}_{\mathbf{2}}} \\\ast & {{\mathbf{P}_{\mathbf{2}}^{\mathsf{T}}{\mathbf{Q}\mathbf{P}}_{\mathbf{2}}} + \mathbf{1}} \end{bmatrix}$. This follows from Property 9 in Section 2.3.3.

### Discrete-Time $\mathcal{H}_{\infty}$-Optimal Dynamic Output Feedback Control

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A discrete-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{d\mathbf{c}},\mathbf{B}_{d\mathbf{c}},\mathbf{C}_{d\mathbf{c}},\mathbf{D}_{d\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by and ${\overset{\sim}{\mathbf{D}}}_{d} = {\mathbf{1} - {\mathbf{D}_{d\mathbf{2}\mathbf{2}}\mathbf{D}_{d\mathbf{c}}}}$.

### Synthesis Method 4.10

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{G}$, $\mathbf{H}$, $\mathbf{J}$, $\mathbf{S} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{H}\mathbf{G}}}$. If $\mathbf{D}_{d\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{d\mathbf{c}} = \mathbf{A}_{d_{\mathbf{K}}}$, $\mathbf{B}_{d\mathbf{c}} = \mathbf{B}_{d_{\mathbf{K}}}$, $\mathbf{C}_{d\mathbf{c}} = \mathbf{C}_{d_{\mathbf{K}}}$, and $\mathbf{D}_{d\mathbf{c}} = \mathbf{D}_{d_{\mathbf{K}}}$.

Given $\mathbf{G}$ and $\mathbf{H}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

The LMI in (4.20) is derived from the LMI in Theorem 8 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix followed by the change of variables $\gamma = \mu^{2}$, $\mathbf{X}_{\mathbf{1}} = {\gamma\mathbf{H}}$, $\mathbf{Y}_{\mathbf{1}} = {\gamma^{- \mathbf{1}}\mathbf{P}}$.

### Synthesis Method 4.11

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. If $\mathbf{D}_{d\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{d\mathbf{c}} = \mathbf{A}_{d_{\mathbf{K}}}$, $\mathbf{B}_{d\mathbf{c}} = \mathbf{B}_{d_{\mathbf{K}}}$, $\mathbf{C}_{d\mathbf{c}} = \mathbf{C}_{d_{\mathbf{K}}}$, and $\mathbf{D}_{d\mathbf{c}} = \mathbf{D}_{d_{\mathbf{K}}}$.

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

The LMI in (4.21) is derived from (4.20) using the change of variables $\mathbf{S} = \mathbf{J} = \mathbf{1}$, $\mathbf{H} = \mathbf{X}_{\mathbf{1}}$, $\mathbf{G} = \mathbf{Y}_{\mathbf{1}}$. The LMI in (4.22) is added to ensure that ${\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}} \geq \mathbf{0}$ in a similar fashion to the approach used .

### Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Control

The goal of mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{1}}$ to $\mathbf{z}_{\mathbf{1}}$, while ensuring that the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer function from $\mathbf{w}_{\mathbf{2}}$ to $\mathbf{z}_{\mathbf{2}}$ is below a specified bound.

### Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Full-State Feedback Control \[5, pp. 329--330\]

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that $(\mathbf{A},\mathbf{B}_{\mathbf{2}})$ is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{1}}$ to the performance output $\mathbf{z}_{\mathbf{1}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{2}}$ to the performance output $\mathbf{z}_{\mathbf{2}}$ is less than $\gamma_{d}$, where

### Synthesis Method 4.12

The mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal full-state feedback controller is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{w}}}$, $\mathbf{F} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The $\mathcal{H}_{2}$-optimal full-state feedback gain is recovered by $\mathbf{K} = {\mathbf{F}\mathbf{P}}^{- \mathbf{1}}$, the $\mathcal{H}_{2}$ norm of $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{s})}$ is less than $\mu = \sqrt{\nu}$, and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{s})}$ is less than $\gamma_{d}$.

### Discrete-Time Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Full-State Feedback Control

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{B}_{d\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u}_{\mathbf{k}} = {\mathbf{K}_{d}\mathbf{x}_{\mathbf{k}}}$) is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{1},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{1},\mathbf{k}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{2},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{2},\mathbf{k}}$ is less than $\gamma_{d}$, where

### Synthesis Method 4.13

The discrete-time mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal full-state feedback controller is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{w}}}$, $\mathbf{F}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The $\mathcal{H}_{2}$-optimal full-state feedback gain is recovered by $\mathbf{K}_{d} = {\mathbf{F}_{d}\mathbf{P}^{- \mathbf{1}}}$, the $\mathcal{H}_{2}$ norm of $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{z})}$ is less than $\mu = \sqrt{\nu}$, and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{z})}$ is less than $\gamma_{d}$.

### Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Dynamic Output Feedback Control

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{1}}$ to the performance output $\mathbf{z}_{\mathbf{1}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{2}}$ to the performance output $\mathbf{z}_{\mathbf{2}}$ is less than $\gamma_{d}$, where and $\overset{\sim}{\mathbf{D}} = {\mathbf{1} - {\mathbf{D}_{\mathbf{2}\mathbf{2}}\mathbf{D}_{\mathbf{c}}}}$.

### Synthesis Method 4.14

Solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}_{\mathbf{1}}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, where $\mathbf{N}_{\mathbf{1}\mathbf{1}} = {{\mathbf{A}\mathbf{Y}}_{\mathbf{1}} + {\mathbf{Y}_{\mathbf{1}}\mathbf{A}^{\mathsf{T}}} + {\mathbf{B}_{\mathbf{2}}\mathbf{C}_{\mathbf{n}}} + {\mathbf{C}_{\mathbf{n}}^{\mathsf{T}}\mathbf{B}_{\mathbf{2}}^{\mathsf{T}}}}$. The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. If $\mathbf{D}_{\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{\mathbf{c}} = \mathbf{A}_{_{\mathbf{K}}}$, $\mathbf{B}_{\mathbf{c}} = \mathbf{B}_{_{\mathbf{K}}}$, $\mathbf{C}_{\mathbf{c}} = \mathbf{C}_{_{\mathbf{K}}}$, and $\mathbf{D}_{\mathbf{c}} = \mathbf{D}_{_{\mathbf{K}}}$.

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

If $\mathbf{D}_{\mathbf{1}\mathbf{1},\mathbf{1}\mathbf{1}} = \mathbf{0}$, $\mathbf{D}_{\mathbf{1}\mathbf{2},\mathbf{1}} \neq \mathbf{0}$, and $\mathbf{D}_{\mathbf{2}\mathbf{1},\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{\mathbf{n}} = \mathbf{0}$ in order to satisfy the equality constraint of (4.23).

### Discrete-Time Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Dynamic Output Feedback Control

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A discrete-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{d\mathbf{c}},\mathbf{B}_{d\mathbf{c}},\mathbf{C}_{d\mathbf{c}},\mathbf{D}_{d\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{1},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{1},\mathbf{k}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{2},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{2},\mathbf{k}}$ is less than $\gamma_{d}$, where and ${\overset{\sim}{\mathbf{D}}}_{d} = {\mathbf{1} - {\mathbf{D}_{d\mathbf{2}\mathbf{2}}\mathbf{D}_{d\mathbf{c}}}}$.

### Synthesis Method 4.15

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}_{\mathbf{1}}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The controller is recovered by and the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. If $\mathbf{D}_{d\mathbf{2}\mathbf{2}} = \mathbf{0}$, then $\mathbf{A}_{d\mathbf{c}} = \mathbf{A}_{d_{\mathbf{K}}}$, $\mathbf{B}_{d\mathbf{c}} = \mathbf{B}_{d_{\mathbf{K}}}$, $\mathbf{C}_{d\mathbf{c}} = \mathbf{C}_{d_{\mathbf{K}}}$, and $\mathbf{D}_{d\mathbf{c}} = \mathbf{D}_{d_{\mathbf{K}}}$.

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

If $\mathbf{D}_{{d\mathbf{1}\mathbf{1}},\mathbf{1}\mathbf{1}} = \mathbf{0}$, $\mathbf{D}_{{d\mathbf{1}\mathbf{2}},\mathbf{1}} \neq \mathbf{0}$, and $\mathbf{D}_{{d\mathbf{2}\mathbf{1}},\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{d\mathbf{n}} = \mathbf{0}$ in order to satisfy the equality constraint of (4.24).

## LMIs in Optimal Estimation and Filtering

This section presents controller synthesis methods using LMIs for a number of well-known optimal state-estimation and filtering problems. The derivation of the LMIs used for synthesis is provided in some cases, while longer derivations can be found in the cited references.

### $\mathcal{H}_{2}$-Optimal State Estimation

The goal of $\mathcal{H}_{2}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

### $\mathcal{H}_{2}$-Optimal Observer \[5, p. 296\]

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e} = {\mathbf{x} - \hat{\mathbf{x}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}$ is to be designed such that the $\mathcal{H}_{2}$ norm of the transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by is minimized. Minimizing the $\mathcal{H}_{2}$ norm of the transfer matrix $\mathbf{T}{(\mathbf{s})}$ is equivalent to minimizing ${\mathcal{J}{(\mu)}} = \mu^{2}$ subject to where $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, $\mu \in {\mathbb{R}}_{> 0}$, $\mathbf{P} > \mathbf{0}$, and $\mathbf{Z} > \mathbf{0}$. A change of variables is performed with $\mathbf{G} = {\mathbf{P}\mathbf{L}}$ and $\nu = \mu^{2}$, which transforms (5.1) and (5.3) into LMIs in the variables $\mathbf{P}$, $\mathbf{G}$, $\mathbf{Z}$, and $\nu$ given by

### Synthesis Method 5.1

The $\mathcal{H}_{2}$-optimal observer gain is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, (5.2), (5.4), and (5.5). The $\mathcal{H}_{2}$-optimal observer gain is recovered by $\mathbf{L} = {\mathbf{P}^{- \mathbf{1}}\mathbf{G}}$ and the $\mathcal{H}_{2}$ norm of $\mathbf{T}{(\mathbf{s})}$ is $\mu = \sqrt{\nu}$.

### Discrete-Time $\mathcal{H}_{2}$-Optimal Observer

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e}_{\mathbf{k}} = {\mathbf{x}_{\mathbf{k}} - {\hat{\mathbf{x}}}_{\mathbf{k}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}_{d}$ is to be designed such that the $\mathcal{H}_{2}$ of the transfer matrix from $\mathbf{w}_{\mathbf{k}}$ to $\mathbf{z}_{\mathbf{k}}$, given by

### Synthesis Method 5.2

The discrete-time $\mathcal{H}_{2}$-optimal observer gain is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, $\mathbf{G}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The $\mathcal{H}_{2}$-optimal observer gain is recovered by $\mathbf{L}_{d} = {\mathbf{P}^{- \mathbf{1}}\mathbf{G}_{d}}$ and the $\mathcal{H}_{2}$ norm of $\mathbf{T}{(\mathbf{z})}$ is $\mu = \sqrt{\nu}$.

### $\mathcal{H}_{\infty}$-Optimal State Estimation

The goal of $\mathcal{H}_{\infty}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

### $\mathcal{H}_{\infty}$--Optimal Observer \[5, p. 295\]

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e} = {\mathbf{x} - \hat{\mathbf{x}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}$ is to be designed such that the $\mathcal{H}_{\infty}$ of the transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

### Synthesis Method 5.3

The $\mathcal{H}_{\infty}$-optimal observer gain is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{P} > \mathbf{0}$ and The $\mathcal{H}_{\infty}$-optimal observer gain is recovered by $\mathbf{L} = {\mathbf{P}^{- \mathbf{1}}\mathbf{G}}$ and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}{(\mathbf{s})}$ is $\gamma$.

### Discrete-Time $\mathcal{H}_{\infty}$--Optimal Observer

Consider the discrete-time LTI plant $\mathcal{G}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e}_{\mathbf{k}} = {\mathbf{x}_{\mathbf{k}} - {\hat{\mathbf{x}}}_{\mathbf{k}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}_{d}$ is to be designed such that the $\mathcal{H}_{\infty}$ of the transfer matrix from $\mathbf{w}_{\mathbf{k}}$ to $\mathbf{z}_{\mathbf{k}}$, given by

### Synthesis Method 5.4

The $\mathcal{H}_{\infty}$-optimal observer gain is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{G}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{P} > \mathbf{0}$ and The $\mathcal{H}_{\infty}$-optimal observer gain is recovered by $\mathbf{L}_{d} = {\mathbf{P}^{- \mathbf{1}}\mathbf{G}_{d}}$ and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}{(\mathbf{z})}$ is $\gamma$.

### Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal State Estimation

The goal of mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{1}}$ to $\mathbf{z}_{\mathbf{1}}$, while ensuring that the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{2}}$ to $\mathbf{z}_{\mathbf{2}}$ is below a specified bound.

### Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Observer

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e} = {\mathbf{x} - \hat{\mathbf{x}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{1}}$ to the performance output $\mathbf{z}_{\mathbf{1}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{2}}$ to the performance output $\mathbf{z}_{\mathbf{2}}$ is less than $\gamma_{d}$, where

### Synthesis Method 5.5

The mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal observer gain is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The mixed-$\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal observer gain is recovered by $\mathbf{L} = {\mathbf{P}^{- \mathbf{1}}\mathbf{G}}$, the $\mathcal{H}_{2}$ norm of $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{s})}$ is less than $\mu = \sqrt{\nu}$, and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{s})}$ is less than $\gamma_{d}$.

### Discrete-Time Mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-Optimal Observer

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e}_{\mathbf{k}} = {\mathbf{x}_{\mathbf{k}} - {\hat{\mathbf{x}}}_{\mathbf{k}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}_{d}$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{1},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{1},\mathbf{k}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{2},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{2},\mathbf{k}}$ is less than $\gamma_{d}$, where

### Synthesis Method 5.6

The discrete-time mixed-$\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal observer gain is synthesized by solving for $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, $\mathbf{G}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{P} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The mixed-$\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal observer gain is recovered by $\mathbf{L}_{d} = {\mathbf{P}^{- \mathbf{1}}\mathbf{G}_{d}}$, the $\mathcal{H}_{2}$ norm of $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{z})}$ is less than $\mu = \sqrt{\nu}$, and the $\mathcal{H}_{\infty}$ norm of $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{z})}$ is less than $\gamma_{d}$.

### Continuous-Time and Discrete-Time Optimal Filtering

The goal of optimal filtering is to design a filter that acts on the output $\mathbf{z}$ of the generalized plant and optimizes the transfer matrix from $\mathbf{w}$ to the filtered output.

Continuous-Time Filtering: Consider the continuous-time generalized LTI plant with minimal states-space realization where it is assumed that $\mathbf{A}$ is Hurwitz. A continuous-time dynamic LTI filter with state-space realization is to be designed to optimize the transfer function from $\mathbf{w}$ to $\overset{\sim}{\mathbf{z}} = {\mathbf{z} - \hat{\mathbf{z}}}$, given by This can alternatively be formulated as a special case of synthesizing a dynamic output "feedback" controller for the generalized plant given by The controller in this case is not truly a feedback controller, as it only appears as a feedthrough term in the performance channel. The synthesis methods presented in this subsection take advantage of this fact, resulting in a simpler formulation than applying the controller synthesis methods in Section 4.

Discrete-Time Filtering: Consider the discrete-time generalized LTI plant with minimal states-space realization where it is assumed that $\mathbf{A}_{d}$ is Schur. A discrete-time dynamic LTI filter with state-space realization is to be designed to optimize the transfer function from $\mathbf{w}_{\mathbf{k}}$ to ${\overset{\sim}{\mathbf{z}}}_{k} = {\mathbf{z}_{\mathbf{k}} - {\hat{\mathbf{z}}}_{\mathbf{k}}}$, given by This can alternatively be formulated as a special case of synthesizing a dynamic output "feedback" controller for the generalized plant given by

### $\mathcal{H}_{2}$-Optimal Filter

An $\mathcal{H}_{2}$-optimal filter is designed to minimize the $\mathcal{H}_{2}$ norm of $\overset{\sim}{\mathbf{P}}{(s)}$ in (5.6).

### Synthesis Method 5.7

\[5, pp. 309--310\] Solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X} > \mathbf{0}$, $\mathbf{Y} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The filter is recovered by the state-space matrices $\mathbf{A}_{\mathbf{f}} = {\mathbf{X}^{- \mathbf{1}}\mathbf{A}_{\mathbf{n}}}$, $\mathbf{B}_{\mathbf{f}} = {\mathbf{X}^{- \mathbf{1}}\mathbf{B}_{\mathbf{n}}}$, $\mathbf{C}_{\mathbf{f}}$, and $\mathbf{D}_{\mathbf{f}}$.

If $\mathbf{D}_{\mathbf{1}\mathbf{1}} = \mathbf{0}$ and $\mathbf{D}_{\mathbf{2}\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{\mathbf{f}} = \mathbf{0}$ in order to satisfy the equality constraint of (5.8).

### Synthesis Method 5.8

\[5, pp. 309--310\] Solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X} > \mathbf{0}$, $\mathbf{Y} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The filter is recovered by the state-space matrices $\mathbf{A}_{\mathbf{f}} = {\mathbf{X}^{- \mathbf{1}}\mathbf{A}_{\mathbf{n}}}$, $\mathbf{B}_{\mathbf{f}} = {\mathbf{X}^{- \mathbf{1}}\mathbf{B}_{\mathbf{n}}}$, $\mathbf{C}_{\mathbf{f}}$, and $\mathbf{D}_{\mathbf{f}}$.

If $\mathbf{D}_{\mathbf{1}\mathbf{1}} = \mathbf{0}$ and $\mathbf{D}_{\mathbf{2}\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{\mathbf{f}} = \mathbf{0}$ in order to satisfy the equality constraint of (5.9).

### Discrete-Time $\mathcal{H}_{2}$-Optimal Filter

### Synthesis Method 5.9

Consider the case where $\mathbf{D}_{d\mathbf{1}\mathbf{1}} = \mathbf{0}$ and $\mathbf{D}_{\mathbf{f}} = \mathbf{0}$. Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X} > \mathbf{0}$, $\mathbf{Y} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The filter is recovered by $\mathbf{A}_{\mathbf{f}} = {- {\mathbf{Y}^{- \mathbf{1}}\mathbf{A}_{d\mathbf{n}}\left({\mathbf{1} - {\mathbf{Y}^{- \mathbf{1}}\mathbf{X}}} \right)^{- \mathbf{1}}}}$, $\mathbf{B}_{\mathbf{f}} = {- {\mathbf{Y}^{- \mathbf{1}}\mathbf{B}_{d\mathbf{n}}}}$, and $\mathbf{C}_{\mathbf{f}} = {\mathbf{C}_{d\mathbf{n}}\left({\mathbf{1} - {\mathbf{Y}^{- \mathbf{1}}\mathbf{X}}} \right)^{- \mathbf{1}}}$.

### Synthesis Method 5.10

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{z}}}$, and $\nu \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\nu)}} = \nu$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Z} > \mathbf{0}$, The filter state-space matrices are recovered by $\mathbf{A}_{\mathbf{f}} = {\mathbf{X}_{\mathbf{2}}^{- \mathbf{1}}\left({\mathbf{A}_{d\mathbf{n}} - {\mathbf{X}_{\mathbf{1}}\mathbf{A}_{d}\mathbf{Y}_{\mathbf{1}}}} \right)\mathbf{Y}_{\mathbf{2}}^{- \mathsf{T}}}$, $\mathbf{B}_{\mathbf{f}} = {\mathbf{X}_{\mathbf{2}}^{- \mathbf{1}}\mathbf{B}_{d\mathbf{n}}}$, $\mathbf{C}_{\mathbf{f}} = {\mathbf{C}_{d\mathbf{n}}\mathbf{Y}_{\mathbf{2}}^{- \mathsf{T}}}$, and $\mathbf{D}_{\mathbf{f}}$, where the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

If $\mathbf{D}_{d\mathbf{1}\mathbf{1}} = \mathbf{0}$ and $\mathbf{D}_{d\mathbf{2}\mathbf{1}} \neq \mathbf{0}$, then it is often simplest to choose $\mathbf{D}_{\mathbf{f}} = \mathbf{0}$ in order to satisfy the equality constraint of (5.10).

This synthesis method is derived from the discrete-time $\mathcal{H}_{2}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.5 using the fact that $\mathcal{H}_{2}$-optimal filter synthesis is a special case of this problem.

### $\mathcal{H}_{\infty}$-Optimal Filter

An $\mathcal{H}_{\infty}$-optimal filter is designed to minimize the $\mathcal{H}_{\infty}$ norm of $\overset{\sim}{\mathbf{P}}{(s)}$ in (5.6).

### Synthesis Method 5.11

\[5, pp. 303--304\] Solve for $\mathbf{A}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{\mathbf{f}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{z}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X} > \mathbf{0}$, $\mathbf{Y} > \mathbf{0}$, The filter is recovered by $\mathbf{A}_{\mathbf{f}} = {\mathbf{X}^{- \mathbf{1}}\mathbf{A}_{\mathbf{n}}}$ and $\mathbf{B}_{\mathbf{f}} = {\mathbf{X}^{- \mathbf{1}}\mathbf{B}_{\mathbf{n}}}$.

### Discrete-Time $\mathcal{H}_{\infty}$-Optimal Filter

### Synthesis Method 5.12

Consider the case where $\mathbf{D}_{d\mathbf{1}\mathbf{1}} = \mathbf{0}$ and $\mathbf{D}_{\mathbf{f}} = \mathbf{0}$. Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X} > \mathbf{0}$, $\mathbf{Y} > \mathbf{0}$, The filter is recovered by $\mathbf{A}_{\mathbf{f}} = {- {\mathbf{Y}^{- \mathbf{1}}\mathbf{A}_{d\mathbf{n}}\left({\mathbf{1} - {\mathbf{Y}^{- \mathbf{1}}\mathbf{X}}} \right)^{- \mathbf{1}}}}$, $\mathbf{B}_{\mathbf{f}} = {- {\mathbf{Y}^{- \mathbf{1}}\mathbf{B}_{d\mathbf{n}}}}$, and $\mathbf{C}_{\mathbf{f}} = {\mathbf{C}_{d\mathbf{n}}\left({\mathbf{1} - {\mathbf{Y}^{- \mathbf{1}}\mathbf{X}}} \right)^{- \mathbf{1}}}$.

### Synthesis Method 5.13

Solve for $\mathbf{A}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{B}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{C}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$, $\mathbf{D}_{d\mathbf{n}} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{y}}}$, $\mathbf{X}_{\mathbf{1}}$, $\mathbf{Y}_{\mathbf{1}} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$, and $\gamma \in {\mathbb{R}}_{> 0}$ that minimize ${\mathcal{J}{(\gamma)}} = \gamma$ subject to $\mathbf{X}_{\mathbf{1}} > \mathbf{0}$, $\mathbf{Y}_{\mathbf{1}} > \mathbf{0}$, The filter state-space matrices are recovered by $\mathbf{A}_{\mathbf{f}} = {\mathbf{X}_{\mathbf{2}}^{- \mathbf{1}}\left({\mathbf{A}_{d\mathbf{n}} - {\mathbf{X}_{\mathbf{1}}\mathbf{A}_{d}\mathbf{Y}_{\mathbf{1}}}} \right)\mathbf{Y}_{\mathbf{2}}^{- \mathsf{T}}}$, $\mathbf{B}_{\mathbf{f}} = {\mathbf{X}_{\mathbf{2}}^{- \mathbf{1}}\mathbf{B}_{d\mathbf{n}}}$, $\mathbf{C}_{\mathbf{f}} = {\mathbf{C}_{d\mathbf{n}}\mathbf{Y}_{\mathbf{2}}^{- \mathsf{T}}}$, and $\mathbf{D}_{\mathbf{f}}$, where the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ satisfy ${\mathbf{X}_{\mathbf{2}}\mathbf{Y}_{\mathbf{2}}^{\mathsf{T}}} = {\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}}$. Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

This synthesis method is derived from the discrete-time $\mathcal{H}_{\infty}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.11 using the fact that $\mathcal{H}_{\infty}$-optimal filter synthesis is a special case of this problem.
