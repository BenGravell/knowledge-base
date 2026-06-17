# On the Stability of the Kuramoto Model of Coupled Nonlinear Oscillators

- arXiv ID: [math/0504419](https://arxiv.org/abs/math/0504419)
- HTML source: [ar5iv](https://ar5iv.labs.arxiv.org/html/math/0504419)

\\IEEEoverridecommandlockouts

# On the Stability of the Kuramoto Model of Coupled Nonlinear Oscillators^†^ 

Ali Jadbabaie^∗^    Nader Motee^∗^    and Mauricio Barahona^‡^ ^∗^ A. Jadbabaie and N. Motee are with the Department of Electrical and Systems Engineering and GRASP Laboratory, University of Pennsylvania, Philadelphia, PA 19104. email: {jadbabai, motee}@grasp.upenn.edu. A. Jadbabaie's research is supported in part by ARO/MURI DAAD19-02-1-0383, ONR/YIP-542371 and NSF-ECS-0347285.$\ddagger$ M. Barahona is with the Department of Bioengineering, Imperial College London, United Kingdom.email: m.barahona@imperial.ac.uk$\dagger$ An earlier version of this paper was presented at the 2004 American Control Conference, ACC 2004.

###### Abstract 

We provide an analysis of the classic Kuramoto model of coupled nonlinear oscillators that goes beyond the existing results for all-to-all networks of identical oscillators. Our work is applicable to oscillator networks of arbitrary interconnection topology with uncertain natural frequencies. Using tools from spectral graph theory and control theory, we prove that for couplings above a critical value, the synchronized state is locally asymptotically stable, resulting in convergence of all phase differences to a constant value, both in the case of identical natural frequencies as well as uncertain ones. We further explain the behavior of the system as the number of oscillators grows to infinity.

## 1 Background and introduction 

Over the past decade, considerable attention has been devoted to the problem of coordinated motion of multiple autonomous agents. A variety of disciplines (as diverse as ecology, the social sciences, statistical physics, computer graphics and, indeed, systems and control theory) are developing an understanding of how a group of moving objects (such as flocks of birds, schools of fish, crowds of people \[20, 11\], or collections of autonomous robots or unmanned vehicles \[18, 19\]) can reach a consensus and move in formation without centralized coordination. Interestingly, this has coincided with a surge of activity in the area of network dynamics, which focusses on the relationship between graph structure and dynamical behavior of large networks of diverse origin.

A classic example of distributed coordination in physics, engineering and biology is the synchronization of arrays of coupled nonlinear oscillators \[15, 16, 25\]. Building on long-standing experiments (dating back to Huyghens and van der Pol), the problem of collective synchronization was explored mathematically by the Russian school of Andronov. Norbert Wiener \[24\] also recognized its ubiquity in the natural world, and even speculated about its relevance to the existence of characteristic rhythms in the brain \[17\].

Following on key insights by Winfree \[25\], Kuramoto \[8\] proposed in the 1970s a tractable model for oscillator synchronization that has become archetypal in the physics and dynamical systems literatures. (See \[15\] for an excellent review of the state-of-the-art on this model.) More recently, researchers in the control community \[7, 22, 12\] have recognized that nonlinear synchronization phenomena are mathematically related to the problem of coordination and consensus among multi-agent systems \[13, 6\].

## 2 Model description 

The classic Kuramoto model describes the dynamics of a set of $N$ phase oscillators $\theta_{i}$ with natural frequencies $\omega_{i}$. The time evolution of the $i$-th oscillator is given by:

  -- ----------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\overset{˙}{\theta}}_{i} = {\omega_{i} + {\frac{K}{N}\hspace{0pt}{\sum\limits_{j = 1}^{N}{\sin{({\theta_{j} - \theta_{i}})}}}}}},$$      \(1\)
  -- ----------------------------------------------------------------------------------------------------------------------------------------- -- -------

where $K$ is the coupling strength, a key parameter in the problem. One of Kuramoto's results was to show numerically that when the $\omega_{i}$'s are randomly chosen from a Cauchy probability distribution in the infinite $N$ limit, there is a critical value of the coupling above which all phase differences remain constant, i.e., the oscillators synchronize \[8, 9\]. If we think of the oscillators as points moving on a circle, they would rotate keeping the phase differences constant.

Kuramoto used the magnitude $R$ of the centroid of the points as a 'natural' measure of synchronization:

  -- ---------------------------------------------------------------------------------------------------------------- -- -------
     $${{R\hspace{0pt}e^{\psi}} = {\frac{1}{N}\hspace{0pt}{\sum\limits_{i = 1}^{N}e^{j\hspace{0pt}\theta_{i}}}}}.$$      \(2\)
  -- ---------------------------------------------------------------------------------------------------------------- -- -------

Clearly, if all the $\omega_{i}$'s are the same then $R = 1$ when all agents are in sync. If the natural frequencies are not identical but the oscillators synchronize, $R$ converges to a constant $R_{\infty} < 1$. On the other hand, when all agents are completely out of phase with respect to each other the value of $R$ remains close to $0$ most of the time. Because it characterizes the dynamical behavior of the system, $R$ is referred to as the order parameter in the physics literature.

Kuramoto's analysis used simple trigonometry to rewrite the state equation (1) in terms of the order parameter. After switching to a rotating frame, Eq. (1) becomes:

  -- ----------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\overset{˙}{\theta}}_{i} = {\omega_{i} - {\frac{K}{N}\hspace{0pt}R\hspace{0pt}{\sin{({\theta_{i} - \psi})}}}}}.$$      \(3\)
  -- ----------------------------------------------------------------------------------------------------------------------- -- -------

In other words, each phase is modulated by the magnitude $R$ and phase $\psi$ of the average phasor. In physics notation, this constitutes a mean field or "all-to-all" model.

With some brilliant intuition, Kuramoto showed that for an infinite number of oscillators there is a critical coupling $K_{c}$ below which the oscillators are incoherent (i.e., fully unsynchronized). In addition, there is another critical coupling $K_{L} \geq K_{c}$ above which all oscillators are synchronized. In that regime, the order parameter $R$ grows exponentially in time until it saturates at a value ${R_{\infty}\hspace{0pt}{(K)}} \leq 1$. The branch of $R$ with $K > K_{L}$ is called the fully synchronized state, while $K < K_{c}$ corresponds to the totally unsynchronized state. Kuramoto also calculated analytically the value for $K_{c}$ and $R_{\infty}$ for a few well-known distributions in the case of an infinite number of oscillators connected all-to-all.

Despite its success, several aspects of the well-studied $N\rightarrow\infty$, all-to-all Kuramoto model are still a puzzle, as summarized beautifully in the review by Steve Strogatz \[15\]. For instance, what does it mean that $R$ stays close to zero in the unsynchronized state $K < K_{c}$? This cannot be true at all times: when $K = 0$ and the $\omega_{i}$'s are irrational with respect to each other, the trajectories are dense on the $N$-torus resulting in an $R$ which will almost surely visit any number between 0 and 1. However, simulations indicate that it is true most of the time. On the other extreme, the case of few oscillators has been tackled in the dynamical systems literature with rigorous bifurcation analysis. However, even basic results are not available for the large but finite $N$ case, which is of utmost interest in systems engineering.

Our goal here is to perform a system theoretic analysis of the finite $N$ case with arbitrary connectivity. To proceed, we rewrite the model in terms of the incidence matrix of the undirected graph that describes the interconnection topology--- the standard all-to-all case is then the specific case of the complete graph. We then provide several necessary as well as sufficient lower bounds for the critical coupling $K_{L}$. These include a bound for $K$ below which there is no fixed-point, and a value of $K$ above which there is a unique fixed-point. This extends similar results in \[5\] for the case of 2 oscillators with a finite set of values for the natural frequencies.

## 3 Graph theoretical formulation of Kuramoto's model 

A good source for the necessary graph theory terminology is \[4\]. We formalize our results through two matrices that encode the topology of the connections. The incidence matrix $B$ of an oriented graph $\mathcal{G}^{\sigma}$ with $N$ vertices and $e$ edges is the $N \times e$ matrix such that: $B_{i\hspace{0pt}j} = 1$ if the edge $j$ is incoming to vertex $i$, $B_{i\hspace{0pt}j} = {- 1}$ if edge $j$ is outcoming from vertex $i$, and $0$ otherwise. The symmetric $N \times N$ matrix defined as: $L = {B\hspace{0pt}B^{T}}$ is called the Laplacian of $\mathcal{G}$ and is independent of the choice of orientation $\sigma$. The Laplacian has several important properties: $L$ is always positive semidefinite with a zero eigenvalue; the algebraic multiplicity of its zero eigenvalue is equal to the number of connected components in the graph; the $N$-dimensional eigenvector associated with the zero eigenvalue is the vector of ones, $\mathbf{1}_{N}$. It is known that the spectrum of the Laplacian matrix $\{{\lambda_{i}\hspace{0pt}{(L)}}\}$ captures many topological properties of the graph. Specifically, Fiedler showed that the first non-zero eigenvalue $\lambda_{2}\hspace{0pt}{(L)}$ (sometimes denoted the algebraic connectivity) gives a measure of connectedness of the graph. If we associate a positive number $W_{i}$ to each edge and we form the diagonal matrix $W_{e \times e}:={\text{diag}\hspace{0pt}{(W_{i})}}$, then the matrix ${L_{W}\hspace{0pt}{(\mathcal{G})}} = {B\hspace{0pt}W\hspace{0pt}B^{T}}$ is a weighted Laplacian which fulfills the above properties.

In this framework, the Kuramoto model (1) can be generalized to any general interconnection topology as:

  -- ------------------------------------------------------------------------------------------------------------------- -- -------
     $${\overset{˙}{\theta} = {\omega - {\frac{K}{N}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}}}},$$      \(4\)
  -- ------------------------------------------------------------------------------------------------------------------- -- -------

where $B$ is the incidence matrix of the unweighted graph, and $\theta$ and $\omega$ are $N \times 1$ vectors. (It is also helpful to define the $e \times 1$ vector of phase differences $\phi:={B^{T}\hspace{0pt}\theta}$.) A generalization of the order parameter defined in (2) for the general Kuramoto model is:

  -- -------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${r^{2} = \frac{{N^{2} - {2\hspace{0pt}e}} + {2\hspace{0pt}\, 1_{e}^{T}\hspace{0pt}{\cos{({B^{T}\hspace{0pt}\theta})}}}}{N^{2}}}.$$      \(5\)
  -- -------------------------------------------------------------------------------------------------------------------------------------- -- -------

It is easy to show that when the graph is complete, this is the square of the magnitude of the average phasor, i.e., for $B = B_{c}$, we have $r_{c}^{2} = R^{2}$. While the average phasor interpretation does not generalize to general connected topologies, the above notion of an order parameter does generalize to arbitrary connected graphs. In fact the order parameter can be conveniently written in terms of the Laplacian matrix $L$ of the underlying graph, as a measure of synchrony, or alignment. Specifically, after some algebra, Equation (5) can be written as

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${r^{2} = {1 - {\frac{1}{N}\hspace{0pt}{\lbrack e^{j\hspace{0pt}\theta}\rbrack}^{\ast}\hspace{0pt}L\hspace{0pt}{\lbrack e^{j\hspace{0pt}\theta}\rbrack}}} = {1 - {\frac{1}{N}\hspace{0pt}{({{{\lbrack{\cos\theta}\rbrack}^{T}\hspace{0pt}L\hspace{0pt}{\lbrack{\cos\theta}\rbrack}} + {{\lbrack{\sin\theta}\rbrack}^{T}\hspace{0pt}L\hspace{0pt}{\lbrack{\sin\theta}\rbrack}}})}}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where ${\lbrack e^{j\hspace{0pt}\theta}\rbrack} = {\lbrack{e^{j\hspace{0pt}\theta_{1}}\hspace{0pt}\cdots\hspace{0pt}e^{j\hspace{0pt}\theta_{N}}}\rbrack}^{T}$ is the vector of complex phasors, and ^∗^ denotes complex conjugate transpose.

The above equation provides us with an interesting interpretation of the order parameter: each individual oscillator $i$ can be thought of as a rotor moving on a circle with unit radius, with velocity vector $v_{i} = e^{j\hspace{0pt}\theta_{i}}$. The total measure of disagreement between all velocity vectors, or the global measure of asynchrony can be written as $\sum_{i}{\sum_{j \in \mathcal{N}_{i}}{\|{v_{i} - v_{j}}\|}^{2}}$, which is nothing but $N^{2}\hspace{0pt}{({1 - r^{2}})}$. In other words, the order parameter is a scaled measure of agreement among velocity vectors of rotors, hence a measure of synchronization. This allows us to extend the stability analysis to a graph with arbitrary connected topology.

###### Remark 1 

In the limit of small angles, the general Kuramoto model (4) gives the continuous-time Vicsek flocking boid model \[21\] which was analyzed in \[6\]: ${\overset{˙}{\theta} = {\omega - {{({K/N})}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}}} \approx {\omega - {{({K/N})}\hspace{0pt}L\hspace{0pt}\theta}}}.$ Conversely, the classic Kuramoto model (1) can be thought of as a nonlinear extension of the Vicsek model for a complete graph.

###### Remark 2 

It is straightforward to show that the analytical simplification (Eq. 3) in the (standard) all-to-all model appear as a result of the special symmetry of the Laplacian of the complete graph:

  -- ------------------------------------------------------------------------------------------------------------------- -- -------
     $${L_{c} = {B_{c}\hspace{0pt}B_{c}^{T}} = {{N\hspace{0pt}I} - {\mathbf{1}_{N}\hspace{0pt}\mathbf{1}_{N}^{T}}}}.$$      \(6\)
  -- ------------------------------------------------------------------------------------------------------------------- -- -------

## 4 Synchronization of identical coupled oscillators 

We start by considering the general Kuramoto model (4) in its unperturbed version, i.e., when all the natural frequencies $\omega_{i}$ are identical:

  -- ------------------------------------------------------------------------------------------------------------ -- -------
     $${\overset{˙}{\theta} = {- {\frac{K}{N}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}}}}.$$      \(7\)
  -- ------------------------------------------------------------------------------------------------------------ -- -------

(By switching to a rotating frame, it is easily shown that we can assume that the natural frequencies $\omega_{i}$ are all zero, without loss of generality.)

###### Theorem 1 

Consider the unperturbed Kuramoto model (7) defined over an arbitrary connected graph with incidence matrix $B$. For any value of the coupling $K > 0$, all trajectories will converge to the set of equilibrium solutions. In particular the synchronized state is locally asymptotically stable. Moreover, the rate of approach to the synchronized state is no worse than ${({{{2\hspace{0pt}K}/\pi}\hspace{0pt}N})}\hspace{0pt}\lambda_{2}\hspace{0pt}{(L)}$, where $\lambda_{2}\hspace{0pt}{(L)}$ is the Fiedler eigenvalue or the algebraic connectivity of the graph.

###### Proof 4.2. 

Consider the function ${U_{1}\hspace{0pt}{(\theta)}} = {1 - r^{2}} = \frac{4\hspace{0pt}\left\| {\sin{(\frac{B^{T}\hspace{0pt}\theta}{2})}} \right\|^{2}}{N^{2}}$, where $r^{2}$ has been defined in (5). A simple calculation reveals that ${\nabla_{\theta}U} = {{({2/N^{2}})}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}}$ which leads to

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\overset{˙}{U}\hspace{0pt}{(\theta)}} = {\nabla_{\theta}{U\hspace{0pt}\overset{˙}{\theta}}} = {- {\frac{2}{K\hspace{0pt}N}\hspace{0pt}{\overset{˙}{\theta}}^{T}\hspace{0pt}\overset{˙}{\theta}}} \leq 0}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Therefore, the positive function $0 \leq {U\hspace{0pt}{(\theta)}} \leq 1$ is a non-increasing function along the trajectories of the system. By using LaSalle's invariance principle we conclude that $U$ is a Lyapunov function for the system, and that all trajectories converge to the set where $\overset{˙}{\theta}$ is zero, i.e., the equilibrium solutions.

Define now the $e \times e$ diagonal matrix ${W\hspace{0pt}{(\phi)}}:={\text{~diag}\hspace{0pt}{({{sinc}{(\phi_{i})}})}}$, where ${{sinc}{(\phi_{i})}} = {{\sin{(\phi_{i})}}/\phi_{i}}$ is positive for $\phi_{i} \in {({- \pi},\pi)}^{e}$. Note also that the angles move on an N- torus. Consider the proper subset of the torus in which $\phi \in {({- \pi},\pi)}^{e}$. The diagonal weight matrix ${W\hspace{0pt}{(\phi)}} > 0$ can be thought of as phase-dependent weight functions on the graph. The trajectories converge to fixed-points, which are the solutions of ${{L_{W}\hspace{0pt}\theta}:={\left( {B\hspace{0pt}W\hspace{0pt}{(\phi)}\hspace{0pt}B^{T}} \right)\hspace{0pt}\theta} = 0}.$ The fact that $({\theta_{0}\hspace{0pt}\mathbf{1}_{N}})$ is a locally exponentially stable equilibrium solution follows easily: for any connected graph the null space of the weighted Laplacian contains only the vector $\mathbf{1}_{N}$. Note that in general, for an arbitrary connected topology the system has many other equilibrium solutions, some of which might even be locally stable. One such example is the ring topology \[10\].

Alternatively, one could use a different Lyapunov function similar to the approach in \[14\] and consider the quadratic Lyapunov function candidate $U_{2} = {\frac{1}{2}\hspace{0pt}{\sum_{i = 1}^{N}{\sum_{j = 1}^{N}{({\theta_{i} - \theta_{j}})}^{2}}}} = {\theta^{T}\hspace{0pt}L_{c}\hspace{0pt}\theta}$, where $L_{c} = {{N\hspace{0pt}I} - \mathbf{1}\mathbf{1}^{\mathbf{T}}}$ is the Laplacian matrix of a complete graph. Note that ${B^{T}\hspace{0pt}\mathbf{1}} = 0$, therefore, a simple calculation reveals that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\overset{˙}{U_{2}} = {- {\frac{K}{N}\hspace{0pt}\theta^{T}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}}} = {- {\frac{K}{N}\hspace{0pt}\theta^{T}\hspace{0pt}B\hspace{0pt}W\hspace{0pt}{(\phi)}\hspace{0pt}B^{T}\hspace{0pt}\theta}} \leq 0}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

It is interesting to note that the Lyapunov function $U_{2}$ is small angle approximation of Lyapunov function $U_{1}$.

Using the same argument as above, we conclude that the largest sublevel set of $U_{2}$ which is contained inside ${{|\theta_{l}|} < {\frac{\pi}{2}\hspace{0pt}l} = 1},{\cdots,e}$ is positively invariant. With the quadratic function $U_{2}\hspace{0pt}{(\theta)}$ however, we can show that locally, the convergence is exponential with the rate determined by the second smallest eigenvalue of the weighted Laplacian:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\overset{˙}{U_{2}} \leq {- {\frac{K}{N}\hspace{0pt}\lambda_{2}\hspace{0pt}{({B\hspace{0pt}W\hspace{0pt}{(\phi)}\hspace{0pt}B^{T}})}\hspace{0pt}{\|\theta_{\mathbf{1}^{\perp}}\|}^{2}}} \leq {- {\frac{2\hspace{0pt}K}{\pi\hspace{0pt}N}\hspace{0pt}\lambda_{2}\hspace{0pt}{(L)}\hspace{0pt}{\|\theta_{\mathbf{1}^{\perp}}\|}^{2}}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

since ${\lambda_{2}\hspace{0pt}{({B\hspace{0pt}W\hspace{0pt}{(\phi)}\hspace{0pt}B^{T}})}} \leq {{({2/\pi})}\hspace{0pt}\lambda_{2}\hspace{0pt}{({B\hspace{0pt}B^{T}})}}$.

###### Corollary 4.3. 

For the complete graph, ${\lambda_{2}\hspace{0pt}{(L_{c})}} = N$ and the synchronization rate for the mean-field model is no worse than ${2\hspace{0pt}K}/\pi$.

###### Remark 4.4. 

Similar results hold even if the topology of the graph changes in time \[6\]. The result can be extended to general notions of connectivity, i.e., when the interconnection graph is not connected at all times but there is a path between any two nodes over contiguous, non-overlapping, and uniformly bounded time intervals. It is also possible to generalize to the case of directed graphs by introducing notions of weak connectivity \[12\].

###### Remark 4.5. 

The synchronization argument can be readily extended to the case of more complicated coupling functions $f\hspace{0pt}{( \cdot )}$ (other than the $\sin{( \cdot )}$ function) so long as ${\phi^{T}\hspace{0pt}f\hspace{0pt}{(\phi)}} \geq 0$.

###### Remark 4.6. 

The function $\mathbf{1}_{e}^{T}\hspace{0pt}{\cos{({B^{T}\hspace{0pt}\theta})}}$ is an energy function for the XY-model in statistical physics. It was considered as a Lyapunov-like function for the Kuramoto model by Van Hemmen and Wreszinski \[5\], as well as in \[7\].

###### Remark 4.7. 

The global results obtained by Watanabe and Strogatz \[23\] require all-to-all connectivity. An extension of the methodology in \[23\] to arbitrary topologies does not appear to be trivial.

## 5 The case of non-identical oscillators 

In the rest of the paper we treat the more complicated case of oscillators with non-identical natural frequencies. Although there is an extensive literature for the $N\rightarrow\infty$ case with all-to-all connectivity, we will focus here on the case of finite $N$ and arbitrary topology given by Eq. (4). We consider the frequencies to be random perturbations which, albeit drawn from a probability distribution, remain constant in time, i.e., the dynamics (4) is deterministic yet uncertain. This problem is distinct to some treatments in the physics literature, which transform the problem into a Fokker-Planck equation, effectively connected to a stochastic differential equation.

Synchronization is best defined in a grounded system, where the phases are defined with respect to a reference variable (or 'ground'). This can be achieved by any projection $V_{N \times {({N - 1})}}$ such that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{{{V^{T}\hspace{0pt}V} = I},{{V\hspace{0pt}V^{T}} = {I - \frac{\mathbf{1}_{N}\hspace{0pt}\mathbf{1}_{N}^{T}}{N}} = \frac{L_{c}}{N}}},{{V^{T}\hspace{0pt}\mathbf{1}_{N}} = \mathbf{0}}}.$$      \(8\)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

Thus, $V$ is a matrix of $N - 1$ orthonormal vectors orthogonal to the vector $\mathbf{1}_{N}$ which generate the set of grounded coordinates $\overline{\theta}:={V^{T}\hspace{0pt}\theta}$ and frequencies $\overline{\omega}:={V^{T}\hspace{0pt}\omega}$. The grounded Kuramoto model is:

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${\overset{˙}{\overline{\theta}} = {\overline{\omega} - {\frac{K}{N}\hspace{0pt}V^{T}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}V\hspace{0pt}\overline{\theta}})}}}} = {\overline{\omega} - {\frac{K}{N}\hspace{0pt}V^{T}\hspace{0pt}B\hspace{0pt}W\hspace{0pt}{(\overline{\theta})}\hspace{0pt}B^{T}\hspace{0pt}V\hspace{0pt}\overline{\theta}}}},$$      \(9\)
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where, again, ${W\hspace{0pt}{(\overline{\theta})}}:={{diag}\hspace{0pt}{({{sinc}{(\phi_{i})}})}}$ and $\phi = {B^{T}\hspace{0pt}V\hspace{0pt}\overline{\theta}}$. In this grounded system, the synchronized state is a fixed point.

###### Remark 5.8. 

From Eq. (9) it is easy to see why the natural frequencies can be centered around zero without loss of generality. Multiply Eq. (9) from the left by $V$ and use (8) and ${B^{T}\hspace{0pt}\mathbf{1}_{N}} = 0$ to recover the original Eq. (4) with new variables $\Theta = {\theta - {{\lbrack{{\langle\omega\rangle}\hspace{0pt}t}\rbrack}\hspace{0pt}\, 1_{N}}}$ and frequencies $\Omega = {\omega - {{\langle\omega\rangle}\hspace{0pt}\, 1_{N}}}$, where $<\omega>$ is the average frequency.

## 6 Bound for the asymptotic value of the order parameter 

Consider a Lyapunov function candidate based on the square of the order parameter $r^{2}$ defined in (5). The derivative of this function along the trajectories is

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${\overset{˙}{r^{2}} = {\frac{1}{N^{2}}\hspace{0pt}\left\lbrack {{\frac{K}{N}\hspace{0pt}{({\sin{B^{T}\hspace{0pt}\theta}})}^{T}\hspace{0pt}B^{T}\hspace{0pt}B\hspace{0pt}{({\sin{B^{T}\hspace{0pt}\theta}})}} - {\omega^{T}\hspace{0pt}B\hspace{0pt}{\sin{B^{T}\hspace{0pt}\theta}}}} \right\rbrack}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

which is an ellipsoid in the $\sin{({B^{T}\hspace{0pt}\theta})}$ coordinate centered at $\frac{N\hspace{0pt}\omega}{K}$. Outside of a neighborhood of the origin given by

  -- -------------------------------------------------------------------------------------------------------------- -- --------
     $${\|{B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}}\|}_{2} > {\frac{N}{K}\hspace{0pt}{\|\omega\|}_{2}}$$      \(10\)
  -- -------------------------------------------------------------------------------------------------------------- -- --------

the derivative is positive, resulting in growth of the order parameter. The boundary of this region contains the equilibria. By using an ultimate boundedness argument, the trajectories are confined to the smallest sublevel-set of $r$ containing the set defined by (10).

We now use (10) to obtain an estimate of the asymptotic value of the order parameter. The vector $\sin{({B^{T}\hspace{0pt}\theta})}$ can be decomposed into two orthogonal components: $y_{1}\hspace{0pt}{(\theta)}$, in the null space of $B$, and $y_{2}\hspace{0pt}{(\theta)}$ in the range space of $B^{T}$. The first component is annihilated when it is multiplied by $B$ on the left. As a result, the region over which ${\overset{˙}{r}}^{2}$ is positive can be characterized as

  -- ------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\|{y_{2}\hspace{0pt}{(\theta)}}\|}_{2} > {\frac{N}{K\hspace{0pt}\sqrt{\lambda_{2}\hspace{0pt}{(L)}}}\hspace{0pt}{\|\omega\|}_{2}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------- --

where $\lambda_{2}\hspace{0pt}{(L)}$ is the algebraic connectivity of the unweighted graph. We now bound the value of $U$ over the region where ${\overset{˙}{r}}^{2}$ is negative. A simple bounding reveals that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{2\hspace{0pt}\mathbf{1}^{T}\hspace{0pt}{\cos\left( {B^{T}\hspace{0pt}\theta} \right)}} \leq {{\|\mathbf{1}\|}^{2} + {\|{\cos\left( {B^{T}\hspace{0pt}\theta} \right)}\|}^{2}} = {{2\hspace{0pt}{\|\mathbf{1}\|}^{2}} - {\|{\sin\left( {B^{T}\hspace{0pt}\theta} \right)}\|}^{2}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

from which

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${r^{2} \leq \frac{N^{2} - {\|{\sin{B^{T}\hspace{0pt}\theta}}\|}^{2}}{N^{2}} \leq \frac{N^{2} - {\|{y_{2}\hspace{0pt}(\theta)}\|}^{2}}{N^{2}} \leq \frac{N^{2} - \frac{N^{2}\hspace{0pt}\left\| w \right\|^{2}}{K^{2}\hspace{0pt}\lambda_{2}\hspace{0pt}(L)}}{N^{2}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

We can immediately observe that the asymptotic behavior of the order parameter is inversely proportional to the algebraic connectivity of the graph. Of course, because of the over-bounding, the bound is conservative---its asymptotic value is 1 as opposed to the actual less-than-one value. Nevertheless, this gives us a bound on the growth rate of $r^{2}$, and, as a result, the growth rate on $r$ is bounded by $\frac{1}{\sqrt{\lambda_{2}\hspace{0pt}{(L)}}}$.

This means that asymptotically

  -- ------------------------------------------------------------------------------------------ --
     $$r \leq \sqrt{1 - \frac{{\| w\|}^{2}}{K^{2}\hspace{0pt}\lambda_{2}\hspace{0pt}{(L)}}}$$   
  -- ------------------------------------------------------------------------------------------ --

which would result in an increase rate of $\mathcal{O}\hspace{0pt}{(\frac{1}{\sqrt{N}})}$ when the graph is complete.

###### Remark 6.9. 

Consider a complete graph where the natural frequencies are independent random variables chosen from a normal distribution $\omega_{i} \sim {\mathcal{N}\hspace{0pt}{(0,\sigma)}}$. Then ${\| w\|}_{2}$ scales as $\sqrt{N}\hspace{0pt}\sigma$, which results in a bound for $r < \sqrt{1 - {({\sigma/K})}^{2}}$ that is independent of $N$.

###### Remark 6.10. 

In \[5\], the authors added a linear term $\omega^{T}\hspace{0pt}\theta$ to the Lyapunov function candidate to guarantee negativity of the derivative everywhere except at the fixed-points, reducing the perturbed model to a gradient system. The linear term, however, makes the Lyapunov function indefinite.

We will see in the next section that if $K$ is large enough to guarantee the existence of a unique fixed point (via a contraction argument), condition (10) will be trivially satisfied. This means that if $K$ is large enough the derivative of the order parameter will be positive, resulting in the asymptotic stability of the synchronized state.

## 7 Bounds for the critical coupling 

As the coupling $K$ is decreased, there is a critical value $K_{L}$ below which no fixed point exists, resulting in a running solution for the grounded system (9). This means that the system cannot be fully synchronized for $K < K_{L}$.

An easy sufficient condition for the fixed point ${\overline{\theta}}^{\ast}$ to be stable is for $\phi^{\ast} = {B^{T}\hspace{0pt}V\hspace{0pt}{\overline{\theta}}^{\ast}}$ to be contained in any closed subset of ${({- \frac{\pi}{2}},\frac{\pi}{2})}^{e}$, which implies that ${|\theta^{\ast}|} < \frac{\pi}{4}$. This is demonstrated by taking the Jacobian of $V^{T}\hspace{0pt}B\hspace{0pt}{\sin{B^{T}\hspace{0pt}\theta}}$, and noting that it is equal to $V^{T}\hspace{0pt}B\hspace{0pt}\text{diag}\hspace{0pt}{\lbrack{\cos{({B^{T}\hspace{0pt}\theta^{\ast}})}}\rbrack}\hspace{0pt}B^{T}\hspace{0pt}V$, which is positive definite over that set.

### 7.1 Critical value of coupling for complete graphs 

Our results generalize those of Van Hemmen et al. \[5\] in the case of a complete graph. Specifically, it can be shown that the critical value of the coupling is determined by the value of $K$ for which the fixed point disappears. This can be explained by looking at the fixed point equation ${{B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta^{\ast}})}}} = \frac{N\hspace{0pt}\omega}{K}}.$

Let $\omega_{m\hspace{0pt}a\hspace{0pt}x} = {\|\omega\|}_{\infty}$ and note that the induced infinity norm of a matrix is the maximum absolute row sum, i.e., ${\| B\|}_{\infty} = d_{m\hspace{0pt}a\hspace{0pt}x}$, where $d_{m\hspace{0pt}a\hspace{0pt}x}$ is the maximum degree of the graph. In the case of a complete graph, $d_{m\hspace{0pt}a\hspace{0pt}x} = {N - 1}$. Then,

  -- ------------------------------------------------------------------------------------------------------ --
     $$\frac{N\hspace{0pt}\omega_{m\hspace{0pt}a\hspace{0pt}x}}{K} \leq d_{m\hspace{0pt}a\hspace{0pt}x}$$   
  -- ------------------------------------------------------------------------------------------------------ --

resulting in the following lower bound for $K_{L}$, the coupling above which a fixed point exists:

  -- ---------------------------------------------------------------------------------------------------------- --
     $${K_{L} > \frac{N\hspace{0pt}\omega_{m\hspace{0pt}a\hspace{0pt}x}}{d_{m\hspace{0pt}a\hspace{0pt}x}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------- --

This bound can be tightened by using the generalized inverse of $V^{T}\hspace{0pt}B$ and bounding the component of the $\sin{({B^{T}\hspace{0pt}\theta})}$ in the range of $B^{T}$. The generalized inverse, denoted by ${({V^{T}\hspace{0pt}B})}^{\#}$, is equal to $B^{T}\hspace{0pt}V\hspace{0pt}\Lambda^{- 1}$, where $\Lambda$ is the $N - 1$ diagonal matrix of the eigenvalues of the unweighted Laplacian. We therefore have the following expression

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{({\sin{({B^{T}\hspace{0pt}\theta})}})}_{R\hspace{0pt}{(B^{T})}} = {B^{T}\hspace{0pt}V\hspace{0pt}\Lambda^{- 1}\hspace{0pt}V^{T}\hspace{0pt}\frac{N\hspace{0pt}\omega}{K}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Noting that $L^{\#} = {V\hspace{0pt}\Lambda^{- 1}\hspace{0pt}V^{T}}$, we have

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{({\sin{({B^{T}\hspace{0pt}\theta})}})}_{R\hspace{0pt}{(B^{T})}} = {B^{T}\hspace{0pt}L^{\#}\hspace{0pt}B\hspace{0pt}{\sin{({B^{T}\hspace{0pt}\theta})}}} = {B^{T}\hspace{0pt}L^{\#}\hspace{0pt}\frac{N\hspace{0pt}\omega}{K}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The generalized inverse of the Laplacian, in the case of a complete graph can be written as $L_{c}^{\#} = {\frac{1}{N}\hspace{0pt}{({I - \frac{\mathbf{1}\mathbf{1}^{\mathbf{T}}}{N}})}}$. Noting that the infinity norm of the $\sin$ vector is less than or equal to 1, and that ${B^{T}\hspace{0pt}L^{\#}\hspace{0pt}B} = \frac{B^{T}\hspace{0pt}B}{N}$, we have

  -- -------------------------------------------------------------------------------------------------------------- --
     $${\frac{{\|{B^{T}\hspace{0pt}\omega}\|}_{\infty}}{K} \leq \frac{{\|{B^{T}\hspace{0pt}B}\|}_{\infty}}{N}},$$   
  -- -------------------------------------------------------------------------------------------------------------- --

which gives us the bound

  -- ------------------------------------------------------------------------------------------------------------ --
     $${K_{L} \geq {{\|{B^{T}\hspace{0pt}\omega}\|}_{\infty}\hspace{0pt}\frac{N}{2\hspace{0pt}{({N - 1})}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------ --

This is in excellent agreement with that of Van Hemmen et al. \[5\] which they obtained for the simplest case of two oscillators.

###### Remark 7.11. 

If the graph is a tree, $V^{T}\hspace{0pt}B$ has full row rank and $\sin{({B\hspace{0pt}\theta})}$ does not have a component in the null space of $L$. In that case $K_{L} > {\|{B^{T}\hspace{0pt}L^{\#}\hspace{0pt}\omega}\|}_{\infty}$ is a tight bound, meaning that it is necessary and sufficient for synchronization. In the general case, however, this bound is just necessary.

### 7.2 Existence and uniqueness of stable fixed points 

The fixed point equation can be written as

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\theta = {{({B\hspace{0pt}W\hspace{0pt}{({B^{T}\hspace{0pt}\theta})}\hspace{0pt}B^{T}})}^{\#}\hspace{0pt}\frac{N\hspace{0pt}\omega}{K}} = {L_{W}^{\#}\hspace{0pt}{({B^{T}\hspace{0pt}\theta})}\hspace{0pt}\frac{N\hspace{0pt}\omega}{K}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Using Brouwer's fixed point theorem (i.e., a continuous function that maps a non-empty compact, convex set $X$ into itself has at least one fixed-point), we can develop conditions which guarantee the existence (but not uniqueness) of the fixed point. If a fixed-point exists in any compact subset of $\theta \in {({- \frac{\pi}{4}},\frac{\pi}{4})}$, it is stable, since this will ensure that $B^{T}\hspace{0pt}\theta$ is between $- \frac{\pi}{2}$ and $\frac{\pi}{2}$. We therefore have to ensure that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${K > {\frac{4}{\pi}\hspace{0pt}N\hspace{0pt}\max\limits_{{|\theta_{i}|} < \frac{\pi}{4}}\hspace{0pt}{\|{L_{W}^{\#}\hspace{0pt}{({B^{T}\hspace{0pt}\theta})}}\|}_{\infty}\hspace{0pt}{\|\omega\|}_{\infty}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Simulations indicate that in the case of a complete graph, the infinity norm of the matrix $L_{W}^{\#}$ scales as $\mathcal{O}\hspace{0pt}{(\frac{1}{N})}$. It is worth mentioning that the norm of $L_{W}^{\#}$ is a well studied object in the theory of Markov chains. The infinity norm of $L_{W}^{\#}$ is a measure of the sensitivity of the stationary distribution of the chain associated with $L$ with respect to additive perturbations \[2\].

If the uncertain natural frequencies are 2-norm bounded, a better strategy would be to impose the boundedness condition with respect to the Euclidean norm. A sufficient condition for local stability of the fixed-point is for $\theta_{i}$ to belong to $({- \frac{\pi}{4}},\frac{\pi}{4})$. This amounts to having the Euclidean norm of $\theta$ be less than $\frac{\pi}{4}\hspace{0pt}\sqrt{N}$. Again, using Brouwer's sufficient condition for existence of fixed-points we have:

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\|{({B\hspace{0pt}W\hspace{0pt}{({B^{T}\hspace{0pt}\theta})}\hspace{0pt}B^{T}})}^{\#}\|}_{2}\hspace{0pt}\frac{N\hspace{0pt}{\|\omega\|}_{2}}{K}} \leq {\frac{\pi}{4}\hspace{0pt}\sqrt{N}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Hence, a sufficient condition for synchronization of all oscillators can be determined in terms of a lower bound for $K$:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${K_{L} \geq {\frac{4}{\pi}\hspace{0pt}\frac{\sqrt{N}\hspace{0pt}{\| w\|}_{2}}{{\min_{{|\theta_{i}|} \leq \frac{\pi}{4}}\lambda_{2}}\hspace{0pt}{({L_{W}\hspace{0pt}{(\theta)}})}}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

where we used the fact that ${\|{({B\hspace{0pt}W\hspace{0pt}{({B^{T}\hspace{0pt}\theta})}\hspace{0pt}B})}^{\#}\|}_{2} = \frac{1}{\lambda_{2}\hspace{0pt}{(L_{W})}}$, and $\lambda_{2}$ is the algebraic connectivity of the (weighted) graph. A lower bound on the minimum value of $\lambda_{2}$ occurs for the minimum value of the weight which is $\frac{2}{\pi}$. As a result,

  -- -------------------------------------------------------------------------------------------------------- -- --------
     $${K_{L} \geq {2\hspace{0pt}\frac{\sqrt{N}\hspace{0pt}{\| w\|}_{2}}{\lambda_{2}\hspace{0pt}{(L)}}}}.$$      \(11\)
  -- -------------------------------------------------------------------------------------------------------- -- --------

###### Remark 7.12. 

Using the upper bound provided for the order parameter earlier, we can derive an upper bound for the asymptotic value of $r$ at $K_{L}$: ${r_{\infty}\hspace{0pt}{(K_{L})}} \leq \frac{\sqrt{3}}{2}$. Furthermore, if the stable fixed-point is in ${({- {\pi/4}},{\pi/4})}^{N}$, then the order parameter is lower bounded by $\sqrt{16 - \pi^{2}}/4$.

### 7.3 Bounds for the existence of a unique fixed-point 

In order to guarantee the existence of a unique fixed point we use Banach's contraction principle and ensure that the right hand side is a contraction. By noting that the Lipschitz constant for the ${sinc}{( \cdot )}$ function is $\alpha_{s} = \frac{1}{2}$, we provide a sufficient condition for contractivity (and therefore uniqueness of the fixed-point).

We impose the contractivity condition on the $N - 1$ dimensional grounded system. In the grounded case, we have $\overline{\theta} = {V^{T}\hspace{0pt}\theta}$, and

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\overline{\theta} = {{({V^{T}\hspace{0pt}B\hspace{0pt}W\hspace{0pt}{({B^{T}\hspace{0pt}\theta})}\hspace{0pt}B^{T}\hspace{0pt}V})}^{- 1}\hspace{0pt}\frac{N\hspace{0pt}V^{T}\hspace{0pt}\omega}{K}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

After some algebra, the contraction requirement amounts to

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${K \geq {\frac{\pi^{2}}{4}\hspace{0pt}\frac{N\hspace{0pt}\lambda_{m\hspace{0pt}a\hspace{0pt}x}\hspace{0pt}{(L)}\hspace{0pt}{\| w\|}_{2}}{\lambda_{2}\hspace{0pt}{(L)}^{2}}}},$$      \(12\)
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

where $\lambda_{m\hspace{0pt}a\hspace{0pt}x}$ is the largest eigenvalue of the Laplacian of the graph.

Interestingly, this value of $K$ also ensures that the derivative of $r^{2}$ is increasing,i.e., inequality (10) is satisfied, which means that the order parameter is increasing. Of course this is probably stronger than what is necessary for uniqueness, as the contraction argument is only sufficient. Nevertheless, we see that there is a large enough but finite value of the coupling which guarantees the existence and uniqueness of fixed points.

We now state the following theorem:

###### Theorem 7.13. 

Consider the Kuramoto model for non-identical coupled oscillators with different natural frequencies $\omega_{i}$. For $K \geq K_{L}:={2\hspace{0pt}\frac{\sqrt{N}\hspace{0pt}\left\| w \right\|_{2}}{\lambda_{2}\hspace{0pt}{(L)}}}$, there exist at least one fixed-point for ${|\theta_{i}|} < \frac{\pi}{4}$ or ${|{({B^{T}\hspace{0pt}\theta})}_{i}|} < \frac{\pi}{2}$. Moreover, for $K \geq {\frac{\pi^{2}}{4}\hspace{0pt}\frac{N\hspace{0pt}\lambda_{m\hspace{0pt}a\hspace{0pt}x}\hspace{0pt}{(L)}\hspace{0pt}\left\| w \right\|_{2}}{\lambda_{2}\hspace{0pt}{(L)}^{2}}}$ there is only one stable fixed-point (modulo a vector in the span of $\mathbf{1}_{N}$), and the order parameter is strictly increasing.

###### Proof 7.14. 

Proof of Theorem 3 : As we see before fixed point equation can be written as

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${V^{T}\hspace{0pt}B\hspace{0pt}W\hspace{0pt}{(\overline{\theta})}\hspace{0pt}B^{T}\hspace{0pt}V\hspace{0pt}\overline{\theta}} = {\frac{K}{N}\hspace{0pt}\overline{\omega}}$$      \(13\)
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

or

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $\overline{\theta} = {{({V^{T}\hspace{0pt}B\hspace{0pt}W\hspace{0pt}{(\overline{\theta})}\hspace{0pt}B^{T}\hspace{0pt}V})}^{- 1}\hspace{0pt}\frac{K}{N}\hspace{0pt}\overline{\omega}}$      \(14\)
     $= {L_{W}\hspace{0pt}{(\overline{\theta})}^{- 1}\hspace{0pt}\frac{K}{N}\hspace{0pt}\overline{\omega}}$                                                                                      \(15\)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

We will use Banach's contraction principle to show that (15) has a unique solution when $V\hspace{0pt}\overline{\theta}$ is in any compact subset of ${({- \frac{\pi}{2}},\frac{\pi}{2})}^{N}$. We therefore need to show that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${\|{\frac{N}{K}\hspace{0pt}{({{L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}^{- 1}} - {L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}^{- 1}}})}\hspace{0pt}\overline{\omega}}\|} \leq {\alpha\hspace{0pt}{\|{{\overline{\theta}}_{1} - {\overline{\theta}}_{2}}\|}}$$      \(16\)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

holds for some $0 \leq \alpha < 1$ and some norm. Using the 2-norm, we have

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     ${\|{\frac{N}{K}\hspace{0pt}{({{L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}^{- 1}} - {L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}^{- 1}}})}\hspace{0pt}\overline{\omega}}\|}_{2}$   $=$      ${\|{\frac{N}{K}\hspace{0pt}L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}^{- 1}\hspace{0pt}{({{L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}} - {L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}}})}\hspace{0pt}L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}^{- 1}\hspace{0pt}\overline{\omega}}\|}_{2}$                                                                                                                                                                                                      \(17\)
                                                                                                                                                                                           $\leq$   $\frac{N}{K}\hspace{0pt}{\|{L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}^{- 1}}\|}_{2}\hspace{0pt}{\|{L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}^{- 1}}\|}_{2}\hspace{0pt}{\|{{L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}} - {L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}}}\|}_{2}\hspace{0pt}{\|\overline{\omega}\|}_{2}$                                                                                                                                                                          
                                                                                                                                                                                           $\leq$   $\frac{N}{K}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}})}}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}})}}\hspace{0pt}{\|{V^{T}\hspace{0pt}B\hspace{0pt}{({{W\hspace{0pt}{({\overline{\theta}}_{1})}} - {W\hspace{0pt}{({\overline{\theta}}_{2})}}})}\hspace{0pt}B^{T}\hspace{0pt}V}\|}_{2}\hspace{0pt}{\|\omega\|}_{2}$                             
                                                                                                                                                                                           $\leq$   $\frac{N}{K}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}})}}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}})}}\hspace{0pt}{\|{V^{T}\hspace{0pt}B}\|}_{2}\hspace{0pt}{\|{{W\hspace{0pt}{({\overline{\theta}}_{1})}} - {W\hspace{0pt}{({\overline{\theta}}_{2})}}}\|}_{\infty}\hspace{0pt}{\|{B^{T}\hspace{0pt}V}\|}_{2}\hspace{0pt}{\|\omega\|}_{2}$      
                                                                                                                                                                                           $\leq$   $\frac{N}{K}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}})}}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}})}}\hspace{0pt}\lambda_{\max}\hspace{0pt}{(L)}\hspace{0pt}{\|{{W\hspace{0pt}{({\overline{\theta}}_{1})}} - {W\hspace{0pt}{({\overline{\theta}}_{2})}}}\|}_{\infty}\hspace{0pt}{\|\omega\|}_{2}$                                               
                                                                                                                                                                                           $\leq$   $\frac{N}{K}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}})}}\hspace{0pt}\frac{1}{\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}})}}\hspace{0pt}\lambda_{\max}\hspace{0pt}{(L)}\hspace{0pt}\alpha_{s}\hspace{0pt}{\| B^{T}\|}_{\infty}\hspace{0pt}{\|{{\overline{\theta}}_{1} - {\overline{\theta}}_{2}}\|}_{\infty}\hspace{0pt}{\|\omega\|}_{2}$                              
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

$\alpha_{s}$ is the Lipschitz constant of $sinc{(.)}$ which is $0.5$. For a weighted graph with non-negative weights $W = {\lbrack w_{i\hspace{0pt}j}\rbrack}$, the second smallest non-zero eigenvalue is given by  \[3\]

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------
     $${\lambda_{m\hspace{0pt}i\hspace{0pt}n}\hspace{0pt}{({L_{W}\hspace{0pt}{(\overline{\theta})}})}} = {\lambda_{2}\hspace{0pt}{({L_{W}\hspace{0pt}{(\theta)}})}} = {{({N - 1})}\hspace{0pt}{\inf\limits_{f \perp {D\hspace{0pt}\mathbf{1}}}\frac{\sum_{i \sim j}{{({f_{i} - f_{j}})}^{2}\hspace{0pt}w_{i\hspace{0pt}j}}}{\sum_{v}{f_{i}^{2}\hspace{0pt}d_{i}}}}}$$      \(18\)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------

with $d_{i} = {\sum_{j}w_{i\hspace{0pt}j}}$ and $D$ denotes the diagonal matrix with the $(i,i)$-th entry having value $d_{i}$. Since ${B^{T}\hspace{0pt}\theta} \in {({- \frac{\pi}{2}},\frac{\pi}{2})}^{e}$ ,we have $\frac{2}{\pi} \leq w_{i\hspace{0pt}j} \leq 1$. Therefore,

  -- ----------------------------------------------------------------------------------------------------------------------------- -- --------
     $${\lambda_{2}\hspace{0pt}{({L_{W}\hspace{0pt}{(\theta)}})}} \geq {\frac{2}{\pi}\hspace{0pt}\lambda_{2}\hspace{0pt}{(L)}}$$      \(19\)
  -- ----------------------------------------------------------------------------------------------------------------------------- -- --------

Applying (19) to (17), we get

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------
     ${\|{\frac{N}{K}\hspace{0pt}{({{L_{W}\hspace{0pt}{({\overline{\theta}}_{1})}^{- 1}} - {L_{W}\hspace{0pt}{({\overline{\theta}}_{2})}^{- 1}}})}\hspace{0pt}\overline{\omega}}\|}_{2} \leq {\frac{N}{K}\hspace{0pt}{(\frac{\pi}{2})}^{2}\hspace{0pt}\frac{\lambda_{N}\hspace{0pt}{(L)}}{\lambda_{2}\hspace{0pt}{(L)}^{2}}\hspace{0pt}{\|{{\overline{\theta}}_{1} - {\overline{\theta}}_{2}}\|}_{\infty}\hspace{0pt}{\|\omega\|}_{2}}$      \(20\)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------

From here, we can find value of $K$'s that make this mapping contractive as follows

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${\frac{N}{K}\hspace{0pt}{(\frac{\pi}{2})}^{2}\hspace{0pt}\frac{\lambda_{N}\hspace{0pt}{(L)}}{\lambda_{2}\hspace{0pt}{(L)}^{2}}\hspace{0pt}{\|\omega\|}_{2}} < 1$$      \(21\)
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

or

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$K > {{(\frac{\pi}{2})}^{2}\hspace{0pt}\frac{N\hspace{0pt}\lambda_{N}\hspace{0pt}{(L)}}{\lambda_{2}\hspace{0pt}{(L)}^{2}}\hspace{0pt}{\|\omega\|}_{2}}$$      \(22\)
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

As a result for $K > K_{c}$, where $K_{c} = {{(\frac{\pi}{2})}^{2}\hspace{0pt}\frac{N\hspace{0pt}\lambda_{N}\hspace{0pt}{(L)}}{\lambda_{2}\hspace{0pt}{(L)}^{2}}\hspace{0pt}{\|\omega\|}_{2}}$, the fixed-point equation (15) has a unique and stable solution. $\square$

## 8 Concluding remarks 

In this paper we provided a stability analysis for the Kuramoto model of coupled nonlinear oscillators for arbitrary topology. We showed that when the oscillators are identical, there are at least two Lyapunov functions which prove asymptotic stability of the synchronized state, when all the phase differences are bounded by $\frac{\pi}{2}$. We also showed that when the natural frequencies are not the same, there is a critical value of the coupling below which a totally synchronized state does not exist. Several bounds for this critical value based on norm bounded uncertain natural frequencies were shown to be in excellent agreement with existing bounds in the physics literature for the case of the all-to-all graph.

We also point out that contrary to the infinite $N$ case, there is no partially synchronized state, i.e., for values of the coupling below the critical value, the system of differential equations has a running solution. Furthermore, we showed that there is always a large enough but finite value of the coupling which results in synchronization of oscillators and convergence of the angles to a unique fixed-point. Another result of this paper is that the value of the order parameter is not zero for the critical coupling $K_{L}$. In fact, at least when the fixed-point is in the $({- {\pi/2}},{\pi/2})$ region, a rough estimate indicates that the value of $r$ is bounded between $\frac{\sqrt{16 - \pi^{2}}}{4} \approx 0.62$ and $\frac{\sqrt{3}}{2}.$ Future research in this direction is needed to determine the bound for $K$ when the natural frequencies are not just norm bounded quantities but uncertain numbers chosen from a probability distribution. Finally we mention that our value for the upper bound of the order parameter is actually quite close to simulations.

Our work hints at the advantageous marriage of systems and control theory and graph theory, when studying dynamical systems over or on networks \[1\].

## 9 Acknowledgements 

We would like to thank Steve Strogatz, Naomi Leonard, George Pappas and Bert Tanner for their helpful comments.

## References 

-   [\[1\] M. Barahona and L.M. Pecora. Synchronization in small-world systems. Phys. Rev. Lett., 89(5):0541011--4, 2002.]
-   [\[2\] Grace E. Cho and Carl D. Meyer. Comparison of perturbation bounds for the stationary distribution of a Markov chain. Linear Algebra and its Applications, 335(1--3):137--150, 2001.]
-   [\[3\] F. Chung. Spectral graph theory. American Mathematical Society, 1997.]
-   [\[4\] C. Godsil and G. Royle. Algebraic Graph Theory. Springer Graduate Texts in Mathematics \# 207, New York, 2001.]
-   [\[5\] J. L. Van Hemmen and W. F. Wreszinski. Lyapunov function for the kuramoto model of nonlinearly coupled oscillators. Journal of Statistical Physics, 72:145--166, 1993.]
-   [\[6\] A. Jadbabaie, J. Lin, and A. S. Morse. Coordination of groups of mobile autonomous agents using nearest neighbor rules. IEEE Transactions on Automatic Control, 48(6):988--1001, June 2003.]
-   [\[7\] E.W. Justh and P.S. Krishnaprasad. A simple control law for UAV formation flying. Technical Report 2002-38, Institute for Systems Research, 2002.]
-   [\[8\] Y. Kuramoto. In International Symposium on Mathematical Problems in Theoretical Physics, volume 39 of Lecture Notes in Physics, page 420. Springer, New York, 1975.]
-   [\[9\] Y. Kuramoto. Chemical Oscillations, Waves, and Turbulence. Springer, Berlin, 1984.]
-   [\[10\] N. Leonard. Personal communications.]
-   [\[11\] D. J. Low. Following the crowd. Nature, 407:465--466, 2000.]
-   [\[12\] L. Mureau. Leaderless coordination via bidirectional and unidirectional time-dependent communication. Submitted to IEEE Transactions on Automatic Control, 2003.]
-   [\[13\] R. Olfati-Saber and R. M. Murray. Consensus problems in networks of agents with switching topology and time-delays. IEEE Transactions on Automatic Control, submitted, 2003.]
-   [\[14\] R. Olfati Saber and R. M. Murray. Consensus protocols for networks of dynamic agents. In Proceedings of the American Control Conference, Denver, CO, 2003.]
-   [\[15\] S. H. Strogatz. From Kuramoto to Crawford: exploring the onset of synchronization in population sof coupled nonlinear oscillators. Physica D, 143:1--20, 2000.]
-   [\[16\] S.H. Strogatz. Norbert Wiener's brain waves. In Frontiers in Mathematical Biology, volume 100 of Lecture Notes in Biomathematics, page 122. Springer, New York, 1994.]
-   [\[17\] Steven Strogatz. SYNC: The Emerging Science of Spontaneous Order. Hyperion Press, New York, 2003.]
-   [\[18\] Herbert G. Tanner, Ali Jadbabaie, and George J. Pappas. Stable flocking of mobile agents, Part I: Fixed topology. In Proceedings of the IEEE Conference on Decision and Control, 2003. (to appear).]
-   [\[19\] Herbert G. Tanner, Ali Jadbabaie, and George J. Pappas. Stable flocking of mobile agents, Part II: Dynamic topology. In Proceedings of the IEEE Conference on Decision and Control, 2003. (to appear).]
-   [\[20\] T. Vicsek. A question of scale. Nature, 411:421, May 24 2001.]
-   [\[21\] T. Vicsek, A. Czirok, E. Ben Jacob, I. Cohen, and O. Schochet. Novel type of phase transitions in a system of self-driven particles. Physical Review Letters, 75:1226--1229, 1995.]
-   [\[22\] W. Wang and J. J. E. Slotine. On partial contraction analysis for couplled nonlinear oscillators. technical Report, Nonlinear Systems Laboratory, MIT, 2003.]
-   [\[23\] Shynia Watanabe and Steven H. Strogatz. Constants of motion for superconducting josephson arrays. Physica D, 74:197--253, 1994.]
-   [\[24\] N. Wiener. Nonlinear Problems in Random Theory. MIT Press, Cambridge, MA, 1958.]
-   [\[25\] A.T. Winfree. The Geometry of Biological Time. Springer, New York, 1980.]
