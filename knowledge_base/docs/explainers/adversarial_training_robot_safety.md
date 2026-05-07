# Adversarial Training is Not Ready for Robot Learning

*Work by Mathias Lechner, Ramin Hasani, Radu Grosu, Daniela Rus, Thomas A. Henzinger*

This research suggests that adversarial training of neural network-based image classifiers, when applied in robot learning settings, can have the opposite of the intended effect, i.e. that adversarially-trained classifiers lead to less safe system operation than their nominal counterparts.

This work highlights the importance in **aligning the specification of the adversarial training and the control objective**. In particular, they demonstrate that the intuitive low-level training goal of maintaining high image classification accuracy under norm-bounded adversarial perturbations is not sufficient to provide the high-level goal of maintaining high safety of system trajectories under the same adversarial perturbations. This suggests that, to achieve true safety, some type of coupling between high-level control and low-level image classification must be enforced during training.

This work also highlights the **large gap between theory and practice** in data-driven control. In the literature on statistical learning for linear systems, rigorous guarantees of robustness are typically provided in a classical systems-theoretic sense e.g. ensuring stability of a system subject to model uncertainties and process + measurement disturbances.

For instance, in the CONLab work [“Policy Iteration for Linear Quadratic Games with Stochastic Parameters”](https://ieeexplore.ieee.org/abstract/document/9115001) we consider the setting of a linear system with full-state linear feedback control. We combine stochastic parameters as a device during control design to induce robustness to structured parametric uncertainty, with additive adversarial disturbances to handle unstructured model uncertainty. We also draw an analogy with the machine learning literature, where unstructured uncertainty is addressed by adversarial training examples, while structured uncertainty is addressed by domain randomization.

On the other hand, to control more complicated nonlinear systems, practitioners often use highly expressive neural networks for encoding and approximating value functions and control policies, as well as for processing raw measurements e.g. LiDAR and video image data, whose post-training behavior is not fully understood. Ensuring safety of neural network-based controllers in robot applications may be possible if the control safety can be meaningfully related to the neural network sensitivity using e.g. the Lipschitz constant (c.f. [“Efficient and Accurate Estimation of Lipschitz Constants for Deep Neural Networks”](https://arxiv.org/abs/1906.04893)) or constraining predictions to a safety set in the output space (c.f. [“Safety Verification and Robustness Analysis of Neural Networks via Quadratic Constraints and Semidefinite Programming”](https://arxiv.org/abs/1903.01287)).

Kudos to the authors for alerting practitioners to the dangers of naively applying adversarial training in robot learning. We will do our part to bridge the theory practice gap and provide techniques for achieving true safety in data-driven robot operations.

## Links

- [Paper on arXiv](https://arxiv.org/abs/2103.08187)
- [Paper on IEEE Xplore](https://ieeexplore.ieee.org/document/9561036)
- [VentureBeat post](https://venturebeat.com/technology/adversarial-training-reduces-safety-of-neural-networks-in-robots-research)
