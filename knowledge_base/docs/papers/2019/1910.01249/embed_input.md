<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Analyzing the Variance of Policy Gradient Estimators for the Linear-Quadratic Regulator

Topics include Policy gradients.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the variance of the REINFORCE policy gradient estimator in environments with continuous state and action spaces, linear dynamics, quadratic cost, and Gaussian noise. These simple environments allow us to derive bounds on the estimator variance in terms of the environment and noise parameters. We compare the predictions of our bounds to the empirical variance in simulation experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient (PG) algorithms are widely used for reinforcement learning (RL) in continuous spaces. PG methods construct an unbiased estimate of the gradient of the RL objective with respect to the policy parameters. They do so without the complication of intermediate steps of dynamics modeling or value function approximation. However, the gradient estimate is known to suffer from high variance. This makes PG methods sample-inefficient with respect to environment interaction, creating an obstacle for applications to real physical systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we seek a more detailed understanding of how the PG gradient estimate variance relates to properties of the continuous-space Markov decision process (MDP) that defines the RL problem instance. Such characterization is well-developed for discrete state spaces, but in continuous spaces, a detailed breakdown is not possible without further restrictions on the set of MDPs and the policy class. We choose to examine systems with linear dynamics, linear policy, quadratic cost, and Gaussian noise, known as LQR systems in control theory.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

LQR systems are a popular case study for analyzing RL algorithms in continuous spaces. Fazel et al. show that the optimization landscape is neither convex nor smooth, but still admits global convergence and PAC-type complexity bounds for a zeroth-order optimization method that explores in parameter space. Malik et al. establish tighter error bounds with more detailed problem-dependence for the same class of algorithms, extended to include noisy dynamics. Yang et al. show convergence for an actor-critic method. Recht provide a broad overview including summaries of the group's prior work on model-based methods and value function approximation. Our variance bounds are similar to those of Malik et al., but we focus on characterizing the variance of policy gradient methods, which explore by taking random actions at each time step, rather than parameter-space exploration methods. Tu and Recht show related bounds for a restricted class of LQR systems as an intermediate step towards sample complexity results.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The earliest and simplest policy gradient algorithm is REINFORCE. More recent algorithms such as TRPO and PPO extend the basic idea of REINFORCE with techniques to inhibit the possibility of making very large changes in the policy action distribution in a single step. In a benchmark test, these algorithms generally learned better policies than REINFORCE, but their additional complexity makes them hard to analyze.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our primary contributions are derivations of bounds on the variance of the REINFORCE gradient estimate as an explicit function of the dynamics, reward, and noise parameters of the LQR problem instance. We validate our bounds with comparisons to the empirical gradient variance in random problems. We also explore the relationship between gradient variance and sample complexity, but find it to be less straightforward, as the problem parameters that affect variance also affect the optimization landscape. We emphasize that our goal is not to draw a conclusion about the utility of using REINFORCE to solve LQR problems, but rather to use LQR as an example system that is simple enough to allow us to "look inside" the REINFORCE policy gradient estimator.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem setting", "weight": 1.0} -->

In this section, we define the general finite-horizon reinforcement learning problem, the REINFORCE policy gradient estimator, and the LQR optimal control problem. We use the notation $\mathcal{P}{(\mathcal{X})}$ for the set of probability distributions over a measurable set $\mathcal{X}$. For arbitrary sets $\mathcal{X}$ and $\mathcal{Y}$, the set of all functions $\mathcal{X}\mapsto\mathcal{Y}$ is denoted as $\mathcal{Y}^{\mathcal{X}}$. Let $\parallel \cdot \parallel$ denote the $\ell_{2} - \ell_{2}$ operator norm of a matrix or the $\ell_{2}$ norm of a vector. The spectral radius (magnitude of largest eigenvalue) of a square matrix is denoted by $\rho{( \cdot )}$. The the set of positive semidefinite (resp.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Policy gradient algorithms", "weight": 1.0} -->

Suppose $\pi$ is parameterized by a real-valued vector $\theta$. Analytical gradient descent of ${\nabla_{\theta}J}{(\pi)}$ is not possible because $T$ and $r$ are only accessible via sampling, with unknown gradients. There exist generic derivative-free optimization algorithms that solve such problems via perturbations in parameter space, but in RL problems, it is also possible to explore via stochastic actions instead. The simplest policy gradient algorithm is REINFORCE, which relies on the following identity (assuming sufficient regularity conditions): An unbiased estimate of the latter expectation can be computed by executing $\pi$ in the MDP for one full trajectory. Unfortunately, this estimate is known to have high variance. Variance reduction is possible by exploiting the Markov property (past rewards are independent of future actions) and/or using control variates, but we analyze plain REINFORCE here for simplicity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "LQR systems", "weight": 1.0} -->

A discrete-time stochastic *linear-quadratic regulator* (LQR) system with state space $\mathcal{S} = {\mathbb{R}}^{n}$ and action space $\mathcal{A} = {\mathbb{R}}^{m}$ is defined by linear dynamics with additive Gaussian noise: for dynamics matrices ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$, and noise covariance $\Sigma_{s} \in {\mathbb{P}}_{+}^{n}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "LQR systems", "weight": 1.0} -->

The reward function is given by $r_{t} = {- {({{s_{t}^{T}Qs_{t}} + {a_{t}^{T}Ra_{t}}})}}$ for cost matrices ${Q \in {\mathbb{P}}_{+}^{n}},{R \in {\mathbb{P}}_{+ +}^{m}}$. Intuitively, the goal is to drive the state towards zero without using too much control effort. The initial state $s_{1}$ follows an arbitrary zero-mean Gaussian distribution. A well-known result in control theory states that, if the system $(A,B)$ is controllable, the infinite-horizon objective is maximized by a stationary linear policy ${a_{t} = {K^{\star}s_{t}}},{K^{\star} \in {\mathbb{R}}^{m \times n}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "LQR systems", "weight": 1.0} -->

The value of $K^{\star}$ depends on $(A,B,Q,R)$, but not on the distributions of $\Sigma_{s}$ or $s_{1}$. The same $K^{\star}$ is also the optimal controller for the deterministic version of the problem. $K^{\star}$ can be computed efficiently. To apply REINFORCE, the policy must be stochastic, so we consider linear stochastic policies for ${K \in {\mathbb{R}}^{m \times n}},{\Sigma_{a} \in {\mathbb{P}}_{+ +}^{m}}$. The state noise $\Sigma_{s}$ is an immutable property of the system, but the action noise $\Sigma_{a}$ is not. Instead, it is usually chosen by the user of the RL algorithm, or learned as a parameter using.

<!-- chunk {"id": "body-0013", "role": "body", "section": "LQR systems", "weight": 1.0} -->

Genuine noise in the system actuators can be subsumed into $\Sigma_{s}' = {\Sigma_{s} + {B\Sigma_{a}}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "LQR systems", "weight": 1.0} -->

In the RL literature, action noise is usually seen as either 1) a tool for exploring of the state space, 2) a method of regularization to avoid converging on bad local optima, or 3) a consequence of a probabilistic interpretation of the RL problem. Its effect on the RL optimization algorithm is less frequently discussed, but in this work we find that it can be significant.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Main result: Variance bounds on the REINFORCE estimator", "weight": 1.0} -->

In this section, we present bounds on the variance of the REINFORCE estimator for LQR systems. The instantiation of REINFORCE (eq. 2) for the system (eqs. 3, 4 and 5) using a single trajectory is: The estimate $\hat{g}$ is a function of the independent random variables ${\{\epsilon_{t}^{a},\epsilon_{t}^{s}\}}_{t = 1}^{H}$. Although $s_{t}$ is linear in ${\{\epsilon_{\tau}^{a},\epsilon_{\tau}^{s}\}}_{\tau = 1}^{t - 1}$, $r_{t}$ is quadratic in $s_{t}$, so the overall form of $\hat{g}$ is a product of a sum and a sum of products of sums.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main result: Variance bounds on the REINFORCE estimator", "weight": 1.0} -->

Therefore, while it is possible to apply matrix concentration inequalities to bound $\|{s_{t} - {{\mathbb{E}}{\lbrack s_{t}\rbrack}}}\|$ with high probability, it is more difficult to bound the dispersion of $\hat{g}$. Instead, we use a more specialized method to derive a bound on which we simplify by bounding ${\mathbb{E}}\left\lbrack {{\mathbf{t}\mathbf{r}}{({{\hat{g}}^{\top}\hat{g}})}} \right\rbrack$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments", "weight": 1.0} -->

(a) Relationship between Σs and Σa Figure 1: Comparison between our upper bound from Theorem 1 (top) and the empirically measured variance (bottom) as they relate to various parameters of the LQR problem. Behavior is qualitatively similar for action noise covariance (a) and control authority (b), but less similar for the stability (c) where our bounds are loose. Further discussion is in Sections 4, 4 and 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

In the first set of experiments, we compare our upper bound of $\nu{(\hat{g})}$ to its empirical value when executing REINFORCE in randomly generated LQR problems. Our results show qualitative similarity in the parameters for which our upper and lower bounds match. On the other hand, the gap with respect to stability-related parameters is also visible. For each experiment shown here, we repeated the experiment with different random seeds and observed qualitatively identical results.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

In each experiment, we vary some of these parameters systematically while holding the others constant, allowing us to visualize the impact of each parameter on $\nu{(\hat{g})}$. We plot the upper bound of Theorem 1 on the top row of Figure 1, and the empirical estimate of $\nu{(\hat{g})}$ on the bottom row. In both cases, since the variance depends on the initial state $s_{1}$, we sample $N = 100$ initial states $s_{1}$ from $\mathcal{N}{(0,{n^{- 1}I})}$ and plot ${\mathbb{E}}_{s_{1} \sim {\mathcal{N}{(0,{n^{- 1}I})}}}\nu{(\hat{g})}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Effect of $\\Sigma_{a}$", "weight": 1.0} -->

In this experiment, we generate a random LQR problem and replace $\Sigma_{a}$ with $\sigma_{a}I$ for $\sigma_{a}$ geometrically spaced in the range $\lbrack 10^{- 2},10^{2}\rbrack$. Using a scaled identity matrix is common practice when applying RL to a problem where there is no *a priori* reason to correlate the noise between different action dimensions. We evaluate the variance at the value $K = K^{\star}$, where $K^{\star}$ is the infinite-horizon optimal controller computed using traditional LQR synthesis, as described in Section 2. Using $K^{\star}$ ensures that ${\rho{({A + {BK}})}} < 1$, a required condition to apply Theorem 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Effect of $\\Sigma_{a}$", "weight": 1.0} -->

Results are shown in Figure 1(a). The separate line plots correspond to scaling the random $\Sigma_{s}$ by the values $\{ 0.1,1,10\}$, while the $x -$axis corresponds to the value of $\sigma_{a}$. For each value of $\sigma_{s}$, there appears to be a unique $\sigma_{a}$ that minimizes $\nu{(\hat{g})}$, and this value of $\sigma_{a}$ increases with $\sigma_{s}$. This phenomenon appears in both the bound and empirical variance.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Effect of $\\| B\\|$", "weight": 1.0} -->

In this experiment, we generate a random problem where $m = n$ and replace $B$ with $bI$ for $b$ geometrically spaced in the range $\lbrack 10^{- 2},10^{2}\rbrack$. The resulting system essentially gives the policy direct control over each state. For each $B$, we compute a separate infinite-horizon optimal $K$ and sample the variance for different $s_{1}$. Results are shown in Figure 1(b). The separate line plots correspond to scaling both the random $\Sigma_{s}$ and the random $\Sigma_{a}$ by the values $\{ 0.1,1,10\}$. The $x -$axis corresponds to the value of $b$. Again, there appears to be a unique $\| B\|$ that minimizes $\nu{(\hat{g})}$, but its value changes minimally for different magnitudes of $\Sigma_{s},\Sigma_{a}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Effect of $\\rho{({A + {BK}})}$", "weight": 1.0} -->

Here we measure the change in variance with respect to the closed-loop spectral radius $\rho{({A + {BK}})}$. To synthesize controllers $K$ such that $\rho{({A + {BK}})}$ obtains a specified value, we use the pole placement algorithm of Tits and Yang. A pole placement algorithm $\mathcal{P}$ is a function such that the eigenvalues of $A + {BK}$ are $\lambda_{1},\ldots,\lambda_{n}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Effect of $\\rho{({A + {BK}})}$", "weight": 1.0} -->

Then, for each desired $\rho$, we compute ${K_{\rho} = {\mathcal{P}{(A,B,{\rho\lambda_{1}},\ldots,{\rho\lambda_{n}})}}}.$ By rescaling the same set of $\lambda_{i}$ instead of sampling a new set for each $\rho$, we avoid confounding effects from changing other properties of $K$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Effect of $\\rho{({A + {BK}})}$", "weight": 1.0} -->

Results are shown in Figure 1(c). Again, we repeat the experiment for different magnitudes of $\Sigma_{s}$ and $\Sigma_{a}$. Unlike the previous two experiments, here we see qualitatively different behavior between our upper bound and the empirical variance. The bound begins to increase rapidly near $\rho = 1$, corresponding to the growth of $1/{({1 - \rho})}$ in the term $H'$, but at $\rho = 0.9$ the $H$ term becomes active in $H'$, and the bound suddenly flattens. In contrast, the empirical variance grows more moderately and does not explode near the threshold of system instability. This provides further evidence that the upper bound of Theorem 1 can be tightened to match the $\sqrt{H'}$ and $\sqrt{H}$ terms in the special-case lower bound of Theorem 2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dimensionality parameters", "weight": 1.0} -->

In all of the preceding experiments, we arbitrarily chose the state and action dimensions ${n = 5},{m = 3}$ and time horizon $H = 10$. To visualize the variance for other values of these parameters, we generate $1000$ random LQR problems with $n$ and $H$ each varying over the set $\{ 3,10,30\}$. We fix $m = {\lceil{n/2}\rceil}$. Results are shown in Figure 2. ‣ 4 Experiments ‣ Analyzing the Variance of Policy Gradient Estimators for the Linear-Quadratic Regulator"). The overall positive trend with a slope greater than $1$ shows that the bound grows superlinearly with respect to the empirical, as expected. One interesting property is the tighter clustering for large values of $n$. This may be due to several eigenvalue distribution results in random matrix theory which state that, as $n\rightarrow\infty$, our random LQR problems tend to become similar up to a basis change.

<!-- chunk {"id": "body-0027", "role": "body", "section": "RL learning curves for varying $\\Sigma_{a}$", "weight": 1.0} -->

The results in Section 4 suggest that, for a fixed $\Sigma_{s}$, the magnitude of $\Sigma_{a}$ has a significant effect on $\nu{(g)}$. This is of practical interest because $\Sigma_{a}$ is usually under control of the RL practitioner. It is therefore natural to ask if the change in variance corresponds to a change in the rate of convergence of REINFORCE. We test this empirically by executing REINFORCE in variants of one random LQR problem with different values of $\Sigma_{a}$ and $\Sigma_{s}$. To avoid a confounding effect from larger $\Sigma_{a}$ incurring greater penalty from the $- {a_{t}^{T}Ra_{t}}$ term in $r_{t}$, we evaluate the trained policies in a modified version of the problem where $\Sigma_{a} = \Sigma_{s} = \mathbf{0}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "RL learning curves for varying $\\Sigma_{a}$", "weight": 1.0} -->

As discussed in Section 2, the optimal $K^{\star}$ for the stochastic problem is also optimal for the deterministic problem, so each problem variant should converge to the same evaluation returns in the limit.

<!-- chunk {"id": "body-0029", "role": "body", "section": "RL learning curves for varying $\\Sigma_{a}$", "weight": 1.0} -->

We initialize $K$ by perturbing the elements of the LQR-optimal controller with i.i.d. Gaussian noise and scaling the perturbation until ${\rho{({A + {BK}})}} \approx 0.98$. After every $10$ iterations of REINFORCE, we evaluate the current policy in the noise-free environment. For each $(\Sigma_{a},\Sigma_{s})$ pair, we repeat this experiment $10$ times with different random seeds. The random seed only affects the $\epsilon_{t}^{a},\epsilon_{t}^{s}$ and $s_{1}$ samples. The aggregate data are shown in Figure 3. Shaded bands correspond to one standard deviation across the separate runs of REINFORCE. The lowercase $\sigma_{a},\sigma_{s}$ refer to scaling factors applied to the initial samples of $\Sigma_{a},\Sigma_{s}$ in the random LQR problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "RL learning curves for varying $\\Sigma_{a}$", "weight": 1.0} -->

The effect is quite different than one would predict from variance alone. For all values of $\Sigma_{s}$ in the experiment, problems with larger $\Sigma_{a}$ converge faster---whereas Figure 1(a) would suggest that the "optimal" value of $\Sigma_{a}$ changes with respect to $\Sigma_{s}$. The fact that larger $\Sigma_{a}$ tends to make REINFORCE converge faster is not obvious, given the $\Sigma_{a}^{- 1}$ term in $\hat{g}$. Also, when $\Sigma_{a}$ is very small and $\Sigma_{s}$ is very large, the algorithm becomes unstable and sees large variations across different random seeds. For the middle values $\Sigma_{a} \in {\{ 0.1,1.0\}}$, we observe that larger $\Sigma_{s}$ causes faster convergence.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we derived bounds on the variance of the REINFORCE policy gradient estimator in the stochastic linear-quadratic control setting. Our upper bound is fully general, while our lower bound applies to the scalar case at a stationary point. The bounds match with respect to all system parameters except the time horizon $H$ and stability $\rho{({A + {BK}})}$. We compared our bound prediction to the empirical variance in a variety of experimental settings, finding a close qualitative match in the parameters for which the bounds are tight.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our experiments in Section 4.1 plotting the empirical convergence rate of REINFORCE suggest that the effect of action noise $\Sigma_{a}$ on the overall RL performance is not fully captured by its effect on the variance. An interesting direction for future work would be to investigate the role of $\Sigma_{a}$ more closely and attempt to disentangle its effect on gradient magnitude, variance, exploration, and regularization. Such an analysis could lead to improved variance reduction methods or algorithms that manipulate $\Sigma_{a}$ to speed up the RL optimization.
