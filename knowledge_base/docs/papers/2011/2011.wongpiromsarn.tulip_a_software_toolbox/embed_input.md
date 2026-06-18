<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TuLiP: A Software Toolbox for Receding Horizon Temporal Logic Planning

Topics include TuLiP, Temporal logic planning, Correct-by-construction control, Linear temporal logic, Receding horizon planning, Formal methods, Embedded control software.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces TuLiP as a Python toolbox for synthesizing embedded control software from temporal-logic specifications. The key contribution is an integrated workflow for finite-state abstraction, adversarial LTL synthesis, and receding-horizon planning that reduces computational burden while preserving correctness guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes TuLiP, a Python-based software toolbox for the synthesis of embedded control software that is provably correct with respect to an expressive subset of linear temporal logic (LTL) specifications. TuLiP combines routines for finite state abstraction of control systems, digital design synthesis from LTL specifications, and receding horizon planning. The underlying digital design synthesis routine treats the environment as adversary; hence, the resulting controller is guaranteed to be correct for any admissible environment profile. TuLiP applies the receding horizon framework, allowing the synthesis problem to be broken into a set of smaller problems, and consequently alleviating the computational complexity of the synthesis procedure, while preserving the correctness guarantee.
