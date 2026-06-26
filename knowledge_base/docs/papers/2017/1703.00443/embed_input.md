<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OptNet: Differentiable Optimization as a Layer in Neural Networks

Topics include Neural networks, Convolutional networks, Optimization, OptNet, ENCODE, Optimization problem.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents OptNet, a network architecture that integrates optimization problems (here, specifically in the form of quadratic programs) as individual layers in larger end-to-end trainable deep networks. These layers encode constraints and complex dependencies between the hidden states that traditional convolutional and fully-connected layers often cannot capture. We explore the foundations for such an architecture: we show how techniques from sensitivity analysis, bilevel optimization, and implicit differentiation can be used to exactly differentiate through these layers and with respect to layer parameters; we develop a highly efficient solver for these layers that exploits fast GPU-based batch solves within a primal-dual interior point method, and which provides backpropagation gradients with virtually no additional cost on top of the solve; and we highlight the application of these approaches in several problems. In one notable example, the method is learns to play mini-Sudoku (4x4) given just input and output games, with no a-priori information about the rules of the game; this highlights the ability of OptNet to learn hard constraints better than other neural architectures.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we consider how to treat exact, constrained optimization as an individual layer within a deep learning architecture. Unlike traditional feedforward networks, where the output of each layer is a relatively simple (though non-linear) function of the previous layer, our optimization framework allows for individual layers to capture much richer behavior, expressing complex operations that in total can reduce the overall depth of the network while preserving richness of representation. Specifically, we build a framework where the output of the $i + 1$th layer in a network is the *solution* to a constrained optimization problem based upon previous layers. This framework naturally encompasses a wide variety of inference problems expressed within a neural network, allowing for the potential of much richer end-to-end training for complex tasks that require such inference procedures.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Concretely, in this paper we specifically consider the task of solving small quadratic programs as individual layers. These optimization problems are well-suited to capturing interesting behavior and can be efficiently solved with GPUs. Specifically, we consider layers of the form where $z$ is the optimization variable, $Q{(z_{i})}$, $q{(z_{i})}$, $A{(z_{i})}$, $b{(z_{i})}$, $G{(z_{i})}$, and $h{(z_{i})}$ are parameters of the optimization problem. As the notation suggests, these parameters can depend in any differentiable way on the previous layer $z_{i}$, and which can eventually be optimized just like any other weights in a neural network. These layers can be learned by taking the gradients of some loss function with respect to the parameters. In this paper, we derive the gradients of by taking matrix differentials of the KKT conditions of the optimization problem at its solution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to the make the approach practical for larger networks, we develop a custom solver which can simultaneously solve multiple small QPs in batch form. We do so by developing a custom primal-dual interior point method tailored specifically to dense batch operations on a GPU. In total, the solver can solve batches of quadratic programs over 100 times faster than existing highly tuned quadratic programming solvers such as Gurobi and CPLEX. One crucial algorithmic insight in the solver is that by using a specific factorization of the primal-dual interior point update, we can obtain a backward pass over the optimization layer virtually "for free" (i.e., requiring no additional factorization once the optimization problem itself has been solved). Together, these innovations enable parameterized optimization problems to be inserted within the architecture of existing deep networks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We begin by highlighting background and related work, and then present our optimization layer. Using matrix differentials we derive rules for computing the backpropagation updates. We then present our solver for these quadratic programs, based upon a state-of-the-art primal-dual interior point method, and highlight the novel elements as they apply to our formulation, such as the aforementioned fact that we can compute backpropagation at very little additional cost. We then provide experimental results that demonstrate the capabilities of the architecture, highlighting potential tasks that these architectures can solve, and illustrating improvements upon existing approaches.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Energy-based learning methods", "weight": 1.0} -->

These methods can be used for tasks like (structured) prediction where the training method shapes the energy function to be low around the observed data manifold and high elsewhere. In recent years, there has been a strong push to further incorporate structured prediction methods like conditional random fields as the "last layer" of a deep network architecture as well as in deeper energy-based architectures. Learning in this context requires observed data, which isn't present in some of the contexts we consider in this paper, and also may suffer from instability issues when combined with deep energy-based architectures as observed in Belanger & McCallum; Belanger et al.; Amos et al..

<!-- chunk {"id": "body-0008", "role": "body", "section": "Analytically", "weight": 1.0} -->

If an analytic solution to the argmin can be found, such as in an unconstrained quadratic minimization, the gradients can often also be computed analytically. This is done in Tappen et al.; Schmidt & Roth. We cannot use these methods for the constrained optimization problems we consider in this paper because there are no known analytic solutions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Unrolling", "weight": 1.0} -->

The argmin operation over an unconstrained objective can be approximated by a first-order gradient-based method and unrolled. These architectures typically introduce an optimization procedure such as gradient descent into the inference procedure. This is done in Domke; Amos et al.; Belanger et al.; Metz et al.; Goodfellow et al.; Stoyanov et al.; Brakel et al.. The optimization procedure is unrolled automatically or manually to obtain derivatives during training that incorporate the effects of these in-the-loop optimization procedures. However, unrolling the computation of a method like gradient descent typically requires a substantially larger network, and adds substantially to the network's computational complexity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Unrolling", "weight": 1.0} -->

In all of these existing cases, the optimization problem is unconstrained and unrolling gradient descent is often easy to do. When constraints are added to the optimization problem, iterative algorithms often use a projection operator that may be difficult to unroll through. In this paper, we do not unroll an optimization procedure but instead use argmin differentiation as described in the next section.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Argmin differentiation", "weight": 1.0} -->

Most closely related to our own work, there have been several papers that propose some form of differentiation through argmin operators. These techniques also come up in bilevel optimization and sensitivity analysis. In the case of Gould et al., the authors describe general techniques for differentiation through optimization problems, but only describe the case of exact equality constraints rather than both equality and inequality constraints (in the case inequality constraints, they add these via a barrier function). Amos et al. considers argmin differentiation within the context of a specific optimization problem (the bundle method) but does not consider a general setting. Johnson et al. performs implicit differentiation on (multi-)convex objectives with coordinate subspace constraints, but don't consider inequality constraints and don't consider in detail general linear equality constraints. Their optimization problem is only in the final layer of a variational inference network while we propose to insert optimization problems anywhere in the network. Therefore a special case of OptNet layers (with no inequality constraints) has a natural interpretation in terms of Gaussian inference, and so Gaussian graphical models (or CRF ideas more generally) provide tools for making the computation more efficient and interpreting or constraining its structure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Argmin differentiation", "weight": 1.0} -->

Similarly, the older work of Mairal et al. considered argmin differentiation for a LASSO problem, deriving specific rules for this case, and presenting an efficient algorithm based upon our ability to solve the LASSO problem efficiently.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Argmin differentiation", "weight": 1.0} -->

In this paper, we use implicit differentiation and techniques from matrix differential calculus to derive the gradients from the KKT matrix of the problem. A notable difference from other work within ML that we are aware of, is that we analytically differentiate through inequality as well as just equality constraints by differentiating the complementarity conditions; this differs from e.g., Gould et al. where they instead approximately convert the problem to an unconstrained one via a barrier method. We have also developed methods to make this approach practical and reasonably scalable within the context of deep architectures.

<!-- chunk {"id": "body-0014", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

Although in the most general form, an OptNet layer can be any optimization problem, in this paper we will study OptNet layers defined by a quadratic program where $z \in {\mathbb{R}}^{n}$ is our optimization variable $Q \in {\mathbb{R}}^{n \times n} \succeq 0$ (a positive semidefinite matrix), $q \in {\mathbb{R}}^{n}$, $A \in {\mathbb{R}}^{m \times n}$, $b \in {\mathbb{R}}^{m}$, $G \in {\mathbb{R}}^{p \times n}$ and $h \in {\mathbb{R}}^{p}$ are problem data, and leaving out the dependence on the previous layer $z_{i}$ as we showed in for notational convenience.

<!-- chunk {"id": "body-0015", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

As is well-known, these problems can be solved in polynomial time using a variety of methods; if one desires exact (to numerical precision) solutions to these problems, then primal-dual interior point methods, as we will use in a later section, are the current state of the art in solution methods. In the neural network setting, the *optimal solution* (or more generally, a *subset of the optimal solution*) of this optimization problems becomes the output of our layer, denoted $z_{i + 1}$, and any of the problem data $Q,q,A,b,G,h$ can depend on the value of the previous layer $z_{i}$. The forward pass in our OptNet architecture thus involves simply setting up and finding the solution to this optimization problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

Training deep architectures, however, requires that we not just have a forward pass in our network but also a backward pass. This requires that we compute the derivative of the solution to the QP with respect to its input parameters, a general topic we topic we discussed previously. To obtain these derivatives, we differentiate the KKT conditions (sufficient and necessary conditions for optimality) of at a solution to the problem using techniques from matrix differential calculus. Our analysis here can be extended to more general convex optimization problems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

The Lagrangian of is given by where $\nu$ are the dual variables on the equality constraints and $\lambda \geq 0$ are the dual variables on the inequality constraints. The KKT conditions for stationarity, primal feasibility, and complementary slackness are where $D{(\cdot)}$ creates a diagonal matrix from a vector and $z^{\star}$, $\nu^{\star}$ and $\lambda^{\star}$ are the optimal primal and dual variables. Taking the differentials of these conditions gives the equations or written more compactly in matrix form Using these equations, we can form the Jacobians of $z^{\star}$ (or $\lambda^{\star}$ and $\nu^{\star}$, though we don't consider this case here), with respect to any of the data parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

For example, if we wished to compute the Jacobian $\frac{\partial z^{\star}}{\partial b} \in {\mathbb{R}}^{n \times m}$, we would simply substitute ${\mathsf{d}b} = I$ (and set all other differential terms in the right hand side to zero), solve the equation, and the resulting value of $\mathsf{d}z$ would be the desired Jacobian.

<!-- chunk {"id": "body-0019", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

In the backpropagation algorithm, however, we never want to explicitly form the actual Jacobian matrices, but rather want to form the left matrix-vector product with some previous backward pass vector $\frac{\partial\ell}{\partial z^{\star}} \in {\mathbb{R}}^{n}$, i.e., $\frac{\partial\ell}{\partial z^{\star}}\frac{\partial z^{\star}}{\partial b}$. We can do this efficiently by noting the solution for the $({\mathsf{d}z},{\mathsf{d}\lambda},{\mathsf{d}\nu})$ involves multiplying the *inverse* of the left-hand-side matrix in by some right hand side.

<!-- chunk {"id": "body-0020", "role": "body", "section": "OptNet: solving optimization within a neural network", "weight": 1.0} -->

Thus, if we multiply the backward pass vector by the transpose of the differential matrix then the relevant gradients with respect to all the QP parameters can be given by | | $\nabla_{G}\ell$ | $= {{D{(\lambda^{\star})}d_{\lambda}z^{\star T}} + {\lambda^{\star}d_{z}^{T}}}$ | $\nabla_{h}\ell$ | $= {- {D{(\lambda^{\star})}d_{\lambda}}}$ | | | where as in standard backpropagation, all these terms are at most the size of the parameter matrices. Some of these parameters should depend on the previous layer $z_{i}$ and the gradients with respect to the previous layer can be obtained through the chain rule. In the next section, we show that the solution to an interior point method provides a factorization we can use to compute these gradient efficiently.

<!-- chunk {"id": "body-0021", "role": "body", "section": "An efficient batched QP solver", "weight": 1.0} -->

Deep networks are typically trained in mini-batches to take advantage of efficient data-parallel GPU operations. Without mini-batching on the GPU, many modern deep learning architectures become intractable for all practical purposes. However, today's state-of-the-art QP solvers like Gurobi and CPLEX do not have the capability of solving multiple optimization problems on the GPU in parallel across the entire minibatch. This makes larger OptNet layers become quickly intractable compared to a fully-connected layer with the same number of parameters.

<!-- chunk {"id": "body-0022", "role": "body", "section": "An efficient batched QP solver", "weight": 1.0} -->

To overcome this performance bottleneck in our quadratic program, we implemented a GPU-based primal-dual interior point method (PDIPM) based on Mattingley & Boyd that solves a batch of quadratic programs, and which provides the necessary gradients needed to train these in an end-to-end fashion. Our performance experiments in Section 4.1 shows that our solver is significantly faster than the standard non-batch solvers Gurobi and CPLEX.

<!-- chunk {"id": "body-0023", "role": "body", "section": "An efficient batched QP solver", "weight": 1.0} -->

Following the method of Mattingley & Boyd, our solver introduces slack variables on the inequality constraints and iteratively minimizes the residuals from the KKT conditions over the primal variable $z \in {\mathbb{R}}^{n}$, slack variable $s \in {\mathbb{R}}^{p}$, and dual variables $\nu \in {\mathbb{R}}^{m}$ associated with the equality constraints and $\lambda \in {\mathbb{R}}^{p}$ associated with the inequality constraints. Each iteration computes the affine scaling directions by solving then centering-plus-corrector directions by solving where $\mu = {{s^{T}\lambda}/p}$ is the duality gap and $\sigma$ is defined in Mattingley & Boyd. Each variable $v$ is updated with ${\Deltav} = {{\Deltav^{aff}} + {\Deltav^{cc}}}$ using an appropriate step size.

<!-- chunk {"id": "body-0024", "role": "body", "section": "An efficient batched QP solver", "weight": 1.0} -->

We actually solve a symmetrized version of the KKT conditions, obtained by scaling the second row block by $D{({1/s})}$. We analytically decompose these systems into smaller symmetric systems and pre-factorize portions of them that don't change (i.e. that don't involve $D{({\lambda/s})}$ between iterations). We have implemented a batched version of this method with the PyTorch library^22^2 and have released it as an open source library at It uses a custom CUBLAS extension to compute batch matrix factorizations and solves in parallel and provides the necessary derivatives for end-to-end learning.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Efficiently computing gradients", "weight": 1.0} -->

The backward pass gradients can be computed "for free" after solving the original QP with this primal-dual interior point method, without an additional matrix factorization or solve. Each iteration cmputes an LU decomposition of the matrix $K_{sym}$,^33^3We perform an LU decomposition of a subset of the matrix formed by eliminating variables to create only a $p \times p$ matrix (the number of inequality constraints) that needs to be factor during each iteration of the primal-dual algorithm, and one $m \times m$ and one $n \times n$ matrix once at the start of the primal-dual algorithm, though we omit the detail here. We also use an LU decomposition as this routine is provided in batch form by CUBLAS, but could potentially use a (faster) Cholesky factorization if and when the appropriate functionality is added to CUBLAS). which is a symmetrized version of the matrix needed for computing the backpropagated gradients.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Efficiently computing gradients", "weight": 1.0} -->

We compute the $d_{z,\lambda,\nu}$ terms by solving the linear system where ${\overset{\sim}{d}}_{\lambda} = {D{(\lambda^{\star})}d_{\lambda}}$ for $d_{\lambda}$ as defined. Thus, all the backward pass gradients can be computed using the factored KKT matrix at the solution. Crucially, because the bottleneck of solving this linear system is computing the factorization of the KKT matrix (cubic time as opposed to the quadratic time for solving via backsubstitution once the factorization is computed), the additional time requirements for computing all the necessary gradients in the backward pass is virtually nonexistent compared with the time of computing the solution. To the best of our knowledge, this is the first time that this fact has been exploited in the context of learning end-to-end systems.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Properties and representational power", "weight": 1.0} -->

In this section we briefly highlight some of the mathematical properties of OptNet layers. The proofs here are straightforward, and are mostly based upon well-known results in convex analysis, so are deferred to the appendix. The first result simply highlights that (because the solution of strictly convex QPs is continuous), that OptNet layers are subdifferentiable everywhere, and differentiable at all but a measure-zero set of points.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Limitations of the method", "weight": 1.5} -->

Although, as we will show shortly, the OptNet layer has several strong points, we also want to highlight the potential drawbacks of this approach. First, although, with an efficient batch solver, integrating an OptNet layer into existing deep learning architectures is potentially practical, we do note that solving optimization problems exactly as we do here has has cubic complexity in the number of variables and/or constraints. This contrasts with the quadratic complexity of standard feedforward layers. This means that we *are* ultimately limited to settings where the number of hidden variables in an OptNet layer is not too large (less than 1000 dimensions seems to be the limits of what we currently find to the be practical, and substantially less if one wants real-time results for an architecture).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Limitations of the method", "weight": 1.5} -->

Secondly, there are many improvements to the OptNet layers that are still possible. Our QP solver, for instance, uses fully dense matrix operations, which makes the solves very efficient for GPU solutions, and which also makes sense for our general setting where the coefficients of the quadratic problem can be learned. However, for setting many real-world optimization problems (and hence for architectures that wish to more closely mimic some real-world optimization problem), there is often substantial structure (e.g., sparsity), in the data matrices that can be exploited for efficiency. There is of course no prohibition of incorporating sparse matrix methods into the fast custom solver, but doing so would require substantial added complexity, especially regarding efforts like finding minimum fill orderings for different sparsity patterns of the KKT systems. In our solver `qpth`, we have started experimenting with cuSOLVER's batched sparse QR factorizations and solves.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Limitations of the method", "weight": 1.5} -->

Lastly, we note that while the OptNet layers can be trained just as any neural network layer, since they are a new creation and since they have manifolds in the parameter space which have no effect on the resulting solution (e.g., scaling the rows of a constraint matrix and its right hand side does not change the optimization problem), there is admittedly more tuning required to get these to work. This situation is common when developing new neural network architectures and has also been reported in the similar architecture of Schmidt & Roth. Our hope is that techniques for overcoming some of the challenges in learning these layers will continue to be developed in future work.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental results", "weight": 1.0} -->

In this section, we present several experimental results that highlight the capabilities of the QP OptNet layer. Specifically we look at 1) computational efficiency over exiting solvers; 2) the ability to improve upon existing convex problems such as those used in signal denoising; 3) integrating the architecture into an generic deep learning architectures; and 4) performance of our approach on a problem that is challenging for current approaches. In particular, we want to emphasize the results of our system on learning the game of (4x4) mini-Sudoku, a well-known logical puzzle; our layer is able to directly learn the necessary constraints using just gradient information and no a priori knowledge of the rules of Sudoku. The code and data for our experiments are open sourced in the `icml2017` branch of and our batched QP solver is available as a library at

<!-- chunk {"id": "body-0032", "role": "body", "section": "Batch QP solver performance", "weight": 1.0} -->

All of the OptNet performance results in this section are run on an unloaded Titan X GPU. Gurobi is run on an unloaded quad-core Intel Core i7-5960X CPU @ 3.00GHz.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Batch QP solver performance", "weight": 1.0} -->

Our OptNet layers are much more computationally expensive than a linear or convolutional layer and a natural question is to ask what the performance difference is. We set up an experiment comparing a linear layer to a QP OptNet layer with a mini-batch size of 128 on CUDA with randomly generated input vectors sized 10, 50, 100, and 500. Each layer maps this input to an output of the same dimension; the linear layer does this with a batched matrix-vector multiplication and the OptNet layer does this by taking the argmin of a random QP that has the same number of inequality constraints as the dimensionality of the problem. Figure 1 shows the profiling results (averaged over 10 trials) of the forward and backward passes. The OptNet layer is significantly slower than the linear layer as expected, yet still tractable in many practical contexts.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Batch QP solver performance", "weight": 1.0} -->

Our next experiment illustrates why standard baseline QP solvers like CPLEX and Gurobi without batch support are too computationally expensive for QP OptNet layers to be tractable. We set up random QP of the form that have 100 variables and 100 inequality constraints in Gurobi and in the serialized and batched versions of our solver `qpth` and vary the batch size.^44^4Experimental details: we sample entries of a matrix $U$ from a random uniform distribution and set $Q = {{U^{T}U} + {10^{- 3}I}}$, sample $G$ with random normal entries, and set $h$ by selecting generating some $z_{0}$ random normal and $s_{0}$ random uniform and setting $h = {{Gz_{0}} + s_{0}}$ (we didn't include equality constraints just for simplicity, and since the number of inequality constraints in the primary driver of complexity for the iterations in a primal-dual interior point method). The choice of $h$ guarantees the problem is feasible.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Total variation denoising", "weight": 1.0} -->

Our next experiment studies how we can use the OptNet architecture to *improve* upon signal processing techniques that currently use convex optimization as a basis. Specifically, our goal in this case is to denoise a noisy 1D signal given training data consistency of noisy and clean signals generated from the same distribution. Such problems are often addressed by convex optimization procedures, and (1D) total variation denoising is a particularly common and simple approach. Specifically, the total variation denoising approach attempts to smooth some noisy observed signal $y$ by solving the optimization problem where $D$ is the first-order differencing operation expressed in matrix form with rows $D_{i} = {e_{i} - e_{i + 1}}$. Penalizing the $\ell_{1}$ norm of the signal *difference* encourages this difference to be sparse, i.e., the number of changepoints of the signal is small, and we end up approximating $y$ by a (roughly) piecewise constant function.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Total variation denoising", "weight": 1.0} -->

To test this approach and competing ones on a denoising task, we generate piecewise constant signals (which are the desired outputs of the learning algorithm) and corrupt them with independent Gaussian noise (which form the inputs to the learning algorithm). Table 1 shows the error rate of these four approaches.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Baseline: Total variation denoising", "weight": 1.0} -->

To establish a baseline for denoising performance with total variation, we run the above optimization problem varying values of $\lambda$ between 0 and 100. The procedure performs best with a choice of $\lambda \approx 13$, and achieves a minimum test MSE on our task of about 16.5 (the units here are unimportant, the only relevant quantity is the relative performances of the different algorithms).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Baseline: Learning with a fully-connected neural network", "weight": 1.0} -->

An alternative approach to denoising is by learning from data. A function $f_{\theta}{(x)}$ parameterized by $\theta$ can be used to predict the original signal. The optimal $\theta$ can be learned by using the mean squared error between the true and predicted signals. Denoising is typically a difficult function to learn and Table 1 shows that a fully-connected neural network perform substantially worse on this denoising task than the convex optimization problem. Section B shows the convergence of the fully-connected network.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning the differencing operator", "weight": 1.0} -->

Between the feedforward neural network approach and the convex total variation optimization, we could instead use a generic OptNet layers that effectively allowed us to solve using *any* denoising matrix, which we randomly initialize. While the accuracy here is substantially lower than even the fully connected case, this is largely the result of learning an over-regularized solution to $D$. This is indeed a point that should be addressed in future work (we refer back to our comments in the previous section on the potential challenges of training these layers), but the point we want to highlight here is that the OptNet layer seems to be learning something very interpretable and understandable. Specifically, Figure 3 shows the $D$ matrix of our solution before and after learning (we permute the rows to make them ordered by the magnitude of where the large-absolute-value entries occurs). What is interesting in this picture is that the learned $D$ matrix typically captures exactly the same intuition as the $D$ matrix used by total variation denoising: a mainly sparse matrix with a few entries of alternating sign next to each other.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning the differencing operator", "weight": 1.0} -->

This implies that for the data set we have, total variation denoising is indeed the "right" way to think about denoising the resulting signal, but if some other noise process were to generate the data, then we can learn that process instead. We can then attain lower actual error for the method (in this case similar though slightly higher than the TV solution), by fixing the learned sparsity of the $D$ matrix and then fine tuning.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Fine-tuning and improving the total variation solution", "weight": 1.0} -->

To finally highlight the ability of the OptNet methods to *improve* upon the results of a convex program, specifically tailoring to the data. Here, we use the same OptNet architecture as in the previous subsection, but initialize $D$ to be the differencing matrix as in the total variation solution. As shown in Table 1, the procedure is able to improve both the training and testing MSE over the TV solution, specifically improving upon test MSE by 12%. Section B shows the convergence of fine-tuning.

<!-- chunk {"id": "body-0042", "role": "body", "section": "MNIST", "weight": 1.0} -->

One compelling use case of an OptNet layer is to learn constraints and dependencies over the output or latent space of a model. As a simple example to illustrate that OptNet layers can be included in existing architectures and that the gradients can be efficiently propagated through the layer, we show the performance of a fully-connected feedforward network with and without an OptNet layer in Section A in the supplemental material.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Sudoku", "weight": 1.0} -->

Finally, we present the main illustrative example of the representational power of our approach, the task of learning the game of Sudoku. Sudoku is a popular logical puzzle, where a (typically 9x9) grid of points must be arranged given some initial point, so that each row, each column, and each 3x3 grid of points must contain one of each number 1 through 9. We consider the simpler case of 4x4 Sudoku puzzles, with numbers 1 through 4, as shown in Figure 4.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sudoku", "weight": 1.0} -->

Sudoku is fundamentally a constraint satisfaction problem, and is trivial for computers to solve when told the rules of the game. However, if we do not know the rules of the game, but are only presented with examples of unsolved and the corresponding solved puzzle, this is a challenging task. We consider this to be an interesting benchmark task for algorithms that seek to capture complex strict relationships between all input and output variables. The input to the algorithm consists of a 4x4 grid (really a 4x4x4 tensor with a one-hot encoding for known entries an all zeros for unknown entries), and the desired output is a 4x4x4 tensor of the one-hot encoding of the solution.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Sudoku", "weight": 1.0} -->

This is a problem where traditional neural networks have difficulties learning the necessary hard constraints. As a baseline inspired by the models at we implemented a multilayer feedforward network to attempt to solve Sudoku problems. Specifically, we report results for a network that has 10 convolutional layers with 512 3x3 filters each, and tried other architectures as well. The OptNet layer we use on this task is a completely generic QP in "standard form" with only positivity inequality constraints but an arbitrary constraint matrix ${Ax} = b$, a small $Q = {0.1I}$ to make sure the problem is strictly feasible, and with the linear term $q$ simply being the input one-hot encoding of the Sudoku problem. We know that Sudoku *can* be approximated well with a linear program (indeed, integer programming is a typical solution method for such problems), but the model here is told nothing about the rules of Sudoku.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Sudoku", "weight": 1.0} -->

We trained these models using ADAM to minimize the MSE (which we refer to as "loss") on a dataset we created consisting of 9000 training puzzles, and we then tested the models on 1000 different held-out puzzles. The error rate is the percentage of puzzles solved correctly if the cells are assigned to whichever index is largest in the prediction. Figure 5 shows that the convolutional is able to learn all of the necessary logic for the task and ends up over-fitting to the training data. We contrast this with the performance of the OptNet network, which learns most of the correct hard constraints and is able to generalize much better to unseen examples.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented OptNet, a neural network architecture where we use optimization problems as a single layer in the network. We have derived the algorithmic formulation for differentiating through these layers, allowing for backpropagating in end-to-end architectures. We have also developed an efficient batch solver for these optimizations based upon a primal-dual interior point method, and developed a method for attaining the necessary gradient information "for free" from this approach. Our experiments highlight the potential power of these networks, showing that they can solve problems where existing networks are very poorly suited, such as learning Sudoku problems purely from data. These models add another important primitive to the toolbox of neural network practitioners and enable many possible future directions of research of differentiating through optimization problems.
