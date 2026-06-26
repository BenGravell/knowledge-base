<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conformal Symplectic and Relativistic Optimization

Topics include Optimization, Symplectic geometry, Momentum methods, Nesterov acceleration, Hamiltonian systems, Relativistic mechanics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes momentum-based optimization algorithms (Nesterov, heavy ball) through the lens of structure-preserving discretizations of dissipative Hamiltonian systems. Proposes a novel relativistic optimizer that normalizes momentum, unifying both Nesterov and heavy ball as special limiting cases, with improved stability and no additional computational overhead. Published at NeurIPS 2020.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Arguably, the two most popular accelerated or momentum-based optimization methods in machine learning are Nesterov's accelerated gradient and Polyaks's heavy ball, both corresponding to different discretizations of a particular second order differential equation with friction. Such connections with continuous-time dynamical systems have been instrumental in demystifying acceleration phenomena in optimization. Here we study structure-preserving discretizations for a certain class of dissipative (conformal) Hamiltonian systems, allowing us to analyze the symplectic structure of both Nesterov and heavy ball, besides providing several new insights into these methods. Moreover, we propose a new algorithm based on a dissipative relativistic system that normalizes the momentum and may result in more stable/faster optimization. Importantly, such a method generalizes both Nesterov and heavy ball, each being recovered as distinct limiting cases, and has potential advantages at no additional cost.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient based optimization methods are ubiquitous in machine learning since they only require first order information on the objective function. This makes them computationally efficient. However, vanilla gradient descent can be slow. Alternatively, *accelerated gradient methods*, whose construction can be traced back to Polyak and Nesterov, became popular due to their ability to achieve best worst-case complexity bounds. The heavy ball method, also known as *classical momentum* (CM) method, is given by where $k = {0,1,\ldots}$ is the iteration number, $\mu \in {}$ is the momentum factor, $\epsilon > 0$ is the learning rate, and $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is the function being minimized. Similarly, *Nesterov's accelerated gradient* (NAG) can be found in the form Both methods have a long history in optimization and machine learning. They are also the basis for the construction of other methods, such as adaptive ones that additionally include some gradient normalization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In discrete-time optimization the "acceleration phenomena" are considered counterintuitive. By this we mean a mechanism by which an algorithm can be accelerated, i.e. have a faster convergence; for instance, it is known that gradient descent converges at a rate of $O{({1/k})}$ for convex functions, while NAG converges at a rate $O{({1/k^{2}})}$, which is optimal in the sense of worst-case complexity. A complete understanding of why NAG is able to achieve such an improved rate is considered by many experts an important open problem, and currently there is no guiding principle to construct accelerated algorithms. A promising direction to understand this has been emerging in connection with continuous-time dynamical systems where many of these difficulties disappear or have an intuitive explanation. Since one is free to discretize a continuous-time system in many different ways, it is only natural to ask which discretization strategies would be most suitable for optimization? Such a question is unlikely to have a simple answer, and may be problem dependent.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, typical discretizations are also known to introduce spurious artifacts and do not reproduce the most important properties of the continuous-time system. Nevertheless, a special class of discretizations in the physics literature known as *symplectic integrators* are to be preferable whenever considering the special class of *conservative Hamiltonian systems*.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

More relevant to optimization is a class of *dissipative* systems known as *conformal Hamiltonian systems*. Recently, results from symplectic integrators were extended to this case and such methods are called *conformal symplectic integrators*. Conformal symplectic methods tend to have long time stability because the numerical trajectories remain in the same conformal symplectic manifold as the original system. Importantly, these methods do not change the phase portrait of the system, i.e. the stability of critical points is preserved. Although symplectic techniques have had great success in several areas of physics and Monte Carlo methods, only recently they started to be considered in optimization and are still mostly unexplored in this context. Very recently a great progress has been made by showing that such an approach is able to preserve the continuous-time rates of convergence up to a controlled error.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we *relate conformal symplectic integrators to optimization* and provide important insights into CM (1.1) and NAG (1.2). We prove that CM is a first order accurate conformal symplectic integrator. On the other hand, we show that NAG is also first order accurate, but not conformal symplectic since it introduces some spurious dissipation---or excitation. However, it does so in an interesting way that depends on the Hessian $\nabla^{2}f$; the symplectic form contracts in a Hessian dependent manner and so do phase space volumes. This is an effect of higher order but can influence the behaviour of the algorithm. We also derive *modified equations* and *shadow Hamiltonians* for both CM and NAG. Moreover, we indicate a tradeoff between stability, symplecticness, and such an spurious contraction, indicating advantages in structure-preserving discretizations for optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization can be challenging in a landscape with large gradients, e.g. for a function with fast growing tails. The only way to control divergences in methods such as (1.1) and (1.2) is to make the step size very small, but then the algorithm becomes slow. One approach to this issue is to introduce a suitable normalization of the gradient. Here we propose an alternative approach motivated by *special relativity* in physics. The reason is that in special relativity there is a limiting speed, i.e. the speed of light. Thus, by discretizing a *dissipative relativistic system*, we obtain an algorithm that incorporates this effect and may result in more stable optimization in settings with large gradients.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we introduce Algorithm 1. Besides the momentum factor $\mu$ and the learning rate $\epsilon$---also present in (1.1) and (1.2)---the above *relativistic gradient descent* (RGD) method has the additional parameters $\delta \geq 0$ and $0 \leq \alpha \leq 1$ which brings some interesting properties: Initial state (x0, v0) and parameters ϵ > 0, δ > 0, μ ∈, α ∈ $x_{k + {1/2}}\leftarrow{x_{k} + {\sqrt{\mu}\left({{\mu\delta{\| v_{k}\|}^{2}} + 1} \right)^{- {1/2}}v_{k}}}$ $v_{k + {1/2}}\leftarrow{{\sqrt{\mu}v_{k}} - {\epsilon{\nabla f}{(x_{k + {1/2}})}}}$ Algorithm 1

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

RGD method for minimizing a smooth function f (x). In practice, we recommend setting α = 1 which results in a conformal symplectic method.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

When $\delta = 0$ and $\alpha = 0$, RGD recovers NAG (1.2). When $\delta = 0$ and $\alpha = 1$, RGD becomes a second order accurate version of CM (1.1), which has a close behavior but an improved stability. Thus, RGD can interpolate between these two methods. Moreover, RGD has the same computational cost as CM or NAG. These facts imply that RGD is at least as efficient as CM and NAG if appropriately tuned.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $y_{k} \equiv {{\alphax_{k + {1/2}}} + {{({1 - \alpha})}x_{k}}}$. The last update in Algorithm 1 implies ${\|{x_{k + 1} - y_{k}}\|} \leq {1/\delta}$. Thus, with $\delta > 0$, RGD is globally bounded regardless how large $\|{\nabla f}\|$ might be; this is in contrast with CM and NAG where $\delta = 0$, i.e. ${\|{x_{k + 1} - y_{k}}\|} \leq \infty$. The square root factor in Algorithm 1 has a "relativistic origin" and its strength is controlled by $\delta$. For this reason, RGD may be more stable than CM and NAG, preventing divergences in settings of large gradients; see Fig. 1 in Section 6 and the plots in Appendix B.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

As we will show, $\alpha = 1$ implies that RGD is *conformal symplectic*, whereas $\alpha = 0$ implies a spurious Hessian driven damping similarly found in NAG. Thus, RGD has the flexibility of being "dissipative-preserving" or introducing some "spurious contraction." However, based on theoretical arguments and empirical evidence, we advocate for the choice $\alpha = 1$.^11^1The only reason for introducing the extra parameter $0 \leq \alpha \leq 1$ into Algorithm 1 is to actually let the experiments decide whether $\alpha = 1$ (symplectic) or $\alpha < 1$ (non-symplectic) is desirable or not.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let us mention a few related works. Applications of symplectic integrators in optimization was first considered in ---although this is different than the conformal symplectic case explored here. Recently, the benefits of symplectic methods in optimization started to be indicated. Actually, even more recently, a generalization of symplectic integrators to a general class of dissipative Hamiltonian systems was proposed, with theoretical results ensuring that such discretizations are "rate-matching" up to a negligible error; this construction is general and contains the conformal case considered here as a particular case. Relativistic systems are obviously an elementary topic in physics but---with some modifications---the relativistic kinetic energy was considered in Monte Carlo methods and also briefly. Finally, we stress that Algorithm 1 is a completely new method in the literature, generalizing perhaps the two most popular existing accelerated methods, namely CM and NAG, and also has the ability to be conformal symplectic besides being adaptive in the momentum which may help controlling divergences. We also provide several new insights into CM and NAG in Section 4.3 and Section 6 which may be of independent interest.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

We start by introducing the basics of conformal Hamiltonian systems and focus on their intrinsic symplectic geometry; we refer to for details. The state of the system is described by a point on phase space, ${(x,p)} \in {\mathbb{R}}^{2n}$, where $x = {x{(t)}}$ is the generalized coordinates and $p = {p{(t)}}$ its conjugate momentum, with $t \in {\mathbb{R}}$ being the time. The system is completely specified by a Hamiltonian function $H:{{\mathbb{R}}^{2n}\rightarrow{\mathbb{R}}}$ and required to obey a modified form of Hamilton's equations: Here $\overset{˙}{x} \equiv \frac{dx}{dt}$, $\overset{˙}{p} \equiv \frac{dp}{dt}$, and $\gamma > 0$ is a damping constant.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

A classical example is given by where $m > 0$ is the mass of a particle subject to a potential $f$. The Hamiltonian is the energy of the system and upon taking its time derivative one finds $\overset{˙}{H} = {- {\gamma{\| p\|}^{2}}} \leq 0$. Thus $H$ is a Lyapunov function and all orbits tend to critical points, which in this case must satisfy ${{\nabla f}{(x)}} = 0$ and $p = 0$. This implies that the system is stable on isolated minimizers of $f$.^22^2This can be generalized for any Hamiltonian $H$ that is strongly convex on $p$ with the minimum at $p = 0$. where $I$ is the $n \times n$ identity matrix, to write the equations of motion (2.1) concisely as^33^3$C{(z)}$ and $D{(z)}$ will be used later on and stand for "conservative" and "dissipative" parts, respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

Note that ${\Omega\Omega^{T}} = {\Omega^{T}\Omega} = I$ and $\Omega^{2} = {- I}$, so that $\Omega$ is real, orthogonal and antisymmetric. Let ${\xi,\eta} \in {\mathbb{R}}^{2n}$ and define the *symplectic 2-form* ${\omega{(\xi,\eta)}} \equiv {\xi^{T}\Omega\eta}$. It is convenient to use the wedge product representation of this 2-form, namely^44^4It is not strictly necessary to be familiar with differential forms and exterior calculus to understand this paper.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

For the current purposes, it is enough to recall that the wedge product is a bilinear and antisymmetric operation, i.e. ${{dx} \land {({{ady} + {bdz}})}} = {{{{adx} \land {dy}} + {bdx}} \land {dz}}$ and ${{dx} \land {dy}} = {{- {dy}} \land {dx}}$ for scalars $a$ and $b$ and 1-forms $dx$, $dy$, $dz$ (think about this as vector differentials); we refer to and for more details if necessary.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

We denote $\omega_{t} \equiv {{dx{(t)}} \land {dp{(t)}}}$. The equations of motion define a flow $\Phi_{t}:{{\mathbb{R}}^{2n}\rightarrow{\mathbb{R}}^{2n}}$, i.e. ${\Phi_{t}\left(z_{0}) \right.} \equiv {z{(t)}}$ where ${z{}} \equiv z_{0}$. Let $J_{t}{(z)}$ denote the Jacobian of $\Phi_{t}{(z)}$. From (2.4) it is not hard to show that (see e.g.) Therefore, a conformal Hamiltonian flow $\Phi_{t}$ *contracts the symplectic form exponentially* with respect to the damping coefficient $\gamma$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

It follows from (2.6) that volumes on phase space shrink as ${{vol}{({\Phi_{t}{(\mathcal{R})}})}} = {\int_{\mathcal{R}}{{|{\det{J_{t}{(z)}}}|}{dz}}} = {e^{- {n\gammat}}{{vol}{(\mathcal{R})}}}$ where $\mathcal{R} \subset {\mathbb{R}}^{2n}$. This contraction is stronger as dimension increases. The conservative case is recovered with $\gamma = 0$ above; in this case, the symplectic structure is preserved and volumes remain invariant (Liouville's theorem). A known and interesting property of conformal Hamiltonian systems is that their Lyapunov exponents sum up in pairs to $\gamma$. This imposes constraints on the admissible dynamics and controls the phase portrait near critical points. For other properties of attractor sets we refer to.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Conformal Hamiltonian systems", "weight": 1.0} -->

Finally, conformal symplectic transformations can be composed and form the so-called conformal group.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conformal symplectic optimization", "weight": 1.0} -->

Consider (2.4) where we associate flows $\Phi_{t}^{C}$ and $\Phi_{t}^{D}$ to the respective vector fields $C{(z)}$ and $D{(z)}$. Conformal symplectic integrators can be constructed as *splitting methods* that approximate the true flow $\Phi_{t}$ by composing the individual flows $\Phi_{t}^{C}$ and $\Phi_{t}^{D}$. Our procedure to obtain a numerical map $\Psi_{h}$, with step size $h > 0$, is to first obtain a numerical approximation to the conservative part of the system, $\overset{˙}{z} = {\Omega{\nabla H}{(z)}}$. This yields a numerical map $\Psi_{h}^{C}$ that approximates $\Phi_{h}^{C}$ for small intervals of time $\lbrack t,{t + h}\rbrack$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conformal symplectic optimization", "weight": 1.0} -->

One can choose any standard *symplectic integrator* for this task. Let us pick the simplest, i.e. the symplectic Euler method \[30, pp. 189\]. We thus have $\Psi_{h}^{C}:{{(x,p)}\mapsto{(X,P)}}$ where Now the dissipative part of the system, $\overset{˙}{z} = {- {\gammaDz}}$, can be integrated exactly. Indeed, $\overset{˙}{x} = 0$ and $\overset{˙}{p} = {- {\gammap}}$, thus $\Psi_{h}^{D}:{{(x,p)} = {(x,{e^{- {\gammah}}p})}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conformal symplectic optimization", "weight": 1.0} -->

With $\Psi_{h} \equiv {\Psi_{h}^{C} \circ \Psi_{h}^{D}}$ we obtain $\Psi_{h}:{{(x,p)}\mapsto{(X,P)}}$ as This is nothing but a *dissipative version* of the symplectic Euler method. Similarly, if we choose the leapfrog method \[30, pp. 190\] for $\Psi_{h}^{C}$ and consider $\Psi_{h} \equiv {\Psi_{h/2}^{D} \circ \Psi_{h}^{C} \circ \Psi_{h/2}^{D}}$ we obtain This is a *dissipative* version of the leapfrog, which is recovered when $\gamma = 0$. Note that in general (3.2) is implicit in $P$, and (3.3) is implicit in $\overset{\sim}{X}$ and $P$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conformal symplectic optimization", "weight": 1.0} -->

However, both will become explicit for separable Hamiltonians, $H = {{T{(p)}} + {f{(x)}}}$, and in this case they are extremely efficient. Note also that (3.2) and (3.3) are completely general, i.e. by choosing a suitable Hamiltonian $H$ one can obtain several possible optimization algorithms from these integrators. Next, we show important properties of these integrators. (Below we denote $t_{k} = {kh}$ for $k = {0,1,\ldots}$, $z_{k} \equiv {z{(t_{k})}}$, etc.)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Symplectic structure of heavy ball and Nesterov", "weight": 1.0} -->

Consider the classical Hamiltonian (2.2) and replace into (3.2) to obtain where we now make the iteration number $k = {0,1,\ldots}$ explicit for convenience of the reader in relating to optimization methods. Introducing a change of variables, we see that (4.1) is precisely the well-known CM method (1.1). Therefore, CM is nothing but a dissipative version of the symplectic Euler method. Thanks to Theorems 3.3 and 3.4

<!-- chunk {"id": "body-0028", "role": "body", "section": "Alternative form", "weight": 1.0} -->

It is perhaps more common to find Nesterov's method in the following form: where $\mu_{k + 1} = {k/{({k + 3})}}$. This is equivalent to (1.2), as can be seen by introducing the variable $v_{k} \equiv {x_{k} - x_{k - 1}}$ and writing the updates in terms of $x$ and $v$. When $\mu_{k}$ is constant, Theorem 4.2. ‣ 4 Symplectic structure of heavy ball and Nesterov") shows that the method is not conformal symplectic. When $\mu_{k} = {k/{({k + 3})}}$, the differential equation associated to (4.16) is equivalent to (2.1)/(2.2) with $\gamma = {3/t}$. It is possible to generalize the above results for time dependent cases. Therefore, also in this case, NAG does not preserve the symplectic structure; we note that (4.7.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Preserving stability and continuous-time rates", "weight": 1.0} -->

An important question is whether being "symplectic" is beneficial or not for optimization. Very recently, it has been shown that symplectic discretizations of dissipative systems may indeed preserve continuous-time rates of convergence when $f$ is smooth and the system is appropriately dampened (choice of $\gamma$); the continuous-time rates can be obtained via Lyapunov analysis. Thus, assuming that we have a suitable conformal Hamiltonian system, conformal symplectic integrators such as the general method (3.3), provide a principled approach to construct optimization algorithms that are guaranteed to respect the main properties of the system, such as stability of critical points and convergence rates. Furthermore, we claim that there is a delicate tradeoff where being conformal symplectic is related to an improved stability, in the sense that the method can operate with larger step sizes, while the spurious dissipation introduced by NAG (Theorem 4.2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Preserving stability and continuous-time rates", "weight": 1.0} -->

‣ 4 Symplectic structure of heavy ball and Nesterov")) may improve the convergence rate slightly, since it introduces more contraction, but at the cost of making the method less stable; we show these details in Section 6. Next, we also provide important additional insights into CM and NAG, such as their modified or perturbed equations and their *shadow Hamiltonians*, which describe these methods to a higher degree of resolution.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Shadow dynamical systems for Nesterov and heavy ball", "weight": 1.0} -->

We have shown above that both CM and NAG are a first order integrators to the conformal Hamiltonian system (4.8), however NAG changes slightly the behaviour of the original system since it introduces spurious damping or excitation. To understand its behaviour more closely, one can ask the following question: *for which continuous-time dynamical system NAG turns out to be a second order integrator?* In other words, we can look for a modified system that captures the behaviour of NAG more closely, up to $O{(h^{3})}$. Every numerical method is known to have a modified or perturbed differential equation (the brief discussion in may also be useful). In answering this question, we thus find the following.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

Let us briefly mention some simple but fundamental concepts to motivate our approach. The previous algorithms are based on (2.2) which leads to a classical Newtonian system where time is just a parameter, independent of the Euclidean space where the trajectories live. This implies that there is no restriction on the speed, ${\| v\|} = {\|{{{dx}/d}t}\|}$, that a particle can attain. This translates to a discrete-time algorithm, such as (4.1), where large gradients $\nabla f$ give rise to a large momenta $p$, implying that the position updates for $x$ can diverge. On the other hand, in special relativity, space and time form a unified geometric entity, the $({n + 1})$-dimensional Minkowski spacetime with coordinates $X = {({ct};x)}$, where $c$ denotes the speed of light.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

An infinitesimal distance on this manifold is given by ${ds^{2}} = {{- {({cdt})}^{2}} + {\|{dx}\|}^{2}}$. Null geodesics correspond to ${ds^{2}} = 0$, implying ${\| v\|}^{2} = {\|{{{dx}/d}t}\|}^{2} = c^{2}$, i.e. no particle can travel faster than $c$. This imposes constraints on the geometry where trajectories take place---it is actually a hyperbolic geometry. With that being said, the idea is that by discretizing a relativistic system we can incorporate these features into an optimization algorithm which may bring benefits such as an improved stability.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

A relativistic particle subject to a potential $f$ is described by the following Hamiltonian: In the classical limit, ${\| p\|} \ll {mc}$, one obtains $H = {{mc^{2}} + {{\| p\|}^{2}/{({2m})}} + {f{(x)}} + {O{({1/c^{2}})}}}$, recovering (2.2) up to the constant $E_{0} = {mc^{2}}$, which has no effect in deriving the equations of motion. Replacing (5.1) into (2.1) we thus obtain a *dissipative relativistic system*: Importantly, in (5.2) the momentum is normalized by the $\sqrt{\cdot}$ factor, so $\overset{˙}{x}$ remains bounded even if $p$ was to go unbounded.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

Now, replacing (5.1) into the first order accurate conformal symplectic integrator (3.2), we readily obtain When $c\rightarrow\infty$ the above updates recover CM (4.1). Thus, this method is a relativistic generalization of CM or heavy ball. Moreover, the method (5.3) is a first order conformal symplectic integrator by construction (see Theorems 3.3 and 3.4).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

One can replace the Hamiltonian (5.1) into (3.3) to obtain a second order version of (5.3). However, motivated by the close connection between NAG and (4.3)---recall the comments following (4.5) about NAG "rolling back" the last update---let us additionally introduce a convex combination, ${\alphax_{k + {1/2}}} + {{({1 - \alpha})}x_{k}}$ where $0 \leq \alpha \leq 1$, between the initial and midpoint of the method. In this manner, we can interpolate between a conformal symplectic regime and a spurious Hessian damping regime (recall Theorem 4.2. ‣ 4 Symplectic structure of heavy ball and Nesterov")). Therefore, we obtain the following integrator: We call this method *Relativistic Gradient Descent* (RGD). By introducing the updates (5.4) assume the equivalent form stated in Algorithm 1 in the introduction.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

RGD (5.4) (resp. Algorithm 1) has several interesting limits, recovering the behaviour of known algorithms as particular cases. For instance, when $c\rightarrow\infty$ (resp. $\delta\rightarrow 0$) it reduces to an interpolation between CM (4.1) (resp. (1.1)) and NAG (4.6) (resp. (1.2)). If we additionally set $\alpha = 0$ it becomes precisely NAG, whether when $\alpha = 1$ it becomes a second order version (in terms of accuracy) of CM.^77^7The dynamics of both CM and this second order version is pretty close, and if anything the latter is even more stable than the former (see Section 6). When $\alpha = 1$, and arbitrary $c$ (or $\delta$), RGD is a conformal symplectic integrator thanks to Theorems 3.3. Recall also that Theorem 3.4 implies that RGD is a second order accurate integrator.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

When $\alpha = 0$, and arbitrary $c$ (or $\delta$), RGD is no longer conformal symplectic and introduces a Hessian driven damping in the spirit of NAG. Finally, the parameter $c$ (or $\delta$) controls the strength of the normalization term in the position updates of (5.4) (or Algorithm 1), which can help preventing divergences when navigating through a rough landscape with large gradients, or fast growing tails. Indeed, note that ${\|{x_{k + 1} - {\alphax_{k + {1/2}}} - {{({1 - \alpha})}x_{k}}}\|} \leq {1/\delta}$ is always bounded for $\delta > 0$; this becomes unbounded when $\delta\rightarrow 0$, i.e. in the classical limit of CM and NAG.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dissipative relativistic optimization", "weight": 1.0} -->

In short, RGD is a novel algorithm with quite some flexibility and unique features, generalizing perhaps the two most important accelerated gradient based methods in the literature, which can be recovered as limiting cases. Next, we illustrate numerically through simple yet insightful examples that RGD can be more stable and faster than CM and NAG.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

Here we illustrate an interesting phenomenon: there is a tradeoff between stability versus convergence rate. Intuitively, an improved rate is associated to a higher "contraction," i.e. the introduction of spurious dissipation in the numerical method. However, this makes the method less stable, and ultimately very sensitive to parameter tuning. On the other hand, a geometric or structure-preserving integrator may have slightly less contraction, since it preserves the original dissipation of the continuous-time system exactly, but it is more stable and able to operate with larger step sizes. Furthermore, a structure-preserving method is guaranteed to reproduce very closely, perhaps even up to a negligible error, the continuous-time rates of convergence. This indicates that there may have benefits in considering this class of methods for optimization, such as conformal symplectic integrators that are being advocated in this paper.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

Stability of a numerical integrator means the region of hyperparameters, e.g. values of the step size, such that the method is able to converge. The larger this region, more stable is the method. The convergence rate is a measure of how fast the method tends to the minimum, and this is related to the amount of contraction between subsequent states, or subsequent values of the objective function. For instance, since NAG introduces some spurious dissipation---recall (4.7. ‣ 4 Symplectic structure of heavy ball and Nesterov")) and (4.20)---we expect that it may have a slightly higher contraction compared to CM, which exactly preserves the dissipation of the continuous-time system---recall (4.24). Thus, such a spurious dissipation can induce a slightly improved convergence rate, but as we will show below, at the cost of making the method more unstable and thus requiring smaller step sizes.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

Let us consider a standard linear stability analysis, which involves a quadratic function (4.14) such that the previous methods can be treated analytically. Thus, replacing (4.14) into CM in the form (4.1) it is possible to write the algorithm as a linear system: where we denote $z = \begin{bmatrix} \end{bmatrix}$. Similarly, NAG in the form (4.6) yields while RGD (5.4), with $c\rightarrow\infty$ and $\alpha = 1$, yields^88^8The case of finite $c$ is nonlinear and not amenable to such an analysis. However, the case $c\rightarrow\infty$ already provides useful insights.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

A linear system is stable if the spectral radius of its transition matrix is ${\rho{(T)}} \leq 1$. We can compute the eigenvalues of the above matrices and check for which range of parameters they remain inside the unit circle; e.g. for given $\gamma$, $m$, and $\lambda$ we can find the allowed range of the step size $h$ for which the maximum eigenvalue in absolute value is ${|\lambda_{\text{max}}|} \leq 1$. Instead of showing the explicit formulas for these eigenvalues, which can be obtained quite simply but are cumbersome, let us illustrate what happens graphically.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

In Fig. 1, the shaded gray area represents the unit circle. Any eigenvalue that leaves this area makes the associated algorithm unstable. Here we fix $m = \lambda = \gamma = 1$ (other choices are equivalent) and we vary the step size $h > 0$. These eigenvalues are in general complex and lie on a circle which is determined by the amount of friction in the system. Note how for CM and RGD this circle is centered at the origin, with radius $\sqrt{\mu} \equiv e^{- {{\gammah}/2}}$, since these methods are conformal symplectic and exactly preserve the dissipation of the underlying continuous-time system.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

However, NAG introduces a spurious damping which is reflected as the circle being translated from the center, at a distance $1/{({e^{\gammah} + 1})}$, and moreover this circle has a smaller radius of $1/{({e^{\gammah} + 1})}$ compared to CM and RGD; since this radius is smaller, NAG may have a faster convergence when these eigenvalues are complex. As we increase $h$ (left to right in Fig. 1), the eigenvalues move counterclockwise on the circles until falling on the real line, where one of them goes to the left while the other goes to the right. Eventually, the leftmost eigenvalue leaves the unit circle for a large enough $h$ (third panel in Fig. 1). Note that NAG becomes unstable first, followed by CM, and only then by RGD.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

The main point is that CM and RGD can still be stable for much larger step sizes compared to NAG, and RGD is even more stable than CM as seen in the rightmost plot in Fig. 1; this is a consequence of RGD being an integrator of order $r = 2$ whereas CM is of order $r = 1$. Hence, even though NAG may have a slightly faster convergence (due to a stronger contraction), it requires a smaller step sizes and its stability is more sensitive compared to a conformal symplectic method. On the other hand, both CM and RGD can operate with larger step sizes, which in practice may even result in a faster solver compared to NAG.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Tradeoff between stability and convergence rate", "weight": 1.0} -->

To provide a more quantitative statement, after computing the eigenvalues of the above transition matrices for given $\mu \equiv e^{- {\gammah}}$, $m$, and $\lambda$, we find the following threshold for stability: We can clearly see that RGD has the largest region for $h$, followed by CM, then by NAG, in agreement with the results of Fig. 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Let us compare RGD (Algorithm 1) against NAG (1.2) and CM (1.1) on some test problems. We stress that all hyperparameters of each of these methods were systematically optimized through Bayesian optimization (the default implementation uses a Tree of Parzen estimators). This yields *optimal* and *unbiased* parameters automatically. Moreover, by checking the distribution of these hyperparameters during the tuning process we can get intuition on the sensitivity of each method. Thus, for each algorithm, we show its convergence rate in Fig. 2 when the best hyperparameters were used. In addition, in Fig. 3 we show the distribution of hyperparameters during the Bayesian optimization step---the parameters are indicated and color lines follow Fig. 2. Such values are obtained only when the respective algorithm was able to converge. We note that usually CM and NAG diverged more often than RGD which seemed more robust to parameter choice. Below we describe some of the optimization problems where such algorithms were tested over. In Appendix B we provide several additional experiments illustrating the benefits of RGD. The actual code related to our implementation is extremely simple and can be found.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Correlated quadratic", "weight": 1.0} -->

Consider ${f{(x)}} = {{({1/2})}x^{T}Qx}$ where $Q_{ij} = \rho^{|{i - j}|}$, $\rho = 0.95$, and $Q$ has size $50 \times 50$---this function was also used. We initialize the position at random, $x_{0,i} \sim {\mathcal{N}{}}$, and the velocity as $v_{0} = 0$. The convergence results are shown in Fig. 2a. The distribution of parameters during tuning are in Fig. 3a, showing that $\alpha\rightarrow 1$ is preferable. This gives evidence for an advantage in being conformal symplectic. Note also that $\delta > 0$, thus "relativistic effects" played a role in improving convergence.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Random quadratic", "weight": 1.0} -->

Consider ${f{(q)}} = {{({1/2})}x^{T}Qx}$ where $Q$ is a $500 \times 500$ positive definite random matrix with eigenvalues uniformly distributed in $\lbrack 10^{- 3},10\rbrack$. Convergence rates are in Fig. 2b with the histograms of parameter search in Fig. 3b. Again, there is a preference towards $\alpha\rightarrow 1$, evidencing benefits in being conformal symplectic.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Rosenbrock", "weight": 1.0} -->

For a challenging problem in higher dimensions, consider the nonconvex Rosenbrock function ${f{(x)}} \equiv {\sum_{i = 1}^{n - 1}\left( {{100{({x_{i + 1} - x_{i}^{2}})}^{2}} + {({1 - x_{i}})}^{2}} \right)}$ with $n = 100$; this case was already studied in detail. Its landscape is quite involved, e.g. there are two minimizers, one global at $x^{\star} = {(1,\ldots,1)}^{T}$ with ${f{(x^{\star})}} = 0$ and one local near $x \approx {({- 1},1,\ldots,1)}^{T}$ with $f \approx 3.99$. There are also---exponentially---many saddle points, however only two of these are actually hard to escape.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Rosenbrock", "weight": 1.0} -->

These four stationary points account for $99.9\%$ of the solutions found by Newton's method. We note that both minimizers lie on a flat, deep, and narrow valley, making optimization challenging. In Fig. 2c we have the convergence of each method initialized at $x_{0,i} = {\pm 2}$ for $i$ odd/even. Fig. 3c shows histograms for parameter selection. Again, we see the favorable symplectic tendency, $\alpha\rightarrow 1$. Here relativistic effects, $\delta \neq 0$, played a predominant role in the improved convergence of RGD.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Matrix completion", "weight": 1.0} -->

Consider an $n \times n$ matrix $M$ of rank $r \ll n$ with observed entries in the support ${(i,j)} \in \Omega$, where ${P_{\Omega}{(M)}_{ij}} = M_{ij}$ if ${(i,j)} \in \Omega$ and ${P_{\Omega}{(M)}_{ij}} = 0$ projects onto this support. The goal is to recover $M$ from the knowledge of $P_{\Omega}{(M)}$. We assume that the rank $r$ is known. In this case, if the number of observed entries is $O{({rn})}$ it is possible to recover $M$ with high probability.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Matrix completion", "weight": 1.0} -->

We do this by solving the nonconvex problem $\min_{U,V}{\|{P_{\Omega}{({M - {UV^{T}}})}}\|}_{F}^{2}$, where ${U,V} \in {\mathbb{R}}^{n \times r}$, by *alternating minimization*: for each iteration we apply the previous algorithms first on $U$ with $V$ held fixed, followed by similar updates for $V$ with the new $U$ fixed. This is a know technique for gradient descent (GD), which we additionally include as a baseline. We generate $M = {RS^{T}}$ where ${R,S} \in {{{\mathbb{R}}n} \times r}$ have iid entries from the normal distribution $\mathcal{N}{}$. We initialize $U$ and $V$ sampled from the standard normal.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Matrix completion", "weight": 1.0} -->

The support is chosen uniformly at random with sampling ratio $s = 0.3$, yielding $p = {sn^{2}}$ observed entries. We set $n = 100$ and $r = 5$. This gives a number of effective degrees of freedom $d = {r{({{2n} - r})}}$ and the "hardness" of the problem can be quantified via ${d/p} \approx 0.325$. Fig. 2d shows the convergence rate, and Fig. 3d the parameter search.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion and outlook", "weight": 1.5} -->

This paper introduces a new perspective on a recent line of research connecting accelerated optimization methods to continuous-time dynamical systems that have been playing a major role in machine learning. We brought *conformal symplectic* techniques for *dissipative systems* into this context, besides proposing a new method called *Relativistic Gradient Descent* (RGD), based on a dissipative relativistic system; see Algorithm 1. RGD generalizes both the classical momentum (CM) or heavy ball method---given by (1.1)---as well as Nesterov's accelerated gradient (NAG)---given by (1.2); each of these methods are recovered as particular cases from RGD which has no additional computational cost compared to CM and NAG. Moreover, RGD has more flexibility, can interpolate between a conformal symplectic behaviour or introduce some Hessian dependent damping in the spirit of NAG, and has potential to control instabilities due to large gradients by normalizing the momentum.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion and outlook", "weight": 1.5} -->

In our experiments, RGD significantly outperformed CM and NAG, specially in settings with large gradients or functions with a fast growth; besides Section 7 we report several additional examples in Appendix B.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion and outlook", "weight": 1.5} -->

We also elucidated what is the symplectic structure behind CM and NAG. We found that the former turns out to be a conformal symplectic integrator (Corollary 4.1. ‣ 4 Symplectic structure of heavy ball and Nesterov")), thus being "dissipative-preserving," while the latter introduces a spurious contraction of the symplectic form by a Hessian driven damping (Theorem 4.2. ‣ 4 Symplectic structure of heavy ball and Nesterov")). This is an effect of second order in the step size but may affect convergence and stability. We pointed out a tradeoff between this extra contraction and the stability of a conformal symplectic method. We also derived modified or perturbed equations for CM and NAG, describing these methods to a higher degree of resolution; this analysis provides several new insights into these methods and may form the basis for exploring these algorithms using different techniques compared to standard approaches in pure optimization.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion and outlook", "weight": 1.5} -->

On a higher level, this paper shows how structure-preserving discretizations of classical dissipative systems can be useful for studying existing optimization algorithms, as well as introduce new methods inspired by real physical systems. A thorough justification for the use of structure-preserving---or "dissipative symplectic"---discretizations in this context was recently provided in under great generality.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion and outlook", "weight": 1.5} -->

Finally, a more refined analysis of RGD is certainly an interesting future problem, though considerably challenging due to the nonlinearity introduced by the $\sqrt{1 + {\delta{\| v\|}^{2}}}$ term in the updates of Algorithm 1. To give an example, even if one assumes a simple quadratic function ${f{(x)}} = {{({\lambda/2})}x^{2}}$, the differential equation (5.2) is nonlinear and does not admit a closed form solution, contrary to the differential equation associated to CM and NAG which is linear and can be readily integrated. Thus, even in continuous-time, the analysis for RGD is likely to be involved. Finally, it would be interesting to consider RGD in a stochastic setting, namely investigate its diffusive properties in a random media, which may bring benefits to nonconvex optimization and sampling.
