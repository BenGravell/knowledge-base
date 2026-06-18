Rectified Flow: A Marginal Preserving Approach to Optimal Transport

Topics include Regression, Optimal transport, Flow, Ordinary differential equation, Convex function.

We present a flow-based approach to the optimal transport (OT) problem between two continuous distributions pi_0, pi_1 on R^(d), of minimizing a transport cost E[c(X_1-X_0)] in the set of couplings (X_0, X_1) whose marginal distributions on X_0, X_1 equals pi_0, pi_1, respectively, where c is a cost function. Our method iteratively constructs a sequence of neural ordinary differentiable equations (ODE), each learned by solving a simple unconstrained regression problem, which monotonically reduce the transport cost while automatically preserving the marginal constraints. This yields a monotonic interior approach that traverses inside the set of valid couplings to decrease the transport cost, which distinguishes itself from most existing approaches that enforce the coupling constraints from the outside. The main idea of the method draws from rectified flow, a recent approach that simultaneously decreases the whole family of transport costs induced by convex functions c (and is hence multi-objective in nature), but is not tailored to minimize a specific transport cost....

## Introduction

The Monge--Kantorovich (MK) optimal transport (OT) problem concerns finding an optimal coupling between two distributions $\pi_{0},\pi_{1}$:

wherewe seek tofind (the law of) an optimal coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$, for which marginal laws of $X_{0},X_{1}$ equal $\pi_{0},\pi_{1}$, respectively, to minimize ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$, called the $c$-transport cost,fora cost function $c$.Theories, algorithms, and applications of optimal transport have attracted a vast literature; see, for example, the monographs of for overviews....

With or without the adjustment step,build a complete theoretical analysis on the statistical error of the method.

In what precise sense is rectified flow solving a multi-objective variant of optimal transport?

This suggests that the marginal law $\rho_{t} ≔ {{Law}{(X_{t})}}$ satisfies

### Lemma 3.3

Under the conditions in Theorem 5.2, we havei) $\mathbf{Z} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{(\mathbf{X})}}$ attains the minimum of.ii) Problem and has a strong duality:

### This work

We present a different approach tocontinuous OTthat re-frames intoa sequence of simple unconstrained nonlinear least squares optimization problems,whichmonotonically reduce the transport cost of a couplingwhile automatically preserving the marginal constraints.Different from theminimax and regularization approaches that enforce the constraints from outside,our method is an *interior* approachwhich starts from a valid coupling (typically the naive independent coupling), and traverses inside the constraint set to decrease the transport cost.Such an interior approach is non-trivial and has not been realized before, because there exists no...

### Rectified flow

We provide a high-level overview ofthe rectified flow of and the main results of this work.For a given coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$,the *rectified flow*induced by $(X_{0},X_{1})$is the time-differentiable process ${\mathbf{Z}} = {\{ Z_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$ over an artificial notion of time $t \in {\lbrack 0,1\rbrack}$,that solves the following ordinary differential equation (ODE):

and $X_{t}$ is the linear interpolation between $X_{0}$ and $X_{1}$.Eq isa least squares regression problem of predicting the line direction of $({X_{1} -...
