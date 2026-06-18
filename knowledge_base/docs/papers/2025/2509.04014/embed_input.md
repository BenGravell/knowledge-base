<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distance between Stochastic Linear Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While the existing stochastic control theory is well equipped to handle dynamical systems with stochastic uncertainties, a paradigm shift using distance measure based decision making is required for the effective further exploration of the field. As a first step, a distance measure between two stochastic linear time invariant systems is proposed here, extending the existing distance metrics between deterministic linear dynamical systems. In the frequency domain, the proposed distance measure corresponds to the worst-case point-wise in frequency Wasserstein distance between distributions characterising the uncertainties using inverse stereographic projection on the Riemann sphere. For the time domain setting, the proposed distance corresponds to the gap metric induced type-q Wasserstein distance between the distributions characterising the uncertainty of plant models. Apart from providing lower and upper bounds for the proposed distance measures in both frequency and time domain settings, it is proved that the former never exceeds the latter. The proposed distance measures will facilitate the provision of probabilistic guarantees on system robustness and controller performances.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Any valid metric in a vector space will induce a topology which will then facilitate a rigorous mathematical construct for performing analysis in that metric space. Inspired by these basic facts, researchers in the early $1980$s aimed at constructing a valid distance metric between dynamical systems in the hope that this research direction will pave way for a mathematically feasible and provable robust control analysis. Predominantly, the following metrics have received a vast appreciation in the control community namely: 1) Gap metric, 2) Graph metric, and 3) $\nu$-Gap metric. Authors in proposed a generic notion of distance between systems that can be used to measure discrepancy between open-loop systems in a feedback sense under several uncertainty structures. All the these metrics are equivalent to each other in the sense that they induce the same topology in the space of dynamical systems where closed loop stability happens to be a robust property. Such robust stability guarantees come with the presumption that all system models are equally probable in the considered neighbourhood set of plant models around the nominal plant model.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, nature is unpredictable while playing the role of an adversary inflicting uncertainties into the system dynamics and having an equally probable plants based assumption might downplay our ability to fully understand the nature's intention. In that sense, one can associate a probability distribution on the realization of the plants within the plant model ambiguity set in consideration. This initiated a research on probabilistic robust control using gap metric. This paper is an extension along the lines of but not with respect to plant models of the same stochastic system rather between two different stochastic systems in terms of their associated possible perturbed plant models. On a similar note, researchers in also proposed several probabilistic robust control approaches to handle the nature violating the assumption on uncertainties with small probabilities.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Authors in proposed a distance between two linear dynamical systems and called the alignment distance which is computed by finding the change of basis that best aligns the state-space realizations of the two linear dynamical systems. Similarly, authors in came up with a Riemannian metric on the space of stable linear systems, with applications to identification problems. One of the prominent attempts in investigating distance between stochastic dynamical systems was done by authors, where they came up with distance between spectral densities of linear time invariant (LTI) stochastic processes using behavioural theory. The theory of stochastic systems is not just limited to the field of mathematics but rather finds its application in many other fields of science. For instance, researchers in the field of medicine have started to think along in this direction too in by coming up with an algorithmic approach to compute and identify appropriate distance metrics for the quantitative comparison of stochastic model outputs and time-evolving stochastic measurements of a system. Many researchers have analysed the robust performance of controllers in the robust control community through the lens of the distance metric theory.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our problem formulation with distance between stochastic LTI systems will eventually evolve towards analysing the resulting probabilistic robust performance of a stabilising controller of one of the stochastic LTI system. However, the main focus of this manuscript will only be on the proposal of an appropriate distance measure and obtaining bounds on them. The subsequent analysis with respect to the probabilistic robust performance is left as a future work. Similarly, adding probabilistic rigour on top of the associated robust stability analysis along the lines of is also left as a future work. Our proposed research also has connections with frequency domain model validation problem considered in where authors presented a frequency domain interpretation of Monge-Kantorovich optimal transport.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose valid distance measures between two stochastic linear dynamical systems in the single input single output (SISO) case both in the frequency domain setting and in the time domain setting.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the frequency domain setting, the proposed distance measure given by (3.3) refers to the worst-case point-wise-in-frequency type-$q$ chordal metric induced Wasserstein distance between distributions governing the uncertainties of the two stochastic linear systems in the Riemann sphere. Under the assumption of distributions being uniform in nature, a support distance based upper bound for proposed distance measure is given in Theorem 3.2 ‣ 3.3 Type-𝑞 Distance Between Systems 𝑃₁ and 𝑃₂ ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems"). On the other hand, using the deviation of the perturbed models of each systems from their respective nominal models, a lower bound for the proposed distance measure is given in Theorem 3.3 ‣ 3.3 Type-𝑞 Distance Between Systems 𝑃₁ and 𝑃₂ ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems").

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extensions with respect to empirical distribution case are also given in Proposition 3.4},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems") and Theorem 3.6},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems").

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the time domain setting, the proposed distance measure given by refers to the gap metric induced type-$q$ Wasserstein distances between the distributions governing the uncertainty of the systems obtained through the push-forward of the distribution of uncertain system parameters under the measurable mapping that connects the parameters and the perturbed model. Upper bounds for the proposed distance measure are proposed in Proposition 4.2 and Theorem 4.3. On the similar lines of the frequency domain setting, a lower bound for the proposed distance measure in the time domain is given using the deviation of the perturbed models of each systems from their respective nominal models in Proposition 4.4.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also prove in Theorem 5.3 that for stochastic LTI systems, the proposed frequency domain distance never exceeds the time domain distance, mimicking the inequality relationship that exists between the $\nu$-gap metric and the gap metric in the deterministic systems setting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Organisation", "weight": 1.0} -->

Following a detailed discussion on the notations and the preliminaries needed for problem formulation in both frequency and time domain settings in Section 2, we will first begin our problem formulation in the frequency domain setting and propose a valid distance metric in Section 3. Following that, we will present the analogous problem formulation in the time domain setting and propose an analogous valid distance metric in Section 4. The proposed distance measures in the frequency and time domain settings are compared in Section 5. Finally, the paper is closed in Section 6 along with the summary of findings and directions for future research. Simulation results are provided throughout the paper to demonstrate the proposed concepts and guarantees. All the Matlab codes responsible for reproducing the simulation results provided in the paper can be found at

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations & Preliminaries", "weight": 1.0} -->

The cardinality and closure of the set $A$ are denoted by $|A|$ and $\overline{A}$ respectively. The set of real numbers, integers and the natural numbers are denoted by ${\mathbb{R}},{\mathbb{Z}},{\mathbb{N}}$ respectively and the subset of natural numbers greater than a given constant say $a \in {\mathbb{N}}$ is denoted by ${\mathbb{N}}_{> a}$. The Euclidean norm of a vector $x \in {\mathbb{R}}^{n}$ is denoted by $\left\| x \right\|_{2}$ or simply $\left\| x \right\|$. The inner product between two vector ${r_{1},r_{2}} \in {\mathbb{R}}^{n}$ is denoted by ${\langle r_{1},r_{2}\rangle}:={r_{1}^{\top}r_{2}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations & Preliminaries", "weight": 1.0} -->

For a matrix $A \in {\mathbb{R}}^{n \times n}$, we denote its transpose, trace, determinant, and the maximum (minimum) singular values by $A^{\top}$, ${\mathbf{T}\mathbf{r}}{(A)}$, $\det{(A)}$, and $\overline{\sigma}{(A)}{({\underset{¯}{\sigma}{(A)}})}$ respectively. An identity matrix of dimension $n$ is denoted by $I_{n}$. The notation ${( \cdot )}_{+}:={\max{(0, \cdot )}}$ shall be used to ensure positivity. For brevity of notation, we shall be abbreviating functions $f{({x{(t)}},{y{(t)}})}$ as $f{(t;x,y)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Notations & Preliminaries", "weight": 1.0} -->

The composition of two functions $f,g$ is denoted by $f \circ g$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Function Spaces & Norms", "weight": 1.0} -->

The space of complex numbers is denoted by $\mathbb{C}$ and $j$ represents the imaginary unit. For a complex variable $z \in {\mathbb{C}}$, we denote its complex conjugate as $z^{\star} \in {\mathbb{C}}$. Let $\mathbf{R}{(s)}$ denote the set of rational functions in $s \in {\mathbb{C}}$ with real coefficients. We use ${\mathcal{P}{(s)}} \subset {\mathbf{R}{(s)}}$ to denote the set of proper rational functions whose poles are in the open left half-plane. Let us denote the set of matrices with elements in $\mathbf{R}{(s)}$ as ${mat}{({\mathbf{R}{(s)}})}$ and similarly let us denote the set of matrices with elements in $\mathcal{P}{(s)}$ as ${mat}{({\mathcal{P}{(s)}})}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Function Spaces & Norms", "weight": 1.0} -->

A continuous-time signal $x \in {\mathbb{R}}^{n}$ is said to be in $\mathcal{L}_{2}$ space if it has bounded energy. Let $\mathcal{H}_{2}$ denote the space of Fourier transform of signals in $\mathcal{L}_{2}$ space but restricted to positive time. Dynamical systems are to be considered as operators on $\mathcal{H}_{2}$ and they will be called *stable* if for any input $u \in \mathcal{H}_{2}$, the system output $y \in \mathcal{H}_{2}$. The Hardy space consisting of transfer functions of stable LTI continuous time systems is denoted by $\mathcal{H}_{\infty}$ and is equipped with the norm

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation in Frequency Domain", "weight": 1.0} -->

While our main aim is to come up with an appropriate frequency domain specific distance metric between stochastic dynamical systems in general, for the ease of exposition, we shall start the problem formulation by analysing simple single input single output (SISO) dynamical systems first. The exposition with multiple input multiple output (MIMO) systems is out of the scope of this manuscript and is being investigated as a part of our future ongoing research (though we believe that exposition should carry forward typically from SISO to MIMO). Let $\Omega = {\lbrack 0,\infty)}$ denote the set of all frequencies.\

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation in Frequency Domain", "weight": 1.0} -->

Then, the transfer function of the $i$^th^ stochastic system for a fixed $s \in {\mathbb{C}}$ can be written as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

and for any Borel measurable set $\mathbf{B} \subset {\mathbb{C}}$, the above push-forward measure satisfies

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Compactness is essential to exclude the case of $\infty$ being included in the support set. Notice that both the distributions and their corresponding support sets of both the plants are frequency-dependent. This modelling assumption makes sense as one usually performs system identification procedure to identify plant models for a system by exciting the system at all frequencies using appropriate input signals. However, notice that we do not make any explicit assumption on the support sets $\mathcal{S}_{P_{1}}{(\omega)}$ and $\mathcal{S}_{P_{2}}{(\omega)}$ being disjoint from each other.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

From now, we shall drop the $({j\omega})$ argument for convenience with the understanding that the formulation corresponds to the quantities at a particular frequency $\omega$ unless otherwise specified. For both the stochastic systems enumerated by $\ell = {1,2}$, we can infer its projected support set as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stereographic Projection of Distribution", "weight": 1.0} -->

To find the distance between the random plants, we first need to understand how their corresponding distributions get transformed under the stereographic projection operation. That is, we need to characterise how the distributions ${\mathbb{P}}_{P_{\ell}{(\omega)}}$ of system $\ell = {\{ 1,2\}}$ will get transformed under the inverse of the stereographic projection operation. We recall Proposition 2.1 and use to obtain the corresponding projected distribution ${\mathbb{P}}_{R_{\ell}{(\omega)}}$ living on the Riemann sphere, for each system $\ell = {1,2}$ due to the inverse of the stereographic projection mapping. An illustration is provided in Figure 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stereographic Projection of Distribution", "weight": 1.0} -->

Equivalently, the distribution ${\mathbb{P}}_{R_{i}{(\omega)}}$ governing the uncertainty of system $i$ with $i \in {\{ 1,2\}}$ on the boundary of the Riemann sphere is related to the distribution $\mathbf{f}_{\theta_{i}}$ of the random parameter $\theta_{i}$ through the push-forward relation as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Stereographic Projection of Distribution", "weight": 1.0} -->

and for any Borel measurable set $\mathbf{B} \subseteq {\partial\Re}$, the above push-forward measure satisfies

<!-- chunk {"id": "body-0026", "role": "body", "section": "Support Distance Between Systems $P_{1}$ and $P_{2}$", "weight": 1.0} -->

In order to understand how far two stochastic dynamical systems $P_{1}$ and $P_{2}$ are in the frequency domain, first we analyse the distance between their support sets $\mathcal{S}_{P_{1}}{(\omega)}$ and $\mathcal{S}_{P_{2}}{(\omega)}$, where the respective system realizations can occur for every frequency $\omega \in \Omega$. To this end, we define the support distance between $P_{1}$ and $P_{2}$ in $\mathbb{C}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Type-$q$ Distance Between Systems $P_{1}$ and $P_{2}$", "weight": 1.0} -->

We address the above shortcoming by proposing the type-$q$ Wasserstein distance between systems by taking into account their distributions ${\mathbb{P}}_{P_{1}{(\omega)}}$, ${\mathbb{P}}_{P_{2}{(\omega)}}$ for every frequency $\omega \in \Omega$. We denote the corresponding set of all possible joint distribution by $\Pi_{\omega}:={\Pi\left( {\mathbb{P}}_{R_{1}{(\omega)}},{\mathbb{P}}_{R_{2}{(\omega)}} \right)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

One can use other variations to define the distance between systems $P_{1}$ and $P_{2}$ using other distance measures such as total variation measure, Hellinger measure, $\chi^{2}$ measure to measure their point-wise-in-frequency distance between the distributions ${\mathbb{P}}_{R_{1}{(\omega)}}$ and ${\mathbb{P}}_{R_{2}{(\omega)}}$ at every frequency $\omega \in \Omega$. Each comes with its own merits and drawbacks. We will stick to the Wasserstein distance based definition for this manuscript.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Note that the $\nu$-gap metric from the robust control literature is defined using the chordal distance between points on the Riemann sphere obtained through the inverse stereographic projection, provided that the two systems satisfy certain winding number constraints. It is certainly possible to take into account the Riemann manifold and use the geodesic distance as the transport cost while computing the Wasserstein distance between distributions on the Riemann sphere. In such a case, the optimal transport plan shall happen along the boundary of the Riemann sphere and as a result the geodesic metric $d_{geo}{(r_{1},r_{2})}$ and hence the distance between the plants can exceed unity. This will cause further issues when a connection between the distance between plants and the associated performance measure $b_{P,C}$ given by is made for analysing the probabilistic robustness, as $b_{P,C}$ does not exceed the value of $1$. This does not mean that the geodesic metric $d_{geo}{(r_{1},r_{2})}$ is a wrong distance metric choice.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Rather, it just means that the corresponding robustness measure that is similar to $b_{P,C}$ and that can handle distance between plants greater than $1$ is yet to be developed, and hence it is just a limitation due to the missing theory. Therefore, it is preferable to use the chordal distance in the subsequent theoretical development to reflect the normalized distance value in $\lbrack 0,1\rbrack$, facilitating future developments regarding probabilistic robust performance results using the performance measure $b_{P,C}$. From the optimal transport perspective, the transport plan will happen through the interior of the Riemann sphere (which is perfectly fine) when the transport cost is computed in terms of the chordal distance metric.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Upper Bound on $d_{q}\\left( P_{1},P_{2} \\right)$", "weight": 1.0} -->

Given any support set, it is possible to define an uniform distribution over it. Using this simple observation, the connection between the support distance and the proposed type-$q$ distance between the systems $P_{1}$ and $P_{2}$ is established in the following theorem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Lower Bound on $d_{q}\\left( P_{1},P_{2} \\right)$", "weight": 1.0} -->

Having obtained an upper bound for the distance metric $d_{q}{(P_{1},P_{2})}$ in Theorem 3.2 ‣ 3.3 Type-𝑞 Distance Between Systems 𝑃₁ and 𝑃₂ ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems"), we now proceed below to get a lower bound using triangle inequality based arguments. We will leverage the nominal distance and the expected deviation of the random plant instances of each systems from their respective nominal models to arrive at a lower bound for the proposed distance measure.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

We believe that a similar lower bound like the one in (28 ‣ 3.3 Type-𝑞 Distance Between Systems 𝑃₁ and 𝑃₂ ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems")) for the $d_{q}{(P_{1},P_{2})}$ can be obtained using \[27, Theorem 14.60\] by adapting the integral-infimum interchange theorem to supremum, where interchange of supremum and integration happens under conditions favouring Fubini-type arguments. Similarly, we can use Dobrushin inequality given any feasible candidate transport plan to obtain a simple yet conservative upper bound for the distance measure. We leave both the expositions as future works.

<!-- chunk {"id": "body-0034", "role": "body", "section": "${\\mathbb{P}}_{P_{1}{(\\omega)}},{\\mathbb{P}}_{P_{2}{(\\omega)}}$ Being Empirical Distributions", "weight": 1.0} -->

where ${\mathbf{δ}}_{{\hat{P}}_{\ell}^{(i)}{({j\omega})}}$ denotes the Dirac delta measure concentrated at the point ${{\hat{P}}_{\ell}^{(i)}{({j\omega})}} \in {\mathbb{C}}$. Then, using from Proposition 2.1, one can obtain the corresponding projected distribution ${\mathbb{P}}_{R_{\ell}{(\omega)}}$, for each system $\ell = {1,2}$. The following proposition describes the computation of distance metric for this special case of empirical distributions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Demonstrations", "weight": 1.0} -->

To demonstrate the proposed distance in the frequency domain, we consider two different systems with their nominal model transfer functions given by ${P_{1}{(s)}} = \frac{1}{1 + {0.5s}}$ and ${P_{2}{(s)}} = \frac{1}{{({1 + {0.2s}})}{({1 + {0.7s}})}}$ respectively. A discretized frequency space $\Omega_{M}$ containing $M = 1000$ points between ${{\lbrack 0.1,10^{3}\rbrack}\text{~rad}}/s$ was formed. At every frequency $\omega \in \Omega_{M}$, $N = 100$ samples of frequency response data were generated by randomly perturbing the nominal frequency response at that frequency. Both the nominal frequency response and the empirical distribution containing the samples at every frequency were projected onto the Riemann sphere using the inverse Stereographic projection given.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical Demonstrations", "weight": 1.0} -->

The chordal distance metric based type-1 Wasserstein distance ${\hat{d}}_{1}{(P_{1},P_{2})}$ between two systems given by (32},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems")) was computed using the linear programming approach. The upper bound using the support distance was computed using Proposition 3.5},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems") and the lower bound was computed using Theorem 3.6},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems"). The results are shown in Figure 2. The proposed frequency domain distance ${\hat{d}}_{1}{(P_{1},P_{2})}$ between the systems $P_{1}$ and $P_{2}$ was found to be $0.2916$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical Demonstrations", "weight": 1.0} -->

The corresponding upper and lower bounds computed using Proposition 3.5},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems") and Theorem 3.6},ℙ_{𝑃₂⁢(𝜔)} Being Empirical Distributions ‣ 3 Problem Formulation in Frequency Domain ‣ Distance Between Stochastic Linear Systems") were found to be $0.3075$ and $0.2831$ respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Summary of Frequency Domain Distance", "weight": 1.0} -->

For SISO systems, the proposed distance measure in the frequency domain using the chordal distance measure mimicking the $\nu$-gap perspective comes in handy with nice pictorial illustration. We believe that this is just a starting point and there are several interesting future research extensions. Though in principle, we expect the theory to carry forward in a similar fashion from SISO to MIMO systems setting, we expect some inherent difficult that comes with higher dimensions to kick. For example, we would be required to work with the Riemann sphere of higher dimensions and associated stereographic projections are more mathematically involved and complex in nature. Another problem is of dealing with the supremum with respect to the frequency parameter. This problem persists even in SISO and will continue to persist even in MIMO setting. To get around these issues, we would like to formulate and obtain an analogous distance measure between stochastic linear systems in the time domain setting using gap metric perspective where the process of taking supremum with respect to $\omega \in \Omega$ would be absent. The exposition with the time domain setting will be carried out in the next section.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem Formulation in Time Domain", "weight": 1.0} -->

In this section, we will present an analogous distance measure in the time domain using the gap metric.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Uncertain Dynamical Systems", "weight": 1.0} -->

Consider two continuous time LTI dynamical systems living in the space of linear stochastic systems denoted by $\mathbf{\Sigma}$. Let the nominal models of both systems $i \in {\{ 1,2\}}$ be given by

<!-- chunk {"id": "body-0041", "role": "body", "section": "Uncertain Dynamical Systems", "weight": 1.0} -->

where for system $i$ at time $t \in {\mathbb{R}}_{\geq 0}$, we refer to its system states as ${x_{i}{(t)}} \in {\mathbb{R}}^{n}$, the control inputs to the system as ${u_{i}{(t)}} \in {\mathbb{R}}^{m}$, the system outputs as ${y_{i}{(t)}} \in {\mathbb{R}}^{l}$ and the matrices $A_{i} \in {\mathbb{R}}^{n \times n}$, $B_{i} \in {\mathbb{R}}^{n \times m}$, $C_{i} \in {\mathbb{R}}^{l \times n}$. Real-world dynamical systems usually have some form of uncertainties associated with them either due to the lack of modelling tools or due to the inaccuracies of the modelling framework.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Uncertain Dynamical Systems", "weight": 1.0} -->

Hence, in practice, all systems have inherent uncertainties affecting their evolution.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Uncertain Dynamical Systems", "weight": 1.0} -->

We note here that ${\Sigma_{i}{({\overline{\theta}}_{i})}} = {\overline{\Sigma}}_{i}$ meaning that the perturbed system equals the nominal system when uncertainty vanishes at ${\overline{\theta}}_{i}$ for system $i$. This does not imply that $\mu_{\theta_{i}} = {\overline{\theta}}_{i}$. The only requirement that is needed is that ${\overline{\theta}}_{i} \in \mathbf{f}_{\theta_{i}}$ (perfectly fine even if the containment happens asymptotically (as number of samples tend to $\infty$)) so that when the uncertainties of the perturbed system vanish, it results in the nominal system.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Gap Between Models", "weight": 1.0} -->

Clearly, ${Gap}_{i}{(\theta_{i})}$ is a random variable in $$ if the $i$^th^ system is stable for all possible perturbations due to $\theta_{i} \sim \mathbf{f}_{\theta_{i}} = {\mathcal{N}{(\mu_{\theta_{i}},\Sigma_{\theta_{i}})}}$. However, we need distance between two systems and rather not between two models of the same system. Towards that we define the distance between the nominal models of two systems $i \in {\{ 1,2\}}$ denoted by ${dist}_{\Sigma_{1},\Sigma_{2}}^{nom}$ as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Gap Between Models", "weight": 1.0} -->

That is, when the uncertainties of both systems $i \in {\{ 1,2\}}$ vanish, then it simply boils down to the simple gap metric between two deterministic nominal system models ${\overline{\Sigma}}_{1}$ and ${\overline{\Sigma}}_{2}$. However, systems always come with uncertainties due to inevitable modelling errors and hence ${dist}_{\Sigma_{1},\Sigma_{2}}^{nom}$ will not truly capture the distance between the two stochastic systems strictly speaking.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Inferring Distribution of Perturbed Plant", "weight": 1.0} -->

In this regard, we propose to measure the distance between the distributions that are governing the randomness of the plant models of system $i \in {\{ 1,2\}}$. That is, the randomness in $\theta_{i}$ manifests itself as the randomness in the plant $\Sigma_{i}{(\theta_{i})}$ meaning that ${\Sigma_{i}{(\theta_{i})}} \sim \mathbf{f}_{i}$, where $\mathbf{f}_{i}$ is the distribution of plant models of $i$^th^ system.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Inferring Distribution of Perturbed Plant", "weight": 1.0} -->

where for any Borel measurable set $\mathbf{B} \subseteq {\mathbb{R}}^{({n^{2} + {nm} + {ln}})}$ (the space of system plants), the push-forward measure satisfies

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

Despite ${Gap}_{i}{(\theta_{i})}$ being random for each of the system, we want to formulate and obtain a deterministic distance measure between two stochastic linear systems, which by the way is the main motive of this manuscript. Consider the special case when the $\theta_{i}$ parameter dependence on the perturbed system dynamics in is affine with $\mathbf{f}_{\theta_{i}}$ being Gaussian. Then, the distribution $\mathbf{f}_{i}$ of the $i$^th^ system due to turns out to be Gaussian as well due to the affine transformation properties of Gaussian random vectors. The following lemma formally establishes this result.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Gap Metric Induced Type-$q$ Wasserstein Distance", "weight": 1.0} -->

Having studied the transformation of the distribution of the parameter under the mapping of the perturbed dynamics to result in the distribution for the perturbed plant models, we are now ready to define the distance between perturbed models of two systems.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Demonstrations", "weight": 1.0} -->

For generating the perturbed models, we choose $d = 4$, $\theta_{1} \sim {\mathcal{N}{(0.01,0.01^{2})}}$, and $\theta_{2} \sim {\mathcal{N}{(0.05,0.05^{2})}}$. Totally, $N = 50$ samples of perturbed models for each of the two dynamical systems were generated along the lines of. The proposed distance measure ${dist}_{\Sigma_{1},\Sigma_{2},\delta_{g}}$ between each of the models for both the systems was computed using using linear programming based approach with the transport cost being the gap metric which was computed using the *gapmetric* command of Matlab. The upper bound and lower bounds for the proposed distance measure were computed using Proposition 4.2 and Proposition 4.4 respectively. The gap between the nominal models ${dist}_{\Sigma_{1},\Sigma_{2}}^{nom}$ was found to be $0.7731$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Demonstrations", "weight": 1.0} -->

We estimated the proposed distance measure ${dist}_{\Sigma_{1},\Sigma_{2},\delta_{g}} = 0.7765$, and its lower and upper bounds as $0.6561$ and $0.8252$ respectively.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Summary", "weight": 1.0} -->

The proposed time domain distance given by facilitates a simple linear programming based computation and also is devoid of additional supremum over frequency operation. We do not claim here that the upper and lower bounds given by Proposition 4.2 and Proposition 4.4 respectively are tight. In the next section, we will show that the frequency domain distance proposed in Section 3 never exceeds the time domain distance proposed in this section.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Comparing Time Domain & Frequency Domain Distance Measures", "weight": 1.0} -->

It is well known from that $\nu$-gap can never exceed the gap metric for linear systems. Along those lines, we will prove in this section that the proposed frequency domain distance measure in Section 3 between two stochastic LTI dynamical system never exceeds its time domain distance measure counterpart proposed in Section 4. We formalise this observation using a comparison theorem followed by a simulation example based demonstration to corroborate our findings.\

<!-- chunk {"id": "body-0054", "role": "body", "section": "Comparing Time Domain & Frequency Domain Distance Measures", "weight": 1.0} -->

In the frequency domain setting, we know that the distribution ${\mathbb{P}}_{R_{i}{(\omega)}}$ governing the uncertainty of system $i$ with $i \in {\{ 1,2\}}$ on the boundary of the Riemann sphere is related to the distribution $\mathbf{f}_{\theta_{i}}$ of the random parameter $\theta_{i}$ through. Analogously, in the time domain setting, the distribution $\mathbf{f}_{i}$ of plant models of system $i \in {\{ 1,2\}}$ and the corresponding distribution $\mathbf{f}_{\theta_{i}}$ of the random parameter $\theta_{i}$ satisfy and with $\Phi_{i}$ denoting the measurable map from the parameter space to the state space of system plants as described earlier in Section 4. We now define a transfer function mapping which when given a state space model, returns a real rational transfer function.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparing Time Domain & Frequency Domain Distance Measures", "weight": 1.0} -->

That is, we define the transfer function mapping ${\mathbf{T}\mathbf{F}}:{\Phi_{i}\rightarrow{\mathbf{R}\mathcal{L}_{\infty}}}$ such that ${{\mathbf{T}\mathbf{F}}{({\Sigma_{i}{(\theta_{i})}})}} = {P_{i}{(\theta_{i};s)}}$. We also need a mapping $\Psi_{\omega}^{\Re}:{\Phi_{i}\rightarrow{\partial\Re}}$ that takes the state space model and maps it to the Riemann sphere after realising a real rational transfer function and subsequently evaluating it at a particular frequency $\omega$ and applying the inverse stereographic projection operation. Such a mapping can be defined using composition as

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

Before we proceed ahead with the comparison theorem, we will first prove a lemma describing how the joint distributions involved in optimal transport defined in the state space and in the Riemann sphere are related to each other and this will be useful in the proof of the comparison theorem to be presented later in this manuscript.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Demonstration", "weight": 1.0} -->

Given two stochastic LTI systems, to demonstrate that the frequency domain distance never exceeds the time domain distance, we consider two different second order LTI systems which vary due to their correspondingly random damping and resonant frequency values. Specifically, consider two second order systems whose nominal damping and resonant frequency values are given by ${\overline{\zeta}}_{1} = 0.35$, ${\overline{\zeta}}_{2} = 0.55$, ${\overline{\omega}}_{n_{1}} = 1.8$, ${\overline{\omega}}_{n_{2}} = 1.2$ respectively. Then, the nominal transfer function models of both the systems are given by

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Demonstration", "weight": 1.0} -->

To compute the distances, $N = 100$ samples of perturbed plant models for both the systems were formed by perturbing along the lines of, the corresponding nominal models of both the systems given. The random parameters $\theta_{i}$ that were used to generate the perturbed models of the system $i \in {\{ 1,2\}}$ are given by $\theta_{i} \sim {\mathcal{N}{(\mu_{\theta_{i}},\Sigma_{\theta_{i}})}}$, where

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical Demonstration", "weight": 1.0} -->

To compute the frequency domain distance, a frequency grid in the log space between $\lbrack 10^{- 2},10^{2}\rbrack$ rad/sec was discretized into $M = 100$ points. Precisely speaking, $\Omega_{M} = {{logspace}{(10^{- 2},10^{2},100)}}$. The quantities of interests namely the frequency domain distance $d_{q}{(P_{1},P_{2})}$ and the time domain distance ${dist}_{\Sigma_{1},\Sigma_{2},\delta_{g}}$ were computed using (3.3) and respectively. In both the distance computations, the corresponding type-$1$ Wasserstein distance computation was carried out using the linear programming technique.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Numerical Demonstration", "weight": 1.0} -->

As a result of the computation, we obtained the frequency domain distance ${d_{q}{(P_{1},P_{2})}} = 0.3795$, the time domain distance ${dist}_{\Sigma_{1},\Sigma_{2},\delta_{g}} = 0.3812$ and the gap metric between the nominal models given by was found out to be $0.3822$. Clearly as expected, we obtained ${d_{q}{(P_{1},P_{2})}} \leq {dist}_{\Sigma_{1},\Sigma_{2},\delta_{g}}$ and thereby agreeing to the claims of Theorem 5.3.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusions", "weight": 1.0} -->

A new distance metric between two SISO stochastic LTI dynamical systems was presented both in the frequency domain and in the time domain. In the frequency domain, the proposed distance corresponds to the worst-case-in-frequency chordal distance metric induced distance between distributions characterising the uncertainties of systems in the Riemann sphere. Analogously, the proposed distance in the time domain corresponds to the gap metric induced type-q Wasserstein distance between the push-forward measures under both systems' corresponding measurable maps from the parameter space to their respective space of system plants. For both the frequency domain and the time domain settings, upper bounds and lower bounds for the proposed distances were given. It was also shown that for stochastic LTI systems, the proposed frequency domain distance measure never exceeds the proposed time domain distance measure counterpart.\

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Seek to extend the study from SISO systems to MIMO systems and further to nonlinear systems

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusions", "weight": 1.0} -->

A preliminary step towards the above extension would be to investigate the probabilistic robustness for linear time varying (LTV) systems by adopting the ideas of and adding probabilistic rigour on top of it and extending it to distance between stochastic LTV systems as done in this manuscript.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Another interesting direction of research will be to investigate the probabilistic robust stability of controllers. That is, given a stabilising controller for one stochastic system, we should investigate the probability of that controller stabilising another stochastic system in the vicinity of the first stochastic system where the vicinity is measured using the proposed distance measure.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusions", "weight": 1.0} -->

It would also be interesting to study probabilistic guarantees on the performance variations for the same controller trying to control two different stochastic systems.
