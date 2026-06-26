<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LMI Properties and Applications in Systems, Stability, and Control Theory

Topics include Stability analysis, Optimization, Control, Control theory.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Linear matrix inequalities (LMIs) commonly appear in systems, stability, and control applications. Many analysis and synthesis problems in these areas can be solved as feasibility or optimization problems subject to LMI constraints. Although most well-known LMI properties and manipulation tricks, such as the Schur complement and the congruence transformation, can be found in standard references, many useful LMI properties are scattered throughout the literature. The purpose of this document is to collect and organize properties, tricks, and applications related to LMIs from a number of references together in a single document. In this sense, the document can be thought of as an "LMI encyclopedia" or "LMI cookbook." Proofs of the properties presented in this document are not included when they can be found in the cited references in the interest of brevity. Illustrative examples are included whenever necessary to fully explain a certain property. Multiple equivalent forms of LMIs are often presented to give the reader a choice of which form may be best suited for a particular problem at hand.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The equivalency of some of the LMIs in this document may be straightforward to more experienced readers, but the authors believe that some readers may benefit from the presentation of multiple equivalent LMIs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear matrix inequalities (LMIs) commonly appear in systems, stability, and control applications. Many analysis and synthesis problems in these areas can be solved as feasibility or optimization problems subject to LMI constraints. Although most well-known LMI properties and manipulation tricks (e.g., Schur complement, congruence transformation) can be found in standard references, many useful LMI properties are scattered throughout the literature. The purpose of this document is to collect and organize properties, tricks, and applications related to LMIs from a number of references together in a single document. Proofs of the properties presented in this document are not included when they can be found in the cited references in the interest of brevity. Illustrative examples are included whenever necessary to fully explain a certain property. Multiple equivalent forms of LMIs are often presented to give the reader a choice of which form may be best suited for a particular problem at hand. The equivalency of some of the LMIs in this document may be straightforward to more experienced readers, but the authors believe that some readers may benefit from the presentation of multiple equivalent LMIs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The document is organized as follows. In the remaining portions of Section 1, the notation used throughout the document is presented and some fundamental LMI properties are discussed. Section 2 features a collection of LMI properties and tricks that are interesting and potentially useful. The LMI properties and tricks in this section are grouped together based on similarities when possible. Applications involving LMIs in systems and stability theory are included in Section 3. Section 4 presents a number of LMI-based optimal controller synthesis methods, while Section 5 includes LMI-based optimal estimation synthesis methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The authors would like to thank the following individuals for alerting us of errors, and providing useful comments and suggestions for improvement: Leila Bridgeman, Jyot Buch, Manash Chakraborty, Steven Dahdah, William Elke, Robyn Fortune, Peter Seiler.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Please note that this document is a work in progress. If you notice any errors or inaccuracies, or have any suggestions of content that should be included in this document, please email either of the authors at rcaverly@umn.edu or james.richard.forbes@mcgill.ca so that changes to future versions can be made.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Example 1.2", "weight": 1.0} -->

The positive definiteness and positive semidefiniteness of a matrix are denoted by $> 0$ and $\geq 0$, respectively (e.g., $\mathbf{A} = \mathbf{A}^{\mathsf{T}} > \mathbf{0}$ is positive definite and $\mathbf{B} = \mathbf{B}^{\mathsf{T}} \geq \mathbf{0}$ is positive semidefinite). Similarly, the negative definiteness and negative semidefiniteness of a matrix are denoted by $< 0$ and $\leq 0$, respectively (e.g., $\mathbf{C} = \mathbf{C}^{\mathsf{T}} < \mathbf{0}$ is negative definite and $\mathbf{D} = \mathbf{D}^{\mathsf{T}} \leq \mathbf{0}$ is negative semidefinite).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Example 1.2", "weight": 1.0} -->

For brevity, the transpose component of a definiteness statement is omitted in this document, for example, $\mathbf{A} = \mathbf{A}^{\mathsf{T}} > \mathbf{0}$ is simply written as $\mathbf{A} > \mathbf{0}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example 1.3", "weight": 1.0} -->

The matrix $\mathbf{P}$ is the design variable in this problem, and this LMI can be directly related to the definition in (1.2) by setting $\mathbf{F}_{\mathbf{0}} = \mathbf{Q}$, $\mathbf{G}_{\mathbf{1}} = \mathbf{1}$, $\mathbf{H}_{\mathbf{1}} = \mathbf{A}$, $\mathbf{X}_{\mathbf{1}} = \mathbf{P}$, and enforcing the constraint $\mathbf{X}_{\mathbf{1}} = \mathbf{X}_{\mathbf{1}}^{\mathsf{T}}$. This LMI can be reformulated in the form of (1.1) by defining the scalar entries of the matrix variable $\mathbf{P}$ as the design variables.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example 1.3", "weight": 1.0} -->

To illustrate this, let us consider the case of $n = 2$ so that each matrix is of dimension $2 \times 2$, and $\mathbf{x} = \begin{bmatrix} \mathbf{p}_{\mathbf{1}} & \mathbf{p}_{\mathbf{2}} & \mathbf{p}_{\mathbf{3}} \end{bmatrix}^{\mathsf{T}}$. Writing the matrix $\mathbf{P}$ in terms of a basis $\mathbf{E}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{2}}$, $i = {1,2,3}$, yields Note that the matrices $\mathbf{E}_{\mathbf{i}}$ are linearly independent and symmetric, thus forming a basis for the symmetric matrix $\mathbf{P}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 1.3", "weight": 1.0} -->

The matrix inequality in (1.3) can be written as Defining $\mathbf{F}_{\mathbf{0}} = \mathbf{Q}$ and $\mathbf{F}_{\mathbf{i}} = \mathbf{F}_{\mathbf{i}}^{\mathsf{T}} = {{\mathbf{E}_{\mathbf{i}}\mathbf{A}} + {\mathbf{A}^{\mathsf{T}}\mathbf{E}_{\mathbf{i}}}}$, $i = {1,2,3}$, yields which now resembles the definition of an LMI in (1.1). Throughout this document, LMIs are typically written in the matrix form of (1.2), rather than the scalar form of (1.1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Relative Definiteness of a Matrix", "weight": 1.0} -->

Knowing the relative definiteness of matrices can be useful. For example, if in the previous example we have $\mathbf{A} < \mathbf{B}$ and also know that $\mathbf{A} > \mathbf{0}$, then we know that $\mathbf{B} > \mathbf{0}$. This follows from $0 < \mathbf{A} < \mathbf{B}$. For more facts involving the relative definiteness of matrices, see \[7, pp. 703--704\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Strict and Nonstrict Matrix Inequalities", "weight": 1.0} -->

Converting a strict matrix inequality into a nonstrict matrix inequality is useful when working with LMI solvers that cannot handle strict constraints.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Concatenation of LMIs", "weight": 1.0} -->

A useful property of LMIs is that multiple LMIs can be concatenated together to form a single LMI. For example, satisfying the LMIs $\mathbf{A} < \mathbf{0}$ and $\mathbf{B} < \mathbf{0}$ is equivalent to satisfying the concatenated LMI More generally, satisfying the LMIs $\mathbf{A}_{\mathbf{i}} < \mathbf{0}$, $i = {1,\ldots,n}$ is equivalent to satisfying the concatenated LMI ${{diag}{\{\mathbf{A}_{\mathbf{1}},\ldots,\mathbf{A}_{\mathbf{n}}\}}} < \mathbf{0}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

A semidefinite program (SDP) is a convex optimization problem of the form \[12, p. 168\] where $\mathbf{x}^{\mathsf{T}} = \begin{bmatrix} {\mathbf{x}_{\mathbf{1}}\cdots\mathbf{x}_{\mathbf{m}}} \end{bmatrix}$, $\mathbf{c} \in {\mathbb{R}}^{\mathbf{m}}$, $\mathbf{F}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {0,\ldots,m}$, and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is an LMI in the variable $\mathbf{x}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

As shown in Example 1.3, the LMI constraint in (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) can be written in matrix form, rather than the standard form.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

The dual problem of the SDP described by (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is given by \[12, pp. 168--169\] where $\mathbf{c}^{\mathsf{T}} = \begin{bmatrix} \mathbf{c}_{\mathbf{1}} & {\cdots\mathbf{c}_{\mathbf{m}}} \end{bmatrix}$. Within the context of duality, the SDP outlined in (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is denoted as the primal problem. Further details on the use of SDP duality within the context of LTI systems can be found.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

When using matrix variables to describe an SDP's LMI constraints, it may be inconvenient to rewrite the objective function in the form of (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). SDP parsers, which will be discussed in Section 1.5, are capable of converting LMIs and linear objective functions in matrix form to the standard form required by most SDP solvers. An example of a linear objective function in matrix form is where $\mathbf{X}$, $\mathbf{Q}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

More generally, a number of convex objective functions involving matrix variables that are not explicitly written in the standard SDP form can be reformulated as SDPs. Some SDP parsers are capable of performing this conversion for the user. Two examples of such objective functions are given, with a brief explanation of how they can be reformulated in the standard SDP form.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1.4", "weight": 1.0} -->

The optimization problem is equivalent to the optimization problem where the Schur complement (see Section 2.3) is used to reformulate the quadratic objective function into an LMI constraint.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1.5", "weight": 1.0} -->

The optimization problem is equivalent to the optimization problem where a property involving the trace of a symmetric matrix (see Section 2.15) and the Schur complement (see Section 2.3) are used to reformulate the quadratic objective function into an LMI constraint.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1.5", "weight": 1.0} -->

Another useful convex objective function is given by ${\mathcal{J}{(\mathbf{X})}} = {\log\left( {\det{(\mathbf{X}^{- \mathbf{1}})}} \right)} = {- {\log\left( {\det{(\mathbf{X})}} \right)}}$, where $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{X} > \mathbf{0}$ \[1, p. 14\],. This objective function cannot be readily converted into the standard SDP form, but can be implemented with most SDP solvers and parsers. In particular, SDPT3 is capable of directly minimizing SDPs with objective functions of the form $- {\log\left( {\det{(\mathbf{X})}} \right)}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical Tools to Solve SDPs", "weight": 1.0} -->

There are many semidefinite program solvers that accept LMI constraints. Most solvers require that LMI constraints be written in the standard form shown in (1.1). This is often not convenient, as it is typical to derive LMI constraints in matrix form, such as the LMI in (1.3). LMI parsers convert LMIs in matrix form to the standard form in (1.1), allowing for a smoother transition from mathematical derivation to numerical implementation. A non-exhaustive list of SDP solvers and LMI parsers are included for reference.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SDP Solvers", "weight": 1.0} -->

There are a number of SDP solvers available. The authors have experience with SeDuMi, SDPT3, and Mosek, though other solvers are available, such as CSDP, CVXOPT, DDS, DSDP, LMILab, PENLAB, SCS, SDPA, SMCP, and SDPNAL. There are advantages and disadvantages to each of these solvers, and sometimes one solver may give a solution to a given problem when others do not. For this reason, it is useful to have multiple solvers available. Comparisons of various LMI solvers and benchmark problems are found.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SDP Solvers", "weight": 1.0} -->

Many solvers, including SeDuMi, SDPT3, are available for free, while Mosek is a commercial software package. A free academic license of Mosek can be requested for research in academic institutions or educational purposes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Parsers", "weight": 1.0} -->

LMI parsers allow the user to define the SDP to be solved within standard software environments, and often in a more convenient matrix form. A number of openly-distributed LMI parsers are available for use within different software environments. The following is a non-exhaustive list of LMI parsers and the solvers they are known to be compatible, sorted by software environment.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Parsers", "weight": 1.0} -->

Yalmip. Solvers: CSDP, DSDP, LMILab, Mosek, PENLAB, SCS, SDPA, SDPT3, SDPNAL, and SeDuMi.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Parsers", "weight": 1.0} -->

CVX. Solvers: Mosek, SDPT3, and SeDuMi.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Parsers", "weight": 1.0} -->

CVXPY. Solvers: SCS. Other solvers can be installed separately.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Parsers", "weight": 1.0} -->

PICOS. Solvers: CVXOPT, Mosek, and SMCP.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Parsers", "weight": 1.0} -->

Irene. Solvers: CSDP, CVXOPT, DSDP, and SDPA.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Parsers", "weight": 1.0} -->

PyLMI-SDP. Solvers: CVXOPT and SDPA.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Parsers", "weight": 1.0} -->

Convex.jl. Solvers: Mosek and SCS.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Parsers", "weight": 1.0} -->

JuMP. Solvers: Mosek and SCS.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Parsers", "weight": 1.0} -->

SciYalmip. Solvers: CSDP and SDPA. Also features the internal solver LMISOLVER.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Parsers", "weight": 1.0} -->

NSPYalmip. Solvers: CSDP and SeDuMi.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Properties and Tricks", "weight": 1.0} -->

This section presents a compilation of LMI properties and tricks from the literature. Many of these properties are used in subsequent sections to reformulate LMIs or transform matrix inequalities into LMIs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Change of Variables \\[1, pp. 100--101\\], \\[4, Sec. 12.3.1\\]", "weight": 1.0} -->

A BMI can sometimes be converted into an LMI using a change of variables.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

It is important that a change of variables is chosen to be a one-to-one mapping in order for the new matrix inequality to be equivalent to the original matrix inequality. In Example 2.1 the change of variable $\mathbf{F} = {\mathbf{K}\mathbf{Q}}$ is a one-to-one mapping since $\mathbf{Q}^{- \mathbf{1}}$ is invertible, which gives a unique solution for the reverse change of variable $\mathbf{K} = {\mathbf{F}\mathbf{Q}}^{- \mathbf{1}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 2.2", "weight": 1.0} -->

A congruence transformation preserves the definiteness of a matrix by ensuring that $\mathbf{Q} < \mathbf{0}$ and ${\mathbf{W}\mathbf{Q}\mathbf{W}}^{\mathsf{T}} < \mathbf{0}$ are equivalent. A congruence transformation is related, but not equivalent to a similarity transformation ${\mathbf{T}\mathbf{Q}\mathbf{T}}^{- \mathbf{1}}$, which preserves not only the definiteness, but also the eigenvalues of a matrix. A congruence transformation is equivalent to a similarity transformation in the special case when $\mathbf{W}^{\mathsf{T}} = \mathbf{W}^{- \mathbf{1}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Young's Relation", "weight": 1.0} -->

Young's relation can be derived from a completion of the squares as follows. which is Young's relation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Iterative convex overbounding is a technique based on Young's relation that is useful when solving an optimization problem with a BMI constraint.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

are design variables in the BMI given by Suppose that $\mathbf{S}_{\mathbf{0}}$ and $\mathbf{R}_{\mathbf{0}}$ are known to satisfy (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

The LMI of (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is equivalent to the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, and is therefore non-conservative for values of $\mathbf{R}$ and $\mathbf{S}$ and are close to the previously known solutions $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Alternatively, the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where $\mathbf{Z} > \mathbf{0}$ is an arbitrary matrix, $\mathbf{D} = {\mathbf{U}\mathbf{V}}$, and the matrices $\mathbf{U}$ and $\mathbf{V}^{\mathsf{T}}$ have full column rank.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Again, the LMI of (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is equivalent to the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, and is therefore non-conservative for values of $\mathbf{R}$ and $\mathbf{S}$ and are close to the previously known solutions $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

A benefit of convex overbounding compared to a linearization approach, is that in addition to ensuring conservatism or error is reduced in the neighborhood of $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, the LMIs of (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) imply (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Iterative convex overbounding is particularly useful when used to solve an optimization problem with BMI constraints. For example, choose $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$ that are initial feasible solutions to (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Then solve for $\mathbf{R}$ and $\mathbf{S}$ that minimize a specified objective function and satisfy (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) or (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), which imply (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) without conservatism when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$. Set $\mathbf{R}_{\mathbf{0}} = \mathbf{R}$ and $\mathbf{S}_{\mathbf{0}} = \mathbf{S}$, and repeat until the objective function meets a specified stopping criteria.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

The benefits of this procedure are that its individual steps are convex optimization problems with very little conservatism in the neighborhood of the solution from the previous iteration, and that it tends to converge quickly to a solution. However, there is no guarantee that the method will converge to even a local solution.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

Consider a special case of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) given by where $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{S} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. The BMI of (2.41 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where $\mathbf{W} > \mathbf{0}$ is an arbitrary matrix.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

Alternatively, the BMI of (2.41 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI where $\mathbf{Z} > \mathbf{0}$ is an arbitrary matrix.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Projection Lemma-Based Properties", "weight": 1.0} -->

Consider $\mathbf{A} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{B}$, $\mathbf{J} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{G} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$, and $\mathbf{P} \in {\mathbb{S}}^{\mathbf{m}}$. The matrix inequality given by implies the matrix inequality If the matrices $\mathbf{J}$ and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.43 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.44 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Projection Lemma-Based Properties", "weight": 1.0} -->

Consider $\mathbf{T} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{A}$, $\mathbf{J}$, $\mathbf{G}$, $\mathbf{P} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The matrix inequality given by implies the matrix inequality If the matrices $\mathbf{J}$ and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.45 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.46 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

The Schur complement, Young's relation, and the projection lemma are three of the most common tools used to transform a BMI into an LMI. The sign of the BMI determines which one is suitable to transform the BMI into an LMI. For example, consider the case of a BMI in the variable $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$ of the form where $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{S} > \mathbf{0}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

The Schur complement is used to obtain an equivalent LMI given by This LMI can also be written as Applying the Projection Lemma, it is known that there exists $\mathbf{Y}$ satisfying (2.52) if and only if $\mathbf{P} < \mathbf{0}$ and $\mathbf{S}^{- \mathbf{1}} > \mathbf{0}$, since ${\mathcal{N}\left(\begin{bmatrix} \end{bmatrix} \right)} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, ${\mathcal{N}\left(\begin{bmatrix} \end{bmatrix} \right)} = {\mathcal{R}\left(\begin{bmatrix} \end{bmatrix} \right)}$, and Notice that the Projection Lemma gives two matrix inequalities that do not depend on the variable $\mathbf{Y}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

This is why the Projection Lemma is also known as the Matrix Elimination Lemma.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

Alternatively, consider the BMI where $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$, $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{m}}$, and $\mathbf{S} > \mathbf{0}$. Young's relation is used to obtain an LMI in $\mathbf{Y}$ given by which implies the BMI of (2.53). Notice that (2.54) involves a new variable $\mathbf{X} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. Using the Schur complement on (2.54) yields which is an LMI in $\mathbf{Y}$ for a fixed $\mathbf{X}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

It is desirable to use the Schur complement of the Projection Lemma over Young's relation whenever possible, as they provides an LMI or LMIs that are equivalent to the original BMI. When using Young's relation, the resulting LMI implies the original BMI, but is not equivalent. This introduces conservatism into an optimization problem.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

If a previously-known solution $\mathbf{Y}_{\mathbf{0}}$ to (2.53) is available, then convex overbounding can be used to reduce conservatism in the neighborhood of $\mathbf{Y}_{\mathbf{0}}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

The BMI of (2.53) is equivalent to the BMI Since the term $\left({\mathbf{Y} - \mathbf{Y}_{\mathbf{0}}} \right)^{\mathsf{T}}\mathbf{S}\left({\mathbf{Y} - \mathbf{Y}_{\mathbf{0}}} \right)$ is positive definite, (2.55) is implied by the LMI The LMI of (2.56) is in general conservative, but this conservatism disappears when $\mathbf{Y} = \mathbf{Y}_{\mathbf{0}}$ and is reduced when $\mathbf{Y}$ is close to $\mathbf{Y}_{\mathbf{0}}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Dilation", "weight": 1.0} -->

Matrix inequalities can be dilated to obtain a larger matrix inequality, often with additional design variables. This can be a useful technique to separate design variables in a BMI.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Dilation", "weight": 1.0} -->

A common technique to dilate an LMI involves the use the projection lemma in reverse or the reciprocal projection lemma. For instance, consider the following example taken from and inspired by the dilated bounded real lemma matrix inequality in \[5, pp. 153--155\] involving the matrices $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$. The matrix inequality Since $\mathbf{P} > \mathbf{0}$, it is also known that which can be rewritten as The matrix inequalities in (2.58) and (2.59) are in the form of the strict projection lemma.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Dilation", "weight": 1.0} -->

Choosing the matrix inequality of (2.60) can be rewritten as Therefore, the matrix inequality of (2.58) with $\mathbf{P} > \mathbf{0}$ is equivalent to the dilated matrix inequality of (2.61).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Examples of Dilated Matrix Inequalities", "weight": 1.0} -->

Examples of some useful dilated matrix inequalities are presented here, while dilated forms of a number of important matrix inequalities are included as equivalent matrix inequalities in their respective sections.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Spectral Radius \\[8, p. 17\\]", "weight": 1.0} -->

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\delta \in {\mathbb{R}}_{> 0}$. The spectral radius of $\mathbf{A}$ is strictly less than $\delta$ (i.e., ${\rho{(\mathbf{A})}} < \delta$) under either of the following necessary and sufficient conditions.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Spectral Radius \\[8, p. 17\\]", "weight": 1.0} -->

There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that There exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{X} > \mathbf{0}$, such that Also see Section 3.25 for a similar condition related to the structured singular value.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Lyapunov Stability \\[7, pp. 1201--1203\\], \\[1, pp. 20--21\\]", "weight": 1.0} -->

The matrix inequality of (3.1) is satisfied under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Asymptotic Stability \\[7, p. 1201--1203\\], \\[1, p. 2\\]", "weight": 1.0} -->

The matrix inequality of (3.2) is satisfied and the matrix $\mathbf{A}$ is Hurwitz under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Discrete-Time Lyapunov Stability \\[7, pp. 1203--1204\\]", "weight": 1.0} -->

The matrix inequality of (3.8) is satisfied and the eigenvalues of $\mathbf{A}_{d}$ satisfy $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| \leq 1$, $i = {1,\ldots,n}$ under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Discrete-Time Asymptotic Stability \\[7, pp. 1203--1204\\], \\[5, pp. 97--98\\]", "weight": 1.0} -->

The matrix inequality of (3.9) is satisfied and the eigenvalues of $\mathbf{A}_{d}$ satisfy $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| < 1$, $i = {1,\ldots,n}$ under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Descriptor System Admissibility", "weight": 1.0} -->

Consider the descriptor system given by ${\mathbf{E}\overset{˙}{\mathbf{x}}} = {\mathbf{A}\mathbf{x}}$, where $\mathbf{E}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The descriptor system is admissible under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Discrete-Time Descriptor System Admissibility", "weight": 1.0} -->

Consider the discrete-time descriptor system given by ${\mathbf{E}_{d}\mathbf{x}_{\mathbf{k} + \mathbf{1}}} = {\mathbf{A}_{d}\mathbf{x}_{\mathbf{k}}}$, where $\mathbf{E}_{d}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The discrete-time descriptor system is admissible under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0075", "role": "body", "section": "KYP (Positive Real) Lemma Without Feedthrough \\[152, p. 219\\] \\[154, p. 14\\]", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly positive real (SPR) under either of the following necessary and sufficient conditions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "KYP (Positive Real) Lemma With Feedthrough \\[1, p. 25\\], \\[152, p. 218\\] \\[155, pp. 79--80\\]", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly positive real (SPR) under either of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discrete-Time KYP (Positive Real) Lemma With Feedthrough \\[155, pp. 171--172\\]", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly positive real (SPR) under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$, where $a$, $b \in {\mathbb{R}}$, and $a < b$, under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Note that the matrix inequality of (3.50) does not allow for the case where the upper bound $b$ is infinite.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

There exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Note that the matrix inequality of (3.51) does not allow for the case where the upper bound $b$ is infinite.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

The parameter ${\overline{\omega}}_{1}$ is included in (3.56 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) to effectively transform $|\omega| \leq {({\omega_{1} - {\overline{\omega}}_{1}})}$ into the strict inequality $|\omega| < \omega_{1}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

(High Frequency Range) The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$ for all $\omega \in \left.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

inequalities in (3.56 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), (3.57 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), and (3.58 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) can be nonstrict.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Minimum Gain Lemma", "weight": 1.0} -->

The system $\mathcal{G}$ also has minimum gain $\nu$ under any of the following sufficient conditions.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discrete-Time Algebraic Riccati Inequality", "weight": 1.0} -->

Consider $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, $\mathbf{B}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, $\mathbf{P}$, $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, and $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$, where $\mathbf{P} > \mathbf{0}$, $\mathbf{Q} \geq \mathbf{0}$, and $\mathbf{R} > \mathbf{0}$. The discrete-time algebraic Riccati inequality given by can be rewritten using the Schur complement lemma as Equivalently, this discrete-time algebraic Riccati inequality is satisfied under any of the following necessary and sufficient conditions.

<!-- chunk {"id": "body-0086", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Stability \\[5, pp. 107--108\\],", "weight": 1.0} -->

The matrix $\mathbf{A}$ is $\mathcal{D}$-stable if and only if any of the following equivalent conditions are satisfied.

<!-- chunk {"id": "body-0087", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Stability \\[5, pp. 107--108\\],", "weight": 1.0} -->

Alternatively, consider the LMI region $\mathcal{D}$ of the complex plane defined by \[3, p. 66\] where $\mathbf{Q}$, $\mathbf{R} \in {\mathbb{S}}^{\mathbf{m}}$ and $\mathbf{S} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{m}}$. The matrix $\mathbf{A}$ is $\mathcal{D}$-stable if and only if there exists $\mathbf{P}$ such that

<!-- chunk {"id": "body-0088", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Admissibility", "weight": 1.0} -->

The pair $(\mathbf{E},\mathbf{A})$ is $\mathcal{D}$-admissible if and only if any of the following equivalent conditions are satisfied.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Transient State Bound for Discrete-Time Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization where $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The Euclidean norm of the state satisfies if there exist $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\gamma \in {\mathbb{R}}_{> 0}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0090", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

Consider the case where the set of perturbation parameters is defined by a regular polyhedron as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Consider the case where the set of perturbation parameters is defined by a polytope as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

Consider the case where the set of perturbation parameters is defined by a regular polyhedron as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that Consider the case where the set of perturbation parameters is defined by a polytope as The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0092", "role": "body", "section": "Delay-Independent Condition \\[5, p. 126\\]", "weight": 1.0} -->

The time-delay system in (3.162) is asymptotically stable if there exist $\mathbf{P}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{S} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0093", "role": "body", "section": "Delay-Dependent Condition \\[5, pp. 128--129\\]", "weight": 1.0} -->

The time-delay system in (3.162) is uniformly asymptotically stable if there exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\beta \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\beta < 1$, such that

<!-- chunk {"id": "body-0094", "role": "body", "section": "Static Output Feedback Algebraic Loop\\[7, p. 1284\\], \\[175, pp. 39--40\\]", "weight": 1.0} -->

The change of variable $\overline{\mathbf{K}} = {\left( {\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}} \right)^{- 1}\mathbf{K}}$ allows for the simplification of matrix inequalities involving the closed-loop system.

<!-- chunk {"id": "body-0095", "role": "body", "section": "LMIs in Optimal Control", "weight": 1.0} -->

This section presents controller synthesis methods using LMIs for a number of well-known optimal control problems. The derivation of the LMIs used for controller synthesis is provided in some cases, while longer derivations can be found in the cited references.

<!-- chunk {"id": "body-0096", "role": "body", "section": "The Continuous-Time Generalized Plant", "weight": 1.0} -->

Consider the generalized LTI plant ${\mathcal{P}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, shown in Figure 1, with a minimal state-space realization \[7, pp. 1291--1292\], \[4, Section 3.8\], \[200, p. 141\], \[201, pp. 14--16\], \[202, pp.

<!-- chunk {"id": "body-0097", "role": "body", "section": "The Continuous-Time Generalized Plant", "weight": 1.0} -->

{\mathbb{R}}^{\mathbf{n}_{\mathbf{u}}}$ is the control input signal, and the state-space matrices are real matrices with appropriate dimensions.

<!-- chunk {"id": "body-0098", "role": "body", "section": "The Continuous-Time Generalized Plant", "weight": 1.0} -->

The generalized LTI plant can also be written in transfer matrix form as where the transfer matrix ${\mathbf{P}{(\mathbf{s})}} \in {\mathbb{C}}^{{({\mathbf{n}_{\mathbf{z}} + \mathbf{n}_{\mathbf{y}}})} \times {({\mathbf{n}_{\mathbf{w}} + \mathbf{n}_{\mathbf{u}}})}}$ is partitioned as The generalized plant, also known as the standard control problem in \[7, pp. 1291--1292\], \[201, pp. 14--16\] is useful, as it is possible to represent a number of LTI systems in this form, as shown in the following example.

<!-- chunk {"id": "body-0099", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Control", "weight": 1.0} -->

The goal of $\mathcal{H}_{2}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Full-State Feedback Control \\[5, pp. 257--258\\]", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{B}_{\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}$ to the performance output $\mathbf{z}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Full-State Feedback Control \\[5, pp. 257--258\\]", "weight": 1.0} -->

A change of variables is performed with $\mathbf{F} = {\mathbf{K}\mathbf{P}}$ and $\nu = \mu^{2}$, which transforms (4.3) and (4.5) into LMIs in the variables $\mathbf{P}$, $\mathbf{F}$, $\mathbf{Z}$, and $\nu$ given by

<!-- chunk {"id": "body-0102", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by and $\overset{\sim}{\mathbf{D}} = {\mathbf{1} - {\mathbf{D}_{\mathbf{2}\mathbf{2}}\mathbf{D}_{\mathbf{c}}}}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Synthesis Method 4.3", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Synthesis Method 4.4", "weight": 1.0} -->

Given $\mathbf{G}$ and $\mathbf{H}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Synthesis Method 4.4", "weight": 1.0} -->

The LMI in (4.9) is derived from the LMI in Theorem 7 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix Similarly, the LMI in (4.10) is derived from the LMI in Theorem 7 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix

<!-- chunk {"id": "body-0106", "role": "body", "section": "Synthesis Method 4.5", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Synthesis Method 4.5", "weight": 1.0} -->

The LMIs in (4.12) and (4.13) are derived from (4.9) and (4.10) using the change of variables $\mathbf{S} = \mathbf{J} = \mathbf{1}$, $\mathbf{H} = \mathbf{X}_{\mathbf{1}}$, $\mathbf{G} = \mathbf{Y}_{\mathbf{1}}$. The LMI in (4.14) is added to ensure that ${\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}} \geq \mathbf{0}$ in a similar fashion to the approach used.

<!-- chunk {"id": "body-0108", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Control", "weight": 1.0} -->

The goal of $\mathcal{H}_{\infty}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control \\[5, pp. 251--252\\]", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{B}_{\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize $\mathcal{H}_{\infty}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}$ to the performance output $\mathbf{z}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control \\[5, pp. 251--252\\]", "weight": 1.0} -->

Substituting the full-state feedback controller into (4.15) and (4.16) yields and a closed-loop transfer matrix From the Bounded Real Lemma in Section 3.2.1, the $\mathcal{H}_{\infty}$ of the closed-loop system is the minimum value of $\gamma \in {\mathbb{R}}_{> 0}$ that satisfies where $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}_{\mathbf{x}}}$ and $\mathbf{P} > \mathbf{0}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by and $\overset{\sim}{\mathbf{D}} = {\mathbf{1} - {\mathbf{D}_{\mathbf{2}\mathbf{2}}\mathbf{D}_{\mathbf{c}}}}$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Two different synthesis methods for the $\mathcal{H}_{\infty}$-optimal dynamic output feedback control problem are presented as follows.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Synthesis Method 4.8", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Synthesis Method 4.9", "weight": 1.0} -->

,\[2, pp. 224--232\] The controller is solved for in the following two steps.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization A discrete-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{d\mathbf{c}},\mathbf{B}_{d\mathbf{c}},\mathbf{C}_{d\mathbf{c}},\mathbf{D}_{d\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by and ${\overset{\sim}{\mathbf{D}}}_{d} = {\mathbf{1} - {\mathbf{D}_{d\mathbf{2}\mathbf{2}}\mathbf{D}_{d\mathbf{c}}}}$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Synthesis Method 4.10", "weight": 1.0} -->

Given $\mathbf{G}$ and $\mathbf{H}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Synthesis Method 4.10", "weight": 1.0} -->

The LMI in (4.20) is derived from the LMI in Theorem 8 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix followed by the change of variables $\gamma = \mu^{2}$, $\mathbf{X}_{\mathbf{1}} = {\gamma\mathbf{H}}$, $\mathbf{Y}_{\mathbf{1}} = {\gamma^{- \mathbf{1}}\mathbf{P}}$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Synthesis Method 4.11", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Control", "weight": 1.0} -->

The goal of mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{1}}$ to $\mathbf{z}_{\mathbf{1}}$, while ensuring that the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer function from $\mathbf{w}_{\mathbf{2}}$ to $\mathbf{z}_{\mathbf{2}}$ is below a specified bound.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Synthesis Method 4.14", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Synthesis Method 4.15", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0122", "role": "body", "section": "LMIs in Optimal Estimation and Filtering", "weight": 1.0} -->

This section presents controller synthesis methods using LMIs for a number of well-known optimal state-estimation and filtering problems. The derivation of the LMIs used for synthesis is provided in some cases, while longer derivations can be found in the cited references.

<!-- chunk {"id": "body-0123", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal State Estimation", "weight": 1.0} -->

The goal of $\mathcal{H}_{2}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0124", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e} = {\mathbf{x} - \hat{\mathbf{x}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}$ is to be designed such that the $\mathcal{H}_{2}$ norm of the transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by is minimized.

<!-- chunk {"id": "body-0125", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

A change of variables is performed with $\mathbf{G} = {\mathbf{P}\mathbf{L}}$ and $\nu = \mu^{2}$, which transforms (5.1) and (5.3) into LMIs in the variables $\mathbf{P}$, $\mathbf{G}$, $\mathbf{Z}$, and $\nu$ given by

<!-- chunk {"id": "body-0126", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Observer", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain.

<!-- chunk {"id": "body-0127", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal State Estimation", "weight": 1.0} -->

The goal of $\mathcal{H}_{\infty}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "$\\mathcal{H}_{\\infty}$--Optimal Observer \\[5, p. 295\\]", "weight": 1.0} -->

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain. Defining the error state $\mathbf{e} = {\mathbf{x} - \hat{\mathbf{x}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}$ is to be designed such that the $\mathcal{H}_{\infty}$ of the transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

<!-- chunk {"id": "body-0129", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$--Optimal Observer", "weight": 1.0} -->

Consider the discrete-time LTI plant $\mathcal{G}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal State Estimation", "weight": 1.0} -->

The goal of mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{1}}$ to $\mathbf{z}_{\mathbf{1}}$, while ensuring that the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{2}}$ to $\mathbf{z}_{\mathbf{2}}$ is below a specified bound.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

Defining the error state $\mathbf{e} = {\mathbf{x} - \hat{\mathbf{x}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{1}}$ to the performance output $\mathbf{z}_{\mathbf{1}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix $\mathbf{T}_{\mathbf{2}\mathbf{2}}{(\mathbf{s})}$ from the exogenous input $\mathbf{w}_{\mathbf{2}}$ to the performance output

<!-- chunk {"id": "body-0133", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form is to be designed, where $\mathbf{L}_{d} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{x}} \times \mathbf{n}_{\mathbf{y}}}$ is the observer gain.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

Defining the error state $\mathbf{e}_{\mathbf{k}} = {\mathbf{x}_{\mathbf{k}} - {\hat{\mathbf{x}}}_{\mathbf{k}}}$, the error dynamics are found to be and the performance output is defined as The observer gain $\mathbf{L}_{d}$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix $\mathbf{T}_{\mathbf{1}\mathbf{1}}{(\mathbf{z})}$ from the exogenous input $\mathbf{w}_{\mathbf{1},\mathbf{k}}$ to the performance output $\mathbf{z}_{\mathbf{1},\mathbf{k}}$ while ensuring the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix

<!-- chunk {"id": "body-0135", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

The goal of optimal filtering is to design a filter that acts on the output $\mathbf{z}$ of the generalized plant and optimizes the transfer matrix from $\mathbf{w}$ to the filtered output.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

Continuous-Time Filtering: Consider the continuous-time generalized LTI plant with minimal states-space realization where it is assumed that $\mathbf{A}$ is Hurwitz. A continuous-time dynamic LTI filter with state-space realization is to be designed to optimize the transfer function from $\mathbf{w}$ to $\overset{\sim}{\mathbf{z}} = {\mathbf{z} - \hat{\mathbf{z}}}$, given by This can alternatively be formulated as a special case of synthesizing a dynamic output "feedback" controller for the generalized plant given by The controller in this case is not truly a feedback controller, as it only appears as a feedthrough term in the performance channel. The synthesis methods presented in this subsection take advantage of this fact, resulting in a simpler formulation than applying the controller synthesis methods in Section 4.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

Discrete-Time Filtering: Consider the discrete-time generalized LTI plant with minimal states-space realization where it is assumed that $\mathbf{A}_{d}$ is Schur. A discrete-time dynamic LTI filter with state-space realization is to be designed to optimize the transfer function from $\mathbf{w}_{\mathbf{k}}$ to ${\overset{\sim}{\mathbf{z}}}_{k} = {\mathbf{z}_{\mathbf{k}} - {\hat{\mathbf{z}}}_{\mathbf{k}}}$, given by This can alternatively be formulated as a special case of synthesizing a dynamic output "feedback" controller for the generalized plant given by

<!-- chunk {"id": "body-0138", "role": "body", "section": "Synthesis Method 5.10", "weight": 1.0} -->

This synthesis method is derived from the discrete-time $\mathcal{H}_{2}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.5 using the fact that $\mathcal{H}_{2}$-optimal filter synthesis is a special case of this problem.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Synthesis Method 5.13", "weight": 1.0} -->

This synthesis method is derived from the discrete-time $\mathcal{H}_{\infty}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.11 using the fact that $\mathcal{H}_{\infty}$-optimal filter synthesis is a special case of this problem.
