Enhancing Sparsity by Reweighted L1 Minimization

Topics include Compressed sensing, Sparse recovery, Reweighted L1, Convex optimization, Iterative reweighting, Signal reconstruction.

Proposes solving a sequence of weighted L1 problems to better approximate sparsity than a single unweighted relaxation. The simple iterative reweighting rule often recovers sparse signals from fewer measurements and became a standard heuristic in compressed sensing and sparse modeling.

It is now well understood that it is possible to reconstruct sparse signals exactly from what appear to be highly incomplete sets of linear measurements and that this can be done by constrained L1 minimization. In this paper, we study a novel method for sparse signal recovery that in many situations outperforms L1 minimization in the sense that substantially fewer measurements are needed for exact recovery. The algorithm consists of solving a sequence of weighted L1-minimization problems where the weights used for the next iteration are computed from the value of the current solution. We present a series of experiments demonstrating the remarkable performance and broad applicability of this algorithm in the areas of sparse signal recovery, statistical estimation, error correction and image processing. Interestingly, superior gains are also achieved when our method is applied to recover signals with assumed near-sparsity in overcomplete representations - not by reweighting the L1 norm of the coefficient sequence as is common, but by reweighting the L1 norm of the transformed object....

## Introduction

What makes some scientific or engineering problems at once interesting and challenging is that often, one has fewer equations than unknowns. When the equations are linear, one would like to determine an object $x_{0} \in {\mathbb{R}}^{n}$ from data $y = {\Phix_{0}}$, where $\Phi$ is an $m \times n$ matrix with fewer rows than columns; i.e., $m < n$. The problem is of course that a system with fewer equations than unknowns usually has infinitely many solutions and thus, it is apparently impossible to identify which of these candidate solutions is indeed the "correct" one without some additional information.

In many instances, however, the object we wish to recover is known to be structured in the sense that it is sparse or compressible. This means that the unknown object depends upon a smaller number of unknown parameters. In a biological experiment, one could measure changes of expression in 30,000 genes and expect at most a couple hundred genes with a different expression level. In signal processing, one could sample or sense signals which are known to be sparse (or approximately so) when expressed in the correct basis....

We mentioned the use of other functionals and reweighting rules. How do they compare?

Finally, any result quantifying the improvement of the reweighted algorithm for special classes of sparse or nearly sparse signals would be significant.

Again $\delta$ is a parameter making sure that the true unknown vector is feasible with high probability.

### Historical progression

Solve the weighted TV minimization problem

Mathematically speaking and under sparsity assumptions, one would want to recover a signal $x_{0} \in {\mathbb{R}}^{n}$, e.g., the coefficient sequence of the signal in the appropriate basis, by solving the combinatorial optimization problem

where ${\| x\|}_{\ell_{0}} = {|{\{ i:{x_{i} \neq 0}\}}|}$. This is a common sense approach which simply seeks the simplest explanation fitting the data. In fact, this method can recover sparse solutions even in situations in which $m \ll n$. Suppose for example that all sets of $m$ columns of $\Phi$ are in general position. Then the program ($P_{0})$ perfectly recovers all sparse signals $x_{0}$ obeying ${\| x_{0}\|}_{\ell_{0}} \leq {m/2}$....
