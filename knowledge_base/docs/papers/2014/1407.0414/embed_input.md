Newton Methods for K-order Markov Constrained Motion Problems

Topics include Robotics, Optimization.

This is a documentation of a framework for robot motion optimization that aims to draw on classical constrained optimization methods. With one exception the underlying algorithms are classical ones: Gauss-Newton (with adaptive step size and damping), Augmented Lagrangian, log-barrier, etc. The exception is a novel any-time version of the Augmented Lagrangian. The contribution of this framework is to frame motion optimization problems in a way that makes the application of these methods efficient, especially by defining a very general class of robot motion problems while at the same time introducing abstractions that directly reflect the API of the source code.

## Introduction

Let $x_{t} \in {\mathbb{R}}^{n}$ be a joint configuration and $x_{0:T} = {(x_{0},\ldots,x_{T})}$ a trajectory of length $T$. Note that troughout this framework we *do not* represent trajectories in the phase space, where the state is $(x_{t},{\overset{˙}{x}}_{t})$---we represent trajectories directly in configuration space. We consider optimization problems of a general "$k$-order non-linear sum-of-squares constrained" form

where $x_{{t - k}:t} = {(x_{t - k},..,x_{t - 1},x_{t})}$ are $k + 1$ tuples of consecutive states. The functions ${f_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{d_{t}}$, ${g_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{m_{t}}$, and ${h_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{l_{t}}$ are arbitrary first-order differentiable non-linear $k$-order vector-valued functions. These define cost terms or inequality/equality constraints for each $t$. Note that the first cost vector $f_{0}{(x_{- k},..,x_{0})}$ depends on states $x_{t}$ with negative $t$. We call these $(x_{- k},..,x_{- 1})$ the *prefix*....

This document by no means aims to document all aspects of the code, esp. those relating to the used kinematics engine etc. It only tries to introduce to the concepts and design decisions behind the KOMO code.

More documentation of optimization and kinematics concepts used in the code can be drawn from my teaching lectures on Optimization and Robotics.

For convenience there is a single high-level method to call the optimization, defined in \<Motion/komo.h\>\

The following definitions also document the API of the code.

The user can define new $k$-order task maps by instantiating the abstraction. There exist a number of predefined task maps. The specification of a task map usually has only a few parameters like "which endeffector shape(s) are you referring to". Typically, a good convention is to define task maps in a way such that *zero* is a desired state or the constraint boundary, such as relative coordinates, alignments or orientation. (But that is not necessary, see the linear transformation below.)

The term $k{(t,t^{\prime})}$ is an optional kernel measuring the (desired) correlation between time steps $t$ and $t^{\prime}$, which we explored but in practice hardly used.

The $k$-order cost vectors ${f_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{d_{t}}$ are very flexible in including various elements that can represent both...
