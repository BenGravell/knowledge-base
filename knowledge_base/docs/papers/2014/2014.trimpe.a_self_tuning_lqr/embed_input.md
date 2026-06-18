<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Self-Tuning LQR Approach Demonstrated on an Inverted Pendulum

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An automatic controller tuning approach is presented that iteratively updates a linear quadratic regulator (LQR) design such that the resulting controller achieves improved closed-loop performance. In each iteration, an updated LQR gain is obtained by adjusting the weighting matrices of the associated quadratic cost. The performance of the resulting controller (measured in terms of another quadratic cost with fixed weights) is evaluated from experimental data obtained by testing the controller in closed-loop operation. The weight adjustment occurs through a stochastic optimization seeking to minimize the experimental cost. Simulation results of a stochastic linear system show that the self-tuning algorithm can recover optimal performance despite having imprecise model knowledge. Experiments on an inverted pendulum demonstrate that the method is effective in improving the system's balancing performance.
