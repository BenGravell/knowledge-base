Autonomous Vehicle Decision-Making and Monitoring Based on Signal Temporal Logic and Mixed-Integer Programming

Topics include Autonomous driving, Temporal logic, Mixed-integer programming, Formal verification, Safety verification, Decision-making, Optimization-based synthesis.

Formulates automated-driving decision making as a mixed-integer optimization problem generated from signal-temporal-logic goals and rules. A notable secondary contribution is reusing the same specifications for online monitoring when predictions or execution deviate from the plan.

We propose a decision-making system for auto-mated driving with formal guarantees, synthesized from Signal Temporal Logic (STL) specifications. STL formulae specifying overall and intermediate driving goals and the traffic rules are encoded as mixed-integer inequalities and combined with a simplified vehicle motion model, resulting in a mixed-integer optimization problem. The specification satisfaction for the actual vehicle motion is guaranteed by imposing constraints on the quantitative semantics of STL. For reducing the com-putational burden, we propose an STL encoding that results in a block-sparse structure. The same STL formulae are used for monitoring faults due to imperfect prediction on the vehicle and environment. We demonstrate our method on an urban scenario with intersections, obstacles, and no-pass zones.
