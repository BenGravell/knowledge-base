Rectified Flow: A Marginal Preserving Approach to Optimal Transport

Topics include Regression, Optimal transport, Flow, Ordinary differential equation, Convex function.

We present a flow-based approach to the optimal transport (OT) problem between two continuous distributions pi_0, pi_1 on R^(d), of minimizing a transport cost E[c(X_1-X_0)] in the set of couplings (X_0, X_1) whose marginal distributions on X_0, X_1 equals pi_0, pi_1, respectively, where c is a cost function. Our method iteratively constructs a sequence of neural ordinary differentiable equations (ODE), each learned by solving a simple unconstrained regression problem, which monotonically reduce the transport cost while automatically preserving the marginal constraints. This yields a monotonic interior approach that traverses inside the set of valid couplings to decrease the transport cost, which distinguishes itself from most existing approaches that enforce the coupling constraints from the outside. The main idea of the method draws from rectified flow, a recent approach that simultaneously decreases the whole family of transport costs induced by convex functions c (and is hence multi-objective in nature), but is not tailored to minimize a specific transport cost.

## Introduction

The

wherewe seek tofind (the law of) an optimal coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$, for which marginal laws of $X_{0},X_{1}$ equal $\pi_{0},\pi_{1}$, respectively, to minimize ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$, called the $c$-transport cost,fora cost function $c$.Theories, algorithms, and applications of optimal transport have attracted a vast literature; see, for example, the monographs of for overviews.

## This work

Our method is made possible by leveraging*rectified flow*,a recent approach to constructing (non-optimal) transport maps for generative modeling and domain transfer.What makes rectified flow specialis that it provides a simple procedurethat turns a given coupling into a new one thatobeys the same marginal laws, while yielding no worse transport cost w.r.t.

## Rectified flow

We provide a high-level overview ofthe rectified flow of and the main results of this work.For

## Discussion and Open Questions

For machine learning (ML) tasks such as generative models and domain transfer, the transport cost is not necessarily the direct object of interest.In these cases,as suggested , rectified flow might be preferred because it is simpler and does not require to specify a particular cost $c$.Question: for such ML tasks, when would it be preferred to use OT with a specific $c$, and how to choose $c$ optimally?

In practice, recursively applying the ($c$-)rectification accumulates errorsbecause the training optimization for the drift field and the simulation of the ODEcan not be conducted perfectly.Howto avoid the error accumulationat each step?Assume ${\{ x_{1,i}\}}_{i} \sim \pi_{1}$, and ${\{ z_{0,i}^{k},z_{1,i}^{k}\}}_{i}$ is obtained by solving the ODE of the $k$-th $c$-rectified flow starting from $z_{0,i}^{k} \sim \pi_{0}$.As we increase $k$, ${\{ z_{0,i}^{k}\}}_{i}$ may yield increasingly bad approximation of $\pi_{1}$ due to the error accumulation.
