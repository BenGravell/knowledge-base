Finite Sample Identification of Bilinear Dynamical Systems

Topics include Bilinear systems, System identification, Sample complexity, Martingale small-ball, Control-affine systems, Nonlinear dynamics.

Gives finite-sample rates for learning bilinear dynamical systems from a single trajectory under a marginal mean-square stability condition. The analysis uses a martingale small-ball argument to obtain dimension- and trajectory-length-dependent rates without the instability penalties that simpler mixing arguments can introduce.

Bilinear dynamical systems are ubiquitous in many different domains and they can also be used to approximate more general control-affine systems. This motivates the problem of learning bilinear systems from a single trajectory of the system's states and inputs. Under a mild marginal mean-square stability assumption, we identify how much data is needed to estimate the unknown bilinear system up to a desired accuracy with high probability. Our sample complexity and statistical error rates are optimal in terms of the trajectory length, the dimensionality of the system and the input size. Our proof technique relies on an application of martingale small-ball condition. This enables us to correctly capture the properties of the problem, specifically our error rates do not deteriorate with increasing instability. Finally, we show that numerical experiments are well-aligned with our theoretical results.

## Introduction

Bilinear systems constitute an important class of nonlinear systems used in modeling systems in a variety of domains from engineering to biology. They also provide global approximators for more general nonlinear systems, and have recently been invoked in the study of Koopman operators for systems with control inputs. Due to the ubiquity of bilinear models, identification of such models from input-output data has also received interest in the literature both in continuous-time and discrete-time.

There is a growing body of literature on non-asymptotic properties and sample complexity of learning dynamical systems. For linear systems, the recent results include that establish that accuracy of the learned models improve at a rate ${\mathcal{O}{({1/\sqrt{T}})}},$ where $T$ is the trajectory length. These results are extended to certain classes of switched and nonlinear systems, where, with the exception of, mixing-time arguments are used to ease the statistical analysis.

To summarize, we make the following contributions towards bilinear system identification: (i) For a bilinear system with state dimension $n$ and input dimension $m$, the system dynamics involve $m + 1$ matrices of size $n \times n$. We estimate these dynamics with an error rate $\mathcal{O}{(\sqrt{{n{({m + 1})}}/T})}$. Our error rate is optimal in terms of the trajectory length $T$ and the dimension of the unknown matrices.

## II-A Bilinear Dynamical Systems

In this paper, we consider the identification of bilinear dynamical systems which are governed by the following state equation,
