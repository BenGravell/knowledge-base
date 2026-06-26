<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Koopman Meets Input-Output Data: Data-Driven Output-Feedback Control of Nonlinear Systems with Closed-Loop Guarantees

Topics include Data-driven control, Output feedback, Koopman operator, Nonlinear systems, Input-output data, Closed-loop guarantees, Bilinear surrogate models, Exponential stability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines Koopman operator ideas with input-output trajectory data to design output-feedback controllers for nonlinear systems with closed-loop guarantees. The method constructs an extended-state bilinear surrogate directly from measurements, then applies robust state-feedback design while proving convergence back for the original nonlinear state.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven control of nonlinear systems from input-output measurements remains a fundamental challenge, as existing approaches with rigorous closed-loop guarantees predominantly require access to full state measurements. In this paper, we address this gap by proposing a data-driven output-feedback controller design method for nonlinear systems that provides provable closed-loop guarantees while operating solely on measured input-output data. Our approach combines Koopman operator theory with an extended state representation of the nonlinear system constructed from input-output trajectories. This allows us to obtain a bilinear surrogate model directly from data, on which robust state-feedback design methods can be applied. By exploiting the observability of the underlying nonlinear system, we establish exponential stability of the extended state, which in turn implies exponential convergence of the original system state to the origin. Finally, we validate our theoretical findings in numerical simulations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven control of dynamical systems has emerged as a powerful paradigm for designing controllers directly from measured data, bypassing the need for first-principles model derivation. This is particularly appealing in practice, where complex system dynamics are often difficult or expensive to model analytically, yet plenty of measurement data are readily available. For linear systems, data-driven control is by now relatively well understood. Willems' fundamental lemma[willems:rapisarda:markovsky:demoor:2005] provides a non-parametric characterization of all trajectories of a linear time-invariant system in terms of a single persistently excited experiment, forming the basis of a large body of work on data-driven predictive control and stabilization[markovsky:rapisarda:2008,coulson:lygeros:dorfler:2019,berberich:kohler:muller:allgower:2020c,faulwasser:ou:pan:schmitz:worthmann:2023].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extensions to output-feedback settings for linear systems have been pursued in several directions, including robust output-feedback controllers[berberich:scherer:allgower:2023], verification of dissipativity properties from input-output data[koch:berberich:allgower:2022], and data-driven output-feedback control of linear MIMO systems[alsalti:lopez:muller:2025]. However, extending these results to the nonlinear setting remains substantially more challenging and is largely open.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For nonlinear systems, data-driven control with closed-loop guarantees typically relies on state or state-derivative data [martin:schon:allgower:2023b], and extensions to the output-feedback case are rare. A notable exception is the work of[dai:depersis:monshizadeh:tesi:2023,dai:depersis:monshizadeh:tesi:2025], who design dynamic output feedback controllers for discrete-time nonlinear systems directly from input-output data with local stability guarantees, requiring that an auxiliary input-output representation of the system can be expressed through a known dictionary of basis functions. Constructing such representations from input-output data in a principled way remains an open challenge, and a natural starting point is the identification of nonlinear systems from data, which has been studied extensively[noel:kerschen:2017,ljung:andersson:tiels:schon:2020].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical approaches include lifting to higher-dimensional feature spaces via basis function expansions, such as LPV[verdult:verhaegen:2002,bamieh:giarre:2002] or polynomial approximations[paduart:lauwers:swevers:smolders:schoukens:pintelon:2010], local or piecewise linear subspace identification[verdult:2002], and probabilistic approaches based on expectation-maximization[schon:wills:ninness:2011] or Gaussian processes[frigola:lindsten:schon:rasmussen:2013,frigola:chen:rasmussen:2014].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A particularly relevant subclass is the class of bilinear systems, which arise naturally as finite-dimensional Koopman representations of nonlinear dynamics[iacob:toth:schoukens:2024] and for which subspace identification methods have been developed[favoreel:demoor:vanoverschee:1999,verdult:verhaegen:1999,chen:maciejowski:1999,chen:maciejowski:2000,favoreel:1999], including kernel-based variants that avoid the exponential growth of data matrices with system order[verdult:verhaegen:2005,wingerden:verhaegen:2009].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite-sample guarantees for bilinear system identification have also been studied recently[sattar:oymak:ozay:2022,sattar:jedra:fazel:dean:2025], direct data-driven controller design has been proposed via LMIs[bisoffi:depersis:tesi:2020a] and model predictive control[xie:berberich:strasser:allgower:2025], and first end-to-end guarantees from identification to closed-loop control have been established in[chatzikiriakos:strasser:allgower:iannelli:2026].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Complementary to system identification, observer design for nonlinear and bilinear systems is a classical and active research area; see [besancon:2007a,besancon:2007b,isidori:2017,bernard:2019,bernard:andrieu:astolfi:2022]. Fundamental notions of nonlinear observability have been established from geometric[nijmeijer:1982,nijmeijer:vanderschaft:1990,hermann:krener:1977] and system-theoretic[sontag:1998,isidori:1985] perspectives, with further results for polynomial[sontag:1979] and discrete-time systems[albertini:dallessandro:1996]. For nonlinear systems more broadly, early results on state reconstruction and convergence of the estimation error are due to[thau:1973]. For bilinear systems specifically, observability conditions[williamson:1977] and stable state estimators have been developed[funahashi:1979,hara:furuta:1976,bornard:couenne:celle:1989,elliott:2009], though observer convergence in this setting typically depends on the applied input sequence.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising framework for handling nonlinear dynamics in a data-driven fashion is Koopman operator theory [koopman:1931,mezic:2005,mauroy:mezic:susuki:2020,bevanda:sosnowski:hirche:2021,brunton:budisic:kaiser:kutz:2022], which lifts nonlinear system dynamics into an infinite-dimensional, linear space through the action of the Koopman operator on observable functions. This viewpoint has sparked a rich literature on data-driven approximation of the Koopman operator, including extended dynamic mode decomposition[williams:kevrekidis:rowley:2015,schmid:2010], kernel-based variants[williams:rowley:kevrekidis:2016,klus:nuske:hamzi:2020,philipp:schaller:worthmann:peitz:nuske:2024], and deep learning approaches[lusch:kutz:brunton:2018,yeung:kundu:hodas:2019,otto:rowley:2019].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Crucially, it has been established that linear Koopman approximations are generally insufficient for controlled systems, and that bilinear structures naturally emerge in Koopman representations of input-affine nonlinear systems[iacob:toth:schoukens:2024]; see also[haseli:cortes:2023a,haseli:cortes:2023b,haseli:cortes:2023c,haseli:cortes:2026,shang:haseli:cortes:zheng:2026] for further theoretical developments on the structure of controlled Koopman operators. Further,[lian:wang:jones:2021,shang:cortes:zheng:2024,xiong:yuan:miao:wang:cortes:papachristodoulou:2025] propose extensions of Willems' fundamental lemma to the nonlinear setting using Koopman embeddings, though typically under restrictive invariance assumptions on the chosen dictionary. Recently,[lazar:2025] addresses these limitations by constructing the Koopman operator on a product Hilbert space formed as the tensor product of state and input observable spaces, relaxing dictionary invariance and measure preservation requirements.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This allows the author to derive a nonlinear fundamental lemma for input-output data by combining the resulting exact infinite-dimensional bilinear representation with Hankel operators and a frame-based persistency of excitation condition. However, the approach inherently relies on infinite-dimensional representations and requires state measurements during the offline data collection phase to construct the lifted Hankel operator. While finite-dimensional EDMD approximations via a Khatri-Rao scheme are proposed, no finite-sample error bounds or closed-loop guarantees are established, limiting its applicability to rigorous data-driven controller design.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key insight for practical applicability is that the Koopman operator can be approximated using delay-coordinate embeddings [mezic:banaszuk:2004,robinson:2005,susuki:mezic:2015,arbabi:mezic:2017b,mezic:2022,koltai:kunde:2024], which are directly constructed from input-output time-series data without requiring state measurements. These findings directly led to Hankel DMD[arbabi:mezic:2017b,kamb:kaiser:brunton:kutz:2020,pan:duraisamy:2020] and latent EDMD[ouala:chapron:collard:gaultier:fablet:2023].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Koopman operator approximations based on delay-coordinate embeddings connect naturally to Takens' theorem[takens:1981] and have been exploited in MPC[korda:mezic:2018a] and various engineering applications such as flow prediction[yuan:zhou:zhou:wen:liu:2021], soft robotics[bruder:fu:gillespie:remy:vasudevan:2021,haggerty:banks:kamenar:cao:curtis:mazic:hawkes:2023], and grip force prediction[bazina:kamenar:fonoberova:mezic:2025].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite-data error bounds for Koopman approximations are provided in[mezic:2022,nuske:peitz:philipp:schaller:worthmann:2023,schaller:worthmann:philipp:peitz:nuske:2023,zhang:zuazua:2023,yadav:mauroy:2025] for EDMD and in[philipp:schaller:worthmann:peitz:nuske:2024,kurdila:paruchuri:powell:guo:bobade:estes:wang:2024,kohne:philipp:schaller:schiela:worthmann:2025,bold:philipp:schaller:worthmann:2025,philipp2025error,strasser:schaller:berberich:worthmann:allgower:2025] for kernel-based EDMD variants.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover,[strasser:schaller:worthmann:berberich:allgower:2025,strasser:schaller:worthmann:berberich:allgower:2026,strasser:berberich:allgower:2025,strasser:berberich:schaller:worthmann:allgower:2025] establish first closed-loop guarantees for Koopman-based controllers, including Koopman-based MPC[worthmann:strasser:schaller:berberich:allgower:2024,bold:grune:schaller:worthmann:2025,bold:schaller:schimperna:worthmann:2025,schimperna:bold:kohler:worthmann:2026,schimperna2025data]; see the recent overview paper[strasser:worthmann:mezic:berberich:schaller:allgower:2026]. However, all of the above results with closed-loop guarantees require state measurements for the construction of the Koopman surrogate model and the subsequent controller design.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Obtaining full state measurements is often impractical or infeasible in real-world applications, where only input-output data are available, motivating the need for output-feedback approaches that avoid this restrictive assumption.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the observer and estimation side, the Koopman framework has been used to design state estimators via various lifting strategies, including bilinear [surana:2016,surana:banaszuk:2016,surana:2020,otto:peitz:rowley:2024], linear observable[lei:yin:2025,lyu:lang:wang:2025,yang:gao:chen:lv:wang:2025], and dual Koopman forms[mohet:mauroy:winkin:2025], as well as kernel-based and neural-network-enhanced Kalman filters[netto:mili:2018a,netto:mili:2018b,jiang:zhang:zuo:shi:su:2022,huang:zheng:fettweis:2024,guo:korotkine:forbes:barfoot:2021]; see[otto:rowley:2021,shi:haseli:mamakoukas:bruder:abraham:murphey:cortes:karydis:2026] for surveys.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Further approaches include robust observer synthesis using linear Koopman approximations with frequency-domain error characterization[dahdah:forbes:2024], and the construction of LPV Koopman models from noisy output data using deep state-space encoders[iacob:beintema:schoukens:toth:2021,iacob:szecsi:mate:beintema:schoukens:toth:2025]. However, these approaches either rely on the restrictive assumption of an exactly invariant Koopman dictionary or do not provide guarantees for the designed observer.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

More broadly, output-feedback control using Koopman embeddings remains largely restricted to settings that assume exact Koopman invariance[kieboom:bartzioka:jafarian:2023], linear Koopman approximations[deutscher:2024,lopez:heinrich:muller:2026], or LPV surrogate models with frequency-domain error characterization[eyuboglu:strasser:allgower:karimi:2026], and a rigorous data-driven output-feedback design for nonlinear systems with provable closed-loop guarantees is missing from the literature.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

To solve this gap, we propose a data-driven output-feedback controller design method for nonlinear systems. In particular, we combine Koopman operator theory with an extended state representation of nonlinear systems based on input-output data. This allows us to build on robust state-feedback design schemes from the literature to exponentially stabilize the nonlinear extended-state system and, thereby, establish closed-loop guarantees for the underlying nonlinear system from input-output data. By exploiting the observability of the system, we show exponential convergence to the origin of the corresponding system's state. The proposed approach is the first Koopman-based controller design method that relies solely on input-output data and provides closed-loop guarantees for the underlying nonlinear system, paving the way forward to rigorous data-driven output-feedback control with closed-loop guarantees. Finally, we validate our theoretical findings in numerical simulations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is structured as follows. [sec:background], we introduce the problem setting and necessary background for the results developed in this paper. Section[sec:IO-representations-extended-state] is devoted to an input-output representation of nonlinear systems. Section[sec:DD-output-feedback-controller-design] contains our main contributions, namely a data-driven output-feedback controller design for nonlinear systems on the basis of a bilinear Koopman surrogate model. Finally, the theoretical results are illustrated in Section[sec:numerical-examples] using numerical simulations, before concluding the paper in Section[sec:conclusion].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem setting and background", "weight": 1.0} -->

First, we introduce the problem setting in Section[sec:problem-setting]. Then, we provide the necessary background on Koopman operator theory and its usage for controlled nonlinear systems in Section[sec:Koopman-background].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem setting", "weight": 1.0} -->

We consider a nonlinear system x_{k+1} &= f(x_k,u_k), \qquad x_0=\bar{x}\in\bbR^n,\\with $x\in\bbX\subseteq\bbR^n$, $u\in\bbU\subseteq\bbR^m$, and $y\in\bbY\subseteq\bbR^p$. The state transition map $f:\bbR^n\times\bbR^m \to \bbR^n$ and the output map $h:\bbR^n\times\bbR^m \to \bbR^p$ are unknown, but assumed to be sufficiently smooth.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem setting", "weight": 1.0} -->

The maps $f,h\in C^1$, i.e., the maps are continuously differentiable, and the sets $\bbX$, $\bbU$, $\bbY$ are compact, convex, and contain the origin in its interior.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem setting", "weight": 1.0} -->

For a given initial state $\bar{x}\in\bbX$ and an input sequence $\useq_{0:L-1}\in\bbU^L$, we define the corresponding state trajectory recursively via such that $x_j$ is the state at time $j$ starting from the initial condition $\bar{x}$ at time zero. The corresponding output is $y_j = h(x_j,u_{j})$. which corresponds to applying the map $f$ $j$times.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem setting", "weight": 1.0} -->

To find a suitable system representation, the unknown system dynamics are estimated from data, where, however, the state $x$ is inaccessible and only input-output measurements are available. In particular, we collect $d\in \bbN$ input-output trajectories of length $L+1$, i.e., Note that we use only input-output data instead of input-state data. For the Koopman surrogate established later, each trajectory of length $L+1$ will be associated with a data triplet of a delay embedding, its successor, and its input. This yields a total of $d$ data triplets used for the data-driven surrogate characterization.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem setting", "weight": 1.0} -->

As usual in data-driven control, we may also collect one single trajectory instead of multiple shorter input-output trajectories. More precisely, instead of the data $\cD$ we could also collect a trajectory of length $L+d+1$, i.e., $\{u_t,y_t\}_{t=-L}^{d}$. Based on this trajectory, we could again define $d$ extended state triplets, leading to the proposed Koopman-based surrogate. Then, all results established in this paper remain valid.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem setting", "weight": 1.0} -->

To characterize when the full system behavior can be inferred from input-output data alone, we define the following.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem setting", "weight": 1.0} -->

For any initial condition $\bar{x}\in\bbX$ and input sequence $\useq_{0:L-1}\in\bbU^L$ for integer $L\geq 1$, we define the observability map of order $L$ as the function that stacks $L$ consecutive output values, i.e., The observability map used here coincides with the one given for uncontrolled systems in[iacob:szecsi:mate:beintema:schoukens:toth:2025], where a Koopman model is identified from noisy input-output data and the estimation error is shown to vanish asymptotically. However, explicit error bounds are not provided, and the convergence result assumes exponential stability of the Koopman model, which is generally difficult to satisfy even when the original system is exponentially stable[philipp:schaller:worthmann:peitz:nuske:2025].

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem setting", "weight": 1.0} -->

$\cO_L$, we can now introduce the notion of uniform observability[gauthier:kupka:1994,gauthier:kupka:2001,gauthier:hammouri:othman:2002,hanba:2009] relevant for the later established results.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem setting", "weight": 1.0} -->

The system[eq:dynamics-nonlinear] is uniformly observable on $\bbX$ if there exists an integer $L\geq 1$ such that, for every admissible input sequence $\useq_{0:L-1}\in\bbU^L$, the map $\cO_L(\cdot,\useq_{0:L-1}): \bbX \to \bbR^{Lp}$ is injective.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem setting", "weight": 1.0} -->

The injectivity corresponding to uniform observability ensures that the initial state $\bar{x}$ can be uniquely recovered based on measured input-output sequences of length $L$, i.e., $\cO_L(x_1,\useq)=\cO_L(x_2,\useq)$ implies $x_1=x_2$. This is a common assumption in data-driven control via input-output data[dai:depersis:monshizadeh:tesi:2023,dai:depersis:monshizadeh:tesi:2025]. In the remainder of the paper, we enforce injectivity and, thus, uniform observability by a slightly stronger condition that ensures well-posedness of the inverse map $\cO_L^{-1}$. This allows us to derive a suitable input-output characterization of the nonlinear system[eq:dynamics-nonlinear]. To this end, we define an extended state based on past input-output data and employ a Koopman lifting, yielding a data-driven bilinear surrogate of the underlying nonlinear system.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem setting", "weight": 1.0} -->

This representation is then used for an output-feedback controller design with closed-loop guarantees for the unknown nonlinear system.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

Consider a discrete-time autonomous dynamical system $ $ with $x_k \in \bbX \subseteq \bbR^n$ and state-transition map $f: \bbX \to \bbX$. Instead of evolving the state directly, the Koopman operator $\cK$[koopman:1931] acts on scalar-valued observable functions $\varphi: \bbX \to \bbR$ by composing them with $f$, i.e., $$(\cK \varphi)(x_k) = \varphi\big(f(x_k)\big) Although the underlying dynamics $f$ may be nonlinear, $\mathcal{K}$ is a linear operator acting on an, in general, infinite-dimensional function space.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

In practice, one works with a finite-dimensional approximation by selecting a dictionary of $N$ observables, i.e., $$\Psi(x) = \begin{bmatrix} \psi_1(x) & \cdots & \psi_N(x) \end{bmatrix}^\top \in \mathbb{R}^N,$$ and seeking a matrix $K \in \bbR^{N \times N}$ such that $$\Psi(x_{k+1}) \approx K \Psi(x_k).$$ A standard data-driven method for identifying $K$ is extended dynamic mode decomposition[williams:kevrekidis:rowley:2015].

<!-- chunk {"id": "body-0038", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

d}, \Psi(X^+) = \begin{bmatrix} \Psi(x_1) & \cdots & \Psi(x_d) \end{bmatrix}\in\bbR^{N\times d},$$ collect the lifted current and successor states, respectively, and $(\cdot)^\dagger$ denotes the MoorePenrose pseudoinverse.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

For a controlled discrete-time system $$x_{k+1} = f(x_k, u_k), \quad x_k \in \bbX,\; u_k \in \bbU,$$ the Koopman framework is extended by treating the input as a parameter of the Assuming $u_k$ is held constant over each sampling interval, consistent with a sample-and-hold implementation, a family of input-dependent Koopman operators $\{\cK^u\}_{u \in \bbU}$ is defined by $$(\cK^u \varphi)(x) = \varphi\big(f(x, u)\big);$$ compare[haseli:cortes:2026]. Each operator $\cK^u$ remains linear in the observable space for fixed$u$. Introducing the same dictionary of observable functions $\Psi$as before, one seeks a finite-dimensional approximation from data.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

In linear EDMD with control [proctor:brunton:kutz:2016], one builds a lifted linear model $$\Psi(x_{k+1}) \approx A \Psi(x_k) + B u_k,$$ where the matrices $A \in \bbR^{N \times N}$ and $B \in \bbR^{N \times m}$ can be identified simultaneously via a least-squares regression over snapshot data. Although this linear evolution of the lifted state would be desirable, as it enables the direct application of linear systems theory and control design to the originally nonlinear controlled system, it introduces fundamental approximation errors. In particular, representations of the above form impose severe limitations on the original system[shang:haseli:cortes:zheng:2026,heeg:worthmann:2026]. This fact prevents closed-loop guarantees and thereby safe control of the underlying nonlinear system[iacob:toth:schoukens:2024,strasser:worthmann:mezic:berberich:schaller:allgower:2026].

<!-- chunk {"id": "body-0041", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

Instead, at least bilinear Koopman surrogates are required to approximate the infinite-dimensional Koopman action. In particular, the Koopman-based control framework proposed in[strasser:2026] leverages the bilinear Koopman surrogate modeling approaches SafEDMD[strasser:schaller:worthmann:berberich:allgower:2025,strasser:schaller:worthmann:berberich:allgower:2026] and kEDMD[strasser:schaller:berberich:worthmann:allgower:2025] to ensure closed-loop properties of the underlying nonlinear system[strasser:berberich:schaller:worthmann:allgower:2025].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

More precisely, the resulting bilinear Koopman surrogate reads $$\Psi(x_{k+1}) = A \Psi(x_k) + B_0 u_k + \tilde{B} (u_k\otimes \Psi(x_k)) + r(x_k,u_k),$$ where the residual can be proportionally bounded by $$\|r(x_k,u_k)\| \leq c_x \|\Psi(x_k)\| + c_u \|u_k\|, \qquad c_x,c_u\geq 0,$$ and the matrices $A\in\bbR^{N\times N}$, $B_0\in\bbR^{N\times m}$, and $\tB\in\bbR^{N\times Nm}$ are either computed via kernel methods or least-squares regression over snapshot data, i.e., = \Psi(X^+) \begin{bmatrix} \Psi(X) \\ U \\

<!-- chunk {"id": "body-0043", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

The main limitation of the bilinear surrogate model [eq:bilinear-surrogate-literature-state] is its dependence on the state $x$, which is typically not accessible in practice and therefore restrictive. This manifests in two ways: first, learning the surrogate model requires state measurements; second, the resulting state-space representation relies on the state for both prediction and controller design. In the remainder of this paper, we circumvent these issues by generalizing the state-dependent Koopman surrogate models introduced above, deriving an input-output characterization that is independent of the unknown state $x$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

In this section, we discuss input-output representations of nonlinear systems, extending the ideas of linear systems, which we recall in Appendix[app:IO-representation-linear] for completeness. We note that the results developed in this section may be of independent interest beyond Koopman-based control; see Remark[rem:IO-interest-beyond-Koopman].

<!-- chunk {"id": "body-0045", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Consider the nonlinear system [eq:dynamics-nonlinear] with $x\in\bbX\subseteq\bbR^n$, $u\in\bbU\subseteq\bbR^m$, and $y\in\bbY\subseteq\bbR^p$, where the state $x$ is inaccessible but only input-output measurements are available. Since the original internal state $x$ is unknown, the core idea is to use past input-output measurements to infer knowledge about the initial condition. In particular, we seek an equivalent input-output representation of the nonlinear system[eq:dynamics-nonlinear] based on an extended state of delayed input-output measurements. To this end, we construct a delay embedding $\xi$ of past input-output measurements over a finite horizon $L$, which we call the extended-state vector, as common in the data-driven control literature.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

More precisely, we define u_{k-L}^\top & u_{k-L+1}^\top & \cdots & u_{k-1}^\top & y_{k-L}^\top & y_{k-L+1}^\top & \cdots & y_{k-1}^\top \end{bmatrix}^\top.$$ In the following, we investigate under which conditions there exists a smooth map $\cR_L$ such that the initial state $\bar{x}$ is uniquely reconstructable from a finite input-output sequence. In particular, we aim at the representation[isidori:1985] $$x_{k-L} = \cR_L(\useq_{k-L:k-1},\yseq_{k-L:k-1});$$ compare the reconstructability map in[iacob:szecsi:mate:beintema:schoukens:toth:2025].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

If such $\cR_L$ exists, we can substitute it into the combined dynamics and output equation to obtain an equivalent closed-form input-output relation that does not rely on the original state $x_{k-L}$. This is exactly characterized by uniform observability of the underlying nonlinear system[eq:dynamics-nonlinear], compare Definition[def:uniform-observability]. In the following, we characterize under which conditions this observability property holds and, thereby, an equivalent input-output representation exists. [ass:smoothness], we directly deduce $\cO_L\in C^1$, i.e., we can compute the Jacobian of $\cO_L$ w.r.t. $\bar{x}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Assumption[ass:lower-bound-Jacobian-observability-map] can be understood as a quantitative injectivity ensuring observability of the underlying system. A pointwise condition that is typically easier to verify in practice compared to Assumption[ass:lower-bound-Jacobian-observability-map] is $$\sigma_{\min}\!\left(\frac{\partial \cO_L}{\partial \bar{x}}(\bar{x},\useq_{0:L-1})\right) \geq \alpha$$ for all $\bar{x}\in\bbX$ and all $\useq_{0:L-1}\in\bbU^L$, where $\sigma_{\min}$ denotes the smallest singular value. However, this pointwise condition does not imply[eq:lower-bound-Jacobian-observability-map] in general, and the stronger Assumption[ass:lower-bound-Jacobian-observability-map] is required for the following result.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

There, we explain a given input-output trajectory of[eq:dynamics-nonlinear] by an extended-state system if there is a bijection between the given trajectory and the extended-state trajectory.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Suppose Assumption[ass:smoothness] and Assumption[ass:lower-bound-Jacobian-observability-map] hold.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Then, any trajectory $\{u_k,y_k\}_{k=-L}^{d}$ of[eq:dynamics-nonlinear] can be explained by the extended-state system with an extended state[eq:extended-state] initialized as u_{-L}^\top & u_{-L+1}^\top & \cdots & u_{-1}^\top & y_{-L}^\top & y_{-L+1}^\top & \cdots & y_{-1}^\top \end{bmatrix}^\top\in\bbR^{L(p+m)},$$ &= \left[\begin{array}{cccc|cccc} \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots \\\vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots

<!-- chunk {"id": "body-0052", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

The structure in $f_\xi$ due to the shifts of inputs and outputs results using similar arguments as in the linear case; see Appendix[app:IO-representation-linear]. It remains to show the last row of $f_\xi$, i.e., the dynamics for $y_k$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

First, we establish the reconstruction of the initial condition Assumption[ass:lower-bound-Jacobian-observability-map] directly implies that $\cO_L(\cdot,\useq_{0:L-1})$ is injective on $\bbX$ for every $\useq_{0:L-1}\in\bbU^L$. In particular, if $\cO_L(x_1,\useq_{0:L-1})=\cO_L(x_2,\useq_{0:L-1})$, then[eq:lower-bound-Jacobian-observability-map] gives $\alpha\|x_1-x_2\|\leq 0$ and, since $\alpha>0$, we conclude $x_1=x_2$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Hence, $\cO_L(\cdot,\useq_{0:L-1})$ is uniformly injective on $\bbX$, which corresponds to uniform observability of the underlying system according to Definition[def:uniform-observability]. Thus, the initial state can be uniquely reconstructed.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

More precisely, for each $\useq_{0:L-1}\in\bbU^L$ there exists a map $\cR_L(\useq_{0:L-1},\cdot): \bbR^{Lp}\to\bbX$ with $\cR_L = \cO_L^{-1}\in C^1$ such that \qquad\iff\qquad \bar{x} = \cR_L(\useq_{0:L-1},\zeta).$$ Applied along a trajectory at time $k$ with $\bar{x}=x_{k-L}$, $\zeta = \yseq_{k-L:k-1}$ and $\useq_{0:L-1}=\useq_{k-L:k-1}$, we obtain the state reconstruction formula[eq:reconstruction-x-from-u-y].

<!-- chunk {"id": "body-0056", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Substituting this into the dynamics[eq:dynamics-nonlinear] with[eq:dynamics-nonlinear-j-th-step] yields = f^L(x_{k-L},\useq_{k-L:k-1}) = f^L(\cR_L(\useq_{k-L:k-1},\yseq_{k-L:k-1}),\useq_{k-L:k-1})$$ $$y_{k} = h(f^L(\cR_L(\useq_{k-L:k-1},\yseq_{k-L:k-1}),\useq_{k-L:k-1}),u_{k}).$$ Finally, we replace $\useq_{k-L:k-1}$ and $\yseq_{k-L:k-1}$ by the respective entries in $\xi_k$ and extract the last row for the definition of $h_\xi$. This concludes the proof.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Proposition[prop:IO-representation-nonlinear] establishes a (non-minimal) input-output representation based on the extended state[eq:extended-state], that has the same input-output behavior as the unknown nonlinear system[eq:dynamics-nonlinear]. Although this representation is a natural nonlinear extension of linear subspace identification, the explicit structural input-output representation in[eq:IO-representation-nonlinear] is hardly exploited in the literature. More precisely, most of the available results for nonlinear subspace identification rely on linear-like approximations of the underlying nonlinear system[bamieh:giarre:2002,verdult:2002,williams:kevrekidis:rowley:2015]. Instead, we follow a different approach and use the inverse map $\cO_L^{-1}$to characterize the initial condition, exploiting uniform observability of the underlying system.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

More precisely, Assumption [ass:lower-bound-Jacobian-observability-map] enforces that the inverse map $\cO_L^{-1}(\useq_{0:L-1},\cdot)$ is well-defined on $\cO_L(\bbX,\useq_{0:L-1})$ for every $\useq_{0:L-1}\in\bbU^L$, since the uniform expansion condition[eq:lower-bound-Jacobian-observability-map] directly implies injectivity of $\cO_L(\cdot,\useq_{0:L-1})$ on $\bbX$, uniformly in $\useq_{0:L-1}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Combining this upper bound with the lower bound in Assumption[ass:lower-bound-Jacobian-observability-map] yields the bi-Lipschitz condition uniformly in $\useq_{0:L-1}\in\bbU^L$, where the upper inequality follows from the mean value inequality for vector-valued $C^1$-maps on the convex set $\bbX$[rudin:1976]. Inverting the lower bound in[eq:bi-Lipschitz-cO] directly yields i.e., the inverse map is Lipschitz continuous uniformly in $\useq_{0:L-1}\in\bbU^L$, which prevents noise amplification in the presence of small measurement errors.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Further, since $\sigma_{\min}(\frac{\partial\cO_L}{\partial\bar{x}})\geq\alpha>0$ uniformly on $\bbX\times\bbU^L$, which is implied by[eq:lower-bound-Jacobian-observability-map] via differentiation, the inverse function theorem[rudin:1976] guarantees that $\cO_L^{-1}\in C^1$, i.e., the inverse map is continuously differentiable. Hence, the initial state$\bar{x}$ can be uniquely and smoothly reconstructed from input-output sequences $\useq_{0:L-1}$, $\yseq_{0:L-1}$, and the extended system representation in[eq:IO-representation-nonlinear] is well-defined.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Takens' theorem[takens:1981,sauer:yorke:casdagli:1991] analyzes the delay-coordinate map$\cO_L$ defined in Definition[def:observability-map] in the autonomous case (i.e., without control input $u$). It states that, for generic systems and output maps, the map $\cO_L$ generically becomes an embedding for $L\geq 2n$. In contrast, uniform observability according to Definition[def:uniform-observability] requires injectivity for a fixed system and uniformly over all input sequences $\useq_{0:L-1}\in\bbU^L$, while the lower bound in Assumption[ass:lower-bound-Jacobian-observability-map] further strengthens this to a quantitative (well-conditioned) embedding, which is not guaranteed by Takens.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

In the remainder of the paper, we use the input-output representation established by Proposition[prop:IO-representation-nonlinear] to derive a Koopman-based output-feedback controller design method. We note, however, that Proposition[prop:IO-representation-nonlinear] is not specific to Koopman-based methods and could serve as a foundation for generalizing other nonlinear data-driven state-feedback designs to the output-feedback setting; see[martin:schon:allgower:2023b] for an overview of such designs with closed-loop guarantees. For example, one could define a set of basis functions and apply a nonlinear data-driven control approach as in[lazar:2024], or construct a polynomial approximation of the nonlinear input-output dynamics in the extended state $\xi$ and combine it with robust control and sum-of-squares (SOS) optimization as in[martin:allgower:2024,martin:2024]. In the present work, Koopman is a particularly natural choice given that the nonlinear dynamics[eq:dynamics-nonlinear] and the associated maps $f_\xi$, $h_\xi$ are unknown.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Data-driven output-feedback controller design for nonlinear systems", "weight": 1.0} -->

After establishing an input-output representation of unknown nonlinear systems, we leverage Koopman operator theory to design an output-feedback controller for nonlinear systems with rigorous closed-loop guarantees. To this end, Section[sec:IO-Koopman-surrogate] is devoted to deriving a bilinear surrogate model for the nonlinear input-output representation of the underlying system. Then, we use this surrogate to design an output-feedback controller in Section[sec:IO-Koopman-controller-design].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

Based on the nonlinear input-output representation[eq:IO-representation-nonlinear] of the underlying nonlinear system[eq:dynamics-nonlinear] established by Proposition[prop:IO-representation-nonlinear], we employ a Koopman lifting to bilinearize the representation, which is subsequently learned via data.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

To this end, we follow the line of thoughts presented in[strasser:schaller:worthmann:berberich:allgower:2026,strasser:worthmann:mezic:berberich:schaller:allgower:2026] and introduce the vector-valued observable function $\Psi: \bbR^{L(m+p)}\to\bbR^{N}$ with $$\Psi(\xi) = \begin{bmatrix} \xi^\top & \psi_{L(m+p)+1} & \cdots & \psi_N The observables $\psi_k$, $k=L(m+p)+1,...,N$, satisfy $\psi_k\in C^1(\bbR^{L(m+p)},\bbR)$ with $\psi_k=0$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

Then, $\Psi$ is pointwise bounded by for all $\xi\in\bbE\coloneqq \bbU^L \times \bbY^L\subseteq\bbR^{L(m+p)}$ with some $L_\Psi\in\bbR$[strasser:schaller:worthmann:berberich:allgower:2026].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

Since the nonlinear system [eq:dynamics-nonlinear] and its input-output representation[eq:IO-representation-nonlinear] are unknown, we characterize the dynamics via data. In particular, we collect input-output data $\cD$ consisting of $d$ trajectories of length $L+1$ as defined in[eq:data-collection-IO]. This trajectory allows us to arrange the data according to the defined extended state[eq:extended-state] for delay depth $L$, i.e., we obtain the extended-state data consisting of $d$ triplets of extended state, its successor, and its input, where $u_k=u_0^{(k)}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

In the following, we present two different data-driven surrogate representations derived using the data In Section[sec:IO-Koopman-surrogate-nominal], we first assume the existence of an exact Koopman bilinearization. Since this is typically not the case for general nonlinear systems, we allow for perturbations in the Koopman-based bilinear surrogate in Section[sec:IO-Koopman-surrogate-perturbed].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

The first presented data-driven surrogate model relies on the following (possibly restrictive) assumption on the employed Koopman bilinearization, which allows for the use of straightforward arguments. We stress, however, that the main results developed in this paper do not rely on this assumption, and the subsequent section considers a realistic and more general setting.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

The Koopman operator action corresponding to the nonlinear input-output representation[eq:IO-representation-nonlinear] admits an exact finite-dimensional bilinear representation of the form $$\Psi(\xi_{k+1}) = A_\mathrm{tr} \Psi(\xi_k) + B_{0,\mathrm{tr}} u_k + \tB_\mathrm{tr} (u_k\otimes \Psi(\xi_k)).$$ for all $\xi\in\bbE$ and $u\in\bbU$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

The unknown matrices $A_\mathrm{tr},B_{0,\mathrm{tr}},\tB_\mathrm{tr}$ of the bilinear Koopman representation[eq:Koopman-bilinearization-exact] are estimated from measured data. To this end, we solve the linear regression problem with the data matrices \Psi(\Xi) &= \begin{bmatrix} \Psi(\xi_1) & \cdots & \Psi(\xi_{d}) \Psi(\Xi^+) &= \begin{bmatrix} \Psi(\xi_1^+) & \cdots & \Psi(\xi_d^+) u_1\otimes \Psi(\xi_1) & \cdots & u_{d} \otimes \Psi(\xi_{d}) The regression problem[eq:regression-bilinear-EDMD-nominal] has a unique solution if $$\rank \begin{bmatrix} i.e., the stacked data matrix has full column rank.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

= \Psi(\Xi^+) \begin{bmatrix} \end{bmatrix}^\dagger = \Psi(\Xi^+) \begin{bmatrix} \end{bmatrix}^\top \left(\end{bmatrix}^\top This leads to the following intermediate result.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

Let Assumption[ass:Koopman-bilinearization-exact] and the rank condition[eq:rank-condition-linear-regression] hold. Then, any trajectory of the nonlinear input-output representation[eq:IO-representation-nonlinear] satisfies &= A \Psi(\xi_k) + B_{0} u_k + \tB (u_k\otimes \Psi(\xi_k)) 0_{p\times L(m+p-1)} & I_{p} & 0_{p\times N-L(m+p)} with $A,B_0,\tilde B$ in[eq:least-squares-solution] for all $\xi\in\bbE$ and $u\in\bbU$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

If the data is chosen such that the rank condition[eq:rank-condition-linear-regression] holds, then the learning error is zero, i.e., the least-squares solution[eq:least-squares-solution] corresponds to the true solution, i.e., $ A\_\mathrm{tr} & B\_{0,\mathrm{tr}} & \tB\_\mathrm{tr} Then, leveraging Assumption[ass:Koopman-bilinearization-exact] establishes[eq:bilinear-surrogate-nominal-dynamics]. The output equation[eq:bilinear-surrogate-nominal-output] directly follows from the nonlinear output equation[eq:IO-representation-nonlinear-output], i.e., &= \left[\begin{array}{cccc|cccc} \end{array}\right] &= \left[\begin{array}{cccc|cccc} \end{array}\right] This establishes[eq:bilinear-surrogate-nominal-output] and, thus, concludes the proof.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

According to Proposition[prop:Koopman-bilinearization-exact], we can design an extended-state-feedback controller for the nonlinear input-output representation[eq:IO-representation-nonlinear] based on the finite-dimensional error-free bilinear surrogate representation[eq:bilinear-surrogate-nominal]. Importantly, an extended-state-feedback controller for[eq:IO-representation-nonlinear] corresponds to an output-feedback controller for the underlying nonlinear system[eq:dynamics-nonlinear].

<!-- chunk {"id": "body-0076", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Since Assumption[ass:Koopman-bilinearization-exact] is typically hard to satisfy for general nonlinear systems, we loosen the assumption and allow for errors in the bilinear representation satisfying a proportional error bound.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

The Koopman operator action corresponding to the nonlinear input-output representation[eq:IO-representation-nonlinear] admits a finite-dimensional perturbed bilinear representation of the form $$\Psi(\xi_{k+1}) = A_\mathrm{tr} \Psi(\xi_k) + B_{0,\mathrm{tr}} u_k + \tB_\mathrm{tr} (u_k\otimes \Psi(\xi_k)) + r_\Psi(\xi_k,u_k),$$ where the residual $r_\Psi(\xi_k,u_k)$ is proportionally bounded by $$\|r_\Psi(\xi,u)\| \leq c_{\Psi,\xi} \|\Psi(\xi)\| + c_{\Psi,u} \|u\|, \qquad c_{\Psi,\xi},c_{\Psi,u} \geq 0$$ for all $\xi\in\bbE$ and

<!-- chunk {"id": "body-0078", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

The proportional structure of bound[eq:Koopman-bilinearization-proportional-error-bound] on the residual error is validated in[strasser:schaller:worthmann:berberich:allgower:2026] and represents a standard assumption in Koopman-based control[strasser:worthmann:mezic:berberich:schaller:allgower:2026]. This bound captures both the bilinear approximation error of the Koopman operator and the projection error arising from the finite-dimensional lifting function $\Psi$. For the latter, the proportional structure is widely assumed in the literature[strasser:schaller:worthmann:berberich:allgower:2026] and explicitly verified, e.g., in the kernel setting[strasser:schaller:berberich:worthmann:allgower:2025]. Moreover,[strasser:schaller:worthmann:berberich:allgower:2026]establishes a proportional bound on the Koopman-bilinearization error for control-affine nonlinear systems.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

As before, we estimate the unknown system matrices $A_\mathrm{tr},B_{0,\mathrm{tr}},\tB_\mathrm{tr}$ using the collected data, i.e., by solving for[eq:least-squares-solution] if the rank condition[eq:rank-condition-linear-regression] is satisfied. This leads us to the first main result of this paper.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Let Assumption[ass:Koopman-bilinearization-perturbed] and the rank condition[eq:rank-condition-linear-regression] hold.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Then, any trajectory of the nonlinear input-output representation[eq:IO-representation-nonlinear] satisfies &= A \Psi(\xi_k) + B_{0} u_k + \tB (u_k\otimes \Psi(\xi_k)) 0_{p\times L(m+p-1)} & I_{p} & 0_{p\times N-L(m+p)} where $A,B_0,\tilde B$ solve the regression problem[eq:regression-bilinear-EDMD-nominal] and where the residuals $r_\Psi(\xi,u)$ and $r_\Delta(\xi,u)$ are bounded by[eq:Koopman-bilinearization-proportional-error-bound] and $$\|r_\Delta(\xi,u)\|^2 \leq c_{\Delta,\xi}^2 \|\Psi(\xi)\|^2 + c_{\Delta,u}^2 \|u\|^2$$ =

<!-- chunk {"id": "body-0082", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Due to the perturbation $r_\Psi$ in[eq:Koopman-bilinearization-perturbed], the least-squares solution $(A,B_0,\tB)$ does not necessarily align with the true solution $(A_\mathrm{tr},B_{0,\mathrm{tr}},\tB_\mathrm{tr})$. Thus, we need to characterize the mismatch between the true values and the least-squares estimate.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

For the sake of compactness, we introduce the abbreviation r_\Psi(\xi_1,u_1) & \cdots & r_\Psi(\xi_{d},u_{d}) First, we exploit results from least-squares optimization[ziemann:tsiamis:lee:jedra:matni:pappas:2023] to derive the upper bound $$\left\|\begin{bmatrix} \Delta A & \Delta B_0 & \Delta \tB \end{bmatrix}\right\| \begin{bmatrix} A_\mathrm{tr} & B_{0,\mathrm{tr}} & \tB_\mathrm{tr} \end{bmatrix} - \begin{bmatrix} A & B_0 & \tB \end{bmatrix} \sigma_{\max}(R_\Psi(\Xi,U) \sigma_{\min}\left(This estimate is further refined by observing $$\sigma_{\max}(R_\Psi(\Xi,U)) \leq

<!-- chunk {"id": "body-0084", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

into[eq:proof-bound-Delta-literature] yields $$\left\|\begin{bmatrix} \Delta A & \Delta B_0 & \Delta \tB \end{bmatrix}\right\| with $c_{\Delta,u}$ defined in[eq:bound-r-Delta-constants].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Hence, we establish[eq:bilinear-surrogate-perturbed-dynamics] by rewriting[eq:Koopman-bilinearization-perturbed] using $ \Delta A & \Delta B\_0 & \Delta \tB \Psi(\xi) \\ u \\ u\otimes \Psi(\xi) The output equation[eq:bilinear-surrogate-perturbed-output] can be deduced using similar arguments as in the proof of Proposition[prop:Koopman-bilinearization-exact].

<!-- chunk {"id": "body-0086", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Further, the proportional error bound on $r_\Psi$ follows from[eq:Koopman-bilinearization-proportional-error-bound] in Assumption[ass:Koopman-bilinearization-perturbed]. It remains to show the bound[eq:bound-r-Delta] on $r_\Delta$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

To this end, we leverage the estimate[eq:proof-Delta-error] to obtain \Delta A & \Delta B_0 & \Delta \tB \|\Psi(\xi)\|^2 + \|u\|^2 + \|u\otimes \Psi(\xi)\|^2 \|\Psi(\xi)\|^2 + \|u\|^2 + \|u\otimes \Psi(\xi)\|^2 \leq \max_{u\in\bbU}\|u\| \|\Psi(\xi)\|.$$ to establish the error bound[eq:bound-r-Delta] with the constants $c_{\Delta,\xi}$ and $c_{\Delta,u}$ defined in[eq:bound-r-Delta-constants].

<!-- chunk {"id": "body-0088", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Theorem[thm:Koopman-bilinearization-perturbed] establishes a suitable bilinear input-output characterization of the underlying nonlinear system for a subsequent robust controller design. As already mentioned earlier, designing a lifted-state-feedback controller for the Koopman surrogate[eq:Koopman-bilinearization-perturbed] and, thus, for the input-output representation[eq:IO-representation-nonlinear] with extended state $\xi$, corresponds to an output-feedback controller for the underlying nonlinear system[eq:dynamics-nonlinear].

<!-- chunk {"id": "body-0089", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

The proof of Theorem [thm:Koopman-bilinearization-perturbed] builds on the same least-squares estimation technique used in[schmitz:bold:philipp:rosenfelder:eberhard:ebel:worthmann:2025] for local affine-linear regression, where the estimation error is controlled by bounding the residual and the smallest singular value of the data matrix separately. Two additional layers of work arise from the Koopman setting. First, the residual is not an externally bounded noise but a structural approximation error, whose norm must be estimated using the proportional bound[eq:Koopman-bilinearization-proportional-error-bound]. Second, the resulting matrix-level mismatch between true and estimated system matrices must be propagated to a pointwise residual bound, which requires the bilinear structure of the surrogate model.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Consequently, the constants $c_{\Delta,\xi}$ and $c_{\Delta,u}$ in[eq:bound-r-Delta-constants] explicitly reflect both the quality of the available data, through $\sigma_{\min}$, and the approximation quality of the lifting function $\Psi$, through the proportionality constants $c_{\Psi,\xi}$ and $c_{\Psi,u}$ in[eq:Koopman-bilinearization-proportional-error-bound].

<!-- chunk {"id": "body-0091", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

If the full state is measurable, i.e., $h(x,u)=x$, Theorem[thm:Koopman-bilinearization-perturbed] provides an alternative characterization of the learning error of the Koopman operator approximation from input-state data.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Here, similar to Assumption[ass:Koopman-bilinearization-perturbed], we assume the existence of a finite-dimensional perturbed bilinear representation of the form $$\Psi(x_{k+1}) = A_\mathrm{tr}(x_k) + B_{0,\mathrm{tr}} u_k + \tB_\mathrm{tr} (u_k \otimes \Psi(x_k)) + r_\Psi(x_k,u_k),$$ where $r_\Psi$ is bounded by[eq:state-data-case-residual-Psi] for some $c_{\Psi,x},c_{\Psi,u}\geq 0$, and compute $A,B_0,\tB$ based on the linear regression problem with the data matrices $X$, $X^+$, $U$, $U_X$ defined analogously to the matrices in[eq:data-matrices-IO-regression] and = c_{\Delta,u} \sqrt{1 +

<!-- chunk {"id": "body-0093", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

\max_{u\in\bbU}\|u\|^2} 2c_{\Psi,x}^2 \|\Psi(X)\|_\mathrm{F}^2 + 2c_{\Psi,u}^2 \|U\|_\mathrm{F}^2 \sigma_{\min}\left(In contrast, SafEDMD[strasser:schaller:worthmann:berberich:allgower:2025,strasser:schaller:worthmann:berberich:allgower:2026] derive proportional error bounds for bilinear approximations of the controlled Koopman generator and controlled Koopman operator by combining multiple autonomous variants and building on the respective error bounds in[schaller:worthmann:philipp:peitz:nuske:2023] and[nuske:peitz:philipp:schaller:worthmann:2023], respectively.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

This, however, requires multiple data sets collected under specific constant control inputs with i.i.d. samples, a sampling strategy that may be restrictive in practice. Instead, Theorem[thm:Koopman-bilinearization-perturbed] and, more specifically, the state-data surrogate[eq:state-data-case-surrogate] characterize the learning error for any data trajectory, without restricting to particular input choices and data requirements, relying instead on results from noisy least-squares optimization. Thus, Theorem[thm:Koopman-bilinearization-perturbed] is of independent interest beyond the input-output case, and may allow for more flexible sampling strategies, a broader class of control problems to be addressed within the Koopman framework, and potentially more interpretable error bounds due to its direct reliance on noisy least-squares optimization.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

If the input-output data is subject to noise, i.e., the nonlinear input-output dynamics[eq:IO-representation-nonlinear] satisfy for $\|w_k\|\leq \bar{w}$, the estimate can be straightforwardly adapted. In particular, the noise enters the lifted data matrix $\Psi(\Xi^+)$ and therefore deteriorates the least-squares estimate. Then, the mismatch between true values and the least-squares solution is bounded by $$\left\|\begin{bmatrix} \Delta A & \Delta B_0 & \Delta \tB \end{bmatrix}\right\| 2c_{\Psi,\xi}^2 \|\Psi(\Xi)\|_\mathrm{F}^2 + 2c_{\Psi,u}^2 \|U\|_\mathrm{F}^2 + \sqrt{d} L_\Psi \bar{w} \sigma_{\min}\left(where we assume Lipschitz continuity of the lifting function $\Psi$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Thus, the structure of the residual bound on $r_\Delta(\xi,u)$ remains unchanged.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

In this section, we establish a Koopman-based bilinear input-output surrogate representation with guaranteed proportional error bounds. This is particularly desirable as it allows for the application of Koopman-based controller designs for bilinear systems with closed-loop guarantees. Here, we exploit the (nonlinear) input-output representation[eq:IO-representation-nonlinear] of the unknown nonlinear system[eq:dynamics-nonlinear], relying on uniform observability of the underlying system. A possible alternative approach would be to first Koopman bilinearize the original nonlinear system, i.e., employing a state-based lifting function to obtain a bilinear surrogate in the lifted Koopman space, again with proportionally bounded residual error. Since this bilinear representation is unknown and the (state-based) lifting function is not accessible, we could use again input-output data to construct a representation with the same input-output behavior as the bilinear surrogate using an extended state.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Comparing both approaches, i.e., 1) input-output characterization for nonlinear systems, then Koopman bilinearization, or 2) Koopman bilinearization, then input-output characterization for bilinear systems, is an interesting direction for future research.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

In the following, we use the Koopman-based input-output surrogate established in Theorem[thm:Koopman-bilinearization-perturbed] to design a robust output-feedback controller with closed-loop guarantees for the nonlinear system[eq:dynamics-nonlinear]. To this end, we build on the state-feedback controller designs established in[strasser:schaller:worthmann:berberich:allgower:2026] using linear matrix inequalities and in[strasser:berberich:allgower:2025] using SOS optimization. Then, we use the proposed extended-state representation[eq:IO-representation-nonlinear] of the underlying nonlinear system[eq:dynamics-nonlinear] to define an output-feedback control law.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

While the generalization from state-feedback to output-feedback design can be done for any robust controller design for bilinear Koopman surrogates with (proportionally) bounded residual error, we rely on the SOS-based design proposed in[strasser:berberich:allgower:2025]as it provides the least conservative (guaranteed) closed-loop properties available in the literature.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Before stating our main theorem, we introduce some necessary SOS notation. We denote the set of all polynomials $s$ in the variable $z\in\bbR^N$ with degree $n_d$ and real coefficients by $\bbR[z,n_d]$. Similarly, we write $\bbR[z,n_d]^{p\times q}$ for the set of all $p \times q$-matrices with elements in $\bbR[z,n_d]$. We call $S\in\bbR[z,2n_d]^{p\times p}$ an SOS matrix in $x$, denoted by $S\in\mathrm{SOS}[z,2n_d]^p$, if it can be decomposed as $S=T^\top T$ for some $T\in\bbR[z,n_d]^{q\times p}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

If $(S-\varepsilon I_p)\in\mathrm{SOS}[z,2n_d]^p$ for some $\varepsilon>0$, we say $S$ is strictly SOS and write $S\in\mathrm{SOS}_+[z,2n_d]^p$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Suppose Assumption[ass:Koopman-bilinearization-perturbed], ensuring an approximate bilinear Koopman representation, holds.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Then, the output-feedback control law $$\mu(\xi) = \frac{1}{u_\mathrm{d}(\Psi(\xi))} L_\mathrm{n}(\Psi(\xi)) P^{-1} \Psi(\xi)$$ achieves robust exponential stability of the perturbed bilinear Koopman surrogate[eq:bilinear-surrogate-perturbed-dynamics] and, thus, exponential stability of the nonlinear extended-state dynamics[eq:IO-representation-nonlinear-state] for all initial conditions $\hat{\xi}\in\Omega(c^*)$ with \Psi(\xi)^\top P^{-1} \Psi(\xi) \leq c \Omega(c)\subseteq \bbE \text{ and } \mu(\xi)\in\bbU \text{ for all } \xi\in\Omega(c) The proof follows the arguments in[strasser:berberich:allgower:2025].

<!-- chunk {"id": "body-0105", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

However, we generalize the result to two different residual error bounds on $r_\Psi$ and $r_\Delta$, which are required in the present paper due to the surrogate structure in[eq:bilinear-surrogate-perturbed]. In particular, we account for an additional uncertainty channel in the robust controller design. In the following, we provide the key differences relative to the proof in[strasser:berberich:allgower:2025].

<!-- chunk {"id": "body-0106", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Then, substituting $K_\mathrm{n}(z)$ and $\cA(z)$ into[eq:Koopman-control-output-feedback], applying the Schur complement twice, and permuting rows and columns[strasser:berberich:allgower:2025] yields \left[\begin{array}{cc|ccc|ccc|c} & \frac{\tau_1(z)}{2 c_{\Psi,\xi}^2} I_N & 0 & 0 & 0 & \frac{\tau_1(z)}{2 c_{\Psi,u}^2} I_m & 0 & \frac{\tau_2(z)}{c_{\Delta,\xi}^2} I_N & 0 & 0 & 0 & \frac{\tau_2(z)}{2 c_{\Delta,u}^2} I_m & 0 & \frac{u_\mathrm{d}(z)}{\rho} P^{2}

<!-- chunk {"id": "body-0107", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

c_{\Delta,u}^2}{\tau_2(z)} I_m & 0 & \frac{\rho}{u_\mathrm{d}(z)} P^{-2} \end{array}\right] for all $z\in\bbR^N$ with $$\tilde{\mathfrak{B}}^\top = \left[\begin{array}{cc|ccc|ccc|c} & u_\mathrm{d}(z) I_N & K_\mathrm{n}(z)^\top & 0 & u_\mathrm{d}(z) I_N & K_\mathrm{n}(z)^\top & 0 \end{array}\right],$$ where the outer matrix $\mathfrak{B}$ follows according to the discussion in[scherer:weiland:2000] Further, we observe that the proportional error bounds[eq:Koopman-bilinearization-proportional-error-bound] and[eq:bound-r-Delta]

<!-- chunk {"id": "body-0108", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

on the residuals $r_\Psi$ and $r_\Delta$ imply the quadratic matrix inequalities \end{bmatrix}^\top \end{bmatrix}^\top Then, exploiting the generalized S-procedure[tan:2006],[eq:proof-dualized-QMI] implies that the robust controller $\mu(\xi)$ exponentially stabilizes the perturbed bilinear surrogate[eq:bilinear-surrogate-perturbed-dynamics] and, thus, with Assumption[ass:Koopman-bilinearization-perturbed], also the underlying nonlinear extended-state dynamics[eq:IO-representation-nonlinear-state][strasser:berberich:allgower:2025].

<!-- chunk {"id": "body-0109", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Theorem[thm:Koopman-control-output-feedback] establishes, to the best of the authors' knowledge, the first Koopman-based output-feedback controller design method with closed-loop guarantees for the underlying nonlinear system. In particular, we establish exponential stability of the extended-state system[eq:IO-representation-nonlinear], which has the equivalent input-output behavior as the underlying nonlinear system (compare Proposition[prop:IO-representation-nonlinear] under Assumptions[ass:smoothness] and[ass:lower-bound-Jacobian-observability-map]). Hence, Theorem[thm:Koopman-control-output-feedback] guarantees closed-loop guarantees for the nonlinear system[eq:dynamics-nonlinear] from input-output data. The parametrization used in Theorem[thm:Koopman-bilinearization-perturbed] for the Koopman-based surrogate can be obtained using the collected input-output data $\cD$and requires no state information. This paves the way forward to Koopman-based control in practical applications, where the full state is typically not accessible.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Note that the output-feedback controller established in Theorem [thm:Koopman-control-output-feedback] is based on the SOS-based state-feedback design proposed in[strasser:berberich:allgower:2025]. However, the Koopman-based bilinear surrogate[eq:bilinear-surrogate-perturbed] derived for the input-output representation[eq:IO-representation-nonlinear] is applicable more generally, i.e., it can be combined with any robust state-feedback controller design for (Koopman-based) bilinear surrogate models that provides closed-loop guarantees for the underlying nonlinear state-space system. In particular, the key contribution of Theorem[thm:Koopman-control-output-feedback] lies in its explicit connection between the input-output behavior of the nonlinear system[eq:dynamics-nonlinear] and the extended-state representation[eq:IO-representation-nonlinear], as formalized in Theorem[thm:Koopman-bilinearization-perturbed]. This connection enables an output-feedback controller design.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Since this relationship is already established in Theorem[thm:Koopman-bilinearization-perturbed], the resulting output-feedback construction directly extends to alternative state-feedback designs based on bilinear surrogate models with (proportionally) bounded residuals.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

The following corollary relates the established exponential stability of the extended state $\xi\in\bbR^{L(m+n)}$ to the original state $x\in\bbR^n$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Suppose Assumptions[ass:smoothness],[ass:lower-bound-Jacobian-observability-map], and[ass:Koopman-bilinearization-perturbed] hold. Let $\alpha\in\bbN$, $\beta\in\bbN_0$ with $\alpha\geq \beta$, $P=P^\top\succ 0$ of size $N\times N$, $L_\mathrm{n}\in\bbR[z,2\alpha-1]^{m\times N}$, $\tau_1,\tau_2\in\mathrm{SOS}_+[z,2\beta]$, $u_\mathrm{d}\in\mathrm{SOS}_+[z,2\alpha]$, and $\rho > 0$ such that[eq:Koopman-control-output-feedback] with $z\in\bbR^N$ holds.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Then, the output-feedback control law[eq:control-law-output-feedback] based on the extended state $\xi$ in[eq:extended-state] achieves exponential convergence of the state $x$ of the nonlinear system[eq:dynamics-nonlinear] to the origin for all initial conditions $\hat{\xi}\in\Omega(c^*)$, where $\Omega(c)$ and $c^*$ are as defined in[eq:Omega-c-star].

<!-- chunk {"id": "body-0115", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Theorem[thm:Koopman-control-output-feedback] already establishes exponential stability of the extended-state representation[eq:IO-representation-nonlinear] using Assumption[ass:Koopman-bilinearization-perturbed]. More precisely, exponential stability of the extended-state system ensures the existence of constants $c>0$ and $\lambda\in$ such that $\|\xi_{k}\| \leq c \lambda^{k} \|\xi_0\|$ for all $k\geq 0$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Using Proposition[prop:IO-representation-nonlinear] and uniform observability based on Assumptions[ass:smoothness] and[ass:lower-bound-Jacobian-observability-map], there exists the well-defined maps $\cO_L$ and $\cO_L^{-1}$ with $y_{k-L,k-1} = \cO(x_{k-L},\useq_{k-L,k-1})$ and $x_{k-L} = \cO_L^{-1}(\xi_k)$, where $\cO$ satisfies the bi-Lipschitz condition in[eq:bi-Lipschitz-cO].

<!-- chunk {"id": "body-0117", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Corollary[cor:Koopman-control-output-feedback-convergence] links the closed-loop properties for the extended-state representation[eq:IO-representation-nonlinear] to the original nonlinear state-space system[eq:dynamics-nonlinear]. In particular, by using the proposed output-feedback controller, we ensure exponential convergence of the state $x$to the origin.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Given the possibly high-dimensional lifting dimension $N$, the SOS program[eq:Koopman-control-output-feedback] may be computationally challenging to solve. While we leave a structured analysis of possible model order reduction techniques for the proposed output-feedback controller design to future work, a direct dimensionality reduction follows from combining the uncertainty characterizations of both residual terms $r_\Psi$ and $r_\Delta$.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

More precisely, solving & \frac{\tau_1(z)}{2 c_{\Psi,\xi}^2 + c_{\Delta,\xi}^2} I_N & \frac{\tau_1(z)}{2 c_{\Psi,u}^2 + c_{\Delta,u}^2} I_m \in\mathrm{SOS}[z,2\alpha]^{3N+n_u}$$ instead of[eq:Koopman-control-output-feedback] in order to obtain the control law $\mu$ in[eq:control-law-output-feedback] reduces the dimension of the SOS program by introducing additional conservatism through the combination of the two residual error bounds.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In this section, we illustrate our theoretical findings in numerical simulations. All our simulations are conducted on an i7 notebook using Yalmip[lofberg:2004] with the semi-definite programming solver MOSEK[mosek:2026]in MATLAB R2026a.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider the continuous-time nonlinear dynamical system which is discretized with a 4th order Runge-Kutta method[dormand:prince:1980] for the sampling time $T_s = 0.1$. Let $\bbX = [-1.5,1.5]^2$, $\bbU = $, and $\bbY=$. We collect $d$ data trajectories of length $L$, where we uniformly sample the initial state from $\bbX$ and evaluate the dynamics to obtain the corresponding input-output measurements. This allows us to construct the extended-state data as in[eq:data-extended-state].

<!-- chunk {"id": "body-0122", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In the following, we illustrate the effectiveness of the proposed Koopman-based surrogate model for prediction (Section [sec:numerical-examples:prediction]) as well as for an output-feedback controller design (Section[sec:numerical-examples:control]).

<!-- chunk {"id": "body-0123", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

First, we investigate the prediction capability of the proposed Koopman-based bilinear surrogate for the input-output behavior of the underlying nonlinear system. To this end, we employ a polynomial lifting function $\Psi(\xi)$, which contains all monomials up to degree $n_d$. Then, we choose $d=100$ and vary the delay length $L$ as well as the degree $n_d$ to build the surrogate in[eq:bilinear-surrogate-perturbed] purely based on input-output data.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

We consider the nominal bilinear surrogate $$\check{\Psi}_{k+1} = A \check{\Psi}_k + B_0 u_k + \tB (u_k \otimes \check{\Psi}_k), \check{\Psi}_0 = \Psi(\xi_0)$$ and compare the open-loop prediction error $$\frac{1}{N} \| \Psi(\xi_k) - \check{\Psi}_k \|$$ for random inputs $u_k$ uniformly sampled from $\bbU$. The resulting open-loop prediction error, averaged over 50 runs, is depicted in Fig.[fig:numerics-prediction-KoopmanIO]. Here, we illustrate different combinations of $L$ and $n_d$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[baseline]%\n \\draw[black, thick] (0,.6ex)--++(1.25em,0);\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}[baseline]%\n \\draw[black, thick, dashed] (0,.6ex)--++(1.25em,0);\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}[baseline]%\n \\draw[black, thick, dotted] (0,.6ex)--++(1.25em,0);\n \\end{tikzpicture}'

<!-- chunk {"id": "body-0126", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

language=<CodeLanguageLabel.TIKZ: 'Tikz'> confidence=None created_by=None text='\\begin{tikzpicture}[baseline]%\n \\draw[black, thick, dashdotted] (0,.6ex)--++(1.25em,0);\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> [Proposed bilinear surrogate[eq:Koopman-bilinearization-perturbed].] [Linear EDMDc surrogate[eq:linear-EDMDc-surrogate].]

<!-- chunk {"id": "body-0127", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

Open-loop prediction error of the (nominal) Koopman-based bilinear surrogateeq:Koopman-surrogate-nominal compared to a linear EDMDc surrogate for $n_d=1$, $L=100$, $n_d=2$, $L=3$, $n_d=2$, $L=10$, and $n_d=3$, $L=6$. The resulting errors are averaged over 50 independent runs.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

We emphasize that choosing $\Psi(\xi)=\xi$, i.e., $n_d=1$, yields a satisfactory prediction error for a sufficiently large delay length $L$. Further, as we see for $n_d=2$, increasing $L$ improves the prediction capabilities of the proposed bilinear surrogate. Here, the initial prediction error at $t=0$ indicates the approximation quality of the employed delay embedding of depth $L$ together with the $N$-dimensional nonlinear lifting function $\Psi$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

We compare the prediction error to a linear EDMDc-based Koopman surrogate as in[eq:EDMDc-linear-dynamics], i.e., $$\check{\Psi}_{k+1}^\mathrm{EDMDc} = A^\mathrm{EDMDc} \check{\Psi}_k^\mathrm{EDMDc} + B^\mathrm{EDMDc} u_k, \check{\Psi}_0^\mathrm{EDMDc} = \Psi(\xi_0)$$ where we use the same polynomial lifting function $\Psi(\xi)$ and the same collected data. Notably, the prediction error of EDMDc is worse than our proposed bilinear surrogate for all combinations of $n_d$ and $L$ studied in this paper. More precisely, the prediction error of EDMDc may quickly explode and, therefore, EDMDc is sensitive to the employed delay length $L$ and chosen degree $n_d$ of the lifting function.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

Thus, our proposed bilinear Koopman surrogate[eq:Koopman-bilinearization-perturbed]offers a more robust prediction w.r.t. the employed lifting and input-output characterization of the underlying nonlinear system.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

Now, we apply the proposed output-feedback controller design in Theorem[thm:Koopman-control-output-feedback] to show that the output of the nonlinear system converges to the origin. To this end, we choose $d=100$ with $L=1$ and a polynomial lifting function $\Psi(\xi)$ including all monomials up to degree $n_d=2$. For the bilinearization error in Assumption[ass:Koopman-bilinearization-perturbed], we assume the residual error bound[eq:Koopman-bilinearization-proportional-error-bound] to hold with constants $c_{\Psi,\xi}=c_{\Psi_u}=1\mathrm{e}-4$. Then, we compute the constants $c_{\Delta,\xi}$, $c_{\Delta,u}$ for the error bound[eq:bound-r-Delta] on the residual $r_\Delta$ according to[eq:bound-r-Delta-constants].

<!-- chunk {"id": "body-0132", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

To solve the SOS program [eq:Koopman-control-output-feedback], we choose $\alpha=\beta=1$ and \end{bmatrix}^\top \in\mathrm{SOS}[\Psi(\xi),2].$$ Then, the output-feedback control law is computed as in[eq:control-law-output-feedback]. To demonstrate its effectiveness, we sample 100 initial conditions $x_{-L}$ uniformly from $\bbX$ and simulate the nonlinear dynamics under a random input sequence $\useq_{-L,-1}$, drawn uniformly from $\bbU^L$, to initialize the extended state as in[eq:extended-state-initialization]. The resulting input-output measurements are used to construct the extended state $\xi_0$, after which the control law[eq:control-law-output-feedback] is applied. Fig.[fig:numerics-control] shows the closed-loop output trajectories $y$ for all 100 initial conditions, each of which converges to the origin.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

[Proposed output-feedback controller[eq:control-law-output-feedback].] [LQR based on EDMDc surrogate[eq:linear-EDMDc-surrogate].]

<!-- chunk {"id": "body-0134", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

Closed-loop simulation of the underlying nonlinear system with the proposed output feedback controller $\mu$ compared to an EDMDc-based LQR controller $\mu_\mathrm{LQR}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

We compare the resulting closed-loop behavior against one of the most widely used Koopman-based controller design approaches in the literature, namely a linear-quadratic regulator (LQR) designed on the linear EDMDc surrogate [eq:linear-EDMDc-surrogate][brunton:brunton:proctor:kutz:2016]. The LQR control law takes the form $\mu_\mathrm{LQR}(\xi) = -K \Psi(\xi)$, where $K_\mathrm{LQR}$ is obtained by solving the corresponding Riccati equation with $Q = R = I$. Unlike our proposed output-feedback controller[eq:control-law-output-feedback], the LQR controller $\mu_\mathrm{LQR}$ offers no closed-loop stability guarantees and fails to reliably stabilize the system.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

By exploiting the bilinear Koopman surrogate of the input-output representation within an SOS framework, we obtain rigorous closed-loop guarantees (Corollary[cor:Koopman-control-output-feedback-convergence]) and successfully stabilize all initial conditions.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

In the simulation above, we choose a delay length of $L = 1$ for the extended state $\xi$ and design the output-feedback controller $\mu$ accordingly. As observed in the prediction results of Section[sec:numerical-examples:prediction], a larger delay length $L$ and richer lifting function $\Psi(\xi)$ would generally be beneficial. However, the SOS-based controller design is computationally demanding with a computational complexity of $\cO((N^{2\alpha+1})^6)$ and therefore limited in the dimension of the extended state and the nonlinear lifting $\Psi$ that can be practically handled. An important direction for future work is thus the investigation of model order reduction schemes for the bilinear Koopman surrogate, which would render the controller design feasible for more appropriate choices of $L$ and $\Psi(\xi)$. Beyond SOS, combining the derived bilinear Koopman surrogate with other controller design techniques, such as MPC, offers another compelling direction to address this limitation.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a data-driven output-feedback controller design method for nonlinear systems that provides provable closed-loop guarantees while relying solely on measured input-output data. By combining Koopman operator theory with an extended state representation constructed from input-output trajectories, we derived a bilinear surrogate model directly from data, on which we applied robust state-feedback methods. Exploiting the observability of the underlying nonlinear system, we established exponential stability of the extended state and, consequently, exponential convergence of the original system state to the origin, with numerical simulations confirming the theoretical findings. To the best of our knowledge, this is the first Koopman-based controller design framework that operates exclusively on input-output data with rigorous closed-loop guarantees, addressing a fundamental gap in the data-driven control literature. Important directions for future work include extending the framework to handle noisy measurements with finite-sample error quantification or combining the design with model order reduction techniques to enhance practical applicability.
