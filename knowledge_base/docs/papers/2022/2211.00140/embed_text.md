<!-- arxiv-full-text:v1 {"arxiv_id": "2211.00140", "source": "arxiv-pdf"} -->

## Introduction

Second-order optimization methods are the backbone of much of industrial and scientific computing. With origins that can be tracked back several centuries to the pioneering works of Newton [Newton, 1687], Raphson [Raphson, 1697] and Simpson [Simpson, 1740], they were extensively studied, generalized, modified, and improved in the last century [Kantorovich, 1948, Moré, 1978, Griewank, 1981a]. For a review of the historical development of the classical Newton-Raphson method, we refer the reader to the work of Ypma. The number of extensions and applications of second-order optimization methods is enormous; for example, the survey of Conn et al. on trust-region and quasi-Newton methods cited over a thousand papers.

## Second-order methods and modern machine learning

Despite the rich history of the field, research on second-order methods has been flourishing up to this day. Some of the most recent development in the area was motivated by the needs of modern machine learning. Data-oriented machine learning depends on large datasets (both in number of features and number of datapoints), which are often stored in distributed/decentalized fashion. Consequently, there is a need for scalable algorithms.

† Mohamed bin Zayed University of Artificial Intelligence, United Arab Emirates ‡ King Abdullah University of Science and Technology, Thuwal, Saudi Arabia § Moscow Institute of Physics and Technology, Russia ¶ ISP RAS Research Center for Trusted Artificial Intelligence, Russia | | National Research University Higher School of Economics, Russia takac.MT@gmail.com To tackle large number of features, Qu et al., Gower et al., Doikov and Richtárik and Hanzely et al. proposed variants of Newton method operating in random low-dimensional subspaces. On the other hand, Pilanci and Wainwright, Xu et al. and Kovalev et al. developed subsampled Newton methods for solving empirical risk minimization (ERM) problems with large training datasets. Additionally, Bordes et al., Mokhtari and Ribeiro, Gower et al., Byrd et al. and Kovalev et al. proposed stochastic variants of quasi-Newton methods. To tackle non-centralized nature of datasets, Shamir et al., Reddi et al., Wang et al. and Crane and Roosta considered distributed variants of Newton method, with improvements under various data/function similarity assumptions. Islamov et al., Safaryan et al., Qian et al., Islamov et al. and Agafonov et al. developed communication-efficient distributed variants of Newton method using the idea of communication compression and error compensation, without the need for any similarity assumptions.

We highlight two main research directions throughout of history of second-order methods: globally convergent methods under additional second-order smoothness [Nesterov and Polyak, 2006] and local methods for self-concordant problems [Nesterov and Nemirovski, 1989]. Former approach lead to various improvements such as acceleration Nesterov, Monteiro and Svaiter, usage of inexact information Ghadimi et al., Agafonov et al., generalization to tensor methods and their acceleration Nesterov [2021a], Gasnikov et al., Kovalev and Gasnikov, superfast second-order methods under higher smoothness Nesterov [2021c,b], Kamzolov and Gasnikov. Latter approach was a breakthrough in 1990s, it lead to interior-point methods. Summary of the results can be found in books Nesterov and Nemirovski, Nesterov. This direction is still popular up to this day Dvurechensky and Nesterov, Hildebrand, Doikov and Nesterov [2022b], Nesterov.

As easy-to-scale alternative to second-order methods, first-order algorithms attracted a lot of attention. Many of their aspects have been explored, including strong results in variance reduction (Roux et al.,Gower et al., Johnson and Zhang, Nguyen et al. ), preconditioning Jahani et al., acceleration (Nesterov, d'Aspremont et al. ) distributed/federated computation (Koneˇ cný et al., Chen et al., Berahas et al., Takáˇ c et al., Richtárik and Takáˇ c, Kairouz et al. ), and decentralized computation [Koloskova et al., 2020, Sadiev et al., 2021, Borodich et al., 2021]. However, the convergence of first-order methods always depends on the conditioning of the underlying problem. Improving conditioning is fundamentally impossible without using higher-order information. Removing this conditioning dependence is possible by incorporating information about the Hessian. This results in second-order methods. Their most compelling advantage is that they can converge extremely quickly, usually in just a few iterations.

## Newton method: benefits and limitations

One of the most famous algorithms in optimization, Newton method, takes iterates of form Its iterates satisfy the recursion ‖∇ f (x k +1) ‖ 2 ≤ c ‖∇ f (x k) ‖ 2 2 (for a constant c > 0), which means that Newton method converges locally quadratically. However, convergence of Newton method is limited to only to the neighborhood of the solution. It is well-known that when initialized far from optimum, Newton can diverge, both in theory and practice (Jarre and Toint, Mascarenhas). We can explain intuition why this happens. Update rule of Newton was chosen to minimize right hand side of Taylor approximation The main problem is that Taylor approximation is not an upper bound, and therefore, global convergence of Newton method is not guaranteed.

## Towards a fast globally convergent Newton method

Even though second-order algorithms with superlinear local convergence rates are very common, global convergence guarantees of any form are surprisingly rare. Many papers proposed globalization strategies, essentially all of them require some combination of the following: line-search, trust regions, damping/truncation, regularization. Some popular globalization strategies show non-increase of functional value during the training. However, this turned out to be insufficient for convergence to the optimum. Jarre and Toint, Mascarenhas designed simple functions (strictly convex with compact level sets) so that Newton method with Armijo stepsizes does not converge to the optimum. To this day, virtually all known global convergence guarantees are for regularized Newton methods, which can be written as where λ k ≥ 0. Parameter λ k is also known as Levenberg-Marquardt regularization [Moré, 1978], which was first introduced for a nonlinear least-squares objective. For simplicity, we disregard differences in the objectives for the literature comparison. Motivation behind update is to replace Taylor approximation in by an upper bound. The first method with proven global convergence rate O (k -2) is Cubic Newton method [Nesterov and Polyak, 2006] for function f with Lipschitz-continuous Hessian, Under this condition, one can upper bound of Taylor approximation eq. as Next iterate of Cubic Newton can be written as a minimizer of right hand side of 1 For our newly-proposed algorithm AICN (Algorithm 1), we are using almost identical step 1 2 The difference between the update of Cubic Newton and AICN is that we measure the cubic regularization term in the local Hessian norms. This seemingly negligible perturbation turned out to be of a great significance for two reasons a) model in is affine-invariant, b) surprisingly, the next iterate of lies in the direction of Newton method step and is obtainable without regularizer λ k (AICN just needs to set stepsize α k). We elaborate on both of these points later in the paper.

Cubic Newton method can be equivalently expressed in form with α k = 1 and λ k = L 2 ‖ x k -x k +1 ‖ 2. However, since such λ k depends on x k +1, resulting algorithm requires additional subroutine for solving its subproblem each iteration. Next work showing convergence rate of regularized Newton method [Polyak, 2009] avoided implicit steps by choosing λ k ∝ ‖∇ f ( x k ) ‖ 2. However, this came with a trade-off for slower convergence rate, O ( k -1 / 4 ). Finally, Mishchenko [4/2021] improved upon both of these works by using explicit regularization α k = 1, λ k ∝ √ L 2 ‖∇ f ( x k ) ‖ 2, and proving global rate O ( k -2 ).

## Contributions

## AICN as a damped Newton method

In this work, we investigate global convergence for most basic globalization strategy, stepsized Newton method without any regularizer (λ k = 0). This algorithm is also referred as damped (or truncated) Newton method; it can be written as 1 Where E a d -dimensional Euclidean space, defined in Section 2.3.

2 Function f is L semi -semi-strongly self-concordant (Definition 3). Instead of L semi, we will use its upper bound L est, L est ≥ L semi.

Table 1: A summary of regularized Newton methods with global convergence guarantees. We consider algorithms with updates of form x k +1 = x k -α k ( ∇ 2 f ( x k ) + λ k I ) -1 ∇ f ( x k ). For simplicity of comparison, we disregard differences in objectives and assumptions. We assume L 2 -smoothness of Hessian, L semi-semi-strong self-concordance, convexity (Definition 3), µ -strong convexity locally and bounded level sets. For regularization parameter holds λ k ≥ 0 and stepsize satisfy 0 < α k ≤ 1. We highlight the best know rates in blue.

| Algorithm | Regularizer λ k ∝ | Stepsize α k = | Affine invariant? (alg., ass., rate) | Avoids line search? | Global convergence rate | Local convergence exponent | Reference | Resulting algorithm was investigated in detail as an interior-point method. Nesterov shows quadratic local convergence for stepsizes α 1 def = 1 1+ G 1, α 2 def = 1+ G 1 1+ G 1 + G 2 1, where 34 G 1 def = L sc ‖∇ f (x k) ‖ ∗ x k. Our algorithm AICN is also damped Newton method with stepsize α = -1+ √ 1+2 G G, where 24 G def = L semi ‖∇ f (x k) ‖ ∗ x k. Mentioned stepsizes α 1, α 2, α share two characteristics. Firstly, all of them depends on gradient computed in the dual norm and scaled by a smoothness constant (G 1 or G). Secondly, all of these stepsizes converge to 1 from below (for ˆ α ∈ { α 1, α 2, α } holds 0 < ˆ α ≤ 1 and lim x → x ∗ ˆ α = 1). Our algorithm uses stepsize bigger by orders of magnitude (see Figure 3 in Appendix A for detailed comparison). The main difference between already established stepsizes α 1, α 2 and our stepsize α are resulting global convergence rates. While stepsize α 2 does not lead to a global convergence rate, and α 1 leads to rate O (k -1 / 2), our stepsize α leads to a significantly faster, O (k -2) rate. Our rate matches best known global rates for regularized Newton methods. We manage to achieve these results by carefully choosing assumptions. While rates for α 1 and α 2 follows from standard self-concordance, our assumptions are a consequence of a slightly stronger version of self-concordance. We will discuss this difference in detail later.

We summarize important properties of regularized Newton methods with fast global convergence guarantees and damped Newton methods in Table 1.

3 Function f is L sc-self-concordant (Definition 1).

4 Dual norm ‖∇ f ( x k ) ‖ ∗ x k = 〈 ∇ f ( x k ), ∇ 2 f ( x k ) -1 ∇ f ( x k ) 〉 is defined in Section 2.3.

## Summary of contributions

To summarize novelty in our work, we present a novel algorithm AICN. Our algorithm can be interpreted in two viewpoints a) as a regularized Newton method (version of Cubic Newton method), b) as a damped Newton method. AICN enjoys the best properties of these two worlds:

- Fast global convergence: AICN converges globally with rate O (k -2) (Theorem 2, 4), which matches state-of-the-art global rate for all regularized Newton methods. Furthermore, it is the first such rate for Damped Newton method. - Fast local convergence: In addition to the fast global rate, AICN decreases gradient norms locally in quadratic rate (Theorem 3). This result matches the best-known rates for both regularized Newton algorithms and damped Newton algorithms. - Simplicity: Previous works on Newton regularizations can be viewed as a popular global-convergence fix for the Newton method. We propose an even simpler fix in the form of a stepsize schedule (Section 3). - Implementability: Step of AICN depends on a smoothness constant L semi (Definition 3). Given this constant, next iterate of AICN can be computed directly.

This is improvement over Cubic Newton [Nesterov and Polyak, 2006], which for a given constant L 2 needs to run line-search subroutine each iteration to solve its subproblem.

- Improvement: Avoiding latter subroutine yields theoretical improvements. If we compute matrix inverses naively, iteration cost of AICN is O (d 3) (where d is a dimension of the problem), which is improvement over O (d 3 log ε -1) iteration cost of Cubic Newton [Nesterov and Polyak, 2006]. - Practical performance: We show that in practice, AICN outperforms all algorithms sharing same convergence guarantees: Cubic Newton [Nesterov and Polyak, 2006] and Globally Regularized Newton [Mishchenko, 4/2021] and Doikov and Nesterov [12/2021], and fixed stepsize Damped Newton method (Section 5). - Geometric properties: We analyze AICN under more geometrically natural assumptions. Instead of smoothness, we use a version of self-concordance (Section 3.1), which is invariant to affine transformations and hence also to a choice of a basis. AICN preserves affine-invariance obtained from assumptions throughout the convergence. In contrast, Cubic Newton uses base-dependent l 2 norm and hence depends on a choice of a basis. This represents an extra layer of complexity. - Alternative analysis: We also provide alternative analysis under weaker assumptions (Appendix C).

The rest of the paper is structured as follows. In Section 2.3 we introduce our notation. In Section 3, we discuss algorithm AICN, affine-invariant properties and self-concordance. In Sections 4.1 and 4.2 we show global and local convergence guarantees, respectively. In Section 5 we present an empirical comparison of AICN with other algorithms sharing fast global convergence.

## Minimization problem & notation

In the paper, we consider a d -dimensional Euclidean space E. Its dual space, E ∗, is composed of all linear functionals on E. For a functional g ∈ E ∗, we denote by 〈 g, x 〉 its value at x ∈ E.

We consider the following convex optimization problem: where f (x) ∈ C 2 is a convex function with continuous first and second derivatives and positive definite Hessian. We assume that the problem has a unique minimizer x ∗ ∈ argmin x ∈ E f (x). Note, that ∇ f (x) ∈ E ∗, ∇ 2 f (x) h ∈ E ∗. Now, we introduce different norms for spaces E and E ∗. Denote x, h ∈ E, g ∈ E ∗. For a self-adjoint positive-definite operator H: E → E ∗, we can endow these spaces with conjugate Euclidean norms: For identity H = I, we get classical Eucledian norm ‖ x ‖ I = 〈 x, x 〉 1 / 2. For local Hessian norm H = ∇ 2 f (x), we use shortened notation Operator norm is defined by for H: E → E ∗ and a fixed x ∈ E. If we consider a specific case E ← R d, then H is a symmetric positive definite matrix.

## New Algorithm: Affine-Invariant Cubic Newton

Finally, we are ready to present algorithm AICN. It is damped Newton method with updates as summarized in Algorithm 1. Stepsize satisfy α k ≤ 1 (from AG inequality,). Also lim x k → x ∗ α k = 1, hence converges to Newton method. Next, we are going to discuss geometric properties of our algorithm.

## Algorithm 1 AICN: Affine-Invariant Cubic Newton

- 1: Requires: Initial point x 0 ∈ E, constant L est s.t. L est ≥ L semi > 0

## Geometric properties: affine invariance

One of the main geometric properties of the Newton method is affine invariance, invariance to affine transformations of variables. Let A: E → E ∗ be a non-degenerate linear transformation. Consider function φ ( y ) = f ( A y ). By affine transformation, we denote f ( x ) → φ ( y ) = f ( A y ), x → A -1 y.

Significance of norms: Note that local Hessian norm ‖ h ‖ ∇ f (x) is affine-invariant because where h = A z. On the other hand, induced norm ‖ h ‖ I is not affine-invariant because With respect to geometry, the most natural norm is local Hessian norm, ‖ h ‖ ∇ f (x). From affine invariance follows that for this norm, the level sets { y ∈ E | ‖ y -x ‖ 2 x ≤ c } are balls centered around x (all directions have the same scaling). In comparison, scaling of the l 2 norm is dependent on eigenvalues of the Hessian. In terms of convergence, one direction in l 2 can significantly dominate others and slow down an algorithm.

Significance for algorithms: Algorithms that are not affine-invariant can suffer from chosen coordinate system. This is the case for Cubic Newton, as its model is bound to base-dependent l 2 norm. Same is true for any other method regularized with an induced norm ‖ h ‖ I. On the other hand, (damped) Newton methods have affine-invariant models, and hence as algorithms independent of the chosen coordinate system. We prove this claim in following lemma (note: α k = 1 and α k from are affine-invariant).

Lemma 1 (Lemma 5.1.1 Nesterov ). Let the sequence { x k } be generated by a damped Newton method with affine-invariant stepsize α k, applied to the function f: x k +1 = x k -α k [ ∇ 2 f ( x k ) ] -1 ∇ f ( x k ). For function φ ( y ), damped Newton method generates { y k }: y k +1 = y k -α k [ ∇ 2 φ ( y k ) ] -1 ∇ φ ( y k ), with y 0 = A -1 x 0. Then y k = A -1 x k.

## Significance in assumptions: self-concordance

We showed that damped Newton methods preserve affine-invariance through iterations. Hence it is more fitting to analyze them under affine-invariant assumptions. Affine-invariant version of smoothness, self-concordance, was introduced in Nesterov and Nemirovski.

Definition 1. Convex function f ∈ C 3 is called self-concordant if where for any integer p ≥ 1, by D p f (x)[h] p def = D p f (x)[h,..., h] we denote the p -th order directional derivative a of f at x ∈ E along direction h ∈ E.

Both sides of inequality are affine-invariant. This assumption corresponds to a big class of optimization methods called interior-point methods. Self-concordance implies uniqueness of the solution, as stated in following proposition.

Proposition 1 (Theorem 5.1.16, Nesterov ). Let a self-concordant function f be bounded below. Then it attains its minimum at a single point.

Rodomanov and Nesterov introduced stronger version of self-concordance assumption.

Definition 2. Convex function f ∈ C 2 is called strongly self-concordant if For our analysis, we introduce definition for functions between self-concordant and strongly self-concordant.

Definition 3. Convex function f ∈ C 2 is called semi-strongly self-concordant if Note that all of the Definitions 1 - 3 are affine-invariant, their respective classes satisfy strong self-concordance ⊆ semi-strong self-concordance ⊆ self-concordance.

Also, for a fixed strongly self-concordant function f and smallest such L sc, L semi, L str holds L sc ≤ L semi ≤ L str.

These notions are related to the convexity and smoothness; strong concordance follows from function L 2 -Lipschitz continuous Hessian and strong convexity.

Proposition 2. Let H: E → E ∗ be a self-adjoint positive definite operator. Suppose there exist µ > 0 and L 2 ≥ 0 such that the function f is µ -strongly convex and its Hessian is L 2 -Lipschitz continuous with respect to the norm ‖ · ‖ H. Then f is strongly self-concordant with constant L str = L 2 µ 3 / 2.

## From assumptions to algorithm

From semi-strong self-concordance we can get a second-order bounds on the function and model.

Lemma 2. If f is semi-strongly self-concordant, then Consequently, we have upper bound for function value in form One can show that is not valid for just self-concordant functions. For example, there is no such upper bound for -log(x). Hence, the semi-strongly self-concordance is significant as an assumption.

We can define iterates of optimization algorithm to be minimizers of the right hand side of, for an estimate constant L est ≥ L semi. It turns out that subproblem is easy to solve. To get an explicit solution, we compute its gradient w.r.t. h. For solution h ∗, it should be equal to zero, We get that step has the same direction as a Newton method and is scaled by α k = (L est 2 ‖ h ∗ ‖ x +1) -1. Now, we substitute h ∗ from to We solve the quadratic equation for α k, and obtain explicit formula for stepsizes of AICN, as. We formalize this connection in theorem, for further explanation see proof in Appendix B.

Theorem 1. For L est ≥ L semi, update of AICN, is a minimizer of upper bound, x k +1 = S f,L est (x k).

## Convergence Results

## Global convergence

Next, we focus on global convergence guarantees. We will utilize the following assumption: Assumption 1 (Bounded level sets). The objective function f has a unique minimizer x ∗. Also, the diameter of the level set L (x 0) def = { x ∈ E: f (x) ≤ f (x 0) } is bounded by a constant D 2 as a, max x ∈L (x 0) ‖ x -x ∗ ‖ 2 ≤ D 2 < + ∞. a We state it in l 2 norm for easier verification. In proofs, we use its variant D in Hessian norms,.

Our analysis proceeds as follows. Firstly, we show that one step of the algorithm decreases function value, and secondly, we use the technique from [Ghadimi et al., 2017] to show that multiple steps lead to O ( k -2 ) global convergence. We start with following lemma.

Lemma 3 (One step globally). Let function f be L semi-semi-strongly self-concordant, convex with positive-definite Hessian and L est ≥ L semi. Then for any x ∈ E, we have This lemma implies that step decreases function value (take y ← x). Using notation of Assumption 1, x k ∈ L (x 0) for any k ≥ 0. Also, setting y ← x and x ← x ∗ in yields ‖ x -x ∗ ‖ x ≤ (‖ x -x ∗ ‖ 2 x ∗ + L est ‖ x -x ∗ ‖ 3 x ∗) 1 2. We denote those distances D and R, They are both affine-invariant and R upper bounds D. While R depends only on the level set L (x 0), D can be used to obtain more tight inequalities. We avoid using common distance D 2, as l 2 norm would ruin affine-invariant properties.

Theorem 2. Let f (x) be a L semi-semi-strongly self-concordant convex function with positive-definite Hessian, constant L est satisfy L est ≥ L semi and Assumption 1 holds. Then, after k +1 iterations of Algorithm 1, we have the following convergence rate: Consequently, AICN converges globally with a fast rate O (k -2). We can now present local analysis.

## Local convergence

For local quadratic convergence are going to utilise following lemmas.

Lemma 4. For convex L semi-semi-strongly self-concordant function f and for any 0 < c < 1 in the neighborhood of solution Lemma 4 formalizes that a inverse hessians of a self-concordant function around the solution is non-degenerate. With this result, we can show one-step gradient norm decrease.

Lemma 5 (One step decrease locally). Let function f be L semi-semi-strongly self-concordant and L est ≥ L semi. If x k such that holds, then for next iterate x k +1 of AICN holds Using Lemma 4, we shift the gradient bound to respective norms, Gradient norm decreases ‖∇ f (x k +1) ‖ ∗ x k +1 ≤ ‖∇ f (x k) ‖ ∗ x k for ‖∇ f (x k) ‖ ∗ x k ≤ (2 -c) 2 -1 2 L est.

Figure 1: Comparison of regularized Newton methods and Damped Newton method for logistic regression task on a9a dataset.

As a result, neighbourhood of the local convergence is { x: ‖∇ f ( x ) ‖ ∗ x ≤ min [ (2 -c ) 2 -1 2 L est; (2 c +1) 2 -1 2 L est ]}. Maximizing by c, we get c = 1 / 3 and neighrbourhood { x: ‖∇ f ( x ) ‖ ∗ x ≤ 8 9 L est }. One step of AICN decreases gradient norm quadratically, multiple steps leads to following decrease.

Theorem 3 (Local convergence rate). Let function f be L semi-semi-strongly self-concordant, L est ≥ L semi and starting point x 0 be in the neighborhood of the solution such that ‖∇ f ( x 0 ) ‖ ∗ x 0 ≤ 8 9 L est. For k ≥ 0, we have quadratic decrease of the gradient norms,

## Numerical Experiments

In this section, we evaluate proposed AICN (Algorithm 1) algorithm on the logistic regression task and second-order lower bound function. We compare it with regularized Newton methods sharing fast global convergence guarantees: Cubic Newton method [Nesterov and Polyak, 2006], and Globally Regularized Newton method with L 2 -constant. Because AICN has a form of a damped Newton method, we also compare it with Damped Newton with fixed (tuned) stepsize α k = α. We report decrease in function value f ( x k ), function value suboptimality f ( x k ) -f ( x ∗ ) with respect to iteration and time. The methods are implemented as PyTorch optimizers. The code is available .

## Logistic regression

For first part, we solve the following empirical risk minimization problem: where { (a i, b i) } i m =1 are given data samples described by features a i and class b i ∈ {-1, 1 }.

In Figure 1, we consider task of classification images on dataset a9a [Chang and Lin, 2011]. Number of features for every data sample is d = 123, m = 20000. We take staring point x 0 def = 10[1, 1,..., 1] ⊤ and µ = 10 -3. Our choice is differ from x 0 = 0 (equal to all zeroes) to show globalisation properties of methods ( x 0 = 0 is very close to the solution, as Newton method converges in 4 iterations). Parameters of all methods are fine-tuned, we choose parameters L est, L 2, α (of AICN, Cubic Newton, Damped Newton, resp.) to largest values having monotone decrease in reported metrics. Fine-tuned values are L est = 0. 97 L 2 = 0. 000215, α = 0. 285. Figure 1 demonstrates that AICN converges slightly faster than Cubic Newton method by iteration, notably faster than Globally Regularized Newton and significantly faster than Damped Newton. AICN outperforms every method by time.

Figure 2: Comparison of regularized Newton methods and Damped Newton method for second-order lower bound function.

## Second-order lower bound function

For second part we solve the following minimization problem: This function is a lower bound for a class of functions with Lipschitz continuous Hessian with additional regularization [Nesterov and Polyak, 2006, Nesterov, 2021a]. In Figure 2, we take d = 20, x 0 = 0 (equal to all zeroes). Parameters L est, L 2, α are fine-tuned to largest values having monotone decrease in reported metrics: L est = 662 L 2 = 0. 662, α = 0. 0172. Figure 2 demonstrates that AICN converges slightly slower than Cubic Newton method, slightly faster than Globally Regularized Newton, and significantly faster than Damped Newton. ain outperforms every method by time. More experiments are presented in Appendix A. Note, that the iteration of the Cubic Newton method needs an additional line-search, so one iteration of Cubic Newton is computationally harder than one iteration of AICN. More experiments are presented in Appendix A.
