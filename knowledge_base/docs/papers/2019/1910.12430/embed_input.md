Differentiable Convex Optimization Layers

Recent work has shown how to embed differentiable optimization problems (that is, problems whose solutions can be backpropagated through) as layers within deep learning architectures. This method provides a useful inductive bias for certain problems, but existing software for differentiable optimization layers is rigid and difficult to apply to new settings. In this paper, we propose an approach to differentiating through disciplined convex programs, a subclass of convex optimization problems used by domain-specific languages (DSLs) for convex optimization. We introduce disciplined parametrized programming, a subset of disciplined convex programming, and we show that every disciplined parametrized program can be represented as the composition of an affine map from parameters to problem data, a solver, and an affine map from the solver's solution to a solution of the original problem (a new form we refer to as affine-solver-affine form). We then demonstrate how to efficiently differentiate through each of these components, allowing for end-to-end analytical differentiation through the entire convex program....

## Introduction

Recent work has shown how to differentiate through specific subclasses of convex optimization problems, which can be viewed as functions mapping problem data to solutions. These layers have found several applications, but many applications remain relatively unexplored (see, e.g., \[4, §8\]).

While convex optimization layers can provide useful inductive bias in end-to-end models, their adoption has been slowed by how difficult they are to use. Existing layers (e.g., ) require users to transform their problems into rigid canonical forms by hand. This process is tedious, error-prone, and time-consuming, and often requires familiarity with convex analysis. Domain-specific languages (DSLs) for convex optimization abstract away the process of converting problems to canonical forms, letting users specify problems in a natural syntax; programs are then lowered to canonical forms and supplied to numerical solvers behind-the-scenes....

### Nonconvex problems

It is possible to differentiate through nonconvex problems, either analytically or by unrolling SGD, Because convex programs can typically be solved efficiently and to high accuracy, it is preferable to use convex optimization layers over nonconvex optimization layers when possible. This is especially true in the setting of low-latency inference. The use of differentiable nonconvex programs in end-to-end learning pipelines, discussed in, is an interesting direction for future research.

with blank spaces representing zeros and the horizontal line denoting the cone boundary. In this case, the parameters $F$, $g$ and $\lambda$ are just negated and copied into the problem data.

$x$ or $y$ is constant (i.e., both parameter-free and variable-free);

[⬇](data:text/plain;base64,aW1wb3J0IHRvcmNoCmZyb20gY3Z4cHlsYXllcnMudG9yY2ggaW1wb3J0IEN2eHB5TGF5ZXIKCkZfdCA9IHRvcmNoLnJhbmRuKG0sIG4sIHJlcXVpcmVzX2dyYWQ9VHJ1ZSkKZ190ID0gdG9yY2gucmFuZG4obSwgMSwgcmVxdWlyZXNfZ3JhZD1UcnVlKQpsYW1iZF90ID0gdG9yY2gucmFuZCgxLCAxLCByZXF1aXJlc19ncmFkPVRydWUpCmxheWVyID0gQ3Z4cHlMYXllcigKICAgIHByb2JsZW0sIHBhcmFtZXRlcnM9W0YsIGcsIGxhbWJkXSwgdmFyaWFibGVzPVt4XSkKeF9zdGFyLCA9IGxheWVyKEZfdCwgZ190LCBsYW1iZF90KQp4X3N0YXIuc3VtKCkuYmFja3dhcmQoKQ==){download=""}

The point of this paper is to do what DSLs have done for convex optimization, but for differentiable convex optimization layers....
