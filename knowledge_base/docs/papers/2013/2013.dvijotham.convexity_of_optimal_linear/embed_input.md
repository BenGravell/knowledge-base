<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convexity of Optimal Linear Controller Design

Topics include Stochastic optimal control, Linear feedback, Convex synthesis, Risk-sensitive control, Structured controllers, Variable stiffness, Distributed control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a stochastic optimal-control formulation where optimizing linear feedback gains is convex for time-varying linear systems with costs built from mixtures of exponentiated quadratics. The paper is a companion to the broader structured-control thread: it shows how nonstandard but meaningful control objectives can make feedback-gain constraints and penalties convex, then demonstrates the approach on practical control examples.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop a general class of stochastic optimal control problems for which the problem of designing optimal linear feedback gains is convex. The class of problems includes arbitrary time varying linear systems and costs that are mixtures of exponentiated quadratics. This allows us to model problems with quadratic state costs and linear constraints on states and state transitions. Further, convexity in the feedback gains lets us impose arbitrary convex constraints or penalties on the feedback matrix: Thus we can model problems like distributed control (by imposing a sparsity structure on the feedback matrix) and variable-stiffness control (by applying time-varying penalties to feedback gain matrices). We show that the convex optimization problem can be solved efficiently by using the structure of the matrices involved. Finally, we present an application of these ideas to a practical problem arising in distributed control of power systems.
