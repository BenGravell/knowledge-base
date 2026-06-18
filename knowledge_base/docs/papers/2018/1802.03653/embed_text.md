## Introduction

Optimization theory has played an increasingly central role in the development of machine learning in recent years. This has happened not only because optimization theory supplies algorithms and convergence rates for learning algorithms, but also because it supplies lower bounds, and hence fundamental understanding. A milestone in this regard was the discovery by Nemirovskii & Yudin of oracle lower bounds for gradient-based optimization, and the ensuing derivation by Nesterov of an "accelerated gradient descent" (AGD) algorithm whose rate is provably better than that of gradient descent, and which matches the oracle lower bound.

A flurry of mathematical and algorithmic results have followed in the wake of these seminal discoveries from the 1980's, but even after three decades there remains a lack of understanding of the general acceleration phenomenon. In particular, a theoretical framework that can *generate* accelerated methods has not yet emerged. Recent progress in this regard has been achieved by considering continuous-time analogs of acceleration methods. Notably, Wibisono et al. presented a variational framework, involving a "Bregman Lagrangian," that generates differential equations with rates that are continuous-time analogs of the discrete-time oracle rates.

The work of Wibisono et al., however, only partially addresses the problem of providing a generative framework for acceleration. They show that any desired rate can be achieved in continuous time---different algorithms follow the same *path* in phase space while doing so at different *speeds*, and that the speed can be arbitrarily fast. Differences in speed thus correspond to a mere change of the clock by which time is measured. The fact that lower bounds for rates emerge in discrete time must therefore have something to do with the discretization of the class of differential equations arising from the Bregman Lagrangian. Wibisono et al. were able to provide an adhoc discretization that yielded an algorithm whose rate matches the rate of Nesterov acceleration in a particular setting, but their framework is silent on a general methodology for providing such discretizations.

The class of differential equations arising from the Bregman Lagrangian must be special in some sense, given that they deliver continuous-time analogs of oracle rates. The notion that certain differential equations are special has a long history in physics, where underlying Lagrangians and Hamiltonians possess certain mathematical symmetries that yield conservation laws for the resulting differential equations. Moreover, the venerable field of symplectic integration shows that it is possible to preserve these conservation laws when discretizing the differential equations. The resulting integrators improve upon classical integrators, e.g., Euler, Runge-Kutta, precisely because they respect the underlying mathematical symmetries. This results in certain error terms canceling, with a variety of favorable consequences, including long-term stability. Of particular relevance to the current setting, the stability of such integrators means that it is possible to take much larger step sizes than with classical integrators. Given that we are interested in "accelerated" methods that arrive at an optimum as quickly as possibly, this feature of symplectic integration seems directly relevant.

In the current paper we show how to apply symplectic integration to gradient-based optimization. Our approach is cast in a Hamiltonian framework, obtained from the Bregman-Lagrangian framework via a Legendre transformation. This Hamiltonian is time-varying, a fact that we address via a lifting procedure. We then show how to derive a symplectic integrator from the lifted Hamiltonian. The end result is a fully generative mathematical pipeline, from problem specification to discrete-time accelerated algorithm. Our algorithms are related to Nesterov's algorithms, but they are *not* exactly the same, and the differences are interesting.

## Bregman Dynamics for Optimization

We begin with a brief review of the dynamical framework introduced in Wibisono et al., including the heuristic discretization that those authors employed to obtain accelerated discrete-time optimization algorithms.

Consider a Euclidean vector space, $\mathcal{X}$, which we will denote as the *configuration manifold*. This configuration manifold is equipped with the Euclidean gradient operator, $\nabla$, and inner product, $\left\langle, \right\rangle$. Formally we should be careful to distinguish between points, vectors, and covectors on the configuration manifold but we will reserve that level of rigor for a more formal geometric treatment presented in Appendix A.

Given a smooth *objective function* on the configuration manifold, $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$, the optimization problem is then to compute minima of $f$:

In accordance with most of the theoretical literature on acceleration, we will focus on the setting in which $f$ is convex and exhibits a single minimum. But it is worth emphasizing that convexity is not needed in our construction of the Hamiltonian nor for the symplectic integrators. Note, moreover, that there is a growing literature on acceleration in the non-convex setting, where the dynamical systems perspective presented here is also proving to be useful; see, e.g., Jin et al..

From a dynamical perspective, the objective function naturally plays the role of a potential energy, with the minimum at the basin of that potential. If we want to generate dynamics that might settle into this basin, however, then we need to consider not the configuration manifold but rather its *tangent bundle*, $T\mathcal{X}$, consisting of points in $\mathcal{X}$ paired with tangent vectors or *velocities*. In particular, we need to complement the potential energy with a kinetic energy function on the tangent bundle.

Following Wibisono et al. we construct a kinetic energy from an auxiliary smooth function, $h:{\mathcal{X}\rightarrow{\mathbb{R}}}$, and its associated *Bregman divergence*, ${D_{h}{(y,x)}} = {{h{(y)}} - {h{(x)}} - \left\langle {{\nabla h}{(x)}},{y - x} \right\rangle}$. For any given point in the tangent bundle, ${(x,v)} \in {T\mathcal{X}}$, we can translate the base point, $x$, in the direction of the velocity, $v$, to give the new point $x^{\prime} = {x + {e^{- {\alpha{(t)}}}v}}$, for a scaling function $\alpha{(t)}$. The divergence between these two points defines the *Bregman kinetic energy*:

This kinetic energy admits the evocative interpretation as a comparison of how $h$ changes under a finite translation:

versus a scaled infinitesimal translation:

Defining a time-dependent potential energy,

we can then construct the *Bregman Lagrangian* as:

From the Bregman Lagrangian we obtain a variational problem on the tangent bundle whose solutions yield smooth trajectories via the ordinary differential equations

The time dependence of the Lagrangian allows the dynamics to rapidly converge to a minimum, as opposed to dynamics obtained from a time-independent Lagrangian which would oscillate around the desired minimum.

Wibisono et al. also defined the following *ideal scaling conditions*:

for ${p,C} \in {\mathbb{R}}^{+}$, and demonstrated that if $f$ and $h$ are sufficiently well behaved then the Bregman dynamics will provably converge to the minimum of $f$ at the polynomial rate, $\mathcal{O}{({1/t^{p}})}$. This captures not only classical Nesterov acceleration, with its rate of $\mathcal{O}{({1/t^{2}})}$, but also higher-order accelerated algorithms for which $p > 2$.

Unfortunately it is not obvious how to discretize these continuous dynamics to obtain a discrete-time algorithm. Wibisono et al. found that simple discretizations yield algorithms that do not not recover accelerated Nesterov methods and can even be unstable. Ultimately they were able to find a stable discretization that yielded the oracle rates. Their discretization was a sophisticated but heuristic discretization, coupling a Crank-Nicolson discretization of the position updates and a backwards Euler discretization of the velocity updates with a third implicit sequence of intermediate positions, $(y_{n})$:

Here $f_{p - 1}{(y;x_{n})}$ is the order-$p$ Taylor expansion of the objective function around $x_{n}$. This third sequence proved to be the key, stabilizing the discretization and preserving the convergence rates of the continuous-time dynamics. This discretization was obtained by analogy with Nesterov's classical updates, and in this paper we will refer to these discretizations as *generalized Nesterov discretizations*.

## Simulating Bregman Dynamics with Symplectic Integrators

The difficulties associated with discretizing Lagrangian dynamics are well known in the mathematical literature. Discretizations of Lagrangian dynamics are often fragile, especially when the dimension of the configuration space is large. Even high-order discretizations can diverge after short integration times. Ultimately this is because any discretization of dynamics on the tangent bundle does not preserve the continuous symmetries of the dynamical system that stabilize the exact dynamics.

Fortunately we can readily construct a discretization that *does* preserve the necessary symmetries, by exploiting the dual *Hamiltonian* representation of the Bregman dynamics. The Hamiltonian system is the Legendre transform of the Lagrangian system, trading velocities, $v$, and the tangent bundle, $T\mathcal{X}$, for dual *momenta*, $r$, and the *cotangent bundle*.

In this section we will first construct the Hamiltonian representation of the Bregman dynamics and then modify that system to circumvent the explicit time dependence and admit the application of symplectic integrators.

### The Bregman Hamiltonian

To build up the Bregman Hamiltonian from the Bregman Lagrangian we first have to relate define momenta as the derivative of the Lagrangian with respect to the velocities,

Given the Legendre conjugate of $h$,

we can invert this relationship to give

We are now in position to construct the *Bregman Hamiltonian*:

The Bregman dynamics can then be generated from the Bregman Hamiltonian by integrating *Hamilton's equations*:

When the Hamiltonian does not explicitly depend on time the dynamics are said to be *autonomous* and there are standard methods for constructing symplectic integrators that preserve the critical symmetries that stabilize the dynamics. These integrators are extremely accurate, defining discretized dynamics that mirror the exact dynamics even for long integration times and high-dimensional configuration spaces.

Unfortunately the explicit time dependence that allows the dynamics to converge to the minimum of the objective also renders the Bregman Hamiltonian *non-autonomous*. Fortunately this problem can be circumvented. As we show in the next section, by introducing a few more auxiliary variables we can lift the non-autonomous Bregman Hamiltonian system into an autonomous, *extended* Hamiltonian system where symplectic integrators are immediately applicable.

### Making the non-autonomous autonomous

For an autonomous dynamical system time is simply a parameterization of motion along a dynamical trajectory. In particular, we can utilize uniform time increments to facilitate stable discretization of those dynamics. When the trajectories themselves explicitly depend on time, however, stable discretizations become all the more challenging. In order to overcome this difficulty we need to decouple the two responsibilities of time in a dynamical system by incorporating the explicit time into the configuration space and introducing a new effective time to parameterize motion along the dynamical trajectories.

The explicit time, $t$, serves as a new position in the extended configuration space, ${(x,t)} \in \Xi$. The extended cotangent bundle then includes a conjugate energy, ${(x,t,r,\mathcal{E})} \in {T^{\ast}\Xi}$. We then define the extended Hamiltonian as

Here the conjugate energy $\mathcal{E}$ must compensate for the time dependence of the original Hamiltonian to ensure that the extended Hamiltonian, $H_{\Xi}$, is constant along dynamical trajectories.

The corresponding equations of motion for the extended Hamiltonian system become

which introduces the effective time, $\tau$, to parameterize the motion along the extended dynamical trajectories. These dynamics projected back down to the original cotangent bundle yield the original Bregman dynamics, but by separating the time dependence of the dynamics from the parameterization of the trajectories these extended dynamics are manifestly autonomous. In particular, we can immediately apply symplectic integrators to the extended Hamiltonian system.

### Building an extended leapfrog integrator

We are now in a position to build a symplectic integrator to simulate the Bregman dynamics. There is a rich literature on symplectic integrators and their exceptional performance, so here we will limit our discussion to the construction and behavior of a simple *leapfrog integrator* for our extended Hamiltonian system. Despite the simplicity of this integrator, we will see in Section 4 that it rivals the performance of the generalized Nesterov discretization.

Symplectic integrators are naturally constructed by splitting the Hamiltonian into component Hamiltonians whose dynamics can be solved exactly, or at least sufficiently close to exactly numerically, and then composing those dynamics together symmetrically. For example, consider the splitting

These three component Hamiltonians generate dynamics in the extended cotangent bundle with the six vector fields,

Regardless of the nature of $h$, the vector fields ${\overset{\rightarrow}{H}}_{A}$, ${\overset{\rightarrow}{H}}_{B2}$, ${\overset{\rightarrow}{H}}_{C1}$, and ${\overset{\rightarrow}{H}}_{C2}$ will always be trivial and hence their evolution can be solved exactly. For example,

On the other hand the component dynamics of ${\overset{\rightarrow}{H}}_{B1}$ and ${\overset{\rightarrow}{H}}_{B3}$ may or may not be trivial, depending on the choice of $h$. Even if they are nonlinear, however, they can be solved implicitly using, for example, fixed-point iterations.

We can now build a symplectic integrator by composing these component dynamics together to approximate the full dynamics. Here we will consider a symmetric *leapfrog* composition,

Applying the Baker-Campell-Hausdorff equation to this composite operator demonstrates that the symmetry of the composition ensures the cancellation of all terms linear and quadratic in the step size, leaving

If we apply the composite operator for $N = {T/\epsilon}$ steps we then we can approximate the evolution of the exact dynamics for time $T$ with error only quadratic in the step size:

Because each component operator exactly solves a dynamical system, their solutions preserve the dynamical symmetries that maintain stable evolution. Moreover, the symmetric composition of these component dynamics yields an approximate dynamics that very accurately tracks the dynamics of the extended Hamiltonian system even for long integration times, at least if the step size is small enough that the expansion converges. Although the approximate dynamics of a symplectic integrator will diverge if the step size is too large, the inherent stability of this approximation admits much larger step sizes, and hence reduced computation, than other discretizations of the dynamics.

This symmetric leapfrog integrator enjoys a global error quadratic in the step size and consequently it is classified as a second-order integrator. Higher-order integrators can just as easily be built up by applying each component operator multiple times in careful arrangements to cancel more and more error terms.

## Experiments

To explore the performance of symplectic optimization numerically, we consider a relatively simple experiment. Let $\mathcal{X}$ be a 50-dimensional Euclidean space equipped with the quadratic objective function

and $\rho = 0.9$ to correlate the objective.

Let the auxiliary function, $h$, also be quadratic but without any interactions among the coordinates,

The Bregman Hamiltonian becomes

and the component vector fields of the extended dynamics take the form

In this case each of these vector fields are trivial and hence can be integrated exactly.

Finally we adopt the ideal scaling conditions for ${\alpha{(t)}},{\beta{(t)}}$ and $\gamma{(t)}$ discussed in Section 2, in which case the vector fields become

Applying these component dynamics to the second-order leapfrog integrator introduced in Section 3.3 then gives the symmetric update sequence

For comparison we implement the three-step dynamical Nesterov discretization derived in Wibisono et al.. Given the ideal scaling conditions and the quadratic auxiliary function, $h$, this algorithm is given by

For both the extended Hamiltonian system and the Nesterov sequence we take $\epsilon = 0.1$, $p = 2$, $C = 0.0625$, and $N = 2$.

Results of this experiment are shown in Figure 1a. We see that the initial convergence rate obtained by symplectic integration and the three-step generalized Nesterov discretization are both roughly $\mathcal{O}{(t^{- 2.95})}$ for this problem. This should be no surprise, given that both approaches are stable discretizations of the same underlying Bregman dynamics. The number of iterations to arrive near the optimum is accordingly similar for the two algorithms for large values of the error criterion. It is smaller for the Nesterov discretization in the case of smaller error values. We return to this phenomenon---the increasing rate of the Nesterov discretization as it approaches the optimum---in the following section.

It is important to emphasize that the number of iterations is not the same as wall-clock time. Indeed, the leapfrog integrator that drives our implementation of symplectic optimization requires only a single gradient evaluation per iteration while the three-step generalized Nesterov discretization requires two to achieve stability. Consequently, as shown in Figure 1b, once we normalize for computational cost the symplectic integrator becomes twice as effective for large values of the error criterion. Whether this improvement persists in comparison to two-step Nesterov algorithms is an open question.

Figure 1: (a) When appropriately tuned, both symplectic optimization and the dynamic Nesterov discretization simulate the same latent Bregman dynamics and hence achieve similar convergence rates, here approximately 𝒪 (t−2.95). (b) The symplectic optimization, however, requires only half of the computational effort of the three-step generalized Nesterov discretization. (c) Moreover, the inherent stability of the symplectic optimization admits larger discretization step sizes and even higher performance improvements.

It is also important to emphasize that with the leapfrog integrator we are able to choose larger step sizes than with the three-step Nesterov discretization. This is due to the inherent stability of symplectic integration. In particular, as shown in Figure 1c, if we increase the step size to $\epsilon = 0.25$ we see that the Nesterov discretization quickly diverges while the leapfrog integrator remains stable. The time to arrive near the optimum decreases uniformly for the leapfrog integrator for this larger value of the step size.

## Achieving Exponential Convergence with a Gradient Flow

As we have seen in Figure 1, the three-step generalized Nesterov discretization exhibits a unique behavior once it has become sufficiently close to the minimum. In that neighborhood the dynamical Nesterov discretization transitions into an exponential rate of convergence towards the minimum and soon surpasses the symplectic optimizer. Interestingly, we have found that this behavior does not persist for a quartic objective function, ${f{(x)}} = \left\langle x,x \right\rangle^{2}$, suggesting that it requires strong convexity of the neighborhood of the objective. Exponential convergence of the generalized Nesterov discretization in regions of strong convexity of the objective was considered in Wibisono et al..

Because this phase of exponential convergence does not appear in symplectic optimization it cannot be a feature of the Bregman dynamics themselves. Instead it must be a side effect of the heuristic discretization of the generalized Nesterov discretization, which introduced the auxiliary sequence,

or, for the conditions of Section 4,

For these conditions this sequence actually simulates a gradient flow on the configuration manifold, and consequently its addition interweaves the Bregman dynamics with a gradient flow. The exact nature of this interweaving, however, seems to ensure that the two evolutions characterize the dynamic Nesterov discretization in different regimes. Away from the minimum of the objective the Bregman dynamics dominate, rapidly pulling the system towards the minimum. Asymptotically, however, the dynamics dampen and eventually the gradient flow becomes dominant.

For sufficiently well-behaved objectives the emergence of the gradient flow allows admits the exponential convergence seen in the quadratic objective of Section 4. The gradient flow not only not only stabilizes the dynamic Nesterov discretization, it can also provide for even faster convergence near the minimum of the objective!

Although symplectic optimization doesn't need a gradient flow for stability, it could possibly benefit from the potentially exponential convergence it admits. Fortunately, incorporating a gradient flow into a symplectic integrator is straightforward---instead of trying to approximate the evolution operator $\exp\left( {\epsilon{\overset{\rightarrow}{H}}_{\Xi}} \right)$ we instead try to approximate

is the gradient field generating the gradient flow. Provided that we construct an appropriate symmetric splitting then the resulting integrator will enjoy the same global error as a symplectic integrator applied to the extended Hamiltonian system.

For the leapfrog integrator we constructed in Section 3.3 all we have to do is add ${\overset{\rightarrow}{X}}_{GF}$ to the central operator, replacing $\exp{({\epsilon{({\overset{\rightarrow}{H}}_{B3})}})}$ with $\exp{({\epsilon{({{\overset{\rightarrow}{H}}_{B3} + {\overset{\rightarrow}{H}}_{GF}})}})}$. Although this combined evolution operator is technically nonlinear and requires an implicit solution, here we will approximate the evolution with the explicit update,

In the quadratic case where the dynamic Nesterov discretization exhibited exponential convergence, this modification of symplectic optimization exhibits the same advantageous behavior (Figure 2a). Moreover, the modified symplectic optimization maintains its superior stability, still allowing for larger step sizes and faster practical convergence (Figure 2b).

Figure 2: (a) By incorporating gradient flow into the leapfrog integration of the Bregman Hamiltonian dynamics we recover the same asymptotic exponential convergence near the minimum of the objective exhibited by the generalized Nesterov discretization. (b) These modified Hamiltonian dynamics remain stable even as we increase the step size, allowing for more efficient computation without compromising the advantageous asymptotic behavior.

Still, while the global error scaling is preserved under the addition of the gradient flow and the modified Hamiltonian optimization works well empirically, we cannot always expect the same stability with the gradient flow. The problem is that gradient flow cannot be generated from a Hamiltonian and hence the modified discretized evolution cannot preserve the symmetries of the underlying dynamics. In practice we have to be careful to tune the gradient flow so that it its contributions, including any violations of the dynamical symmetries, are negligible until the Hamiltonian dynamics have converged close to the minimum of the objective.

## Discussion

Wibisono et al. introduced a dynamical system that converged to the minimum of a given objective function at the same rate as accelerated Nesterov methods. Moreover, by carefully discretizing the Lagrangian representation of these dynamics they were able to explicitly derive entire families of known accelerated Nesterov discretizations. Given the dynamical system itself, however, discretization is more systematically achieved by considering the Hamiltonian view of the system and appealing to symplectic integrators.

In particular, this systematic approach allows us to isolate the effects of the dynamics from other modifications, such as the gradient flow added to stabilize the original discretization of the Lagrangian representation of the dynamics. This separation then allows us to analyze the performance of the latent Bregman dynamics and that of any amendments independently.

This then positions us to study the general nature and optimality of the Bregman dynamics themselves. This study may not even be limited to Euclidean configuration spaces but perhaps also any manifold in a single unified setting. We discuss details of the systematically geometric construction of the Bregman dynamics and possible generalizations in Appendix A.

This systematic foundation may also allow us to formalize many of the empirical behaviors exhibited by Nesterov methods. For example, the folk wisdom is that Nesterov methods do not perform particularly well when the objective is stochastic. This behavior, however, is not particularly surprising given the nature of symplectic integrators. As discussed in Betancourt, the stochastic variations in the objective introduces a bias into symplectic integrators that corrupts their accuracy by pushing the numerical approximations away from the true dynamics. Intuitively the dynamical evolution moves so quickly that the variation in the stochastic objective doesn't have sufficient time to average out, unlike slower methods such as such as Robbins-Monro that do work well with stochastic objectives. On the other hand, the time dependence of the Bregman dynamics may provide a way of compensating for this bias. Only with a formal understanding of the Bregman dynamics afforded by this new perspective will be able to identify the necessary structure.

Unfortunately, the introduction of Hamiltonian symplectic integrators also complicates the formal analysis of Hamiltonian optimization itself. For example, the accuracy of leapfrog integrators comes from cancellations in their symmetric updates, but any individual update can have large error. Hence we cannot expect to be able to bound convergence term-by-term. Indeed the stability of symplectic integrators is a global property---the discretized dynamics oscillate around the true dynamics and discrete updates will in general deviate away from the exact dynamics before finally returning. To understand the convergence of the discretized dynamics we instead have to take non-local and topological considerations into account, as is done in *backwards error analysis*.

Ultimately, however, the direct window into Bregman dynamics provided by their Hamiltonian representation and corresponding symplectic integration enables not only a better understanding of existing accelerated Nesterov methods but also a principled way of developing new implementations and generalizations.
