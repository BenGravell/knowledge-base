<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Stability of the Kuramoto Model of Coupled Nonlinear Oscillators

Topics include Kuramoto model, Synchronization, Spectral graph theory, Oscillator networks, Nonlinear systems, Local stability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends Kuramoto synchronization analysis beyond identical all-to-all oscillator networks to arbitrary graph topologies with uncertain natural frequencies. The paper connects coupling thresholds and local stability to spectral graph quantities, making the model useful for networked control analysis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an analysis of the classic Kuramoto model of coupled nonlinear oscillators that goes beyond the existing results for all-to-all networks of identical oscillators. Our work is applicable to oscillator networks of arbitrary interconnection topology with uncertain natural frequencies. Using tools from spectral graph theory and control theory, we prove that for couplings above a critical value, the synchronized state is locally asymptotically stable, resulting in convergence of all phase differences to a constant value, both in the case of identical natural frequencies as well as uncertain ones. We further explain the behavior of the system as the number of oscillators grows to infinity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

We provide an analysis of the classic Kuramoto model of coupled nonlinear oscillators that goes beyond the existing results for all-to-all networks of identical oscillators. Our work is applicable to oscillator networks of arbitrary interconnection topology with uncertain natural frequencies. Using tools from spectral graph theory and control theory, we prove that for couplings above a critical value, the synchronized state is locally asymptotically stable, resulting in convergence of all phase differences to a constant value, both in the case of identical natural frequencies as well as uncertain ones. We further explain the behavior of the system as the number of oscillators grows to infinity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Model description", "weight": 1.0} -->

The classic Kuramoto model describes the dynamics of a set of $N$ phase oscillators $\theta_{i}$ with natural frequencies $\omega_{i}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Model description", "weight": 1.0} -->

where $K$ is the coupling strength, a key parameter in the problem. One of Kuramoto's results was to show numerically that when the $\omega_{i}$'s are randomly chosen from a Cauchy probability distribution in the infinite $N$ limit, there is a critical value of the coupling above which all phase differences remain constant, i.e., the oscillators synchronize. If we think of the oscillators as points moving on a circle, they would rotate keeping the phase differences constant.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Model description", "weight": 1.0} -->

Clearly, if all the $\omega_{i}$'s are the same then $R = 1$ when all agents are in sync. If the natural frequencies are not identical but the oscillators synchronize, $R$ converges to a constant $R_{\infty} < 1$. On the other hand, when all agents are completely out of phase with respect to each other the value of $R$ remains close to $0$ most of the time. Because it characterizes the dynamical behavior of the system, $R$ is referred to as the order parameter in the physics literature.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Model description", "weight": 1.0} -->

Kuramoto's analysis used simple trigonometry to rewrite the state equation in terms of the order parameter. After switching to a rotating frame, Eq.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Model description", "weight": 1.0} -->

In other words, each phase is modulated by the magnitude $R$ and phase $\psi$ of the average phasor. In physics notation, this constitutes a mean field or "all-to-all" model.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Model description", "weight": 1.0} -->

With some brilliant intuition, Kuramoto showed that for an infinite number of oscillators there is a critical coupling $K_{c}$ below which the oscillators are incoherent (i.e., fully unsynchronized). In addition, there is another critical coupling $K_{L} \geq K_{c}$ above which all oscillators are synchronized. In that regime, the order parameter $R$ grows exponentially in time until it saturates at a value ${R_{\infty}{(K)}} \leq 1$. The branch of $R$ with $K > K_{L}$ is called the fully synchronized state, while $K < K_{c}$ corresponds to the totally unsynchronized state. Kuramoto also calculated analytically the value for $K_{c}$ and $R_{\infty}$ for a few well-known distributions in the case of an infinite number of oscillators connected all-to-all.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model description", "weight": 1.0} -->

Despite its success, several aspects of the well-studied $N\rightarrow\infty$, all-to-all Kuramoto model are still a puzzle, as summarized beautifully in the review by Steve Strogatz. For instance, what does it mean that $R$ stays close to zero in the unsynchronized state $K < K_{c}$? This cannot be true at all times: when $K = 0$ and the $\omega_{i}$'s are irrational with respect to each other, the trajectories are dense on the $N$-torus resulting in an $R$ which will almost surely visit any number between 0 and 1. However, simulations indicate that it is true most of the time. On the other extreme, the case of few oscillators has been tackled in the dynamical systems literature with rigorous bifurcation analysis. However, even basic results are not available for the large but finite $N$ case, which is of utmost interest in systems engineering.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model description", "weight": 1.0} -->

Our goal here is to perform a system theoretic analysis of the finite $N$ case with arbitrary connectivity. To proceed, we rewrite the model in terms of the incidence matrix of the undirected graph that describes the interconnection topology--- the standard all-to-all case is then the specific case of the complete graph. We then provide several necessary as well as sufficient lower bounds for the critical coupling $K_{L}$. These include a bound for $K$ below which there is no fixed-point, and a value of $K$ above which there is a unique fixed-point. This extends similar results in for the case of 2 oscillators with a finite set of values for the natural frequencies.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Graph theoretical formulation of Kuramoto's model", "weight": 1.0} -->

A good source for the necessary graph theory terminology is. We formalize our results through two matrices that encode the topology of the connections. The incidence matrix $B$ of an oriented graph $\mathcal{G}^{\sigma}$ with $N$ vertices and $e$ edges is the $N \times e$ matrix such that: $B_{ij} = 1$ if the edge $j$ is incoming to vertex $i$, $B_{ij} = {- 1}$ if edge $j$ is outcoming from vertex $i$, and $0$ otherwise. The symmetric $N \times N$ matrix defined as: $L = {BB^{T}}$ is called the Laplacian of $\mathcal{G}$ and is independent of the choice of orientation $\sigma$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Graph theoretical formulation of Kuramoto's model", "weight": 1.0} -->

The Laplacian has several important properties: $L$ is always positive semidefinite with a zero eigenvalue; the algebraic multiplicity of its zero eigenvalue is equal to the number of connected components in the graph; the $N$-dimensional eigenvector associated with the zero eigenvalue is the vector of ones, $\mathbf{1}_{N}$. It is known that the spectrum of the Laplacian matrix $\{{\lambda_{i}{(L)}}\}$ captures many topological properties of the graph. Specifically, Fiedler showed that the first non-zero eigenvalue $\lambda_{2}{(L)}$ (sometimes denoted the algebraic connectivity) gives a measure of connectedness of the graph.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Graph theoretical formulation of Kuramoto's model", "weight": 1.0} -->

If we associate a positive number $W_{i}$ to each edge and we form the diagonal matrix $W_{e \times e}:={\text{diag}{(W_{i})}}$, then the matrix ${L_{W}{(\mathcal{G})}} = {BWB^{T}}$ is a weighted Laplacian which fulfills the above properties.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Graph theoretical formulation of Kuramoto's model", "weight": 1.0} -->

where $B$ is the incidence matrix of the unweighted graph, and $\theta$ and $\omega$ are $N \times 1$ vectors. (It is also helpful to define the $e \times 1$ vector of phase differences $\phi:={B^{T}\theta}$.)

<!-- chunk {"id": "body-0017", "role": "body", "section": "Graph theoretical formulation of Kuramoto's model", "weight": 1.0} -->

It is easy to show that when the graph is complete, this is the square of the magnitude of the average phasor, i.e., for $B = B_{c}$, we have $r_{c}^{2} = R^{2}$. While the average phasor interpretation does not generalize to general connected topologies, the above notion of an order parameter does generalize to arbitrary connected graphs. In fact the order parameter can be conveniently written in terms of the Laplacian matrix $L$ of the underlying graph, as a measure of synchrony, or alignment. Specifically, after some algebra, Equation can be written as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Graph theoretical formulation of Kuramoto's model", "weight": 1.0} -->

The above equation provides us with an interesting interpretation of the order parameter: each individual oscillator $i$ can be thought of as a rotor moving on a circle with unit radius, with velocity vector $v_{i} = e^{j\theta_{i}}$. The total measure of disagreement between all velocity vectors, or the global measure of asynchrony can be written as $\sum_{i}{\sum_{j \in \mathcal{N}_{i}}{\|{v_{i} - v_{j}}\|}^{2}}$, which is nothing but $N^{2}{({1 - r^{2}})}$. In other words, the order parameter is a scaled measure of agreement among velocity vectors of rotors, hence a measure of synchronization. This allows us to extend the stability analysis to a graph with arbitrary connected topology.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the limit of small angles, the general Kuramoto model gives the continuous-time Vicsek flocking boid model which was analyzed: ${\overset{˙}{\theta} = {\omega - {{({K/N})}B{\sin{({B^{T}\theta})}}}} \approx {\omega - {{({K/N})}L\theta}}}.$ Conversely, the classic Kuramoto model can be thought of as a nonlinear extension of the Vicsek model for a complete graph.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It is straightforward to show that the analytical simplification (Eq.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Synchronization of identical coupled oscillators", "weight": 1.0} -->

We start by considering the general Kuramoto model in its unperturbed version, i.e.,

<!-- chunk {"id": "body-0022", "role": "body", "section": "Synchronization of identical coupled oscillators", "weight": 1.0} -->

(By switching to a rotating frame, it is easily shown that we can assume that the natural frequencies $\omega_{i}$ are all zero, without loss of generality.)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

Similar results hold even if the topology of the graph changes in time. The result can be extended to general notions of connectivity, i.e., when the interconnection graph is not connected at all times but there is a path between any two nodes over contiguous, non-overlapping, and uniformly bounded time intervals. It is also possible to generalize to the case of directed graphs by introducing notions of weak connectivity.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

The synchronization argument can be readily extended to the case of more complicated coupling functions $f{( \cdot )}$ (other than the $\sin{( \cdot )}$ function) so long as ${\phi^{T}f{(\phi)}} \geq 0$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

The function $\mathbf{1}_{e}^{T}{\cos{({B^{T}\theta})}}$ is an energy function for the XY-model in statistical physics. It was considered as a Lyapunov-like function for the Kuramoto model by Van Hemmen and Wreszinski, as well as.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 4.7", "weight": 1.0} -->

The global results obtained by Watanabe and Strogatz require all-to-all connectivity. An extension of the methodology in to arbitrary topologies does not appear to be trivial.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The case of non-identical oscillators", "weight": 1.0} -->

In the rest of the paper we treat the more complicated case of oscillators with non-identical natural frequencies. Although there is an extensive literature for the $N\rightarrow\infty$ case with all-to-all connectivity, we will focus here on the case of finite $N$ and arbitrary topology given by Eq.. We consider the frequencies to be random perturbations which, albeit drawn from a probability distribution, remain constant in time, i.e., the dynamics is deterministic yet uncertain. This problem is distinct to some treatments in the physics literature, which transform the problem into a Fokker-Planck equation, effectively connected to a stochastic differential equation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The case of non-identical oscillators", "weight": 1.0} -->

Synchronization is best defined in a grounded system, where the phases are defined with respect to a reference variable (or 'ground'). This can be achieved by any projection $V_{N \times {({N - 1})}}$ such that

<!-- chunk {"id": "body-0029", "role": "body", "section": "The case of non-identical oscillators", "weight": 1.0} -->

Thus, $V$ is a matrix of $N - 1$ orthonormal vectors orthogonal to the vector $\mathbf{1}_{N}$ which generate the set of grounded coordinates $\overline{\theta}:={V^{T}\theta}$ and frequencies $\overline{\omega}:={V^{T}\omega}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 5.8", "weight": 1.0} -->

From Eq. it is easy to see why the natural frequencies can be centered around zero without loss of generality. Multiply Eq. from the left by $V$ and use and ${B^{T}\mathbf{1}_{N}} = 0$ to recover the original Eq. with new variables $\Theta = {\theta - {{\lbrack{{\langle\omega\rangle}t}\rbrack}\, 1_{N}}}$ and frequencies $\Omega = {\omega - {{\langle\omega\rangle}\, 1_{N}}}$, where $<\omega>$ is the average frequency.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

Consider a Lyapunov function candidate based on the square of the order parameter $r^{2}$ defined. The derivative of this function along the trajectories is

<!-- chunk {"id": "body-0032", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

which is an ellipsoid in the $\sin{({B^{T}\theta})}$ coordinate centered at $\frac{N\omega}{K}$. Outside of a neighborhood of the origin given by

<!-- chunk {"id": "body-0033", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

the derivative is positive, resulting in growth of the order parameter. The boundary of this region contains the equilibria. By using an ultimate boundedness argument, the trajectories are confined to the smallest sublevel-set of $r$ containing the set defined.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

We now use to obtain an estimate of the asymptotic value of the order parameter. The vector $\sin{({B^{T}\theta})}$ can be decomposed into two orthogonal components: $y_{1}{(\theta)}$, in the null space of $B$, and $y_{2}{(\theta)}$ in the range space of $B^{T}$. The first component is annihilated when it is multiplied by $B$ on the left. As a result, the region over which ${\overset{˙}{r}}^{2}$ is positive can be characterized as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

where $\lambda_{2}{(L)}$ is the algebraic connectivity of the unweighted graph. We now bound the value of $U$ over the region where ${\overset{˙}{r}}^{2}$ is negative. A simple bounding reveals that

<!-- chunk {"id": "body-0036", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

We can immediately observe that the asymptotic behavior of the order parameter is inversely proportional to the algebraic connectivity of the graph. Of course, because of the over-bounding, the bound is conservative---its asymptotic value is 1 as opposed to the actual less-than-one value. Nevertheless, this gives us a bound on the growth rate of $r^{2}$, and, as a result, the growth rate on $r$ is bounded by $\frac{1}{\sqrt{\lambda_{2}{(L)}}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Bound for the asymptotic value of the order parameter", "weight": 1.0} -->

which would result in an increase rate of $\mathcal{O}{(\frac{1}{\sqrt{N}})}$ when the graph is complete.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 6.9", "weight": 1.0} -->

Consider a complete graph where the natural frequencies are independent random variables chosen from a normal distribution $\omega_{i} \sim {\mathcal{N}{(0,\sigma)}}$. Then ${\| w\|}_{2}$ scales as $\sqrt{N}\sigma$, which results in a bound for $r < \sqrt{1 - {({\sigma/K})}^{2}}$ that is independent of $N$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 6.10", "weight": 1.0} -->

In, the authors added a linear term $\omega^{T}\theta$ to the Lyapunov function candidate to guarantee negativity of the derivative everywhere except at the fixed-points, reducing the perturbed model to a gradient system. The linear term, however, makes the Lyapunov function indefinite.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 6.10", "weight": 1.0} -->

We will see in the next section that if $K$ is large enough to guarantee the existence of a unique fixed point (via a contraction argument), condition will be trivially satisfied. This means that if $K$ is large enough the derivative of the order parameter will be positive, resulting in the asymptotic stability of the synchronized state.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Bounds for the critical coupling", "weight": 1.0} -->

As the coupling $K$ is decreased, there is a critical value $K_{L}$ below which no fixed point exists, resulting in a running solution for the grounded system. This means that the system cannot be fully synchronized for $K < K_{L}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Critical value of coupling for complete graphs", "weight": 1.0} -->

Our results generalize those of Van Hemmen et al. in the case of a complete graph. Specifically, it can be shown that the critical value of the coupling is determined by the value of $K$ for which the fixed point disappears. This can be explained by looking at the fixed point equation ${{B{\sin{({B^{T}\theta^{\ast}})}}} = \frac{N\omega}{K}}.$

<!-- chunk {"id": "body-0043", "role": "body", "section": "Critical value of coupling for complete graphs", "weight": 1.0} -->

Let $\omega_{max} = {\|\omega\|}_{\infty}$ and note that the induced infinity norm of a matrix is the maximum absolute row sum, i.e., ${\| B\|}_{\infty} = d_{max}$, where $d_{max}$ is the maximum degree of the graph. In the case of a complete graph, $d_{max} = {N - 1}$. Then,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Critical value of coupling for complete graphs", "weight": 1.0} -->

This bound can be tightened by using the generalized inverse of $V^{T}B$ and bounding the component of the $\sin{({B^{T}\theta})}$ in the range of $B^{T}$. The generalized inverse, denoted by ${({V^{T}B})}^{\#}$, is equal to $B^{T}V\Lambda^{- 1}$, where $\Lambda$ is the $N - 1$ diagonal matrix of the eigenvalues of the unweighted Laplacian. We therefore have the following expression

<!-- chunk {"id": "body-0045", "role": "body", "section": "Critical value of coupling for complete graphs", "weight": 1.0} -->

The generalized inverse of the Laplacian, in the case of a complete graph can be written as $L_{c}^{\#} = {\frac{1}{N}{({I - \frac{\mathbf{1}\mathbf{1}^{\mathbf{T}}}{N}})}}$. Noting that the infinity norm of the $\sin$ vector is less than or equal to 1, and that ${B^{T}L^{\#}B} = \frac{B^{T}B}{N}$, we have

<!-- chunk {"id": "body-0046", "role": "body", "section": "Critical value of coupling for complete graphs", "weight": 1.0} -->

This is in excellent agreement with that of Van Hemmen et al. which they obtained for the simplest case of two oscillators.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 7.11", "weight": 1.0} -->

If the graph is a tree, $V^{T}B$ has full row rank and $\sin{({B\theta})}$ does not have a component in the null space of $L$. In that case $K_{L} > {\|{B^{T}L^{\#}\omega}\|}_{\infty}$ is a tight bound, meaning that it is necessary and sufficient for synchronization. In the general case, however, this bound is just necessary.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Existence and uniqueness of stable fixed points", "weight": 1.0} -->

The fixed point equation can be written as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Existence and uniqueness of stable fixed points", "weight": 1.0} -->

Using Brouwer's fixed point theorem (i.e., a continuous function that maps a non-empty compact, convex set $X$ into itself has at least one fixed-point), we can develop conditions which guarantee the existence (but not uniqueness) of the fixed point. If a fixed-point exists in any compact subset of $\theta \in {({- \frac{\pi}{4}},\frac{\pi}{4})}$, it is stable, since this will ensure that $B^{T}\theta$ is between $- \frac{\pi}{2}$ and $\frac{\pi}{2}$. We therefore have to ensure that

<!-- chunk {"id": "body-0050", "role": "body", "section": "Existence and uniqueness of stable fixed points", "weight": 1.0} -->

Simulations indicate that in the case of a complete graph, the infinity norm of the matrix $L_{W}^{\#}$ scales as $\mathcal{O}{(\frac{1}{N})}$. It is worth mentioning that the norm of $L_{W}^{\#}$ is a well studied object in the theory of Markov chains. The infinity norm of $L_{W}^{\#}$ is a measure of the sensitivity of the stationary distribution of the chain associated with $L$ with respect to additive perturbations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Existence and uniqueness of stable fixed points", "weight": 1.0} -->

If the uncertain natural frequencies are 2-norm bounded, a better strategy would be to impose the boundedness condition with respect to the Euclidean norm. A sufficient condition for local stability of the fixed-point is for $\theta_{i}$ to belong to $({- \frac{\pi}{4}},\frac{\pi}{4})$. This amounts to having the Euclidean norm of $\theta$ be less than $\frac{\pi}{4}\sqrt{N}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Existence and uniqueness of stable fixed points", "weight": 1.0} -->

where we used the fact that ${\|{({BW{({B^{T}\theta})}B})}^{\#}\|}_{2} = \frac{1}{\lambda_{2}{(L_{W})}}$, and $\lambda_{2}$ is the algebraic connectivity of the (weighted) graph. A lower bound on the minimum value of $\lambda_{2}$ occurs for the minimum value of the weight which is $\frac{2}{\pi}$. As a result,

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 7.12", "weight": 1.0} -->

Using the upper bound provided for the order parameter earlier, we can derive an upper bound for the asymptotic value of $r$ at $K_{L}$: ${r_{\infty}{(K_{L})}} \leq \frac{\sqrt{3}}{2}$. Furthermore, if the stable fixed-point is in ${({- {\pi/4}},{\pi/4})}^{N}$, then the order parameter is lower bounded by $\sqrt{16 - \pi^{2}}/4$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Bounds for the existence of a unique fixed-point", "weight": 1.0} -->

In order to guarantee the existence of a unique fixed point we use Banach's contraction principle and ensure that the right hand side is a contraction. By noting that the Lipschitz constant for the ${sinc}{( \cdot )}$ function is $\alpha_{s} = \frac{1}{2}$, we provide a sufficient condition for contractivity (and therefore uniqueness of the fixed-point).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Bounds for the existence of a unique fixed-point", "weight": 1.0} -->

We impose the contractivity condition on the $N - 1$ dimensional grounded system. In the grounded case, we have $\overline{\theta} = {V^{T}\theta}$, and

<!-- chunk {"id": "body-0056", "role": "body", "section": "Bounds for the existence of a unique fixed-point", "weight": 1.0} -->

After some algebra, the contraction requirement amounts to

<!-- chunk {"id": "body-0057", "role": "body", "section": "Bounds for the existence of a unique fixed-point", "weight": 1.0} -->

where $\lambda_{max}$ is the largest eigenvalue of the Laplacian of the graph.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Bounds for the existence of a unique fixed-point", "weight": 1.0} -->

Interestingly, this value of $K$ also ensures that the derivative of $r^{2}$ is increasing,i.e., inequality is satisfied, which means that the order parameter is increasing. Of course this is probably stronger than what is necessary for uniqueness, as the contraction argument is only sufficient. Nevertheless, we see that there is a large enough but finite value of the coupling which guarantees the existence and uniqueness of fixed points.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

In this paper we provided a stability analysis for the Kuramoto model of coupled nonlinear oscillators for arbitrary topology. We showed that when the oscillators are identical, there are at least two Lyapunov functions which prove asymptotic stability of the synchronized state, when all the phase differences are bounded by $\frac{\pi}{2}$. We also showed that when the natural frequencies are not the same, there is a critical value of the coupling below which a totally synchronized state does not exist. Several bounds for this critical value based on norm bounded uncertain natural frequencies were shown to be in excellent agreement with existing bounds in the physics literature for the case of the all-to-all graph.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

We also point out that contrary to the infinite $N$ case, there is no partially synchronized state, i.e., for values of the coupling below the critical value, the system of differential equations has a running solution. Furthermore, we showed that there is always a large enough but finite value of the coupling which results in synchronization of oscillators and convergence of the angles to a unique fixed-point. Another result of this paper is that the value of the order parameter is not zero for the critical coupling $K_{L}$. In fact, at least when the fixed-point is in the $({- {\pi/2}},{\pi/2})$ region, a rough estimate indicates that the value of $r$ is bounded between $\frac{\sqrt{16 - \pi^{2}}}{4} \approx 0.62$ and $\frac{\sqrt{3}}{2}.$ Future research in this direction is needed to determine the bound for $K$ when the natural frequencies are not just norm bounded quantities but uncertain numbers chosen from a probability distribution.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

Finally we mention that our value for the upper bound of the order parameter is actually quite close to simulations.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

Our work hints at the advantageous marriage of systems and control theory and graph theory, when studying dynamical systems over or on networks.
