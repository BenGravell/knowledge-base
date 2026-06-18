Non-asymptotic Identification of LTI Systems from a Single Trajectory

Topics include Stability analysis, Kalman filtering, Accuracy, Sample complexity, Learning, LTI.

We consider the problem of learning a realization for a linear time-invariant (LTI) dynamical system from input/output data. Given a single input/output trajectory, we provide finite time analysis for learning the system's Markov parameters, from which a balanced realization is obtained using the classical Ho-Kalman algorithm. By proving a stability result for the Ho-Kalman algorithm and combining it with the sample complexity results for Markov parameters, we show how much data is needed to learn a balanced realization of the system up to a desired accuracy with high probability.

## Introduction

Many modern control design techniques rely on the existence of a fairly accurate state-space model of the plant to be controlled. Although in some cases a model can be obtained from first principles, there are many situations in which a model should be learned from input/output data. Classical results in system identification provide asymptotic convergence guarantees for learning models from data. However, finite sample complexity properties have been rarely discussed in system identification literature; and earlier results are conservative.

There is recent interest from the machine learning community in data-driven control and non-asymptotic analysis. Putting aside the reinforcement learning literature and restricting our attention to linear state-space models, the work in this area can be divided into two categories: (i) directly learning the control inputs to optimize a control objective or analyzing the predictive power of the learned representation, (ii) learning the parameters of the system model from limited data. For the former problem, the focus has been on exploration/exploitation type formulations and regret analysis.

In this paper we focus on learning a realization for an LTI system from a single *input/output* trajectory. This setting is significantly more challenging than earlier studies that assume that (multiple independent) *state* trajectories are available. One of our main contributions is to derive sample complexity results in learning the Markov parameters, to be precisely defined later, of the system using a least squares algorithm. Markov parameters play a central role in system identification and they can also be directly used in control design when the system model itself is not available.

## Problem Setup

We first introduce the basic notation. Spectral norm $\parallel \cdot \parallel$ returns the largest singular value of a matrix. Multivariate normal distribution with mean $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ is denoted by $\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}$. ${\mathbf{X}}^{\ast}$ denotes the transpose of a matrix $\mathbf{X}$. ${\mathbf{X}}^{\dagger}$ returns the Moore--Penrose inverse of the matrix $\mathbf{X}$. Covariance matrix of a random vector $\mathbf{v}$ is denoted by $\mathbf{\Sigma}{({\mathbf{v}})}$. $\text{tr}{( \cdot )}$ returns the trace of a matrix.
