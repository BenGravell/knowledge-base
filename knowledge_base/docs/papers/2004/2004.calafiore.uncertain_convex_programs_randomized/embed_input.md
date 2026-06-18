<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Uncertain Convex Programs: Randomized Solutions and Confidence Levels

Topics include Scenario optimization, Uncertain convex programs, Randomized algorithms, Chance constraints, Robust optimization, Sample complexity, Probabilistic robustness, Constraint sampling.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the scenario approach for uncertain convex programs by replacing infinitely many uncertain constraints with a random finite sample and certifying the violation probability of the resulting solution. The paper is foundational for scenario optimization because it provides explicit sample-size confidence bounds that make probabilistic robustness computationally tractable.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many engineering problems can be cast as optimization problems subject to convex constraints that are parameterized by an uncertainty or 'instance' parameter. Two main approaches are generally available to tackle constrained optimization problems in presence of uncertainty: robust optimization and chance-constrained optimization. Robust optimization is a deterministic paradigm where one seeks a solution which simultaneously satisfies all possible constraint instances. In chance-constrained optimization a probability distribution is instead assumed on the uncertain parameters, and the constraints are enforced up to a pre-specified level of probability. Unfortunately however, both approaches lead to computationally intractable problem formulations. In this paper, we consider an alternative 'randomized' or 'scenario' approach for dealing with uncertainty in optimization, based on constraint sampling. In particular, we study the constrained optimization problem resulting by taking into account only a finite set of N constraints, chosen at random among the possible constraint instances of the uncertain problem. We show that the resulting randomized solution fails to satisfy only a small portion of the original constraints, provided that a sufficient number of samples is drawn. Our key result is to provide an efficient and explicit bound on the measure (probability or volume) of the original constraints that are possibly violated by the randomized solution.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This volume rapidly decreases to zero as N is increased.
