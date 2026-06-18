<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Koopman Meets Input-Output Data: Data-Driven Output-Feedback Control of Nonlinear Systems with Closed-Loop Guarantees

Topics include Data-driven control, Output feedback, Koopman operator, Nonlinear systems, Input-output data, Closed-loop guarantees, Bilinear surrogate models, Exponential stability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines Koopman operator ideas with input-output trajectory data to design output-feedback controllers for nonlinear systems with closed-loop guarantees. The method constructs an extended-state bilinear surrogate directly from measurements, then applies robust state-feedback design while proving convergence back for the original nonlinear state.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven control of nonlinear systems from input-output measurements remains a fundamental challenge, as existing approaches with rigorous closed-loop guarantees predominantly require access to full state measurements. In this paper, we address this gap by proposing a data-driven output-feedback controller design method for nonlinear systems that provides provable closed-loop guarantees while operating solely on measured input-output data. Our approach combines Koopman operator theory with an extended state representation of the nonlinear system constructed from input-output trajectories. This allows us to obtain a bilinear surrogate model directly from data, on which robust state-feedback design methods can be applied. By exploiting the observability of the underlying nonlinear system, we establish exponential stability of the extended state, which in turn implies exponential convergence of the original system state to the origin. Finally, we validate our theoretical findings in numerical simulations.
