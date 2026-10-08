<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-Based Methods for Factored Task and Motion Planning

Topics include Task and motion planning, Factored transition systems, Conditional sampling, Probabilistic completeness, Robotic manipulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates hybrid task-and-motion planning as factored transition systems and develops conditional-sampling algorithms with probabilistic completeness guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a general-purpose formulation of a large class of discrete-time planning problems, with hybrid state and control-spaces, as factored transition systems. Factoring allows state transitions to be described as the intersection of several constraints each affecting a subset of the state and control variables. Robotic manipulation problems with many movable objects involve constraints that only affect several variables at a time and therefore exhibit large amounts of factoring. We develop a theoretical framework for solving factored transition systems with sampling-based algorithms. The framework characterizes conditions on the submanifold in which solutions lie, leading to a characterization of robust feasibility that incorporates dimensionality-reducing constraints. It then connects those conditions to corresponding conditional samplers that can be composed to produce values on this submanifold. We present two domain-independent, probabilistically complete planning algorithms that take, as input, a set of conditional samplers. We demonstrate the empirical efficiency of these algorithms on a set of challenging task and motion planning problems involving picking, placing, and pushing.
