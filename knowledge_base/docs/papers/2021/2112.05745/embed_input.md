<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis

Topics include Model predictive control, Predictive control, Safety, Robustness, Neural networks, Accuracy, Sampling-based methods, Control, Sampling, Convex hull.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we analyze an efficient sampling-based algorithm for general-purpose reachability analysis, which remains a notoriously challenging problem with applications ranging from neural network verification to safety analysis of dynamical systems. By sampling inputs, evaluating their images in the true reachable set, and taking their epsilon-padded convex hull as a set estimator, this algorithm applies to general problem settings and is simple to implement. Our main contribution is the derivation of asymptotic and finite-sample accuracy guarantees using random set theory. This analysis informs algorithmic design to obtain an epsilon-close reachable set approximation with high probability, provides insights into which reachability problems are most challenging, and motivates safety-critical applications of the technique. On a neural network verification task, we show that this approach is more accurate and significantly faster than prior work. Informed by our analysis, we also design a robust model predictive controller that we demonstrate in hardware experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Forward reachability analysis entails characterizing the reachable set of outputs of a given function corresponding to a set of inputs. This type of analysis underpins a plethora of applications in model predictive control, neural network verification, and safety analysis of dynamical systems. Sampling-based reachability analysis techniques are a particularly simple class of methods to implement; however, conventional wisdom suggests that if insufficient representative samples are considered, these methods may not be robust in that they cannot rule out edge cases missed by the sampling procedure. Alternatively, by leveraging structure in specific problem formulations or computational methods designed for exhaustivity (e.g., branch and bound), a large range of algorithms with deterministic accuracy and performance guarantees have been developed. However, these methods often sacrifice simplicity and generality for their power, motivating the development of algorithms that avoid such restrictions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we analyze a simple yet efficient sampling-based algorithm for general-purpose reachability analysis. As depicted in Figure 1, it consists of 1) sampling inputs, 2) propagating these inputs, and 3) taking the padded convex hull of these output samples. We refer to this Randomized Uncertainty Propagation algorithm as $\epsilon$-RandUP: it is simple to implement, benefits from statistical accuracy guarantees, and applies to a wide range of problems including reachability analysis of uncertain dynamical systems with neural network controllers.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

it works with any choice of possibly nonlinear reachability maps and non-convex input sets,

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

its estimate of the reachable set is conservative with high probability and tighter than prior work,

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

it is efficient and does not require precomputations, which is a key advantage for learning-based control applications where uncertainty bounds and models are updated in real-time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is a thorough analysis of the statistical properties of $\epsilon$-RandUP.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove that the set estimator converges to the $\epsilon$-padded convex hull of the true reachable set as the number of samples increases. Our assumption about the sampling distribution is weaker than in related work and implies that sampling the boundary of the input set is sufficient. This asymptotic result justifies using $\epsilon$-RandUP as a thrustworthy baseline for offline validation whenever the reachability map and the input set are complex and no tractable algorithm exists.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive a finite-sample bound for the Hausdorff distance between the output of $\epsilon$-RandUP and the convex hull of the true reachable set, assuming that the reachability map is Lipschitz continuous. This result informs algorithmic design (e.g., how to choose the number of samples to obtain an $\epsilon$-accurate approximation with high probability), sheds insights into which problems are most challenging, and motivates using this simple algorithm in safety-critical applications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate $\epsilon$-RandUP on a neural network controller verification task and show that it is highly competitive with prior work. We also embed this algorithm within a robust model predictive controller and present hardware results demonstrating the reliability of the approach.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem definition", "weight": 1.0} -->

Let $\mathcal{X} \subset {\mathbb{R}}^{p}$ be a compact nonempty set of inputs and $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{n}}$ be a continuous function. In this work, we tackle the general problem of reachability analysis, i.e., characterizing the set of reachable outputs $y = {f{(x)}}$ for all possible inputs $x \in \mathcal{X}$. This problem is also often referred to as uncertainty propagation. Mathematically, the objective consists of efficiently computing an accurate approximation of the reachable set $\mathcal{Y} \subset {\mathbb{R}}^{n}$, which is defined as

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem definition", "weight": 1.0} -->

To tackle this problem, $\epsilon$-RandUP relies on the choice of three parameters: a number of samples $M \in {\mathbb{N}}$, a padding constant $\epsilon > 0$, and a sampling distribution ${\mathbb{P}}_{\mathcal{X}}$ on measurable subsets of ${\mathbb{R}}^{p}$. As depicted in Figure 1, $\epsilon$-RandUP consists of sampling $M$ independent identically-distributed inputs $x_{i}$ in $\mathcal{X}$ according to ${\mathbb{P}}_{\mathcal{X}}$, of evaluating each output $y_{i} = {f{(x_{i})}}$, and of computing the $\epsilon$-padded convex hull

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem definition", "weight": 1.0} -->

Our analysis hinges on the observation that the reachable set estimator ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$ is a random compact set, i.e., ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$ is a random variable taking values in the family of nonempty compact sets $\mathcal{K}$. We refer to Appendix A for rigorous definitions using random set theory. Intuitively, different input samples $x_{i}$ in $\mathcal{X}$ induce different output samples $y_{i}$ in $\mathcal{Y}$, resulting in different approximated reachable sets ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$. To characterize the accuracy of the estimator, we use the Hausdorff metric, which is defined as

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem definition", "weight": 1.0} -->

This metric induces a topology and an associated $\sigma$-algebra, which enables rigorously defining random compact sets as random variables and describing their convergence; see Appendix A. Interestingly, the distribution of a random compact set is characterized by the probability that it intersects any given compact set. We use this fact in Sections 4 and 5, where we characterize the probability that the set estimator ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$ intersects well-chosen sets along the boundary of the true reachable set. By analyzing the distribution of ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$, this approach allows bounding the Hausdorff distance between ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$ and the convex hull of the true reachable set $\text{H}{(\mathcal{Y})}$ with high probability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Asymptotic analysis", "weight": 1.0} -->

In this section, we provide an asymptotic analysis under minimal assumptions about the input set and the reachability map (namely, that $\mathcal{X}$ is compact and $f$ is continuous). To enable the reconstruction of the true convex hull $\text{H}{(\mathcal{Y})}$ using the sampling-based set estimator ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$, we make one assumption about the sampling distribution ${\mathbb{P}}_{\mathcal{X}}$ for the inputs $x_{i}$. Note that by definition, ${{\mathbb{P}}_{\mathcal{X}}{(\mathcal{X})}} = 1$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

This assumption states that the probability of sampling an output arbitrarily close to any point on the boundary of the true reachable set is strictly positive. In other words, the boundary of the reachable set should be contained in the support of the distribution of the output samples $y_{i}$. Assumption 1 is weaker than the associated assumption, which can be restated as "${{\mathbb{P}}_{\mathcal{X}}{({f^{- 1}{(A)}})}} > 0$ for any open set $A \subset {\mathbb{R}}^{n}$ such that ${\mathcal{Y} \cap A} \neq \varnothing$". Indeed, Assumption 1 only considers open neighborhoods of the boundary $\partial\mathcal{Y}$, as opposed to all open sets intersecting $\mathcal{Y}$. Selecting a sampling distribution ${\mathbb{P}}_{\mathcal{X}}$ that satisfies Assumption 1 is easy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For instance, if $\mathcal{X}$ has a smooth boundary (see Assumption 4), then the uniform distribution over $\mathcal{X}$ satisfies Assumption 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 is sufficient to prove that the random set estimator ${\hat{\mathcal{Y}}}_{\epsilon}^{M}$ converges to the $\epsilon$-padded convex hull of $\mathcal{Y}$ as the number of samples $M$ increases. Below, we prove a more general result which allows for variations of the padding radius $\epsilon$ as the number of samples increases.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Finite-sample analysis", "weight": 1.0} -->

Theorem 1 ‣ 4 Asymptotic analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis") provides asymptotic convergence guarantees that support the application of $\epsilon$-RandUP in general scenarios (e.g., as a baseline for offline validation in complex problem settings), but does not provide finite-sample guarantees which are of practical interest in safety-critical applications. Deriving stronger statistical guarantees requires leveraging more information about the structure of the problem. We derive finite-sample rates under general assumptions in Section 5.1 and analyze a particular case in Section 5.2. We discuss practical implications of our results in Section 5.3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "General finite-sample statistical guarantees", "weight": 1.0} -->

To derive convergence rates and outer-approximation guarantees given a finite number of samples $M$, we first make an assumption about the smoothness of the reachability map $f$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Next, we make an assumption about the sampling distribution ${\mathbb{P}}_{\mathcal{X}}$ along the input set boundary $\partial\mathcal{X}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Given any boundary input $x \in {\partial\mathcal{X}}$, the constant $\Lambda_{\epsilon}^{L}$ characterizes the probability of sampling an input $x_{i}$ that is $\epsilon/{({2L})}$-close to $x$. Selecting a sampling distribution that satisfies Assumption 3 is simple; we provide examples in Sections 5.2 and 6. As we show next, these two assumptions are sufficient to derive finite-sample convergence rates for $\epsilon$-RandUP. Recall that $D{({\partial\mathcal{X}},d)}$ denotes the $d$-packing number of $\partial\mathcal{X}$, which is necessarily finite by the compactness of $\mathcal{X}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Analysis of a particular setting: smooth input set and continuous distribution", "weight": 1.0} -->

In many applications, the boundary of the input set is smooth (e.g., $\mathcal{X}$ is a $2$-norm ball). In this setting, we can apply Theorem 2. ‣ 5.1 General finite-sample statistical guarantees ‣ 5 Finite-sample analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis") to derive finite-sample guarantees for general continuous sampling distributions. We state this smoothness assumption below.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Assumption 4 guarantees that for any parameter $x$ on the boundary $\partial\mathcal{X}$, one can find a ball of radius $r$ contained in $\mathcal{X}$ that also contains $x$, see Figure 2. This assumption corresponds to a general inwards-curvature condition of the boundary $\partial\mathcal{X}$. It is a common assumption in the literature and is related to the notion of reach that bounds the curvature of the boundary $\partial\mathcal{X}$. To guarantee its satisfaction, one can replace $\mathcal{X}$ with $\mathcal{X} \oplus {B{(0,r)}}$ before performing reachability analysis, which would yield a more conservative estimate of $\mathcal{Y}$. Next, we state an assumption about the sampling distribution ${\mathbb{P}}_{\mathcal{X}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

This assumption states that the sampling distribution admits a lower-bounded continuous density. Specifically, there exists a density function $p_{\mathcal{X}}:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}_{+}}$ such that ${{\mathbb{P}}_{\mathcal{X}}{(A)}} = {\int_{A}{p_{\mathcal{X}}{(x)}\text{d}x}} \geq {p_{0}{\int_{A}{\text{d}x}}} = {p_{0}\lambda{(A)}}$ for any measurable subset $A \subset \mathcal{X}$. For instance, the uniform distribution over $\mathcal{X}$ satisfies this assumption. Similarly to Assumption 3, this density assumption can be relaxed to neighborhoods of $\partial\mathcal{X}$; we leave this extension for future work. We obtain the following corollary.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Insights: the difficulty of reachability analysis and algorithmic design", "weight": 1.0} -->

Assuming the smoothness of $f$ is necessary: given an input set $\mathcal{X}$ and a sampling distribution ${\mathbb{P}}_{\mathcal{X}}$, one can construct problems for which sampling-based reachability analysis algorithms require arbitrarily many samples to compute an $\epsilon$-accurate approximation of $\mathcal{Y}$, see Section 6.1. To derive finite-sample rates, assuming that the reachability map $f$ is $L$-Lipschitz (Assumption 2) is necessary if only assumptions on input coverage density (Assumption 3) are available.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Insights: the difficulty of reachability analysis and algorithmic design", "weight": 1.0} -->

The smoother the easier: a smaller Lipschitz constant $L$ and a larger radius parameter $r$ induce tighter bounds in Theorem 2. ‣ 5.1 General finite-sample statistical guarantees ‣ 5 Finite-sample analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis"), requiring a smaller number of samples $M$ to obtain a desired accuracy with high probability $1 - \delta_{M}$. Indeed, such conditions guarantee a lower bound on the probability of sampling outputs $y_{i} = {f{(x_{i})}} \in \mathcal{Y}$ that are close to the boundary $\partial\mathcal{Y}$, which is necessary to accurately reconstruct the true convex hull of the reachable set from samples.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Insights: the difficulty of reachability analysis and algorithmic design", "weight": 1.0} -->

Scalability: by Theorem 2. ‣ 5.1 General finite-sample statistical guarantees ‣ 5 Finite-sample analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis"), the number of required samples to reach a desired $\epsilon$-accuracy with high probability depends on the covering number. This constant characterizes the size of the parameter space in terms of dimensionality (the number of different parameters) and volume (variations of each parameter). Given any $\mathcal{X} \in \mathcal{K}$ and $d = {\sup_{x \in {\partial\mathcal{X}}}{\| x\|}}$, a simple and general bound for the covering number is ${D{({\partial\mathcal{X}},\epsilon)}} \leq \left( {{2d\sqrt{n}}/\epsilon} \right)^{n}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results and applications", "weight": 1.0} -->

We perform a sensitivity analysis in Section 6.1 to illustrate the insights from Theorem 2. ‣ 5.1 General finite-sample statistical guarantees ‣ 5 Finite-sample analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis"). In Section 6.2, we compute the reachable sets of a dynamical system with a simple neural network policy and compare with prior work. Finally, in Section 6.3, we embed $\epsilon$-RandUP in a model predictive control (MPC) framework to reliably control a robotic platform. Our code and hardware results are available at and All computation times are measured on a computer with a 3.70GHz Intel Core i7-8700K CPU.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sensitivity analysis", "weight": 1.0} -->

We analyze the sensitivity of $\epsilon$-RandUP to the sampling distribution and the smoothness of the reachability map. We consider a $2$-dimensional input ball $\mathcal{X} = {B{}}$ and the map ${f{(x)}} = {({Lx_{1}},x_{2})}$ with $L \geq 1$. Clearly, $\mathcal{X}^{\mathsf{c}}$ is $1$-convex and $f$ is $L$-Lipschitz continuous, so Corollary 3 applies for any sampling distribution satisfying Assumption 5.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sensitivity analysis", "weight": 1.0} -->

We consider a distribution ${\mathbb{P}}_{\mathcal{X}}^{\alpha}$ that depends on a parameter $\alpha \geq 1$, such that ${\mathbb{P}}_{\mathcal{X}}^{\alpha}$ varies from a uniform distribution over $\mathcal{X}$ for $\alpha = 1$ to a uniform distribution over the boundary $\partial\mathcal{X}$ as $\alpha\rightarrow\infty$. Given $\delta_{M} = 10^{- 3}$, we determine the minimum padding $\epsilon$ guaranteeing ${{\mathbb{P}}{({{d_{H}{({\hat{\mathcal{Y}}}^{M},\mathcal{Y})}} \leq \epsilon})}} \geq {1 - \delta_{M}}$ using Corollary 3, see Appendix E.1. We take $M = 1000$ samples and present results in Figure 3.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sensitivity analysis", "weight": 1.0} -->

We observe better performance than the predicted finite-sample bounds and that distributions with a higher probability of sampling close to the boundary (i.e., larger values of $\alpha$) perform better, corresponding to lower Hausdorff distance errors. Also, $\epsilon$-RandUP performs better on problems with smoother reachability maps, as is visible from our empirical evaluation and theoretical bounds on the Hausdorff distance. This validates the discussion in Section 5.3.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Verification of neural network controllers", "weight": 1.0} -->

We compare $\epsilon$-RandUP with the formal method ReachLP ^11^1Comparisons with ReachSDP, which is more conservative than ReachLP, show a similar trend. and with two recently-derived sampling-based approaches: the kernel method proposed in and GoTube. We implement GoTube using the $\epsilon$-RandUP algorithm where we replace the last convex hull bounding step with an outer-bounding ball. As ground-truth, we use the reachable sets from $\epsilon$-RandUP with $\epsilon = \, 0$ and $M = \, 10^{6}$, which is motivated by the asymptotic results from Theorem 1 ‣ 4 Asymptotic analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis") and was previously done. We refer to Appendix E.2 for details and present results in Figures 4 and 5.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Verification of neural network controllers", "weight": 1.0} -->

Formal methods that explicitly bound the output of each layer of the neural network can guarantee that their reachable set approximations are always conservative. However, obtaining tight approximations with ReachLP requires splitting the input set: a computationally expensive procedure (Fig. 5, bottom). Figures 4 and 5 show that ReachLP is more conservative than $\epsilon$-RandUP even when considering polytopic outputs with eight facets. As shown in Figure 4 (right), the conservatism of these methods increases over time. This shows that even when considering small neural networks, verifying safety specifications over long horizons remains an open challenge.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Verification of neural network controllers", "weight": 1.0} -->

Sampling-based approaches do not suffer from the long-horizon conservatism of formal methods. This comes at the expense of probabilistic guarantees (that rely on knowledge of the Lipschitz constant of the model), as opposed to deterministic conservatism guarantees. $\epsilon$-RandUP and GoTube have comparable computation time^22^2Plotting the kernel-based level set estimator in from $M$ samples requires classifying a dense grid of points. To evaluate the computation time of this method, we only account for the time to classify $M$ new samples. and are significantly faster than other approaches. $\epsilon$-RandUP is significantly more accurate than prior work, especially for larger values of $M$. Also, the results from Theorem 2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Verification of neural network controllers", "weight": 1.0} -->

‣ 5.1 General finite-sample statistical guarantees ‣ 5 Finite-sample analysis ‣ A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis") allow for principled hyperparameter selection for $\epsilon$-RandUP: given $\epsilon = 0.02$, sampling $1400$ uniformly-distributed inputs on $\partial\mathcal{X}$ is sufficient for the output sets to be conservative with probability at least $1 - 10^{- 4}$ (for $L = 1$, see Section E.2).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Verification of neural network controllers", "weight": 1.0} -->

These experiments show that for short-horizon problems ($5$ steps) with relatively simple network architectures, both ReachLP and $\epsilon$-RandUP return accurate reachable set approximations. For longer-horizon problems ($9$ steps) with networks of moderate dimensions (which allows using existing methods to pre-compute a Lipschitz constant, see and Section D), $\epsilon$-RandUP is guaranteed to efficiently return non-overly-conservative reachable set approximations with high probability. Finally, though we do not present such results here, the generality of $\epsilon$-RandUP allows it to tackle complex model architectures (see for experiments with longer horizons and more complex networks with uncertain weights) for which no alternative methods exist, albeit without finite-sample accuracy guarantees.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Application to robust model predictive control", "weight": 1.0} -->

Finally, we show that $\epsilon$-RandUP can be embedded in a robust MPC formulation to reliably control a planar spacecraft system actuated by cold-gas thrusters. Its state at time $t \geq 0$ is denoted as $x_{t} \in {\mathbb{R}}^{6}$ and its control inputs are given as $u_{t} \in {\mathbb{R}}^{3}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Application to robust model predictive control", "weight": 1.0} -->

We use an auxiliary linear feedback controller and an uncertain linear model $x_{t + 1} = {f{(x_{t},u_{t},m,F)}}$ that depends on an uncertain mass $m \in {{\lbrack 10,18\rbrack}\text{kg}}$ (depending on the payload transported by the robot and the current weight of the gas tanks) and an unknown force $F = {(F_{x},F_{y})} \in {{\lbrack{- 0.015},0.015\rbrack}^{2}\text{N}}$ that accounts for the tilt of the table.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Application to robust model predictive control", "weight": 1.0} -->

To control the system from an initial state $x_{0} \in {\mathbb{R}}^{n}$ to a goal region $\mathcal{X}_{\text{goal}} \subset {\mathbb{R}}^{n}$ while minimizing fuel consumption and remaining in a feasible set $\mathcal{X}_{\text{free}}$ (i.e.,

<!-- chunk {"id": "body-0042", "role": "body", "section": "Application to robust model predictive control", "weight": 1.0} -->

The numerical implementation is described. With a Python implementation, $\epsilon = 0.03$, and $M = 10^{3}$, our MPC controller runs at $10$Hz which is sufficient for this platform and could be improved, e.g., by parallelizing computations on a GPU. We compare with a MPC baseline that does not consider uncertainty over the parameters (i.e., assumes ${(m,F)} \in {{\{ 14\}} \times {\{{}\}}}$). As shown in Figure 6 and in the attached video, this baseline is unsafe and collides with an obstacle. In contrast, our reachability-aware controller is recursively feasible, satisfies all constraints, and allows safely reaching the goal. These experiments motivate the development of efficient reachability algorithms that can be embedded in generic control frameworks to account for uncertain parameters.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We derived new asymptotic and finite-sample statistical guarantees for $\epsilon$-RandUP, a simple yet efficient algorithm for reachability analysis of general systems. We demonstrated its efficacy for a neural network verification task and its applicability to robust model predictive control. In future work, we will investigate tighter finite-sample bounds by leveraging further information about the smoothness of the input set boundary $\partial\mathcal{X}$. Of practical interest is investigating which sampling distributions enable better sample efficiency, interfacing $\epsilon$-RandUP with Lipschitz constant computation methods (e.g., for neural networks), exploring methods to scale to high-dimensional input spaces, and applying the technique to safety-aware reinforcement learning.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The authors thank Robin Brown for her helpful feedback and insightful discussions about neural network verification, Edward Schmerling for his helpful comments and suggestions, and Adam Thorpe for helpful discussions about kernel methods. The NASA University Leadership Initiative (grant #80NSSC20M0163) provided funds to assist the authors with their research, but this article solely reflects the opinions and conclusions of its authors and not any NASA entity. NVIDIA provided funds to assist the authors with their research. L.J. was supported by the National Science Foundation via grant CBET-2112085.
