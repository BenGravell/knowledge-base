<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Goldstein-Levitin-Polyak Gradient Projection Method

Topics include Gradient projection, Projected gradient descent, Step-size rules, Active-set identification, Constrained optimization, Armijo rule, Optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Bertsekas analyzes the Goldstein-Levitin-Polyak gradient projection method and proposes convergent step-size rules with finite active-constraint identification under mild assumptions. The paper connects projected-gradient methods to Armijo-style line search and to later superlinear local methods once the active set is identified.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers some aspects of a gradient projection method proposed by Goldstein, Levitin and Polyak, and more recently, in a less general context, by McCormick. We propose and analyze some convergent step-size rules to be used in conjunction with the method. These rules are similar in spirit to the efficient Armijo rule for the method of steepest descent and under mild assumptions they have the desirable property that they identify the set of active inequality constraints in a finite number of iterations. As a result the method may be converted towards the end of the process to a conjugate direction, quasi-Newton or Newton's method, and achieve the attendant superlinear convergence rate. As an example we propose some quadratically convergent combinations of the method with Newton's method. Such combined methods appear to be very efficient for large-scale problems with many simple constraints such as those often appearing in optimal control.
