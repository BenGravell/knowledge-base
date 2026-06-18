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

Consider the matrix $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, which can be decomposed as

<!-- chunk {"id": "body-0009", "role": "body", "section": "Example 1.2", "weight": 1.0} -->

This confirms that when determining the definiteness of a matrix there is no loss of generality in restricting the matrix to be symmetric.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example 1.2", "weight": 1.0} -->

The positive definiteness and positive semidefiniteness of a matrix are denoted by $> 0$ and $\geq 0$, respectively (e.g., $\mathbf{A} = \mathbf{A}^{\mathsf{T}} > \mathbf{0}$ is positive definite and $\mathbf{B} = \mathbf{B}^{\mathsf{T}} \geq \mathbf{0}$ is positive semidefinite). Similarly, the negative definiteness and negative semidefiniteness of a matrix are denoted by $< 0$ and $\leq 0$, respectively (e.g., $\mathbf{C} = \mathbf{C}^{\mathsf{T}} < \mathbf{0}$ is negative definite and $\mathbf{D} = \mathbf{D}^{\mathsf{T}} \leq \mathbf{0}$ is negative semidefinite).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example 1.2", "weight": 1.0} -->

For brevity, the transpose component of a definiteness statement is omitted in this document, for example, $\mathbf{A} = \mathbf{A}^{\mathsf{T}} > \mathbf{0}$ is simply written as $\mathbf{A} > \mathbf{0}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 1.3", "weight": 1.0} -->

Note that the matrices $\mathbf{E}_{\mathbf{i}}$ are linearly independent and symmetric, thus forming a basis for the symmetric matrix $\mathbf{P}$. The matrix inequality in (1.3) can be written as

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 1.3", "weight": 1.0} -->

which now resembles the definition of an LMI in (1.1). Throughout this document, LMIs are typically written in the matrix form of (1.2), rather than the scalar form of (1.1).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Relative Definiteness of a Matrix", "weight": 1.0} -->

Knowing the relative definiteness of matrices can be useful. For example, if in the previous example we have $\mathbf{A} < \mathbf{B}$ and also know that $\mathbf{A} > \mathbf{0}$, then we know that $\mathbf{B} > \mathbf{0}$. This follows from $0 < \mathbf{A} < \mathbf{B}$. For more facts involving the relative definiteness of matrices, see \[7, pp. 703--704\].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Strict and Nonstrict Matrix Inequalities", "weight": 1.0} -->

Converting a strict matrix inequality into a nonstrict matrix inequality is useful when working with LMI solvers that cannot handle strict constraints.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Concatenation of LMIs", "weight": 1.0} -->

A useful property of LMIs is that multiple LMIs can be concatenated together to form a single LMI. For example, satisfying the LMIs $\mathbf{A} < \mathbf{0}$ and $\mathbf{B} < \mathbf{0}$ is equivalent to satisfying the concatenated LMI

<!-- chunk {"id": "body-0017", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

A semidefinite program (SDP) is a convex optimization problem of the form \[12, p. 168\]

<!-- chunk {"id": "body-0018", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

where $\mathbf{x}^{\mathsf{T}} = \begin{bmatrix}
{\mathbf{x}_{\mathbf{1}}\cdots\mathbf{x}_{\mathbf{m}}}
\end{bmatrix}$, $\mathbf{c} \in {\mathbb{R}}^{\mathbf{m}}$, $\mathbf{F}_{\mathbf{i}} \in {\mathbb{S}}^{\mathbf{n}}$, $i = {0,\ldots,m}$, and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is an LMI in the variable $\mathbf{x}$. As shown in Example 1.3, the LMI constraint in (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) can be written in matrix form, rather than the standard form.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

The dual problem of the SDP described by (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is given by \[12, pp. 168--169\]

<!-- chunk {"id": "body-0020", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

where $\mathbf{c}^{\mathsf{T}} = \begin{bmatrix}
\mathbf{c}_{\mathbf{1}} & {\cdots\mathbf{c}_{\mathbf{m}}}
\end{bmatrix}$. Within the context of duality, the SDP outlined in (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (1.5 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is denoted as the primal problem. Further details on the use of SDP duality within the context of LTI systems can be found.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

When using matrix variables to describe an SDP's LMI constraints, it may be inconvenient to rewrite the objective function in the form of (1.4 ‣ 1 Preliminaries ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). SDP parsers, which will be discussed in Section 1.5, are capable of converting LMIs and linear objective functions in matrix form to the standard form required by most SDP solvers. An example of a linear objective function in matrix form is

<!-- chunk {"id": "body-0022", "role": "body", "section": "Semidefinite Programs (SDPs)", "weight": 1.0} -->

More generally, a number of convex objective functions involving matrix variables that are not explicitly written in the standard SDP form can be reformulated as SDPs. Some SDP parsers are capable of performing this conversion for the user. Two examples of such objective functions are given, with a brief explanation of how they can be reformulated in the standard SDP form.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1.4", "weight": 1.0} -->

where the Schur complement (see Section 2.3) is used to reformulate the quadratic objective function into an LMI constraint.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1.5", "weight": 1.0} -->

where a property involving the trace of a symmetric matrix (see Section 2.15) and the Schur complement (see Section 2.3) are used to reformulate the quadratic objective function into an LMI constraint.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 1.5", "weight": 1.0} -->

Another useful convex objective function is given by ${\mathcal{J}{(\mathbf{X})}} = {\log\left( {\det{(\mathbf{X}^{- \mathbf{1}})}} \right)} = {- {\log\left( {\det{(\mathbf{X})}} \right)}}$, where $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{X} > \mathbf{0}$ \[1, p. 14\],. This objective function cannot be readily converted into the standard SDP form, but can be implemented with most SDP solvers and parsers. In particular, SDPT3 is capable of directly minimizing SDPs with objective functions of the form $- {\log\left( {\det{(\mathbf{X})}} \right)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Tools to Solve SDPs", "weight": 1.0} -->

There are many semidefinite program solvers that accept LMI constraints. Most solvers require that LMI constraints be written in the standard form shown in (1.1). This is often not convenient, as it is typical to derive LMI constraints in matrix form, such as the LMI in (1.3). LMI parsers convert LMIs in matrix form to the standard form in (1.1), allowing for a smoother transition from mathematical derivation to numerical implementation. A non-exhaustive list of SDP solvers and LMI parsers are included for reference.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SDP Solvers", "weight": 1.0} -->

There are a number of SDP solvers available. The authors have experience with SeDuMi, SDPT3, and Mosek, though other solvers are available, such as CSDP, CVXOPT, DDS, DSDP, LMILab, PENLAB, SCS, SDPA, SMCP, and SDPNAL. There are advantages and disadvantages to each of these solvers, and sometimes one solver may give a solution to a given problem when others do not. For this reason, it is useful to have multiple solvers available. Comparisons of various LMI solvers and benchmark problems are found.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SDP Solvers", "weight": 1.0} -->

Many solvers, including SeDuMi, SDPT3, are available for free, while Mosek is a commercial software package. A free academic license of Mosek can be requested for research in academic institutions or educational purposes.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Parsers", "weight": 1.0} -->

LMI parsers allow the user to define the SDP to be solved within standard software environments, and often in a more convenient matrix form. A number of openly-distributed LMI parsers are available for use within different software environments. The following is a non-exhaustive list of LMI parsers and the solvers they are known to be compatible, sorted by software environment.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Parsers", "weight": 1.0} -->

Yalmip. Solvers: CSDP, DSDP, LMILab, Mosek, PENLAB, SCS, SDPA, SDPT3, SDPNAL, and SeDuMi.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Parsers", "weight": 1.0} -->

CVX. Solvers: Mosek, SDPT3, and SeDuMi.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Parsers", "weight": 1.0} -->

CVXPY. Solvers: SCS. Other solvers can be installed separately.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Parsers", "weight": 1.0} -->

PICOS. Solvers: CVXOPT, Mosek, and SMCP.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Parsers", "weight": 1.0} -->

Irene. Solvers: CSDP, CVXOPT, DSDP, and SDPA.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Parsers", "weight": 1.0} -->

PyLMI-SDP. Solvers: CVXOPT and SDPA.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Parsers", "weight": 1.0} -->

Convex.jl. Solvers: Mosek and SCS.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Parsers", "weight": 1.0} -->

JuMP. Solvers: Mosek and SCS.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Parsers", "weight": 1.0} -->

SciYalmip. Solvers: CSDP and SDPA. Also features the internal solver LMISOLVER.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Parsers", "weight": 1.0} -->

NSPYalmip. Solvers: CSDP and SeDuMi.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Properties and Tricks", "weight": 1.0} -->

This section presents a compilation of LMI properties and tricks from the literature. Many of these properties are used in subsequent sections to reformulate LMIs or transform matrix inequalities into LMIs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Change of Variables \\[1, pp. 100--101\\], \\[4, Sec. 12.3.1\\]", "weight": 1.0} -->

A BMI can sometimes be converted into an LMI using a change of variables.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

is bilinear in the variables $\mathbf{Q}$ and $\mathbf{K}$. Define a change of variable as $\mathbf{F} = {\mathbf{K}\mathbf{Q}}$ to obtain

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

which is an LMI in the variables $\mathbf{Q}$ and $\mathbf{F}$. Once this LMI is solved, the original variable can be recovered by $\mathbf{K} = {\mathbf{F}\mathbf{Q}}^{- \mathbf{1}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

It is important that a change of variables is chosen to be a one-to-one mapping in order for the new matrix inequality to be equivalent to the original matrix inequality. In Example 2.1 the change of variable $\mathbf{F} = {\mathbf{K}\mathbf{Q}}$ is a one-to-one mapping since $\mathbf{Q}^{- \mathbf{1}}$ is invertible, which gives a unique solution for the reverse change of variable $\mathbf{K} = {\mathbf{F}\mathbf{Q}}^{- \mathbf{1}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 2.2", "weight": 1.0} -->

is linear in the variable $\mathbf{V}$ and bilinear in the variable pair $(\mathbf{P},\mathbf{K})$. Choose the matrix $\mathbf{W} = {\text{diag}{\{\mathbf{P}^{- \mathbf{1}},\mathbf{V}^{- \mathbf{1}}\}}}$ to obtain an equivalent BMI given by

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 2.2", "weight": 1.0} -->

which is an LMI in the variables $\mathbf{X}$, $\mathbf{U}$, and $\mathbf{F}$. Once (2.2) is solved, the original variable $\mathbf{K}$ is recovered by the reverse change of variable $\mathbf{K} = {\mathbf{F}\mathbf{U}}^{- \mathbf{1}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 2.2", "weight": 1.0} -->

A congruence transformation preserves the definiteness of a matrix by ensuring that $\mathbf{Q} < \mathbf{0}$ and ${\mathbf{W}\mathbf{Q}\mathbf{W}}^{\mathsf{T}} < \mathbf{0}$ are equivalent. A congruence transformation is related, but not equivalent to a similarity transformation ${\mathbf{T}\mathbf{Q}\mathbf{T}}^{- \mathbf{1}}$, which preserves not only the definiteness, but also the eigenvalues of a matrix. A congruence transformation is equivalent to a similarity transformation in the special case when $\mathbf{W}^{\mathsf{T}} = \mathbf{W}^{- \mathbf{1}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Schur Complement Lemma-Based Properties", "weight": 1.0} -->

If the two matrix inequalities in (2.6) hold, then a solution to (2.5) is given by

<!-- chunk {"id": "body-0049", "role": "body", "section": "Young's Relation", "weight": 1.0} -->

is known as Young's relation or Young's inequality.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Young's Relation", "weight": 1.0} -->

Young's relation can be derived from a completion of the squares as follows.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Proof. Substituting $\mathbf{S} = {\epsilon\mathbf{1}}$ into (2.27 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) yields

<!-- chunk {"id": "body-0052", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Substituting (2.30 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) into (2.29 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) yields (2.28 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$

<!-- chunk {"id": "body-0053", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Proof. Expanding the left-hand side of (2.31 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) yields

<!-- chunk {"id": "body-0054", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

From Young's relation it can be shown that

<!-- chunk {"id": "body-0055", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Substituting (2.33 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) into (2.32 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) gives (2.31 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$

<!-- chunk {"id": "body-0056", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Consider $\mathbf{X}$, $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{S} > \mathbf{0}$. A special case of (2.31 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) with $\mathbf{F} = \mathbf{S}$ is given by

<!-- chunk {"id": "body-0057", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Adding $\mathbf{X}^{\mathsf{T}}\mathbf{P}^{- \mathbf{1}}\mathbf{X}$ to both sides of the inequality and rearranging gives

<!-- chunk {"id": "body-0058", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Using the matrix inversion lemma \[7, p. 304\], it is known that

<!-- chunk {"id": "body-0059", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Substituting (2.36 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) into (2.35 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), factoring the left side of the inequality, and knowing ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \leq \mathbf{1}$ gives (2.34 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$

<!-- chunk {"id": "body-0060", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Adding $\mathbf{X}^{\mathsf{T}}{\mathbf{P}\mathbf{X}}$ to both sides of the inequality and rearranging gives

<!-- chunk {"id": "body-0061", "role": "body", "section": "Special Cases of Young's Relation", "weight": 1.0} -->

Factoring the left side of the inequality and knowing ${\mathbf{F}^{\mathsf{T}}\mathbf{F}} \geq \mathbf{1}$ gives (2.37 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). $\square$

<!-- chunk {"id": "body-0062", "role": "body", "section": "Young's Relation-Based Properties", "weight": 1.0} -->

is satisfied if there exists $\lambda \in {\mathbb{R}}_{> 0}$ such that

<!-- chunk {"id": "body-0063", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Iterative convex overbounding is a technique based on Young's relation that is useful when solving an optimization problem with a BMI constraint.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Suppose that $\mathbf{S}_{\mathbf{0}}$ and $\mathbf{R}_{\mathbf{0}}$ are known to satisfy (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")). The BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI

<!-- chunk {"id": "body-0065", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Alternatively, the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI

<!-- chunk {"id": "body-0066", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Again, the LMI of (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is equivalent to the BMI of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, and is therefore non-conservative for values of $\mathbf{R}$ and $\mathbf{S}$ and are close to the previously known solutions $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

A benefit of convex overbounding compared to a linearization approach, is that in addition to ensuring conservatism or error is reduced in the neighborhood of $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$, the LMIs of (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) imply (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Iterative convex overbounding is particularly useful when used to solve an optimization problem with BMI constraints. For example, choose $\mathbf{R}_{\mathbf{0}}$ and $\mathbf{S}_{\mathbf{0}}$ that are initial feasible solutions to (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

Then solve for $\mathbf{R}$ and $\mathbf{S}$ that minimize a specified objective function and satisfy (2.39 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) or (2.40 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), which imply (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) without conservatism when $\mathbf{R} = \mathbf{R}_{\mathbf{0}}$ and $\mathbf{S} = \mathbf{S}_{\mathbf{0}}$. Set $\mathbf{R}_{\mathbf{0}} = \mathbf{R}$ and $\mathbf{S}_{\mathbf{0}} = \mathbf{S}$, and repeat until the objective function meets a specified stopping criteria.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Iterative Convex Overbounding", "weight": 1.0} -->

The benefits of this procedure are that its individual steps are convex optimization problems with very little conservatism in the neighborhood of the solution from the previous iteration, and that it tends to converge quickly to a solution. However, there is no guarantee that the method will converge to even a local solution.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

Consider a special case of (2.38 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) given by

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

where $\mathbf{Q} \in {\mathbb{S}}^{\mathbf{n}}$, $\mathbf{R} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{m}}$, and $\mathbf{S} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. The BMI of (2.41 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

where $\mathbf{W} > \mathbf{0}$ is an arbitrary matrix. Alternatively, the BMI of (2.41 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) is implied by the LMI

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

where $\mathbf{Z} > \mathbf{0}$ is an arbitrary matrix.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Projection Lemma-Based Properties", "weight": 1.0} -->

If the matrices $\mathbf{J}$ and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.43 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.44 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Projection Lemma-Based Properties", "weight": 1.0} -->

If the matrices $\mathbf{J}$ and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.45 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.46 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Projection Lemma-Based Properties", "weight": 1.0} -->

If the matrices $\mathbf{J}_{\mathbf{1}}$, $\mathbf{J}_{\mathbf{2}}$, and $\mathbf{G}$ are free (i.e., they are design variables), then the matrix inequalities (2.47 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) and (2.48 ‣ 2 LMI Properties and Tricks ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) are equivalent.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Finsler's Lemma \\[1, pp. 22--23\\], \\[4, Sec. 12.3.5\\],", "weight": 1.0} -->

if and only if there exists $\sigma$ such that

<!-- chunk {"id": "body-0079", "role": "body", "section": "Alternative Form of Finsler's Lemma, \\[87, pp. 90--97\\], \\[88, pp. 41--48\\]", "weight": 1.0} -->

There exists $\sigma \in {\mathbb{R}}$ such that

<!-- chunk {"id": "body-0080", "role": "body", "section": "Modified Finsler's Lemma \\[72, p. 37\\],", "weight": 1.0} -->

if and only if there exists $\epsilon$ such that

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

The Schur complement, Young's relation, and the projection lemma are three of the most common tools used to transform a BMI into an LMI. The sign of the BMI determines which one is suitable to transform the BMI into an LMI. For example, consider the case of a BMI in the variable $\mathbf{Y} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$ of the form

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

This LMI can also be written as

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

Notice that the Projection Lemma gives two matrix inequalities that do not depend on the variable $\mathbf{Y}$. This is why the Projection Lemma is also known as the Matrix Elimination Lemma.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

which implies the BMI of (2.53). Notice that (2.54) involves a new variable $\mathbf{X} \in {\mathbb{R}}^{\mathbf{m} \times \mathbf{n}}$. Using the Schur complement on (2.54) yields

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

which is an LMI in $\mathbf{Y}$ for a fixed $\mathbf{X}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

It is desirable to use the Schur complement of the Projection Lemma over Young's relation whenever possible, as they provides an LMI or LMIs that are equivalent to the original BMI. When using Young's relation, the resulting LMI implies the original BMI, but is not equivalent. This introduces conservatism into an optimization problem.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

If a previously-known solution $\mathbf{Y}_{\mathbf{0}}$ to (2.53) is available, then convex overbounding can be used to reduce conservatism in the neighborhood of $\mathbf{Y}_{\mathbf{0}}$. The BMI of (2.53) is equivalent to the BMI

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion on the Schur Complement, Young's Relation, Convex Overbounding, and the Projection Lemma", "weight": 1.5} -->

The LMI of (2.56) is in general conservative, but this conservatism disappears when $\mathbf{Y} = \mathbf{Y}_{\mathbf{0}}$ and is reduced when $\mathbf{Y}$ is close to $\mathbf{Y}_{\mathbf{0}}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Dilation", "weight": 1.0} -->

Matrix inequalities can be dilated to obtain a larger matrix inequality, often with additional design variables. This can be a useful technique to separate design variables in a BMI.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Dilation", "weight": 1.0} -->

A common technique to dilate an LMI involves the use the projection lemma in reverse or the reciprocal projection lemma. For instance, consider the following example taken from and inspired by the dilated bounded real lemma matrix inequality in \[5, pp. 153--155\] involving the matrices $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$ and $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$. The matrix inequality

<!-- chunk {"id": "body-0091", "role": "body", "section": "Dilation", "weight": 1.0} -->

Since $\mathbf{P} > \mathbf{0}$, it is also known that

<!-- chunk {"id": "body-0092", "role": "body", "section": "Dilation", "weight": 1.0} -->

The matrix inequalities in (2.58) and (2.59) are in the form of the strict projection lemma. Specifically, (2.58) is in the form of ${\mathbf{N}_{\mathbf{G}}^{\mathsf{T}}{(\mathbf{A})}\mathbf{\Phi}{(\mathbf{P})}\mathbf{N}_{\mathbf{G}}{(\mathbf{A})}} < \mathbf{0}$, where

<!-- chunk {"id": "body-0093", "role": "body", "section": "Dilation", "weight": 1.0} -->

The projection lemma states that (2.58) and (2.59) are equivalent to

<!-- chunk {"id": "body-0094", "role": "body", "section": "Dilation", "weight": 1.0} -->

the matrix inequality of (2.60) can be rewritten as

<!-- chunk {"id": "body-0095", "role": "body", "section": "Dilation", "weight": 1.0} -->

Therefore, the matrix inequality of (2.58) with $\mathbf{P} > \mathbf{0}$ is equivalent to the dilated matrix inequality of (2.61).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Examples of Dilated Matrix Inequalities", "weight": 1.0} -->

Examples of some useful dilated matrix inequalities are presented here, while dilated forms of a number of important matrix inequalities are included as equivalent matrix inequalities in their respective sections.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Example 2.5", "weight": 1.0} -->

which is satisfied based on the definition of $\mathbf{R}$. By the dualization lemma, (2.64) is satisfied with $\mathbf{R} \geq \mathbf{0}$ if and only if

<!-- chunk {"id": "body-0098", "role": "body", "section": "Condition Number of a Matrix \\[1, pp. 37--38\\]", "weight": 1.0} -->

If $n \leq m$, the inequality ${\kappa{(\mathbf{A})}} \leq \gamma$ holds if there exists $\mu$ such that

<!-- chunk {"id": "body-0099", "role": "body", "section": "Spectral Radius \\[8, p. 17\\]", "weight": 1.0} -->

Consider $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$ and $\delta \in {\mathbb{R}}_{> 0}$. The spectral radius of $\mathbf{A}$ is strictly less than $\delta$ (i.e., ${\rho{(\mathbf{A})}} < \delta$) under either of the following necessary and sufficient conditions.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Spectral Radius \\[8, p. 17\\]", "weight": 1.0} -->

Also see Section 3.25 for a similar condition related to the structured singular value.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Trace of a Matrix with a Slack Variable", "weight": 1.0} -->

is satisfied if and only if there exists $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{n}}$ such that

<!-- chunk {"id": "body-0102", "role": "body", "section": "Trace of a Matrix with a Slack Variable", "weight": 1.0} -->

is satisfied if and only if there exists $\mathbf{Z} \in {\mathbb{S}}^{\mathbf{m}}$ such that

<!-- chunk {"id": "body-0103", "role": "body", "section": "Quadratic Inequalities", "weight": 1.0} -->

\[7, p. 731\] Consider $\mathbf{x} \in {\mathbb{R}}^{\mathbf{n}}$. The matrix inequality given by

<!-- chunk {"id": "body-0104", "role": "body", "section": "Miscellaneous Properties and Results", "weight": 1.0} -->

Moreover, the following statements hold.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Lyapunov Stability \\[7, pp. 1201--1203\\], \\[1, pp. 20--21\\]", "weight": 1.0} -->

The matrix inequality of (3.1) is satisfied under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Asymptotic Stability \\[7, p. 1201--1203\\], \\[1, p. 2\\]", "weight": 1.0} -->

The matrix inequality of (3.2) is satisfied and the matrix $\mathbf{A}$ is Hurwitz under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discrete-Time Lyapunov Stability \\[7, pp. 1203--1204\\]", "weight": 1.0} -->

The matrix inequality of (3.8) is satisfied and the eigenvalues of $\mathbf{A}_{d}$ satisfy $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| \leq 1$, $i = {1,\ldots,n}$ under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discrete-Time Asymptotic Stability \\[7, pp. 1203--1204\\], \\[5, pp. 97--98\\]", "weight": 1.0} -->

The matrix inequality of (3.9) is satisfied and the eigenvalues of $\mathbf{A}_{d}$ satisfy $\left| {\lambda_{i}{(\mathbf{A}_{d})}} \right| < 1$, $i = {1,\ldots,n}$ under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Descriptor System Admissibility", "weight": 1.0} -->

Consider the descriptor system given by ${\mathbf{E}\overset{˙}{\mathbf{x}}} = {\mathbf{A}\mathbf{x}}$, where $\mathbf{E}$, $\mathbf{A} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The descriptor system is admissible under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Discrete-Time Descriptor System Admissibility", "weight": 1.0} -->

Consider the discrete-time descriptor system given by ${\mathbf{E}_{d}\mathbf{x}_{\mathbf{k} + \mathbf{1}}} = {\mathbf{A}_{d}\mathbf{x}_{\mathbf{k}}}$, where $\mathbf{E}_{d}$, $\mathbf{A}_{d} \in {\mathbb{R}}^{\mathbf{n} \times \mathbf{n}}$. The discrete-time descriptor system is admissible under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Continuous-Time Bounded Real Lemma, \\[121, pp. 85--86\\]", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Discrete-Time Bounded Real Lemma", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Descriptor System Bounded Real Lemma", "weight": 1.0} -->

The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Discrete-Time Descriptor System Bounded Real Lemma", "weight": 1.0} -->

Consider a discrete-time descriptor system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, described by

<!-- chunk {"id": "body-0115", "role": "body", "section": "Discrete-Time Descriptor System Bounded Real Lemma", "weight": 1.0} -->

The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{\infty} < \gamma$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Continuous-Time $\\mathcal{H}_{2}$ Norm", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Continuous-Time $\\mathcal{H}_{2}$ Norm", "weight": 1.0} -->

The $\mathcal{H}_{2}$ norm of $\mathcal{G}$ is the minimum value of $\mu \in {\mathbb{R}}_{> 0}$ that satisfies any of the above conditions.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$ Norm Without Feedthrough", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$ Norm With Feedthrough", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Descriptor System $\\mathcal{H}_{2}$ Norm", "weight": 1.0} -->

The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Discrete-Time Descriptor System $\\mathcal{H}_{2}$ Norm", "weight": 1.0} -->

Consider a discrete-time descriptor system, ${\mathcal{G}}:{\ell_{2e}\rightarrow\ell_{2e}}$, described by

<!-- chunk {"id": "body-0122", "role": "body", "section": "Discrete-Time Descriptor System $\\mathcal{H}_{2}$ Norm", "weight": 1.0} -->

The descriptor system is admissible and the inequality $\left\| {\mathcal{G}} \right\|_{2} < \mu$ holds under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Generalized $\\mathcal{H}_{2}$ Norm (Induced $\\mathcal{L}_{2}$-$\\mathcal{L}_{\\infty}$ Norm)", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{2,\infty} < \mu$ holds under any of following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Peak-to-Peak Norm (Induced $\\mathcal{L}_{\\infty}$-$\\mathcal{L}_{\\infty}$ Norm) \\[3, pp. 74--75\\],", "weight": 1.0} -->

The inequality $\left\| {\mathcal{G}} \right\|_{\infty,\infty} < \mu$ holds under any of the following equivalent sufficient conditions.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Peak-to-Peak Norm (Induced $\\mathcal{L}_{\\infty}$-$\\mathcal{L}_{\\infty}$ Norm) \\[3, pp. 74--75\\],", "weight": 1.0} -->

The peak-to-peak norm of $\mathcal{G}$ is smaller than any $\mu \in {\mathbb{R}}_{> 0}$ that satisfies either of the above conditions.

<!-- chunk {"id": "body-0126", "role": "body", "section": "KYP Lemma for QSR Dissipative Systems", "weight": 1.0} -->

Note that the Bounded Real Lemma (Section 3.2.1) is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {- \mathbf{1}}$, $\mathbf{S} = \mathbf{0}$, and $\mathbf{R} = {\gamma^{\mathbf{2}}\mathbf{1}}$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Discrete-Time KYP Lemma for QSR Dissipative Systems, \\[151, p. 495\\]", "weight": 1.0} -->

Note that the Discrete-Time Bounded Real Lemma (Section 3.2.2) is a special case of the Discrete-Time KYP Lemma for QSR dissipative systems with $\mathbf{Q} = {- \mathbf{1}}$, $\mathbf{S} = \mathbf{0}$, and $\mathbf{R} = {\gamma^{\mathbf{2}}\mathbf{1}}$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "KYP (Positive Real) Lemma Without Feedthrough \\[152, p. 219\\] \\[154, p. 14\\]", "weight": 1.0} -->

This is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = \mathbf{0}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "KYP (Positive Real) Lemma Without Feedthrough \\[152, p. 219\\] \\[154, p. 14\\]", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly positive real (SPR) under either of the following necessary and sufficient conditions.

<!-- chunk {"id": "body-0130", "role": "body", "section": "KYP (Positive Real) Lemma With Feedthrough \\[1, p. 25\\], \\[152, p. 218\\] \\[155, pp. 79--80\\]", "weight": 1.0} -->

This is a special case of the KYP Lemma for QSR dissipative systems with $\mathbf{Q} = \mathbf{0}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$.

<!-- chunk {"id": "body-0131", "role": "body", "section": "KYP (Positive Real) Lemma With Feedthrough \\[1, p. 25\\], \\[152, p. 218\\] \\[155, pp. 79--80\\]", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly positive real (SPR) under either of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Discrete-Time KYP (Positive Real) Lemma With Feedthrough \\[155, pp. 171--172\\]", "weight": 1.0} -->

This is a special case of the Discrete-Time KYP Lemma for QSR dissipative systems with $\mathbf{Q} = \mathbf{0}$, $\mathbf{S} = {\frac{1}{2} \cdot \mathbf{1}}$, and $\mathbf{R} = \mathbf{0}$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Discrete-Time KYP (Positive Real) Lemma With Feedthrough \\[155, pp. 171--172\\]", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly positive real (SPR) under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0134", "role": "body", "section": "KYP Lemma for Descriptor Systems \\[155, pp. 91--93\\],", "weight": 1.0} -->

Consider a square, LTI descriptor system given by

<!-- chunk {"id": "body-0135", "role": "body", "section": "Discrete-Time KYP Lemma for Descriptor Systems", "weight": 1.0} -->

Consider a square, discrete-time LTI descriptor system given by

<!-- chunk {"id": "body-0136", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

The system $\mathcal{G}$ is inside the cone $\lbrack a,b\rbrack$, where $a$, $b \in {\mathbb{R}}$, and $a < b$, under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

Note that the matrix inequality of (3.50) does not allow for the case where the upper bound $b$ is infinite.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

The system $\mathcal{G}$ is inside the cone of radius $r$ centered at $c$, where $r \in {\mathbb{R}}_{> 0}$ and $b \in {\mathbb{R}}$, under any of the following equivalent necessary and sufficient conditions.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Conic Sector Lemma", "weight": 1.0} -->

Note that the matrix inequality of (3.51) does not allow for the case where the upper bound $b$ is infinite.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

where $a \in {\mathbb{R}}$, $b \in {\mathbb{R}}_{> 0}$, and $a < b$. The following generalized KYP Lemmas give conditions for $\mathcal{G}$ to be inside the cone $\lbrack a,b\rbrack$ within finite frequency bandwidths.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

If $\omega_{1}\rightarrow\infty$, $\mathbf{P} > \mathbf{0}$, and $\mathbf{Q} = \mathbf{0}$, then the traditional Conic Sector Lemma is recovered.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

The parameter ${\overline{\omega}}_{1}$ is included in (3.56 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) to effectively transform $|\omega| \leq {({\omega_{1} - {\overline{\omega}}_{1}})}$ into the strict inequality $|\omega| < \omega_{1}$.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

The parameter ${\overline{\omega}}_{2}$ is included in (3.57 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) to effectively transform $\omega_{1} \leq |\omega| \leq {({\omega_{2} - {\overline{\omega}}_{2}})}$ into the strict inequality $\omega_{1} \leq |\omega| < \omega_{2}$.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Generalized KYP (GKYP) Lemma for Conic Sectors", "weight": 1.0} -->

If $(\mathbf{A},{\mathbf{B}_{,}\mathbf{C}},\mathbf{D})$ is a minimal realization, then the matrix inequalities in (3.56 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), (3.57 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")), and (3.58 Lemma for Conic Sectors ‣ 3.7 Conic Sectors ‣ 3 LMIs in Systems and Stability Theory ‣ LMI Properties and Applications in Systems, Stability, and Control Theory")) can be nonstrict.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Minimum Gain Lemma", "weight": 1.0} -->

If $\mathcal{G}$ is a square system (i.e., $m = p$) or ${\text{span}{(\mathbf{C})}} \subseteq {\text{span}{(\mathbf{D})}}$, then the preceding conditions are necessary and sufficient for $\mathcal{G}$ to have minimum gain $\nu \in {\mathbb{R}}_{\geq 0}$. The minimum gain lemma is a special case of the exterior conic sector lemma with $a = {- \nu}$ and $b = \nu$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Minimum Gain Lemma", "weight": 1.0} -->

The system $\mathcal{G}$ also has minimum gain $\nu$ under any of the following sufficient conditions.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Negative Imaginary Lemma", "weight": 1.0} -->

The system $\mathcal{G}$ is strictly negative imaginary if ${\det{(\mathbf{A})}} \neq \mathbf{0}$ and either (3.76) is satisfied with $\mathbf{P} > \mathbf{0}$ or (3.77) is satisfied with $\mathbf{Q} > \mathbf{0}$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Generalized Negative Imaginary Lemma", "weight": 1.0} -->

The following generalized KYP Lemmas give conditions for $\mathcal{G}$ to be negative imaginary within finite frequency bandwidths.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Generalized Negative Imaginary Lemma", "weight": 1.0} -->

If $\omega_{1}\rightarrow\infty$, $\mathbf{P} > \mathbf{0}$, and $\mathbf{Q} = \mathbf{0}$, then the traditional Negative Imaginary Lemma is recovered.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Algebraic Riccati Inequality", "weight": 1.0} -->

can be rewritten using the Schur complement lemma as

<!-- chunk {"id": "body-0151", "role": "body", "section": "Discrete-Time Algebraic Riccati Inequality", "weight": 1.0} -->

can be rewritten using the Schur complement lemma as

<!-- chunk {"id": "body-0152", "role": "body", "section": "Discrete-Time Algebraic Riccati Inequality", "weight": 1.0} -->

Equivalently, this discrete-time algebraic Riccati inequality is satisfied under any of the following necessary and sufficient conditions.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Continuous-Time Strong Stabilizability", "weight": 1.0} -->

Moreover, a controller that strongly stabilizes $\mathcal{G}$ is given by the state-space realization

<!-- chunk {"id": "body-0154", "role": "body", "section": "Discrete-Time Strong Stabilizability", "weight": 1.0} -->

Moreover, a discrete-time controller that strongly stabilizes $\mathcal{G}$ is given by the state-space realization

<!-- chunk {"id": "body-0155", "role": "body", "section": "System Zeros with Feedthrough", "weight": 1.0} -->

If the system is square ($m = p$), then $\mathbf{D}$ full rank implies $\mathbf{D}^{- \mathbf{1}}$ exists and (3.89) simplifies to

<!-- chunk {"id": "body-0156", "role": "body", "section": "Discrete-Time System Zeros with Feedthrough", "weight": 1.0} -->

If the system is square ($m = p$), then $\mathbf{D}_{d}$ full rank implies $\mathbf{D}_{d}^{- \mathbf{1}}$ exists and (3.99) simplifies to

<!-- chunk {"id": "body-0157", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Stability \\[5, pp. 107--108\\],", "weight": 1.0} -->

The matrix $\mathbf{A}$ is $\mathcal{D}$-stable if and only if any of the following equivalent conditions are satisfied.

<!-- chunk {"id": "body-0158", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Stability \\[5, pp. 107--108\\],", "weight": 1.0} -->

where $\otimes$ is the Kroenecker product.

<!-- chunk {"id": "body-0159", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Stability \\[5, pp. 107--108\\],", "weight": 1.0} -->

Alternatively, consider the LMI region $\mathcal{D}$ of the complex plane defined by \[3, p. 66\]

<!-- chunk {"id": "body-0160", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Admissibility", "weight": 1.0} -->

The pair $(\mathbf{E},\mathbf{A})$ is $\mathcal{D}$-admissible if and only if any of the following equivalent conditions are satisfied.

<!-- chunk {"id": "body-0161", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Admissibility", "weight": 1.0} -->

where $\otimes$ is the Kroenecker product and $\mathbf{1}_{\mathbf{m}\mathbf{m}}$ is an $m \times m$ matrix filled with ones.

<!-- chunk {"id": "body-0162", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Admissibility", "weight": 1.0} -->

where $\otimes$ is the Kroenecker product and $\mathbf{1}_{\mathbf{m}\mathbf{m}}$ is an $m \times m$ matrix filled with ones.

<!-- chunk {"id": "body-0163", "role": "body", "section": "General LMI Region $\\mathcal{D}$-Admissibility", "weight": 1.0} -->

where $\otimes$ is the Kroenecker product and $\mathbf{1}_{\mathbf{m}\mathbf{m}}$ is an $m \times m$ matrix filled with ones.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Circular Region", "weight": 1.0} -->

where $\mathbf{E}^{\dagger}$ is the pseudoinverse of $\mathbf{E}$. The region $\mathcal{D}$ describes a circular region of the complex plane with radius $r = \sqrt{{- {a/d}} + {b^{2}/d^{2}}}$ centered at $(c,0)$, where $c = {- {b/d}}$.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Transient State Bound for Autonomous LTI Systems \\[1, p. 88\\],", "weight": 1.0} -->

Consider the continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0166", "role": "body", "section": "Transient State Bound for Discrete-Time Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0167", "role": "body", "section": "Transient State Bound for Non-Autonomous LTI Systems \\[1, p. 77--78\\]", "weight": 1.0} -->

Consider the continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0168", "role": "body", "section": "Transient State Bound for Discrete-Time Non-Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0169", "role": "body", "section": "Transient Output Bound for Autonomous LTI Systems \\[1, p. 88\\],", "weight": 1.0} -->

Consider the continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0170", "role": "body", "section": "Transient Output Bound for Discrete-Time Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0171", "role": "body", "section": "Transient Output Bound for Non-Autonomous LTI Systems", "weight": 1.0} -->

Consider the continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0172", "role": "body", "section": "Transient Output Bound for Discrete-Time Non-Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0173", "role": "body", "section": "Transient Impulse Response Bound", "weight": 1.0} -->

Consider the single-input multi-output continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0174", "role": "body", "section": "Discrete-Time Transient Impulse Response Bound", "weight": 1.0} -->

Consider the single-input multi-output discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0175", "role": "body", "section": "Output Energy Bound for Autonomous LTI Systems \\[1, pp. 85--86\\]", "weight": 1.0} -->

Consider the continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0176", "role": "body", "section": "Output Energy Bound for Discrete-Time Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0177", "role": "body", "section": "Output Energy Bound for Non-Autonomous LTI Systems", "weight": 1.0} -->

Consider the continuous-time LTI system with state-space realization

<!-- chunk {"id": "body-0178", "role": "body", "section": "Output Energy Bound for Discrete-Time Non-Autonomous LTI Systems", "weight": 1.0} -->

Consider the discrete-time LTI system with state-space realization

<!-- chunk {"id": "body-0179", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

Consider the uncertain continuous-time linear system with state-space representation

<!-- chunk {"id": "body-0180", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

The following statements can be made for particular sets of perturbations.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

Consider the case where the set of perturbation parameters is defined by a regular polyhedron as

<!-- chunk {"id": "body-0182", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0183", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

Consider the case where the set of perturbation parameters is defined by a polytope as

<!-- chunk {"id": "body-0184", "role": "body", "section": "Continuous-Time Quadratic Stability \\[5, pp. 112--115\\]", "weight": 1.0} -->

The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0185", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

Consider the uncertain discrete-time linear system with state-space representation

<!-- chunk {"id": "body-0186", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

The following statements can be made for particular sets of perturbations.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

Consider the case where the set of perturbation parameters is defined by a regular polyhedron as

<!-- chunk {"id": "body-0188", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0189", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

Consider the case where the set of perturbation parameters is defined by a polytope as

<!-- chunk {"id": "body-0190", "role": "body", "section": "Discrete-Time Quadratic Stability \\[5, pp. 116--118\\]", "weight": 1.0} -->

The uncertain system in (3.160) is quadratically stable if and only if there exists $\mathbf{P} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0191", "role": "body", "section": "Stability of Time-Delay Systems", "weight": 1.0} -->

Consider the continuous-time linear time-delay system with state-space representation

<!-- chunk {"id": "body-0192", "role": "body", "section": "Delay-Independent Condition \\[5, p. 126\\]", "weight": 1.0} -->

The time-delay system in (3.162) is asymptotically stable if there exist $\mathbf{P}$, $\mathbf{S} \in {\mathbb{S}}^{\mathbf{n}}$, where $\mathbf{P} > \mathbf{0}$ and $\mathbf{S} > \mathbf{0}$, such that

<!-- chunk {"id": "body-0193", "role": "body", "section": "Delay-Dependent Condition \\[5, pp. 128--129\\]", "weight": 1.0} -->

The time-delay system in (3.162) is uniformly asymptotically stable if there exists $\mathbf{X} \in {\mathbb{S}}^{\mathbf{n}}$ and $\beta \in {\mathbb{R}}_{> 0}$, where $\mathbf{X} > \mathbf{0}$ and $\beta < 1$, such that

<!-- chunk {"id": "body-0194", "role": "body", "section": "Static Output Feedback Algebraic Loop\\[7, p. 1284\\], \\[175, pp. 39--40\\]", "weight": 1.0} -->

Consider a continuous-time LTI system, ${\mathcal{G}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, with state-space realization

<!-- chunk {"id": "body-0195", "role": "body", "section": "Static Output Feedback Algebraic Loop\\[7, p. 1284\\], \\[175, pp. 39--40\\]", "weight": 1.0} -->

The change of variable $\overline{\mathbf{K}} = {\left( {\mathbf{1} - {\mathbf{K}\mathbf{D}}_{\mathbf{2}\mathbf{2}}} \right)^{- 1}\mathbf{K}}$ allows for the simplification of matrix inequalities involving the closed-loop system.

<!-- chunk {"id": "body-0196", "role": "body", "section": "LMIs in Optimal Control", "weight": 1.0} -->

This section presents controller synthesis methods using LMIs for a number of well-known optimal control problems. The derivation of the LMIs used for controller synthesis is provided in some cases, while longer derivations can be found in the cited references.

<!-- chunk {"id": "body-0197", "role": "body", "section": "The Continuous-Time Generalized Plant", "weight": 1.0} -->

Consider the generalized LTI plant ${\mathcal{P}}:{\mathcal{L}_{2e}\rightarrow\mathcal{L}_{2e}}$, shown in Figure 1, with a minimal state-space realization \[7, pp. 1291--1292\], \[4, Section 3.8\], \[200, p. 141\], \[201, pp. 14--16\], \[202, pp. 809--817\]

<!-- chunk {"id": "body-0198", "role": "body", "section": "The Continuous-Time Generalized Plant", "weight": 1.0} -->

The generalized plant, also known as the standard control problem in \[7, pp. 1291--1292\], \[201, pp. 14--16\] is useful, as it is possible to represent a number of LTI systems in this form, as shown in the following example.

<!-- chunk {"id": "body-0199", "role": "body", "section": "The Discrete-Time Generalized Plant", "weight": 1.0} -->

The discrete-time generalized LTI plant ${\mathcal{P}}:{\ell_{2e}\rightarrow\ell_{2e}}$, shown in Figure 1, is described by the state-space realization

<!-- chunk {"id": "body-0200", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Control", "weight": 1.0} -->

The goal of $\mathcal{H}_{2}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0201", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Full-State Feedback Control \\[5, pp. 257--258\\]", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0202", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Full-State Feedback Control \\[5, pp. 257--258\\]", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}$,$\mathbf{B}_{\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}$ to the performance output $\mathbf{z}$. Substituting the full-state feedback controller into (4.1) and (4.2) yields

<!-- chunk {"id": "body-0203", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Full-State Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0204", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization

<!-- chunk {"id": "body-0205", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

<!-- chunk {"id": "body-0206", "role": "body", "section": "Synthesis Method 4.3", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0208", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

A discrete-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{d\mathbf{c}},\mathbf{B}_{d\mathbf{c}},\mathbf{C}_{d\mathbf{c}},\mathbf{D}_{d\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{2}$ norm of the closed-loop system transfer matrix from $\mathbf{w}_{\mathbf{k}}$ to $\mathbf{z}_{\mathbf{k}}$, given by

<!-- chunk {"id": "body-0209", "role": "body", "section": "Synthesis Method 4.4", "weight": 1.0} -->

Given $\mathbf{G}$ and $\mathbf{H}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Synthesis Method 4.4", "weight": 1.0} -->

The LMI in (4.9) is derived from the LMI in Theorem 7 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix

<!-- chunk {"id": "body-0211", "role": "body", "section": "Synthesis Method 4.4", "weight": 1.0} -->

Similarly, the LMI in (4.10) is derived from the LMI in Theorem 7 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix

<!-- chunk {"id": "body-0212", "role": "body", "section": "Synthesis Method 4.5", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Synthesis Method 4.5", "weight": 1.0} -->

The LMIs in (4.12) and (4.13) are derived from (4.9) and (4.10) using the change of variables $\mathbf{S} = \mathbf{J} = \mathbf{1}$, $\mathbf{H} = \mathbf{X}_{\mathbf{1}}$, $\mathbf{G} = \mathbf{Y}_{\mathbf{1}}$. The LMI in (4.14) is added to ensure that ${\mathbf{1} - {\mathbf{X}_{\mathbf{1}}\mathbf{Y}_{\mathbf{1}}}} \geq \mathbf{0}$ in a similar fashion to the approach used.

<!-- chunk {"id": "body-0214", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Control", "weight": 1.0} -->

The goal of $\mathcal{H}_{\infty}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0215", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control \\[5, pp. 251--252\\]", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0216", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control \\[5, pp. 251--252\\]", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}$,$\mathbf{B}_{\mathbf{2}}$) is stabilizable. A full-state feedback controller ${\mathcal{K}} = \mathbf{K} \in {\mathbb{R}}^{\mathbf{n}_{\mathbf{u}} \times \mathbf{n}_{\mathbf{x}}}$ (i.e., $\mathbf{u} = {\mathbf{K}\mathbf{x}}$) is to be designed to minimize $\mathcal{H}_{\infty}$ norm of the closed loop transfer matrix from the exogenous input $\mathbf{w}$ to the performance output $\mathbf{z}$. Substituting the full-state feedback controller into (4.15) and (4.16) yields

<!-- chunk {"id": "body-0217", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control \\[5, pp. 251--252\\]", "weight": 1.0} -->

From the Bounded Real Lemma in Section 3.2.1, the $\mathcal{H}_{\infty}$ of the closed-loop system is the minimum value of $\gamma \in {\mathbb{R}}_{> 0}$ that satisfies

<!-- chunk {"id": "body-0218", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0219", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization

<!-- chunk {"id": "body-0220", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

A continuous-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{\mathbf{c}},\mathbf{B}_{\mathbf{c}},\mathbf{C}_{\mathbf{c}},\mathbf{D}_{\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

<!-- chunk {"id": "body-0221", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Two different synthesis methods for the $\mathcal{H}_{\infty}$-optimal dynamic output feedback control problem are presented as follows.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Synthesis Method 4.8", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Synthesis Method 4.9", "weight": 1.0} -->

,\[2, pp. 224--232\] The controller is solved for in the following two steps.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization

<!-- chunk {"id": "body-0225", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

A discrete-time dynamic output feedback LTI controller with state-space realization $(\mathbf{A}_{d\mathbf{c}},\mathbf{B}_{d\mathbf{c}},\mathbf{C}_{d\mathbf{c}},\mathbf{D}_{d\mathbf{c}})$ is to be designed to minimize the $\mathcal{H}_{\infty}$ norm of the closed-loop system transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

<!-- chunk {"id": "body-0226", "role": "body", "section": "Synthesis Method 4.10", "weight": 1.0} -->

Given $\mathbf{G}$ and $\mathbf{H}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Synthesis Method 4.10", "weight": 1.0} -->

The LMI in (4.20) is derived from the LMI in Theorem 8 of by performing a congruence transformation involving a multiplication on the left and right by the symmetric matrix

<!-- chunk {"id": "body-0228", "role": "body", "section": "Synthesis Method 4.11", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Control", "weight": 1.0} -->

The goal of mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal control is to design a controller that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{1}}$ to $\mathbf{z}_{\mathbf{1}}$, while ensuring that the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer function from $\mathbf{w}_{\mathbf{2}}$ to $\mathbf{z}_{\mathbf{2}}$ is below a specified bound.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control \\[5, pp. 329--330\\]", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0231", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Full-State Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0232", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the continuous-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization

<!-- chunk {"id": "body-0233", "role": "body", "section": "Synthesis Method 4.14", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Dynamic Output Feedback Control", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with minimal state-space realization

<!-- chunk {"id": "body-0235", "role": "body", "section": "Synthesis Method 4.15", "weight": 1.0} -->

Given $\mathbf{X}_{\mathbf{1}}$ and $\mathbf{Y}_{\mathbf{1}}$, the matrices $\mathbf{X}_{\mathbf{2}}$ and $\mathbf{Y}_{\mathbf{2}}$ can be found using a matrix decomposition, such as a LU decomposition or a Cholesky decomposition.

<!-- chunk {"id": "body-0236", "role": "body", "section": "LMIs in Optimal Estimation and Filtering", "weight": 1.0} -->

This section presents controller synthesis methods using LMIs for a number of well-known optimal state-estimation and filtering problems. The derivation of the LMIs used for synthesis is provided in some cases, while longer derivations can be found in the cited references.

<!-- chunk {"id": "body-0237", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal State Estimation", "weight": 1.0} -->

The goal of $\mathcal{H}_{2}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0238", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0239", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form

<!-- chunk {"id": "body-0240", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

and the performance output is defined as

<!-- chunk {"id": "body-0241", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

The observer gain $\mathbf{L}$ is to be designed such that the $\mathcal{H}_{2}$ norm of the transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

<!-- chunk {"id": "body-0242", "role": "body", "section": "$\\mathcal{H}_{2}$-Optimal Observer \\[5, p. 296\\]", "weight": 1.0} -->

is minimized. Minimizing the $\mathcal{H}_{2}$ norm of the transfer matrix $\mathbf{T}{(\mathbf{s})}$ is equivalent to minimizing ${\mathcal{J}{(\mu)}} = \mu^{2}$ subject to

<!-- chunk {"id": "body-0243", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Observer", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0244", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Observer", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form

<!-- chunk {"id": "body-0245", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{2}$-Optimal Observer", "weight": 1.0} -->

and the performance output is defined as

<!-- chunk {"id": "body-0246", "role": "body", "section": "$\\mathcal{H}_{\\infty}$-Optimal State Estimation", "weight": 1.0} -->

The goal of $\mathcal{H}_{\infty}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}$ to $\mathbf{z}$.

<!-- chunk {"id": "body-0247", "role": "body", "section": "$\\mathcal{H}_{\\infty}$--Optimal Observer \\[5, p. 295\\]", "weight": 1.0} -->

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0248", "role": "body", "section": "$\\mathcal{H}_{\\infty}$--Optimal Observer \\[5, p. 295\\]", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form

<!-- chunk {"id": "body-0249", "role": "body", "section": "$\\mathcal{H}_{\\infty}$--Optimal Observer \\[5, p. 295\\]", "weight": 1.0} -->

and the performance output is defined as

<!-- chunk {"id": "body-0250", "role": "body", "section": "$\\mathcal{H}_{\\infty}$--Optimal Observer \\[5, p. 295\\]", "weight": 1.0} -->

The observer gain $\mathbf{L}$ is to be designed such that the $\mathcal{H}_{\infty}$ of the transfer matrix from $\mathbf{w}$ to $\mathbf{z}$, given by

<!-- chunk {"id": "body-0251", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$--Optimal Observer", "weight": 1.0} -->

Consider the discrete-time LTI plant $\mathcal{G}$ with state-space realization

<!-- chunk {"id": "body-0252", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$--Optimal Observer", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form

<!-- chunk {"id": "body-0253", "role": "body", "section": "Discrete-Time $\\mathcal{H}_{\\infty}$--Optimal Observer", "weight": 1.0} -->

and the performance output is defined as

<!-- chunk {"id": "body-0254", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal State Estimation", "weight": 1.0} -->

The goal of mixed $\mathcal{H}_{2}$-$\mathcal{H}_{\infty}$-optimal state estimation is to design an observer that minimizes the $\mathcal{H}_{2}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{1}}$ to $\mathbf{z}_{\mathbf{1}}$, while ensuring that the $\mathcal{H}_{\infty}$ norm of the closed-loop transfer matrix from $\mathbf{w}_{\mathbf{2}}$ to $\mathbf{z}_{\mathbf{2}}$ is below a specified bound.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

Consider the continuous-time generalized plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0256", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}$,$\mathbf{C}_{\mathbf{2}}$) is detectable. An observer of the form

<!-- chunk {"id": "body-0257", "role": "body", "section": "Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

and the performance output is defined as

<!-- chunk {"id": "body-0258", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

Consider the discrete-time generalized LTI plant $\mathcal{P}$ with state-space realization

<!-- chunk {"id": "body-0259", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

where it is assumed that ($\mathbf{A}_{d}$,$\mathbf{C}_{d\mathbf{2}}$) is detectable. An observer of the form

<!-- chunk {"id": "body-0260", "role": "body", "section": "Discrete-Time Mixed $\\mathcal{H}_{2}$-$\\mathcal{H}_{\\infty}$-Optimal Observer", "weight": 1.0} -->

and the performance output is defined as

<!-- chunk {"id": "body-0261", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

The goal of optimal filtering is to design a filter that acts on the output $\mathbf{z}$ of the generalized plant and optimizes the transfer matrix from $\mathbf{w}$ to the filtered output.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

Continuous-Time Filtering: Consider the continuous-time generalized LTI plant with minimal states-space realization

<!-- chunk {"id": "body-0263", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

where it is assumed that $\mathbf{A}$ is Hurwitz. A continuous-time dynamic LTI filter with state-space realization

<!-- chunk {"id": "body-0264", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

is to be designed to optimize the transfer function from $\mathbf{w}$ to $\overset{\sim}{\mathbf{z}} = {\mathbf{z} - \hat{\mathbf{z}}}$, given by

<!-- chunk {"id": "body-0265", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

This can alternatively be formulated as a special case of synthesizing a dynamic output "feedback" controller for the generalized plant given by

<!-- chunk {"id": "body-0266", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

The controller in this case is not truly a feedback controller, as it only appears as a feedthrough term in the performance channel. The synthesis methods presented in this subsection take advantage of this fact, resulting in a simpler formulation than applying the controller synthesis methods in Section 4.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

Discrete-Time Filtering: Consider the discrete-time generalized LTI plant with minimal states-space realization

<!-- chunk {"id": "body-0268", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

where it is assumed that $\mathbf{A}_{d}$ is Schur. A discrete-time dynamic LTI filter with state-space realization

<!-- chunk {"id": "body-0269", "role": "body", "section": "Continuous-Time and Discrete-Time Optimal Filtering", "weight": 1.0} -->

This can alternatively be formulated as a special case of synthesizing a dynamic output "feedback" controller for the generalized plant given by

<!-- chunk {"id": "body-0270", "role": "body", "section": "Synthesis Method 5.10", "weight": 1.0} -->

This synthesis method is derived from the discrete-time $\mathcal{H}_{2}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.5 using the fact that $\mathcal{H}_{2}$-optimal filter synthesis is a special case of this problem.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Synthesis Method 5.13", "weight": 1.0} -->

This synthesis method is derived from the discrete-time $\mathcal{H}_{\infty}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.11 using the fact that $\mathcal{H}_{\infty}$-optimal filter synthesis is a special case of this problem.
