CoSaMP: Iterative Signal Recovery from Incomplete and Inaccurate Samples

Topics include Compressed sensing, Sparse recovery, Greedy algorithms, Signal reconstruction, CoSaMP, Error bounds.

Introduces CoSaMP, a greedy sparse-recovery algorithm with provable accuracy, stability, and runtime guarantees under standard compressed-sensing assumptions. It combines matching-pursuit style support identification with least-squares refinement and pruning.

Compressive sampling offers a new paradigm for acquiring signals that are compressible with respect to an orthonormal basis. The major algorithmic challenge in compressive sampling is to approximate a compressible signal from noisy samples. This paper describes a new iterative recovery algorithm called CoSaMP that delivers the same guarantees as the best optimization-based approaches. Moreover, this algorithm offers rigorous bounds on computational cost and storage. It is likely to be extremely efficient for practical problems because it requires only matrix-vector multiplies with the sampling matrix. For many cases of interest, the running time is just O(N*log^2(N)), where N is the length of the signal.

## Introduction

Most signals of interest contain scant information relative to their ambient dimension, but the classical approach to signal acquisition ignores this fact. We usually collect a complete representation of the target signal and process this representation to sieve out the actionable information. Then we discard the rest. Contemplating this ugly inefficiency, one might ask if it is possible instead to acquire *compressive samples*. In other words, is there some type of measurement that automatically winnows out the information from a signal? Incredibly, the answer is sometimes yes.

*Compressive sampling* refers to the idea that, for certain types of signals, a small number of nonadaptive samples carries sufficient information to approximate the signal well.

: How many samples are necessary to reconstruct signals to a specified precision? What type of samples? How can these sampling schemes be implemented in practice?

: Given the compressive samples, what algorithms can efficiently construct a signal approximation?

This paper presents and analyzes a novel signal reconstruction algorithm that achieves these desiderata. The algorithm is called CoSaMP, from the acrostic *Compressive Sampling Matching Pursuit*. As the name suggests, the new method is ultimately based on orthogonal matching pursuit (OMP), but it incorporates several other ideas from the literature to accelerate the algorithm and to provide strong guarantees that OMP cannot. Before we describe the algorithm, let us deliver an introduction to the theory of compressive sampling.

## Discussion and Related Work

CoSaMP draws on both algorithmic ideas and analytic techniques that have appeared before. This section describes the other major signal recovery algorithms, and it compares them with CoSaMP. It also attempts to trace the key ideas in the algorithm back to their sources.
