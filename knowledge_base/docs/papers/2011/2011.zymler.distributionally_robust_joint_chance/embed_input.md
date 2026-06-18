<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Joint Chance Constraints with Second-Order Moment Information

Topics include Distributionally robust optimization, Joint chance constraints, Worst-case conditional value at risk, Semidefinite programming, Moment ambiguity, Robust control, Sequential convex optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops SDP-representable approximations for chance constraints when only moments and support are known, using worst-case CVaR as the organizing surrogate. The important contribution is separating the exact individual-constraint cases from a tunable joint-constraint approximation whose scaling parameters can be optimized and interpreted through duality, giving a practical route for robust water-reservoir control and similar safety-limited problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop tractable semidefinite programming based approximations for distributionally robust individual and joint chance constraints, assuming that only the first- and second-order moments as well as the support of the uncertain parameters are given. It is known that robust chance constraints can be conservatively approximated by Worst-Case Conditional Value-at-Risk (CVaR) constraints. We first prove that this approximation is exact for robust individual chance constraints with concave or (not necessarily concave) quadratic constraint functions, and we demonstrate that the Worst-Case CVaR can be computed efficiently for these classes of constraint functions. Next, we study the Worst-Case CVaR approximation for joint chance constraints. This approximation affords intuitive dual interpretations and is provably tighter than two popular benchmark approximations. The tightness depends on a set of scaling parameters, which can be tuned via a sequential convex optimization algorithm. We show that the approximation becomes essentially exact when the scaling parameters are chosen optimally and that the Worst-Case CVaR can be evaluated efficiently if the scaling parameters are kept constant. We evaluate our joint chance constraint approximation in the context of a dynamic water reservoir control problem and numerically demonstrate its superiority over the two benchmark approximations.
