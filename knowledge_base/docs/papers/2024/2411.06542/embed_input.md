Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?

Topics include Robotics, Robustness, Control.

Designing planners and controllers for contact-rich manipulation is extremely challenging as contact violates the smoothness conditions that many gradient-based controller synthesis tools assume. Contact smoothing approximates a non-smooth system with a smooth one, allowing one to use these synthesis tools more effectively. However, applying classical control synthesis methods to smoothed contact dynamics remains relatively under-explored. This paper analyzes the efficacy of linear controller synthesis using differential simulators based on contact smoothing. We introduce natural baselines for leveraging contact smoothing to compute (a) open-loop plans robust to uncertain conditions and/or dynamics, and (b) feedback gains to stabilize around open-loop plans. Using robotic bimanual whole-body manipulation as a testbed, we perform extensive empirical experiments on over 300 trajectories and analyze why LQR seems insufficient for stabilizing contact-rich plans.

## Introduction

Dexterous manipulation is full of contact-rich interactions, enabling various tasks through complex frictional interactions. Historically, the non-smooth nature of contact has precluded a range of planning and control methods that rely on gradients of the dynamics. Recent advances have utilized *contact smoothing* --- where non-smooth dynamics are replaced by a continuously differentiable proxy --- to great effect as surrogate dynamics models for *planning* through contact. One may hope, then, that smoothing enables the use gradient-based *control*.

This work suggests that the above hope may face significant obstacles. We introduce LQR control for contact-manipulation via contact smoothing. Furthermore, we present and analyze robust trajectory optimization, hoping that the generated trajectories are robust to the model errors accumulated by using a surrogate dynamics model for control, and thus more amenable to LQR. Then, we extensively evalute the performance of these methods, both in simulation and in hardware, on a bimanual whole-body manipulation as shown in Fig..

> *Despite its efficacy in planning through contact, dynamical smoothing alone is unsatisfactory as a means to obtaining linear control policies.*

Finally, we identify the key factors leading to the inadequacies of linear control; namely, the *unilaterality* of contact, and the tendency of controllers to "push and pull" unless the dynamics are only very-slightly smoothed.

## Conclusion

Is linear feedback on smoothed dynamics sufficient for stabilizing contact-rich plans? Our analysis and experiments suggest that designing LQR for contact-rich plans does not work well in general. However, we observe that MP-TrajOPT enables LQR to improve its performance when MP-TrajOPT is solved, although MP-TrajOPT often fails to converge. Through this paper, we first present how contact smoothing technique can be used for designing trajectory optimization baselines and LQR. Then, we extensively conduct various experiments of LQR under different uncertainties.
