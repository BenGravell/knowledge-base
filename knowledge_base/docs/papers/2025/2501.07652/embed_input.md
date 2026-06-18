<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite Sample Identification of Partially Observed Bilinear Dynamical Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of learning a realization of a partially observed bilinear dynamical system (BLDS) from noisy input-output data. Given a single trajectory of input-output samples, we provide a finite time analysis for learning the system's Markov-like parameters, from which a balanced realization of the bilinear system can be obtained. Our bilinear system identification algorithm learns the system's Markov-like parameters by regressing the outputs to highly correlated, nonlinear, and heavy-tailed covariates. Moreover, the stability of BLDS depends on the sequence of inputs used to excite the system. These properties, unique to partially observed bilinear dynamical systems, pose significant challenges to the analysis of our algorithm for learning the unknown dynamics. We address these challenges and provide high probability error bounds on our identification algorithm under a uniform stability assumption. Our analysis provides insights into system theoretic quantities that affect learning accuracy and sample complexity. Lastly, we perform numerical experiments with synthetic data to reinforce these insights.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning the dynamical behavior of nonlinear systems is an important and challenging problem with applications ranging from engineering, physics, biology, to language modeling, and sequence predictions. Bilinear dynamical systems (BLDS) constitute a simple yet powerful class of nonlinear systems naturally arising in a variety of domains from engineering, biology, quantum mechanical processes to recommendation systems. Moreover, bilinear systems approximate a much broader class of nonlinear systems via Carleman linearization or Koopman canonical transform of control-affine nonlinear systems. Therefore, learning the dynamics of BLDS from input-output data is an important and useful problem which has attracted significant interest, both in the case of continuous-time and discrete-time. However, theoretical guarantees of learning BLDS from a single trajectory of noisy input-output data is lacking, with current guarantees existing only for bilinear systems with complete state observations. Our goal in this paper is to provide an algorithm and theoretical guarantees for learning partially observed BLDS from noisy input-output data sampled from a single trajectory.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We achieve this by learning the system's *Markov-like parameters*, which uniquely identify the end-to-end behavior of the system, and can be used to recover the state-space matrices up to a similarity transform using existing algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal relates to the problem of learning linear dynamical system (LDS) from partial state-observations. In this setting, a line of recent work focuses on finite sample error bounds. study methods which use least squares regression to learn the system's Markov parameters or Hankel matrix, which can then be used to recover the state-space matrices (up to a similarity transform) using classic Ho-Kalman Algorithm. study system identification with Hankel nuclear norm regularization. Other works have focused on learning to predict the behavior of partially observed LDS via gradient descent and spectral filtering. The linear setting has been extended to (decode-able) nonlinear observations and bilinear partial observations. However, to the best of our knowledge, sample complexity and non-asymptotic analysis for partially observed nonlinear dynamical systems (including BLDS) have not been considered before.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Non-asymptotic learning of (non)linear dynamical systems with complete state observations has also attracted significant attention recently. Most of the advancements in this direction are focused on linear systems, where an optimal error rate is achieved by using either mixing-time or martingale-based arguments. These results have been extended to switched linear dynamical systems, as well as certain classes of nonlinear dynamical systems, including state transition models with nonlinear activation functions, nonlinear features, or from a nonparametric perspective. However, the problem of learning nonlinear dynamical systems from partial observations of a single trajectory is still an open problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Can we learn a partially observed bilinear dynamical system from a single trajectory?*

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main difficulty arises from the fact that the hidden states evolve according to a bilinear state equation, for which the analysis tools developed for learning partially observed LDS do not work. Moreover, the stability of a BLDS explicitly depends on the input sequence, which is in stark contrast to the deterministic notion of stability in the case of LDS.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We overcome the aforementioned challenges and provide theoretical guarantees for learning partially observed bilinear dynamical systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sample complexity and error bounds: We provide the first sample complexity analysis and finite-sample error bounds for learning a realization of a partially observed BLDS from a single trajectory of input-output data. Unlike LDS, the output of a bilinear system maps to the history of inputs via nonlinear features (obtained by the Kronecker products of past inputs) and a sequence of Markov-like parameters with exponentially increasing length. Our main result ) provides $\overset{\sim}{\mathcal{O}}{({1/\sqrt{T}})}$ error rate for learning these parameters from a single trajectory of length $T$. Our sample complexity bound $\overset{\sim}{\Omega}\left( {({p + 1})}^{L + 1} \right)$ grows exponentially with the history length $L$ (where $p$ is the input dimension), which correctly captures the dependence on the number of unknown Markov-like parameters (growing exponentially with $L$). For stable bilinear systems (defined in §2.2), this can be mitigated by choosing a smaller history of inputs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Input choice and stability: Stability of BLDS is typically input dependent. We work with a novel notion of stability. ‣ Uniform stability in bilinear dynamical systems: ‣ 2.2 Input Choice & Stability of Bilinear Dynamical Systems ‣ 2 Preliminaries ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems")) that generalizes the classic notion of stability for LDS to the BLDS. We also define a notion of stability radius which governs our choice of inputs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Persistence of excitation: Of independent interest, we establish the persistence of excitation ) for a broader class of inputs (possibly heavy-tailed) satisfying a hyper-contractivity condition. Our persistence of excitation result holds for nonlinear, correlated, and heavy-tailed covariates (i.e., the input features).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerical experiments: Lastly, we perform experiments with synthetic data to verify our theoretical findings. Interestingly, our experiments show that exciting the system with inputs sampled uniformly at random from a sphere leads to better estimation of Markov-like parameters as compared to Gaussian inputs, empirically reinforcing our theory on choice of inputs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows: § sets up the problem and introduces the notion of stability. § provides our main result on learning Markov-like parameters of partially observed BLDS. § discusses our proof idea, and provides persistence of excitation result for a broader class of inputs. Lastly, we perform numerical experiments in §, and conclude with a discussion of future directions in §.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a partially observed bilinear dynamical system with the following state-space representation: for all $t \geq 0$,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this work, we wish to identify the unknown parameters of the system from a single trajectory of input-output samples ${\{{({\mathbf{u}}_{t},{\mathbf{y}}_{t})}\}}_{t = 1}^{T}$. To that end, we focus on the task of learning the so-called *Markov-like parameters* of the system. Once learned, these Markov-like parameters can be exploited using the classic Ho-Kalman algorithm to recover the unknown matrices of the system up to some similarity transform as will be described in §. Next, we clarify our choice of inputs and discuss the required stability assumption.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Stability of bilinear dynamical systems is typically input dependent. To see that, we can unroll the state dynamics in (2.1) to write: for all $t \geq 0$,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

where we define ${{\mathbf{u}}_{t} \circ {\mathbf{A}}}:={{\mathbf{A}}_{0} + {\sum_{k = 1}^{p}{{({\mathbf{u}}_{t})}_{k}{\mathbf{A}}_{k}}}}$ for the ease of notation. Then, observe that the products of matrices $\prod_{k = 0}^{\ell - 1}{({{\mathbf{u}}_{t - k} \circ {\mathbf{A}}})}$ may grow exponentially in norm if we consistently choose large inputs. This is precisely why stability in bilinear dynamical systems is more challenging than other classes of systems such as linear dynamical systems or switched systems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Traditionally, notions like Mean Square Stability (MSS) have been considered to reason about the stability behavior of bilinear systems. Typically, these notions are asymptotic in nature, require distributional assumptions on the inputs, permit diverging trajectories with nonzero probability, and may not allow us to obtain tight guarantees. We introduce an alternative notion of stability that naturally generalizes the classical notion of stability in standard LTI systems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Input choice", "weight": 1.0} -->

We consider that the inputs ${\{{\mathbf{u}}_{t}\}}_{t \geq 0}$ are sampled in an i.i.d. manner from some distribution $\mathcal{D}_{\mathbf{u}}$ on ${\mathbb{R}}^{p}$. For ease of exposition, we will focus on the case where inputs are sampled uniformly at random from a sphere of radius $\sqrt{p}$, that is, ${\mathbf{u}}_{t} \sim {{Unif}{({\sqrt{p} \cdot \mathcal{S}^{p - 1}})}}$. More generally, as long as the inputs are isotropic and are bounded with high probability, our results will still hold at the expanse of longer proofs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Input choice", "weight": 1.0} -->

Putting together this input choice with the stability definition, we are now ready to present the assumption we make on the stability of the bilinear system (2.1).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

There exists $\kappa \geq 1$ and $\rho \in {}$ such that the partially observed bilinear dynamical system (2.1) is $({\sqrt{p} \cdot \mathcal{S}^{p - 1}},\kappa,\rho)$-uniformly-stable.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

In view of Assumption. ‣ Input choice: ‣ 2.2 Input Choice & Stability of Bilinear Dynamical Systems ‣ 2 Preliminaries ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems"), choosing inputs uniformly at random from $\sqrt{p} \cdot \mathcal{S}^{p - 1}$ guarantees stability almost surely. More generally, we can choose to sample inputs from any set $\mathcal{U}$, so long as the system is stable under such set in the sense of Definition -uniform-stability). ‣ Uniform stability in bilinear dynamical systems: ‣ 2.2 Input Choice & Stability of Bilinear Dynamical Systems ‣ 2 Preliminaries ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems"). However, the quality of estimation depends on whether inputs sampled from $\mathcal{U}$ are persistently exciting or not (see §4.1).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Learning the Markov-like Parameters", "weight": 1.0} -->

The Markov-like parameters are defined in a similar vein (except nonlinear input-output map) to the classical Markov parameters for partially observed LTI systems. By unrolling the dynamics (2.1),

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learning the Markov-like Parameters", "weight": 1.0} -->

We can simplify the form of (3.1) by adopting a more convenient notation and expanding further some of the products that involve the inputs. First, we introduce $\mathbf{\epsilon}_{t}:={{\mathbf{C}}\left( {\prod_{\ell = 1}^{L}{({{\mathbf{u}}_{t - \ell} \circ {\mathbf{A}}})}}) \right.{\mathbf{x}}_{t

<!-- chunk {"id": "body-0026", "role": "body", "section": "Learning the Markov-like Parameters", "weight": 1.0} -->

With the dynamics written in the form of (3.4), it is natural to use the least squares estimation method to learn the Markov-like parameters from the observations ${\{{\mathbf{y}}_{t},{\mathbf{u}}_{t}\}}_{t = 1}^{T}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sample Complexity Analysis", "weight": 1.0} -->

where we use the submultiplicativity of $\parallel \cdot \parallel_{\text{op}}$ and the triangular inequality. Next, we will analyze each of three terms appearing in the decomposition above separately and obtain corresponding bounds in high probability. Once these bounds have been established, the proof concludes immediately (see details in Appendix C.1). In what follows, we focus on presenting the results regarding the analysis of the three terms. We note that the challenge in analyzing this terms lies in the presence of non-trivial dependencies and nonlinearities. As such, recent analysis tools from the non-asymptotic system identification literature do not apply, and this is precisely what we manage to tackle.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Persistence of Excitation", "weight": 1.0} -->

We show persistence of excitation which is necessary to ensure that the LSE is a consistent estimator. More precisely, we will establish that smallest singular value of the design matrix $\overset{\sim}{\mathbf{U}}$ whose rows correspond to ${\{{\overset{\sim}{\mathbf{u}}}_{t}^{\top}\}}_{t = L}^{T}$ is bounded from below by $\overset{\sim}{\Omega}{(\sqrt{{T - L} + 1})}$. One of the major sources of difficulty in establishing this persistence of excitation result challenging is the nonlinear dependence of ${\overset{\sim}{\mathbf{u}}}_{t}$ on ${\mathbf{u}}_{t - L},\ldots,{\mathbf{u}}_{t}$ for all $t \geq L$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Persistence of Excitation", "weight": 1.0} -->

We need to understand how distributional properties of the input impact the lower spectrum of ${\overset{\sim}{\mathbf{U}}}^{\top}\overset{\sim}{\mathbf{U}}$. To that end, we start by introducing the property of hypercontractivity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 2 (Distributional properties of the input)", "weight": 1.0} -->

Again, it can be verified that Assumption. ‣ 4.1 Persistence of Excitation ‣ 4 Sample Complexity Analysis ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems") is satisfied by inputs sampled from $\mathcal{N}{(0,{\mathbf{I}}_{p})}$ or ${Unif}{({\sqrt{p} \cdot \mathcal{S}^{p - 1}})}$. More importantly, Assumption. ‣ 4.1 Persistence of Excitation ‣ 4 Sample Complexity Analysis ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems") covers a wide range of input distributions that may even be heavy-tailed, as it only requires conditions on the first four moments of the distribution. This contrast with classical assumptions that require the input distribution to have sub-Gaussian tails, and is also consistent with the intuition that bounding the smallest singular value of random matrix requires weaker moment conditions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Analysis of the Truncation Bias", "weight": 1.0} -->

Indeed, first, the sequences ${\{{\overset{\sim}{\mathbf{u}}}_{t}\}}_{t \geq L}$ and ${\{\mathbf{\epsilon}_{t}\}}_{t \geq L}$ are non-trivially dependent, and second, $\mathbf{\epsilon}_{t}$ is only zero-mean conditioned on future inputs ${\mathbf{u}}_{t - L},\ldots,{\mathbf{u}}_{T}$ and is still dependent on ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{t - L - 1}$. It is worth noting that this type of dependence does not arise when learning partially observed linear dynamical systems.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Analysis of the Truncation Bias", "weight": 1.0} -->

Indeed, the analysis of the truncation bias term in linear systems involves $\mathbf{\epsilon}_{t}$ that are only dependent on the covariates ${\mathbf{x}}_{t - L}$ and are independent of ${\mathbf{u}}_{t - L},\ldots,{\mathbf{u}}_{t}$. In addition to that, when learning linear systems $L$ can be made large enough to trivially bound the truncation bias, whereas in bilinear systems our bounds pay exponential dependence on $L$ so choosing this parameter more carefully is more important.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In Figure, we plot the estimation error ${\|{{\mathbf{G}} - \hat{\mathbf{G}}}\|}_{\text{op}}^{2}$ over different values of $\rho_{0},\rho_{k},L$ and $T$. Each experiment is repeated $10$ times and we plot the mean and one standard deviation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Figure 1(a) ‣ Figure 1 ‣ 5 Numerical Experiments ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems") and Figure 1(c) ‣ Figure 1 ‣ 5 Numerical Experiments ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems") correspond to estimation with Gaussian inputs ${\{{\mathbf{u}}_{t}\}}_{t \geq 0}\overset{\text{i.i.d.}}{\sim}\mathcal{N}{(0,{\mathbf{I}}_{p})}$, whereas, Figure 1(b) ‣ Figure 1 ‣ 5 Numerical Experiments ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems") and Figure 1(d) ‣ Figure 1 ‣ 5 Numerical Experiments ‣ Finite Sample Identification of Partially Observed Bilinear Dynamical Systems") correspond to estimation with uniformly distributed inputs ${\{{\mathbf{u}}_{t}\}}_{t \geq

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We observe double descent curves for $L = 7$. This is because our regression problem is unregularized and has ${{{({p + 1})}^{L} + p} - 1} = 2188$ unknown parameters, and the number of input-features (${\overset{\sim}{\mathbf{u}}}_{t}$) is $T - 7$. Hence, for $L = 7$, we see the peak at $T = 2195$, and the error decays smoothly after this point. Note that the peak occurs at ${T - L} = {{{({p + 1})}^{L} + p} - 1}$ (where the number of unknown parameters become equal to the number of input-features). For $L = {\{ 5,6\}}$, we do not see the double descent because we start at $T = 1000$ which is greater than ${{({p + 1})}^{L} + p} - 1$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion and Future Direction", "weight": 1.5} -->

We provide the first non-asymptotic learning bounds for partially observed BLDS. Given finite input-output data sampled from a single trajectory of BLDS, we learn its Markov-like parameters, provide an upper bound on the estimation error with $\overset{\sim}{\mathcal{O}}{({1/\sqrt{T}})}$ dependence, and provide a bound on the number of samples required, scaling as $\overset{\sim}{\Omega}\left( {({p + 1})}^{L + 1} \right)$. These parameters uniquely characterize the input-output map of a BLDS via nonlinear input features, hence, can be used to recover the state-space matrices. Our results hold under a novel notion of stability that generalizes the classic notion of stability for LDS to the BLDS.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion and Future Direction", "weight": 1.5} -->

There are several interesting future directions. First, can the exponential dependence on $L$ be avoided? We believe this can be done by carefully designing the inputs such that the number of Markov-like parameters do not grow exponentially in $L$. Second, can our results be extended to account for marginally-stable BLDS? This requires stabilization of a partially observed BLDS with unknown state-space matrices which itself is an interesting future direction. Other possible directions include exploring the benefit of regularization (e.g., Hankel nuclear norm regularization) for BLDS identification, exploring gradient-based methods for learning partially observed BLDS, and adaptive control of BLDS.
