<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Physics-Informed Kernel Embeddings: Integrating Prior System Knowledge with Data-Driven Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven control algorithms use observations of system dynamics to construct an implicit model for the purpose of control. However, in practice, data-driven techniques often require excessive sample sizes, which may be infeasible in real-world scenarios where only limited observations of the system are available. Furthermore, purely data-driven methods often neglect useful a priori knowledge, such as approximate models of the system dynamics. We present a method to incorporate such prior knowledge into data-driven control algorithms using kernel embeddings, a nonparametric machine learning technique based in the theory of reproducing kernel Hilbert spaces. Our proposed approach incorporates prior knowledge of the system dynamics as a bias term in the kernel learning problem. We formulate the biased learning problem as a least-squares problem with a regularization term that is informed by the dynamics, that has an efficiently computable, closed-form solution. Through numerical experiments, we empirically demonstrate the improved sample efficiency and out-of-sample generalization of our approach over a purely data-driven baseline. We demonstrate an application of our method to control through a target tracking problem with nonholonomic dynamics, and on spring-mass-damper and F-16 aircraft state prediction tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The practical deployment of autonomous systems demands algorithms that can account for stochasticity and unexpected events due to humans in the loop or dramatic changes in the environment. Model-based approaches to stochastic optimal control offer an analytic representation that is highly generalizable, but often rely upon strict model assumptions, and can become inaccurate when deployed in new environments. They are particularly susceptible to model misspecifications, which can lead to inaccurate predictions that may lead to unpredictable or unsafe behaviors. Data-driven control can account for poorly-characterized disturbances, but typically neglect prior system knowledge. Additionally, these methods often exhibit poor data efficiency, meaning they require excessive sample sizes in order to adequately characterize the dynamical system behavior.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a method to incorporate (potentially) imperfect knowledge of the system dynamics in kernel embeddings in order to numerically estimate expectations in stochastic optimal control and state prediction problems. Specifically, we propose physics-informed kernel embeddings, a nonparametric statistical learning technique based in reproducing kernel Hilbert spaces (RKHS) that incorporates prior knowledge of the dynamics as inductive bias. As shown in Thorpe and Oishi; Thorpe et al., data-driven reformulations of stochastic optimal control problems using kernel embeddings can efficiently be solved as a linear program by exploiting the mathematical properties of the RKHS. However, despite the applicability to control, these techniques have thus far not seen widespread popularity, and presently do not take prior system knowledge into account.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

* These authors contributed equally to this work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We modify the regularized least-squares problem used to learn kernel embeddings with an additional bias term that encodes prior knowledge of the dynamics (Figure 1). We present a representer theorem, which provides a closed-form solution to the learning problem. Finally, we describe how the proposed physics-informed kernel embeddings may be applied to solve approximate stochastic optimal control problems. We experimentally demonstrate our approach on state prediction and control tasks, including a spring-mass-damper system with a limited sample of system observations, a highly nonlinear F-16 aircraft, and a target tracking problem with nonholonomic dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let (X, B X) be a Borel space called the state space and (U, B U) be a compact Borel space called the control or input space. We consider discrete-time stochastic systems of the form where x t ∈ X is the state of the system at time t, u t ∈ U is the control action, θ ∈ Θ are model parameters, and w t are independent random variables representing the stochastic disturbance. The system evolves from an initial condition x 0 ∈ X (which may be taken from an initial distribution P 0 on X). For notational convenience, we can represent the dynamics in via a stochastic kernel Q: B X ×X ×U → that assigns a probability measure Q (· | x, u) to every (x, u) ∈ X × U on the measurable space (X, B X), as shown in Bertsekas and Shreve.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We presume the dynamics in are unknown, meaning we do not have direct knowledge of the system dynamics or the uncertainty. Instead, we presume that a sample S, consisting of observations taken independently and identically distributed (i.i.d.) from the system evolution is available, e.g. observations of the system transitions S = { ( x 1, u 1, y 1 ),..., ( x M, u M, y M ) }. where x i and u i are taken from X and U, respectively, and y i ∼ Q ( · | x i, u i ). Such a sample may be collected from high-fidelity simulation or via observations of the system evolution from system trajectories. In addition, we presume that we have prior (potentially imperfect) knowledge of the dynamics, ˜ f: X × U → X. Such prior knowledge may be available, for instance, if we only have access to a first-order approximation of the dynamics, if the deterministic dynamics are available but the stochastic uncertainty is unknown, or if the model parameters θ are poorly estimated.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We solve, under the conditions above, two problems: 1) state prediction, where we seek to estimate the expected future state of the system after taking an action u in a given state x, and 2) unconstrained stochastic optimal control, which can generally be written as where c: X → R is a (well-posed) arbitrary cost function that could capture, e.g. LQR, MPC, or other typical control objectives. We focus on and because they are representative of common problems in controls. As shown in Thorpe and Oishi, by embedding the integral operator of the stochastic kernel Q as an element in a high-dimensional space of functions known as a reproducing kernel Hilbert space (RKHS), we can approximate the expected value as a linear operation in the RKHS, and the approximate kernel-based reformulation of can be solved as a linear program. This is important because it provides a data-driven approach that is potentially amenable to run-time implementations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The main challenges are twofold: kernel embeddings neglect important information about the dynamics and are therefore more susceptible to errors, and they are susceptible to common sampling issues such as limited sample information.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The key contribution of this paper is a method to incorporate potentially imperfect knowledge of the system dynamics in the kernel embedding to numerically estimate and. We propose physics-informed kernel embeddings, that incorporates prior dynamics knowledge in kernel distribution embeddings, and apply our proposed technique to the problem of state prediction and control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Kernel Embeddings of Distributions", "weight": 1.0} -->

Define the kernel k: X ×X → R, which is a positive definite function. According to the Moore-Aronszajn theorem, given a positive definite kernel k, there exists a corresponding RKHS H of functions from X to R which satisfies the following properties: (i) For all x ∈ X, k ( x, · ) ∈ H, and (ii) For all f ∈ H and x ∈ X, f ( x ) = 〈 f, k ( x, · ) 〉 H, which is known as the reproducing property. Similarly, let l: U × U → R be a reproducing kernel over U and let U be its associated RKHS.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Kernel Embeddings of Distributions", "weight": 1.0} -->

Note that expectations E y ∼ Q (·| x,u) [c (y)] are linear in the function argument c. As shown in Gr¨ unew¨ alder et al., assuming the kernel k is measurable and bounded, there exists an element m (x, u) ∈ H called the kernel distribution embedding, such that by the reproducing property, 〈 c, m (x, u) 〉 H = E y ∼ Q (·| x,u) [c (y)]. We can compute an empirical estimate ˆ m (x, u) of the embedding m (x, u) using data S. As shown in Gr¨ unew¨ alder et al., the estimate ˆ m (x, u) can be computed as the solution to a regularized least-squares (RLS) problem, where V is a vector-valued RKHS of functions from X × U to H and λ > 0 is the regularization parameter. The solution to is given by a well-known class of theorems known as representer theorems Sch¨ olkopf et al..

<!-- chunk {"id": "body-0014", "role": "body", "section": "Incorporating Prior Knowledge of the Dynamics in the Kernel Embedding", "weight": 1.0} -->

Following Sch¨ olkopf et al., we propose to learn a physics-informed kernel embedding estimate via the following biased RLS problem, which differs from in that it includes an additional penalty term 〈 f, f 0 〉 V, where f 0 ∈ V is a user-specified bias term. As discussed in Sch¨ olkopf et al., this is a way to introduce bias into the regularization, and penalizes the difference between the learned function and the bias f 0, instead of only the RKHS norm ‖ f ‖ 2 V. The solution to can be characterized via a representer theorem, which we present as Theorem 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Incorporating Prior Knowledge of the Dynamics in the Kernel Embedding", "weight": 1.0} -->

Theorem 1 If ˆ f ∈ V minimizes the risk functional, it is unique and has the form where the coefficients β i ∈ H, i = 1,..., M, are the unique solution of the set of linear equations, Proof The proof is similar to. Let f be any element of V such that f (x i, u i) = k (y i, ·), which minimizes the least-squared error of the data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Incorporating Prior Knowledge of the Dynamics in the Kernel Embedding", "weight": 1.0} -->

Let g = f -ˆ f, and note that 1 2 ‖ f ‖ 2 V can be expanded as 1 2 ‖ f ‖ 2 V = 1 2 ‖ g + ˆ f ‖ 2 V = 1 2 ‖ g ‖ 2 V + 〈 g, ˆ f 〉 V + 1 2 ‖ ˆ f ‖ 2 V. Let E (f) be the risk functional, Taking the difference between the risk E (f) from and the risk E (ˆ f) using, and using the above expansion, we obtain where the final term uses the fact that 〈 ˆ f, f 0 〉 V -〈 f, f 0 〉 V = 〈 ˆ f -f, f 0 〉 V = -〈 g, f 0 〉 V. Using the fact that for any g ∈ V and f ∈ H, 〈 f, g (x, u) 〉 H = 〈 g, k (x i, ·) l (u i, ·) f 〉 V, which comes from well-known properties of the vector-valued RKHS V, and equations and, we have that Then, using, we have that from which we conclude that ˆ f is the unique minimizer of E (uniqueness follows from the convexity of V),

<!-- chunk {"id": "body-0017", "role": "body", "section": "Incorporating Prior Knowledge of the Dynamics in the Kernel Embedding", "weight": 1.0} -->

In practical terms, Theorem 1 shows that the solution ˆ m 0 to can be represented as a combination of two elements in the RKHS: a bias term f 0, and a linear combination of kernel functions ∑ M i =1 β i k ( x i, · ) l ( u i, · ) that represents the data-driven part.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Incorporating Prior Knowledge of the Dynamics in the Kernel Embedding", "weight": 1.0} -->

Now it remains to choose a bias f 0. A natural choice for f 0 is given by such that for any c ∈ H, 〈 c, f 0 (x, u) 〉 H = 〈 c, k (˜ f (x, u), ·) 〉 H = c (˜ f (x, u)) by the reproducing property. Then, using the solution ˆ m 0 to the RLS problem in given by Theorem 1 and the bias term f 0, we have that for any function c ∈ H, where c ∈ R M and ˜ c ∈ R M are vectors with elements c i = c (y i) and ˜ c i = c (˜ f (x i, u i)), respectively, W = (G + λI) -1, where G ∈ R M × M, is a positive semi-definite matrix with elements G ij = k (x i, x j) l (u i, u j), and K (x, u) ∈ R M is a vector that depends on x and u that has elements [K (x, u)] i = k (x i, x) l (u i, u).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Incorporating Prior Knowledge of the Dynamics in the Kernel Embedding", "weight": 1.0} -->

The estimate in has a simple interpretation via addition and subtraction of the cost over the approximate dynamics from the expected cost, E y ∼ Q ( ·| x,u ) [ c ( y ) -c ( ˜ f ( x, u ))] + c ( ˜ f ( x, u )). Specifically, the first term c ⊤ WK ( x, u ) on the right-hand side of corresponds to the purely datadriven kernel distribution embedding estimate; the second term ˜ c ⊤ WK ( x, u ) represents a kernel distribution embedding with the training data { ( x i, u i, ˜ f ( x i, u i )) } i M =1, where we substitute the approximate dynamics over the data points ˜ f ( x i, u i ) for the observations y i in the dataset S; and the third term g ( ˜ f ( x, u )) is a correction that shifts the estimate such that it is centered around ˜ f.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Control Using Physics-Informed Kernel Embeddings", "weight": 1.0} -->

In this section, we demonstrate how physics-informed kernel embeddings can be used to solve the kernel-based control problem. A stochastic policy π: B U ×X → for the system in is a stochastic kernel that assigns a probability measure π ( · | x ) to every x ∈ X on ( U, B U ). As shown in Thorpe and Oishi; Thorpe et al., we can represent the stochastic policy π as a kernel embedding p ( x ) in the RKHS U -a linear combination of kernels over a user-specified control set A = { ˜ u j } P j =1, given by p ( x ) = ∑ P j =1 γ j ( x ) l (˜ u j, · ), where γ ( x ) ∈ R P are real coefficients that depend on the value of x.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Control Using Physics-Informed Kernel Embeddings", "weight": 1.0} -->

We use the physics-informed kernel embedding ˆ m 0 (in place of the embedding ˆ m) as in to estimate the expected cost with respect to Q. Using ˆ m 0, the policy embedding p (x) can be found as the solution to the following problem, where c ∈ R M and ˜ c ∈ R M are as, W ∈ R M × M is a real matrix as, R (x) ∈ R M × P is a real matrix that depends on x, with elements [R (x)] ij = k (x i, x) l (u i, ˜ u j), and C (x) ∈ R P is a vector with elements [C (x)] j = c (˜ f (x, ˜ u j)). Notably, the problem in is a linear program, and can be solved efficiently. According to Boyd et al., since we seek to minimize a linear combination by choosing non-negative weights, it is immediately clear that we should allocate as much weight as possible to the smallest terms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Control Using Physics-Informed Kernel Embeddings", "weight": 1.0} -->

Thus, the solution is a vector γ ∗ (x) ∈ R P of all zeros except at the index corresponding to the control action in A that gives the lowest expected cost, where it is one. See Thorpe and Oishi for more details.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

In all experiments, we use a Gaussian kernel function k ( x, x ′ ) = exp( -‖ x -x ′ ‖ 2 / 2 σ 2 ), σ > 0, and the hyperparameters σ and λ are chosen via cross-validation. See Sch¨ olkopf et al.; Song et al. and Li et al. for a detailed discussion of parameter selection. Code to reproduce all experiments is available.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Spring-Mass-Damper System", "weight": 1.0} -->

For the purpose of analysis, we first consider the prediction problem in with an (uncontrolled) spring-mass-damper system. The equations of motion are given by m ¨ q = -b ˙ q -kq. We presume that we have access to imperfect system dynamics ˜ f ( x ) = -( k/m ) q, corresponding to an undamped spring-mass system. We generate a synthetic dataset S = { ( x i, y i ) } i M =1 with varying sample sizes M = 10, 50, 100, 500, where the states x i are taken randomly from a bounded region of X, and y i = f ( x i ) are corresponding next states at the subsequent timestep. We consider two cases for the sample: 1) the states x i are taken within the region [0, 0. 15] × [0, 0. 15], meaning we only have information within a limited operating regime, and 2) the states are taken within the region [ -0. 15, 0. 15] × [ -0. 15, 0. 15], which fully encompasses the operating region.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Spring-Mass-Damper System", "weight": 1.0} -->

Using the sample S, we then compute the physics-informed kernel embedding ˆ m 0 using with σ = 0. 2, and use ˆ m 0 to predict the system evolution via over N = 100 time steps from a fixed initial condition x 0 = [0. 1, 0. 1] ⊤. To provide a baseline for comparison, we also use the purely data-driven embedding ˆ m, computed using S via to compute.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Spring-Mass-Damper System", "weight": 1.0} -->

The top row of Figure 2 shows the performance of our approach for sample sizes M = 10, 50, 100, 500 when data is collected from a limited region of the state space. Our approach demonstrates good empirical performance, and accurately predicts the evolution of the system despite having imperfect knowledge based on the undamped system under a wide range of conditions. As expected, the purely data-driven prediction does not accurately predict the system evolution outside the data region, even as the amount of data increases (top right plot). When data is collected over the entire region of interest, the quality of the purely data-driven estimate improves as the amount of data increases (bottom row of Figure 2). Note that our proposed approach has sound performance even while using only a small fraction of the data. We note the following important trends.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Spring-Mass-Damper System", "weight": 1.0} -->

Approximate physics knowledge improves out-of-distribution prediction accuracy. As shown in the top row of Figure 2, in contrast to the purely data-driven embedding, the physicsinformed kernel embeddings generalize beyond the training dataset.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Spring-Mass-Damper System", "weight": 1.0} -->

Approximate physics knowledge improves sample efficiency. As seen in the bottom row of Figure 2, when the observed transition data encompasses the entire region of interest, our approach is able to accurately predict the dynamics using only 10 data points.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Spring-Mass-Damper System", "weight": 1.0} -->

Approximate physics knowledge reduces the prediction error. Figure 3 compares the empirical prediction error of the physics-informed kernel embedding ˆ m 0 against the purely data-driven embedding ˆ m. We randomly sample 100 initial states x 0 uniformly in the region [ -0. 1, 0. 1] × [ -0. 1, 0. 1], and use the learned embeddings to predict the evolution of the state 100 time steps into the future. Figure 3 shows the median cumulative prediction error along these predicted trajectories (measured as the Euclidean distance between the true state vector and the predicted state vector). We observe that for small datasets (particularly for M smaller than 200 ) the physics-informed kernel embedding enjoys prediction error values that are two orders of magnitude smaller than those of the purely data-driven kernel embedding, and that the baseline method requires at least 5, 000 data points to achieve comparable levels of accuracy.

<!-- chunk {"id": "body-0030", "role": "body", "section": "F-16 Aircraft", "weight": 1.0} -->

We consider a ground collision avoidance scenario for an F-16 aircraft at initial altitude, as described in Djeumou and Topcu; Heidlauf et al.. The underlying nonlinear dynamics, containing 13 states and 4 control inputs, capture the ( 6 -DOF) motion via evolution of velocity v t, angle of attack α, sideslip β, altitude h, attitude angles: roll φ, pitch θ, yaw ψ, and their corresponding rates p, q, r, engine power and two more states p n, p e for translation along north and east, as in Stevens et al.. The plant is built on linearly interpolated lookup tables that incorporate wind tunnel data describing the engine model, and other dynamic coefficients. We inject zero-mean Gaussian noise with a standard deviation of 1% of the magnitude of each state, such that the noise scales with the state magnitude. We consider the case where the true dynamics are unknown, but presume that we have access to approximate dynamics with incorrect model parameters, including a gravitational constant of g = 7. 0, and the interpolated lookup tables for the elevator control are half of their original values.

<!-- chunk {"id": "body-0031", "role": "body", "section": "F-16 Aircraft", "weight": 1.0} -->

These changes significantly alter the response of the aircraft to pulling up and avoiding collision with the ground.

<!-- chunk {"id": "body-0032", "role": "body", "section": "F-16 Aircraft", "weight": 1.0} -->

We collect a sample S = { ( x 0,i, ξ i ) } i M =1, consisting of M = 500 initial conditions x 0,i taken uniformly such that [ v t, α, β, φ, θ, p, q, r, h, power ] ⊤ ∈ × [ -0. 01, 0. 09] × [ -0. 05, 0. 05] × [0. 55, 0. 95] × [ -1. 2, -0. 8] × [ -0. 2, 0. 2] × [ -0. 2, 0. 2] × [ -0. 2, 0. 2] × × [8. 7, 9. 3], and the resulting trajectories from those initial conditions ξ i ∼ T ( · | x 0,i ) using the true, nominal dynamics, where T: B X N ×X → is a stochastic kernel that represents the LQR-controlled, closed-loop system dynamics over N = 1500 time steps. Using trajectory data modifies the probability model to be a stochastic kernel over state trajectories, but does not significantly alter the kernel estimate.

<!-- chunk {"id": "body-0033", "role": "body", "section": "F-16 Aircraft", "weight": 1.0} -->

Modifications of our approach to accommodate trajectory data is described in Thorpe et al..

<!-- chunk {"id": "body-0034", "role": "body", "section": "Control of a Nonholonomic Vehicle System", "weight": 1.0} -->

We solve for a target tracking control problem with a nonholonomic vehicle, as in Thorpe and Oishi. The dynamics are given by ˙ x 1 = u 1 sin( x 3 ), ˙ x 2 = u 1 cos( x 3 ), ˙ x 3 = u 2, where x = [ x 1, x 2, x 3 ] ⊤ ∈ R 3 is the state and u = [ u 1, u 2 ] ⊤ ∈ R 2 is the control input, which we constrain to be within the bounds [0. 2, 1. 5] × [ -10. 1, 10. 1]. We discretize the system in time and apply an affine disturbance with an exponential distribution w t ∼ Exp(0. 1), with PDF f ( x; α ) = α exp( -αx ) if x ≥ 0 and f ( x; α ) = 0 if x < 0. We presume that the deterministic discrete-time dynamics are given as approximate dynamical system knowledge, but that the stochastic dynamics are unknown (i.e. we do not have prior knowledge of the disturbance).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Control of a Nonholonomic Vehicle System", "weight": 1.0} -->

Weseek to solve, where we minimize the squared Euclidean distance to a moving target over a time horizon of N = 60. Wedefine a trajectory of target waypoints z 0, z 1,..., z N (shown in black in Figure 5). We consider the case where the future target position is unknown. Thus, we solve the following (unconstrained) optimization problem at each time step: min π E [ ‖ x t +1 -z t ‖ 2 ] as. See Thorpe and Oishi for more details. We collect a sample S = { ( x i, u i, y i ) } i M =1 of size M = 500, where the states x i are taken uniformly in the region shown in Figure 5. To compute the control algorithm, we generate a sample A = { ˜ u j } P j =1 of P = 210 control actions taken uniformly in the region [0. 2, 1. 2] × [ -10. 1, 10. 1]. We then presume that the true dynamics are unknown for the purpose of computing the control inputs. We then computed the physics informed kernel embedding ˆ m 0 with σ = 0.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Control of a Nonholonomic Vehicle System", "weight": 1.0} -->

75. Using ˆ m 0, we simulate the system from an initial condition x 0 = [ -1, 0, π/ 2] ⊤ and solve at each time step to compute the stochastic policy. The total computation time was approximately 0. 272 seconds, and the results are shown in Figure 5. Using the same sample size, the baseline method from Thorpe and Oishi fails to generate a meaningful trajectory (not shown). To generate a comparable trajectory, we used a much larger sample size, M = 5000, shown in blue in Figure 5, and the computation time was approximately 5. 993 seconds. This shows that our method demonstrates better empirical and computational performance, and requires less data due to the inclusion of prior dynamics knowledge.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions & Future Work", "weight": 1.0} -->

In this paper, we presented physics-informed kernel embeddings, a novel technique for incorporating prior system knowledge in data-driven representations of system dynamics using kernel distribution embeddings. Numerical experiments demonstrate the effectiveness of the proposed method on prediction tasks, including for systems with imperfect system knowledge on a spring-mass-damper system and highly nonlinear dynamics on an F-16 system, and on control tasks via a nonholonomic system target tracking problem. Results show that our approach generalizes well outside the data regime, is computationally efficient, and is robust to common sampling issues.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions & Future Work", "weight": 1.0} -->

An important direction for future work in this area involves an exploration of how to incorporate other forms of prior knowledge, such as known system properties (e.g. symmetry, invariance) into the learning problem. Additionally, of practical interest is a characterization of the effect that poor or inaccurate approximate knowledge has on the learned representation.
