Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?

Topics include Robotics, Robustness, Control.

Designing planners and controllers for contact-rich manipulation is extremely challenging as contact violates the smoothness conditions that many gradient-based controller synthesis tools assume. Contact smoothing approximates a non-smooth system with a smooth one, allowing one to use these synthesis tools more effectively. However, applying classical control synthesis methods to smoothed contact dynamics remains relatively under-explored. This paper analyzes the efficacy of linear controller synthesis using differential simulators based on contact smoothing. We introduce natural baselines for leveraging contact smoothing to compute (a) open-loop plans robust to uncertain conditions and/or dynamics, and (b) feedback gains to stabilize around open-loop plans. Using robotic bimanual whole-body manipulation as a testbed, we perform extensive empirical experiments on over 300 trajectories and analyze why LQR seems insufficient for stabilizing contact-rich plans. The video summarizing this paper and hardware experiments is found here:

## Introduction

Dexterous manipulation is full of contact-rich interactions, enabling various tasks through complex frictional interactions. Historically, the non-smooth nature of contact has precluded a range of planning and control methods that rely on gradients of the dynamics. Recent advances have utilized *contact smoothing* --- where non-smooth dynamics are replaced by a continuously differentiable proxy --- to great effect as surrogate dynamics models for *planning* through contact. One may hope, then, that smoothing enables the use gradient-based *control*.

Figure 1: These figures show snapshots of hardware experiments using LQR and open-loop controllers under perturbations to initial conditions of cylinder. The thick and thin lines represent the desired frame at the terminal time step and the current frame of the cylinder, respectively. While LQR outperforms open-loop in this example, a more comprehensive evaluation shows that LQR generally performs poorly. The hardware experiment videos can be found here.

## Conclusion

Is linear feedback on smoothed dynamics sufficient for stabilizing contact-rich plans? Our analysis and experiments suggest that designing LQR for contact-rich plans does not work well in general. However, we observe that MP-TrajOPT enables LQR to improve its performance when MP-TrajOPT is solved, although MP-TrajOPT often fails to converge. Through this paper, we first present how contact smoothing technique can be used for designing trajectory optimization baselines and LQR. Then, we extensively conduct various experiments of LQR under different uncertainties....

We adopt a higher control loop frequency in Drake simulations, which necessitates interpolation of these discrete-time quantities. To do so, we convert the knot points into continuous time using First-Order Hold (FOH): states $\mathbf{x}^{\text{FOH}}{(t)}$, feedforward control input $\mathbf{v}^{\text{FOH}}{(t)}$, and feedback control input trajectories $\mathbf{K}^{\text{FOH}}{(t)}$. For $\mathbf{K}^{\text{FOH}}{(t)}$, we interpolate elements of $\mathbf{K}_{t}$ using FOH....

Using, we can compute LQR feedback gains $\mathbf{K}$. The objective of using LQR is to design a controller that can locally stabilize the system. In this work, we consider the following optimal control problem given $\mathbf{x}_{t}$ and ${\mathbf{v}_{t},t} \in \mathcal{T}$.
