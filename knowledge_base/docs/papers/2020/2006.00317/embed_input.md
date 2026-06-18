Control Design for Risk-Based Signal Temporal Logic Specifications

We present a general framework for risk semantics on Signal Temporal Logic (STL) specifications for stochastic dynamical systems using axiomatic risk theory. We show that under our recursive risk semantics, risk constraints on STL formulas can be expressed in terms of risk constraints on atomic predicates. We then show how this allows a (stochastic) STL risk constraint to be transformed into a risk-tightened deterministic STL constraint on a related deterministic nominal system, enabling the application of existing STL methods. For affine predicate functions and a (coherent) Distributionally Robust Value at Risk measure, we show how risk constraints on atomic predicates can be reformulated as tightened deterministic affine constraints. We demonstrate the framework using a Model Predictive Control (MPC) design with an STL risk constraint.

## Introduction

TEMPORAL logics allow to reason about temporal properties of systems and have traditionally been used in formal verification and model checking. More recently, temporal logics have also been used to impose highly expressive mission specifications on complex autonomous systems. For systems under linear temporal logic (LTL) and metric interval temporal logic (MITL) specifications, motion planning and control synthesis algorithms have been proposed .

*Signal Temporal Logic (STL)* is a temporal logic interpreted over dense-time real-valued *(deterministic)* signals similar to MITL; it allows to additionally impose quantitative spatial properties by means of predicates that go beyond the abstract use of propositions in LTL and MITL. STL is hence more expressive and has been the focus of motion planning and control synthesis in areas such as robotics.

A large fraction of the aforementioned research focuses on finite abstractions and/or *deterministic* systems. However, methodological advances are required to account for inherent uncertainties and high-dimensional continuous spaces in autonomous systems, especially due to *stochastic uncertainties* arising from the use of noisy data and learning components. Robust extensions of have been presented . Probabilistic notions of STL for stochastic systems have been presented .

Contributions. 1) We present a general framework for defining risk semantics of STL specifications for *stochastic dynamical systems* using axiomatic risk theory. In particular, we compose risk metrics with predicate functions, which become stochastic in the considered setup. 2) We then recursively define risk semantics for Boolean and temporal STL operators. For a given STL specification, we show that these risk semantics can be expressed as risk constraints on predicate functions over certain time intervals.

## Conclusion and Future Work

We presented a general framework for risk-based STL specifications for stochastic systems using axiomatic risk theory. We are exploring several extensions and variations in ongoing and future work, including explicit reformulations for various risk measures and ambiguity sets, non-affine predicates, non-linear dynamics, infinite-horizon persistent tasks, and alternative risk semantics.
