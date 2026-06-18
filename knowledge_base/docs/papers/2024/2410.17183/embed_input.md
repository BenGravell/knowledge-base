Risk-Averse Model Predictive Control for Racing in Adverse Conditions

Model predictive control (MPC) algorithms can be sensitive to model mismatch when used in challenging nonlinear control tasks. In particular, the performance of MPC for vehicle control at the limits of handling suffers when the underlying model overestimates the vehicle's capabilities. In this work, we propose a risk-averse MPC framework that explicitly accounts for uncertainty over friction limits and tire parameters. Our approach leverages a sample-based approximation of an optimal control problem with a conditional value at risk (CVaR) constraint. This sample-based formulation enables planning with a set of expressive vehicle dynamics models using different tire parameters. Moreover, this formulation enables efficient numerical resolution via sequential quadratic programming and GPU parallelization. Experiments on a Lexus LC 500 show that risk-averse MPC unlocks reliable performance, while a deterministic baseline that plans using a single dynamics model may lose control of the vehicle in adverse road conditions.

## Introduction

Expert racing drivers are able to pilot a vehicle at its performance limits by using all the available friction potential between the tires and the road. They are able to do this reliably lap after lap despite changes in the vehicle's performance and behavior due to tire temperature, tire wear, and especially, weather conditions. However, current approaches to autonomous vehicle control struggle in such settings because they are sensitive to discrepancies between the model used for control and the true system. This sensitivity motivates the design of new algorithms that can robustly leverage the full vehicle capabilities.

Research in autonomous racing has boomed in the last decade, see for a survey. State of the art control approaches to racing use model predictive control (MPC) to maximize path progress along a planning horizon while respecting constraints such as track bounds. These works use vehicle dynamics models of varying fidelity such as point mass models, singletrack models with Pacejka and Fiala tire models, and data-driven models.

These modeling challenges motivate the design of MPC tools that explicitly account for uncertainty to optimally trade off robustness and performance. Previous uncertainty-aware MPC methods for racing use stochastic MPC and tube MPC. Using a linear model of the vehicle with additive disturbances capturing model mismatch, these methods have demonstrated reliable racing performance. In, using Gaussian process models allowed online adaptation to gradually improve laptime.

We

We propose a risk-constrained racing formulation that explicitly accounts for uncertainty over tire forces. It includes a conditional value at risk (CVaR) constraint for track bounds, nonlinear uncertain dynamics, and a cost to minimize expected lap time.

## Conclusion

We presented a risk-averse MPC framework for racing and showed that accounting for different tire parameters provides a natural avenue for infusing robustness into MPC. By leveraging a particular sample-based risk-averse formulation, our method accurately accounts for uncertain nonlinear tire dynamics and is amenable to online replanning in MPC.
