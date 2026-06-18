PySINDy: A Comprehensive Python Package for Robust Sparse System Identification

Topics include SINDy, System identification, Software, Python, Sparse regression.

Comprehensive Python package implementing SINDy with support for multiple sparse regression algorithms, customizable feature libraries, etc.

Automated data-driven modeling, the process of directly discovering the governing equations of a system from data, is increasingly being used across the scientific community. PySINDy is a Python package that provides tools for applying the sparse identification of nonlinear dynamics (SINDy) approach to data-driven model discovery. In this major update to PySINDy, we implement several advanced features that enable the discovery of more general differential equations from noisy and limited data. The library of candidate terms is extended for the identification of actuated systems, partial differential equations (PDEs), and implicit differential equations. Robust formulations, including the integral form of SINDy and ensembling techniques, are also implemented to improve performance for real-world data. Finally, we provide a range of new optimization algorithms, including several sparse regression techniques and algorithms to enforce and promote inequality constraints and stability.

## Summary

Automated data-driven modeling, the process of directly discovering the governing equations of a system from data, is increasingly being used across the scientific community. PySINDy is a Python package that provides tools for applying the sparse identification of nonlinear dynamics (SINDy) approach to data-driven model discovery. In this major update to PySINDy, we implement several advanced features that enable the discovery of more general differential equations from noisy and limited data.

## Statement of need

Traditionally, the governing laws and equations of nature have been derived from first principles and based on rigorous experimentation and expert intuition. In the modern era, cheap and efficient sensors have resulted in an unprecedented growth in the availability of measurement data, opening up the opportunity to perform automated model discovery using data-driven modeling. These data-driven approaches are also increasingly useful for processing and interpreting the information in these large datasets.

The original PySINDy code provided an implementation of the traditional SINDy method, which assumes that the dynamical evolution of a state variable ${\mathbf{q}{(t)}} \in {\mathbb{R}}^{n}$ follows an ODE described by a function $\mathbf{f}$,

where $\mathbf{\Xi} = {\lbrack{\mathbf{ξ}}_{1},{\mathbf{ξ}}_{2},\ldots,{\mathbf{ξ}}_{p}\rbrack}$ contain the sparse coefficients. In order for this strategy to be successful, a reasonably accurate approximation of $\mathbf{f}{(\mathbf{q})}$ should exist as a sparse expansion in the span of $\mathbf{θ}$. Therefore, background scientific knowledge about expected terms in $\mathbf{f}{(\mathbf{q})}$ can be used to choose the library $\mathbf{θ}$.

## Conclusion

The goal of the PySINDy package is to enable anyone with access to measurement data to engage in scientific model discovery. The package is designed to be accessible to inexperienced users, adhere to scikit-learn standards, include most of the existing SINDy variations in the literature, and provide a large variety of functionality for more advanced users. We hope that researchers will use and contribute to the code in the future, pushing the boundaries of what is possible in system identification.
