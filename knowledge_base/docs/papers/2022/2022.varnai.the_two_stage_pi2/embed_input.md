<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Two-Stage PI2 Control Strategy

Topics include Path integral policy improvement, Stochastic optimal control, Feedback control, Feedforward control, Reinforcement learning, Nonlinear control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Reframes PI2 as a two-stage strategy in which feedforward controls are optimized for closed-loop performance and the required feedbacks are implemented at run time. The paper simplifies the feedback-control side of PI2 for a broad class of stochastic nonlinear systems and demonstrates the resulting control law numerically.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

PI2 is a stochastic optimal control method generally regarded as a reinforcement learning algorithm. Recent work, however, suggests that the reinforcement learning aspect of PI2 actually appears when optimizing feedforward controls which will lead to optimal closed-loop performance once combined with feedback controls. These feedbacks are necessary to achieve the predicted performance, yet have been largely neglected in the literature and applications due to their complexity. In this letter, we show that the feedbacks actually take a simple-to-implement form for a wide range of system dynamics, paving way for future research and applications of PI2. The correctness of the results is demonstrated through numerical simulations.
