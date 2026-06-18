<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PySINDy: A Comprehensive Python Package for Robust Sparse System Identification

Topics include SINDy, System identification, Software, Python, Sparse regression.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Comprehensive Python package implementing SINDy with support for multiple sparse regression algorithms, customizable feature libraries, etc.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Automated data-driven modeling, the process of directly discovering the governing equations of a system from data, is increasingly being used across the scientific community. PySINDy is a Python package that provides tools for applying the sparse identification of nonlinear dynamics (SINDy) approach to data-driven model discovery. In this major update to PySINDy, we implement several advanced features that enable the discovery of more general differential equations from noisy and limited data. The library of candidate terms is extended for the identification of actuated systems, partial differential equations (PDEs), and implicit differential equations. Robust formulations, including the integral form of SINDy and ensembling techniques, are also implemented to improve performance for real-world data. Finally, we provide a range of new optimization algorithms, including several sparse regression techniques and algorithms to enforce and promote inequality constraints and stability. Together, these updates enable entirely new SINDy model discovery capabilities that have not been reported in the literature, such as constrained PDE identification and ensembling with different sparse regression optimizers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Summary", "weight": 1.0} -->

Automated data-driven modeling, the process of directly discovering the governing equations of a system from data, is increasingly being used across the scientific community. PySINDy is a Python package that provides tools for applying the sparse identification of nonlinear dynamics (SINDy) approach to data-driven model discovery. In this major update to PySINDy, we implement several advanced features that enable the discovery of more general differential equations from noisy and limited data. The library of candidate terms is extended for the identification of actuated systems, partial differential equations (PDEs), and implicit differential equations. Robust formulations, including the integral form of SINDy and ensembling techniques, are also implemented to improve performance for real-world data. Finally, we provide a range of new optimization algorithms, including several sparse regression techniques and algorithms to enforce and promote inequality constraints and stability. Together, these updates enable entirely new SINDy model discovery capabilities that have not been reported in the literature, such as constrained PDE identification and ensembling with different sparse regression optimizers.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Statement of need", "weight": 1.0} -->

Traditionally, the governing laws and equations of nature have been derived from first principles and based on rigorous experimentation and expert intuition. In the modern era, cheap and efficient sensors have resulted in an unprecedented growth in the availability of measurement data, opening up the opportunity to perform automated model discovery using data-driven modeling. These data-driven approaches are also increasingly useful for processing and interpreting the information in these large datasets. A number of such approaches have been developed in recent years, including the dynamic mode decomposition, Koopman theory, nonlinear autoregressive algorithms, neural networks, Gaussian process regression, operator inference and reduced-order modeling, genetic programming, and sparse regression. These approaches have seen many variants and improvements over the years, so data-driven modeling software must be regularly updated to remain useful to the scientific community. The SINDy approach has experienced particularly rapid development, motivating this major update to aggregate these innovations into a single open-source tool that is transparent and easy to use for non-experts or scientists from other fields.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Statement of need", "weight": 1.0} -->

The original PySINDy code provided an implementation of the traditional SINDy method, which assumes that the dynamical evolution of a state variable ${\mathbf{q}{(t)}} \in {\mathbb{R}}^{n}$ follows an ODE described by a function $\mathbf{f}$,

<!-- chunk {"id": "body-0007", "role": "body", "section": "Statement of need", "weight": 1.0} -->

where $\mathbf{\Xi} = {\lbrack{\mathbf{ξ}}_{1},{\mathbf{ξ}}_{2},\ldots,{\mathbf{ξ}}_{p}\rbrack}$ contain the sparse coefficients. In order for this strategy to be successful, a reasonably accurate approximation of $\mathbf{f}{(\mathbf{q})}$ should exist as a sparse expansion in the span of $\mathbf{θ}$. Therefore, background scientific knowledge about expected terms in $\mathbf{f}{(\mathbf{q})}$ can be used to choose the library $\mathbf{θ}$. To pose SINDy as a regression problem, we assume we have a set of state measurements sampled at time steps $t_{1},\ldots,t_{m}$ and rearrange the data into the data matrix $\mathbf{Q} \in {\mathbb{R}}^{m \times n}$,

<!-- chunk {"id": "body-0008", "role": "body", "section": "Statement of need", "weight": 1.0} -->

A matrix of derivatives in time, $\mathbf{Q}_{t}$, is defined similarly and can be numerically computed from $\mathbf{Q}$. PySINDy defaults to second order finite differences for computing derivatives, although a host of more sophisticated methods are now available, including arbitrary order finite differences, Savitzky-Golay derivatives (i.e. polynomial-filtered derivatives), spectral derivatives with optional filters, arbitrary order spline derivatives, and total variational derivatives.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Statement of need", "weight": 1.0} -->

After $\mathbf{Q}_{t}$ is obtained, Eq. becomes $\mathbf{Q}_{t} \approx {\mathbf{\Theta}{(\mathbf{Q})}\mathbf{\Xi}}$ and the goal of the SINDy sparse regression problem is to choose a sparse set of coefficients $\mathbf{\Xi}$ that accurately fits the measured data in $\mathbf{Q}_{t}$. We can promote sparsity in the identified coefficients via a sparse regularizer $R{(\mathbf{\Xi})}$, such as the $l_{0}$ or $l_{1}$ norm, and use a sparse regression algorithm such as SR3 to solve the resulting optimization problem,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Statement of need", "weight": 1.0} -->

The original PySINDy package was developed to identify a particular class of systems described by Eq.. Recent variants of the SINDy method are available that address systems with control inputs and model predictive control (MPC), systems with physical constraints, implicit ODEs, PDEs, and weak form ODEs and PDEs. Other methods, such as ensembling and sub-sampling, are often vital for making the identification of Eq. more robust. In order to incorporate these new developments and accommodate the wide variety of possible dynamical systems, we have extended PySINDy to a more general setting and added significant new functionality. Our code^11^1 is thoroughly documented, contains extensive examples, and integrates a wide range of functionality, some of which may be found in a number of other local SINDy implementations^22^2

<!-- chunk {"id": "body-0011", "role": "body", "section": "Statement of need", "weight": 1.0} -->

In contrast to some of these existing codes, PySINDy is completely open-source, professionally-maintained (for instance, providing unit tests and adhering to PEP8 stylistic standards), and minimally dependent on non-standard Python packages.

<!-- chunk {"id": "body-0012", "role": "body", "section": "New Features", "weight": 1.0} -->

Given spatiotemporal data ${\mathbf{Q}{(\mathbf{x},t)}} \in {\mathbb{R}}^{m \times n}$, and optional control inputs $\mathbf{u} \in {\mathbb{R}}^{m \times r}$ (note $m$ has been redefined here to be the product of the number of spatial measurements and the number of time samples), PySINDy can now approximate algebraic systems of PDEs (and corresponding weak forms) in an arbitrary number of spatial dimensions. Assuming the system is described by a function $\mathbf{g}$, we have

<!-- chunk {"id": "body-0013", "role": "body", "section": "New Features", "weight": 1.0} -->

ODEs, implicit ODEs, PDEs, and other dynamical systems are subsets of Eq.. We can accommodate control terms and partial derivatives in the SINDy library by adding them as columns in $\mathbf{\Theta}{(\mathbf{Q})}$, which becomes $\mathbf{\Theta}{(\mathbf{Q},\mathbf{Q}_{t},\mathbf{Q}_{x},\ldots,\mathbf{u})}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "New Features", "weight": 1.0} -->

In addition, we have extended PySINDy to handle more complex modeling scenarios, including trapping SINDy for provably stable ODE models for fluids, models trained using multiple dynamic trajectories, and the generation of many models with sub-sampling and ensembling methods for cross-validation and probabilistic system identification. In order to solve Eq., PySINDy implements several different sparse regression algorithms. Greedy sparse regression algorithms, including step-wise sparse regression (SSR) and forward regression orthogonal least squares (FROLS), are now available. For maximally versatile candidate libraries, the new GeneralizedLibrary class allows for tensoring, concatenating, and otherwise combining many different candidate libraries, along with optionally specifying a subset of the inputs to use for generating each of the libraries. Fig. 1 illustrates the PySINDy code structure, changes, and high-level goals for future work, and YouTube tutorials for this new functionality are available online.

<!-- chunk {"id": "body-0015", "role": "body", "section": "New Features", "weight": 1.0} -->

PySINDy includes extensive Jupyter notebook tutorials that demonstrate the usage of various features of the package and reproduce nearly the entirety of the examples from the original SINDy paper, trapping SINDy paper, and the PDE-FIND paper. We include an extended example for the quasiperiodic shear-driven cavity flow. As a simple illustration of the new functionality, we demonstrate how SINDy can be used to identify the Kuramoto-Sivashinsky (KS) PDE from data. We train the model on the first 60% of the data from Rudy et al., which in total contains 1024 spatial grid points and 251 time steps. The KS model is identified correctly and the prediction for $\overset{˙}{\mathbf{q}}$ on the remaining testing data indicates strong performance in Fig. 2. Lastly, we provide a useful flow chart in Fig. 3 so that users can make informed choices about which advanced methods are suitable for their datasets.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The goal of the PySINDy package is to enable anyone with access to measurement data to engage in scientific model discovery. The package is designed to be accessible to inexperienced users, adhere to scikit-learn standards, include most of the existing SINDy variations in the literature, and provide a large variety of functionality for more advanced users. We hope that researchers will use and contribute to the code in the future, pushing the boundaries of what is possible in system identification.
