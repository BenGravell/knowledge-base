Risk-averse Shortest Path Problems

Topics include Risk-averse routing, Shortest path problem, Conditional value at risk, Distributional robustness, Dynamic programming, Uncertain travel times, Worst-case conditional value at risk.

Studies shortest-path policies under uncertain arc lengths when optimizing expected travel time is too risk-neutral for one-shot decisions. The paper formulates CVaR and worst-case CVaR routing variants, shows how risk-averse objectives change the policy structure, and connects distributional ambiguity to tractable dynamic-programming style algorithms for routing with partial distributional information.

We investigate routing policies for shortest path problems with uncertain arc lengths. The objective is to minimize a risk measure of the total travel time. We use the conditional value-at-risk (CVaR) for when the arc lengths (durations) have known distributions and the worst-case CVaR for when these distributions are only partially described. Policies which minimize the expected travel time (average-optimal policies) are desirable for experiments that are repeated several times, but the fact that they take no account of risk makes them unsuitable for decisions that need to be taken only once. In these circumstances, policies that minimize a risk measure provide protection against rare events with high cost.
