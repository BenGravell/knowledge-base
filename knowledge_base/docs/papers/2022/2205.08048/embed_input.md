<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Short Introduction to the Koopman Representation of Dynamical Systems

Topics include Online algorithms, Dynamic mode decomposition, AKA, Dynamical systems, Transfer operator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Koopman representation is an infinite dimensional linear representation of linear or nonlinear dynamical systems. It represents the dynamics of output maps (aka observables), which are functions on the state space whose evaluation is interpreted as an output. Conceptually simple derivations and commentary on the Koopman representation are given. We emphasize an important duality between initial conditions and output maps of the original system, and those of the Koopman representation. This duality is an important consideration when this representation is used in data-driven applications such as the Dynamic Mode Decomposition (DMD) and its variants. The adjoint relation between the Koopman representation and the transfer operator of mass transport is also shown.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

The Koopman representation is an infinite dimensional linear representation of linear or nonlinear dynamical systems. It represents the dynamics of output maps (aka observables), which are functions on the state space whose evaluation is interpreted as an output. Conceptually simple derivations and commentary on the Koopman representation are given. We emphasize an important duality between initial conditions and output maps of the original system, and those of the Koopman representation. This duality is an important consideration when this representation is used in data-driven applications such as the Dynamic Mode Decomposition (DMD) and its variants. The adjoint relation between the Koopman representation and the transfer operator of mass transport is also shown.

<!-- chunk {"id": "body-0004", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

The simplest approach to define the Koopman representation is in a general and abstract manner using the flow map of a dynamical system. This conceptually simple approach clarifies some of the properties of the representation without getting sidetracked by the details of the underlying differential or difference equations, or modal and spectral decompositions. Those should be introduced after the basic features and properties of the representation are established.

<!-- chunk {"id": "body-0005", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

Consider a continuous (or discrete) time dynamical system written abstractly where at each time, $x_{t} \in \mathbf{X}$, the state space, $y_{t} \in \mathbf{Y}$, the output space, the mapping $f:{\mathbf{X}\rightarrow\mathbf{X}}$ is a vector field that generates the dynamics (or the one-step iteration in the discrete-time case), and the mapping $\overline{G}:{\mathbf{X}\rightarrow\mathbf{Y}}$ is the output (i.e. "readout") mapping if the state is not directly observed, but only through the output variables $y_{t}$. If the state is directly observed, then the mapping $\overline{G}$ is simply the identity mapping. The spaces $\mathbf{X}$ and $\mathbf{Y}$ might be in ${\mathbb{R}}^{n}$ for finite vector states, or some function space when the states and outputs are spatial fields.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

In other treatments of the Koopman representation, the output equation is typically ignored. A point I would like to make here is that it crucial to include it even if the state is directly observed. The reason for denoting the output mapping $\overline{G}$ with an overbar notation will become clear shortly.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

If this equation represents a well-posed dynamical system, then there is a family (parameterized by $t$) of flow maps $\mathcal{F}_{t}:{\mathbf{X}\rightarrow\mathbf{X}}$ such that which map the initial condition $\overline{x}$ to the solution $x_{t}$ at time $t$. The family $\left\{ \mathcal{F}_{t} \right\}$ satisfies the semigroup property $\mathcal{F}_{t_{1} + t_{2}} = {\mathcal{F}_{t_{1}} \circ \mathcal{F}_{t_{2}}}$, where $\circ$ is function composition.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

The evolution of the output starting from any initial condition $\overline{x}$ is then given by applying the output mapping to the state The key idea of the Koopman representation is to "flip the roles" of $\overline{G}$ and $\overline{x}$ in the above equation, i.e. regard evaluation at $\overline{x}$ as an output map, regard $\overline{G}$ as an initial state, and evolve $G$ rather than $x$ in time. Specifically, define the operator family $\left\{ \mathcal{K}_{t} \right\}$ by For each $t$, the operator $\mathcal{K}_{t}$ acts on the space $\mathcal{M}(\mathbf{X},\mathbf{Y})$ of all observation maps $G:{\mathbf{X}\rightarrow\mathbf{Y}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

Note that $\mathcal{K}_{t}G$ is the pullback of $\overline{G}$ by $\mathcal{F}_{t}$. This is illustrated in Figure 1.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

We now use the operator family $\left\{ \mathcal{K}_{t} \right\}$ to propagate the initial output map $\overline{G}$ and generate a "trajectory" of output maps The original output can now be obtained by simply observing where we used in the second equality, and defined the sampling operator ${\mathcal{S}_{\overline{x}}(G)}:={G\left(\overline{x} \right)}$ which "samples" the map $G_{t}$ at the point $\overline{x}$ in the state space. With this construction, we have two different evolutions and output maps that produce the same output $y$ It is in this sense that the Koopman representation is a "representation" of the original dynamical system. Given any trajectory of the original system, we can produce the same exact trajectory as an output of the Koopman system provided we start it with initial condition $\overline{G}$ and use the output map $\mathcal{S}_{\overline{x}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

Note the duality of the roles of initial conditions and output maps, which are "flipped" between the two representations. The output map $\overline{G}$ of the original system becomes the initial condition of the Koopman evolution (which is the reason we denoted it with an overbar earlier), while the output map $\mathcal{S}_{\overline{x}}$ of the Koopman representation is parametrized by the initial conditions of the original system. It is important to note that even if the state is directly observed in the original dynamical system (i.e. the map $\overline{G}$ is the identity), as the Koopman state $\left\{ G_{t} \right\}$ evolves forward in time, $G_{t}$ will typically not be the identity for $t > 0$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

If $\mathbf{Y}$ is a vector space, then $\mathcal{M}(\mathbf{X},\mathbf{Y})$ is endowed with a vector space structure, and it follows simply from the definition that the family $\left\{ \mathcal{K}_{t} \right\}$ is a semigroup of linear operators. Indeed For each $t$, $\mathcal{K}_{t}$ is a linear operator where $\overset{1}{=}$ and $\overset{3}{=}$ follow from the definition, and $\overset{2}{=}$ follows from the definition of the sum of two functions that take values in a vector space. which follows from the semigroup property of the flow map.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

Therefore, the family $\left\{ \mathcal{K}_{t} \right\}$ is a semigroup of linear operators on the space $\mathcal{M}{(\mathbf{X},\mathbf{Y})}$ of all output maps $G:{\mathbf{X}\rightarrow\mathbf{Y}}$. It is also clear that the sampling operator $\mathcal{S}_{\overline{x}}:{{\mathcal{M}(\mathbf{X},\mathbf{Y})}\rightarrow\mathbf{Y}}$ is linear if $\mathbf{Y}$ is a vector space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

$x_{t} = {\mathcal{F}_{t}\left(\overline{x} \right)}$ $G_{t} = {\mathcal{K}_{t}\left(\overline{G} \right)}$ $y_{t} = {\overline{G}\left(x_{t} \right)}$ $y_{t} = \mathcal{S}_{\overline{x}}\left(G_{t} \right) =:G_{t}\left(\overline{x} \right)$ Table 1: The relations between the original dynamical system’s equations and those of its Koopman representation, whose state space is the set ℳ (X, Y) of maps between the original system’s state X and output Y spaces. For the original system, the flow map ℱt evolves an initial condition $\overline{x}$ to the state xt at time t.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

The output yt is obtained from the state by the output map (observable) $\overline{G}$, which may be the identity map if the state is itself the output. The Koopman representation evolves the map $\overline{G}$ forward with the linear Koopman flow 𝒦t. The Koopman “state” is then a time-varying output map Gt. The original output is obtained from the Koopman state by “sampling” it $y_{t} = G_{t}{(\overline{x})} =:\mathcal{S}_{\overline{x}}{(G_{t})}$ at the initial condition $\overline{x}$ of the original system. Thus the roles of the initial states and output maps are reversed between the two representations. Both the Koopman evolution 𝒦t and the Koopman output operator $\mathcal{S}_{\overline{x}}$ are linear.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Basic Construction", "weight": 1.0} -->

Table 1 shows a side-by-side comparison of the relations between the original dynamical system and its Koopman representation. The state space of the Koopman representation is the set $\mathcal{M}(\mathbf{X},\mathbf{Y})$ of all output maps. The original output map $\overline{G}$ becomes the initial condition of an evolution governed by the linear semigroup $\left\{ \mathcal{K}_{t} \right\}$. This evolution produces a trajectory of output maps $\left\{ G_{t} \right\}$. At each time $t$, the output signal $y_{t}$ is given by evaluating the current Koopman state $G_{t}$ at $\overline{x}$. Thus the Koopman representation has a linear state evolution as well as a linear output map, and is therefore a linear dynamical system.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

As already seen, much can be deduced about the Koopman representation from general principles without actually writing down the differential or difference equations of the representation. None the less, it is instructive and simple to derive those equations. The discrete-time case is easiest and we do that first.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

For a discrete time system the evolution $\mathcal{F}$ is simply the iterates of the map $f$, and therefore $\mathcal{F}_{1} = f$. The generator of the corresponding Koopman representations is just $K = \mathcal{K}_{1}$. We therefore can write | | $y_{t}$ | ${= {\mathcal{S}_{\overline{x}}G_{t}}},$ | $\left({\mathcal{S}_{\overline{x}}G} \right)$ | ${:={G\left(\overline{x} \right)}}.$ | | | Thus the Koopman generator is just the pullback of a function $G$ by the one-step iteration map $f$. This is a time-invariant, discrete-time linear system.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

In continuous time, one can derive a Partial Differential Equation (PDE) that the evolving output map $\left\{ G_{t} \right\}$ satisfies. Since $\left\{ \mathcal{K}_{t} \right\}$ is a semigroup of linear operators, its generator $K$ can be calculated from the derivative at $t = 0$ which is defined in terms of the following (strong) limit The action of $K$ on any function $G\left(. \right)$ is then calculated as The equality $\overset{1}{=}$ follows from the chain rule, while $\overset{2}{=}$ follows from the original differential equation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

The operator $K$ is the generator of a PDE for a time-varying output map ${g(x,t)}:={G_{t}(x)}$ which we now write as a function of $x$ and $t$ Note that $\frac{\partial g}{\partial x}(x,t)$ is the Jacobian matrix^11^1The Jacobian of $g$ has the entry $\frac{\partial g_{i}}{\partial x_{j}}$ in the $i$'th row and $j$'th column. of $g$ with respect to $x$, and this equation is vector-valued in general.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

Equation can be written in compact matrix-vector notation if $g$ and $f$ are viewed as a row, rather than a column vector-valued functions as follows Thus if we regard $f$ and $g$ as row vectors^22^2This is consistent with writing a PDE in terms of differential forms., the Koopman generator can be very compactly written as $K = {f\frac{\partial}{\partial x}}$ as above. When $y$ is scalar, and thus $g$ is scalar-valued, there is no difference between a row and column vector representation, and $K$ can be written in the more common (but clumsy) notation $f \cdot \nabla$ Finally we note that since $K$ is the infinitesimal generator of the semigroup $\mathcal{K}_{t}$, we write this formally as $\mathcal{K}_{t} = e^{tK}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

The system is a linear PDE of the hyperbolic type. In fact, if $f$ is a divergence free vector field, then this equation is precisely the advection equation with a spatially varying velocity field of $- {f(x)}$. The trajectories of the original dynamical system are the characteristic curves of this PDE in that case.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Differential and Difference Equations", "weight": 1.0} -->

The Koopman representation (e.g. ) is a linear time-invariant system, so its dynamical properties are completely determined by the linear operator $K$. A modal (spectral) analysis of $K$ reveals all the modes of motion of the system. The spectrum of $K$ is typically infinite and can have both discrete and continuous parts. Many properties of the original dynamical system (too numerous to mention here) can be obtained from the eigenfunctions of $K$. Those include limit cycles and isostables.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Elephant in the Room: The Curse of Dimensionality", "weight": 1.0} -->

Just like the Hamilton-Jacobi-Bellman equation of Dynamic Programming, the Carleman linearization, the forward Kolmogorov, and the Fokker-Planck equations, the Koopman representation suffers from the curse of dimensionality. If the state space of the original system is ${\mathbb{R}}^{n}$, then the state space of the Koopman representation is identified with fields over $n$-dimensional space. If for example, a numerical grid of size $N$ is used to discretize each state in the original system, then the Koopman representation involves a discretization over a grid of size $N^{n}$. This exponential growth in complexity makes even simulating a general Koopman representation impractical^33^3This is of course in the absence any special structure or symmetries that can be exploited. for $n$ larger than 5 or 6. The situation is similar to simulating a PDE over $n$ spatial dimensions. Simulating such a system in $3$-dimensional space is feasible, but still computationally taxing for most modern computers.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Elephant in the Room: The Curse of Dimensionality", "weight": 1.0} -->

Similar simulations over say $6$-dimensional space are only perhaps possible with the most powerful computing machines available today.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Elephant in the Room: The Curse of Dimensionality", "weight": 1.0} -->

Explicit analysis of the Koopman representation is therefore typically only done for systems of dimensions 2 or 3, where the modal decomposition of the Koopman representation can offer considerable insight into the dynamical system's behavior. For higher dimensional systems, one way to sidestep the curse of dimensionality is to use "data-driven" techniques. These however suffer from another significant problem which is described next.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

The side-by-side comparison in Table 1 clarifies an important aspect of data-driven techniques that invoke the Koopman representation. In such techniques, state or output trajectories of the original system are generated through numerical simulations or experimental observations. A corollary of the existence of the Koopman representation implies that the same trajectories can be generated by a (infinite-dimensional) linear system. Thus linear system identification techniques can be used to model this data. However, note that even if the original state is fully observed (i.e. the initial output map $\overline{G}$ is the identity, that is $y_{t} = x_{t}$), the Koopman state $\left\{ G_{t} \right\}$ is never directly measured by the output since the operator $\mathcal{S}_{\overline{x}}$ is not the identity. A set of numerically or experimentally generated trajectories correspond to a particular initial condition $\overline{x}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

In the Koopman representation, $\overline{x}$ appears as parametrizing the output operator $\mathcal{S}_{\overline{x}}$. To consider these trajectories as being generated by the Koopman representation is to make a particular choice of the output operator $\mathcal{S}_{\overline{x}}$ corresponding to the initial condition $\overline{x}$ that generated those trajectories.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

The role of the output equation in is not fully appreciated in the literature. For each different initial condition $\overline{x}$ of the original dynamical system, there is a different output operator $\mathcal{S}_{\overline{x}}$. In this context, there is in fact not just one Koopman representation, but an infinite number of such representations parameterized by the initial condition $\overline{x}$. All the representations share the same generator $K$, but they have different output operators. If one is trying to analyze $K$ directly from its analytical description, this distinction is irrelevant, but if one is using simulation data to identify the Koopman representation, then these distinctions become important to understand.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

Depending on the initial condition $\overline{x}$, the full dynamics of the Koopman representation may or may not be observable (in the standard sense of linear systems observability) with the output operator $\mathcal{S}_{\overline{x}}$. To make this point concrete, consider the discrete-time Koopman representation. The unobservable subspace $\mathbf{X}_{\overline{o}}$ of this system is the null space of the operator which will typically be non-trivial, and will depend on the choice of $\overline{x}$. Let $\mathbf{X} = {\mathbf{X}_{o} \oplus \mathbf{X}_{\overline{o}}}$ be a decomposition of the state space into the direct sum of the unobservable subspace, and some complement $\mathbf{X}_{o}$ of it.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

With respect to this decomposition, the system equations are then transformed into the Kalman observable decomposition where $C_{o}$ is the restriction of the operator $\mathcal{S}_{\overline{x}}$ to the subspace $\mathbf{X}_{o}$. With this decomposition, the states $G_{o}$ and $G_{\overline{o}}$ are termed the observable and unobservable states respectively. This decomposition has the property that the pair $\left(C_{o},K_{o} \right)$ are observable. This means the states $G_{o}$ can be fully reconstructed from time series of the output $y$ (thus the term observable states). However, the unobservable states have no effect on the output at any time. This can be intuitively seen from the above equations. The states $G_{o}$ are coupled into the states $G_{\overline{o}}$, but not vice versa, and only the states $G_{o}$ are observable from the output.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

If the upper-right coupling term in the above decomposition of $K$ were not zero, then it might be possible to reconstruct the states $G_{\overline{o}}$ from $G_{o}$ (which in turn are observable from the output). The structure of the above decomposition however precludes that possibility. In terms of system identification, this means that only the operators $(C_{o},K_{o})$ are identifiable from output data, while the operators $K_{\overline{o}o}$ and $K_{\overline{o}}$ are not.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

The above implies that there is a part of the dynamics of the Koopman representation that cannot be identified from output data. However, the choice of the output $y_{t} = {\mathcal{S}_{\overline{x}}G_{t}}$ does depend on the initial condition $\overline{x}$ of the original system. This is intuitively clear if we think about identifying the Koopman representation from simulation data. For some systems, a choice of $\overline{x}$ for the simulation may not lead to exploration of the full state space and the corresponding system dynamics. For such situations, one may infer that the Koopman system $\left( \mathcal{S}_{\overline{x}},K \right)$ is not fully observable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

The preceding ideas are important to understand issues and limitations in data-driven approaches such as the Dynamic Mode Decomposition (DMD) and its variants. When such data analysis techniques are used on trajectories of non-linear dynamical systems, a justification is given that the Koopman representation guarantees that these trajectories can also be generated by a linear system with possibly larger (or infinite) dimensional state space. The algorithms then proceed to do what is essentially linear system identification^44^4This is meant to provide a larger context in which to view these methods. It is not meant to imply that DMD-type algorithms have already appeared in the system identification literature. On the contrary, the latter literature has historically been concerned with low-dimensional systems with a relatively small number of inputs and outputs. DMD on the other hand is tailored for high dimensional systems and trajectories generated from Computational Fluid Dynamics (CFD) models. with trajectories that were generated by a nonlinear system.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

A common issue in system identification is that the trajectories used may not be "rich enough"^55^5This corresponds to the persistency of excitation condition in system identification. to fully characterize the entire dynamical behavior of the original system, and this corresponds exactly to the Koopman representation not being fully observable. A choice of a different initial condition can be made, and the resulting trajectories appended for use in system identification. Another portion of the state space of the original system can then be explored, and this corresponds to adding another output to the Koopman representation to make it more observable than with only a single simulation.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Koopman Representation from Data: System Identification", "weight": 1.0} -->

For example, suppose $N$ simulations were performed from the initial conditions ${\overline{x}}_{1},\ldots,{\overline{x}}_{N}$. If the output time series $\left\{ {y_{i}(t)} \right\}$ from each simulation are stacked together synchronously in time (assuming they are all of the same length), the corresponding output equation would be The unobservable subspace of this "bigger" output operator $\mathcal{S}_{{\overline{x}}_{1},\ldots,{\overline{x}}_{N}}$ can only be smaller than the unobservable subspaces of the individual operators $\mathcal{S}_{{\overline{x}}_{i}}$. In fact, it will be in their intersection. This implies that more of the operator $K$ is identifiable than with any one simulation. For the original nonlinear system, this means that the choice of multiple initial conditions leads to exploration of more of the state space than with any one of them.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

It is instructive to understand the representation in the case of linear time-invariant systems. Consider the discrete-time case for convenience. Applying Several observations can be made Finite Dimensionality: The original output map is linear (multiplication by the matrix $\overline{C}$), and therefore all subsequent output maps are linear. This implies that they can be finitely parametrized by the entries of the matrices $C_{t}$, i.e. the Koopman representation is finite dimensional in this case! In other words, even though the Koopman representation as defined is infinite dimensional, the initial state, and therefore all subsequent states are linear maps, and the system never evolves outside the (finite-dimensional) subspace of linear maps from ${\mathbb{R}}^{n}$ to the output space^66^6The following question then immediately poses itself: For what other classes of dynamics is the Koopman representation finite dimensional?.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

Duality: The state iteration in the Koopman representation is given by right multiplication by the matrix $A$. We can therefore conclude that the modes (eigenvectors) of the Koopman representation are parametrized by the eigenvectors of $A^{\ast}$. The non-zero Koopman eigenvalues are simply those of $A$ (when $A$ is real, otherwise their complex conjugates).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

Grammians: The observability Grammian of the original system is For stable systems, it gives a quadratic form that measures the effect of any initial condition $\overline{x}$ on the $\ell^{2}$ norm of the corresponding output $y$ by It is interpreted as a measure of how "observable" the initial condition $\overline{x}$ is from the output $y$. For example, the eigenvector of $W$ corresponding to the largest eigenvalue is the most observable direction in state space.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

Applying the same idea to the Koopman representation, we can naturally define^77^7The definition given here is when the original dynamics are linear. In the nonlinear case, the definition would be $W_{K}:={\sum_{t = 0}^{\infty}{K^{t}\mathcal{S}_{\overline{x}}\mathcal{S}_{\overline{x}}^{\ast}K^{\ast t}}}$, where $\mathcal{S}_{\overline{x}}$ is point-evaluation operator. a "Koopman Grammian" The $\ell^{2}$ norm of an output can now be written as Note that this equation is simply a reshuffle of, but it can be given an alternate (or dual) interpretation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

If we regard output maps as the object to search over, then ${trace}\left({\overline{C}W_{K}{\overline{C}}^{\ast}} \right)$ measure how observable an output map $\overline{C}$ makes the initial condition $\overline{x}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

Another setting for the Koopman Grammian is a stochastic one. If $R:={\mathcal{E}\left\{ {\overline{x}{\overline{x}}^{\ast}} \right\}}$ is a given covariance of the distribution of initial states, then the eigenvectors of $W_{K}:={\sum_{t = 0}^{\infty}{A^{t}RA^{\ast t}}}$ sorted in descending order of the eigenvalues, give the best choices of output maps. In other words, to choose the best $q$ outputs, the optimal output map matrix $\overline{C}$ is the one with rows made from the first $q$ eigenvectors of $W_{K}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Linear Dynamics", "weight": 1.0} -->

Non-normality: If $A$ is non-normal or $\overline{C}$ non-unitary, then there need not be a relation between the eigenvectors of $W$ and those of $A$. This statement applies equally to $W_{K}$ and $K$. In the nonlinear case, a similar statement can be made when $K$ is non-normal, this happens when the underlying dynamical maps are not measure preserving.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

The transport (aka transfer) operator represents the transport of a mass distribution in state space by the dynamics of the system. It also represents the propagation in time of an initial probability density function by the unforced dynamics, i.e. it is the forward Kolmogorov (equivalently, Fokker-Planck) equation with no diffusion term. It is also referred to as the Perron-Frobenius operator in the general case, or the Liouville operator when the dynamics are Hamiltonian. The transfer operator gives another linear representation of the dynamics of a nonlinear system. We will call this the transport representation, and show that it and the Koopman representations are are adjoints of each other.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

We first present a self contained derivation of the transport representation. Let $T:{\Omega\longrightarrow\Omega}$ be an invertible map defined on a subset $\Omega$ of a measure space (e.g. ${\mathbb{R}}^{n}$). One can think of this map as describing the transport of some material with non-uniform density in $\Omega$. An expression for the final density in terms of the original density and the transport map $T$ can be easily derived. This situation is illustrated in Figure 2.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

Let $y$ and $x$ be a coordinate system in the domain and range respectively, and let $\phi_{1}$ and $\phi_{2}$ be the density functions before and after the transformation $T$ respectively. If we consider an arbitrary volume element $A$ in the range, the total mass of material in that volume element is given by where equality follows from the fact that the material in $A$ is transported from the volume element $T^{- 1}(A)$. Now using the transformation $x = {T(y)}$ and changing variables in the second integral yields where $\left| {\frac{\partial T^{- 1}}{\partial x}(x)} \right|$ is the determinant of the Jacobian of the map $T^{- 1}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

Since this equality holds for any volume element, we have derived the relation between $\phi_{1}$ and $\phi_{2}$ as This motivates our formal definition of the transport semi-group $\mathcal{T}_{t}$ which acts on functions $\phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ that are transported by the flow $\mathcal{F}$ of the dynamical system We note that although this definition is motivated in terms of material transport, an identical interpretation can be carried out in terms of probability density functions. This formula is also valid for vector-valued densities $\phi$, where each vector component of $\phi$ can be interpreted as the density of a distinct component of a material.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

Comparing, we see that $\mathcal{T}_{t}$ can be thought of as a push forward of the function $\phi$ by the map $\mathcal{F}_{t}$ with a "weighting" by the determinant of the Jacobian. Therefore it is not surprising that there is a formal mathematical connection between the transport and Koopman evolution semi-groups: they are adjoints with respect to the $L^{2}$ inner product. To verify this, start from the definitions assume for simplicity that $\Omega = \mathbf{X} = {\mathbb{R}}^{n}$, and calculate for any two functions ${\phi,\psi} \in {L^{2}\left({\mathbb{R}}^{n} \right)}$ where we have used the change of variables $y = {\mathcal{F}_{t}(x)}$ in the integration. This shows that indeed $\mathcal{T}_{t}^{\ast} = \mathcal{K}_{t}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

The infinitesimal generator $K = {f\frac{\partial}{\partial x}}$ of $\mathcal{K}_{t}$ has already been computed. To compute the infinitesimal generator of the transport operator, it is possible to repeat this exercise using the definition of $\mathcal{T}_{t}$. Alternatively, we can exploit the fact that the semi-groups $\mathcal{K}_{t}$ and $\mathcal{T}_{t}$ are adjoints, which means their infinitesimal generators $K$ and $T$ are also adjoints. This is true under fairly mild conditions on the semigroups, and symbolically is written as The computation of the generator adjoint $T = K^{\ast}$ is a fairly easy exercise in integration by parts^88^8Caution: The operator $T$ here is not the same as the transformation $T$, which was only used to motivate the definition of the transport semigroup..

<!-- chunk {"id": "body-0050", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

For simplicity, we do this for the scalar case (i.e. single output, and the space of observables is thus scalar valued functions on the state space). First expand the inner product $\left\langle \phi,{K\psi} \right\rangle$ by We thus discover that The last expression can be written in several different forms by observing that The operator $T$ is therefore sometimes written symbolically as Therefore $T$ is the sum of a differential operator $f \cdot \nabla$ and the operator of multiplication by the function $\nabla f$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

In the case when $f$ is a divergence free vector field (i.e. ${\nabla f} = 0$), this expression simplifies to $T = {- {f \cdot \nabla}}$. Comparing this, we see that in the case of divergence-free $f$ i.e. both operators $T$ and $K$ are skew Hermitian. This implies that the semi-groups $\mathcal{T}_{t} = e^{tT}$ and $\mathcal{K}_{t} = e^{tK}$ are unitary, that is, their evolutions preserve $L^{2}$ norms.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Relation to the Transport Representation", "weight": 1.0} -->

Finally, we note that the partial differential equation for a density function propagated by the transport operator is
