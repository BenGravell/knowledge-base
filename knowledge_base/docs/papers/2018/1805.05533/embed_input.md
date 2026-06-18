Discovering Transforms: A Tutorial on Circulant Matrices, Circular Convolution, and the Discrete Fourier Transform

Topics include Transforms, DFT, Discrete fourier transform, Fourier transform.

How could the Fourier and other transforms be naturally discovered if one didn't know how to postulate them? In the case of the Discrete Fourier Transform (DFT), we show how it arises naturally out of analysis of circulant matrices. In particular, the DFT can be derived as the change of basis that simultaneously diagonalizes all circulant matrices. In this way, the DFT arises naturally from a linear algebra question about a set of matrices. Rather than thinking of the DFT as a signal transform, it is more natural to think of it as a single change of basis that renders an entire set of mutually-commuting matrices into simple, diagonal forms. The DFT can then be "discovered" by solving the eigenvalue/eigenvector problem for a special element in that set. A brief outline is given of how this line of thinking can be generalized to families of linear operators, leading to the discovery of the other common Fourier-type transforms, as well as its connections with group representations theory.

## Introduction

The Fourier transform in all its forms is ubiquitous. Its many useful properties are introduced early on in Mathematics, Science and Engineering curricula. Typically, it is introduced as a transformation on functions or signals, and then its many useful properties are easily derived. Those properties are then shown to be remarkably effective in solving certain differential equations, or in analyzing the action of time-invariant linear dynamical systems, amongst many other uses.

The above question is interesting for several reasons. First, it is more intellectually satisfying to introduce a new mathematical object from familiar and well-known objects rather than having it postulated "out of thin air". In this tutorial we demonstrate how the DFT arises naturally from the problem of simultaneous diagonalization of all circulant matrices, which share symmetry properties that enable this diagonalization.

To make the point above, and to have a concrete discussion, in this tutorial we consider primarily the case of circulant matrices. This case is also particularly useful because it yields the DFT, which is the computational workhorse for all Fourier-type analysis. Given an $n$-vector $a:={(a_{0},\ldots,a_{n - 1})}$, define the associated matrix $C_{a}$ whose first column is made up of these numbers, and each subsequent column is obtained by a circular shift of the previous column

Note that each row is also obtained from the pervious row by a circular shift. Thus the entire matrix is completely determined by any one of its rows or columns. Such matrices are called circulant. They are a subclass of Toeplitz matrices, and as mentioned, have very special properties due to their intimate relation to the Discrete Fourier Transform (DFT) and circular convolution.
