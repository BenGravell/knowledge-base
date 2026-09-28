<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning and Control beyond Linearity: Towards a Non-asymptotic Theory for Bilinear Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This tutorial provides a unified view of the emerging area of bilinear learning and control. Using linear systems as a benchmark, it explains what fundamentally changes in the bilinear settings, how recent theory addresses finite-sample learning and control, and how these ideas connect to broader themes in nonlinear control, representation learning, and data-driven decision making. For learning, we emphasize tools that are particularly useful in the bilinear settings, such as one-sided Bernstein's inequality for dependent and heavy-tailed covariates, blocking arguments, and martingale concentration for input-dependent noise. We then apply these tools to obtain finite-sample learning guarantees for fully observed bilinear systems, partially observed bilinear systems, and linear systems with bilinear observations. For control, we discuss quadratic control from bilinear observations, where the classical separation principle fails, and review tractable approaches based on belief-space receding horizon control. We also cover stabilization of bilinear dynamics under state feedback using semi-definite programming, LMI relaxations, sum-of-squares methods, and Koopman-based lifting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We conclude by discussing connections to reinforcement learning and machine learning, and some open problems in combined learning and control of bilinear systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning and control of linear dynamical systems (time-invariant or time-varying) form the backbone of modern control theory. The recent surge of interest in data-driven control and non-asymptotic analysis of linear dynamical systems[dean2019sample,simchowitz2018learning,oymak2021revisiting,sarkar2019near,tsiamis2019finite], motivated by problems such as robot control in unknown environments, has also provided a key benchmark for reinforcement learning with continuous state and action spaces. This line of work has produced powerful tools for non-asymptotic system identification[dean2019sample,simchowitz2018learning,oymak2021revisiting,sun2022finite], uncertainty quantification[mania2019certainty], regret analysis[abbasi2011regret,lale2020explore,abeille2020efficient], and controller synthesis[abbasi2019model,faradonbeh2020optimism,hazan2020nonstochastic].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, much of what makes the linear setting analytically tractable depends on structural simplifications such as easy exploration, decoupling of estimation and control via the separation principle, and closed-form optimal controllers. These simplifications often fail in real-world systems. As a result, while the linear case remains foundational, it offers only a limited view of the challenges that arise in learning and control beyond linearity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bilinear dynamical systems provide a mathematically structured yet expressive framework that bridges classical linear systems and fully nonlinear dynamics. They arise naturally in a variety of domains from engineering, biology [bilinearbook], quantum mechanical processes[pardalos2010optimization], recommendation systems[koren2021advances] to sequence modeling[gu2023mamba]. Moreover, bilinear systems approximate a much broader class of nonlinear systems via Carleman linearization[kowalski1991nonlinear] or Koopman canonical transform[surana2016koopman,goswami2017global, bruder2021advantages,strasser2026overview] of control-affine nonlinear systems[svoronos1980bilinear,Lo1975bilinear]. Bilinear systems exhibit several phenomena that do not appear in the linear setting. In particular, fundamental system properties such as stability, stabilizability, controllability, and observability can depend on the input sequence[sattar2022finite, sattar2025finite].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will consider several canonical bilinear models, including fully observed bilinear state-space systems [sattar2022finite], partially observed bilinear systems[sattar2025finite], and linear systems with bilinear observation models[sattar2024learning,choi2025explore]. Across these formulations, we will provide a self-contained exposition of non-asymptotic learning[sattar2022finite,sattar2025finite,sattar2024learning,choi2025explore,chatzikiriakos2026endtoend] and control[chatzikiriakos2026endtoend,sattar2025sub,cao2026dual,strasser2023robust,strasser2023control,strasser2025koopman,strasser2026safedmd,strasser2025sos,strasser2025performance].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is our ambition that this tutorial serves as a comprehensive reference for new researchers as to what the state-of-the-art techniques are in the area of non-asymptotic analysis of bilinear systems. In particular, we aim to provide a self-contained exposition reviewing the main results along with the most important proof ideas. An important goal is to make the presentation accessible to a wider audience, without requiring prior background on bilinear systems theory. Lastly, we strive to establish a sound theoretical understanding of learning and control problems beyond linear dynamical systems. We aim to achieve this by revisiting the least squares theory for bilinear systems, introducing new tools, such as one-sided concentration approaches to persistence of excitation for heavy-tailed covariates, and input-dependent Martingale bounds for controlling error terms. Besides technical goals, this tutorial aims to establish a common language between control theorists, machine learning theorists, and statisticians; to push the boundary of non-asymptotic learning and control beyond linear dynamics.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Setting", "weight": 1.0} -->

In this tutorial, we consider the learning and control of dynamical systems that are governed by the state-space equations of the form where $x_t\in \mathbb{R}^{d_x}$, $u_t \in \mathbb{R}^{d_u}$, $y_t \in \mathbb{R}^{d_y}$, $w_t \in \mathbb{R}^{d_x}$, and $v_t \in \mathbb{R}^{d_y}$ denote the state, input, output, process noise, and measurement noise at time $t \geq 0$, respectively. The functions $(f_\theta,g_\theta)$ are parameterized by $\theta \in \mathbb{R}^{d_{\theta}}$ which may be unknown.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Setting", "weight": 1.0} -->

The goal of this tutorial is to learn and control the dynamical systems of the form[eqn:general\_dynamics] from a single input-output trajectory $\lbrace(u_t,y_t)\rbrace_{t=0}^T$. Without loss of generality, we consider $x_0 = 0$ throughout the manuscript.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Setting", "weight": 1.0} -->

The noise processes $\lbrace w_t \rbrace_{t\ge0}$ and $\lbrace v_t \rbrace_{t\ge 0}$ are assumed to be sequences of independent, zero-mean, $\sigma^2$-sub-Gaussian random vectors taking values in $\mathbb{R}^{d_x}$ and $\mathbb{R}^{d_y}$, respectively, for some variance proxy parameter $\sigma > 0$ (i.e., $\mathbb{E}[w_t]= 0$, and $\mathbb{E}[\exp(\left< z,w_t \right>)] \leq \exp(\sigma^2 \tn{z}^2/2)$ for all $z \in \mathbb{R}^{d_x}$).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Setting", "weight": 1.0} -->

Throughout this tutorial, we focus on dynamical systems of the form [eqn:general\_dynamics], where at least one of the state-space functions $(f_\theta,g_\theta)$ is bilinear in $(x_t,u_t)$. Bilinearity arises when there is inherent interaction, not merely linear superposition, between the state and input. Bilinear dynamics often arise from physical conservation laws when the control input corresponds to a flow parameter.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Setting", "weight": 1.0} -->

In a simple RC circuit with capacitor voltage as state $x(t)$ and variable conductance as input $u(t)$, Kirchhoff's Current Law states that u(t)(v\_{\mathrm{in}}-x(t))$. The forward Euler discretizations with step size $h$ results in the bilinear dynamics x_t -\frac{h}{C} u_t x_t + \frac{hv_{\mathrm{in}}}{C} u_t.$$ Bilinear state evolution also appears broadly beyond physical dynamical systems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Setting", "weight": 1.0} -->

Posterior computations in hidden Markov models (HMMs) can be written Consider an HMM with $S$ discrete states and $O$ possible observations, with state transition matrix $T\in\mathbb R^{S\times S}$ and emission matrix $E\in\mathbb R^{S\times O}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Setting", "weight": 1.0} -->

Let $x_t\in\mathbb R^S$ denote the vector of unnormalized forward probabilities $(x_t)_i = p(s_t=i,o_{0:t})$, let $y_t\in\mathbb R^O$ denote the vector of unnormalized observation probabilities $(y_{t})_o = \mathbb{P}(o_{t+1}=o, o_{0:t})$, and let $u_t=e_{o_t}\in\mathbb R^O$ be a one-hot encoding of the observation The forward recursion is bilinear: These example both motivate the general form for a multi-input-multi-output bilinear dynamical system.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Setting", "weight": 1.0} -->

A dynamical system of particular interest to us which is a special case of [eqn:general\_dynamics] is a partially-observed bilinear dynamical systems with linear state observation (BDS-PO). It has the state-space representation where $A_0, A_1, \dots, A_{d_u}$ denote the $d_u+1$ state matrices taking values in $\mathbb{R}^{d_x \times d_x}$, $B \in \mathbb{R}^{d_x \times d_u}$ denotes the input matrix, $C \in \mathbb{R}^{d_y \times d_x}$, and $D \in \mathbb{R}^{d_y \times d_u}$ denote the observation/measurement matrices. All of these matrices constitute the parameter $\theta=(A_0,...,A_{d_u},B,C,D)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Setting", "weight": 1.0} -->

We are interested both in learning the input-output behavior of unknown bilinear systems from a single trajectory of input-output samples $\lbrace(u_t,y_t)\rbrace_{t=0}^T$ and in feedback control design.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Setting", "weight": 1.0} -->

We may also expect bilinearity to arise in the measurement equation. In general, bilinear observations occur when the measurement involves an interaction between the state and the input.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Setting", "weight": 1.0} -->

Consider thermal observation of a circuit whose state contains the current $I_t$, as it can arise from parasitic inductance, and suppose the applied voltage $u_t$ is the input. The electrical power $I_t u_t$ is dissipated as heat, so a thermal measurement may be modeled as proportional to the dissipated power, i.e., where $C$ both selects $I_t$ from the overall state $x_t$ and includes the constant $\alpha$. This thermal observation is bilinear in the state and input.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Setting", "weight": 1.0} -->

Bilinear observations may also occur more broadly, from personalized recommendation systems to quantum mechanical systems. [Recommendations under preference dynamics] The simplest model of personalized recommendation posits that $y=u^\top x+$noise, where $y$ is an observed preference signal like a rating, e.g., 1-5 stars, $u$ is a latent factor for a recommended item, e.g., a movie, and $x$ is a latent factor for a user to whom the item was recommended. Supposing that user preferences are actually dynamic gives rise to a dynamical system of the form [eqn:general\_dynamics] in which the measurement equation is bilinear.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Task of Learning Bilinear Systems", "weight": 1.0} -->

In this section, we consider the task of learning the input-output behavior of unknown bilinear systems. We first cast the problem as a linear regression problem with nonlinear features, approximation bias, and intricate dependencies. We then present the least-squares solution with decompositions into relevant error terms and give an overview of the prototypical analysis strategy. Finally, we conclude with notes discussing existing ideas, alternative decompositions, and comparison with linear systems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our objective is to identify the parameter $\theta$, describing the state-space functions $(f_\theta,g_\theta)$ which can be in particular bilinear in $(x_t, u_t)$. The approach we aim to present, and which naturally applies to various families of bilinear systems, consists of reducing the dynamics to a linear form with an approximation bias of the form \forall~ t \ge 0, \qquad y_t = G\,\phi_t + z_t + \eta_t, where $\{y_t\}_{t \geq 0}$ is a sequence of outputs (when partially observed) or states (when fully observed) taking values in $\mathbb{R}^{d_y}$. $\{\phi_t\}_{t\geq 0}$ is a sequence of dependent, nonlinear features, constructed from inputs and/or states, taking values in $\mathbb{R}^{d_\phi}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

$\{z_t\}_{t \geq 0}$ is a sequence of approximation (or truncation) biases, that are intricately dependent on past states and inputs, taking values in $\mathbb{R}^{d_y}$. $\{\eta_t\}_{t \geq 0}$ is a sequence of dependent, correlated, and possibly heavy-tailed noise processes, taking values in $\mathbb{R}^{d_y}$. $G \in \mathbb{R}^{d_y \times d_\phi}$is the feature-to-output matrix and is a-priori unknown.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The matrix $G$ encodes information about the unknown parameter $\theta$ which, as we will see, is possible to extract using subspace methods such as Ho-Kalman [ho1966effective, oymak2021revisiting]. Therefore, we will mainly focus on the task of identifying $G$ and the challenges that come with that for bilinear systems.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The linear form [eqn:feature\_map] emerges from expressing $y_t$ using past states and inputs. This is achieved by unrolling the dynamics, say up to a truncation length $\tau>0$, as y_t &= g_\theta(f_\theta(f_\theta(\cdots (f_\theta(x_{t-\tau}, u_{t- \tau})+ w_{t-\tau},u_{t-\tau +1}) \cdots) + w_{t-2}, u_{t-1})+ w_{t-1}, u_t) + v_t.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

y_t &= g_\theta(f_\theta(f_\theta(\cdots (f_\theta(x_{t-\tau}, u_{t- \tau})+ w_{t-\tau},u_{t-\tau +1}) \cdots) \nonumber \\&\qquad\qquad\qquad\qquad\quad+ w_{t-2}, u_{t-1})+ w_{t-1}, u_t) + v_t The reader may notice that the form [eqn:feature\_map] is quite similar to that often appearing in the study of linear dynamical systems[ljung1999system, simchowitz2018learning, faradonbeh2018finite, sarkar2019near, sarkar2021finite, tsiamis2019finite, oymak2018non, ziemann2023tutorial].

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The key difference lies in the statistical dependencies that arise between the outputs $\{y_t\}_{t \geq 0}$, features $\{\phi_t\}_{t\geq 0}$, approximation biases $\{z_t\}_{t \geq 0}$, and the noise sequence $\{\eta_t\}_{t \geq 0}$. As we shall see, these dependencies pose non-trivial challenges for the analysis of identification procedures for bilinear systems.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To illustrate the intricate dependencies arising when performing a reduction of bilinear systems to a linear form with approximation bias, we consider the example of bilinear dynamical systems with partial linear observations [Bilinear dynamical systems] Fix a history length $\tau>0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

It can be shown that the state-space representation [eqn:BDS-PO] can be alternately represented as the non-linear input-output map \tilde{u}_{t-1} \otimes \tilde{u}_{t-2} \otimes u_{t-3} \\ \vdots \\\tilde{u}_{t-1} \otimes \tilde{u}_{t-2} \otimes \cdots \otimes u_{t-\tau+1} \end{bmatrix} + C \left(\prod_{\ell = 1}^{\tau-1} (u_{t-\ell}\circ A) \right) x_{t-\tau+1} + F_t \, \omega_t, \tilde{u}_{t-1} \otimes \tilde{u}_{t-2} \otimes u_{t-3} \\ \vdots

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The precise form of the feature-to-output matrix $G$ and the error matrix $F_t$ are deferred to [subsec:sysid\_partial\_bds].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In the first part of this tutorial, we aim to provide the key technical tools that one needs to solve the following identification problem: Given a single trajectory of the feature-output pairs $\lbrace \phi_t, y_t \rbrace_{t=1}^{T}$ obeying [eqn:feature\_map], construct an estimate $\widehat{G}$ of $G$ such that for a prescribed level of confidence $\delta \in $, \mathbb{P}\left(\opn{\widehat{G} - G} \le \varepsilon \right) \ge 1 - \delta, where $\varepsilon$ corresponds to the estimation error rate and typically would depend on the sample size $T$, the confidence level $\delta$, the dimensions $d_y$ and $d_\phi$, and the properties of the underlying bilinear system.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In general, under suitable noise assumptions on the underlying dynamical system, one expects the estimation error rate to satisfy \varepsilon \propto C_{\rm sys} \times \sqrt{\frac{\textup{problem dimension} + \log(1/\delta)}{\textup{sample size}}}, where $C_{\rm sys}$ denotes the system dependent constants. Furthermore, as we shall see next, an error rate of the above form [eq:err\_rate]will only be possible provided the sample size is sufficiently large, i.e., verifying a condition of the form T \gtrsim C_{\rm sys} \times (\textup{problem dimension} + \log(1/\delta)).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

This is similar to what one would expect for learning linear dynamical systems [ziemann2023tutorial], except that an understanding of the optimal dependencies on the underlying system properties and dimensions are far less understood for bilinear systems. Therefore, our focus in this paper will be on how to obtain rates that are at least reasonable in dimension dependence and somewhat tight in terms of $\delta$ and the sample size $T$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Least-Squares Regression Revisited", "weight": 1.0} -->

Given the linear form [eqn:feature\_map], a natural choice for estimating $G$ using a single finite trajectory of feature-output pairs $\lbrace \phi_t, y_t \rbrace_{t=1}^{T}$ is that of the Least-Squares Estimator (LSE), which is defined as \widehat{G} \in \argmin_{G \in \mathbb{R}^{d_y \times d_{\phi}}} \sum_{t=1}^{T} \tn{y_t - G \phi_{t}}^2.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Least-Squares Regression Revisited", "weight": 1.0} -->

To analyze the estimation error [eq:est error], a natural approach is to split it first into two terms, one that depends on the approximation biases, and the one that depends on the noise process.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Least-Squares Regression Revisited", "weight": 1.0} -->

The purpose of the first part of this paper is precisely to provide the tools for the analysis of these three terms, which will be the subject of the subsequent sections. Again, one may recognize that the error decomposition in [eqn:estimation\_error\_decomposition] is very similar to that used for linear dynamical systems [ziemann2022single]. Here, we want to emphasize that the major distinction lies in the statistical dependencies that arise between $\lbrace \phi_t \rbrace_{t\ge 1}$, $\lbrace \eta_t \rbrace_{t\ge 1}$, and $\lbrace z_t \rbrace_{t\ge 1}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Overview", "weight": 1.0} -->

The remainder of Part[part:learning] is organized as follows: In [sec:prels], we will provide some of the key probabilistic tools that we will rely on for the subsequent analysis. In [sec:onesided], we provide a a generic one-sided approach for establishing a persistence of excitation with heavy-tailed covariates. Finally, in [sec:sysid], we specialize the previously presented tools to the various classes of bilinear systems to obtain finite-sample bounds.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Notes", "weight": 1.0} -->

The approach of unrolling the dynamics to obtain a linear form with approximation bias has been extensively used in the study linear dynamical systems, particularly under partial observability [oymak2021revisiting, sarkar2021finite, he2026finite]. For bilinear systems, the same approach applies with the caveat that the resulting features are nonlinear, and have complex dependencies with the bias and noise terms [berk2012identification, sattar2022finite, sattar2024learning, sattar2025finite, chatzikiriakos2026endtoend].

<!-- chunk {"id": "body-0039", "role": "body", "section": "Notes", "weight": 1.0} -->

Least-squares estimation for system identification has a rich history [ljung1999system]. The decompositions that we presented have been recently analyzed quite extensively [simchowitz2018learning, faradonbeh2018finite, sarkar2019near, sarkar2021finite, tsiamis2019finite, oymak2018non, ziemann2023tutorial]. The decomposition of the statistical estimation error into a self-normalized term and a persistence of excitation term is due to [lai1982least, lai1983asymptotic] where they established the asymptotic properties of least squares for linear system identification. [sarkar2019near] revisited this decomposition using modern concentration tools to obtain finite sample size bounds. [simchowitz2018learning] was first to establish the so-called learning without mixing guarantees, i.e., finite-sample guarantees that do not degrade with the stability radius, by replacing mixing-time arguments with a block-martingale small-ball condition that lower bounds the empirical Gram matrix.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Notes", "weight": 1.0} -->

Most of these results focus on analyzing the estimation error in the operator norm. Recently, [zheng2026near, zhou2026clt] establish sharper finite sample bounds for the Frobenius norm error. In particular, [zhou2026clt]rely on a different decomposition than the ones typically used prior work and presented in this tutorial, and this is precisely what leads to their refined analysis.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Concentrations, Coverings, and Martingales", "weight": 1.0} -->

Before we present our main analysis tools for learning bilinear systems, we present a few preliminary concentration and covering tools that are frequently used in our analysis.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Concentration Inequalities", "weight": 1.0} -->

Concentration inequalities are powerful tools that allow us to derive quantitative bounds on the deviation of random quantities around their expected values [boucheron2003concentration]. Therefore, they are extremely useful for deriving non-asymptotic bounds for system identification, notably for linear dynamical systems [matni2019tutorial, ziemann2023tutorial]. There is a plethora of such inequalities with various strengths and weaknesses and our aim is not to cover all of these, nor to explain how to derive them. Instead, we only recall some of these that happen to be useful for our exposition.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Concentration Inequalities", "weight": 1.0} -->

First, we present below a one-sided Bernstein's inequality (Proposition 2.14 in [wainwright2019high]). This inequality characterizes the tail probability of the deviation of a sum of random variables bounded from above by their respective variances.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Concentration Inequalities", "weight": 1.0} -->

Let $X_1, \dots, X_n$ be independent random variables taking values in $\mathbb{R}$ and satisfying for all $i \in [n]$, $X_i \le b$ almost surely. We have for all $\varepsilon > 0$, \mathbb{P} \left(\sum_{i=1}^n \left(X_i - \mathbb{E}[X_i]\right) \geq n\varepsilon\right) \leq \exp \left(\frac{-n \varepsilon^2}{\frac{2}{n}\sum_{i=1}^n \mathbb{E}[X_i^2] + \frac{2b\varepsilon}{3}}\right).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Concentration Inequalities", "weight": 1.0} -->

Using Proposition [thrm:onesided\_bernstein], we can immediately deduce the following result: Let $X_1, \dots, X_n$ be i.i.d. copies of a random variable $X$ taking values in $\mathbb{R}$ with finite fourth moment. We have for all $\varepsilon \in $, \mathbb{P} \left(\sum_{i=1}^n X_i^2 \leq n(1-\varepsilon)\mathbb{E}[X^2]\right) \leq \exp \left(- \frac{n \varepsilon^2}{2} \cdot \frac{\mathbb{E}[X^2]^2}{\mathbb{E}[X^4] }\right). \nonumber The statement in Proposition [corr:onesided\_bernstein] only requires a fourth moment assumption to hold.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Concentration Inequalities", "weight": 1.0} -->

Therefore, this result is particularly powerful and will prove useful for establishing persistence of excitation results under heavy tailed covariates as we shall see in [sec:onesided].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Covering Arguments", "weight": 1.0} -->

In the previous subsection, we have seen concentration inequalities that hold for sums of scalar random variables. However, most of the quantities we aim to analyze are either matrices or vectors. To analyze such quantities, we use the so-called $\epsilon$-net arguments, which consist of reducing the analysis of matrices or vectors to simpler scalar terms for which scalar concentration inequalities can immediately apply. To start, let us define what we mean by nets in the case of the unit sphere in $\mathbb{R}^d$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Covering Arguments", "weight": 1.0} -->

Let $\epsilon > 0$. A finite set $\mathcal{N} \subseteq \mathcal{S}^{d-1}$ is said to be an $\epsilon$-net of $\mathcal{S}^{d-1}$ with respect to the norm $\tn{\cdot}$ if for all $x \in \mathcal{S}^{d-1}$ there exist $x' \in \mathcal{N}$ such that $\tn{x - x'} \le \epsilon$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Covering Arguments", "weight": 1.0} -->

For our purposes, we will need to use an $\epsilon$-net argument to control either the operator norm $\Vert W \Vert_{\textup{op}}$ of some random matrix $W$, or its minimum eigenvalue $\lambda_{\min}(W)$. Below, we present two lemmas that make this argument precise.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Covering Arguments", "weight": 1.0} -->

Let $W$ be a $k \times d$ random matrix, and $\epsilon \in $. Let $\mathcal{N}$ be an $\epsilon$-net of $\mathcal{S}^{d-1}$ with maximal cardinality.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Covering Arguments", "weight": 1.0} -->

Then, for all $\nu > 0$, we have \mathbb{P}\left(\Vert W \Vert_{\textup{op}} > \nu \right) &\le \left(1+\frac{2}{\epsilon}\right)^d \max_{x \in \mathcal{N}}\mathbb{P}\left(\tn{W x} Furthermore, if $W$ is a $d \times d$ symmetric random matrix, and $\epsilon \in (0,1/2)$, then, \mathbb{P}\left(\Vert W \Vert_{\textup{op}} > \nu \right) &\le \left(1+\frac{2}{\epsilon}\right)^d \max_{x \in \mathcal{N}}\mathbb{P}\left(\vert x^\top W x\vert > (1 - 2\epsilon)\nu \right), Let $W$ be a $d \times d$ symmetric random matrix, and $\epsilon

<!-- chunk {"id": "body-0052", "role": "body", "section": "Covering Arguments", "weight": 1.0} -->

Let $\mathcal{N}$ be an $\epsilon$-net of $\mathcal{S}^{d-1}$ with maximal cardinality. Then, for all $\nu > 0$, we have &\mathbb{P}\left(\lambda_{\min}(W) < \nu \right) \le \left(1+\frac{2}{\epsilon}\right)^{d} \max_{x \in \mathcal{N}} \mathbb{P}(x^\top W x < \nu + 2\epsilon \Vert W \Vert_{\textup{op}}) The proof of Lemma [lem:two-sided-net-nonsym] is standard and is therefore omitted. It can be found in [vershynin2018high,wainwright2019high,tao2023topics]. The proof of Lemma[lem:one sided net] is deferred to Appendix[app:covering].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Vector-valued Martingales & Concentration", "weight": 1.0} -->

An important class of vector-valued random variables that we will be using in our exposition is that of subgaussian random variables.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Vector-valued Martingales & Concentration", "weight": 1.0} -->

A random vector $x$ taking values in $\mathbb{R}^{d}$ is said to be $\sigma^2$-subgaussian with variance proxy parameter $\sigma>0$, if for every $\lambda \in \mathbb{R}^{d}$ we have \mathbb{E}[\exp(\lambda^\top x)] \leq \exp\left(\frac{\sigma^2 \tn{\lambda}^2}{2}\right).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Vector-valued Martingales & Concentration", "weight": 1.0} -->

Next, we present a version of Azuma-Hoeffding's inequality which is useful for analyzing sums of causally dependent random variables. In our case, the need for such a bound arises when upper bounding the truncation bias term.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Vector-valued Martingales & Concentration", "weight": 1.0} -->

Another key inequality is the self-normalized martingale concentration bound due to [abbasi2011improved]. Below, we present a version of this bound that can be found in [ziemann2023tutorial].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Notes", "weight": 1.0} -->

The topic of concentration of measure has been the subject of extensive research in the past century [boucheron2003concentration, van2014probability], and this tutorial cannot do it justice. The reader may also refer to the tutorials [matni2019tutorial] and [ziemann2023tutorial] that give a gentle exposition of such topics tailored for the control community. The concentration inequalities we present are somewhat standard, and there are many references where they can be found [boucheron2003concentration, van2014probability, vershynin2018high, wainwright2019high, rigollet2023high]. The idea of using covering or net arguments to analyze the operator norm of a random matrix or its minimum eigenvalue can be found in numerous handbooks [van2014probability, vershynin2018high, tao2023topics]. The exposition we follow is inspired by that in [vershynin2018high].

<!-- chunk {"id": "body-0058", "role": "body", "section": "Notes", "weight": 1.0} -->

It is worth mentioning that there exists other approaches to deal with the operator norm or minimum eigenvalue, notably generic chaining [van2014probability, vershynin2018high] and the PAC-Bayes approach [oliveira2016lower]. The self-normalized martingale bound we present is due to [abbasi2011regret], but the original ideas for deriving it are due to [de2004self, de2009self].

<!-- chunk {"id": "body-0059", "role": "body", "section": "Persistence of", "weight": 1.0} -->

Excitation with Heavy-tailed Covariates In this section, we provide a self-contained analysis of the lower tail of the empirical covariance matrix $\widehat{\Sigma}_T:= \sum_{t=1}^T \phi_t \phi_t^\top$ appearing in our error bound in [eqn:estimation\_error]. One advantage of analyzing the lower spectrum of the empirical covariance is that it decouples stability and persistence of excitation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

$\phi_t$ can be dependent, correlated, and heavy-tailed. More specifically, we assume the following dependence structure (as illustrated by Figure[fig:sliding-window-block-dependent]).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

A sequence of random vectors $\{x_t\}_{t \geq 0}$, taking values in $\mathbb{R}^{d_x}$, is said to have a block dependent structure, if there exists an integer $\tau \geq 1$ such that $x_{t_1}$ and $x_{t_2}$ are independent if and only if $|t_1 - t_2| > \tau$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

One of the major sources of difficulty in establishing the persistence of excitation result is the nonlinear dependence of $\phi_{t}$ on $u_{t-\tau+1}, \dots, u_{t}$ for all $t \ge \tau$. We need to understand how distributional properties of the input impact the lower spectrum of $\widehat{\Sigma}_T$. To that end, we start by introducing the property of hyper-contractivity, which guarantees a subgaussian-type lower tail of the empirical covariance matrix $\widehat{\Sigma}_T$, despite heavy-tailed and block-dependent covariates.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

A $d_x$-dimensional random vector $x $ is $(4,2, \gamma) $-hypercontractive, if $\mathbb{E}[(u^\top x)^4] \le \gamma \mathbb{E}[(u^\top x)^2]^2$, for all $u \in \mathbb{R}^{d_x}$. $(4,2,\gamma)$-hypercontractivity property is satisfied by many classical distributions. Notably, a $d_x$-dimensional standard Gaussian random vector satisfies it with $\gamma = 3$, while a $d_x$-dimensional random vector sampled uniformly from $\sqrt{d_x} \cdot \mathcal{S}^{d_x-1}$ satisfies it with $\gamma = 3/(1+2/d_x)$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

In [sec:sysid], we show that, in the case of bilinear systems, the nonlinear covariates $\{\phi_t\}_{t=1}^T$ are $(4,2,\gamma)$-hyper-contractive. Specifically, we will derive an upper bound on $\gamma$for various bilinear systems.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

[Distributional properties of $\phi_t$] $\lbrace \phi_t \rbrace_{t\ge 1}$ is a sequence of block-dependent, zero-mean, isotropic A $d_{\phi}$-dimensional random vector $\phi$ is isotropic if for all $x \in \mathbb{R}^{d_\phi}$, $\mathbb{E}[(x^\top \phi)^2] = \Vert x \Vert_{\ell_2}^2$., and $(4, 2, \gamma)$-hypercontractive for some $\gamma > 1$, random vectors taking values in $\mathbb{R}^{d_{\phi}}$. [assump:phi\_t distribution] covers a wide range of input distributions that may even be heavy-tailed, as it only requires conditions on the first four moments of the distribution.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Distributional Assumptions on the Covariates", "weight": 1.0} -->

This contrast with classical assumptions that require the input distribution to have subgaussian tails, and is also consistent with the intuition that bounding the smallest singular value of random matrix requires weaker moment conditions [koltchinskii2015bounding].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Lower Bound on the Spectrum of the Empirical Covariance", "weight": 1.0} -->

We are now ready to present our main result on the persistence of excitation.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Lower Bound on the Spectrum of the Empirical Covariance", "weight": 1.0} -->

Suppose the covariate process $\lbrace \phi_{t}\rbrace_{t \ge 1}$ satisfies Assumption[assump:phi\_t distribution]. Then, for all $\delta \in $, the event \lambda_{\min}\left(\sum_{t=1}^{T} \phi_t \phi_t^\top \right) \geq T/4, holds with probability at least $1- \delta$, provided that T &\gtrsim \tau\,\gamma\left (\log\left(\frac{2\tau}{\delta}\right) + d_{\phi} \log\left(1+\frac{16d_{\phi}}{\delta}\right) \right).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Lower Bound on the Spectrum of the Empirical Covariance", "weight": 1.0} -->

The proof of Theorem [thm:persistence] is deferred to Appendix [app:persistence excitation]. Interestingly, despite the presence of nonlinearities and dependencies in the covariate process $\{\phi_t\}_{t \geq 1}$, persistence of excitation is still guaranteed.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Notes", "weight": 1.0} -->

In general, to derive high-probability lower bounds on the smallest singular value of a random matrix, there are two approaches, namely a two-sided approach and one-sided approach. The two-sided approach aims at controlling both sides of the spectrum of the random matrix simultaneously (see For this purpose, one often relies on the net argument in Lemma[lem:two-sided-net-nonsym]. [jedra2020finite] leveraged this two-sided approach and used the Hanson inequality[rudelson2013hanson] to derive tight concentration bounds on the entire spectrum of the covariates matrix in the case of linear systems. The two-sided approach only provides meaningful bounds when dealing with stable systems. The one-sided approach aims at controlling directly the minimum eigenvalue and therefore typically requires weaker assumptions. Standard implementations of this approach also rely on a net argument, but would require a finer lower tail control for each fixed direction. In particular, such control may follow from a small-ball condition, as first observed in[Mendel2]. This idea was subsequently used to establish persistence of excitation for marginally stable linear systems[simchowitz2018learning].

<!-- chunk {"id": "body-0071", "role": "body", "section": "Notes", "weight": 1.0} -->

It is also worth mentioning that other techniques, such as PAC-Bayes methods[oliveira2016lower] and matrix Freedman inequalities[tropp2015introduction], can yield lower-tail bounds for the minimum eigenvalue without relying on a net argument.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Notes", "weight": 1.0} -->

The approach we present in this section for establishing persistence of excitation follows that of [sattar2025finite\_arXiv], which is a one-sided approach. It relies on the net argument of Lemma[lem:one sided net], then uses a one-sided Bernstein's inequality given in Proposition [corr:onesided\_bernstein] together with a blocking trick[yu1994rates].

<!-- chunk {"id": "body-0073", "role": "body", "section": "Bilinear System Identification", "weight": 1.0} -->

In this section, we provide end-to-end guarantees for learning bilinear dynamical systems in different settings (depending on whether the bilinearity appears in the state update equation or the observation model). Specifically, we use the tools and results from Sections[sec:prels] and[sec:onesided] to analyze the least-squares algorithm for estimating the Markov-like parameter matrix $G$ in each setting, using a single input-output trajectory $\{(u_t,y_t)\}_{t=0}^T$, and derive finite-sample learning guarantees.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Linear Dynamical Systems with Bilinear Observations", "weight": 1.0} -->

The first class of dynamical systems of the form [eqn:general\_dynamics] which is of interest to us is the linear dynamical systems with bilinear observations (LDS-BO). The state-space representation of LDS-BO is given by where $A \in \mathbb{R}^{d_x \times d_x}$ is the state matrix, $B \in \mathbb{R}^{d_x \times d_u}$ is the input matrix, and $C_0, C_1, \dots, C_{d_u}$ are the $d_u +1$ observation matrices taking values in $\mathbb{R}^{d_y \times d_x}$. Note that, unlike partially observed linear dynamical systems, the inputs $\{u_t\}_{t \geq 0}$ in [eqn:LDS-BO] directly interact with the states $\{x_t\}_{t \geq 0}$ to affect the observation $y_t$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Linear Dynamical Systems with Bilinear Observations", "weight": 1.0} -->

The parameters $\lbrace \lbrace C_k B \rbrace_{k=0}^{d_u}, \lbrace C_k A B \rbrace_{k=0}^{d_u}, \dots,$ $\lbrace C_k A^{\tau-1} B \rbrace_{k=0}^{d_u} \rbrace $ are what we refer to as the Markov-like parameters of the system Note that though the form of the Markov parameters is the same as for LTI systems, the relationship between inputs and outputs differs due to the bilinear observation..

<!-- chunk {"id": "body-0076", "role": "body", "section": "Linear Dynamical Systems with Bilinear Observations", "weight": 1.0} -->

$\tilde{u}_t$ and $\omega_t$ are as defined in [eqn:util\_omega\_def], and lastly, the matrix $H_t$ appearing in the noise process $\{\eta_t\}_{t \geq 0}$ is given by The goal here is to estimate the Markov-like parameter matrix $G$ by regressing $\{y_t\}_{t=\tau}^T$ on $\{\phi_t\}_{t=\tau}^T$. Before that, we state our assumptions on the system[eqn:LDS-BO].

<!-- chunk {"id": "body-0077", "role": "body", "section": "Linear Dynamical Systems with Bilinear Observations", "weight": 1.0} -->

The dynamical system in [eqn:LDS-BO] is strictly stable, i.e., $\rho(A) < 1$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Linear Dynamical Systems with Bilinear Observations", "weight": 1.0} -->

It is well-known that, when $\rho(A) < 1$, there exist $\rho \in (\rho(A), 1)$ and $\kappa \geq 1$ such that $\|A^k\| \leq \kappa \rho^k$ for all $k \in \mathbb{Z}_+$. The quantity $\kappa:= \sup_{k \in \mathbb{Z}_+}(\norm{A^k}/ \rho^k)$ is finite by Gelfand's formula, and it measures the transient response of the system and can be upper bounded by its $\mathcal{H}_\infty$ norm[tu2017non]. This decay condition is important for showing that the residual term $z_t$ is small when $\tau$ is large enough, and is a relatively common assumption[oymak2021revisiting, lee2022improved].

<!-- chunk {"id": "body-0079", "role": "body", "section": "Linear Dynamical Systems with Bilinear Observations", "weight": 1.0} -->

(b) $\lbrace w_t \rbrace_{t=0}^T$ and $\lbrace v_t \rbrace_{t=0}^T$ are sequences of independent, zero-mean, $\sigma^2$-subgaussian random vectors taking values in $\mathbb{R}^{d_x}$ and $\mathbb{R}^{d_y}$, respectively.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Learning Markov-like Parameter Matrix", "weight": 1.0} -->

In this subsection, we derive finite-sample guarantees on learning the Markov-like parameter matrix $G$ given by [eqn:G\_phi\_r\_eta\_LDS\_BO] via regressing $\{y_t\}_{t=\tau+1}^T$ on $\{\phi_t\}_{t=\tau+1}^T$. Now, recall from Section[subsec:LSE] that estimating $G$ via least-squares regression gives the estimation error decomposition [eqn:estimation\_error] and [eqn:estimation\_error\_decomposition]which are upper bounded to get the following result.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Learning Markov-like Parameter Matrix", "weight": 1.0} -->

The proof of Theorem[thm:main\_LDS\_BO] is deferred to Appendix[app:LDS-BO]. Theorem[thm:main\_LDS\_BO] extends the results in [sattar2024learning], [choi2025explore] to a more general bilinear observation model with $y_t = (u_t \circ C) x_t + v_t$ (unlike $y_t = u^\top C x_t + v_t$ in [sattar2024learning], [choi2025explore]). The proof of Theorem[thm:main\_LDS\_BO] relies on showing that $\phi_t$ in [eqn:G\_phi\_r\_eta\_LDS\_BO] satisfies the hypercontractivity condition (Def.[def:hypercont]) with $\gamma=9$. This is combined with Theorem[thm:persistence]to guarantee persistence of excitation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Fully Observed Bilinear Dynamical Systems", "weight": 1.0} -->

In this subsection, we consider the class of state-observed bilinear dynamical systems (BDS), which is also a special case of the dynamical systems of the form[eqn:general\_dynamics]. The state-space representation of BDS is given by $$x_{t+1} = A_0 x_t + \sum_{k=1}^{d_u} (u_t)_k A_k x_t + B u_t + w_t, \tag{BDS}$$ where $A_0, A_1, \dots, A_{d_u}$ denote the $d_u+1$ state matrices taking values in $\mathbb{R}^{d_x \times d_x}$, and $B$ denote the input matrix taking values in $\mathbb{R}^{d_x \times d_u}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Fully Observed Bilinear Dynamical Systems", "weight": 1.0} -->

Note that [eqn:BDS-FO] can also be viewed as a dynamical system with input-dependent state matrix $u_t \circ A = A_0 + \sum_{k=1}^{d_u} (u_t)_k A_k $. The learning problem in this setting can also be formulated as a least-squares regression. Specifically, note that [eqn:BDS-FO] can alternately be written as \text{where} \quad G &= \begin{bmatrix} B & A_0 & A_1 & \cdots & A_{d_u}\end{bmatrix}, \\\text{and} \quad \phi_t &= \begin{bmatrix} u_{t} \\\tilde{u}_{t} \otimes x_{t}\end{bmatrix}, where $\tilde{u}_t$ is as defined in [eqn:util\_omega\_def].

<!-- chunk {"id": "body-0084", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Stability of bilinear dynamical systems is typically input dependent. To see that, we can unroll the state dynamics in [eqn:BDS-FO] to write for all $t \ge 0$ x_{t+1} & = \sum_{\ell = 0}^t \left(\prod_{k = 0}^{\ell-1} (u_{t-k} \circ A)\right) \left(B u_{t-\ell} + w_{t-\ell}\right).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Observe that the products of matrices $\prod_{k = 0}^{\ell-1} (u_{t-k} \circ A)$may grow exponentially in norm if we consistently choose large inputs. This is precisely why stability in bilinear dynamical systems is more challenging than other classes of systems such as linear dynamical systems or switched systems.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Traditionally, notions like Mean Square Stability (MSS) have been considered to reason about the stability behavior of bilinear systems [kubrusly1985mean, pardalos2010optimization, sattar2022finite]. Typically, these notions are asymptotic in nature, require distributional assumptions on the inputs, permit diverging trajectories with nonzero probability, and may not allow us to obtain tight guarantees. We introduce an alternative notion of stability that naturally generalizes the classical notion of stability in standard LTI systems.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

The quantity $\kappa(\mathcal{M}, \rho)$ is defined in similar vein to that by [mania2019certainty] for LDS, and it captures the transient behavior of a system with state transition matrices varying in $\mathcal{M}$. Note that if $\rho(\mathcal{M}) < 1$, then for any $\rho > \rho(\mathcal{M})$, the quantity $\kappa(\mathcal{M}, \rho)$ is finite. Now, given a set $\mathcal{U} \subseteq \mathbb{R}^{d_u}$, we denote $\mathcal{U} \circ A:= \lbrace A_0 + \sum_{i=1}^{d_u} (u)_i A_i: u \in \mathcal{U} \rbrace$and introduce the following definition of stability.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Let $\mathcal{U} \subseteq \mathbb{R}^{d_u}$, $\kappa \ge 1$, and $ 0< \rho < 1$. We say that a bilinear dynamical system (as defined in [eqn:BDS-FO]) with state-transition matrices $\mathcal{A}:= \lbrace A_0, \dots, A_{d_u} \rbrace$ is $( \mathcal{U}, \kappa, \rho)$-uniformly-stable, if the joint spectral radius of the set $\mathcal{U} \circ \mathcal{A}$ satisfies: (i) $\rho(\mathcal{U} \circ \mathcal{A}) < \rho< 1$; and (ii) $\kappa(\mathcal{U}\circ \mathcal{A}, \rho) \le \kappa $.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Note that, if there exists a nonempty and bounded set $\mathcal{U} \subseteq \mathbb{R}^p$ such that $\rho(\mathcal{U} \circ \mathcal{A})< 1$, then for any $\rho(\mathcal{U} \circ \mathcal{A}) < \rho < 1$, the system is $(\mathcal{U}, \kappa, \rho)$-uniformly stable with $\kappa = \kappa(\mathcal{U} \circ \mathcal{A}, \rho) \vee 1$. Furthermore, we note that Definition [def:stability] naturally generalizes that introduced by [monfared2023stabilization]. Indeed, there the authors assume that there exists $u^\star$ such that $\rho(u^\star \circ A) < 1$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

This is equivalent to assuming that their system is $(\lbrace u^\star\rbrace, \kappa, \rho)$-uniformly-stable for some $\kappa \ge 1$ and $\rho(u^\star \circ A) <\rho < 1$. We need stronger requirements on the stability of the system in comparison with [monfared2023stabilization] because we are concerned with the task of identification. This requirement stems from the need to have persistence of excitation so that estimation is possible.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

Input choice We consider that the inputs $\lbrace u_t \rbrace_{t\ge 0}$ are sampled in an i.i.d. manner from some distribution $\mathcal{D}_{u}$ on $\mathbb{R}^{d_u}$. For ease of exposition, we will focus on the case where inputs are sampled uniformly at random from a sphere of radius $\sqrt{d_u}$, i.e., $u_t \sim \mathrm{Unif}(\sqrt{d_u} \cdot\mathcal{S}^{d_u-1})$. More generally, as long as the inputs are isotropic and are bounded with high probability, our results will still hold at the expense of longer proofs. Putting together this input choice with the stability definition, we are now ready to present the assumption we make on the stability of the bilinear system [eqn:BDS-FO].

<!-- chunk {"id": "body-0092", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

There exists $\kappa \ge 1$ and $\rho \in $ such that the bilinear dynamical system [eqn:BDS-FO] is $(\sqrt{d_u}\cdot\mathcal{S}^{d_u-1}, \kappa, \rho)$-uniformly stable.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Input Choice & Stability of Bilinear Dynamical Systems", "weight": 1.0} -->

In view of Assumption [assump:stability], choosing inputs uniformly at random from $\sqrt{d_u}\cdot \mathcal{S}^{d_u-1}$ guarantees stability almost surely. More generally, we can choose to sample inputs from any set $\mathcal{U}$, as long as the system is stable under such a set in the sense of Definition [def:stability]. However, the quality of estimation depends on whether inputs sampled from $\mathcal{U}$ are persistently exciting or not (see [sec:onesided]).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Learning State-Space Parameter Matrix", "weight": 1.0} -->

We are now ready to use the estimation error decomposition in [eqn:estimation\_error\_decomposition] to derive finite-sample learning guarantees for the bilinear system[eqn:BDS-FO]as follows.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Learning State-Space Parameter Matrix", "weight": 1.0} -->

The proof of Theorem[thm:main\_BDS\_FO] is deferred to the Appendix[app:BDS-FO]. The result in Theorem[thm:main\_BDS\_FO] is novel, and it is derived using the results and tools introduced in the previous sections. As compared to[sattar2022finite] (which requires Gaussian inputs/noise, mean square stability, and $B=0$), Theorem[thm:main\_BDS\_FO] holds for sub-Gaussian noise, non-zero activation matrix $B$, and uniform stability. Specifically, [sattar2022finite] shows that for Gaussian inputs/noise, the nonlinear features $\tilde{x}_t = \tilde{u}_t \otimes x_t$ satisfy the block Martingale small ball condition[simchowitz2019learning] with a block of length $k=1$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Learning State-Space Parameter Matrix", "weight": 1.0} -->

On the other hand, Theorem[thm:main\_BDS\_FO] is derived by proving that the nonlinear features $\phi_t = [u_t^\top~~\tilde{u}_t^\top \otimes x_t^\top]$ satisfy the hypercontractivity condition (Def.[def:hypercont]) with $\gamma \leq \bar \gamma$ under uniform stability. Combining this with the results of [sec:onesided] guarantees persistence of excitation, which is then combined with self-normalized martingale bounds for vector-valued noise processes to get the desired result. The errors due to noise and truncation are bounded using martingale-based concentration arguments. Combining these gives the desired learning guarantees for[eqn:LDS-BO].

<!-- chunk {"id": "body-0097", "role": "body", "section": "Learning Markov-like Parameter Matrix", "weight": 1.0} -->

In this subsection, we derive finite-sample guarantees on learning Markov-like parameter matrix $G$ (given by [eqn:G\_phi\_r\_eta\_BDS\_PO]) via regressing $\{y_t\}_{t=\tau+1}^T$ on $\{\phi_t\}_{t=\tau+1}^T$. Since the covariates and the residual/noise processes $\{\phi_t\}_{t=\tau+1}^T$, $\{z_t\}_{t=\tau+1}^T$, and $\{\eta_t\}_{t=\tau+1}^T$ are highly dependent, we use the estimation error decomposition in [eqn:estimation\_error] and [eqn:estimation\_error\_decomposition]which are upper bounded to get the following result.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Learning Markov-like Parameter Matrix", "weight": 1.0} -->

The proof of Theorem[thm:main\_BDS\_PO] is deferred to the Appendix[app:BDS-PO]. From the bound in Theorem[thm:main\_BDS\_PO], we see the recovery error $\Vert \widehat{G} - G \Vert_\textup{op} $ scales as, ignoring all other dependencies, $\tilde{\mathcal{O}} (\sqrt{(d_u+1)^{\tau}/(T-\tau)})$. This contrasts with partially observed linear systems, where typically we only have a polynomial dependence in the history length $\tau$, and also reflects the difficulty in learning bilinear systems from partial observations. To recover the unknown matrices $C, A_0, \dots, A_{d_u}, B$, we require $\tau$ large enough, typically larger than $2d_{x}$ (see Remark 3 in [sattar2025finite]).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Notes", "weight": 1.0} -->

The early literature on bilinear system identification has for the most part focused on developing estimation procedures. These include least squares and variants thereof [fnaiech1987recursive], augmented by subspace methods for partially observed systems [favoreel1999subspace,verdult2001identification,verdult2005kernel], as well as expectationmaximization algorithms [gibson2005maximum]. The asymptotic properties of these identification procedures have received comparatively less attention. A notable contribution in this direction is [chen1996strong], which established strong consistency and convergence-rate guarantees for extended least-squares estimation of discrete-time stochastic bilinear systems. Alongside the choice of estimator, the role of input design has been investigated in the continuous-time setting. Specifically, [juang2005continuous] developed identification procedures using specially designed inputs, and [SontagWangMegretski2009] characterized input classes sufficient for generic inputoutput identifiability. This overview is by no means exhaustive, and we refer the reader to the cited works and the references therein for further developments.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Notes", "weight": 1.0} -->

In contrast to this established identification literature, non-asymptotic learning guarantees for bilinear dynamical systems remain relatively sparse. [sattar2022finite] provided the first finite-time guarantees for learning state-observed bilinear systems under mean-square stability[kubrusly1985mean, pardalos2010optimization] and Gaussian inputs/noise. Specifically, [sattar2022finite] used the tools for deriving learning guarantees for linear dynamical systems, such as block martingale small ball methods [simchowitz2018learning], and self-normalized martingales[sarkar2018fast]. More recently, [chatzikiriakos2026endtoend] derived finite-sample identification bounds from i.i.d. data using constant-input experiments that reduce bilinear identification to linear and affine subproblems, and incorporated these bounds into robust controller design. These results also motivate further investigation of input design for learning partially observed bilinear systems. In the linear setting, carefully designed control inputs, rather than i.i.d.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Notes", "weight": 1.0} -->

Gaussian inputs, can yield strong statistical estimation rates[sun2022finite]. We believe that for partially observed bilinear dynamical systems, the exponential growth of the number of Markov-like parameters, leading to an error rate of $\tilde{\mathcal{O}} (\sqrt{(d_u+1)^{\tau}/(T-\tau)})$, can be avoided by the input design. Lastly, the learning guarantees in [sec:sysid] require uniformly stable bilinear systems. In the linear setting, non-asymptotic identification guarantees extend to marginally stable systems under both full and partial observation [simchowitz2018learning, sarkar2018fast, simchowitz2019learning, bakshi2023new], and to certain classes of unstable systems under full observation [sarkar2018fast,faradonbeh2018finite]. Extending the presented guarantees beyond uniformly stable bilinear systems, even to the marginally stable case, remains an open problem.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Notes", "weight": 1.0} -->

We now turn our discussion to the control of bilinear systems. First, we discuss the design of optimal controllers under quadratic costs and partial observations. Unlike for linear systems, bilinearity, even only in the observations, complicates the optimal control solution. In particular, we show that the well-known separation principleof linear quadratic control does not apply when the observations are bilinear. Naively following this principle may even lead to failures of stabilization. Instead, we propose and numerically investigate a method based on receding horizon control in belief space.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Notes", "weight": 1.0} -->

Second, we turn to stabilization of bilinear dynamics under perfect state observation. Turning from challenges that arise due to noise and partial observation, with bilinearity only in the measurements, we instead focus on the challenges of controlling imperfectly modeled deterministic bilinear dynamics under full state observation. We review strategies based on semidefinite programming, using linear matrix inequality (LMI)-based techniques and sum-of-squares (SOS) optimization, for designing controllers and Lyapunov functions. Finally, we discuss connections between bilinear control and general classes of nonlinear dynamics through Koopman theory, highlighting the broad applications.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Control of Linear Dynamics from Partial Bilinear Observations", "weight": 1.0} -->

We consider quadratic control of [eqn:LDS-BO] with Gaussian noise (BO-LQG), defined in the finite-horizon optimal control problem \min_{\mu_{0:T-1}} &\mathbb{E} \left[x_T^\top Q_T x_T + \sum_{t=0}^{T-1} \left(x_t^\top Q x_t {+} u_t^\top R u_t \right) \right] \\\text{s.t.} \quad &eqn:LDS-BO, \quad \text{and} \quad u_t = \mu_t(u_0, \dots, u_{t-1},y_0, \dots, y_{t-1}), \end{aligned} \tag{BO-LQG}$$ \min_{\mu_{0:T-1}} &\mathbb{E} \left[x_T^\top Q_T x_T +

<!-- chunk {"id": "body-0105", "role": "body", "section": "Control of Linear Dynamics from Partial Bilinear Observations", "weight": 1.0} -->

We additionally define the shorthand $\mathcal{I}_t:= \{u_0, \dots, u_{t-1},y_0, \dots, y_{t-1} \}$ as the information available at time $t \geq 0$. Moreover, we assume the following.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Control of Linear Dynamics from Partial Bilinear Observations", "weight": 1.0} -->

[eqn:bilinear LQG] is a slight variation on the classical linear-quadratic Gaussian (LQG) problem; if the matrices $C_1=\cdots=C_{d_u}=0$, it reduces to LQG. In classical LQG, the optimal controller follows the separation principle, i.e., state estimation and control design can be solved independently. In particular, the state is estimated via Kalman filtering [kalman1960new], and the control input is obtained by applying the optimal linear feedback gain to the state estimate. In the following, we explore how the separation principle can fail in this simple departure from standard LQG.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Kalman Filtering", "weight": 1.0} -->

State estimation for bilinear systems follows the same logic as for linear time-varying systems. We thus begin by defining the Kalman filter for For notational convenience, we define the input-dependent observation matrix $C(u_t):= C_0 + \sum_{k=1}^{d_u}(u_t)_k C_k$. Let $\hat{x}_{t|t- 1}:= \mathbb{E} [x_t | \mathcal{I}_t]$ be the estimated state at time $t$, and $\Sigma_{t|t- 1}:= \mathbb{E} \left[(x_t - \mathbb{E} [x_t | \mathcal{I}_t])(x_t - \mathbb{E} [x_t | \mathcal{I}_t])^\top\right]$ be the estimation error covariance.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Kalman Filtering", "weight": 1.0} -->

Unlike Kalman filtering from linear measurements, both the Kalman gain $L(u_t)$ and the error covariance $\Sigma_{t + 1|t}$ depend on the control inputs up to time $t$. Nonetheless, it is easy to show that the Kalman filter provides the full posterior state distribution. The following lemma readily follows from[kalman1960new] by replacing $C_t$ with $C(u_t)$, which is a deterministic quantity conditioned on $u_t$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Kalman Filtering", "weight": 1.0} -->

Under Assumption[assump noise, initial, cost](i) & (ii), the Kalman filtering algorithm gives the full posterior distribution of the state $x_t$ given the information $\mathcal{I}_t$, $x_t | \mathcal{I}_t \sim \mathcal{N}(\hat{x}_{t|t- 1}, \Sigma_{t|t- 1})$. [lemma:optimality of KF] readily follows from[kalman1960new] by replacing $C_t$ with $C(u_t)$ which is a deterministic quantity conditioned on $u_t$. Moreover, since the posterior distribution of the state $x_t$ is Gaussian, using similar argument as[bertsekas2012dynamic], we note that the values $\hat{x}_{t|t- 1}, \Sigma_{t|t- 1}$computed by the Kalman filter are sufficient statistics for any policy.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Kalman Filtering", "weight": 1.0} -->

| scale=0.20 Figures/nonconvex_cost_exp_2_new.png | scale=0.20 Figures/nonconvex_cost_exp_3_new.png | scale=0.20 Figures/nonconvex_cost_exp_4_new.png | scale=0.20 Figures/nonconvex_cost_exp_5_new.png | The landscape of $f(u)=f_\text{LQG}(u) + g(u)$ depends on the distance between the global minima of $f_\text{LQG}(u)$ and the global maxima of $g(u)$, which depends on how far the LQG input is from an input which leads to loss of observability, which in the scalar case is given by $-\frac{C_0}{C_1}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

The certainty equivalent separation principle treats the state estimate $\hat x_{t|t-1}$ as if it were true. As a result, the policy follows the linear-quadratic regulation (LQR) state-feedback rule. We refer to this as the LQG controller. At every time $0 \leq t \leq T{-}1$, the LQG controller is given by \text{where}\quad L_t &= -(B^\top K_{t+1} B + R)^{-1}B^\top K_{t+1} A, and the matrices $K_t$, starting from $K_T = Q_T$, are given recursively by the Riccati equation P_t &= A^\top K_{t+1} B (B^\top K_{t+1} B + R)^{-1}B^\top K_{t+1} A, \\This strategy computes actions according only to state estimates with no accounting for the effect of the control input on observation.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

It is immediate to observe failure modes of this approach, especially when First, consider the case that $\hat x_0$, the mean of the initial state's prior distribution, is equal to zero. Then, we have $u_0=0$, $C=0$, and, hence, $L(u_t)=0$ and $\hat x_{1|0}=0$. This pattern continues, and no control input is applied. If the matrix $A$ has spectral radius larger than one, the state grows exponentially over the time horizon and so does the accumulated cost. Even when $\hat x_0\neq 0$, similar issues can emerge, as illustrated in the following example.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

Consider a system with $A=1$, $B=\begin{bmatrix}0 & 1\end{bmatrix}$, $C_0=C_2=0$ and $C_1=1$. The optimal state-feedback control gains satisfy $K_t e_1 = 0$ since the first control input incurs a cost but does not affect the state. As a result, $(u_t)_1 = 0$ and thus $C(u_t) = 0$ for all $t \geq 0$.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

Consider a system with $A{=}1$, $B{=}\begin{bmatrix}0 & 1\end{bmatrix}$, $C_0{=}C_2{=}0$ and $C_1{=}1$. The optimal state-feedback control gains satisfy $K_t e_1 {=} 0$ since the first control input incurs a cost but does not affect the state. As a result, $(u_t)_1 {=} 0$ and thus $C(u_t) {=} 0$ for all $t {\geq} 0$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

In this example, no information about the state is ever observed. As a result, using the separation principle is basically equivalent to applying the optimal open-loop sequence of actions. It is not difficult to verify that alternative linear policies can achieve a lower quadratic cost by preventing this loss of observability.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

We now show that the sub-optimality of the separation principle indeed holds more generally by analyzing the dynamic programming procedure. Using the same proof technique as [bertsekas2012dynamic], the optimal policy for the last stage is given by $u_{T-1}^\star = u_{T-1}^{LQG}$, which is the LQG controller given by[eqn:LQG Policy]. However, things change for $t \leq T-2$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

The second term $g(u_{T-2})$ corresponds to the estimation error covariance at time $T-1$, and it depends on control input $u_{T-2}$ via the input dependent observation matrix $C(u_{T-2})$. This dependence is the precise violation of the separation principle.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

The LQG controller may locally maximize the cost, and the optimal control policy $\mu^\star_t(\mathcal I_t)$ is not affine in the estimated state $\hat x_{t|t-1}$ in general.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

Consider $T=2$ and the dynamic programming algorithm described above. Let $u_\text{LQG}= \mathcal A^{-1} \mathcal B \hat x$ and suppose that $C(u_\text{LQG})=0$. In this case, the minimum of $f_{LQG}$ coincides with the maximum of $g$. Depending on their relative magnitudes, this can result in a local maximum for their sum $f=f_{LQG}+g$. Concretely, in the scalar case $n=m=p=1$, we may compute the second derivative of $f$ and evaluate it at $u_\text{LQG}$: f''(u\_\text{LQG}) = 2\mathcal{A} - (2\mathcal{G} C\_1^2 \Sigma\_{0}^2)/\Sigma\_v.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

$ This is negative when $\mathcal G C\_1^2 \Sigma\_{0}^2 > \mathcal A \Sigma\_v$, i.e. when the measurement noise is small relative to the state uncertainty. In the scalar setting, one may further characterize all critical points of $f$ as the roots of a degree 5 polynomial. By verifying that there does not exist an affine control law which satisfies this critical point equation for all $\hat x$, we conclude that the optimal policy is not generally affine. [thm:summary_sep] summarizes Theorems 1 and 2 in[sattar2025sub]. Finding an analytical expression for the optimal controller is challenging in general because of: (i) non-convexity, (ii) nonlinearity, and (iii) the existence of multiple critical points. We investigate the trade-off numerically in Figure[figure1] by plotting $f_\text{LQG}$ and $f$in a one dimensional setting. We see cases where the LQG control is optimal, sub-optimal, or even a local maximum.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

These cases vary based on how close the LQG input is to an input which causes loss of observability.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Separation Principle", "weight": 1.0} -->

Thus we conclude that control designed based on the separation principle is not generally reliable for BO-LQG. It is natural to ask whether iteratively linearizing the dynamics around the current state estimate and following LQG control could recover a better controller. We argue that it cannot: in the BO-LQG setting, this iterative linearization scheme converges after a single step to the LQG controller analyzed above. The reason is that, for any fixed input $u_t$, the observation model is already exactly linear in $x_t$; the state dynamics are also already linear. Consequently, linearizing introduces no additional error, so the iterativeprocedure terminates immediately, and the resulting controller coincides with the suboptimal policy analyzed in this section.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Model Predictive Control in Belief Space", "weight": 1.0} -->

separation in optimal control is that of separating the computation of the posterior distribution of the state from the computation of the control input. This idea motivates us to reformulate [eqn:bilinear LQG] in terms of the values $(\hat{x}_{t|t-1}, \Sigma_{t|t-1})=:b_t $ computed by the Kalman filter. By a similar argument as[bertsekas2012dynamic], this belief state is a sufficient statistic for any control policy. Belief space planning is a common strategy in robotics to handle practical issues like path planning under perception uncertainties [platt2010belief]. We take inspiration from this perspective and reformulate the original optimal control problem into a belief space control problem.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Model Predictive Control in Belief Space", "weight": 1.0} -->

First, the original finite-horizon quadratic cost [eqn:bilinear LQG] can be rewritten in terms of the belief state \mathbb{E} \big[x_t^\top Q x_t \mid \mathcal{I}_t \big] &= \hat x_{t|t-1}^\top Q \hat x_{t|t-1} + \tr(Q\Sigma_{t|t-1}).

<!-- chunk {"id": "body-0125", "role": "body", "section": "Model Predictive Control in Belief Space", "weight": 1.0} -->

Notice that this is a stochastic optimal control problem with a fully observed (belief) state. Thus, the challenge has transformed from reasoning about partial observation to synthesizing a controller for nonlinear dynamics, which arise from the nonlinear covariance evolution.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Model Predictive Control in Belief Space", "weight": 1.0} -->

We now propose a belief-space model predictive control (MPC) method, B-MPC, that plans over a deterministic surrogate of the belief dynamics induced by the Kalman filter. Notice that the belief state update is stochastic and depends on the bilinear observation $y_t = C(u_t) x_t + v_t$. Consider its deterministic surrogate \bar \Sigma_{t+1} &= A \bar\Sigma_t A^\top +\bar L(u_t)C(u_t) \bar\Sigma_{t}A^\top + \Sigma_w, $\bar L(u_t)$ is defined analogously to $L(u_t)$ in [eq:kf\_bo] with $\Sigma_{t|t{-}1}$ replaced by $\bar\Sigma_{t}$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Model Predictive Control in Belief Space", "weight": 1.0} -->

Let $\bar b_t:= (\bar x_t, \bar \Sigma_t)$ and define the finite horizon MPC objective at time $t \geq 0$ as $$J_t^{\text{MPC},H}(u_t,\dots,u_{t{+}H{-}1}; b_t) = \sum_{\tau = t}^{t+H-1} \ell(\bar b_\tau, u_\tau) + \phi(\bar b_{t+H}),$$ where the trajectory $(\bar b_\tau)_{\tau=t}^{t+H}$ is generated by [eqn:det-belief-update] as a function of inputs $u_t,\dots,u_{t+H-1}$, starting from $\bar b_t = (\hat x_{t|t-1},\Sigma_{t|t-1})$, the true current belief state.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Model Predictive Control in Belief Space", "weight": 1.0} -->

Algorithm[alg:B-MPC]presents the MPC strategy.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Kalman filter diagnostics. [width=, trim=0.5 0 0 0, clip]Figures/action\_gap\_vs\_tr\_sigma\_synthetic\_large.png Action difference vs $\text{tr}(\Sigma)$. [width=, trim=0 0 0 0.5, clip]Figures/counterfactual\_input\_scatter\_on\_sep\_rollout\_per\_dim\_largev2.png Counterfactual action comparison.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Comparisons between Sep, Sep-MPC, and B-MPC: (a) Kalman filter state estimation error and covariance trace over 10 trials (mean and $95\%$ confidence interval). (b) Action difference ($\ell_2$ norm) versus covariance trace for synthetic belief states. (c) Comparison of counterfactual actions taken by Sep-MPC vs. B-MPC along the same trajectory.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We conclude with numerical comparisons of the performance of controllers based on the separation principle with that of In particular, we consider Sep, which applies the finite-horizon state-feedback policy $u_t=L_t \hat x_{t|t-1}$ (the separation principle policy in [eqn:LQG Policy]), and Sep-MPC which computes the state-feedback gain for the same horizon $H$ as B-MPC. The controller performance is compared on a multi-block double integrator system with $d_x{=}6$, $d_u{=}3$, and $d_y{=}3$, where the scale of $C_0$ is $10^{-2}$. We use $H{=}15$ and approximately solve the B-MPC minimization using L-BFGS. Full experimental details and results are presented in[cao2026dual].

<!-- chunk {"id": "body-0132", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The first observation presented in [cao2026dual] is that B-MPC can achieve cost reductions of close to $40\%$. The improvement is due to a reduction in the state component of the cost, and it comes at the expense of a slightly increased input cost. Figure[fig:kf-rollout] explains the performance difference: B-MPC maintains lower state estimation errors by controlling the size of the posterior covariance $\tr(\Sigma_{t|t-1})$. To understand this difference, we explore how the control inputs differ between the controllers. First, we generate a single trajectory using Sep-MPC to produce a sequence of belief states $(b_t)_{t=0}^{T-1}$ and inputs $(u_t^\texttt{Sep-MPC})_{t=0}^{T-1}$. Then, for each $b_t$, we compute the counterfactual B-MPC control input $u_t^\texttt{B-MPC}$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Figure[fig:input-scatter] shows that B-MPC inputs are spread away from zero, which can be viewed as information-gathering actions. Recalling that $C_0$ is small, near-zero inputs cause the input-dependent measurement matrix $C(u_t)\approx 0$, leading to reduced state estimation accuracy. Finally, we explore reasons for disagreement by sampling synthetic belief states, solving both B-MPC and Sep-MPC, and recording the Euclidean distance between the inputs. Figure[fig:action-gap-synthetic] shows the result. For both systems, the gap between B-MPC and Sep-MPC increases monotonically as $\tr(\Sigma)$ grows. The larger deviation when uncertainty is high aligns with the information-gathering nature of B-MPCactions.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Notes", "weight": 1.0} -->

Bilinear dynamical systems, including those with partial observations, are classical models. However, to our knowledge, the particular BO-LDS model was only recently formulated by [sattar2024learning,liu2025probabilistic] and first studied in the context of system identification. Control of BO-LDS was studied by[choi2025explore], but only for open-loop policies. In this section, we reviewed the results of [sattar2025sub] which establish that the optimal closed-loop controller does not follow the separation principle. It remains an open question how to design controllers which guarantee stability, let alone bounded sub-optimality, for BO-LDS. The preliminary numerical results from the belief space MPC method proposed by [cao2026dual]provide one path forward.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Notes", "weight": 1.0} -->

Belief space planning was coined by in the context of generic partially observed Markov decision processes. In general, it can be intractable except in relatively small discrete settings. Nonetheless, it became a common strategy in robotics to handle practical issues like path planning under perception uncertainties. [platt2010belief] and [van2012motion] formulate belief space planning approximations based on iterative linearization in iLQG. More broadly, optimal control under decision-relevant and reducible uncertainty is studied as dual control, a term introduced by When control inputs have such a dual effect (both regulating and probing), [bar1974dual] show that the separation principle will not hold. [heirung2017dual]present an MPC strategy for dual adaptive control.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Notes", "weight": 1.0} -->

Summary of different control methods for bilinear systems.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Notes", "weight": 1.0} -->

| Control algorithm | System class | Objective | Strengths; Limitations | Summary of different control methods for bilinear systems.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Notes", "weight": 1.0} -->

| Control algorithm | System class | Objective | Strengths; Limitations |

<!-- chunk {"id": "body-0139", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Bilinear dynamical systems of the form [eqn:BDS-FO] represent a central system class in nonlinear control theory. They are the simplest systems in which state and input interact multiplicatively, yet they are expressive enough to approximate broad classes of nonlinear dynamics via Carleman linearization or Koopman-operator lifting[bilinearbook,koopman1931hamiltonian,carleman1932application]. Controlling[eqn:BDS-FO] is fundamentally harder than controlling a linear time-invariant (LTI) system because the effective system matrix $u_t \circ \mathcal{A}$depends on the applied input, so standard pole-placement and LQR design do not apply directly.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Every method presented in this section faces the same challenge: the bilinear term $\sum_{k=1}^{d_u} (u_t)_k A_k x_t$ couples state and input, making the closed-loop system nonlinear even under linear feedback. Two broad families of tractable controller-design methods have emerged in the literature, differing in how they handle this coupling. The first (Section[sec:control-bilinear-LMI-overapprox]) treats the bilinear term as a structured uncertainty appended to a linear nominal model and exploits robust-control tools, most prominently Petersen's lemma and ellipsoidal state bounds, to reduce the design to a semidefinite program (SDP). The second (Section[sec:control-bilinear-SOS]) embraces the polynomial (in fact bilinear) character of the dynamics and searches directly for polynomial Lyapunov functions and rational controllers via sum-of-squares (SOS) optimization, recovering less conservative guarantees at the cost of higher computational effort.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Table[tab:comp\_control]at the end of this section summarizes the trade-offs at a glance, which may be helpful before diving into the details.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Although data collected during learning may be corrupted by process noise (cf.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Part[part:learning]), the controller design focuses on the noise-free part of the dynamics, i.e., the control objective is nominal stabilization of[eqn:BDS-FO] with $w_t = 0$. In particular, we assume that the only uncertainty in the system dynamics arises from the identification error, which is common in the literature on (stochastic) data-driven control; see, e.g.,[vanWaarde2022noisy,martin2023guarantees,faulwasser2023behavioral]and the references therein.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Here, the central challenge is that the identification error of the identified bilinear dynamics must be structurally compatible with the subsequent controller synthesis, i.e., the shape of this error bound matters. In particular, the robust controller designs in Sections[sec:control-bilinear-LMI-overapprox] and[sec:control-bilinear-SOS], which establish end-to-end guarantees for unknown bilinear systems, require the residual $r$ to be bounded by a quadratic expression that vanishes at the origin $(x_t,u_t)=$and grows as the state and input move away from it.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Recall the finite time error bounds from Theorem [thm:main\_BDS\_FO], which readily gives high probability point-wise error bounds, \|\hat{A}_k - A_k\| &\leq \varepsilon_{A_k}, \qquad k=0,...,d_u, \\\|\hat{B} - B\| &\leq \varepsilon_{B}, or ellipsoidal error bounds \begin{bmatrix}\widehat{A_0 + A_i} - (A_0 + A_i)\\ \hat{b}_i - b_i\end{bmatrix} \in \mathcal{E}_{B_i}$$ for $i=1,\ldots,d_u$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

In particular, these bounds ensure that after sufficiently many observations, we may write a single residual identification error bound \begin{bmatrix} x_t \\ u_t\end{bmatrix}^\top \begin{bmatrix} x_t \\ u_t\end{bmatrix}$$ that holds with probability at least $1-\delta$ for a failure probability $\delta > 0$. Here, the positive semidefinite matrix $Q_\Delta$ in constructed as in[chatzikiriakos2026endtoend]. Thus, the learning error bounds of Part[part:learning] on the identification of the true system[eqn:BDS-FO] are structurally compatible with control, i.e., the identification residual $r$ in[eq:residual\_dynamics]satisfies the quadratic bound which will be exploited for the robust controller synthesis.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Control of Bilinear Dynamics", "weight": 1.0} -->

Having established the quadratic bound [eq:residual-quadratic-bound], we now turn to controller synthesis. The next two subsections each propose a different way to handle the bilinear term $\widehat{\mathcal{N}}(I_{d_u}\otimes x_t)u_t$ in[eq:residual\_dynamics]. Section[sec:control-bilinear-LMI-overapprox] overapproximates it as a structured uncertainty and solves an LMI, while Section[sec:control-bilinear-SOS]keeps the polynomial structure intact and uses SOS optimization.

<!-- chunk {"id": "body-0148", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The guiding idea of this subsection is simple. pretend the bilinear coupling is a linear unknown. More precisely, the term $\widehat{\mathcal{N}}(I_{d_u}\otimes x_t)u_t$ is rewritten as $\widehat{\mathcal{N}}\Delta(x_t)u_t$, where $\Delta(x_t)=I_{d_u}\otimes x_t$ is treated as an unknown matrix confined to a bounded set. This converts the nonlinear stabilization problem into a robust-control problem for an uncertain linear system, which can be solved with standard semidefinite programming. The price is additional conservatism, i.e., the LMI is feasible for all bounded $\Delta$, not just those arising from actual state trajectories. Figure[fig:lmi\_diagram] illustrates the overall pipeline.

<!-- chunk {"id": "body-0149", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[\n node distance=0.55cm and 1.1cm,\n box/.style={draw, rounded corners=3pt, minimum width=2.6cm, minimum height=0.85cm, align=center, font=\\small},\n bigbox/.style={draw, dashed, rounded corners=5pt, inner sep=6pt},\n arr/.style={-Stealth, thick},\n label/.style={font=\\scriptsize\\itshape}\n]\n % Row 1: data pipeline\n \\node[box, fill=blue!10] (data) {Data\\\\$\\{x_t,u_t\\}$};\n \\node[box, fill=blue!10, right=of data] (id) {OLS identification\\\\$\\hat A_0,\\hat A_k,\\hat B$};\n \\node[box,

<!-- chunk {"id": "body-0150", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

fill=orange!15, right=of id] (bound) {Quadratic error\\\\bound $Q_\\Delta$};\n % Row 2: design pipeline\n \\node[box, fill=green!12, below=1.15cm of bound,xshift=-1.9cm] (lmi) {SDP / LMI\\\\feasibility};\n \\node[box, fill=green!12, left=of lmi] (lfr) {LFR / uncertainty\\\\overapprox.\\ $\\mathbf\\Delta$};\n \\node[box, fill=red!10, right=of lmi] (ctrl) {Rational\\\\controller $u(x_t)$};\n \\node[box, fill=red!10, left=of lfr] (lyap) {Lyapunov function\\\\$V(x_t)$, ROA};\n % Brace labels\n \\begin{scope}[on background layer]\n

<!-- chunk {"id": "body-0151", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

\\node[bigbox, fit=(lfr)(lmi), fill=green!8, inner sep=5pt] (synth) {};\n \\end{scope}\n % Arrows top row\n \\draw[arr] (data) -- (id);\n \\draw[arr] (id) -- (bound);\n % Arrows from identification/bound into the merged synthesis box\n \\draw[arr] (id.south) -- ($(synth.north west)!0.5!(synth.north east)$);\n \\draw[arr] (bound.south) -- ($(synth.north west)!0.75!(synth.north east)$);\n % Internal arrow inside synthesis box\n \\draw[arr] (lfr) -- (lmi);\n % Arrows out of synthesis box to red boxes\n \\draw[arr] (synth.west) -- (lyap.east);\n \\draw[arr] (synth.east) --

<!-- chunk {"id": "body-0152", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

(ctrl.west);\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Pipeline for the LMI-based controller design.

<!-- chunk {"id": "body-0153", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The collected data are used to identify a nominal bilinear model and derive a quadratic error bound characterized by $Q_\Delta$. The bilinear coupling is then overapproximated as a structured uncertainty $\mathbf{\Delta}$, reducing controller and Lyapunov certificate synthesis to a single SDP.

<!-- chunk {"id": "body-0154", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

To make this precise, we define $\Delta(x_t):= I_{d_u} \otimes x_t \in \mathbb{R}^{d_u d_x \times d_u}$ and write[eq:residual\_dynamics] as $$x_{t+1} = \hat{A}_0 x_t + \widehat{\mathcal{N}} \Delta(x_t) u_t + \hat{B} u_t + r(x_t,u_t).$$ Note that[eq:bil\_compact] represents the original bilinear interaction. In this form, $\Delta(x_t)$ plays the role of an artificial uncertainty. Here, the key observation is that $\Delta(x_t)=I_{d_u}\otimes x_t$ is not an arbitrary matrix, but it is entirely determined by the state $x_t$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

If we know that $x_t$ lies in a pre-specified ellipsoid $\mathcal{X}$, we can characterize $\Delta(x_t)$ exactly, i.e., without additional conservatism, via a suitable multiplier class, recasting the bilinear dynamics as a linear fractional representation (LFR) that is linear in both the state and the uncertainty channel. The identification residual $r$ then enters as a second, separate uncertainty channel in the same LFR, and both are handled simultaneously in one LMI, yielding end-to-end guarantees for the true unknown system. This robust-LFR viewpoint is developed in[strasser2023robust,strasser2023control] for discrete-time bilinear systems and extended to continuous-time systems in[strasser2025koopman]. It builds on the same fundamental objective as earlier LMI-based ROA methods[tarbouriech2009lmi,amato2009stabilization], namely, simultaneous controller synthesis and local ROA certification.

<!-- chunk {"id": "body-0156", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The key difference is that, in these earlier approaches, the analysis is performed directly on the nonlinear closed-loop system induced by a fixed linear state-feedback law, whereas the framework in[strasser2023robust,strasser2023control,strasser2025koopman] recasts the bilinear dynamics as an LFR with structured uncertainty. We note that an LFR is a common representation of uncertain systems[zhou1996robust], which enables the use of modern robust and gain-scheduling synthesis techniques. A controller is then designed that renders the system stable for all uncertainty realizations consistent with $\mathcal{X}$, and a Lyapunov sublevel set $\mathcal{X}_{\mathrm{RoA}} \subseteq \mathcal{X}$is certified as a positively invariant ROA.

<!-- chunk {"id": "body-0157", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

Crucially, the LFR framework is particularly well-suited for incorporating the identification residual $r$ from[eq:residual\_dynamics]. To this end, the nominal bilinear controller design of[strasser2023control] has been extended in[strasser2026safedmd,chatzikiriakos2026endtoend] to account for the learning error of bilinear systems, yielding end-to-end guarantees for the underlying unknown bilinear system. In particular, the residual $r(x_t, u_t)$ enters the LFR[eq:lfr\_bilinear] as an additional input channel, and the quadratic bound[eq:residual-quadratic-bound] is incorporated as a second structured uncertainty block. The LMI synthesis then simultaneously certifies stability against both the state-dependent bilinear coupling and the identification error, leading to a controller that is guaranteed to exponentially stabilize the true(unknown) bilinear system with high probability, not just the estimated one.

<!-- chunk {"id": "body-0158", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

LFR of the bilinear system We define the pre-specified ellipsoidal state region $\mathcal{X}$ via the quadratic inequality \begin{bmatrix} x \\ 1 \end{bmatrix}^\top \begin{bmatrix} Q_x & S_x \\ S_x^\top & R_x \end{bmatrix} \begin{bmatrix} x \\ 1 \end{bmatrix} \geq 0 \right\},$$ where $Q_x \prec 0$ and $R_x \succ 0$. Further, we assume the existence of \tilde{Q}_x & \tilde{S}_x \\ \tilde{S}_x^\top & \tilde{R}_x The simple choice $Q_x = -I$, $S_x = 0$, $R_x = c$ recovers the ball $\|x\|^2 \leq c$.

<!-- chunk {"id": "body-0159", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

Rewriting[eq:bil\_compact] by collecting the auxiliary signal $\zeta_t:= \Delta(x_t) u_t$, one obtains the LFR

<!-- chunk {"id": "body-0160", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

+ \widehat{\mathcal{N}} \zeta_t which is linear in $(x_t, u_t, \zeta_t, r(x_t,u_t))$. Here, in the feedback path appears both the residual $r(x_t,u_t)$ satisfying[eq:residual-quadratic-bound] as well as the artificially introduced state-dependent uncertainty $\Delta(x_t) \in \mathbf{\Delta}\subseteq\mathbb{R}^{d_u d_x \times d_u}$. The set $\mathbf{\Delta}$ characterizes the uncertainty and, due to its link to the state $x_t$ via $\Delta(x_t) = I_{d_u}\otimes x_t$, should be chosen in line with the pre-specified ellipsoidal region $\mathcal{X}$.

<!-- chunk {"id": "body-0161", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The key observation of[strasser2023control] is that the structure $\Delta(x_t) = I_{d_u} \otimes x_t$ with $x_t \in \mathcal{X}$ can be characterized exactly and without conservatism via the multiplier class \Lambda \otimes Q_x & \Lambda \otimes S_x \\\Lambda \otimes S_x^\top & \Lambda \otimes R_x 0 \preceq \Lambda \in \mathbb{R}^{d_u \times d_u} More precisely, $\Delta = I_{d_u} \otimes x_t$ with $x_t \in \mathcal{X}$ if and only if $\begin{bmatrix} \Delta^\top & I \end{bmatrix} \Pi_\Delta \begin{bmatrix} \Delta^\top & I \end{bmatrix}^\top \succeq 0$ for all $\Pi_\Delta \in

<!-- chunk {"id": "body-0162", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

This is an exact (non-conservative) characterization for multi-input systems, reducing to the standard ellipsoidal description $\mathbf{\Delta}=\mathcal{X}$ for scalar inputs ($d_u = 1$).

<!-- chunk {"id": "body-0163", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

Controller design and stability guarantee Substituting a full-information control law parametrized as $u_t = K x_t + K_w w_t$ (which reduces to linear feedback $u_t = Kx_t$ when $K_w = 0$) into[eq:lfr\_bilinear] and applying the multiplier characterization[eq:multiplier] together with a quadratic Lyapunov function $V(x) = x^\top P^{-1} x$, one obtains via the dualization lemma a convex LMI feasibility problem in $(P, L, L_w, \Lambda, \tau)$, where $L:= KP$, $L_w$ encodes $K_w$, and $\tau$ is a multiplier for the S-procedure[boyd1994lmi].

<!-- chunk {"id": "body-0164", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

see[strasser2023control] and[chatzikiriakos2026endtoend] for the precise statement.

<!-- chunk {"id": "body-0165", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The decision variables are $(P, L, L_w, \Lambda)$, with total matrix size $\mathcal{O}((d_x + d_u + d_u d_x)^2)$ variables, and the controller gains are recovered as $K = LP^{-1}$ and $K_w = L_w(\Lambda^{-1} \otimes I_{d_x})$.

<!-- chunk {"id": "body-0166", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

If feasible, the recovered controller &= \left(I - K_w(I_{d_u} \otimes x_t)\right)^{-1} K x_t is a rational function of $x_t$, and asymptotically stabilizes the bilinear system for all $x_0 \in \mathcal{X}_{\mathrm{RoA}}$. Here, $\mathcal{X}_{\mathrm{RoA}}\subseteq \mathcal{X}$ ensures that the uncertainty characterization[eq:multiplier] remains valid along all closed-loop trajectories.

<!-- chunk {"id": "body-0167", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

Positive invariance of $\mathcal{X}_{\mathrm{RoA}}$ follows from the Lyapunov decrease $\Delta V(x_t) < 0$ for all $x_t \in \mathcal{X} \supseteq \mathcal{X}_{\mathrm{RoA}}$, and the volume of $\mathcal{X}_{\mathrm{RoA}}$ is maximized by solving $\max \log\det(P)$ or $\max \mathrm{tr}(P)$subject to the LMI constraints.

<!-- chunk {"id": "body-0168", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The framework extends naturally to quadratic performance (e.g., $\mathcal{L}_2$-gain bounds) by augmenting the LFR[eq:lfr\_bilinear] with a performance channel. Concretely, an exogenous disturbance input $d_t$ and a regulated output $z_t = C_z x_t + D_z u_t + \mathcal{N}_z (I_{d_u}\otimes x_t) u_t$ are introduced as an additional input-output channel in the LFR, alongside the existing uncertainty channels for the bilinear coupling and the identification residual. The quadratic performance condition is then imposed as a further linear constraint in the LMI feasibility problem, following standard robust-control techniques[boyd1994lmi]; see[strasser2023control] for the precise statement and proof.

<!-- chunk {"id": "body-0169", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

The performance channel does not introduce new decision variables, i.e., the same $(P, L, L_w, \Lambda)$ remain, but augments the LMI with additional rows and columns corresponding to the disturbance input and regulated output dimensions, leading to a moderately larger SDP. The result is, for instance, a certified local $\mathcal{L}_2$-gain bound $\|z\|_{\ell_2} \leq \gamma \|d\|_{\ell_2}$ valid for all trajectories starting in $\mathcal{X}_{\mathrm{RoA}}$.

<!-- chunk {"id": "body-0170", "role": "body", "section": "LMI-Based Design via Uncertainty Overapproximation", "weight": 1.0} -->

Summary and limitations. The discussed LFR approach yields a rational state-feedback controller with end-to-end stability guarantees and a certified ellipsoidal ROA, obtained from a single SDP of size $\mathcal{O}((d_x + d_u + d_u d_x)^2)$. The conservatism relative to the true ROA stems from three sources: (i)the bilinear term $\Delta(x_t)u_t$ is treated as an uncertainty ranging over all of $\mathbf{\Delta}$, even though actual trajectories are only a subset of those realizations; (ii)the Lyapunov function is restricted to the quadratic class $V(x)=x^\top P^{-1}x$; and (iii)the ROA must be contained in the pre-specified region $\mathcal{X}$ used to construct the multipliers. All three limitations are addressed by the SOS approach of Section[sec:control-bilinear-SOS], at the cost of a significantly larger SDP.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

The LMI approaches of Section[sec:control-bilinear-LMI-overapprox] achieve tractability by replacing the state-dependent factor $I_{d_u}\otimes x_t$ in the bilinear term with a worst-case bounding uncertainty $\Delta(x_t)\in\mathbf{\Delta}$. However, this over-approximation is conservative: the true state trajectory can only follow paths consistent with the bilinear dynamics, whereas the LMI is feasible for all trajectories of all uncertainty realizations in $\mathbf{\Delta}$, most of which never occur. Sum-of-squares (SOS) optimization offers a different path. Instead of over-approximating the bilinear term, it searches within the class of polynomial Lyapunov functions for a certificate that holds exactly along bilinear trajectories. The bilinear dynamics[eq:residual\_dynamics] is a polynomial system, so a polynomial feedback law yields a polynomial closed-loop, and checking Lyapunov decrease reduces to checking nonnegativity of a polynomial, which is where SOS comes.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

Figure[fig:sos\_diagram]illustrates this pipeline.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

The following subsections introduce the SOS framework, explain why bilinear systems are a particularly natural fit for it, and describe how bilinear controller synthesis can be cast as a single convex program via a rational controller parameterization.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[\n node distance=0.55cm and 1.0cm,\n box/.style={draw, rounded corners=3pt, minimum width=2.8cm, minimum height=0.85cm, align=center, font=\\small},\n bigbox/.style={draw, dashed, rounded corners=5pt, inner sep=6pt},\n arr/.style={-Stealth, thick},\n label/.style={font=\\scriptsize\\itshape}\n] \n % Row 1: data\n \\node[box, fill=blue!10] (data) {Data\\\\$\\{x_t,u_t\\}$};\n \\node[box, fill=blue!10, right=of data] (id) {OLS identification\\\\$\\hat A_0,\\hat A_k,\\hat B$};\n \\node[box,

<!-- chunk {"id": "body-0175", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

fill=orange!15, right=of id] (bound) {Quadratic error\\\\bound $Q_\\Delta$};\n % Row 2: SOS synthesis (merged green box containing two sub-boxes)\n \\node[box, fill=green!12, below=1.15cm of bound,xshift=-1.9cm] (sos) {SOS program\\\\(single SDP)};\n \\node[box, fill=green!12, left=of sos] (poly) {Polynomial\\\\closed-loop $f(x,\\pi)$};\n % Outer red boxes\n \\node[box, fill=red!10, left=1.05 of poly] (lyap) {Lyapunov function\\\\$V(x_t)$, ROA};\n \\node[box, fill=red!10, right=1.05 of sos] (ctrl) {Rational\\\\controller $u(x_t)$};\n % Merged green synthesis

<!-- chunk {"id": "body-0176", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

bigbox (drawn first, on background)\n \\begin{scope}[on background layer]\n \\node[bigbox, fit=(poly)(sos), fill=green!8, inner sep=5pt] (synth) {};\n \\end{scope}\n % Arrows top row\n \\draw[arr] (data) -- (id);\n \\draw[arr] (id) -- (bound);\n % Arrows from identification/bound into the merged synthesis box\n \\draw[arr] (id.south) -- ($(synth.north west)!0.5!(synth.north east)$);\n \\draw[arr] (bound.south) -- ($(synth.north west)!0.75!(synth.north east)$);\n % Internal arrow inside synthesis box\n \\draw[arr] (poly) -- (sos);\n % Arrows out of synthesis box to red boxes\n \\draw[arr] (synth.west) --

<!-- chunk {"id": "body-0177", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

(lyap.east);\n \\draw[arr] (synth.east) -- (ctrl.west);\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Pipeline for the SOS-based controller design.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Sum-of-Squares Optimization Exploiting the Bilinear Structure", "weight": 1.0} -->

The bilinear closed-loop is treated directly as a polynomial system. A single SOS program, formulated using the rational controller parameterizationeq:rational\_K and the quadratic error bound characterized by $Q_\Delta$, simultaneously searches for a polynomial Lyapunov function and the controller, yielding a less conservative ROA than the LMI approach.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

The use of SOS for polynomial Lyapunov functions in nonlinear control was pioneered by Parrilo[parrilo2000structured] and developed into a systematic framework by Prajna, Papachristodoulou, and Parrilo[prajna2002introducing,papachristodoulou2005tutorial]. This tool has found notable success, e.g., systems biology, where nonlinear ODE models of gene regulatory networks are naturally polynomial or admit polynomial approximations. For instance,[el2003model] apply SOS techniques to model validation and robust stability analysis of the bacterial heat shock response, demonstrating that parametric robustness questions in gene regulatory networks can be addressed algorithmically via semidefinite programming. Moreover, using SOS methods, the G-protein signaling cascade in yeast is analyzed in[yi2005application].

<!-- chunk {"id": "body-0180", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

A further application, closer to the setting of the present paper, appear in[prajna2007framework, elsamad2006stochastic], who construct barrier certificates via SOS methods to compute bounds on the probability that a stochastic biological process reaches an unsafe region of the state space in finite time, illustrated on the bacteriophage-$\lambda$genetic switch.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

Because the bilinear dynamics [eq:residual\_dynamics] is polynomial in $(x_t, u_t)$, any polynomial feedback $u_t = \pi(x_t)$ yields a polynomial closed-loop vector field $$f(x, \pi(x)):= \hat{A}_0 x + \sum_{k=1}^{d_u}(\pi(x))_k \hat{A}_k x + \hat{B}\pi(x) + r(x,\pi(x)),$$ making the Lyapunov decrease condition $V(f(x,\pi(x))) - V(x) < 0$ a polynomial inequality in $x$ for any fixed polynomial $V$ and (polynomial) uncertainty bound on $r$.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

With a linear feedback $\pi(x) = Kx$, the closed-loop map[eq:cl\_vector\_field] is degree-2 in $x$, so a degree-4 Lyapunov function $V \in \mathbb{R}[x,4]$ already suffices to certify decrease[tan2006stability]. More generally, for degree-$(2\alpha-1)$ feedback, the Lyapunov degree must be at least $4\alpha$, but the key observation is that the SDP size is determined solely by the degree of the bilinear term and the controller, not by any additional conservatism from an uncertainty overapproximation. We emphasize that the decrease condition and the uncertainty characterization can be combined using the S-procedure[boyd1994lmi] with a polynomial multiplier[tan:2006].

<!-- chunk {"id": "body-0183", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

Rational Controller Parameterization and a single Synthesis SDP The rational controller parameterization of[strasser2025sos] is the key to turning the joint synthesis into a single convex SOS program. The central idea is to write the control law as with a polynomial matrix $L \in \mathbb{R}[x,2\alpha-1]^{d_u \times d_x}$ and a strictly SOS scalar polynomial $\kappa \in \mathrm{SOS}_+[x, 2\alpha]$.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

Substituting[eq:rational\_K] into the closed-loop map[eq:cl\_vector\_field] and multiplying the Lyapunov decrease condition through by $\kappa(x) > 0$ yields a condition that is affine in the decision variables $(P, L, \tau, \rho)$ for a fixed $\kappa$, where $P \succ 0$ encodes the Lyapunov function via $V(x) = x^\top P^{-1} x$, $\tau$ is a polynomial multiplier for the S-procedure, and $\rho$ is a slack variable. This condition takes the form of a polynomial matrix in $x$ required to belong to $-\mathrm{SOS}_+[x, 2\alpha]^{3d_x+d_u}$, i.e., to be strictly negative semidefinite as a polynomial matrix[strasser2025sos]. This leads to a single convex SOS program in $(P, L, \tau, \rho)$ solvable as one SDP.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

In particular, we have an iterative solution strategy, where we fix $\kappa$ and solve for $(P, L, \tau, \rho)$, then iterate, decomposing the problem into a sequence of convex sub-problems[tan2006stability,henrion2005polynomial]. More precisely, the SOS synthesis problem is as follows.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

Find $P \succ 0$, $L \in \mathbb{R}[x,2\alpha-1]^{d_u \times d_x}$, $\tau\in\mathrm{SOS}_+[x,2\alpha]$, $\rho>0$, and a fixed $\kappa \in \mathrm{SOS}_+[x,2\alpha]$ such that & \kappa \hat{A}_0 P + \hat{B} L + \widehat{\mathcal{N}} (L \otimes x) & \begin{bmatrix} \kappa P \\ L \end{bmatrix} is in $\mathrm{SOS}[x,2\alpha]^{3d_x + d_u}$, where we refer to[strasser2025sos] and[chatzikiriakos2026endtoend] for the precise formulation and details.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

The resulting controller $u(x_t)$ in[eq:rational\_K] is a rational function of the state and globally exponentially stabilizes[eq:residual\_dynamics] if the residual error bound holds globally as well. As discussed in[chatzikiriakos2026endtoend], this bound, however, only holds within a compact input set $\mathbb{U}$, i.e., the stability guarantees are valid for all initial conditions $x_0 \in \mathcal{X}_{\mathrm{RoA}}(c):= \{x: x^\top P^{-1} x \leq c\}$ with $c\geq 0$ chosen such that $u(x_t)\in\mathbb{U}$ for all $x\in\mathcal{X}_{\mathrm{RoA}}(c)$.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

Relation to the uncertainty-based LMI design The rational parameterization[eq:rational\_K] is structurally analogous to the gain-scheduling controller[eq:rational\_controller] of Section[sec:control-bilinear-LMI-overapprox]. More precisely, both exploit the bilinear structure to express the control law as a rational function of the state. The key difference is that the uncertainty-based LMI design works with a rational control law with linear polynomials as numerator and denominator, whereas the numerator and denominator of the SOS-controller are polynomials of any chosen degree. Here, the complexity of the LMI design scales better with state dimension, but is typically significantly more conservative due to the over-approximation of the bilinear term. The SOS design, on the other hand, directly exploits the bilinearity to find larger ROA estimates at the cost of a more demanding SDP. We emphasize that a larger polynomial degree enlarges the ROA estimate but increases the computational complexity.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

SOS controller synthesis within model predictive control The approach is further extended to data-driven min-max MPC in[xie2025minmax], where the SOS program minimizes the worst-case cost over all bilinear systems consistent with a set of noisy measurements. In particular, an infinite-horizon min-max optimal control problem is formulated over the set of bilinear systems consistent with the collected data under bounded noise, and the worst-case cost is upper-bounded and minimized using an SOS relaxation of the resulting polynomial program following the same rational controller parameterization of[eq:rational\_K]. The resulting Lyapunov function is obtained directly from the SOS solution, and the scheme is shown to certify robust closed-loop stability and constraint satisfaction for all noise realizations satisfying the assumed bound.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

Summary and limitations The SOS approach produces less conservative stability certificates than the LMI methods because it works directly with the polynomial structure of the closed-loop rather than over-approximating the bilinear term. The rational controller parameterization[eq:rational\_K] is the key that keeps the synthesis convex. In particular, for a fixed $\kappa$, all remaining decision variables enter the SOS condition affinely such that the design is solvable via an SDP. The principal limitation is computational. More precisely, the SDP size grows as $\mathcal{O}(d_x^{2\alpha})$ with state dimension $d_x$ and controller degree $\alpha$, making the approach practical mainly for $d\_x \lesssim 10$$15$ at $\alpha=1$. Additionally, the stability guarantee is global subject to the residual bound holding globally.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Bilinear Systems as Polynomial Systems", "weight": 1.0} -->

If the bound is only valid on a compact input set $\mathbb{U}$, the certified ROA $\mathcal{X}_{\mathrm{RoA}}(c)$must be chosen such that the input constraint is respected for all states in the ROA.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We conclude this section by comparing both design paradigms in a numerical experiment. Here, we consider the two-dimensional bilinear dynamics investigated in[chatzikiriakos2026endtoend]. Data are collected from two independent experiments for inputs $u_t\equiv 0$ and $u_t\equiv 1$, where identification error bounds together with the quadratic residual bound[eq:residual-quadratic-bound] are derived following the procedure of Part[part:learning] with data length $T_0 = T_1 = T$. A key observation from[chatzikiriakos2026endtoend] is the trade-off between data requirements, ROA size, and computational cost across the two design paradigms. For the LMI-based design, feasibility depends on the size of the prescribed region $\mathcal{X}$.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In particular, a small ball $\|x\|_2^2 \leq 0.1$ requires as few as $T = 33$ samples, while certifying a larger region $\|x\|_2^2 \leq 0.9$ demands up to $T = 3999$ samples, with a computation time below $0.01\,\text{s}$ in all cases; see Fig.[fig:exmp-control-bilinear] for the corresponding certified ROAs.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Certified ROAs for the LMI-based design with $\mathcal{X} = \{x \mid \|x\|_2^2 \leq c\}$ for $c \in \{0.1, 0.6, 0.9\}$, using different types of error bounds. Here, we consider individual (eq:error-bound-individual, dashed) and ellipsoidal (eq:error-bound-ellipsoidal, solid) error bounds.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The SOS-based design with $\alpha=1$, which produces a globally stabilizing controller on all of $\mathbb{R}^2$, requires $T = 1040$ samples, at a modest increase in computation time to $0.0135\,\text{s}$, reflecting the higher complexity of the SOS program relative to the LMI. For further numerical studies on the discussed bilinear controller designs and their feasibility and performance we refer to[strasser2023control] and[strasser2025sos].

<!-- chunk {"id": "body-0196", "role": "body", "section": "Notes", "weight": 1.0} -->

Various control approaches for bilinear control have been proposed in the literature[pedrycz1980stabilization,longchamp2003stable,gutman2003stabilizing,derese1980design,benallou1988optimal,lin1994kyp,khlebnikov2018discrete]. Most of them, however, rely on inherently non-convex methods or over-approximate the bilinear term as in the LFR approach of Section[sec:control-bilinear-LMI-overapprox]. An alternative, cheaper over-approximation uses a norm-ball uncertainty rather than the exact ellipsoidal multiplier class[eq:multiplier].

<!-- chunk {"id": "body-0197", "role": "body", "section": "Notes", "weight": 1.0} -->

If the state stays inside an ellipsoid $\mathcal{E}$, $\Delta(x_t)$ is norm-bounded by a known scalar, and Petersen's lemma[petersen1987stabilization,khlebnikov2008petersens,bisoffi2020bilinear] converts the Lyapunov decrease condition into a single LMI via an auxiliary multiplier $\lambda$, reducing the design of a linear gain $u_t=Kx_t$ to a line search over $\lambda$ with a small SDP at each step. This underlies the continuous- and discrete-time designs of[khlebnikov2016quadratic,khlebnikov2018discrete] and its extension to quadratic-bilinear systems[otto2025petersen], and the data-driven matrix-ellipsoidal variant of[bisoffi2022petersen], further extended to setpoint stabilization in[bisoffi2024setpoint].

<!-- chunk {"id": "body-0198", "role": "body", "section": "Notes", "weight": 1.0} -->

While computationally cheaper than the LFR-based design, this approach is more conservative, as the bilinear term is absorbed into a single scalar multiplier rather than the exact, state-dependent characterization[eq:multiplier], and it only applies to the nominal system, i.e., without the identification residual $r$ in[eq:residual\_dynamics]. Incorporating $r$ as a second uncertainty channel would require an additional scalar parameter, with no guarantee of joint feasibility without further rank constraints, where, to our knowledge, this extension remains open. In contrast, the LFR-based approach introduces a dedicated uncertainty channel for $r$ from the outset, accommodating both the bilinear coupling and the identification error simultaneously with end-to-end guarantees[chatzikiriakos2026endtoend].

<!-- chunk {"id": "body-0199", "role": "body", "section": "Notes", "weight": 1.0} -->

Beyond this alternative over-approximation, the two paradigms of Sections [sec:control-bilinear-LMI-overapprox] and[sec:control-bilinear-SOS] are complementary, as summarized in Table[tab:comp\_control].

<!-- chunk {"id": "body-0200", "role": "body", "section": "Notes", "weight": 1.0} -->

Comparison of the two controller-design paradigms for bilinear systems.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Notes", "weight": 1.0} -->

| | LMI (uncertainty overapprox.) | SOS (polynomial Lyapunov) | Comparison of the two controller-design paradigms for bilinear systems.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Notes", "weight": 1.0} -->

| | LMI (uncertainty overapprox.) | SOS (polynomial Lyapunov) | The LFR-based design is preferred when $d_x$ is large or a certified ellipsoidal ROA suffices, while the SOS-based design is preferred when a tighter, less conservative certificate is needed and $d\_x \lesssim 10$$15$ at degree $\alpha=1$ keeps the SDP tractable. The principal bottleneck of the SOS approach is the SDP size, which grows as $\mathcal{O}(d_x^{2\alpha})$. This may be mitigated by exploiting chordal sparsity[zheng2019chordal], low-rank Gram matrix solvers[majumdar2020recent], or first-order SDP solvers[ahmadi2017improving], and, if only a regional rather than global certificate is needed, by invoking Putinar's Positivstellensatz[putinar1993positive]to restrict the Lyapunov decrease condition to a prescribed sublevel set.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Notes", "weight": 1.0} -->

Together, these directions make SOS-based controller synthesis an active research area with growing practical reach beyond small-scale systems.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Notes", "weight": 1.0} -->

Both paradigms of this section account for the quadratic error bound on the identification residual in [eq:residual-quadratic-bound]and thus support end-to-end data-driven controller design with stability guarantees for the underlying bilinear system.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Nonlinear Control based on Koopman Operator Theory and Bilinear Models", "weight": 1.0} -->

The previous part of this tutorial established a complete pipeline for learning and controlling bilinear dynamical systems of the form[eqn:BDS-FO]. A natural question is whether the scope of this pipeline extends beyond bilinear systems to more general nonlinear systems, typically arising in practical applications. The Koopman operator framework provides a compelling answer to this question. It shows that a broad class of nonlinear (control-affine) systems can be lifted to an approximate bilinear representation in a higher-dimensional observable space, so that the entire control machinery developed in the preceding section is generalizable to nonlinear systems. In particular, we consider discrete-time nonlinear systems where $u_t \in \mathbb{R}^{d_u}$ is the control input and $G:\mathbb{X}\to\mathbb{R}^{d_x\times d_u}$ is a state-dependent input matrix. Then, Koopman operator theory allows for the learning and control of (higher-dimensional) bilinear dynamics, representing the nonlinear behavior.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Nonlinear Control based on Koopman Operator Theory and Bilinear Models", "weight": 1.0} -->

To this end, we first introduce linear Koopman theory for discrete-time autonomous systems (Section[sec:koopman-autonomous]). Then, we motivate the transition from linear to bilinear lifted models of controlled systems (Section[sec:koopman-controlled]), and explain how the approximation error incurred by a finite dictionary and finite data fits precisely into the quadratic residual bound[eq:residual-quadratic-bound] (Section[sec:koopman-error]). This enables closing the loop to the LMI and SOS controller designs of Sections[sec:control-bilinear-LMI-overapprox] and[sec:control-bilinear-SOS] (Section[sec:koopman-control]).

<!-- chunk {"id": "body-0207", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

Consider an autonomous discrete-time nonlinear system $$x_{t+1} = F(x_t), \qquad x_t \in \mathbb{X} \subseteq \mathbb{R}^{d_x},$$ with a continuous map $F:\mathbb{X}\to\mathbb{X}$. Rather than tracking the state $x_t$ directly, the Koopman operator $\mathcal{K}_0$ acts on observable functions $\psi:\mathbb{X}\to\mathbb{R}$ via the pull-back $$(\mathcal{K}_0\psi)(x):= \psi(F(x)).$$ In other words, $\mathcal{K}_0$ propagates observables one time step forward along trajectories of[eq:nonlinear-autonomous]. While $F$ is nonlinear, $\mathcal{K}_0$ is a linear operator.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

However, the price for this linearity is that $\mathcal{K}_0$ acts on an infinite-dimensional function space, i.e., the Koopman operator is linear but infinite dimensional.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

Koopman-invariant subspaces and finite representations If there exists a finite set of observables $\psi_1,\ldots,\psi_N:\mathbb{X}\to\mathbb{R}$ whose span is Koopman-invariant, i.e., $\mathcal{K}_0\psi_i \in \mathrm{span}\{\psi_1,\ldots,\psi_N\}$ for all $i$, then the dynamics on that subspace can be represented exactly by a finite-dimensional linear system.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

Defining the lifted state $\Psi(x):= \begin{bmatrix}\psi_1(x) & \cdots & \psi_N(x)\end{bmatrix}^\top \in \mathbb{R}^N$, the lifted dynamics reads $$\Psi(x_{t+1}) = \mathcal{K}_0\Psi(x_t) = K \Psi(x_t),$$ where $K \in \mathbb{R}^{N\times N}$ is the finite matrix representing $\mathcal{K}_0$ on the chosen subspace. This is the key insight of Koopman theory: nonlinear dynamics becomes linear in the lifted coordinates, provided a Koopman-invariant subspace is found.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

Finite-dimensional approximation via EDMD In practice, a Koopman-invariant subspace is rarely available in closed form. Instead, one chooses a dictionary $\mathbb{V} = \mathrm{span}\{\psi_1,\ldots,\psi_N\}$ of $N$ basis observables (e.g., polynomials, radial basis functions, or neural-network features), and computes the best linear approximation of $\mathcal{K}_0$ on $\mathbb{V}$ from data $\{(x_t, x_{t+1})\}_{t=1}^T$. To this end, a common approximation technique is extended dynamic mode decomposition (EDMD,[williams2015edmd]).

<!-- chunk {"id": "body-0212", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

This boils down to the OLS problem = \underset{K \in \mathbb{R}^{N\times N}}{\arg\min} \sum_{t=1}^{T}\bigl\|\Psi(x_{t+1}) - K\Psi(x_t)\bigr\|^2.$$ The resulting estimator $\hat{A}_0$ yields a purely data-driven linear surrogate $\Psi_{t+1} \approx \hat{A}_0 \Psi_t$, which can be used for the prediction of the underlying nonlinear system. $\mathbb{V}$ happens to be Koopman-invariant, the projection step introduces a residual $r_\Psi$. This residual error quantifies how well $\mathbb{V}$ approximates an invariant subspace and consists of both learning and projection errors.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Koopman Operator for Autonomous Discrete-Time Systems", "weight": 1.0} -->

Crucially, the residual depends on the state $x_t$ through the nonlinear map $F$, and for a sufficiently rich dictionary one can show that $\|r_\Psi(x_t)\|^2 \leq c_x\|\Psi(x_t)\|^2$ for some constant $c_x \geq 0$ that decreases as the dictionary is enriched; see, e.g.,[nuske2023finite,philipp2024error,strasser2026overview].

<!-- chunk {"id": "body-0214", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

We now extend the Koopman framework to control-affine nonlinear systems of the form[eq:control-affine]. Lifting the nonlinear dynamics using the dictionary $\Psi$ yields

<!-- chunk {"id": "body-0215", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

+ \sum_{k=1}^{d_u}(u_t)_k \bigl[\Psi\bigl(F(x_t) + (G(x_t))_k\bigr) - \Psi(F(x_t))\bigr] where $(G(x_t))_k$ denotes the $k$-th column of $G(x_t)$. Two natural choices of surrogate model arise from how one approximates the input-dependent terms.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

Linear EDMDc and its limitations The simplest approximation, proposed in[brunton2016koopman,korda2018mpc], linearizes the input dependence and approximates $$\Psi(x_{t+1}) \approx \hat{A}_0 \Psi(x_t) + \hat{B}_u u_t,$$ for some constant matrix $\hat{B}_u \in \mathbb{R}^{N\times d_u}$. This linear EDMDc model is computationally attractive and can be identified via OLS. However, for control-affine systems the input appears through $G(x_t)$, a state-dependent factor, so the effective lifted input map is not constant. In particular, the linear model[eq:edmdc] absorbs the state dependence into a constant $\hat{B}_u$, introducing a systematic error that grows with the strength of the nonlinear input coupling. More fundamentally, it can be shown that linear surrogate models do not, in general, admit finite-dimensional exact representations for control-affine nonlinear systems.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

Hence, the associated identification error cannot be made small by increasing the dictionary alone[bruder2021bilinear,brunton2022koopman,strasser2026overview].

<!-- chunk {"id": "body-0218", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

Bilinear Koopman models are necessary The bilinear structure of the lifted model is not an artifact of the chosen approximation scheme, but is instead grounded in the mathematical structure of the Koopman framework itself. In particular, the Koopman generator preserves control-affinity exactly[surana2016koopman], i.e., it is affine in the control input $u$. This Koopman generator acts on $\Psi$ via the Lie derivative corresponding to the continuous-time counterpart of[eq:control-affine]. In particular, the drift term $\mathcal{L}_F \psi$ is input-independent, and each control channel contributes an additive term $u_k \mathcal{L}_{G_k}\psi$ that is linear in $u_k$. Defining $z_t=\Psi(x_t)$, the resulting lifted control-affine representation is thus a bilinear dynamics. This observation motivates the bilinear lifted model as the natural finite-dimensional surrogate also in discrete time.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

In discrete time, the Koopman operator of the controlled system,:= \Psi\bigl(F(x) + G(x)u\bigr),$$ is generally nonlinear in $u$ through the composition $\Psi \circ (F(\cdot) + G(\cdot)u)$. The bilinear structure emerges only as an approximation[peitz2020data,philipp2025error]. Further,[goswami2017bilinear,surana2016koopman] show that this approximation becomes exactwhen the dictionary spans a Koopman-invariant subspace, i.e., the bilinear model is the minimal exact finite-dimensional representation.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

Approximating the Koopman operator via an EDMD-type regression gives the bilinear Koopman surrogate

<!-- chunk {"id": "body-0221", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

+ \sum_{k=1}^{d_u}(u_t)_k \hat{A}_k \Psi(x_t),$$ where $\hat{A}_0$, $\hat{A}_1$ $\hat{A}_{d_u}$ and $\hat{B}$ approximate variants of the Koopman operator, resulting in a decoupled-experiment OLS procedure for different constant control inputs; compare[chatzikiriakos2026endtoend, This is precisely a bilinear dynamical system of the form[eqn:BDS-FO] in the lifted state $z_t:= \Psi(x_t) \in \mathbb{R}^N$. The matrices $\hat{A}_0$, $\hat{A}_1$ $\hat{A}_{d_u}$ and $\hat{B}$ play the same role as in the bilinear identification problem and can be estimated from data.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

The bilinear structure[eq:bilinear-koopman] is thus not merely a modeling convenience, but it is the structure inherited from the control-affine form of the dynamics, exact at the level of the Koopman generator and recovered approximately at the level of the Koopman operator. Thus, bilinear Koopman models are not only more flexible than linear ones but are the minimal structure that captures the control-affine nonlinearity without additional conservatism[iacob2024koopman].

<!-- chunk {"id": "body-0223", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

For the special case $F(x) = A_0 x$ and $G(x) = B$ (i.e., an LTI system), any dictionary $\Psi$ that includes the identity ($\psi_k(x) = x_k$) as observables recovers an exact linear representation with $\hat{A}_k = 0$ for $k \geq 1$ and $\hat{B} = B$. In particular, LTI systems are a degenerate special case of the bilinear Koopman surrogate[eq:bilinear-koopman] without bilinear coupling terms. Any richer nonlinear control-affine system requires the bilinear terms $(u_t)_k\hat{A}_k z_t$ for a finite-dimensional representation, which underscores why the bilinear setting is the right level of generality for Koopman-based control.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Koopman for Controlled Systems: Why Bilinear?", "weight": 1.0} -->

We emphasize that the state-independent control matrix $\hat{B}$ is crucial for the expressiveness of the approximation, i.e., a linear system could not be represented by[eq:bilinear-koopman] without this term.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Approximation Error as a Quadratic Residual Bound", "weight": 1.0} -->

The bilinear surrogate[eq:bilinear-koopman] is generally an approximation, not an exact representation, due to the use of a finite dictionary and finite data for learning. Writing $z_t = \Psi(x_t)$ and collecting the approximation error, the true lifted dynamics satisfy = \hat{A}_0 z_t + \sum_{k=1}^{d_u}(u_t)_k \hat{A}_k z_t + \hat{B} u_t where the Koopman residual

<!-- chunk {"id": "body-0226", "role": "body", "section": "Approximation Error as a Quadratic Residual Bound", "weight": 1.0} -->

- \hat{A}_0 z_t - \sum_{k}(u_t)_k\hat{A}_k z_t - \hat{B}u_t$$ captures the combined effect of finite-dictionary closure error and learning error. Equation[eq:koopman-bilinear-residual] is of the same form as[eq:residual\_dynamics], so the bilinear control framework applies directly once a suitable bound on $r_\Psi$ is available.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Approximation Error as a Quadratic Residual Bound", "weight": 1.0} -->

Quadratic bound on the Koopman residual Under standard regularity assumptions on $F$, $G$, and the dictionary $\Psi$ as well as appropriate data collection during learning, the Koopman residual satisfies a proportional (quadratic) bound of the form $$r_\Psi(z_t, u_t)^\top r_\Psi(z_t, u_t) \begin{bmatrix}z_t \\ u_t\end{bmatrix}^\top \begin{bmatrix}z_t \\ u_t\end{bmatrix},$$ for a positive semidefinite matrix $Q_\Psi \succeq 0$; see[strasser2025kernel,strasser2025koopman,strasser2026safedmd,strasser2026overview] for precise statements and conditions. More precisely, $Q_\Psi$ can be bounded from data using results from linear and bilinear system identification.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Approximation Error as a Quadratic Residual Bound", "weight": 1.0} -->

Here, the identification residual from a specific EDMD variant, i.e., an OLS regression, for the bilinear lifted model satisfies the quadratic bound with $Q_\Psi$ taking the same role as $Q_\Delta$ in[eq:residual-quadratic-bound]. Further, preliminary results of[chatzikiriakos2026endtoend] indicate that finite-sample guarantees for bilinear systems carry over to the lifted system.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Approximation Error as a Quadratic Residual Bound", "weight": 1.0} -->

Three key features make the bound[eq:koopman-quadratic-bound] compatible with the controller designs of Sections[sec:control-bilinear-LMI-overapprox] and[sec:control-bilinear-SOS]. First, $r_\Psi = 0$, so the bound is tight at the origin. Second, the bound grows quadratically away from the origin, which matches the structure required by both the LMI S-procedure and the SOS optimization using robust control techniques. Third, $Q_\Psi$ can be evaluated, and the residual error decreases in the infinite-data limit and infinite dictionary $\Psi$ (or if the dictionary is Koopman-invariant). In the limit of an exact Koopman-invariant dictionary and infinite data, $Q_\Psi \to 0$ and the bilinear surrogate becomes exact, so the controller designed for the lifted system recovers a true stabilizer for the nonlinear system without any residual conservatism. The quadratic bound therefore not only enables rigorous guarantees for finite dictionaries, but also makes the framework asymptotically exact.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Approximation Error as a Quadratic Residual Bound", "weight": 1.0} -->

A richer dictionary (larger $N$) reduces the closure error and, hence, tightens $Q_\Psi$, yielding less conservative stability certificates. However, a larger dictionary increases the state dimension $N$ of the lifted bilinear model, which affects the complexity of the SDP associated with the controller design problem. The size of the LMI design scales as $\mathcal{O}(N^3)$ and the SOS design as $\mathcal{O}(N^{2\alpha})$. Practitioners therefore face a trade-off between model fidelity (larger $N$, smaller $Q_\Psi$) and computational tractability. For control applications, the LMI approach of Section[sec:control-bilinear-LMI-overapprox] typically scales better to large dictionaries, while SOS methods are preferable when a tight ROA certificate is needed with a moderate dictionary.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

Combining the elements above, Figure[fig:koopman\_pipeline] summarizes the end-to-end pipeline for data-driven control of a nonlinear control-affine system[eq:control-affine] using the bilinear Koopman surrogate and the controller designs of Section[sec:control-bilinear-systems].

<!-- chunk {"id": "body-0232", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[\n node distance=0.55cm and 1.1cm,\n box/.style={draw, rounded corners=3pt, minimum width=2.6cm, minimum height=0.85cm,\n align=center, font=\\small},\n bigbox/.style={draw, dashed, rounded corners=5pt, inner sep=6pt},\n arr/.style={-Stealth, thick}\n]\n % Row 1: data pipeline\n \\node[box, fill=blue!10] (data) {Data\\\\$\\{x_t, u_t\\}$};\n \\node[box, fill=blue!10, right=of data] (lift) {Dictionary\\\\$z_t = \\Psi(x_t)$};\n \\node[box, fill=blue!10, right=of lift] (id) {Bilinear

<!-- chunk {"id": "body-0233", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

EDMD\\\\$\\hat{A}_0,\\hat{A}_k,\\hat{B}$};\n \\node[box, fill=orange!15,right=of id] (bound) {Koopman error\\\\bound $Q_\\Psi$};\n % Row 2: design\n \\node[box, fill=green!12, below=1.15cm of id] (design) {LMI or SOS\\\\synthesis};\n \\node[box, fill=red!10, right=of design] (ctrl) {Controller\\\\$u(x_t)$};\n \\node[box, fill=red!10, left=of design] (cert) {Lyapunov function\\\\$V(x_t)$, ROA};\n % Arrows\n \\draw[arr] (data) -- (lift);\n \\draw[arr] (lift) -- (id);\n

<!-- chunk {"id": "body-0234", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

\\draw[arr] (id) -- (bound);\n \\draw[arr] (id) -- (design);\n \\draw[arr] (bound) -- (design);\n \\draw[arr] (design)-- (ctrl);\n \\draw[arr] (design)-- (cert);\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> End-to-end pipeline for data-driven control of nonlinear systems via Koopman bilinear surrogates.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

Measured data are first lifted through a dictionary to form a bilinear EDMD model. The Koopman approximation error is quantified as a quadratic bound $Q_\Psi$, and the LMI or SOS controller-design methods of Sectionssec:control-bilinear-LMI-overapprox andsec:control-bilinear-SOS are applied directly to the lifted bilinear system.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

Identification of the bilinear lifted model Given $T$ trajectory samples $\{(x_t, u_t, x_{t+1})\}_{t=1}^T$ from the nonlinear system[eq:control-affine], one first evaluates the dictionary to obtain the lifted data $\{(z_t, u_t, z_{t+1})\}$ with $z_t:= \Psi(x_t)$. The decoupled-experiment identification strategy of[chatzikiriakos2026endtoend] then applies directly to the lifted data, yielding OLS estimates $\hat{A}_0,\hat{A}_1,\ldots,\hat{A}_{d_u},\hat{B}$ together with a quadratic error characterization for the lifted bilinear system (cf.[strasser2026safedmd]). This provides all the ingredients required by the bilinear controller designs in Section[sec:control-bilinear-systems].

<!-- chunk {"id": "body-0237", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

LMI-based stabilization with Koopman surrogates The LFR-based controller design of Section[sec:control-bilinear-LMI-overapprox] applies directly to the lifted bilinear system with lifted state dimension $N$ in place of $d_x$ and lifted bilinear matrices $\hat{A}_k$ acting on $z_t = \Psi(x_t)$ rather than $x_t$. The result is a nonlinear controller with rational structure, i.e., $u_\Psi(x_t) = u(\Psi(x_t))$. This controller asymptotically stabilizes the bilinear surrogate[eq:koopman-bilinear-residual] and, under the quadratic bound $Q_\Psi$, provably stabilizes the true nonlinear system[eq:control-affine] for all $x_0$ whose lifted image lies in the certified ROA $\mathcal{X}_{\mathrm{RoA}} \subseteq \mathbb{R}^N$.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

This approach is developed in[strasser2023robust,strasser2025koopman,strasser2026safedmd], where it is referred to as SafEDMD, and provides the first data-driven controller with rigorous stability guarantees for discrete-time nonlinear systems via Koopman surrogates.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

SOS-based stabilization with Koopman surrogates The LMI approach relies on overapproximating the bilinearity, which can, especially in the context of Koopman lifted bilinear systems, introduce severe conservatism (compare[strasser2025koopman]). Instead, the SOS-based design framework of Section[sec:control-bilinear-SOS] applies directly in the lifted coordinates, and the resulting stability certificates can be pulled back to the original state space via a suitable characterization of the Lyapunov function; see[strasser2025sos,strasser2025performance] for details. Compared with the LMI approach, the SOS method yields, as for the bilinear setting, larger ROA estimates in the lifted space at the cost of a higher-dimensional SDP (growing as $\mathcal{O}(N^{2\alpha})$ in the dictionary size $N$ and controller degree $\alpha$), so it is best suited to moderate-size dictionaries.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

Closed-loop guarantees for the nonlinear system A subtlety that arises in the Koopman setting is the relationship between closed-loop guarantees of the lifted bilinear model and closed-loop guarantees of the original nonlinear system. The key quantity is the Lyapunov function used for proving the closed-loop guarantees. In particular, it is crucial to directly construct the Lyapunov function and its decrease inequality in the original state $x_t$. One possibility to get such a construction is by including the identity ($\psi_k(x) = x_k$ for $k = 1,\ldots,d_x$) as observables in $\Psi$. Then, the original state $x_t$ is a linear projection of the lifted state $z_t=\Psi(x_t)$, and closed-loop stability of the original system[strasser2026safedmd,strasser2025koopman,chatzikiriakos2026endtoend] can be deduced by robust stability of the lifted perturbed bilinear system.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Data-Driven Control of Nonlinear Systems via Koopman Bilinear Surrogates", "weight": 1.0} -->

More precisely, the certified ROA $\mathcal{X}_{\mathrm{RoA}}$ is directly expressed in the original state space as a sublevel set of the (nonlinear) Lyapunov function $V(x)=\Psi(x)^\top P \Psi(x)$.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We conclude this section with a numerical illustration of the Koopman-based control pipeline on a nonlinear inverted pendulum lifted to a bilinear surrogate via the dictionary $\Psi(x) = \begin{bmatrix} x_1 & x_2 & \sin(x_1)\end{bmatrix}^\top$. Data are collected for $T = 2000$ under sub-Gaussian noise, yielding a lifted bilinear model of dimension $N = 3$ together with the quadratic residual bound[eq:koopman-quadratic-bound]. Applying the SOS-based controller of Section[sec:control-bilinear-SOS] with $\alpha=1$ yields a stabilizing rational controller (compare[chatzikiriakos2026endtoend]).

<!-- chunk {"id": "body-0243", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

The advantage of exploiting the bilinear structure via SOS rather than overapproximating it via the LMI is particularly pronounced in the Koopman setting, where the nonlinear lifting causes the true trajectories to occupy only a small subset of the artificial uncertainty set $\mathbf{\Delta}$, so that the LMI overapproximation introduces severe conservatism. As illustrated in Fig.[fig:exmp-control-nonlinear][strasser2025sos], the SOS-based design yields a ROA with a high coverage of the sampling region. In contrast, the LMI-based approach requires significantly more data samples to achieve feasibility and still yields a substantially smaller ROA.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Sampling region (thick) and guaranteed ROAs of the SOS-based controller design (dashed).

<!-- chunk {"id": "body-0245", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

For further numerical examples on Koopman-based control of nonlinear systems using bilinear surrogates, we refer to the survey article[strasser2026overview] and the references therein.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Notes", "weight": 1.0} -->

- Any control-affine nonlinear system[eq:control-affine] can be lifted to a bilinear system[eq:bilinear-koopman] in observable coordinates. Moreover, bilinear models are the minimal exact finite-dimensional Koopman representation, and, in particular, linear surrogates are insufficient for representing controlled systems. - The finite-dictionary and finite-data approximation error fits exactly the quadratic bound[eq:koopman-quadratic-bound] required by the bilinear controller designs, with the matrix $Q_\Psi$ playing the same role as $Q_\Delta$ in the bilinear identification setting. - As a result, the complete pipeline of Part[part:learning] (OLS identification with finite-sample error bounds) and the bilinear controller designs of Section[sec:control-bilinear-systems] apply to nonlinear systems, simply replacing the bilinear state $x_t$ by the lifted state $z_t = \Psi(x_t)$.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Notes", "weight": 1.0} -->

This generalizes the bilinear theory discussed in this tutorial paper to a broad class of nonlinear systems, establishing bilinear system identification and control as core primitives in data-driven nonlinear control via the Koopman operator.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Notes", "weight": 1.0} -->

While Koopman-based control based on robust bilinear controller designs are shown to be useful to derive closed-loop guarantees for data-driven control of nonlinear systems, several other Koopman-based controller design approaches exist. The approach in[sinha2022data] uses Petersen's lemma for a nominal bilinear controller design but, since it does not account for the residual, provides no closed-loop guarantees. The work in[moyalan2023data,vaidya2025koopman] instead formulates data-driven optimal and stabilizing control via the Perron-Frobenius operator, dual to the Koopman operator and acting on densities rather than observables, yielding a convex (occupation-measure, density-function, or Hamilton-Jacobi based) reformulation solved via linear or SOS programming. However, it does not explicitly account for the surrogate's learning error and hence lacks the end-to-end guarantees of the approaches in Section[sec:koopman-control].

<!-- chunk {"id": "body-0249", "role": "body", "section": "Notes", "weight": 1.0} -->

A complementary direction combines a Koopman-based LPV surrogate with a data-driven integral quadratic constraint (IQC) characterization of the modeling error in the frequency domain, iteratively refining the IQC multiplier and the controller[eyuboglu2026koopman]. This is reported to be less conservative on selected examples, but currently only yields asymptotic, rather than finite-sample, guarantees.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Notes", "weight": 1.0} -->

Open questions in the realm of Koopman-based control include (i) better tractability of the controller designs discussed in Section [sec:koopman-control] as the lifted dimension $N$ grows; (ii) a systematic comparison with the set-membership approach of[xie2026koopman] and with control from partial observations[iacob2025learning,strasser2026inputoutput]; (iii) combining finite-sample residual bounds with multi-step (rather than one-step) identification schemes[eyuboglu2025efficient], which report improved long-horizon prediction and closed-loop performance over EDMD; and (iv) extending the IQC-based characterization of[eyuboglu2026koopman]to finite-sample guarantees.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Notes", "weight": 1.0} -->

The tools developed in this tutorial (non-asymptotic system identification, belief-space and robust control, and Koopman-lifted bilinear surrogates) connect to a much larger landscape of modern data-driven and learning-based control and reinforcement learning. In Part III, we highlight several connections to these broader themes and discuss open directions. We emphasize that this is not an exhaustive account of the connections between bilinear control and modern machine learning, but we present it as one path forward among several. We expect the boundary between non-asymptotic control theory and ML-driven control to continue to blur.

<!-- chunk {"id": "body-0252", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

In this section, we briefly explore approaches that address learning and control of a dynamical system simultaneously. One class of end-to-end approaches builds directly on the separate learning and control stages. model-based by the machine learning community or indirect by the adaptive control community, these approaches update model estimates online and then recompute control policies based on them. By carefully designing inputs that both regulate and excite the system, such techniques can be shown to have decaying time-average sub-optimality, a metric referred to as regret. Regret guarantees have been established mainly in the setting of linear dynamics, including under state[dean2018regret] and partial observation[mania2019certainty,lale2020logarithmic], but also more broadly for Markov jump linear systems[du2021certainty] and linear time-varying systems[minasyan2021online]. Establishing such methods and guarantees remains an open question for bilinear dynamical systems.

<!-- chunk {"id": "body-0253", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

Another approach whose analysis for continuous control problems (LQR, LQG, robust control, etc.) has gained attention in recent years, in part due to its empirical success in reinforcement learning (RL), is based on gradient-based techniques known as policy optimization methods. This type of approach is distinct from putting together separate learning and control stages (i.e., first learn the dynamics and then design the control); instead, the policy (or the control law, mapping states to actions) is directly updated using exact or approximate estimates of the cost gradient (see, e.g., [aagarwal2021policygradient] and references therein). Here we focus on the statistical and computational analysis of these methods (which is the theme of this tutorial) applied to control problems with continuous states and actions[hu2023toward]. There has been much recent progress on this front for a variety of control problems under linear dynamics.

<!-- chunk {"id": "body-0254", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

For the LQR problem, [fazel2018global] showed that direct policy optimization converges to the optimal policy starting from any stabilizing policydespite nonconvexity, the loss landscape satisfies the gradient dominance property (a special case of the Polyak-Lojasiewicz property). The article [hu2023toward] surveys recently developed theoretical results on the optimization landscape, global convergence, and sample complexity of policy optimization for a variety of (linear) continuous control problems, such as the LQR, risk-sensitive, state-feedback $\mathcal{H}_\infty$, and LQG control. More recent work includes policy optimization for the output estimation problem [umenberger2022policysearch].

<!-- chunk {"id": "body-0255", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

However, the analysis tools for linear dynamics do not readily extend to the nonlinear case, including bilinear systems. Yet, the practical deep RL algorithms that motivate this line of work (policy gradient, natural policy gradient, and actor-critic methods such as TRPO [schulman2015trust], PPO[schulman2017proximal], and SAC[haarnoja2018soft]) are routinely applied to genuinely nonlinear and often partially observed systems, typically without any comparable guarantee. [agarwal2022reinforcement] give a comprehensive statistical and computational treatment of policy optimization, exploration, and function approximation for general Markov decision processes (MDPs) underlying much of this practice, of which the LQR, LQG, $\mathcal{H}_\infty$and risk-sensitive control results mentioned above are particularly clean and analytically tractable cases studied in control.

<!-- chunk {"id": "body-0256", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

Representation learning for low-rank and linear MDPs poses a similar question to the dictionary learning problem for the Koopman operator in Section[sec:koopman]: when, and how efficiently, a feature map can be learned under which the relevant dynamics become linear. [agarwal2020flambe] give a statistically and computationally efficient algorithm (FLAMBE) for representation learning in low-rank MDPs with finite-sample guarantees, in a similar spirit to the finite-sample bounds for the bilinear dictionary of Part[part:learning]. Further, [uehara2022representation] extend this to oracle-efficient algorithms in both the online and offline settings, and [zhang2022making] show how to make such representations practical at scale via contrastive objectives. Finally, the Koopman operator has itself been imported directly into RL.

<!-- chunk {"id": "body-0257", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

For instance, [rozwood2024koopman] lift the Bellman equation into Koopman coordinates so that the value function evolves linearly in the lifted space, a direct structural echo of the belief-space reformulation of Section[sec:koopman-control], now applied to the value function rather than to the state. We discuss further connections between Koopman theory and modern machine learning in Section[sec:connections-modern-ml].

<!-- chunk {"id": "body-0258", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

Developing end-to-end learning and control and guarantees for bilinear dynamical systems requires addressing several open questions. On the learning side, it is necessary to derive results for closed-loop inputs, rather than the i.i.d. noise injection considered in Section[sec:sysid]. Closed-loop inputs introduce additional dependence between covariates over time, and without sufficient noise injection, may even fail to guarantee persistence of excitation. It may also be necessary to consider learning from unstable or marginally stable systems. On the control side, it is necessary to develop methods that work in the presence of process noise, measurement noise, partial observation, and modeling errors. Furthermore, it is necessary to derive guarantees on closed-loop behavior like stability and sub-optimality. One possible starting point is to consider model-based learning of the separation principle controller for LQG-BO (Section [subsec:sp]) and analyze the sub-optimality with respect to the oracle separation principle controller. Another possible direction is to study online model-based stabilization of unknown bilinear dynamics using the tools from Section [sec:control-bilinear-systems].

<!-- chunk {"id": "body-0259", "role": "body", "section": "End-to-End Learning and Control and Reinforcement Learning", "weight": 1.0} -->

The success of policy optimization methods in practice and their analytical guarantees for linear dynamical systems brings up the question of whether problems in bilinear systems can be addressed similarly. Even with full observations, loss landscape analysis for the learning and control of a BDS is more complicated than the linear case, and strong properties such as gradient dominance or only-strict-saddles likely do not hold without additional assumptions. Perhaps a starting point is to consider learning a separation-principle controller for LQG-BO (Section [subsec:sp]) via policy optimization, given a cost-gradient oracle. More broadly, this topic is an interesting direction for future research.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Further Connections to Machine Learning", "weight": 1.0} -->

In this section, we highlight three connections that are especially pertinent to the material of Sections [sec:sysid][sec:koopman]: nonparametric and kernel-based learning as an alternative to the parametric identification of Part[part:learning]; representation learning in the age of foundation models, viewed through the Koopman lens of Section[sec:koopman]; and world models and predictive architectures, whose guiding philosophy, i.e., to predict in a learned representation rather than in the raw state, closely parallels the Koopman approach.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Nonparametric and Kernel-Based Learning: RKHS and Gaussian Processes", "weight": 1.0} -->

[part:learning], we identified the bilinear and Koopman-lifted dynamics via parametric least-squares regression: the dictionary $\Psi$ (or the bilinear factors $A_0,\ldots,A_{d_u}$) is fixed ahead of time, and only finitely many coefficients are estimated from data. An alternative, nonparametric route is to place a prior directly on the unknown dynamics via a reproducing kernel Hilbert space (RKHS) or a Gaussian process (GP), letting the effective dictionary grow with the data rather than being fixed in advance. This is attractive precisely where the finite-dictionary and finite-data approximation error of Section[sec:koopman-error] is a concern. More precisely, a well-specified kernel can, in principle, drive the Koopman residual bound $Q_\Psi$ in[eq:koopman-quadratic-bound] to zero as data accumulate, without committing to a particular finite basis.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Nonparametric and Kernel-Based Learning: RKHS and Gaussian Processes", "weight": 1.0} -->

[bonalli2026non] give a representative example outside the Koopman setting, establishing non-asymptotic rates for RKHS-based nonparametric identification of the drift and diffusion of a stochastic differential equation, with rates that tighten as the unknown coefficients become smoother. Within the Koopman setting specifically, [kostic2022learning] lay the statistical foundations, casting Koopman operator estimation as a regression problem restricted to an RKHS and introducing a notion of risk from which several estimators, together with guarantees on the estimated spectral decomposition, follow. [bevanda2026nonparametric] extend this approach to control-affine systems, developing an RKHS-based representation for control-Koopman operators that dispenses with an explicit finite dictionary or input parametrization altogether, casting operator estimation as an infinite-dimensional regression problem in a control-affine RKHS.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Nonparametric and Kernel-Based Learning: RKHS and Gaussian Processes", "weight": 1.0} -->

Their framework yields arbitrarily accurate finite-rank approximations without a priori restricting the hypothesis space to a fixed finite span (directly addressing the finite-dictionary approximation error that motivates the residual bound $Q_\Psi$ in Section[sec:koopman-error]) and uses sketching to keep the resulting estimators scalable, extending the classical (linear) kernel-EDMD line of work[williams2015kernelEDMD] to the control setting with an explicit approximation-error analysis. Two further papers connect this line of work directly back to the controller designs of Section[sec:control-bilinear-systems]: [strasser2025kernel] derive kernel-based error bounds for bilinear Koopman surrogate models of exactly the form used throughout Section[sec:koopman], giving a kernel-based route to the quadratic bound $Q_\Psi$ in[eq:koopman-quadratic-bound], and [bold2025kernel] give a complementary error and stability analysis for kernel-based Koopman approximants for control under flexible, non-i.i.d. sampling schemes.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Nonparametric and Kernel-Based Learning: RKHS and Gaussian Processes", "weight": 1.0} -->

Gaussian processes offer a Bayesian counterpart to the same RKHS-based idea, replacing worst-case (frequentist) error bounds with a calibrated posterior over the unknown dynamics. This is already a mature tool for nonlinear control. [berkenkamp2017safe] combine GP regression of unmodeled dynamics with Lyapunov-based stability certificates in a model-based RL loop, and a substantial body of follow-up work builds GP-based model predictive control with probabilistic safety and stability guarantees[koller2018learning,maiworm2021online]. Conceptually, a GP posterior variance plays a role analogous to the ellipsoidal or quadratic identification-error bounds of Section[sec:control-bilinear-systems], but is data-adaptive (shrinking where data is dense) rather than a fixed worst-case set.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Nonparametric and Kernel-Based Learning: RKHS and Gaussian Processes", "weight": 1.0} -->

It remains open how to combine a GP or RKHS uncertainty quantification directly with the LMI or SOS controller synthesis of Section[sec:control-bilinear-systems], replacing the quadratic residual bound $Q_\Delta$ (or $Q_\Psi$) with a state-dependent, data-adaptive counterpart derived from the posterior covariance, while retaining a convex synthesis problem.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Representation Learning, Foundation Models, and Koopman Embeddings", "weight": 1.0} -->

Another connection concerns how the dictionary or embedding itself is produced. Section[sec:koopman] treats the dictionary $\Psi$ as either hand-specified or learned via a fixed-basis regression (EDMD). The broader ML community is increasingly learning such embeddings with large sequence-to-sequence architectures, e.g., in foundation models and vision-language-action (VLA) models for control, and it is natural to ask how these relate to the Koopman lifting used in this tutorial. A recent example is [li2025mamko], who replace the constant, offline-fitted Koopman operator with one generated online by a Mamba-style selective state-space model. Here, the operator itself becomes a function of the recent input-output history, rather than a fixed matrix estimated once from batch data. This can be read as a data-conditioned, time-varying relaxation of the bilinear surrogate[eq:bilinear-koopman], in which the Koopman operator's dependence on the input is no longer restricted to being bilinear but is instead parameterized by a recurrent/SSM-based network.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Representation Learning, Foundation Models, and Koopman Embeddings", "weight": 1.0} -->

The trade-off is that the resulting model no longer comes with the finite-sample guarantees of Sections[sec:sysid] and[sec:koopman-error]. Related deep-learning-based Koopman parameterizations, which similarly trade the guarantees of a fixed finite dictionary for greater expressiveness, include the deep autoencoder architecture of [lusch2018deep], which learns Koopman eigenfunctions directly from trajectory data, and its control-affine extensions[yeung2019learning,han2020deep], which learn a bilinear Koopman representation end-to-end for use in prediction and control.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Representation Learning, Foundation Models, and Koopman Embeddings", "weight": 1.0} -->

More broadly, the idea that a learned embedding linearizes (or bilinearizes) otherwise nonlinear control-affine dynamics recurs across the RL and robotics literature under different names. embed-to-control learns a locally linear latent dynamics model directly from raw observations[watter2015embed], Koopman Q-learning exploits a learned Koopman-linear latent space for offline RL[weissenbacher2022koopman], and task-oriented Koopman encoders trained contrastively have been used directly for control[lyu2023taskoriented]. Each of these can be viewed through the same lens as Section[sec:koopman], i.e., an embedding $\Psi$(now learned end-to-end rather than fixed) is chosen so that the induced dynamics in the embedding space are (bi)linear, after which linear or bilinear control machinery applies. Note that this is one thread among many connecting embedding learning to Koopman theory; we have not attempted to survey the rapidly growing literature on foundation models and VLAs for control, and we expect this connection to develop further substantially.

<!-- chunk {"id": "body-0269", "role": "body", "section": "World Models and Predictive Architectures", "weight": 1.0} -->

Closely related to the embeddings of Section [sec:connections-foundation-models] and the planning in belief-space in Section[sec:Blief-space MPC] is the broader notion of a world model. There, a learned model predicts future (latent) states, typically used for planning or as a training signal for a policy. The joint-embedding predictive architecture (JEPA) proposed by [lecun2022path] formalizes one influential instance of this idea, training an encoder and predictor to forecast future representations rather than future raw observations, with concrete instantiations for images and video[assran2023ijepa,bardes2025vjepa]. The belief-space MPC controller design problem we studies in [sec:Blief-space MPC] for controlling linear dynamical systems from bilinear observations fits into the framework of the recent work on adaptive MPC control using world models[wang2026adajepa]. The appeal of predicting in representation space rather than observation space is structurally similar to the appeal of the Koopman lifting in Section[sec:koopman].

<!-- chunk {"id": "body-0270", "role": "body", "section": "World Models and Predictive Architectures", "weight": 1.0} -->

Both approaches posit that some transformation of the state admits simpler (ideally linear or low-order) predictive dynamics than the raw state itself, and both must contend with a representation-collapse or degeneracy failure mode that has no direct analogue in the finite-dimensional, spectrally well-posed Koopman setting we have considered. Unlike the Koopman surrogates of Section[sec:koopman], JEPA-style world models do not currently come with the finite-sample error bounds that make the residual $r_\Psi$ compatible with the robust controller designs of Section[sec:control-bilinear-systems]. Closing this gap e.g., deriving a Koopman-style residual bound for a learned, JEPA-style predictor, or conversely identifying conditions under which a JEPA-trained representation is provably (approximately) Koopman-invariant, is, to our knowledge, open.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we set out to give a self-contained tutorial on non-asymptotic learning and control of bilinear dynamical systems. We reviewed identification of input-output behavior using least-squares estimation with nonlinear features, highlighting the statistical tools used for handling quantities that do not arise in the linear analysis. On the control side, we discussed how the separation principle, a cornerstone of linear control, can fail to hold in the bilinear setting, motivating a belief-space perspective. We also introduced Lyapunov-, semidefinite-, and SOS- approaches to state-feedback stabilization under modeling errors. Finally, we reviewed the generality of these techniques for nonlinear control-affine systems through Koopman operator theory.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We hope to show that bilinear systems retain enough structure to support finite-sample guarantees in the spirit of classical linear theory, while already surfacing many of the difficulties: input-dependent stability, coupled state estimation and control, and nonconvex optimization landscapes that characterize nonlinear systems more broadly. Open questions reflect the current boundary of what is understood for nonlinear systems, and we expect that closing them will require ideas drawn jointly from control theory, statistics, and machine learning. We hope this tutorial offers both the technical foundation and the shared vocabulary needed for researchers across these communities to take up that work, and that bilinear systems continue to serve as a productive testbed for extending non-asymptotic learning and control beyond the linear setting.
