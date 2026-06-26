<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Micro Lie Theory for State Estimation in Robotics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A Lie group is an old mathematical abstract object dating back to the XIX century, when mathematician Sophus Lie laid the foundations of the theory of continuous transformation groups. As it often happens, its usage has spread over diverse areas of science and technology many years later. In robotics, we are recently experiencing an important trend in its usage, at least in the fields of estimation, and particularly in motion estimation for navigation. Yet for a vast majority of roboticians, Lie groups are highly abstract constructions and therefore difficult to understand and to use. This may be due to the fact that most of the literature on Lie theory is written by and for mathematicians and physicists, who might be more used than us to the deep abstractions this theory deals . In estimation for robotics it is often not necessary to exploit the full capacity of the theory, and therefore an effort of selection of materials is required. In this paper, we will walk through the most basic principles of the Lie theory, with the aim of conveying clear and useful ideas, and leave a significant corpus of the Lie theory behind.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Even with this mutilation, the material included here has proven to be extremely useful in modern estimation algorithms for robotics, especially in the fields of SLAM, visual odometry, and the like. Alongside this micro Lie theory, we provide a chapter with a few application examples, and a vast reference of formulas for the major Lie groups used in robotics, including most jacobian matrices and the way to easily manipulate them. We also present a new C++ template-only library implementing all the functionality described here.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has been a remarkable effort in the last years in the robotics community to formulate estimation problems properly. This is motivated by an increasing demand for precision, consistency and stability of the solutions. Indeed, proper modeling of the states and measurements, the functions relating them, and their uncertainties, is crucial to achieving these goals. This has led to designs involving what has been known as 'manifolds', which in this context are no less than the smooth topologic surfaces of the Lie groups where the state representations evolve. Relying on the Lie theory (LT) we are able to construct a rigorous calculus corpus to handle uncertainties, derivatives and integrals with precision and ease. Typically, these works have focused on the well-known manifolds of rotation SO and rigid motion SE.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

When being introduced to Lie groups for the first time, it is important to try to regard them from different points of view. The topological viewpoint, see Fig. 1, involves the shape of the manifold and conveys powerful intuitions of its relation to the tangent space and the exponential map. The algebraic viewpoint involves the group operations and their concrete realization, allowing the exploitation of algebraic properties to develop closed-form formulas or to simplify them. The geometrical viewpoint, particularly useful in robotics, associates group elements to the position, velocity, orientation, and/or other modifications of bodies or reference frames. The origin frame may be identified with the group's identity, and any other point on the manifold represents a certain 'local' frame. By resorting to these analogies, many mathematical abstractions of the LT can be brought closer to intuitive notions in vector spaces, geometry, kinematics, and other more classical fields.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lie theory is by no means simple. To grasp a minimum idea of what LT can be, we may consider the following three references. First, Abbaspour's *"Basic Lie theory"* comprises more than 400 pages. With a similar title, Howe's *"Very basic Lie theory"* comprises 24 (dense) pages, and is sometimes considered a must-read introduction. Finally, the more modern and often celebrated Stillwell's *"Naive Lie theory"* comprises more than 200 pages. With such precedents labeled as 'basic', 'very basic' and 'naive', the aim of this paper at merely LABEL:LastPage pages is to simplify Lie theory even more (thus our adjective 'micro' in the title). This we do in two ways. First, we select a small subset of material from the LT. This subset is so small that it merely explores the potential of LT. However, it appears very useful for uncertainty management in the kind of estimation problems we deal with in robotics (*e.g.* inertial pre-integration, odometry and SLAM, visual servoing, and the like), thus enabling elegant and rigorous designs of optimal optimizers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we explain it in a didactical way, with plenty of redundancy so as to reduce the entry gap to LT even more, which we believe is still needed. That is, we insist on the efforts in this direction of, to name a paradigmatic title, Stillwell's, and provide yet a more simplified version. The main text body is generic, though we try to keep the abstraction level to a minimum. Inserted examples serve as a grounding base for the general concepts when applied to known groups (rotation and motion matrices, quaternions, etc.). Also, plenty of figures with very verbose captions re-explain the same concepts once again. We put special attention to the computation of Jacobians (a topic that is not treated in ), which are essential for most optimal estimators and the source of much trouble when designing new algorithms. We provide a chapter with some applicative examples for robot localization and mapping, implementing EKF and nonlinear optimization algorithms based on LT.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

And finally, several appendices contain ample reference for the most relevant details of the most commonly used groups in robotics: unit complex numbers, quaternions, 2D and 3D rotation matrices, 2D and 3D rigid motion matrices, and the trivial translation groups.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet our most important simplification to Lie theory is in terms of scope. The following passage from Howe may serve us to illustrate what we leave behind: "*The essential phenomenon of Lie theory is that one may associate in a natural way to a Lie group $\mathcal{G}$ its Lie algebra $\mathfrak{g}$. The Lie algebra $\mathfrak{g}$ is first of all a vector space and secondly is endowed with a bilinear nonassociative product called the Lie bracket \[...\]. Amazingly, the group $\mathcal{G}$ is almost completely determined by $\mathfrak{g}$ and its Lie bracket. Thus for many purposes one can replace $\mathcal{G}$ with $\mathfrak{g}$. Since $\mathcal{G}$ is a complicated nonlinear object and $\mathfrak{g}$ is just a vector space, it is usually vastly simpler to work with $\mathfrak{g}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

\[...\] This is one source of the power of Lie theory.*" In, Stillwell even speaks of "*the miracle of Lie theory*". In this work, we will effectively relegate the Lie algebra to a second plane in favor of its equivalent vector space ${\mathbb{R}}^{n}$, and will not introduce the Lie bracket at all. Therefore, the connection between the Lie group and its Lie algebra will not be made here as profound as it should. Our position is that, given the target application areas that we foresee, this material is often not necessary. Moreover, if included, then we would fail in the objective of being clear and useful, because the reader would have to go into mathematical concepts that, by their abstraction or subtleness, are unnecessarily complicated.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our effort is in line with other recent works on the subject, which have also identified this need of bringing the LT closer to the roboticist. Our approach aims at appearing familiar to the target audience of this paper: an audience that is skilled in state estimation (Kalman filtering, graph-based optimization, and the like), but not yet familiar with the theoretical corpus of the Lie theory. We have for this taken some initiatives concerning notation, especially in the definition of the derivative, bringing it close to the vectorial counterparts, thus making the chain rule clearly visible. As said, we opted to practically avoid the material proper to the Lie algebra, and prefer instead to work on its isomorphic tangent vector space ${\mathbb{R}}^{n}$, which is where we ultimately represent uncertainty or (small) state increments. All these steps are undertaken with absolutely no loss in precision or exactness, and we believe they make the understanding of the LT and the manipulation of its tools easier.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is accompanied by a new open-source C++ header-only library, called manif, which can be found at manif implements the widely used groups $\text{SO}{}$, $\text{SO}{}$, $\text{SE}{}$ and $\text{SE}{}$, with support for the creation of analytic Jacobians. The library is designed for ease of use, flexibility, and performance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A The Lie group", "weight": 1.0} -->

The Lie group encompasses the concepts of *group* and *smooth manifold* in a unique body: a Lie group $\mathcal{G}$ is a smooth manifold whose elements satisfy the group axioms. We briefly present these two concepts before joining them together.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A The Lie group", "weight": 1.0} -->

On one hand, a differentiable or *smooth manifold* is a topological space that locally resembles linear space. The reader should be able to visualize the idea of manifold (Fig. 2): it is like a curved, smooth (hyper)-surface, with no edges or spikes, embedded in a space of higher dimension. In robotics, we say that our state vector evolves on this surface, that is, the manifold describes or is defined by the constraints imposed on the state. For example, vectors with the unit norm constraint define a spherical manifold of radius one. The smoothness of the manifold implies the existence of a unique tangent space at each point. This space is a linear or vector space on which we are allowed to do calculus.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A The Lie group", "weight": 1.0} -->

On the other hand, a *group* $(\mathcal{G}, \circ)$ is a set, $\mathcal{G}$, with a composition operation, $\circ$, that, for elements ${\mathcal{X},\mathcal{Y},\mathcal{Z}} \in \mathcal{G}$, satisfies the following axioms, In a *Lie group*, the manifold looks the same at every point (like *e.g.* in the surface of a sphere, see Exs. II-A and II-A), and therefore all tangent spaces at any point are alike. The group structure imposes that the composition of elements of the manifold remains on the manifold and that each element has an inverse also in the manifold,. A special one of these elements is the identity and thus a special one of the tangent spaces is the tangent at the identity, which we call the Lie algebra of the Lie group. Lie groups join the local properties of smooth manifolds, allowing us to do calculus, with the global properties of groups, enabling the nonlinear composition of distant objects.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B The group actions", "weight": 1.0} -->

Importantly, Lie groups come with the power to transform elements of other sets, producing *e.g.* rotations, translations, scalings, and combinations of them. These are extensively used in robotics, both in 2D and 3D.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B The group actions", "weight": 1.0} -->

Given a Lie group $\mathcal{M}$ and a set $\mathcal{V}$, we note $\mathcal{X} \cdot v$ the *action* of $\mathcal{X} \in \mathcal{M}$ on $v \in \mathcal{V}$, For $\cdot$ to be a group action, it must satisfy the axioms, Common examples are the groups of rotation matrices $\text{SO}{(n)}$, the group of unit quaternions, and the groups of rigid motion $\text{SE}{(n)}$. Their respective actions on vectors satisfy See Table I for a more detailed exposition, and the appendices.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B The group actions", "weight": 1.0} -->

$\exp\left(\begin{bmatrix} \lbrack{\mathbf{θ}}\rbrack_{\times} & {\mathbf{ρ}} \\\end{bmatrix} \right)$ Table I: Typical Lie groups used in 2D and 3D motion, including the trivial ℝn.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B The group actions", "weight": 1.0} -->

See the appendices for full reference The group composition may be viewed as an action of the group on itself, $\circ:\mathcal{M} \times \mathcal{M}\rightarrow\mathcal{M}$. Another interesting action is the *adjoint action*, which we will see in Section II-F.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C The tangent spaces and the Lie algebra", "weight": 1.0} -->

Given $\mathcal{X}{(t)}$ a point moving on a Lie group's manifold $\mathcal{M}$, its velocity $\overset{˙}{\mathcal{X}} = {\partial{\mathcal{X}/{\partial t}}}$ belongs to the space tangent to $\mathcal{M}$ at $\mathcal{X}$ (Fig. 2), which we note $T_{\mathcal{X}}\mathcal{M}$. The smoothness of the manifold, *i.e.*, the absence of edges or spikes, implies the existence of a unique tangent space at each point. The structure of such tangent spaces is the same everywhere.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C1 The Lie algebra $\\mathfrak{m}$", "weight": 1.0} -->

The tangent space at the identity, $T_{\mathcal{E}}\mathcal{M}$, is called the *Lie algebra* of $\mathcal{M}$, and noted $\mathfrak{m}$, Every Lie group has an associated Lie algebra. We relate the Lie group with its Lie algebra through the following facts (see Figs. 1 and 6): The Lie algebra $\mathfrak{m}$ is a vector space.^11^1In any Lie algebra, the vector space is endowed with a non-associative product called the Lie bracket. In this work, we will not make use of it. As such, its elements can be *identified* with vectors in ${\mathbb{R}}^{m}$, whose dimension $m$ is the number of degrees of freedom of $\mathcal{M}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C1 The Lie algebra $\\mathfrak{m}$", "weight": 1.0} -->

The *exponential map*, $\exp:{{\mathfrak{m}}\rightarrow\mathcal{M}}$, exactly converts elements of the Lie algebra into elements of the group. The log map is the inverse operation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C1 The Lie algebra $\\mathfrak{m}$", "weight": 1.0} -->

Vectors of the tangent space at $\mathcal{X}$ can be transformed to the tangent space at the identity $\mathcal{E}$ through a linear transform. This transform is called the *adjoint*.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C1 The Lie algebra $\\mathfrak{m}$", "weight": 1.0} -->

The structure of the Lie algebra can be found (see Examples II-C2 and II-D) by time-differentiating the group constraint. For multiplicative groups this yields the new constraint ${{\mathcal{X}^{- 1}\overset{˙}{\mathcal{X}}} + {\overset{˙}{\mathcal{X}^{-1}}\mathcal{X}}} = 0$, which applies to the elements tangent at $\mathcal{X}$ (the term $\overset{˙}{\mathcal{X}^{-1}}$ is the derivative of the inverse). The elements of the Lie algebra are therefore of the form,^22^2For additive Lie groups the constraint ${\mathcal{X} - \mathcal{X}} = 0$ differentiates to $\overset{˙}{\mathcal{X}} = \overset{˙}{\mathcal{X}}$, that is, no constraint affects the tangent space. This means that the tangent space is the same as the group space. See App.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C1 The Lie algebra $\\mathfrak{m}$", "weight": 1.0} -->

E and 𝑇⁢(𝑛) ‣ A micro Lie theory for state estimation in robotics") for more details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C2 The Cartesian vector space ${\\mathbb{R}}^{m}$", "weight": 1.0} -->

The elements ${\mathbf{τ}}^{\land}$ of the Lie algebra have non-trivial structures (skew-symmetric matrices, imaginary numbers, pure quaternions, see Table I) but the key aspect for us is that they can be expressed as linear combinations of some base elements $E_{i}$, where $E_{i}$ are called the *generators* of $\mathfrak{m}$ (they are the derivatives of $\mathcal{X}$ around the origin in the $i$-th direction). It is then handy to manipulate just the coordinates as vectors in ${\mathbb{R}}^{m}$, which we shall note simply $\mathbf{τ}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C2 The Cartesian vector space ${\\mathbb{R}}^{m}$", "weight": 1.0} -->

Vectors ${\mathbf{τ}} \in {\mathbb{R}}^{m}$ are handier for our purposes than their isomorphic ${\mathbf{τ}}^{\land} \in {\mathfrak{m}}$, since they can be stacked in larger state vectors, and more importantly, manipulated with linear algebra using matrix operators. In this work, we enforce this preference of ${\mathbb{R}}^{m}$ over $\mathfrak{m}$, to the point that most of the operators and objects that we define (specifically: the adjoint, the Jacobians, the perturbations and their covariances matrices, as we will see soon) are on ${\mathbb{R}}^{m}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C2 The Cartesian vector space ${\\mathbb{R}}^{m}$", "weight": 1.0} -->

[The rotation group SO, its Lie algebra 𝔰 𝔬, and the vector space ℝ3] In the rotation group SO, of 3 × 3 rotation matrices R, we have the orthogonality condition R⊤ R = I. The tangent space may be found by taking the time derivative of this constraint, that is ${{\mathbf{R}^{\top}\overset{˙}{\mathbf{R}}} + {{\overset{˙}{\mathbf{R}}}^{\top}\mathbf{R}}} = 0$, which we rearrange as $${{\mathbf{R}^{\top}\overset{˙}{\mathbf{R}}} = {- {({\mathbf{R}^{\top}\overset{˙}{\mathbf{R}}})}^{\top}}}.$$ This expression reveals that $\mathbf{R}^{\top}\overset{˙}{\mathbf{R}}$ is a skew-symmetric matrix (the negative of its transpose).

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C2 The Cartesian vector space ${\\mathbb{R}}^{m}$", "weight": 1.0} -->

Since [ω]× ∈ 𝔰 𝔬 has 3 DoF, the dimension of SO is m = 3. The Lie algebra is a vector space whose elements can be decomposed into with $\mathbf{E}_{x} = \begin{bmatrix} \end{bmatrix}$, $\mathbf{E}_{y} = \begin{bmatrix} \end{bmatrix}$, $\mathbf{E}_{z} = \begin{bmatrix} \end{bmatrix}$ the generators of 𝔰 𝔬, and where ω = (ωx, ωy, ωz) ∈ ℝ3 is the vector of angular velocities. The one-to-one linear relation above allows us to identify 𝔰 𝔬 with ℝ3 — we write 𝔰 𝔬 ≅ ℝ3. We pass from 𝔰 𝔬 to ℝ3 and viceversa using the linear operators hat and vee,

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

[The exponential map of SO] We have seen in Ex. II-C2 that ${\overset{˙}{\mathbf{R}} = {\mathbf{R}\lbrack{\mathbf{ω}}\rbrack_{\times}} \in {T_{\mathbf{R}}\text{SO}{}}}.$ For ω constant, this is an ordinary differential equation (ODE), whose solution is R (t) = R0 exp ([ω]× t). At the origin R0 = I we have the exponential map, We now define the vector θ ≜ u θ ≜ ω t ∈ ℝ3 as the integrated rotation in angle-axis form, with angle θ and unit axis u. Thus [θ]× ∈ 𝔰 𝔬 is the total rotation expressed in the Lie algebra. We substitute it above.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

{\lbrack\mathbf{u}\rbrack_{\times}^{2}\left({{{{\frac{1}{2}\theta^{2}} - {\frac{1}{4!}\theta^{4}}} + {\frac{1}{6!}\theta^{6}}} - \cdots} \right)}},$ where we identify the series of sin θ and cos θ, yielding the closed form, This expression is the well known Rodrigues rotation formula. It can be used as the capitalized exponential just by doing R = Exp (u θ) = exp ([u θ]×).

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

The exponential map $\exp{}$ allows us to exactly transfer elements of the Lie algebra to the group (Fig. 1), an operation generically known as *retraction*. Intuitively, $\exp{}$ wraps the tangent element around the manifold following the great arc or *geodesic* (as when wrapping a string around a ball, Figs. 1, 3 and 4). The inverse map is the $\log{}$, *i.e.*, the unwrapping operation. The $\exp{}$ map arises naturally by considering the time-derivatives of $\mathcal{X} \in \mathcal{M}$ over the manifold, as follows.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

From we have, For $\mathbf{v}$ constant, this is an ordinary differential equation (ODE) whose solution is Since $\mathcal{X}{(t)}$ and $\mathcal{X}{}$ are elements of the group, then ${\exp{({\mathbf{v}^{\land}t})}} = {\mathcal{X}{}^{- 1}\mathcal{X}{(t)}}$ must be in the group too, and so $\exp{({\mathbf{v}^{\land}t})}$ maps elements $\mathbf{v}^{\land}t$ of the Lie algebra to the group. This is known as the *exponential map*.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

In order to provide a more generic definition of the exponential map, let us define the tangent increment ${\mathbf{τ}} \triangleq {\mathbf{v}t} \in {\mathbb{R}}^{m}$ as velocity per time, so that we have ${\mathbf{τ}}^{\land} = {\mathbf{v}^{\land}t} \in {\mathfrak{m}}$ a point in the Lie algebra. The exponential map, and its inverse the logarithmic map, can be now written as, Closed forms of the exponential in multiplicative groups are obtained by writing the absolutely convergent Taylor series, and taking advantage of the algebraic properties of the powers of ${\mathbf{τ}}^{\land}$ (see Ex. II-D and II-D for developments of the exponential map in $\text{SO}{}$ and $S^{3}$). These are then inverted to find the logarithmic map.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

Key properties of the exponential map are where, a surprising and powerful statement, can be proved easily by expanding the Taylor series and simplifying the many terms $\mathcal{X}^{- 1}\mathcal{X}$. [The unit quaternions group S3 (cont.)] In the group S3 (recall Ex. II-A and see e.g.), the time derivative of the unit norm condition q* q = 1 yields $${{\mathbf{q}^{\ast}\overset{˙}{\mathbf{q}}} = {- {({\mathbf{q}^{\ast}\overset{˙}{\mathbf{q}}})}^{\ast}}}.$$ This reveals that $\mathbf{q}^{\ast}\overset{˙}{\mathbf{q}}$ is a pure quaternion (its real part is zero).

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

Pure quaternions u v ∈ ℍp have the form where u ≜ i ux + j uy + k uz is pure and unitary, v is the norm, and i, j, k are the generators of the Lie algebra 𝔰3 = ℍp. Re-writing the condition above we have, $\overset{˙}{\mathbf{q}} = {\mathbf{q}\mathbf{u}v}$ which integrates to q = q0 exp (u v t). Letting q0 = 1 and defining ϕ ≜ u ϕ ≜ u v t we get the exponential map, $\mathbf{q} = {\exp{({\mathbf{u}\phi})}} \triangleq {\sum{\frac{\phi^{k}}{k!}\mathbf{u}^{k}}}$ The powers of u follow the pattern 1, u, −1, −u, 1, ⋯. Thus we group the terms in 1 and u and identify the series of cos ϕ and sin ϕ.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-D The exponential map", "weight": 1.0} -->

We get the closed form, q = exp (u ϕ) = cos (ϕ) + u sin (ϕ), which is a beautiful extension of the Euler formula, exp (i ϕ) = cos ϕ + i sin ϕ. The elements of the Lie algebra ϕ = u ϕ ∈ 𝔰3 can be identified with the rotation vector θ ∈ ℝ3 trough the mappings hat and vee, where the factor 2 accounts for the double effect of the quaternion in the rotation action, x′ = q x q*. With this choice of Hat and Vee, the quaternion exponential q = Exp (u θ) = cos (θ/2) + u sin (θ/2) is equivalent to the rotation matrix R = Exp (u θ).

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-D1 The capitalized exponential map", "weight": 1.0} -->

The capitalized Exp and Log maps are convenient shortcuts to map vector elements ${\mathbf{τ}} \in {{\mathbb{R}}^{m}\mspace{7mu}{({\cong {T_{\mathcal{E}}\mathcal{M}}})}}$ directly with elements $\mathcal{X} \in \mathcal{M}$. We have, Clearly from Fig. 6, See the Appendices for details on the implementation of these maps for different manifolds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-E Plus and minus operators", "weight": 1.0} -->

Plus and minus allow us to introduce increments between elements of a (curved) manifold, and express them in its (flat) tangent vector space. Denoted by $\oplus$ and $\ominus$, they combine one Exp/Log operation with one composition. Because of the non-commutativity of the composition, they are defined in right- and left- versions depending on the order of the operands.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-E Plus and minus operators", "weight": 1.0} -->

The right operators are (see Fig. 4-*right*), Because in $\operatorname{Exp}{({{}_{}^{\mathcal{X}}{\mathbf{τ}}})}$ appears at the right hand side of the composition, ${}_{}^{\mathcal{X}}{\mathbf{τ}}$ belongs to the tangent space at $\mathcal{X}$ (see): we say by convention^33^3The convention sticks to that of frame transformation, *e.g.* ${{}_{}^{G}\mathbf{x}} = {\mathbf{R}^{L}\mathbf{x}}$, where the matrix $\mathbf{R} \in {\text{SO}{}}$ transforms local vectors into global. Notice that this convention is not shared by all authors, and for example uses the opposite, ${{}_{}^{L}\mathbf{x}} = {\mathbf{R}^{G}\mathbf{x}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-E Plus and minus operators", "weight": 1.0} -->

that ${}_{}^{\mathcal{X}}{\mathbf{τ}}$ is expressed in the *local* frame at $\mathcal{X}$ --- we note reference frames with a left superscript.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-E Plus and minus operators", "weight": 1.0} -->

Notice that while left- and right- $\oplus$ are distinguished by the operands order, the notation $\ominus$ in and is ambiguous. In this work, we express perturbations locally by default and therefore we use the right- forms of $\oplus$ and $\ominus$ by default.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-G Derivatives on Lie groups", "weight": 1.0} -->

Among the different ways to define derivatives in the context of Lie groups, we concentrate on those in the form of Jacobian matrices mapping vector tangent spaces. This is sufficient here since in these spaces uncertainties and increments can be properly and easily defined. Using these Jacobians, the formulas for uncertainty management in Lie groups will largely resemble those in vector spaces.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-G Derivatives on Lie groups", "weight": 1.0} -->

The Jacobians described hereafter fulfill the chain rule, so that we can easily compute any Jacobian from the partial Jacobian blocks of *inversion*, *composition*, *exponentiation* and *action*. See Section III-A for details and proofs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "II-G1 Reminder: Jacobians on vector spaces", "weight": 1.0} -->

This column vector responds to where $\mathbf{e}_{i}$ is the $i$-th vector of the natural basis of ${\mathbb{R}}^{m}$. Regarding the numerator, notice that the vector is the variation of $f{(\mathbf{x})}$ when $\mathbf{x}$ is perturbed in the direction of $\mathbf{e}_{i}$, and that the respective Jacobian column is just $\mathbf{j}_{i} = {{\partial{{\mathbf{v}_{i}{(h)}}/{\partial h}}}|}_{h = 0} = {\lim_{h\rightarrow 0}{{\mathbf{v}_{i}{(h)}}/h}}$. In this work, for the sake of convenience, we introduce the compact form, with $\mathbf{h} \in {\mathbb{R}}^{m}$, which aglutinates all columns to form the definition of.

<!-- chunk {"id": "body-0046", "role": "body", "section": "II-G1 Reminder: Jacobians on vector spaces", "weight": 1.0} -->

We remark that is just a notation convenience (just as is), since division by the vector $\mathbf{h}$ is undefined and proper computation requires. However, this form may be used to calculate Jacobians by developing the numerator into a form linear in $\mathbf{h}$, and identifying the left hand side as the Jacobian, that is, Notice finally that for small values of $\mathbf{h}$ we have the linear approximation,

<!-- chunk {"id": "body-0047", "role": "body", "section": "II-G2 Right Jacobians on Lie goups", "weight": 1.0} -->

Inspired by the standard derivative definition above, we can now use our $\oplus$ and $\ominus$ operators to define Jacobians of functions $f:{\mathcal{M}\rightarrow\mathcal{N}}$ acting on manifolds (see Fig. 8). Using the right- $\{ \oplus, \ominus \}$ in place of $\{ +, - \}$ we obtain a form akin to the standard derivative,^44^4The notation $\frac{D\mathcal{Y}}{D\mathcal{X}} = \frac{Df{(\mathcal{X})}}{D\mathcal{X}}$ is chosen in front of other alternatives in order to make the chain rule readable, *i.e.*, $\frac{D\mathcal{Z}}{D\mathcal{X}} = {\frac{D\mathcal{Z}}{D\mathcal{Y}}\frac{D\mathcal{Y}}{D\mathcal{X}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "II-G2 Right Jacobians on Lie goups", "weight": 1.0} -->

We call this Jacobian the *right Jacobian of $f$*. Notice that (41c) is just the standard derivative of the rather complicated function ${g{({\mathbf{τ}})}} = {\operatorname{Log}\left({{{f{(\mathcal{X})}^{- 1}} \circ f}{({\mathcal{X} \circ {\operatorname{Exp}{({\mathbf{τ}})}}})}} \right)}$. Writing it as in (41a) conveys much more intuition: it is the derivative of $f{(\mathcal{X})}$ with respect to $\mathcal{X}$, only that we expressed the infinitesimal variations in the tangent spaces!

<!-- chunk {"id": "body-0049", "role": "body", "section": "II-G2 Right Jacobians on Lie goups", "weight": 1.0} -->

Indeed, thanks to the way right- $\oplus$ and $\ominus$ operate, variations in $\mathcal{X}$ and $f{(\mathcal{X})}$ are now expressed as vectors in the local tangent spaces, *i.e.*, tangent respectively at $\mathcal{X} \in \mathcal{M}$ and ${f{(\mathcal{X})}} \in \mathcal{N}$. This derivative is then a proper Jacobian matrix ${\mathbb{R}}^{n \times m}$ linearly mapping the *local* tangent spaces ${T_{\mathcal{X}}\mathcal{M}}\rightarrow{T_{f{(\mathcal{X})}}\mathcal{N}}$ (and we mark the derivative with a local '$\mathcal{X}$' superscript). Just as in vector spaces, the columns of this matrix correspond to directional derivatives.

<!-- chunk {"id": "body-0050", "role": "body", "section": "II-G2 Right Jacobians on Lie goups", "weight": 1.0} -->

As before, we use (41a) to actually find Jacobians by resorting to the same mechanism. For example, for a 3D rotation $f:{{{\text{SO}{}}\rightarrow{\mathbb{R}}^{3}};{{f{(\mathbf{R})}} = {\mathbf{R}\mathbf{p}}}}$, we have $\mathcal{M} = {\text{SO}{}}$ and $\mathcal{N} = {\mathbb{R}}^{3}$ and so (see App. B-C5 ‣ A micro Lie theory for state estimation in robotics")), Many examples of this mechanism can be observed in Section III and the appendices. Remark that whenever the function $f$ passes from one manifold to another, the plus and minus operators in (41a) must be selected appropriately: $\oplus$ for the domain $\mathcal{M}$, and $\ominus$ for the codomain or image $\mathcal{N}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "II-G2 Right Jacobians on Lie goups", "weight": 1.0} -->

For small values of $\mathbf{τ}$, the following approximation holds,

<!-- chunk {"id": "body-0052", "role": "body", "section": "II-G3 Left Jacobians on Lie groups", "weight": 1.0} -->

Derivatives can also be defined from the left- plus and minus operators, leading to, which we call the *left Jacobian of $f$*. Notice that now ${\mathbf{τ}} \in {T_{\mathcal{E}}\mathcal{M}}$, and the numerator belongs to $T_{\mathcal{E}}\mathcal{N}$, thus the left Jacobian is a $n \times m$ matrix mapping the *global* tangent spaces, ${T_{\mathcal{E}}\mathcal{M}}\rightarrow{T_{\mathcal{E}}\mathcal{N}}$, which are the Lie algebras of $\mathcal{M}$ and $\mathcal{N}$ (and we mark the derivative with a global or origin '$\mathcal{E}$' superscript). For small values of $\mathbf{τ}$ the following holds, Figure 9: Linear maps between all tangent spaces involved in a function 𝒴 = f (𝒳), from ℳ to 𝒩.

<!-- chunk {"id": "body-0053", "role": "body", "section": "II-G3 Left Jacobians on Lie groups", "weight": 1.0} -->

We can show from (see Fig. 9) that left and right Jacobians are related by the adjoints of $\mathcal{M}$ and $\mathcal{N}$,

<!-- chunk {"id": "body-0054", "role": "body", "section": "II-G4 Crossed right--left Jacobians", "weight": 1.0} -->

One can also define Jacobians using right-plus but left-minus, or vice versa. Though improbable, these are sometimes useful, since they map local to global tangents or vice versa. To keep it short, we will just relate them to the other Jacobians through the adjoints, where $\mathcal{Y} = {f{(\mathcal{X})}}$. Now, the upper and lower super-scripts indicate the reference frames where the differentials are expressed. Respective small-tau approximations read,

<!-- chunk {"id": "body-0055", "role": "body", "section": "II-H Uncertainty in manifolds, covariance propagation", "weight": 1.0} -->

We define local perturbations $\mathbf{τ}$ around a point $\overline{\mathcal{X}} \in \mathcal{M}$ in the tangent vector space $T_{\overline{\mathcal{X}}}\mathcal{M}$, using right- $\oplus$ and $\ominus$, Covariances matrices can be properly defined on this tangent space at $\overline{\mathcal{X}}$ through the standard expectation operator ${\mathbb{E}}{\lbrack \cdot \rbrack}$, allowing us to define Gaussian variables on manifolds, $\mathcal{X} \sim {\mathcal{N}{(\overline{\mathcal{X}},\mathbf{\Sigma}_{\mathcal{X}})}}$, see Fig. 10. Notice that although we write $\mathbf{\Sigma}_{\mathcal{X}}$, the covariance is rather that of the tangent perturbation $\mathbf{τ}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "II-H Uncertainty in manifolds, covariance propagation", "weight": 1.0} -->

Perturbations can also be expressed in the global reference, that is, in the tangent space at the origin $T_{\mathcal{E}}\mathcal{M}$, using left- $\oplus$ and $\ominus$, This allows global specification of covariance matrices using left-minus. For example, a 3D orientation that is known up to rotations in the horizontal plane can be associated to a covariance ${{}_{}^{\mathcal{E}}\mathbf{\Sigma}} = {\operatorname{diag}{(\sigma_{\phi}^{2},\sigma_{\theta}^{2},\infty)}}$. Since "horizontal" is a global specification, ${}_{}^{\mathcal{E}}\mathbf{\Sigma}$ must be specified in the global reference.

<!-- chunk {"id": "body-0057", "role": "body", "section": "II-H Uncertainty in manifolds, covariance propagation", "weight": 1.0} -->

Since global and local perturbations are related by the adjoint, their covariances can be transformed with Covariance propagation through a function $f:{{\mathcal{M}\rightarrow\mathcal{N}};{\mathcal{X}\mapsto\mathcal{Y} = {f{(\mathcal{X})}}}}$ just requires the linearization with Jacobian matrices (41a) to yield the familiar formula,

<!-- chunk {"id": "body-0058", "role": "body", "section": "II-I Discrete integration on manifolds", "weight": 1.0} -->

{\mathbf{τ}}_{2} \oplus \cdots \oplus {\mathbf{τ}}_{k}}}.$ We write all these variants in recursive form, Figure 11: Motion integration on a manifold.

<!-- chunk {"id": "body-0059", "role": "body", "section": "II-I Discrete integration on manifolds", "weight": 1.0} -->

Each motion data produces a step τk ∈ T𝒳k − 1 ℳ, which is wrapped to a local motion increment or ‘delta’ δk = Exp (τk) ∈ ℳ, and then composed with 𝒳k − 1 to yield 𝒳k = 𝒳k − 1 ∘ δk = 𝒳k − 1 ∘ Exp (τk) = 𝒳k − 1 ⊕ τk ∈ ℳ.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Differentiation rules on manifolds", "weight": 1.0} -->

For all the typical manifolds $\mathcal{M}$ that we use, we can determine closed forms for the elementary Jacobians of *inversion*, *composition*, *exponentiation* and *action*. Moreover, some of these forms can be related to the adjoint ${\mathbf{A}\mathbf{d}}_{\mathcal{X}}$, which becomes a central block of the differentiation process. Other forms for $\operatorname{Log}$, $\oplus$ and $\ominus$ can be easily derived from them. Once these forms or 'blocks' are found, all other Jacobians follow by the chain rule. Except for the so-called *left Jacobian*, which we also present below, all Jacobians developed here are right-Jacobians, *i.e.*, defined by (41a). By following the hints here, the interested reader should find no particular difficulties in developing the left-Jacobians.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-A The chain rule", "weight": 1.0} -->

Notice that when mixing right, left and crossed Jacobians, we need to chain also the reference frames, as in *e.g.* where the first identity of is proven by writing, and identifying in the first and third rows.

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-B3 Jacobians of $\\mathcal{M}$", "weight": 1.0} -->

We define the *right Jacobian of $\mathcal{M}$* as the right Jacobian of $\mathcal{X} = {\operatorname{Exp}{({\mathbf{τ}})}}$, *i.e.*, for ${\mathbf{τ}} \in {\mathbb{R}}^{m}$, which is defined with (41a). The right Jacobian maps variations of the argument $\mathbf{τ}$ into variations in the *local* tangent space at $\operatorname{Exp}{({\mathbf{τ}})}$. From (41a) it is easy to prove that, for small $\delta{\mathbf{τ}}$, the following approximations hold, Complementarily, the *left Jacobian of $\mathcal{M}$* is defined, using the left Jacobian, leading to the approximations The left Jacobian maps variations of the argument $\mathbf{τ}$ into variations in the *global* tangent space or Lie algebra.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-B3 Jacobians of $\\mathcal{M}$", "weight": 1.0} -->

From we can relate left- and right- Jacobians with the adjoint, Also, the chain rule allows us to relate $\mathbf{J}_{r}$ and $\mathbf{J}_{l}$, Closed forms of $\mathbf{J}_{r}$, ${}\mathbf{J}_{r}^{- 1}$, $\mathbf{J}_{l}$ and ${}\mathbf{J}_{l}^{- 1}$ exist for the typical manifolds in use. See the appendices for reference.

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-B4 Group action", "weight": 1.0} -->

For $\mathcal{X} \in \mathcal{M}$ and $v \in \mathcal{V}$, we define with (41a) Since group actions depend on the set $\mathcal{V}$, these expressions cannot be generalized. See the appendices for reference.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Composite manifolds", "weight": 1.0} -->

At the price of losing some consistency with the Lie theory, but at the benefit of obtaining some advantages in notation and manipulation, one can consider large and heterogeneous states as manifold composites (or bundles).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Composite manifolds", "weight": 1.0} -->

We consider the space of translations t ∈ ℝn and rotations R ∈ SO (n). We have for this the well-known SE (n) manifold of rigid motions $\mathbf{M} = \begin{bmatrix} \end{bmatrix}$ (see Apps. C and D), which can also be constructed as T (n) × SO (n) (see Apps. A, B and E). These two are very similar, but have different tangent parametrizations: while SE (n) uses τ = (θ, ρ) with M = exp (τ∧), T (n) × SO (n) uses τ = (θ, p) with M = exp (p∧) exp (θ∧). They share the rotational part θ, but clearly ρ ≠ p (see [11, pag. 35] for further details). In short, SE (n) performs translation and rotation simultaneously as a continuum, while T (n) × SO (n) performs chained translation+rotation. In radical contrast, in the composite ⟨ℝn, SO (n)⟩ rotations and translations do not interact at all.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Composite manifolds", "weight": 1.0} -->

By combining composition with Exp we obtain the (right) plus operators, {\mathbf{R}{\operatorname{Exp}{({\mathbf{θ}})}}} & {\mathbf{t} + {{\mathbf{R}\mathbf{V}}{({\mathbf{θ}})}{\mathbf{ρ}}}} \\{\mathbf{R}{\operatorname{Exp}{({\mathbf{θ}})}}} & {\mathbf{t} + {\mathbf{R}\mathbf{p}}} \\{\mathbf{R}{\operatorname{Exp}{({\mathbf{θ}})}}} where either ⊕ may be used for the system dynamics, e.g. motion integration, but usually not * X, which might however be used to model perturbations.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Composite manifolds", "weight": 1.0} -->

This makes * X, * X valuable operators for computing derivatives and covariances.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Composite manifolds", "weight": 1.0} -->

A *composite manifold* $\mathcal{M} = {\langle\mathcal{M}_{1},\cdots,\mathcal{M}_{M}\rangle}$ is no less than the concatenation of $M$ non-interacting manifolds. This stems from defining identity, inverse and composition acting on each block of the composite separately, thereby fulfilling the group axioms, as well as a non-interacting retraction map, which we will also note as "exponential map" for the sake of unifying notations (notice the angled brackets), thereby ensuring smoothness. These yield the composite's right- plus and minus (notice the diamond symbols), The key consequence of these considerations (see Ex. IV) is that new derivatives can be defined,^66^6We assume here right derivatives, but the same applies to left derivatives.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Composite manifolds", "weight": 1.0} -->

using ${\ast}X{}$ and ${\ast}X{}$, With this derivative, Jacobians of functions $f:{\mathcal{M}\rightarrow\mathcal{N}}$ acting on composite manifolds can be determined in a per-block basis, which yields simple expressions requiring only knowledge on the manifold blocks of the composite, where $\frac{Df_{i}}{D\mathcal{X}_{j}}$ are each computed with (41a). For small values of $\mathbf{τ}$ the following holds, When using these derivatives, covariances and uncertainty propagation must follow the convention. In particular, the covariance matrix becomes for which the linearized propagation using applies.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Landmark-based localization and mapping", "weight": 1.0} -->

We provide three applicative examples of the theory for robot localization and mapping. The first one is a Kalman filter for landmark-based localization. The second one is a graph-based smoothing method for simultaneous localization and mapping. The third one adds sensor self-calibration. They are based on a common setup, explained as follows.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Landmark-based localization and mapping", "weight": 1.0} -->

We consider a robot in the plane (see Section V-D for the 3D case) surrounded by a small number of punctual landmarks or *beacons*. The robot receives control actions in the form of axial and angular velocities and is able to measure the location of the beacons with respect to its own reference frame.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Landmark-based localization and mapping", "weight": 1.0} -->

The robot pose is in $\text{SE}{}$ (App. C ‣ A micro Lie theory for state estimation in robotics")) and the beacon positions in ${\mathbb{R}}^{2}$ (App. E and 𝑇⁢(𝑛) ‣ A micro Lie theory for state estimation in robotics")), The control signal $\mathbf{u}$ is a twist in ${\mathfrak{s}}{\mathfrak{e}}{}$ comprising longitudinal velocity $v$ and angular velocity $\omega$, with no lateral velocity component, integrated over the sampling time $\deltat$. The control is corrupted by additive Gaussian noise $\mathbf{w} \sim {\mathcal{N}{(\mathbf{0},\mathbf{W})}}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Landmark-based localization and mapping", "weight": 1.0} -->

This noise accounts for possible lateral wheel slippages $u_{s}$ through a value of $\sigma_{s} \neq 0$, At the arrival of a control $\mathbf{u}_{j}$ at time $j$, the robot pose is updated, Landmark measurements are of the range and bearing type, though they are put in Cartesian form for simplicity. Their noise $\mathbf{n} \sim {\mathcal{N}{(\mathbf{0},\mathbf{N})}}$ is zero mean Gaussian, where we notice the rigid motion action $\mathcal{X}^{- 1} \cdot \mathbf{b}_{k}$ (see App. C ‣ A micro Lie theory for state estimation in robotics")).

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-A Localization with error-state Kalman filter on manifold", "weight": 1.0} -->

We initially consider the beacons $\mathbf{b}_{k}$ situated at known positions. We define the pose to estimate as $\hat{\mathcal{X}} \in {\text{SE}{}}$. The estimation error $\delta\mathbf{x}$ and its covariance $\mathbf{P}$ are expressed in the tangent space at $\hat{\mathcal{X}}$, At each robot motion we apply ESKF prediction, with the Jacobians computed from the blocks in App. C ‣ A micro Lie theory for state estimation in robotics"), At each beacon measurement $\mathbf{y}_{k}$ we apply ESKF correction, with the Jacobian computed from the blocks in App. C ‣ A micro Lie theory for state estimation in robotics"), Notice that the only changes with respect to a regular EKF are in and, where regular $+$ are substituted by $\oplus$. The Jacobians on the contrary are all computed using the Lie theory (see App. C ‣ A micro Lie theory for state estimation in robotics")).

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-A Localization with error-state Kalman filter on manifold", "weight": 1.0} -->

Interstingly, their usage is the same as in standard EKF --- see *e.g.* the equation of the Kalman gain, which is the standard $\mathbf{K} = {{\mathbf{P}\mathbf{H}}^{\top}{({{\mathbf{H}\mathbf{P}\mathbf{H}}^{\top} + \mathbf{N}})}^{- 1}}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-B Smooting and Mapping with graph-based optimization", "weight": 1.0} -->

We consider now the problem of smoothing and mapping (SAM), where the variables to estimate are the beacons' locations and the robot's trajectory. The solver of choice is a graph-based iterative least-squares optimizer. For simplicity, we assume the trajectory comprised of three robot poses $\{{\mathcal{X}_{1}\cdots\mathcal{X}_{3}}\}$, and a world with three beacons $\{{\mathbf{b}_{4}\cdots\mathbf{b}_{6}}\}$. The problem state is the composite The resulting factor graph is shown in Fig. 12. Each prior or measurement contributes a factor in the graph. Motion measurements from pose $i$ to $j$ are derived, while measurements of beacon $k$ from pose $i$ respond to, Figure 12: SAM factor graph with 3 poses and 3 beacons. Each measurement contributes a factor in the graph. There are 2 motion factors (black) and 5 beacon factors (gray). A prior factor on 𝒳1 provides global observability.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B Smooting and Mapping with graph-based optimization", "weight": 1.0} -->

We highlight here the use of the composite notation, which allows block-wise definitions of the Jacobian and the update. We also remark the use of the $\text{SE}{}$ manifold in the motion and measurement models, as we did in the ESKF case in Section V-A.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C Smoothing and mapping with self-calibration", "weight": 1.0} -->

We define the bias correction function $c{}$, The state composite is augmented with the unknowns $\mathbf{c}$, and the motion residual becomes The procedure is as in Section V-B above, and just the total Jacobian is modified with an extra column on the left, where $\mathbf{J}_{\mathbf{c}}^{\mathbf{r}_{ij}} = {\mathbf{\Omega}_{ij}^{\top{/2}}\mathbf{J}_{\mathbf{c}}^{c{(\mathbf{u}_{ij},\mathbf{c})}}}$, with $\mathbf{J}_{\mathbf{c}}^{c{(\mathbf{u}_{ij},\mathbf{c})}}$ the $3 \times 2$ Jacobian of. The optimal solution is obtained.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C Smoothing and mapping with self-calibration", "weight": 1.0} -->

The resulting optimal state $\mathcal{X}$ includes an optimal estimate of $\mathbf{c}$, that is, the self-calibration of the sensor bias.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-D 3D implementations", "weight": 1.0} -->

It is surprisingly easy to bring all the examples above to 3D. It suffices to define all variables in the correct spaces: $\mathcal{X} \in {\text{SE}{}}$ and $\mathbf{u} \in {\mathbb{R}}^{6} \cong {{\mathfrak{s}}{\mathfrak{e}}{}}$ (App. D ‣ A micro Lie theory for state estimation in robotics")), and ${\{\mathbf{b}_{k},\mathbf{y}\}} \in {\mathbb{R}}^{3}$ (App. E and 𝑇⁢(𝑛) ‣ A micro Lie theory for state estimation in robotics")). Jacobians and covariances matrices will follow with appropriate sizes. The interest here is in realizing that all the math in the algorithms, that is from onwards, is exactly the same for 2D and 3D: the abstraction level provided by the Lie theory has made this possible.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented the essential of Lie theory in a form that should be useful for an audience skilled in state estimation, with a focus on robotics applications. This we have done through several initiatives: First, a selection of materials that avoids abstract mathematical concepts as much as possible. This helps to focus Lie theory to make its tools easier to understand and to use.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Second, we chose a didactical approach, with significant redundancy. The main text is generic and covers the abstract points of Lie theory. It is accompanied by boxed examples, which ground the abstract concepts to particular Lie groups, and plenty of figures with very verbose captions.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Third, we have promoted the usage of handy operators, such as the capitalized $\operatorname{Exp}{}$ and $\operatorname{Log}{}$ maps, and the plus and minus operators $\oplus, \ominus,{{\ast}X{}},{{\ast}X{}}$. They allow us to work on the Cartesian representation of the tangent spaces, producing formulas for derivatives and covariance handling that greatly resemble their counterparts in standard vector spaces.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Fourth, we have made special emphasis on the definition, geometrical interpretation, and computation of Jacobians. For this, we have introduced notations for the Jacobian matrices and covariances that allow a manipulation that is visually powerful. In particular, the chain rule is clearly visible with this notation. This helps to build intuition and reducing errors.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Fifth, we present in the appendices that follow an extensive compendium of formulas for the most common groups in robotics. In 2D, we present the rotation groups of unit complex numbers $S^{1}$ and rotation matrices $\text{SO}{}$, and the rigid motion group $\text{SE}{}$. In 3D, we present the groups of unit quaternions $S^{3}$ and rotation matrices $\text{SO}{}$, both used for rotations, and the rigid motion group $\text{SE}{}$. We also present the translation groups for any dimension, which can be implemented by either the standard vector space ${\mathbb{R}}^{n}$ under addition, or by the matrix translation group $T{(n)}$ under multiplication.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Sixth, we have presented some applicative examples to illustrate the capacity of Lie theory to solve robotics problems with elegance and precision. The somewhat naive concept of composite group helps to unify heterogeneous state vectors into a Lie-theoretic form.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, we accompany this text with the new C++ library manif implementing the tools described here. manif can be found at The applications in Section V are demonstrated in manif as examples.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Though we do not introduce any new theoretical material, we believe the form in which Lie theory is here exposed will help many researchers enter the field for their future developments. We also believe this alone represents a valuable contribution.
