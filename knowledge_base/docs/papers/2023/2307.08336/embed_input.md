<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RAYEN: Imposition of Hard Convex Constraints on Neural Networks

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the numerous applications of convex constraints in Robotics, enforcing them within learning-based frameworks remains an open challenge. Existing techniques either fail to guarantee satisfaction at all times, or incur prohibitive computational costs. This paper presents RAYEN, a framework for imposing hard convex constraints on the output or latent variables of a neural network. RAYEN guarantees constraint satisfaction during both training and testing, for any input and any network weights. Unlike prior approaches, RAYEN avoids computationally expensive orthogonal projections, soft constraints, conservative approximations of the feasible set, and slow iterative corrections. RAYEN supports any combination of linear, convex quadratic, second-order cone (SOC), and linear matrix inequality (LMI) constraints, with negligible overhead compared to unconstrained networks. For instance, it imposes 1K quadratic constraints on a 1K-dimensional variable with only 8 ms of overhead compared to a network that does not enforce these constraints. An LMI constraint with 300x300 dense matrices on a 10K-dimensional variable can be guaranteed with only 12 ms additional overhead.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When used in neural networks that approximate the solution of constrained trajectory optimization problems, RAYEN runs 20 to 7468 times faster than state-of-the-art algorithms, while guaranteeing constraint satisfaction at all times and achieving a near-optimal cost (<1.5% optimality gap). Finally, we demonstrate RAYEN's ability to enforce actuator constraints on a learned locomotion policy by validating constraint satisfaction in both simulation and real-world experiments on a quadruped robot. The code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

Convex constraints play a crucial role in many areas of Robotics such as control, trajectory planning, state estimation, signal processing, and computer vision. For example, linear constraints are extensively used to guarantee safety in obstacle avoidance, convex quadratic constraints are leveraged in barrier functions, SOC constraints are used in grasping, contacts, and motion planning, and LMI constraints are important in pose-graph optimization and Lyapunov's stability theory. In recent years, there has been an extensive use of neural networks in all these applications due to their expressive power. However, their lack of constraint satisfaction guarantees greatly limits their applicability, especially for safety-critical applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

There are some convex constraints that can be easily imposed on the output (or latent variable) of a neural network. For instance, box constraints can be imposed using sigmoid functions, nonnegative constraints can be enforced using relu functions, simplex constraints can be guaranteed using softmax functions, and some spherical or ellipsoidal constraints can be imposed using normalization. However, these methods are not applicable to more general types of constraints.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

One common way to bias the network towards the satisfaction of the constraints is via soft constraints, which consist of the addition of terms in the training loss to penalize the violation of the constraints. Similar penalties are also used in physics-informed neural networks. The main disadvantage of this approach is that there are no constraint satisfaction guarantees at test time. Works such as Chzhen and Donti use data-driven approaches to approximately enforce the constraints, but also lack hard constraint guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

When the constraints are homogeneous linear inequality constraints (i.e., $\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{0}$), Frerix et al. leverage the Minkowski-Weyl theorem to guarantee the satisfaction of these linear constraints at all times.^11^1The Minkowski-Weyl theorem can be leveraged for any (convex) polyhedron defined by $\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{b}$, but focuses on the case $\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{0}$ The main disadvantage of this approach is that it is only applicable to linear inequality constraints. Moreover, this method requires running offline the double description method to obtain the V-representation (vertices and rays) of the polyhedron defined by its H-representation (intersection of half-spaces). Even if done offline, the double description method becomes intractable for high-dimensional problems. Other related methods that focus on linear constraints include.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

In contrast to these works, which focus only on linear constraints, RAYEN supports any combination of linear, convex quadratic, SOC, and LMI constraints. To avoid the orthogonal projection step, Maruyama proposes to first use a sigmoid to constrain the output to a hypercube that encloses the feasible set, and then use the distances to the border of the set to scale it down to force it to stay in the set. However, the question of how to compute these distances, which is crucial for its computational tractability, is left unanswered. Moreover, the results shown in Maruyama are only for linear constraints, and linear equality constraints are not taken into account.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

There have also been many recent advances in implicit layers that solve different types of optimization problems, with some works focusing on quadratic programming or, more generally, convex optimization problems. These implicit layers can be leveraged to enforce constraints on the network during training and/or testing by obtaining the orthogonal projection onto the feasible set. This orthogonal projection could also be obtained using the Dykstra's Projection Algorithm. While the use of these orthogonal projections guarantees the satisfaction of the constraints, it is typically at the expense of very high computation times. By leveraging analytic expressions of the distance to the boundaries of the convex set, RAYEN is able to avoid this slow orthogonal projection step and guarantee the constraints in a much more computationally-efficient manner.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

With the goal of reducing the computation time, Donti et al. proposed DC3, an algorithm that first uses completion to guarantee the equality constraints, and then enforces the inequality constraints by using an inner gradient descent procedure that takes steps along the manifold defined by the equality constraints. This inner gradient descent procedure is performed both at training and testing time. While DC3 is typically less computationally expensive than projection-based methods, this inequality correction may still require many steps, as we will show in Section 6.1. Moreover, this inner gradient correction may also suffer from convergence issues for general convex constraints. Compared to DC3, RAYEN does not need to rely on an inner gradient descent correction, avoiding therefore any convergence issues and substantially reducing the computation time. Other approaches that also rely on (potentially computationally expensive) iterative algorithms to ensure the feasibility include Grontas et al., Nguyen and Donti, and Liang and Chen. Similarly, works such as Schneider and Kuhn need to use Newton-Raphson or bisection methods for general convex sets, while Liang et al. propose to learn homeomorphic projections and use bisection to enforce feasibility.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

Another option to enforce convex constraints is to perform a projection relying on computationally-expensive differentiable convex optimization solvers used as an implicit layer of the network. By eschewing iterative algorithms and learned projections in favor of leveraging analytically-found distances to the set boundaries, RAYEN significantly reduces computational overhead.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

There have also been extensive sets of works that use neural networks for Constraint Satisfaction Problems, where the goal is to generate a set of variables defined over finite and discrete domains (Boolean domains for example) that satisfy some constraints. Our focus is instead on convex constraints, where the decision variables are defined over continuous (and potentially unbounded) domains.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

Since our initial preprint, subsequent works have expanded on these themes. For instance, Konstantinov and Utkin proposes a similar framework for linear and convex quadratic constraints, while Liu et al. builds upon our approach by employing a homeomorphism between the convex constraint set and a unit ball.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

The contributions of this work are therefore summarized as follows: Framework to impose by construction hard convex constraints on the output or latent variable of a neural network. The constraints are guaranteed to be satisfied at all times, for any input and/or weights of the network. No conservative approximations of the set are used.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

Any combination of linear, convex quadratic, SOC, and LMI constraints is supported. For example, RAYEN can impose 1K quadratic constraints on a 1K-dimensional variable with a computation overhead of only 8 ms. Similarly, a $300\times 300$ dense LMI constraint can be imposed on a 10K-dimensional variable with an overhead of less than 11 ms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

When used in neural networks that approximate the solution of optimization problems, RAYEN showcases computation times between 20 and 7468 times faster than other state-of-the-art algorithms, while generating feasible solutions whose costs are very close to the optimal value.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction and Related Work", "weight": 1.5} -->

The notation used throughout the paper is available in Table 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Scalar, column vector, matrix, and set Euclidean norm of the vector c C is a (symmetric) positive semidefinite matrix C is a (symmetric) positive definite matrix $\bar{\boldsymbol{c}}:=\frac{\boldsymbol{c}}{\left\|\boldsymbol{c}\right\|}$ Maximum of the elements of the column vector c Maximum of the elements of the set 𝒞 Infimum of the set 𝒞 ${\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\text{relu}\left(a\right)}$

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

${\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\text{relu}\left(\boldsymbol{a}\right)}$ relu(⋅) applied elementwise to the elements of the vector a Frontier of the set 𝒞 Element-wise inequality, element-wise equality Matrix or vector of zeros/ones (dimensions given by the context).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

If the dimensions need to be specified, the subscript a × b (rows × columns) will be used Affine hull of a set 𝒮 (i.e., smallest affine set containing 𝒮) i-th element of the column vector c ∈ ℝa. i ∈ {0, …, a − 1} i-th row of the matrix C, i ∈ {0, …, a − 1}. If C ∈ ℝa × b, then C[i,:] ∈ ℝ1 × b (i.e., a row vector).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

C[𝒮,:] is a matrix whose rows are the rows of C whose indexes are in the set 𝒮 ⊆ ℕ. Analogous definition for c[𝒮] Element-wise absolute value Softmax function. I.e., if b = softmax(a), then b[i] = ea[i]/∑jea[j] Column vector containing all the eigenvalues of the matrix C Linear Matrix Inequality Table 1: Notation used in this paper This work addresses the problem of how to ensure that the output (or a latent variable) $\boldsymbol{y}:=\left[\begin{array}{ccc}\boldsymbol{y}_{}&\cdots&\boldsymbol{y}_{[k-1]}\end{array}\right]^{T}\in\mathbb{R}^{k}$ of a neural network lies in a convex set $\mathcal{Y}$ defined by the following constraints: Figure 2: Sets 𝒴 ⊆ ℝk and 𝒵 ⊆ ℝn.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

z0 is a point in the interior of 𝒵, and any point z ∈ 𝒵 is mapped to its corresponding point y ∈ 𝒴 using y = f(z). In this example, the dimension of the ambient space is k = 3, while the dimension of aff (𝒴) is n = 2. For visualization purposes, here 𝒴 is defined by only linear and quadratic constraints. The values of κL and κQ (inverse distances to, respectively, ∂𝒵L and ∂𝒵Q along the direction $\bar{\boldsymbol{v}}:=\frac{\boldsymbol{v}}{\left\|\boldsymbol{v}\right\|}$, see Section 4), are also shown. In this figure, y0:= f(z0) and y1:= f(z1).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

where $\boldsymbol{P}_{i}\succeq\boldsymbol{0}\;\forall i=0,...,\eta-1$, and where $\boldsymbol{F}_{0},...,\boldsymbol{F}_{k}$ are symmetric matrices. This set $\mathcal{Y}$, which can be bounded or unbounded, is defined by linear constraints (Eqs. 1 and 2), convex quadratic constraints (Eq. 3), SOC constraints (Eq. 4), and LMI constraints (Eq. 5, also known as semidefinite constraints). Constraints 1, 2, 3, and 4 could also be written as an LMI constraint, but for notational convenience throughout the paper (and without any loss of generality), we explicitly distinguish them. Note also that several LMIs can be converted into one LMI by simply stacking the matrices appropriately (see, e.g., Boyd and Vandenberghe).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Let us also introduce the following definitions: Hence, we have that $\mathcal{Y}:=\mathcal{Y}_{L}\cap\mathcal{Y}_{Q}\cap\mathcal{Y}_{S}\cap\mathcal{Y}_{M}$. For simplicity, we will assume throughout the paper that $\text{aff}\left(\mathcal{Y}_{L}\right)=\text{aff}\left(\mathcal{Y}\right)$, where $\text{aff}\left(\cdot\right)$ denotes the affine hull.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Some degenerate cases do not satisfy this assumption, but in those cases the same set $\mathcal{Y}$ can be parametrized with a different set of constraints for which this assumption holds.^22^2An example of a degenerate case in 3D (i.e., $k=3$) with only linear and quadratic constraints would be when $\mathcal{Y}_{L}$ is the unit cube, and $\mathcal{Y}_{Q}$ is a cylinder tangent to one of its faces such that $\mathcal{Y}=\mathcal{Y}_{L}\cap\mathcal{Y}_{Q}$ is the segment they have in common. By simply reparametrizing $\mathcal{Y}$ with only linear constraints (the segment itself), then the assumption $\text{aff}\left(\mathcal{Y}_{L}\right)=\text{aff}\left(\mathcal{Y}\right)$ is satisfied.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Overall, RAYEN works as follows (see also Fig. 2): In an offline phase (Section 3), the affine hull of $\mathcal{Y}$ is obtained, and the constraints are expressed in that linear subspace. Letting $\mathcal{Z}$ denote the feasible set in this subspace, an interior point $\boldsymbol{z}_{0}$ of this set $\mathcal{Z}$ is also found. In the online phase (Section 4), a linear map is applied to an upstream latent variable of the network to obtain a vector $\boldsymbol{v}$ of the same dimension as the subspace, that will determine the step direction from $\boldsymbol{z}_{0}$. The length $\lambda\geq 0$ of this step is adjusted to ensure that $\boldsymbol{z}_{0}+\lambda\frac{\boldsymbol{v}}{\left\|\boldsymbol{v}\right\|}$ lies in $\mathcal{Z}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

After lifting to the original dimension, the output is therefore guaranteed to lie in $\mathcal{Y}$. These offline and online steps are also detailed in Alg. 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

1 Compute affine hull of 𝒴 (Section 3.1) 3 Compute z0, an interior point of 𝒵 (Section 3.3) Online (both training and testing): 4 Pass the input through the NN to obtain x ∈ ℝm 5 Pass x ∈ ℝm through L(m, n) to obtain v ∈ ℝn 7 Compute z1 and y:= f(z1) (Eqs. 7 and 10) (The output y is guaranteed to be in 𝒴) Compute loss and backpropagate Algorithm 1 Pseudocode of the steps involved in RAYEN. Here, L(a, b) denotes a linear layer with input size a and output size b. The online phase is also depicted in Fig. 4.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Affine Hull of $\\mathcal{Y}$", "weight": 1.0} -->

To find the affine hull of the set $\mathcal{Y}$, we first express all the linear constraints (Eqs. 1 and 2) as linear inequality constraints by simply stacking the matrices: and therefore $\mathcal{Y}_{L}$ is now $\left\{\boldsymbol{y}\in\mathbb{R}^{k}|\tilde{\boldsymbol{A}}\boldsymbol{y}\leq\tilde{\boldsymbol{b}}\right\}$. To reduce the computation time during the online phase, the redundant constraints of the inequality system $\tilde{\boldsymbol{A}}\boldsymbol{y}\leq\tilde{\boldsymbol{b}}$ (if there are any) are then deleted.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Affine Hull of $\\mathcal{Y}$", "weight": 1.0} -->

This is done by solving a sequence of Linear Programs (see, e.g. Szedlak), which obtains the reduced system of inequalities $\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{b}$ such that $\mathcal{Y}_{L}=\left\{\boldsymbol{y}\in\mathbb{R}^{k}|\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{b}\right\}$. Then, another sequence of Linear Programs is solved to find the set which contains the indexes of the constraints that are always active for all the points in $\mathcal{Y}_{L}$ (see, e.g. or).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Affine Hull of $\\mathcal{Y}$", "weight": 1.0} -->

Defining $\mathcal{I}:=\{0,...,a-1\}\backslash\mathcal{E}$ (where $a$ is the number of rows of $\boldsymbol{A}$), let us now introduce the following notation:^33^3Note that if $\mathcal{I}=\emptyset$, then we need $\boldsymbol{b}_{\mathcal{I}}=1$ (instead of $\boldsymbol{b}_{\mathcal{I}}=0$) to make sure that there exists a point in the interior of $\mathcal{Z}_{L}:=\left\{\boldsymbol{z}\in\mathbb{R}^{n}|\boldsymbol{0}_{1\times n}\boldsymbol{z}\leq 1\right\}\equiv\mathbb{R}^{n}$ (see Section 3.3).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Affine Hull of $\\mathcal{Y}$", "weight": 1.0} -->

Then, the affine hull of $\mathcal{Y}$ is given by where we have used the assumption that $\text{aff}\left(\mathcal{Y}\right)=\text{aff}\left(\mathcal{Y}_{L}\right)$ (see Section 2). The dimension of this affine hull is then Note also that In general, $\left(\boldsymbol{A}_{\mathcal{E}},\boldsymbol{b}_{\mathcal{E}}\right)$ may be different than $\left(\boldsymbol{A}_{2},\boldsymbol{b}_{2}\right)$, and $\left(\boldsymbol{A}_{\mathcal{I}},\boldsymbol{b}_{\mathcal{I}}\right)$ may be different than $\left(\boldsymbol{A}_{1},\boldsymbol{b}_{1}\right)$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Affine Hull of $\\mathcal{Y}$", "weight": 1.0} -->

This can happen, for example, when $\text{aff}\left(\left\{\boldsymbol{y}\in\mathbb{R}^{k}|\boldsymbol{A}_{1}\boldsymbol{y}\leq\boldsymbol{b}_{1}\right\}\right)\neq\mathbb{R}^{k}$ (intuitively this means that the inequality constraint defined by Eq. 1 hides equality constraints), or when there are redundant constraints in Eqs. 1 and/or 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Interior point of $\\mathcal{Z}$", "weight": 1.0} -->

&\boldsymbol{W}\left(\boldsymbol{f}(\boldsymbol{z}_{0})\right)\succ\boldsymbol{0}\end{split}$ | | | Hence, a way to find this interior point $\boldsymbol{z}_{0}$ is to solve the convex program: and then checking that $\epsilon^{*}>0$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Interior point of $\\mathcal{Z}$", "weight": 1.0} -->

In these constraints, $\epsilon\geq 0$ is a decision variable that dictates how much slack we have while satisfying each inequality constraint. By maximizing $\epsilon$, we ensure that the strict inequalities of Eq. LABEL:eq:constraints_interior are satisfied. $\delta$ is a fixed positive parameter that simply prevents this optimization problem from being unbounded, which happens when the feasible set $\mathcal{Z}$ is unbounded. We choose $\delta=0.5$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "RAYEN: Online", "weight": 1.0} -->

As shown in Fig. 4, to obtain an $n$-dimensional latent variable $\boldsymbol{v}$ (where $n$ is the dimension of $\text{aff}\left(\mathcal{Y}\right)$, see Eq. 6), we first apply a linear layer to the upstream latent variable of the network $\boldsymbol{x}\in\mathbb{R}^{m}$. This mapping can be omitted if $m=n$. Assuming now $\boldsymbol{v}\neq\boldsymbol{0}$,^44^4If $\boldsymbol{v}=\boldsymbol{0}$, we simply take $\boldsymbol{z}_{1}:=\boldsymbol{z}_{0}$, and therefore $\kappa$ does not need to be computed.

<!-- chunk {"id": "body-0037", "role": "body", "section": "RAYEN: Online", "weight": 1.0} -->

let us define the inverse distance to the frontier of $\mathcal{Z}$ along $\bar{\boldsymbol{v}}:=\frac{\boldsymbol{v}}{\left\|\boldsymbol{v}\right\|}$ as Then, it is clear that^55^5Note that another option would be to use $\boldsymbol{z}_{1}:=\left(\boldsymbol{z}_{0}+\frac{1}{e^{\beta}+\kappa}\bar{\boldsymbol{v}}\right)\in\mathcal{Z}\;$ where $\left[\begin{array}{cc}\boldsymbol{v}&\beta\end{array}\right]^{T}$ is the output of the layer before RAYEN.

<!-- chunk {"id": "body-0038", "role": "body", "section": "RAYEN: Online", "weight": 1.0} -->

Empirically, however, this approach generated worse results than the ones obtained using Eq. 10. Still, we left this second approach also available in the code since the performance may depend on the specific problem and training process and that therefore $\boldsymbol{f}\left(\boldsymbol{z}_{1}\right)\in\mathcal{Y}$. Note that no conservatism is introduced here. In other words, and given that $\mathcal{Y}$ is a convex set, for any point $\boldsymbol{y}\in\mathcal{Y}$, there exists at least one $\boldsymbol{v}$ such that $\boldsymbol{f}\left(\boldsymbol{z}_{1}\right)\in\mathcal{Y}$ holds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computation of $\\kappa_{L}$", "weight": 1.0} -->

Taking into account now all the faces of $\mathcal{Z}_{L}$, we have that $\kappa_{L}$ is given by where $\varoslash$ denotes the element-wise division between two matrices, and where $\boldsymbol{D}$ can be computed offline because it does not depend on $\bar{\boldsymbol{v}}$. Note that if $\kappa_{L}=0$, then $\mathcal{Z}_{L}$ is unbounded along the ray that starts at $\boldsymbol{z}_{0}$ and follows $\bar{\boldsymbol{v}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computation of $\\kappa_{Q}$", "weight": 1.0} -->

The inverse of the distance from $\boldsymbol{z}_{0}$ to $\partial\mathcal{Z}_{Q_{i}}$ along the direction $\bar{\boldsymbol{v}}$ can be obtained by computing the nonnegative $\kappa_{Q,i}$ that satisfies: where $\boldsymbol{f}(\cdot)$ is defined in Eq. 7. Multiplying both sides of this equation by $\kappa_{Q,i}^{2}$ yields a quadratic equation on $\kappa_{Q,i}$, from which its nonnegative root $\kappa_{Q,i}^{+}$ can be easily obtained. Taking now into account all the quadratic constraints, $\kappa_{Q}$ is therefore given: Figure 5: Eigenvalues of δH + S as a function of δ. In this example, H ≻ 0 and S are 3 × 3 matrices. κM, defined in Eq. 12, is also shown here.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computation of $\\kappa_{S}$", "weight": 1.0} -->

Similar to the previous case, the inverse of the distance from $\boldsymbol{z}_{0}$ to $\partial\mathcal{Z}_{S_{j}}$ along the direction $\bar{\boldsymbol{v}}$ can be obtained by computing the nonnegative $\kappa_{S,j}$ that satisfies: Squaring both sides of Eq. 11, and then multiplying them by $\kappa_{S,j}^{2}$ yields a quadratic equation on $\kappa_{S,j}$, from which its two roots $\kappa_{S,j}^{}$ and $\kappa_{S,j}^{}$ can be easily obtained.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Computation of $\\kappa_{S}$", "weight": 1.0} -->

The inverse of the distance from $\boldsymbol{z}_{0}$ to $\partial\mathcal{Z}_{S_{j}}$ along $\bar{\boldsymbol{v}}$ will therefore be given by^66^6The $\text{relu}(\cdot)$ operator is needed because both roots can be negative due to the fact that we have squared both sides of Eq. 11. Both roots being negative means that in that case $\mathcal{Z}_{S_{j}}$ is unbounded in the direction $\bar{\boldsymbol{v}}$ and therefore we have $\kappa_{S,j}=0$. When both roots are positive, we need to select the largest one, which is why the $\text{max}\left(\cdot\right)$ operator is needed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Computation of $\\kappa_{S}$", "weight": 1.0} -->

Taking into account all the SOC constraints, $\kappa_{S}$ is therefore given by

<!-- chunk {"id": "body-0044", "role": "body", "section": "Computation of $\\kappa_{M}$", "weight": 1.0} -->

The inverse of the distance from $\boldsymbol{z}_{0}$ to $\partial\mathcal{Z}_{M}$ along the direction $\bar{\boldsymbol{v}}$ is defined as: then the condition $\boldsymbol{z}_{0}+\lambda\bar{\boldsymbol{v}}\in\mathcal{Z}_{M}$ is equivalent to Dividing everything by $\lambda$ (recall that $\lambda>0$) and rearranging the terms we have where $\boldsymbol{H}\succ\boldsymbol{0}$ derives from the fact that $\boldsymbol{z}_{0}$ is an interior point of $\mathcal{Z}_{M}$. Hence: Let us now distinguish two cases: If $\boldsymbol{S}\succeq\boldsymbol{0}$, then it is clear that $\kappa_{M}=0$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Computation of $\\kappa_{M}$", "weight": 1.0} -->

Otherwise, we need $\kappa_{M}\boldsymbol{H}+\boldsymbol{S}\in\partial\mathcal{Z}_{M}$. Note that the matrices that belong to $\partial\mathcal{Z}_{M}$ have at least one zero eigenvalue. Therefore, defining (where $\boldsymbol{v}_{i}$ is the eigenvector associated with the zero eigenvalue of $\tau_{i}\boldsymbol{H}+\boldsymbol{S}$), we know that $\kappa_{M}\in\mathcal{T}$. Also note that the rest of the eigenvalues need to be positive.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Computation of $\\kappa_{M}$", "weight": 1.0} -->

Given that $\boldsymbol{H}\succ\boldsymbol{0}$, we can conclude that An example is available in Fig. 5. Note also that: Letting $\boldsymbol{L}$ denote the lower triangular matrix with positive diagonal entries such that $\boldsymbol{H}^{-1}=\boldsymbol{L}\boldsymbol{L}^{T}$ (i.e., the Cholesky decomposition of $\boldsymbol{H}^{-1}$), and using the fact that $\text{eig}\left(-\boldsymbol{H}^{-1}\boldsymbol{S}\right)=\text{eig}\left(\boldsymbol{L}^{T}\left(-\boldsymbol{S}\right)\boldsymbol{L}\right)$ (see proof in Appendix A.1="eig"⁢(𝑳^𝑇⁢(-𝑺)⁢𝑳) ‣ Appendix A Appendix ‣ RAYEN: Imposition of Hard Convex Constraints

<!-- chunk {"id": "body-0047", "role": "body", "section": "Computation of $\\kappa_{M}$", "weight": 1.0} -->

on Neural Networks")), we have that^77^7Eq. 13 can also be written as $-\boldsymbol{S}\boldsymbol{v}_{i}=\tau_{i}\boldsymbol{H}\boldsymbol{v}_{i}$, and hence $\kappa_{M}$ could also be found solving the generalized eigenvalue problem of the pair $\left(-\boldsymbol{S},\boldsymbol{H}\right)$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Computation of $\\kappa_{M}$", "weight": 1.0} -->

Putting everything together, we can conclude that:^88^8Note that Eq. 14 gives $\kappa_{M}=0$ for the case $\boldsymbol{S}\succeq\boldsymbol{0}$. This can be easily proven as follows: As the eigenvalues of the product of two positive semidefinite matrices are nonnegative (see, e.g., ), then, if $\boldsymbol{S}\succeq\boldsymbol{0}$, we have that $\text{eig}\left(-\boldsymbol{H}^{-1}\boldsymbol{S}\right)=\text{eig}\left(\boldsymbol{L}^{T}\left(-\boldsymbol{S}\right)\boldsymbol{L}\right)\leq\boldsymbol{0}$. And hence, Eq. 14 gives $\kappa_{M}=0$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Computation of $\\kappa_{M}$", "weight": 1.0} -->

As only the maximum eigenvalue is needed, we can use methods such as power iteration, LOBPCG, or the Lanczos algorithm to avoid computing the whole spectrum of the matrix. Note also that the matrix $\boldsymbol{L}$ can be computed offline, since it does not depend on $\boldsymbol{v}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remarks", "weight": 1.0} -->

Fig. 6 shows the results of RAYEN applied to 12 different sets $\mathcal{Y}$. For each set, we generate 12K samples $\boldsymbol{v}\in\mathbb{R}^{n}$ sampled uniformly in the box $[-2.5,2.5]^{n}$ (see Fig. 4), compute the corresponding $\kappa$, and plot the resulting point $\boldsymbol{y}=\boldsymbol{f}\left(\boldsymbol{z}_{1}\right)\in\mathbb{R}^{k}$ for each of those samples. All these points $\boldsymbol{y}$ are guaranteed to lie in the set $\mathcal{Y}$. Note also that the density of the produced points is higher in the frontiers of the set due to the $\text{min}\left(\frac{1}{\kappa},\left\|\boldsymbol{v}\right\|\right)$ operation performed.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example", "weight": 1.0} -->

Fig. 2 shows an example with $k=3$, $n=2$, and only linear and quadratic constraints. The steps performed by RAYEN in the offline and online phases are described as follows (see also Alg. 1).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Offline", "weight": 1.0} -->

In the offline phase, RAYEN performs these steps: The feasible set $\;\subset\mathbb{R}^{3}$ is defined as the intersection between its (linear equality constraints, Section 3.1), a (linear inequality), and an (quadratic inequality). The intersection between the and the is denoted as $\subset\mathbb{R}^{3}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Offline", "weight": 1.0} -->

Then, using the matrix $\boldsymbol{N}$ (Eq. 7), we compute $\;\subset\mathbb{R}^{2}$ as the intersection between $\;\subset\mathbb{R}^{2}$ and $\;\subset\mathbb{R}^{2}$ The interior point $\boldsymbol{z}_{0}$ of can then be found solving the optimization problem of Section 3.3.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Online (both training and testing)", "weight": 1.0} -->

In the online phase, RAYEN performs these steps: After passing the input through the network and the linear layer (Fig. 4), we obtain $\boldsymbol{v}\in\mathbb{R}^{2}$. $\kappa_{L}$, which is the inverse of the distance from $\boldsymbol{z}_{0}$ to the border of, following the direction $\boldsymbol{v}$ (Section 4.1). $\kappa_{Q}$, which is the inverse of the distance from $\boldsymbol{z}_{0}$ to the border of, following the direction $\boldsymbol{v}$ (Section 4.2). $\kappa:=\text{max}\left[\begin{array}{cccc}\kappa_{L}&\kappa_{Q}\end{array}\right]^{T}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Online (both training and testing)", "weight": 1.0} -->

Does not support quadratic constraints Table 4: Trajectory optimization problems 1 and 2 (in both original and standard form) and losses used in Section 6.1. psoft, L and psoft, Q are defined, respectively, in Eq. 15 and Eq. 16. The decision variables are the control points of the spline p(t). In these optimizations, the constraint $\mathcal{Q}_{j}^{\text{MV}}\subseteq\mathcal{P}_{\left\lfloor\frac{j}{2}\right\rfloor},\;\forall j\in J$ is a linear constraint, because the MINVO control points are linear functions of the spline control points.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results", "weight": 1.0} -->

In this Section, we first study how RAYEN is able to approximate the optimal solution of trajectory optimization problems with constraints (Section 6.1). Then, in Section 6.2, we use RAYEN to constrain the individual and total torques of the joints obtained by a learning-based locomotion policy for a quadruped robot. Finally, in Section 6.3, we analyze RAYEN's computation time when applied to different constraints of varying dimensions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Position, velocity, acceleration, and jerk Initial and final positions Number of intervals of the B-Spline Number of position control points of the B-Spline l-th acceleration control point of the B-Spline l-th jerk control point of the B-Spline j is the index of the interval of the trajectory, j ∈ J:= {0, 1,..., ninterv − 1} 𝒬jMV is the set of position control points of the interval j using the MINVO basis. Analogous definition for the velocity control points 𝒱jMV Sequence of overlapping polyhedra.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

They can be obtained using methods such as Weights used in the cost functions (see Table 4) $\boldsymbol{\gamma}:=\left[\begin{array}{cccc}\alpha_{\text{v}}&\alpha_{\text{a}}&\alpha_{\text{j}}&\mathbf{\mathbf{p}}_{f}^{T}\end{array}\right]^{T}$ Floor function (i.e., rounding to the nearest integer ≤ a) Table 5: Notation used in the formulation of the trajectory optimization problems (Section 6.1).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

One of the (many) applications of being able to impose constraints on neural networks is when they are used to approximately solve optimization problems much faster than standard solvers. In this section, we analyze how a neural network equipped with RAYEN is able to approximate the optimal solution of a trajectory optimization problem while satisfying all the constraints. Specifically, they are trajectory optimization problems that aim at obtaining the clamped uniform B-Spline that minimizes a weighted sum of the velocity smoothness, the acceleration smoothness, and the jerk smoothness, while ensuring that the whole trajectory remains within a sequence of overlapping polyhedra that represent the free space. This problem (or small variations of it) appears extensively in many trajectory planning problems in Robotics, such as. Using the notation shown in Table 5, the optimization problems are available in Table 4 ‣ 5 Example ‣ RAYEN: Imposition of Hard Convex Constraints on Neural Networks"). The constraints are these: Initial and final constraints: The initial and final states are stop conditions. The initial position is fixed, while the final position of the trajectory is included in the cost as a soft constraint.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

This final position is taken inside $\mathcal{P}_{n_{\text{polyh}}-1}$ (the last polyhedron of the corridor).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Corridor constraints: Each interval of the trajectory is assigned to one polyhedron, and the convex hull property of the MINVO basis is leveraged to ensure that each interval remains inside that assigned polyhedron. Compared to approaches that only impose constraints on discretization points along the trajectory, this approach guarantees safety for the whole trajectory $t\in[0,t_{f}]$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Dynamic limit constraints: Optimization 1 uses linear constraints to impose a maximum velocity $v_{\text{max}}$ and acceleration $a_{\text{max}}$. Optimization 2 uses quadratic constraints instead, and also imposes a maximum jerk $j_{\text{max}}$. Similar to the corridor constraints, we also leverage here the convex hull property of the MINVO basis.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Hence, optimization problem 1 has only linear constraints, while optimization problem 2 has both linear and convex quadratic constraints. Both have a convex quadratic objective function, which depends on a parameter $\boldsymbol{\gamma}$. Nonconvex objective functions could also be used, but we use convex objective functions to enable a direct comparison with the globally optimal solution obtained using a state-of-the-art convex optimization solver, such as Gurobi.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Optimization 1 (Linear Constraints) $\begin{array}{c}\text{{Num. of}}\\\text{{params}}\end{array}$ Same distribution as training: γ ∈ TE1, in Different distribution as training: γ ∈ TE1, out Optimization 2 (Linear and Convex Quadratic Constraints) $\begin{array}{c}\text{{Num. of}}\\\text{{params}}\end{array}$ Same distribution as training: γ ∈ TE2, in Different distribution as training: γ ∈ TE2, out Does not support quadratic constraints Figure 7: Comparison of the computation time vs. the normalized loss (defined as the loss obtained divided by the globally-optimal loss obtained by Gurobi) for the methods that generate feasible solutions. The dashed line corresponds to a normalized cost of 1.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

We compare RAYEN with the following approaches (see also Table 3): UU: Both training and testing are Unconstrained. This method produces directly $\boldsymbol{y}=\boldsymbol{v}$. A soft cost, described below, is added to the training loss to penalize the violation of the constraints.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

UP: When training, this method simply outputs $\boldsymbol{f}(\boldsymbol{v})$ (see Eq. 7), meaning that $\boldsymbol{y}$ is Unconstrained with respect to the inequality constraints. When testing, this method outputs $\boldsymbol{f}(\boldsymbol{v}^{\prime})$, where $\boldsymbol{v}^{\prime}$ is the orthogonal Projection of $\boldsymbol{v}$ onto $\mathcal{Z}$. The projection is computed using. This method also has a soft cost in the training loss to penalize the violation of the constraints.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

PP: The orthogonal Projection onto $\mathcal{Z}$ is performed during both training and testing. These projections are implemented using.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

DC3: Algorithm proposed. Completion is used to enforce the equality constraints, and then an inner gradient decent method (which is also performed in the testing phase) enforces the inequality constraints. This method also includes a soft cost in the training loss to penalize the violation of the constraints.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Bar: Generalization of the barycentric coordinates method (proposed for constraints $\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{0}$) for any constraint of the type $\boldsymbol{A}\boldsymbol{y}\leq\boldsymbol{b}$. This method only supports linear constraints. The matrices of vertices $\boldsymbol{V}$ and rays $\boldsymbol{R}$ (see Table 3) are computed offline using the double description method on the H-representation (half-space representation) of $\mathcal{Y}_{L}$. As detailed in Table 3, the $\text{softmax}(\cdot)$ operator produces the weights for the convex combination of the vertices, while the $\text{abs}(\cdot)$ operator produces the weights for the conical combination of the rays.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Defining the following soft costs: the training and test losses in each algorithm are defined in Table 4 ‣ 5 Example ‣ RAYEN: Imposition of Hard Convex Constraints on Neural Networks"). In these losses, the soft costs are weighted with $\omega\geq 0$. The methods Bar, PP, and RAYEN do not need a soft cost since all the constraints are guaranteed to be satisfied both during training and testing. Note also that in DC3, the term $\left\|\boldsymbol{A}_{2}\boldsymbol{y}-\boldsymbol{b}_{2}\right\|^{2}$ of $p_{\text{soft},L}$ will always be zero since this algorithm satisfies the equality constraints by construction.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

All the methods are implemented in Pytorch, and the Adam optimizer with a learning rate of $10^{-4}$ is used for training. A total of 2000 epochs are performed for training, and the policy with the best validation loss is selected for testing. For each optimization problem, a total of 1216 samples of $\boldsymbol{\gamma}\in\mathbb{R}^{n_{\boldsymbol{\gamma}}}$ are drawn from uniform distributions detailed in Appendix A.2, and $\approx 70\%$ of them are used in the training set and $\approx 30\%$ in the validation set. The batch size for training is 256. All these results were obtained with the double-precision floating-point format and using a desktop equipped with an Intel Core i9-12900 × 24, 64GB of RAM, and an NVIDIA GeForce RTX 4080.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

For each optimization problem $j\in\{1,2\}$, we use two testing sets (each one with 512 samples $\boldsymbol{\gamma}\in\mathbb{R}^{n_{\boldsymbol{\gamma}}}$): $\text{TE}_{j,\text{in}}$ and $\text{TE}_{j,\text{out}}$. $\text{TE}_{j,\text{in}}$ uses the same distribution as the one used for training, while $\text{TE}_{j,\text{out}}$ does not. Details on these distributions are available in Appendix A.2. The goal of using the test set $\text{TE}_{j,\text{out}}$ is to study how well the trained policy generalizes to unseen inputs. The results for these test sets are shown in Table 6 and plotted in Fig. 7. In these results, the violation is defined as the squared distance to the closest point in the feasible set.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

The loss is normalized with the globally-optimal loss obtained by Gurobi. Hence, a normalized loss smaller than $1$ implies that the solution violates the constraints. Both problems 1 and 2 are convex, and therefore the optimal solution found by Gurobi is globally optimal.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

The following conclusions can be extracted from these results: Same distribution as in training: Optimization 1: RAYEN is able to obtain the normalized loss closest to the globally-optimal one, while guaranteeing a zero violation of the constraints. The methods UP, PP, DC3 with $\omega=5000$, Bar, and RAYEN generate feasible solutions. In terms of computation time, RAYEN is between 20 and 7468 times faster than these methods.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Optimization 2: Again, RAYEN is able to obtain the normalized loss closest to the globally-optimal one while guaranteeing a zero violation of the constraints. Compared to the feasible approaches (UP and PP), RAYEN's computation time is between 2094 and 2417 times faster.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Generalization: Different distribution as in training: Optimization 1: Both RAYEN and Bar are able to obtain normalized losses very close to the globally-optimal one, while guaranteeing a zero violation of the constraints. Although Bar's loss is slightly better than RAYEN's (1.0070 vs. 1.0076), Bar's method is 16 times slower, and it requires 197 times as many parameters as RAYEN. This high number of parameters required by Bar is due to the high number of vertices of the polyhedron $\mathcal{Y}$. Note also that Bar only supports linear constraints.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Optimization 2: RAYEN is the algorithm that has the best generalization (smallest normalized loss) while achieving a zero violation of the constraints.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

It is also important to note that, when tested in the same distribution as the training set, the violations of both UU and DC3 tend to decrease with higher values of $\omega$. These violations however tend to become quite large when using a different distribution than the one used in training.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Trajectory optimization", "weight": 1.0} -->

Using RAYEN, some examples of the trajectories generated by the trained network for 100 different $\boldsymbol{\gamma}$ taken from the testing set $\text{TE}_{1,\text{in}}$ (see Appendix A.2) are shown in Fig. 8. The initial and final boundary conditions, kinematic limits (velocity, acceleration, and jerk), and collision-avoidance constraints (defined by the green safety corridor) are guaranteed to be satisfied at all times.^99^9As the degree of the spline of the Optimization 1 is 2, then the term $\int_{0}^{t_{f}}\left\|\mathbf{j}(t)\right\|^{2}dt$ is clearly $0$, and therefore $\alpha_{\text{j}}$ does not affect the optimal solution. We keep this term simply for consistency purposes with Optimization 2, but it could also be removed as well.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

In recent years, the use of neural networks for locomotion policies in legged robotics has shown unprecedented performance and robustness. Typically trained through reinforcement learning, the system's hardware limits are either handled directly through the simulator, or implicitly handled through shaping rewards or termination of the training episode. Although constrained RL methods exist, they only enforce constraints in an expected value fashion. Especially for torque-controlled robots, training a policy that guarantees (or at least that is aware) of the actuator limits is vital.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

We present a case study in which RAYEN is used to enforce four constraints commonly encountered in legged robotics literature. While the first constraint can be handled via simple clipping, the remaining three introduce coupling among the admissible leg torques, rendering independent clipping infeasible.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

Joint torque limits with a box constraint Here, the vector $\boldsymbol{\tau}$ contains all the individual joint torques, the inequalities are element-wise, and $\boldsymbol{\tau}_{\mathrm{min}}$ and $\boldsymbol{\tau}_{\mathrm{max}}$ are vectors that represent, respectively, the lower and upper torque limits. Note that $\boldsymbol{\tau}_{\mathrm{min}}$ and $\boldsymbol{\tau}_{\mathrm{max}}$ are usually symmetrical, but could also depend on other characteristic motor variables, as in Shin et al..

<!-- chunk {"id": "body-0083", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

Sum of absolute torques over all $n_{j}$ joints (weighted $\ell_{1}$-ball) which directly limits the total current draw^1010^10We employ the common assumption that the drawn current per joint is proportional to the effective torque. $I_{\mathrm{abs}}$, in practice usually limited by a fuse.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

Sum of absolute torques per leg (weighted $\ell_{1}$-ball) This constraint limits the total current draw $I_{\mathrm{leg}}$ of all joints per leg, in practice usually limited by a dedicated fuse or in our case by a power cable connector type.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

Limit on torques squared (weighted $\ell_{2}$-ball) Assuming a proportional relation of torque squared and thermal power losses, this constraint can be leveraged to regularize the motor temperatures implicitly. Overheating can be mitigated by limiting the total cooling power $p_{\text{tot}}$, whereby $\boldsymbol{C}$ can be adjusted to account for different thermal constants.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

As a concrete example application, we apply the torque constraints to a locomotion policy which we train to follow base velocity commands, with the same setup as presented in Rudin et al.. During training, we enforce all of the above constraints using RAYEN. The feasible region in torque space therefore results in the intersection of weighted $\ell_{1}$, $\ell_{2}$, and $\ell_{\infty}$-balls (i.e., the intersection of ellipsoidal, diamond-like, and box-like constraints). As previous work has shown, training a motion policy using joint impedance position references as action space has several training and robustness benefits over training with torque output directly, e.g., allowing the policy to be evaluated at a lower frequency. To satisfy the constraints on torque level, RAYEN is therefore applied to the higher frequency torque, as shown in Fig. 9.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Torque Constraints on Legged Robot", "weight": 1.0} -->

Fig. 10 shows the results of the multiple robot experiments conducted with and without RAYEN, both in simulation and on the real-world ANYmal D quadruped. We show the joint torque commands produced by the locomotion policies and the constraint functions of the ball constraints. Subfigures \"A\" and \"B\" show the unconstrained case in simulation and the real-world, respectively. In this baseline setting, we can clearly see violation in all four constraint groups, whereby the limits are denoted by dotted lines. In contrast, subfigures \"C\" and \"D\" show the constrained case in simulation and the real-world, respectively. By utilizing the proposed method, we can clearly see strict constraint satisfaction of all the constraints. These results demonstrate that the RAYEN framework reliably enforces the prescribed physical limits during operation on the physical ANYmal D quadruped, successfully bridging the gap between simulation and real-world deployment.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Computation time", "weight": 1.0} -->

A natural question to ask is what is the additional computation time of a neural network equipped with RAYEN compared to the same neural network without RAYEN (and therefore, without constraint guarantees). For this analysis, we will take $n=m=k$ and choose two networks with the same architecture (Fig. 12). Once trained, the only difference between the networks is in the weights, since one of them has been trained with RAYEN and another one without it. Hence, differences in computation time at testing time will be primarily determined by the computation time of the RAYEN module (Fig. 12). To study the computation time of this module, we generate random dense constraints of varying dimensions and measure the computation time required by RAYEN to impose these constraints on $\boldsymbol{y}\in\mathbb{R}^{k}$ for a random $\boldsymbol{v}\in\mathbb{R}^{n}$ (Fig. 12). All the details of how these random constraints are generated are available in the code released.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Computation time", "weight": 1.0} -->

We run RAYEN with the double-precision floating-point format and on a desktop with an Intel Core i9-12900 × 24, 64GB of RAM, and an NVIDIA GeForce RTX 4080. The computation times per sample achieved by RAYEN are shown in Fig. 11. Note that the computation overhead is negligible, even for high-dimensional variables, as shown in the following statistics: 2K linear constraints on a 10K-dimensional variable: $<0.9$ ms.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Computation time", "weight": 1.0} -->

1K dense convex quadratic constraints on a 1K-dimensional variable: $<8$ ms.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Computation time", "weight": 1.0} -->

500 dense SOC constraints on a 1K-dimensional variable with matrices $\boldsymbol{M}_{j}$ of 300 rows: $<8$ ms.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Computation time", "weight": 1.0} -->

A dense $300\times 300$ LMI constraint on a 10K-dimensional variable: $<11$ ms.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Other types of constraints", "weight": 1.0} -->

This paper has focused on convex constraints in which the parameters that define these constraints (i.e., $\boldsymbol{A}_{1},\boldsymbol{b}_{1},\boldsymbol{A}_{2},\boldsymbol{b}_{2},\boldsymbol{P}_{i},...)$ are fixed and known beforehand. However, in some problems in Robotics, such as in model predictive control (MPC) or trajectory planning, the parameters that define the constraints change in each iteration, or the constraints may be nonconvex. Although we leave the handling of these generic constraints for future work, in this section we detail several ways in which RAYEN could be applied to these more generic cases.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Non-fixed Convex Constraints", "weight": 1.0} -->

In order to be able to impose convex constraints whose parameters are not fixed and/or depend on the previous layers (or input) of the network, we need to take some extra care: The constraints must define a nonempty set at all times, and $\mathcal{Z}$ must have interior points. There are many different ways to ensure this. For instance, if there are no equality constraints, one way would be to ensure these conditions: Figure 13: Two examples of nonconvex sets 𝒴 for which RAYEN could still guarantee zero violation. In both cases, the nonconvex set is defined as a nonlinear transformation of the convex set 𝒞.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Non-fixed Convex Constraints", "weight": 1.0} -->

Then, we can take $\boldsymbol{z}_{0}=\boldsymbol{0}$, as it is guaranteed to be in the interior of $\mathcal{Z}$. Eqs. 21, 22, and 23 can be easily enforced, e.g., using sigmoid functions. Eq. 24 can be enforced by setting $\boldsymbol{F}_{k}:=\boldsymbol{\Gamma}^{T}\boldsymbol{\Gamma}+\epsilon\boldsymbol{I}\ $, where $\epsilon>0$ is a predefined scalar, and where the matrix $\boldsymbol{\Gamma}$ depends on the previous layers (or input) of the network. When there are only linear constraints, other ways to guarantee a nonempty feasible set are explained in and. $\boldsymbol{P}_{i}\succeq\boldsymbol{0}$ ($i=0,...,\eta-1$) is required.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Non-fixed Convex Constraints", "weight": 1.0} -->

Without any loss of generality, this can be enforced by setting $\boldsymbol{P}_{i}:=\boldsymbol{V}_{i}^{T}\boldsymbol{V}_{i}$, where $\boldsymbol{V}_{i}$ is a matrix that depends on the previous layers (or input) of the network.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Non-fixed Convex Constraints", "weight": 1.0} -->

If these conditions are satisfied, then the offline phase (Section 3) is not needed, since $\boldsymbol{z}_{0}$ is already known, and the matrices $\boldsymbol{A}_{p}$ and $\boldsymbol{b}_{p}$ can be easily found online by simply computing the nullspace of $\boldsymbol{A}_{\mathcal{E}}$ (Eq. 8).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Non-fixed Convex Constraints", "weight": 1.0} -->

Another option that allows non-fixed constraints is to use an implicit layer to solve the optimization problem that finds the interior point $\boldsymbol{z}_{0}$. This however can be very computationally expensive.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Nonconvex Constraints", "weight": 1.0} -->

RAYEN could also be applied to any nonconvex set $\mathcal{Y}$ that can be expressed as a (differentiable) function of a convex set $\mathcal{C}$. In other words: where $\mathcal{C}$ is a convex set (defined by Eqs. 1-5), and where $\boldsymbol{\eta}(\boldsymbol{c})$ is differentiable. Fig. 13 shows two examples of such sets. In these cases, RAYEN is applied first to obtain a point $\boldsymbol{c}\in\mathcal{C}$, and then $\boldsymbol{y}=\boldsymbol{\eta}(\boldsymbol{c})$ is applied to obtain a point $\boldsymbol{y}\in\mathcal{Y}$. Backpropagation happens through both $\boldsymbol{\eta}(\cdot)$ and RAYEN.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Nonconvex Constraints", "weight": 1.0} -->

Note also that the function $\boldsymbol{\eta}(\cdot)$ could have some parameters that depend on the input or latent variable of the network.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Nonconvex Constraints", "weight": 1.0} -->

Moreover, and because of the way RAYEN works, it could also be applied to the cases where $\mathcal{Z}$ is a (potentially nonconvex) star-shaped set, as long as $\boldsymbol{z}_{0}$ is taken as the star point of $\mathcal{Z}$ (see, e.g., Krantz or Freitag and Busam ).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Nonconvex Constraints", "weight": 1.0} -->

Compared to methods such as DC3, one limitation of the proposed framework is that it currently does not support generic nonconvex constraints. However, as shown by the results in Section 6.1, when the constraints are convex the performance of our method is much better than.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Conclusion and Future work", "weight": 1.5} -->

This work presented RAYEN, a framework to impose hard convex constraints on the output or latent variable of a neural network. RAYEN is able to guarantee by construction the satisfaction of any combination of linear, convex quadratic, SOC, and LMI constraints. When applied to approximate the solution of constrained optimization problems, RAYEN showcases computation times between 20 and 7468 times faster than state-of-the-art algorithms, while guaranteeing the satisfaction of the constraints at all times and obtaining a loss very close to the optimal one.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Conclusion and Future work", "weight": 1.5} -->

Future work includes the application of RAYEN to non-fixed convex constraints (Section 7.1), and the incorporation of more types of convex constraints (such as, for example, exponential cone constraints). RAYEN could still be used for any convex constraint as long as the corresponding $\kappa_{\square}$ for that constraint can be found. Even if an analytic solution for $\kappa_{\square}$ does not exist, one could always leverage implicit layers that find the roots of nonlinear equations to numerically find it. We also plan to study how RAYEN could be used to impose generic nonconvex constraints (via, e.g., sequential convexification), to impose Lipschitz constraints, to impose generic matrix manifolds constraints, or leveraged for safe robot control.
