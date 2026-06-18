Iteratively Saturated Kalman Filtering

The Kalman filter (KF) provides optimal recursive state estimates for linear-Gaussian systems and underpins applications in control, signal processing, and others. However, it is vulnerable to outliers in the measurements and process noise. We introduce the iteratively saturated Kalman filter (ISKF), which is derived as a scaled gradient method for solving a convex robust estimation problem. It achieves outlier robustness while preserving the KF's low per-step cost and implementation simplicity, since in practice it typically requires only one or two iterations to achieve good performance. The ISKF also admits a steady-state variant that, like the standard steady-state KF, does not require linear system solves in each time step, making it well-suited for real-time systems.

## Introduction

The Kalman filter is the prevalent tool for state estimation, prized for its simplicity, low computational cost, and optimality for linear-Gaussian systems. It has found extensive use in many fields, including control, signal processing, robotics, navigation, neural interface systems, and econometrics \[Kalman1960, MalikTBH2010, SmetsW2007, Huber2022\]. Despite its popularity, the KF is notoriously vulnerable to outliers in the measurements and process noise in the dynamics \[MasreliezM1977\].

In this work, we propose the iteratively saturated Kalman filter, which is a modification of the standard KF's update (or correction) step. It iterates a modified KF update step, in which a saturating nonlinearity is applied to compensate for both measurement and process noise outliers. The method is derived as a scaled gradient method \[Davidon1959, FletcherR1963\] for solving a particular convex robust estimation problem involving the Huber function. Since the ISKF typically requires only one or two iterations to achieve good performance, it retains the standard KF's ease of implementation and per-step cost.

The rest of the paper is organized as follows. We review prior work in §1.2. The system model is given in §1.3, and the iteratively saturated Kalman filter is introduced in §1.4. We derive the filter as a scaled gradient method in §1.5. Finally, we present numerical experiments in §1.8 and conclude in §1.9.

## Conclusion

We have introduced the iteratively saturated Kalman filter, a modification of the standard KF's update step that makes it robust to outliers. The method is derived as a scaled gradient method for solving a particular convex maximum a posteriori estimation problem. The steady-state variant of the ISKF matches the computational efficiency of the steady-state KF, and is well-suited for real-time applications.
