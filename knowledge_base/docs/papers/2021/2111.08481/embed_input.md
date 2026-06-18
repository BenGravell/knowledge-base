PySINDy: A Comprehensive Python Package for Robust Sparse System Identification

Topics include SINDy, System identification, Software, Python, Sparse regression.

Comprehensive Python package implementing SINDy with support for multiple sparse regression algorithms, customizable feature libraries, etc.

Automated data-driven modeling, the process of directly discovering the governing equations of a system from data, is increasingly being used across the scientific community. PySINDy is a Python package that provides tools for applying the sparse identification of nonlinear dynamics (SINDy) approach to data-driven model discovery. In this major update to PySINDy, we implement several advanced features that enable the discovery of more general differential equations from noisy and limited data. The library of candidate terms is extended for the identification of actuated systems, partial differential equations (PDEs), and implicit differential equations. Robust formulations, including the integral form of SINDy and ensembling techniques, are also implemented to improve performance for real-world data. Finally, we provide a range of new optimization algorithms, including several sparse regression techniques and algorithms to enforce and promote inequality constraints and stability....

## Summary

Automated data-driven modeling, the process of directly discovering the governing equations of a system from data, is increasingly being used across the scientific community. PySINDy is a Python package that provides tools for applying the sparse identification of nonlinear dynamics (SINDy) approach to data-driven model discovery. In this major update to PySINDy, we implement several advanced features that enable the discovery of more general differential equations from noisy and limited data....

## Statement of need

## Conclusion

The goal of the PySINDy package is to enable anyone with access to measurement data to engage in scientific model discovery. The package is designed to be accessible to inexperienced users, adhere to scikit-learn standards, include most of the existing SINDy variations in the literature, and provide a large variety of functionality for more advanced users. We hope that researchers will use and contribute to the code in the future, pushing the boundaries of what is possible in system identification.

## New Features

A matrix of derivatives in time, $\mathbf{Q}_{t}$, is defined similarly and can be numerically computed from $\mathbf{Q}$. PySINDy defaults to second order finite differences for computing derivatives, although a host of more sophisticated methods are now available, including arbitrary order finite differences, Savitzky-Golay derivatives (i.e. polynomial-filtered derivatives), spectral derivatives with optional filters, arbitrary order spline derivatives, and total variational derivatives.

In addition, we have extended PySINDy to handle more complex modeling scenarios, including trapping SINDy for provably stable ODE models for fluids, models trained using multiple dynamic trajectories, and the generation of many models with sub-sampling and ensembling methods for cross-validation and probabilistic system identification. In order to solve Eq., PySINDy implements several different sparse regression algorithms. Greedy sparse regression algorithms, including step-wise sparse regression (SSR) and forward regression orthogonal least squares (FROLS), are now available....

Traditionally, the governing laws and equations of nature have been derived from first principles and based on rigorous experimentation and expert intuition....
