<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Algebraic Equation for the Discrete-Time Linear Quadratic Regulator Problem

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The discrete-time, infinite-horizon linear quadratic regulator (LQR) is studied with the objective of establishing a unified perspective on the problem by relying simultaneously on Dynamic Programming and the discrete Minimum Principle. While it is well known that the two strategies independently yield the optimal solution, it is shown here that their combination provides much deeper insights on the nature of the optimal solution and on the strategies by means of which it can be computed. More precisely, the optimal cost, captured by the matrix P, and the feedback gain matrix K are jointly related via the observability matrix of the underlying state/costate (Hamiltonian) dynamics when the state alone is measured. Such an abstract property is then instrumental for deriving alternative characterizations of the optimal solution. First, an algebraic equation, referred to as the policy algebraic equation, is established in the variable K alone and with dimension typically much smaller than the size of the classic ARE arising in discrete-time LQR, although comprising polynomial equations of higher degree. This equation permits the direct construction of the optimal feedback gain (i.e., the actor) without the need for the simultaneous computation of the optimal cost (i.e., the critic).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The structure of the policy algebraic equation naturally lends itself to an iterative approach towards its solution, which is restricted to the space of policies alone and which does not require the explicit solution of any intermediate (linear) equation at each step. Furthermore, as a consequence of the above properties, it is possible to derive a Riccati equation in P, although with coefficients defined by polynomial functions of K, with the property that the constant and quadratic terms are symmetric and sign-definite. This aspect is remarkably different from the classic ARE associated to the discrete-time LQR and more akin to the continuous-time counterpart.summary: ''
