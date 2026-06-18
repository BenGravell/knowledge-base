CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples

Topics include Compressed sensing, Sparse recovery, Greedy algorithms, Signal reconstruction, CoSaMP, Error bounds.

Introduces CoSaMP, a greedy sparse-recovery algorithm with provable accuracy, stability, and runtime guarantees under standard compressed-sensing assumptions. It combines matching-pursuit style support identification with least-squares refinement and pruning.

Compressive sampling offers a new paradigm for acquiring signals that are compressible with respect to an orthonormal basis. The major algorithmic challenge in compressive sampling is to approximate a compressible signal from noisy samples. This paper describes a new iterative recovery algorithm called CoSaMP that delivers the same guarantees as the best optimization-based approaches. Moreover, this algorithm offers rigorous bounds on computational cost and storage. It is likely to be extremely efficient for practical problems because it requires only matrix-vector multiplies with the sampling matrix. For many cases of interest, the running time is just O(N*log^2(N)), where N is the length of the signal.

## Introduction

Most signals of interest contain scant information relative to their ambient dimension, but the classical approach to signal acquisition ignores this fact. We usually collect a complete representation of the target signal and process this representation to sieve out the actionable information. Then we discard the rest. Contemplating this ugly inefficiency, one might ask if it is possible instead to acquire *compressive samples*. In other words, is there some type of measurement that automatically winnows out the information from a signal? Incredibly, the answer is sometimes yes.

*Compressive sampling* refers to the idea that, for certain types of signals, a small number of nonadaptive samples carries sufficient information to approximate the signal well. Research in this area has two major components:

The iteration invariant, Theorem 2.1. ‣ 2.3. Performance Guarantees ‣ 2. The CoSaMP Algorithm ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), states that if the error is large then CoSaMP makes substantial progress. This approach to the overall analysis echoes the analysis of other greedy iterative algorithms, including the Fourier sampling method and HHS Pursuit.

Finally, mixed-norm error bounds, such as that in Theorem A. ‣ 1.2. Signal Recovery Algorithms ‣ 1. Introduction ‣ CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples"), have become an important feature of the compressive sampling literature. This idea appears in the work of Candès--Romberg--Tao on convex relaxation; it is used in the analysis of HHS pursuit; it also plays a role in the theoretical treatment of Cohen--Dahmen--DeVore.

Suppose $\mathbf{\Phi}$ has restricted isometry constant $\delta_{r}$. Let $T$ be a set of indices, and let $\mathbf{x}$ be a vector. Provided that $r \geq \left| {T \cup {{supp}{(\mathbf{x})}}} \right|$,

CoSaMP was designed to be a practical method for signal recovery. An efficient implementation of the algorithm requires some ideas from numerical linear algebra, as well as some basic techniques from the theory of algorithms. This section discusses the key issues and develops an analysis of the running time for the two most common scenarios.

Let $T$ be a set of at most $3s$ indices, and define the least-squares signal estimate $\mathbf{b}$ by the formulae
