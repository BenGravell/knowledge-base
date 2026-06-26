## Introduction

One of the main paradigms in the field of systems and control is that of *model-based* control. Indeed, many control design techniques rely on a system model, represented by e.g. a state-space system or transfer function. In practice, system models are rarely known a priori and have to be identified from measured data using system identification methods such as prediction error or subspace identification. As a consequence, the use of model-based control techniques inherently leads to a two-step control procedure consisting of system identification followed by control design.

In contrast, *data-driven* control aims to bypass this two-step procedure by constructing controllers directly from data, without (explicitly) identifying a system model. This direct approach is not only attractive from a conceptual point of view but can also be useful in situations where system identification is difficult or even impossible because the data do not give sufficient information.

The first contribution to data-driven control is often attributed to Ziegler and Nichols for their work on tuning PID controllers. Adaptive control, iterative feedback tuning and unfalsified control can also be regarded as classical data-driven control techniques. More recently, the problem of finding optimal controllers from data has received considerable attention. The proposed solutions to this problem are quite varied, ranging from the use of batch-form Riccati equations to approaches that apply reinforcement learning. Additional noteworthy data-driven control problems include predictive control, model reference control and (intelligent) PID control. For more references and classifications of data-driven control techniques, we refer to the survey.

In addition to control problems, also *analysis* problems have been studied within a data-based framework. The authors of analyze the stability of an input/output system using time series data. The papers deal with data-based controllability and observability analysis. Moreover, the problem of verifying dissipativity on the basis of measured system trajectories has been studied .

A result that is becoming increasingly popular in the study of data-driven problems is the so-called *fundamental lemma* by Willems and coworkers. This result roughly states that all possible trajectories of a linear time-invariant system can be obtained from any given trajectory whose input component is persistently exciting. The fundamental lemma has clear implications for system identification. Indeed, it provides criteria under which the data are sufficiently informative to uniquely identify the system model within a given model class. In addition, the result has also been applied to data-driven control problems. The idea is that control laws can be obtained directly from data, with the underlying mechanism that the system is represented implicitly by the so-called Hankel matrix of a measured trajectory. This framework has led to several interesting control strategies, first in a behavioral setting, and more recently in the context of state-space systems.

The above approaches all use persistently exciting data in the control design, meaning that one could (hypothetically) identify the system model from the same data. An intriguing question is therefore the following: is it possible to obtain a controller from data that are *not* informative enough to uniquely identify the system? An affirmative answer would be remarkable, since it would highlight situations in which data-driven control is more powerful than the combination of system identification and model-based control. On the other hand, a negative answer would also be significant, as it would give a theoretic justification for the use of persistently exciting data for data-driven analysis and control.

To address the above question, this paper introduces a general framework to study data informativity problems for data-driven analysis and control. Specifically, our contributions are the following: Inspired by the concept of data informativity in system identification, we introduce a general notion of informativity for data-driven analysis and control.

We study the data-driven analysis of several system theoretic properties like stability, stabilizability and controllability. For each of these problems, we provide necessary and sufficient conditions under which the data are informative for this property, i.e., conditions required to ascertain the system's property from data.

We study data-driven control problems such as stabilization by state feedback, stabilization by dynamic measurement feedback, deadbeat control and linear quadratic regulation. In each of the cases, we give conditions under which the data are informative for controller design.

For each of the studied control problems, we develop methods to compute a controller from data, assuming that the informativity conditions are satisfied.

Our work has multiple noteworthy implications. First of all, we show that for problems like stabilization by state feedback, the corresponding informativity conditions on the data are *weaker* than those for system identification. This implies that a stabilizing feedback can be obtained from data that are not sufficiently informative to uniquely identify the system.

Moreover, for problems such as linear quadratic regulation (LQR), we show that the informativity conditions are essentially the same as for system identification. Therefore, our results provide a theoretic justification for imposing the strong persistency of excitation conditions in prior work on the LQR problem, such as and.

The paper is organized as follows. In Section II we introduce the problem at a conceptual level. Subsequently, in Section III we provide data informativity conditions for controllability and stabilizability. Section IV deals with data-driven control problems with input/state data. Next, Section V discusses control problems where ouput data plays a role. Finally, Section VI contains our conclusions and suggestions for future work.

## Problem formulation

In this section we will first introduce the informativity framework for data-driven analysis and control in a fairly abstract manner.

Let $\Sigma$ be a model class, i.e. a given set of systems containing the 'true' system denoted by $\mathcal{S}$. We assume that the 'true' system $\mathcal{S}$ is not known but that we have access to a set of data, $\mathcal{D}$, which are generated by this system. In this paper we are interested in assessing system-theoretic properties of $\mathcal{S}$ and designing control laws for it from the data $\mathcal{D}$.

Given the data $\mathcal{D}$, we define $\Sigma_{\mathcal{D}} \subseteq \Sigma$ to be the set of all systems that are consistent with the data $\mathcal{D}$, i.e. that could also have generated these data.

We first focus on data-driven analysis. Let $\mathcal{P}$ be a system-theoretic property. We will denote the set of all systems within $\Sigma$ having this property by $\Sigma_{\mathcal{P}}$.

Now suppose we are interested in the question whether our 'true' system $\mathcal{S}$ has the property $\mathcal{P}$. As the only information we have to base our answer on are the data $\mathcal{D}$ obtained from the system, we can only conclude that the 'true' system has property $\mathcal{P}$ if all systems consistent with the data $\mathcal{D}$ have the property $\mathcal{P}$. This leads to the following definition:

### Definition 1 (Informativity)

We say that the data $\mathcal{D}$ are informative for property $\mathcal{P}$ if $\Sigma_{\mathcal{D}} \subseteq \Sigma_{\mathcal{P}}$.

Next, we illustrate the above abstract setup by an example.

### Example 2

For given $n$ and $m$, let $\Sigma$ be the set of all discrete-time linear input/state systems of the form where $\mathbf{x}$ is the $n$-dimensional state and $\mathbf{u}$ is the $m$-dimensional input. Let the 'true' system $\mathcal{S}$ be represented by the matrices $(A_{s},B_{s})$.

An example of a data set $\mathcal{D}$ arises when considering data-driven problems on the basis of input and state measurements. Suppose that we collect input/state data on $q$ time intervals $\{ 0,1,\ldots,T_{i}\}$ for $i = {1,2,\ldots,q}$. Let denote the input and state data on the $i$-th interval. By defining we clearly have $X_{+}^{i} = {{A_{s}X_{-}^{i}} + {B_{s}U_{-}^{i}}}$ for each $i$ because the 'true' system is assumed to generate the data. Now, introduce the notation We then define the data as $\mathcal{D}:={(U_{-},X)}$. In this case, the set $\Sigma_{\mathcal{D}}$ is equal to $\Sigma_{(U_{-},X)}$ defined by Clearly, we have ${(A_{s},B_{s})} \in \Sigma_{\mathcal{D}}$.

Suppose that we are interested in the system-theoretic property $\mathcal{P}$ of stabilizability. The corresponding set $\Sigma_{\mathcal{P}}$ is then equal to $\Sigma_{stab}$ defined by Then, the data $(U_{-},X)$ are informative for stabilizability if $\Sigma_{(U_{-},X)} \subseteq \Sigma_{stab}$. That is, if all systems consistent with the input/state measurements are stabilizable.

In general, if the 'true' system $\mathcal{S}$ can be uniquely determined from the data $\mathcal{D}$, that is $\Sigma_{\mathcal{D}} = {\{\mathcal{S}\}}$ and $\mathcal{S}$ has the property $\mathcal{P}$, then it is evident that the data $\mathcal{D}$ are informative for $\mathcal{P}$. However, the converse may not be true: $\Sigma_{\mathcal{D}}$ might contain many systems, all of which have property $\mathcal{P}$. This paper is interested in necessary and sufficient conditions for informativity of the data. Such conditions reveal the minimal amount of information required to assess the property $\mathcal{P}$. A natural problem statement is therefore the following:

### Problem 1 (Informativity problem)

Provide necessary and sufficient conditions on $\mathcal{D}$ under which the data are informative for property $\mathcal{P}$.

The above gives us a general framework to deal with data-driven analysis problems. Such analysis problems will be the main focus of Section III.

This paper also deals with data-driven control problems. The objective in such problems is the data-based design of controllers such that the closed loop system, obtained from the interconnection of the 'true' system $\mathcal{S}$ and the controller, has a specified property.

As for the analysis problem, we have only the information from the data to base our design . Therefore, we can only guarantee our control objective if the designed controller imposes the specified property when interconnected with any system from the set $\Sigma_{\mathcal{D}}$.

For the framework to allow for data-driven control problems, we will consider a system-theoretic property $\mathcal{P}{(\mathcal{K})}$ that depends on a given controller $\mathcal{K}$. For properties such as these, we have the following variant of informativity:

### Definition 3 (Informativity for control)

We say that the data $\mathcal{D}$ are informative for the property $\mathcal{P}{( \cdot )}$ if there exists a controller $\mathcal{K}$ such that $\Sigma_{\mathcal{D}} \subseteq \Sigma_{\mathcal{P}{(\mathcal{K})}}$.

### Example 4

For systems and data like in Example 2, we can take the controller $\mathcal{K} = K \in {\mathbb{R}}^{m \times n}$ and the property ${\mathcal{P}{(\mathcal{K})}}:$ 'interconnection with the state feedback $K$ yields a stable closed loop system'. The corresponding set of systems $\Sigma_{\mathcal{P}{(\mathcal{K})}}$ is equal to $\Sigma_{K}$ defined by The first step in any data-driven control problem is to determine whether it is possible to obtain a suitable controller from given data. This leads to the following informativity problem:

### Problem 2 (Informativity problem for control)

Provide necessary and sufficient conditions on $\mathcal{D}$ under which there exists a controller $\mathcal{K}$ such that the data are informative for property $\mathcal{P}{(\mathcal{K})}$.

The second step of data-driven control involves the design of a suitable controller. In terms of our framework, this can be stated as:

### Problem 3 (Control design problem)

Under the assumption that the data $\mathcal{D}$ are informative for property $\mathcal{P}{( \cdot )}$, find a controller $\mathcal{K}$ such that $\Sigma_{\mathcal{D}} \subseteq \Sigma_{\mathcal{P}{(\mathcal{K})}}$.

As stated in the introduction, we will highlight the strength of this framework by solving multiple problems. We stress that throughout the paper it is assumed that the data are given and are not corrupted by noise.

## Data-driven analysis

In this section, we will study data-driven analysis of controllability and stabilizability given input and state measurements. As in Example 2, consider the discrete-time linear system We will consider data consisting of input and state measurements. We define the matrices $U_{-}$ and $X$ as in (3a) and define $X_{-}$ and $X_{+}$ as in (3b). The set of all systems compatible with these data was introduced. In order to stress that we deal with input/state data, we rename it here as Note that the defining equation of is a system of linear equations in the unknowns $A$ and $B$. The solution space of the corresponding homogeneous equations is denoted by $\Sigma_{i/s}^{0}$ and is equal to We consider the problem of data-driven analysis for systems of the form. If $(A_{s},B_{s})$ is the only system that explains the data, data-driven analysis could be performed by first identifying this system and then analyzing its properties. It is therefore of interest to know under which conditions there is only one system that explains the data.

### Definition 5

We say that the data $(U_{-},X)$ are informative for system identification if $\Sigma_{i/s} = {\{{(A_{s},B_{s})}\}}$.

It is straightforward to derive the following result:

### Proposition 6

The data $(U_{-},X)$ are informative for system identification if and only if Furthermore, if holds, there exists a right inverse^22^2Note that $\begin{bmatrix} \end{bmatrix}$ is not unique whenever $T > {n + m}$. $\begin{bmatrix} \end{bmatrix}$ such that and for any such right inverse $A_{s} = {X_{+}V_{1}}$ and $B_{s} = {X_{+}V_{2}}$.

As we will show in this section, the condition is not necessary for data-driven analysis in general. We now proceed by studying data-driven analysis of controllability and stabilizability. Recall the Hautus test \[45, Theorem 3.13\] for controllability: a system $(A,B)$ is controllable if and only if for all $\lambda \in {\mathbb{C}}$. For stabilizability, we require that holds for all $\lambda$ outside the open unit disc.

Now, we introduce the following sets of systems: Using Definition 1. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"), we obtain the notions of informativity for controllability and stabilizability. To be precise:

### Definition 7

We say that the data $(U_{-},X)$ are informative for controllability if $\Sigma_{i/s} \subseteq \Sigma_{\text{cont}}$ and informative for stabilizability if $\Sigma_{i/s} \subseteq \Sigma_{\text{stab}}$.

In the following theorem, we give necessary and sufficient conditions for the above notions of informativity. The result is remarkable as only data matrices are used to assess controllability and stabilizability.

### Theorem 8 (Data-driven Hautus tests)

The data $(U_{-},X)$ are informative for controllability if and only if Similarly, the data $(U_{-},X)$ are informative for stabilizability if and only if Before proving the theorem, we will discuss some of its implications. We begin with computational issues.

### Remark 9

Similar to the classical Hautus test, (11. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) and (12. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) can be verified by checking the rank for finitely many complex numbers $\lambda$. Indeed, (11. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) is equivalent to ${{rank}{(X_{+})}} = n$ and for all $\lambda \neq 0$ with $\lambda^{- 1} \in {\sigma{({X_{-}X_{+}^{\dagger}})}}$, where $X_{+}^{\dagger}$ is any right inverse of $X_{+}$. Here, $\sigma{(M)}$ denotes the spectrum, i.e. set of eigenvalues of the matrix $M$. Similarly, (12. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) is equivalent to ${{rank}{({X_{+} - X_{-}})}} = n$ and for all $\lambda \neq 1$ with ${({\lambda - 1})}^{- 1} \in {\sigma{({X_{-}{({X_{+} - X_{-}})}^{\dagger}})}}$, where ${({X_{+} - X_{-}})}^{\dagger}$ is any right inverse of $X_{+} - X_{-}$.

A noteworthy point to mention is that there are situations in which we can conclude controllability/stabilizability from the data without being able to identify the 'true' system uniquely, as illustrated next.

### Example 10

Suppose that $n = 2$, $m = 1$, $q = 1$, $T_{1} = 2$ and we obtain the data This implies that Clearly, by Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control") we see that these data are informative for controllability, as As therefore all systems explaining the data are controllable, we conclude that the 'true' system is controllable. It is worthwhile to note that the data are not informative for system identification, as Proof of Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control"). We will only prove the characterization of informativity for controllability. The proof for stabilizability uses very similar arguments, and is hence omitted.

Note that the condition (11. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) is equivalent to the implication: Suppose that the implication holds. Let ${(A,B)} \in \Sigma_{i/s}$ and suppose that ${z^{\ast}\begin{bmatrix} \end{bmatrix}} = 0$. We want to prove that $z = 0$. Note that ${z^{\ast}\begin{bmatrix} \end{bmatrix}} = 0$ implies that or equivalently ${z^{\ast}X_{+}} = {\lambdaz^{\ast}X_{-}}$. This means that $z = 0$. We conclude that $(A,B)$ is controllable, i.e., $(U_{-},X)$ are informative for controllability.

Conversely, suppose that $(U_{-},X)$ are informative for controllability. Let $z \in {\mathbb{C}}^{n}$ and $\lambda \in {\mathbb{C}}$ be such that ${z^{\ast}X_{+}} = {\lambdaz^{\ast}X_{-}}$. This implies that for all ${(A,B)} \in \Sigma_{i/s}$, we have ${z^{\ast}\begin{bmatrix} \end{bmatrix}\begin{bmatrix} \end{bmatrix}} = {\lambdaz^{\ast}X_{-}}$. In other words, We now distinguish two cases, namely the case that $\lambda$ is real, and the case that $\lambda$ is complex. First suppose that $\lambda$ is real. Without loss of generality, $z$ is real. We want to prove that $z = 0$. Suppose on the contrary that $z \neq 0$ and ${z^{\top}z} = 1$. We define the (real) matrices In view of, we find that ${(\overline{A},\overline{B})} \in \Sigma_{i/s}$. Moreover, This means that However, this is a contradiction as $(\overline{A},\overline{B})$ is controllable by the hypothesis that $(U_{-},X)$ are informative for controllability. We conclude that $z = 0$ which shows that holds for the case that $\lambda$ is real.

Secondly, consider the case that $\lambda$ is complex. We write $z$ as $z = {p + {iq}}$, where ${p,q} \in {\mathbb{R}}^{n}$ and $i$ denotes the imaginary unit. If $p$ and $q$ are linearly dependent, then $p = {\alphaq}$ or $q = {\betap}$ for ${\alpha,\beta} \in {\mathbb{R}}$. If $p = {\alphaq}$ then substitution of $z = {{({\alpha + i})}q}$ into ${z^{\ast}X_{+}} = {\lambdaz^{\ast}X_{-}}$ yields that is, ${q^{\top}X_{+}} = {\lambdaq^{\top}X_{-}}$. As $q^{\top}X_{+}$ is real and $\lambda$ is complex, we must have ${q^{\top}X_{+}} = 0$ and ${q^{\top}X_{-}} = 0$. This means that ${z^{\ast}X_{+}} = {z^{\ast}X_{-}} = 0$, hence ${z^{\ast}X_{+}} = {\muz^{\ast}X_{-}}$ for any real $\mu$, which means that $z = 0$ by case 1. Using the same arguments, we can show that $z = 0$ if $q = {\betap}$.

It suffices to prove now that $p$ and $q$ are linearly dependent. Suppose on the contrary that $p$ and $q$ are linearly independent. Since $\lambda$ is complex, $n \geqslant 2$. Therefore, by linear independence of $p$ and $q$ there exist ${\eta,\zeta} \in {\mathbb{R}}^{n}$ such that We now define the real matrices $\overline{A}$ and $\overline{B}$ as By we have ${(\overline{A},\overline{B})} \in \Sigma_{i/s}$. Next, we compute This implies that ${z^{\ast}\begin{bmatrix} {\overline{A} - {\lambdaI}} & \overline{B} \end{bmatrix}} = 0$. Using the fact that $(\overline{A},\overline{B})$ is controllable, we conclude that $z = 0$. This is a contradiction with the fact that $p$ and $q$ are linearly independent. Thus $p$ and $q$ are linearly dependent and therefore implication holds. This proves the theorem. $\blacksquare$ In addition to controllability and stabilizability, we can also study the *stability* of an autonomous system of the form To this end, let $X$ denote the matrix of state measurements obtained, as defined in (3a). The set of all autonomous systems compatible with these data is Then, we say the data $X$ are *informative for stability* if any matrix $A \in \Sigma_{\text{s}}$ is stable, i.e. Schur. Using Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control") we can show that stability can only be concluded if the 'true' system can be uniquely identified.

### Corollary 11

The data $X$ are informative for stability if and only if $X_{-}$ has full row rank and $X_{+}X_{-}^{\dagger}$ is stable for any right inverse $X_{-}^{\dagger}$, equivalently $\Sigma_{s} = {\{ A_{s}\}}$ and $A_{s} = {X_{+}X_{-}^{\dagger}}$ is stable.

Proof. Since the 'if' part is evident, we only prove the 'only if' part. By taking $B = 0$, it follows from Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control") that the data $X$ are informative for stability if and only if Let $z$ be such that ${z^{\top}X_{-}} = 0$. Take $A \in \Sigma_{s}$ and $\lambda > 1$ such that $\lambda$ is not an eigenvalue of $A$. Note that Since ${{rank}{({X_{+} - {\lambdaX_{-}}})}} = n$, we may conclude that $z = 0$. Hence, $X_{-}$ has full row rank. Therefore, $\Sigma_{s} = {\{ A_{s}\}}$ where $A_{s} = {X_{+}X_{-}^{\dagger}}$ for any right inverse $X_{-}^{\dagger}$ and $A_{s}$ is stable. $\blacksquare$ Note that there is a subtle but important difference between the characterizations (12. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) and. For the first the data $X$ are assumed to be generated by a system with inputs, whereas the data for the second characterization are generated by an autonomous system.

## Control using input and state data

In this section we will consider various state feedback control problems on the basis of input/state measurements. First, we will consider the problem of data-driven stabilization by static state feedback, where the data consist of input and state measurements. As described in the problem statement we will look at the informativity and design problems separately as special cases of Problem 2. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control") and Problem 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"). We will then use similar techniques to obtain a result for deadbeat control.

After this, we will shift towards the linear quadratic regulator problem, where we wish to find a stabilizing feedback that additionally minimizes a specified quadratic cost.

### IV-A Stabilization by state feedback

In what follows, we will consider the problem of finding a stabilizing controller for the system, using only the data $(U_{-},X)$. To this end, we define the set of systems $(A,B)$ that are stabilized by a given $K$: In addition, recall the set $\Sigma_{i/s}$ as defined in and $\Sigma_{i/s}^{0}$. In line with Definition 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control") we obtain the following notion of informativity for stabilization by state feedback.

### Definition 12

We say that the data $(U_{-},X)$ are informative for stabilization by state feedback if there exists a feedback gain $K$ such that $\Sigma_{i/s} \subseteq \Sigma_{K}$.

### Remark 13

At this point, one may wonder about the relation between informativity for stabilizability (as in Section III) and informativity for stabilization. It is clear that $(U_{-},X)$ are informative for stabilizability if $(U_{-},X)$ are informative for stabilization by state feedback. However, the reverse statement does not hold in general. This is due to the fact that all systems $(A,B)$ in $\Sigma_{i/s}$ may be stabilizable, but there may not be a *common* feedback gain $K$ such that $A + {BK}$ is stable for all of these systems. Note that the existence of a common stabilizing $K$ for all systems in $\Sigma_{i/s}$ is essential, since there is no way to distinguish between the systems in $\Sigma_{i/s}$ based on the given data $(U_{-},X)$.

The following example further illustrates the difference between informativity for stabilizability and informativity for stabilization.

### Example 14

Consider the scalar system where ${{\mathbf{x}},{\mathbf{u}}} \in {\mathbb{R}}$. Suppose that $q = 1$, $T_{1} = 1$ and ${x{}} = 0$, ${u{}} = 1$ and ${x{}} = 1$. This means that $U_{-} = \begin{bmatrix} \end{bmatrix}$ and $X = \begin{bmatrix} \end{bmatrix}$. It can be shown that $\Sigma_{i/s} = {\{{(a,1)}\mid{a \in {\mathbb{R}}}\}}$. Clearly, all systems in $\Sigma_{i/s}$ are stabilizable, i.e., $\Sigma_{i/s} \subseteq \Sigma_{\text{stab}}$. Nonetheless, the data are not informative for *stabilization*. This is because the systems $({- 1},1)$ and $$ in $\Sigma_{i/s}$ cannot be stabilized by the *same* controller of the form ${u{(t)}} = {Kx{(t)}}$. We conclude that informativity of the data for stabilizability does not imply informativity for stabilization by state feedback.

The notion of informativity for stabilization by state feedback is a specific example of informativity for control. As described in Problem 2. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"), we will first find necessary and sufficient conditions for informativity for stabilization by state feedback. After this, we will design a corresponding controller, as described in Problem 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control").

In order to be able to characterize informativity for stabilization, we first state the following lemma.

### Lemma 15

Suppose that the data $(U_{-},X)$ are informative for stabilization by state feedback, and let $K$ be a feedback gain such that $\Sigma_{i/s} \subseteq \Sigma_{K}$. Then ${A_{0} + {B_{0}K}} = 0$ for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. Equivalently, Proof. We first prove that $A_{0} + {B_{0}K}$ is *nilpotent* for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. By hypothesis, $A + {BK}$ is stable for all ${(A,B)} \in \Sigma_{i/s}$. Let ${(A,B)} \in \Sigma_{i/s}$ and ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$ and define the matrices $F:={A + {BK}}$ and $F_{0}:={A_{0} + {B_{0}K}}$. Then, the matrix $F + {\alphaF_{0}}$ is stable for all $\alpha \geqslant 0$. By dividing by $\alpha$, it follows that, for all $\alpha \geqslant 1$, the spectral radius of the matrix is smaller than $1/\alpha$. From the continuity of the spectral radius by taking the limit as $\alpha$ tends to infinity, we see that $F_{0} = {A_{0} + {B_{0}K}}$ is nilpotent for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. Note that we have whenever ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. This means that ${({A_{0} + {B_{0}K}})}^{T}{({A_{0} + {B_{0}K}})}$ is nilpotent. Since the only symmetric nilpotent matrix is the zero matrix, we see that ${A_{0} + {B_{0}K}} = 0$ for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. This is equivalent to which is equivalent to ${{{im}\begin{bmatrix} \end{bmatrix}} \subseteq {{im}\begin{bmatrix} \end{bmatrix}}}.$ $\blacksquare$ The previous lemma is instrumental in proving the following theorem that gives necessary and sufficient conditions for informativity for stabilization by state feedback.

### Theorem 16

The data $(U_{-},X)$ are informative for stabilization by state feedback if and only if the matrix $X_{-}$ has full row rank and there exists a right inverse $X_{-}^{\dagger}$ of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is stable.

Moreover, $K$ is such that $\Sigma_{i/s} \subseteq \Sigma_{K}$ if and only if $K = {U_{-}X_{-}^{\dagger}}$, where $X_{-}^{\dagger}$ satisfies the above properties.

Proof. To prove the 'if' part of the first statement, suppose that $X_{-}$ has full row rank and there exists a right inverse $X_{-}^{\dagger}$ of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is stable. We define $K:={U_{-}X_{-}^{\dagger}}$. Next, we see that for all ${(A,B)} \in \Sigma_{i/s}$. Therefore, $A + {BK}$ is stable for all ${(A,B)} \in \Sigma_{i/s}$, i.e., $\Sigma_{i/s} \subseteq \Sigma_{K}$. We conclude that the data $(U_{-},X)$ are informative for stabilization by state feedback, proving the 'if' part of the first statement. Since $K = {U_{-}X_{-}^{\dagger}}$ is such that $\Sigma_{i/s} \subseteq \Sigma_{K}$, we have also proven the 'if' part of the second statement as a byproduct.

Next, to prove the 'only if' part of the first statement, suppose that the data $(U_{-},X)$ are informative for stabilization by state feedback. Let $K$ be such that $A + {BK}$ is stable for all ${(A,B)} \in \Sigma_{i/s}$. By Lemma 15 we know that This implies that $X_{-}$ has full row rank and there exists a right inverse $X_{-}^{\dagger}$ such that By, we obtain ${A + {BK}} = {X_{+}X_{-}^{\dagger}}$, which shows that $X_{+}X_{-}^{\dagger}$ is stable. This proves the 'only if' part of the first statement. Finally,, the stabilizing feedback gain $K$ is indeed of the form $K = {U_{-}X_{-}^{\dagger}}$, which also proves the 'only if' part of the second statement. $\blacksquare$ Theorem 16 gives a characterization of all data that are informative for stabilization by state feedback and provides a stabilizing controller. Nonetheless, the procedure to compute this controller might not be entirely satisfactory since it is not clear how to find a right inverse of $X_{-}$ that makes $X_{+}X_{-}^{\dagger}$ stable. In general, $X_{-}$ has many right inverses, and $X_{+}X_{-}^{\dagger}$ can be stable or unstable depending on the particular right inverse $X_{-}^{\dagger}$. To deal with this problem and to solve the design problem, we give a characterization of informativity for stabilization in terms of linear matrix inequalities (LMI's). The feasibility of such LMI's can be verified using standard methods.

### Theorem 17

The data $(U_{-},X)$ are informative for stabilization by state feedback if and only if there exists a matrix $\Theta \in {\mathbb{R}}^{T \times n}$ satisfying Moreover, $K$ satisfies $\Sigma_{i/s} \subseteq \Sigma_{K}$ if and only if $K = {U_{-}\Theta{({X_{-}\Theta})}^{- 1}}$ for some matrix $\Theta$ satisfying.

### Remark 18

To the best of our knowledge, LMI conditions for data-driven stabilization were first studied . In fact, the linear matrix inequality is the same as that of \[40, Theorem 3\]. However, an important difference is that the results in assume that the input $u$ is persistently exciting of sufficiently high order. In contrast, Theorem 17, as well as Theorem 16, do not require such conditions. The characterization provides the minimal conditions on the data under which it is possible to obtain a stabilizing controller.

### Example 19

Consider an unstable system of the form, where $A_{s}$ and $B_{s}$ are given by We collect data from this system on a single time interval from $t = 0$ until $t = 2$, which results in the data matrices Clearly, the matrix $X_{-}$ is square and invertible, and it can be verified that is stable, since its eigenvalues are $\frac{1}{2}{({1 \pm {\sqrt{2}i}})}$. We conclude by Theorem 16 that the data $(U_{-},X)$ are informative for stabilization by state feedback. The same conclusion can be drawn from Theorem 17 since solves. Next, we can conclude from either Theorem 16 or Theorem 17 that the stabilizing feedback gain in this example is unique, and given by $K = {U_{-}X_{-}^{- 1}} = \begin{bmatrix} \end{bmatrix}$. Finally, it is worth noting that the data are not informative for system identification. In fact, ${(A,B)} \in \Sigma_{i/s}$ if and only if for some ${a_{1},a_{2}} \in {\mathbb{R}}$.

Proof of Theorem 17. To prove the 'if' part of the first statement, suppose that there exists a $\Theta$ satisfying. In particular, this implies that $X_{-}\Theta$ is symmetric positive definite. Therefore, $X_{-}$ has full row rank. By taking a Schur complement and multiplying by $- 1$, we obtain Since $X_{-}\Theta$ is positive definite, this implies that $X_{+}\Theta{({X_{-}\Theta})}^{- 1}$ is stable. In other words, there exists a right inverse $X_{-}^{\dagger}:={\Theta{({X_{-}\Theta})}^{- 1}}$ of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is stable. By Theorem 16, we conclude that $(U_{-},X)$ are informative for stabilization by state feedback, proving the 'if' part of the first statement. Using Theorem 16 once more, we see that $K:={U_{-}\Theta{({X_{-}\Theta})}^{- 1}}$ stabilizes all systems in $\Sigma_{i/s}$, which in turn proves the 'if' part of the second statement.

Subsequently, to prove the 'only if' part of the first statement, suppose that the data $(U_{-},X)$ are informative for stabilization by state feedback. Let $K$ be any feedback gain such that $\Sigma_{i/s} \subseteq \Sigma_{K}$. By Theorem 16, $X_{-}$ has full row rank and $K$ is of the form $K = {U_{-}X_{-}^{\dagger}}$, where $X_{-}^{\dagger}$ is a right inverse of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is stable. The stability of $X_{+}X_{-}^{\dagger}$ implies the existence of a symmetric positive definite matrix $P$ such that Next, we define $\Theta:={X_{-}^{\dagger}P}$ and note that Via the Schur complement we conclude that Since ${X_{-}X_{-}^{\dagger}} = I$, we see that $P = {X_{-}\Theta}$, which proves the 'only if' part of the first statement. Finally, by definition of $\Theta$, we have $X_{-}^{\dagger} = {\ThetaP^{- 1}} = {\Theta{({X_{-}\Theta})}^{- 1}}$. Recall that $K = {U_{-}X_{-}^{\dagger}}$, which shows that $K$ is of the form $K = {U_{-}\Theta{({X_{-}\Theta})}^{- 1}}$ for $\Theta$ satisfying. This proves the 'only if' part of the second statement and hence the proof is complete. $\blacksquare$ In addition to the stabilizing controllers discussed in Theorems 16 and 17, we may also look for a controller of the form ${{\mathbf{u}}{(t)}} = {K{\mathbf{x}}{(t)}}$ that stabilizes the system in *finite time*. Such a controller is called a *deadbeat controller* and is characterized by the property that ${{({A_{s} + {B_{s}K}})}^{t}x_{0}} = 0$ for all $t \geqslant n$ and all $x_{0} \in {\mathbb{R}}^{n}$. Thus, $K$ is a deadbeat controller if and only if $A_{s} + {B_{s}K}$ is nilpotent. Now, for a given matrix $K$ define Then, analogous to the definition of informativity for stabilization by state feedback, we have the following definition of informativity for deadbeat control.

### Definition 20

We say that the data $(U_{-},X)$ are informative for deadbeat control if there exists a feedback gain $K$ such that $\Sigma_{i/s} \subseteq \Sigma_{K}^{\text{nil}}$.

Similarly to Theorem 16, we obtain the following necessary and sufficient conditions for informativity for deadbeat control.

### Theorem 21

The data $(U_{-},X)$ are informative for deadbeat control if and only if the matrix $X_{-}$ has full row rank and there exists a right inverse $X_{-}^{\dagger}$ of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is nilpotent.

Moreover, if this condition is satisfied then the feedback gain $K:={U_{-}X_{-}^{\dagger}}$ yields a deadbeat controller, that is, $\Sigma_{i/s} \subseteq \Sigma_{K}^{\text{nil}}$.

### Remark 22

In order to compute a suitable right inverse $X_{-}^{\dagger}$ such that $X_{+}X_{-}^{\dagger}$ is nilpotent, we can proceed as follows. Since $X_{-}$ has full row rank, we have $T \geqslant n$. We now distinguish two cases: $T = n$ and $T > n$. In the former case, $X_{-}$ is nonsingular and hence $X_{+}X_{-}^{- 1}$ is nilpotent. In the latter case, there exist matrices $F \in {\mathbb{R}}^{T \times n}$ and $G \in {\mathbb{R}}^{T \times {({T - n})}}$ such that $\begin{bmatrix} \end{bmatrix}$ is nonsingular and ${X_{-}\begin{bmatrix} \end{bmatrix}} = \begin{bmatrix} \end{bmatrix}$. Note that $X_{-}^{\dagger}$ is a right inverse of $X_{-}$ if and only if $X_{-}^{\dagger} = {F + {GH}}$ for some $H \in {\mathbb{R}}^{{({T - n})} \times n}$. Finding a right inverse $X_{-}^{\dagger}$ such that $X_{+}X_{-}^{\dagger}$ is nilpotent, therefore, amounts to finding $H$ such that ${X_{+}F} + {X_{+}GH}$ is nilpotent, i.e. has only zero eigenvalues. Such a matrix $H$ can be computed by invoking \[45, Thm. 3.29 and Thm. 3.32\] for the pair $({X_{+}F},{X_{+}G})$ and the stability domain ${{\mathbb{C}}_{g} = {\{ 0\}}}.$

### IV-B Informativity for linear quadratic regulation

Consider the discrete-time linear system. Let $x_{x_{0},u}{( \cdot )}$ be the state sequence of resulting from the input $u{( \cdot )}$ and initial condition ${x{}} = x_{0}$. We omit the subscript and simply write $x{( \cdot )}$ whenever the dependence on $x_{0}$ and $u$ is clear from the context.

Associated to system, we define the quadratic cost functional where $Q = Q^{\top}$ is positive semidefinite and $R = R^{\top}$ is positive definite. Then, the linear quadratic regulator (LQR) problem is the following:

### Problem 4 (LQR)

Determine for every initial condition $x_{0}$ an input $u^{\ast}$, such that ${\lim_{t\rightarrow\infty}{x_{x_{0},u^{\ast}}{(t)}}} = 0$, and the cost functional $J{(x_{0},u)}$ is minimized under this constraint.

Such an input $u^{\ast}$ is called optimal for the given $x_{0}$. Of course, an optimal input does not necessarily exist for all $x_{0}$. We say that the linear quadratic regulator problem is solvable for $(A,B,Q,R)$ if for every $x_{0}$ there exists an input $u^{\ast}$ such that The cost $J{(x_{0},u^{\ast})}$ is finite.

The limit ${\lim_{t\rightarrow\infty}{x_{x_{0},u^{\ast}}{(t)}}} = 0$.

The input $u^{\ast}$ minimizes the cost functional, i.e., for all $\overline{u}$ such that ${\lim_{t\rightarrow\infty}{x_{x_{0},\overline{u}}{(t)}}} = 0$.

In the sequel, we will require the notion of observable eigenvalues. Recall from e.g. \[45, Section 3.5\] that an eigenvalue $\lambda$ of $A$ is $(Q,A)$-observable if The following theorem provides necessary and sufficient conditions for the solvability of the linear quadratic regulator problem for $(A,B,Q,R)$. This theorem is the discrete-time analogue to the continuous-time case stated in \[45, Theorem 10.18\].

### Theorem 23

Let $Q = Q^{\top}$ be positive semidefinite and $R = R^{\top}$ be positive definite. Then the following statements hold: If $(A,B)$ is stabilizable, there exists a unique largest real symmetric solution $P^{+}$ to the discrete-time algebraic Riccati equation (DARE) in the sense that $P^{+} \geqslant P$ for every real symmetric $P$ satisfying. The matrix $P^{+}$ is positive semidefinite.

If, in addition to stabilizability of $(A,B)$, every eigenvalue of $A$ on the unit circle is $(Q,A)$-observable then for every $x_{0}$ a unique optimal input $u^{\ast}$ exists. Furthermore, this input sequence is generated by the feedback law ${\mathbf{u}} = {K{\mathbf{x}}}$, where Moreover, the matrix $A + {BK}$ is stable.

In fact, the linear quadratic regulator problem is solvable for $(A,B,Q,R)$ if and only if $(A,B)$ is stabilizable and every eigenvalue of $A$ on the unit circle is $(Q,A)$-observable.

If the LQR problem is solvable for $(A,B,Q,R)$, we say that $K$ given by is the optimal feedback gain for $(A,B,Q,R)$.

Now, for any given $K$ we define $\Sigma_{K}^{Q,R}$ as the set of all systems of the form for which $K$ is the optimal feedback gain corresponding to $Q$ and $R$, that is, This gives rise to another notion of informativity in line with Definition 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"). Again, let $\Sigma_{i/s}$ be given.

### Definition 24

Given matrices $Q$ and $R$, we say that the data $(U_{-},X)$ are *informative for linear quadratic regulation* if there exists $K$ such that $\Sigma_{i/s} \subseteq \Sigma_{K}^{Q,R}$.

In order to provide necessary and sufficient conditions for the corresponding informativity problem, we need the following auxiliary lemma.

### Lemma 25

Let $Q = Q^{\top}$ be positive semidefinite and $R = R^{\top}$ be positive definite. Suppose the data $(U_{-},X)$ are informative for linear quadratic regulation. Let $K$ be such that $\Sigma_{i/s} \subseteq \Sigma_{K}^{Q,R}$. Then, there exist a square matrix $M$ and a symmetric positive semidefinite matrix $P^{+}$ such that for all ${(A,B)} \in \Sigma_{i/s}$ Proof. Since the data $(U_{-},X)$ are informative for linear quadratic regulation, $A + {BK}$ is stable for every ${(A,B)} \in \Sigma_{i/s}$. By Lemma 15, this implies that ${A_{0} + {B_{0}K}} = 0$ for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. Thus, there exists $M$ such that $M = {A + {BK}}$ for all ${(A,B)} \in \Sigma_{i/s}$. For the rest, note that Theorem 23 implies that for every ${(A,B)} \in \Sigma_{i/s}$ there exists $P_{(A,B)}^{+}$ satisfying the DARE It is important to note that, although $K$ is independent of the choice of $(A,B)$, the matrix $P_{(A,B)}^{+}$ might depend on $(A,B)$. We will, however, show that also $P_{(A,B)}^{+}$ is independent of the choice of $(A,B)$.

By rewriting, we see that Since $M$ is stable, $P_{(A,B)}^{+}$ is the unique solution to the discrete-time Lyapunov equation, see e.g. \[46, Section 6\]. Moreover, since $M$ and $K$ do not depend on the choice of ${(A,B)} \in \Sigma_{i/s}$, it indeed follows that $P_{(A,B)}^{+}$ does not depend on $(A,B)$. It follows from -- that $P^{+}:=P_{(A,B)}^{+}$ satisfies --. $\blacksquare$ The following theorem solves the informativity problem for linear quadratic regulation.

### Theorem 26

Let $Q = Q^{\top}$ be positive semidefinite and $R = R^{\top}$ be positive definite. Then, the data $(U_{-},X)$ are informative for linear quadratic regulation if and only if at least one of the following two conditions hold: The data $(U_{-},X)$ are informative for system identification, that is, $\Sigma_{i/s} = {\{{(A_{s},B_{s})}\}}$, and the linear quadratic regulator problem is solvable for $(A_{s},B_{s},Q,R)$. In this case, the optimal feedback gain $K$ is of the form where $P^{+}$ is the largest real symmetric solution to.

For all ${(A,B)} \in \Sigma_{i/s}$ we have $A = A_{s}$. Moreover, $A_{s}$ is stable, ${QA_{s}} = 0$, and the optimal feedback gain is given by $K = 0$.

### Remark 27

Condition (ii) of Theorem 26 is a pathological case in which $A$ is stable and ${QA} = 0$ for all matrices $A$ that are compatible with the data. Since ${x{(t)}} \in {{im}A}$ for all $t > 0$, we have ${Qx{(t)}} = 0$ for all $t > 0$ if the input function is chosen as $u = 0$. Additionally, since $A$ is stable, this shows that the optimal input is equal to $u^{\ast} = 0$. If we set aside condition (ii), the implication of Theorem 26 is the following: if the data are informative for linear quadratic regulation they are also informative for system identification.

At first sight, this might seem like a negative result in the sense that data-driven LQR is only possible with data that are also informative enough to uniquely identify the system. However, at the same time, Theorem 26 can be viewed as a positive result in the sense that it provides fundamental justification for the data conditions imposed in e.g.. Indeed, in the data-driven infinite horizon LQR problem^33^3Note that the authors of formulate this problem as the minimization of the $H_{2}$-norm of a certain transfer matrix. is solved using input/state data under the assumption that the input is persistently exciting of sufficiently high order. Under the latter assumption, the input/state data are informative for system identification, i.e., the matrices $A_{s}$ and $B_{s}$ can be uniquely determined from data. Theorem 26 justifies such a strong assumption on the richness of data in data-driven linear quadratic regulation.

The data-driven *finite* horizon LQR problem was solved under a persistency of excitation assumption . Our results suggest that also in this case informativity for system identification is necessary for data-driven LQR, although further analysis is required to prove this claim.

Proof of Theorem 26. We first prove the 'if' part. Sufficiency of the condition (i) readily follows from Theorem 23. To prove the sufficiency of the condition (ii), assume that the matrix $A$ is stable and ${QA} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. By the discussion following Theorem 26, this implies that $u^{\ast} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. Hence, for $K = 0$ we have $\Sigma_{i/s} \subseteq \Sigma_{K}^{Q,R}$, i.e., the data are informative for linear quadratic regulation.

To prove the 'only if' part, suppose that the data $(U_{-},X)$ are informative for linear quadratic regulation. From Lemma 25, we know that there exist $M$ and $P^{+}$ satisfying -- for all ${(A,B)} \in \Sigma_{i/s}$. By substituting into and using, we obtain In addition, it follows from that ${- {{({R + {B^{\top}P^{+}B}})}K}} = {B^{\top}P^{+}A}$. By using, we have Since and hold for all ${(A,B)} \in \Sigma_{i/s}$, we have that for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. Note that ${({FA_{0}},{FB_{0}})} \in \Sigma_{i/s}^{0}$ for all $F \in {\mathbb{R}}^{n \times n}$ whenever ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$. This means that for all $F \in {\mathbb{R}}^{n \times n}$. Therefore, either $\begin{bmatrix} \end{bmatrix} = 0$ for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$ or ${P^{+}M} = 0$. The former is equivalent to $\Sigma_{i/s}^{0} = {\{ 0\}}$. In this case, we see that the data $(U_{-},X)$ are informative for system identification, equivalently $\Sigma_{i/s} = {\{{(A_{s},B_{s})}\}}$, and the LQR problem is solvable for $(A_{s},B_{s},Q,R)$. Therefore, condition (i) holds. On the other hand, if ${P^{+}M} = 0$ then we have for all ${(A,B)} \in \Sigma_{i/s}$. From the identity we see that ${P^{+}A} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. Then, it follows from that $K = 0$. Since ${A_{0} + {B_{0}K}} = 0$ for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$ due to Lemma 15, we see that $A_{0}$ must be zero. Hence, we have $A = A_{s}$ for all ${(A,B)} \in \Sigma_{i/s}$ and $A_{s}$ is stable. Moreover, it follows from that $P^{+} = Q$. Therefore, ${QA_{s}} = 0$. In other words, condition (ii) is satisfied, which proves the theorem. $\blacksquare$ Theorem 26 gives necessary and sufficient conditions under which the data are informative for linear quadratic regulation. However, it might not be directly clear how these conditions can be verified given input/state data. Therefore, in what follows we rephrase the conditions of Theorem 26 in terms of the data matrices $X$ and $U_{-}$.

### Theorem 28

Let $Q = Q^{\top}$ be positive semidefinite and $R = R^{\top}$ be positive definite. Then, the data $(U_{-},X)$ are informative for linear quadratic regulation if and only if at least one of the following two conditions hold: The data $(U_{-},X)$ are informative for system identification. Equivalently, there exists $\begin{bmatrix} \end{bmatrix}$ such that holds. Moreover, the linear quadratic regulator problem is solvable for $(A_{s},B_{s},Q,R)$, where $A_{s} = {X_{+}V_{1}}$ and $B_{s} = {X_{+}V_{2}}$.

There exists $\Theta \in {\mathbb{R}}^{T \times n}$ such that ${X_{-}\Theta} = {({X_{-}\Theta})}^{\top}$, ${U_{-}\Theta} = 0$, Proof. The equivalence of condition (i) of Theorem 26 and condition (i) of Theorem 28 is obvious. It remains to be shown that condition (ii) of Theorem 26 and condition (ii) of Theorem 28 are equivalent as well. To this end, suppose that there exists a matrix $\Theta \in {\mathbb{R}}^{T \times n}$ such that the conditions of (ii) holds. By Theorem 17, we have $\Sigma_{i/s} \subseteq \Sigma_{K}$ for $K = 0$, that is, $A$ is stable for all ${(A,B)} \in \Sigma_{i/s}$. In addition, note that for all ${(A,B)} \in \Sigma_{i/s}$. This shows that ${QA} = 0$ and therefore that condition (ii) of Theorem 26 holds. Conversely, suppose that $A$ is stable and ${QA} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. This implies that $K = 0$ is a stabilizing controller for all ${(A,B)} \in \Sigma_{i/s}$. By Theorem 17, there exists a matrix $\Theta \in {\mathbb{R}}^{T \times n}$ satisfying the first three conditions of (ii). Finally, it follows from ${QA} = 0$ and that $\Theta$ also satisfies the fourth equation of (ii). This proves the theorem. $\blacksquare$

### IV-C From data to LQ gain

In this section our goal is to devise a method in order to compute the optimal feedback gain $K$ directly from the data. For this, we will employ ideas from the study of Riccati inequalities (see e.g ).

The following theorem asserts that $P^{+}$ as in Lemma 25 can be found as the unique solution to an optimization problem involving only the data. Furthermore, the optimal feedback gain $K$ can subsequently be found by solving a set of linear equations.

### Theorem 29

Let $Q = Q^{\top} \geqslant 0$ and $R = R^{\top} > 0$. Suppose that the data $(U_{-},X)$ are informative for linear quadratic regulation. Consider the linear operator $P\mapsto{\mathcal{L}{(P)}}$ defined by Let $P^{+}$ be as in Lemma 25. The following statements hold: The matrix $P^{+}$ is equal to the unique solution to the optimization problem There exists a right inverse $X_{-}^{\dagger}$ of $X_{-}$ such that Moreover, if $X_{-}^{\dagger}$ satisfies, then the optimal feedback gain is given by $K = {U_{-}X_{-}^{\dagger}}$.

### Remark 30

From a design viewpoint, the optimal feedback gain $K$ can be found in the following way. First solve the semidefinite program in Theorem 29(i). Subsequently, compute a solution $X_{-}^{\dagger}$ to the linear equations ${X_{-}X_{-}^{\dagger}} = I$ and. Then, the optimal feedback gain is given by $K = {U_{-}X_{-}^{\dagger}}$.

### Remark 31

The data-driven LQR problem was first solved using semidefinite programming in \[40, Theorem 4\]. There, the optimal feedback gain was found by minimizing the trace of a weighted sum of two matrix variables, subject to two LMI constraints. The semidefinite program in Theorem 29 is attractive since the dimension of the unknown $P$ is (only) $n \times n$. In comparison, the dimensions of the two unknowns in \[40, Theorem 4\] are $T \times n$ and $m \times m$, respectively. In general, the number of samples $T$ is much larger^44^4In fact, this is always the case under the persistency of excitation conditions imposed in as such conditions can only be satisfied provided that $T \geqslant {{nm} + n + m}$. than $n$. An additional attractive feature of Theorem 29 is that $P^{+}$ is obtained from the data. This is useful since the minimal cost associated to any initial condition $x_{0}$ can be computed as $x_{0}^{\top}P^{+}x_{0}$.

The data-driven LQR approach in is quite different from Theorem 29 since the solution to the Riccati equation is approximated using a batch-form solution to the *Riccati difference equation*. A similar approach was used in for the *finite horizon* data-driven LQR/LQG problem. In the setup of, the approximate solution to the Riccati equation is exact only if the number of data points tends to infinity. The main difference between our approach and the one in is hence that the solution $P^{+}$ to the Riccati equation can be obtained exactly from *finite* data via Theorem 29.

Proof of Theorem 29. We begin with proving the first statement. Note that for all ${(A,B)} \in \Sigma_{i/s}$. We claim that the following implication holds: To prove this claim, let $P$ be such that $P = P^{\top} \geqslant 0$ and ${\mathcal{L}{(P)}} \leqslant 0$. Since the data are informative for linear quadratic regulation, they are also informative for stabilization by state feedback. Therefore, the optimal feedback gain $K$ satisfies due to Lemma 15. Therefore, the above expression for $\mathcal{L}{(P)}$ implies that for all ${(A,B)} \in \Sigma_{i/s}$. This yields where $M$ is as in Lemma 25. By subtracting this, we obtain Since $M$ is stable, this discrete-time Lyapunov inequality implies that ${P^{+} - P} \geqslant 0$ and hence $P^{+} \geqslant P$. This proves the claim.

Note that $R + {B^{\top}P^{+}B}$ is positive definite. Then, it follows from that via a Schur complement argument. Therefore, ${\mathcal{L}{(P^{+})}} \leqslant 0$. Since $P^{+} \geqslant P$, we have ${{tr}P^{+}} \geqslant {{tr}P}$. Together, this shows that $P^{+}$ is a solution to the optimization problem stated in the theorem.

Next, we prove uniqueness. Let $\overline{P}$ be another solution of the optimization problem. Then, we have that $\overline{P} = {\overline{P}}^{\top} \geqslant 0$, ${\mathcal{L}{(\overline{P})}} \leqslant 0$, and ${{tr}\overline{P}} = {{tr}P^{+}}$. From, we see that $P^{+} \geqslant \overline{P}$. In particular, this implies that ${(P^{+})}_{ii} \geqslant {\overline{P}}_{ii}$ for all $i$. Together with ${{tr}\overline{P}} = {{tr}P^{+}}$, this implies that ${(P^{+})}_{ii} = {\overline{P}}_{ii}$ for all $i$. Now, for any $i$ and $j$, we have where $e_{i}$ denotes the $i$-th standard basis vector. This leads to ${(P^{+})}_{ij} \leqslant {\overline{P}}_{ij}$ and ${(P^{+})}_{ij} \geqslant {\overline{P}}_{ij}$, respectively. We conclude that ${(P^{+})}_{ij} = {\overline{P}}_{ij}$ for all $i,j$. This proves uniqueness.

Finally, we prove the second statement. It follows from and that The optimal feedback $K$ is stabilizing, therefore it follows from Theorem 16 that $K$ can be written as $K = {U_{-}\Gamma}$, where $\Gamma$ is some right inverse of $X_{-}$. Note that this implies the existence of a right inverse $X_{-}^{\dagger}$ of $X_{-}$ satisfying. Indeed, $X_{-}^{\dagger}:=\Gamma$ is such a matrix. Moreover, if $X_{-}^{\dagger}$ is a right inverse of $X_{-}$ satisfying then ${{({U_{-} - {KX_{-}}})}X_{-}^{\dagger}} = 0$ by and positive definiteness of $R$. We conclude that the optimal feedback gain is equal to $K = {U_{-}X_{-}^{\dagger}}$, which proves the second statement. $\blacksquare$

## Control using input and output data

In this section, we will consider problems where the output does play a role. In particular, we will consider the problem of stabilization by dynamic measurement feedback. We will first consider this problem based on input, state and output measurements. Subsequently, we will turn our attention to the case of input/output data.

Consider the 'true' system We want to design a stabilizing dynamic controller of the form such that the closed-loop system, given by is stable. This is equivalent to the condition that

### V-A Stabilization using input, state and output data

Suppose that we collect input/state/output data on $\ell$ time intervals $\{ 0,1,\ldots,T_{i}\}$ for $i = {1,2,\ldots,q}$. Let ${U_{-},X,X_{-}},$ and $X_{+}$ be defined as in and let $Y_{-}$ be defined in a similar way as $U_{-}$. Then, we have relating the data and the 'true' system. The set of all systems that are consistent with these data is then given: In addition, for given $K$, $L$ and $M$, we define the set of systems that are stabilized by the dynamic controller by Subsequently, in line with Definition 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"), we consider the following notion of informativity:

### Definition 32

We say the data $(U_{-},X,Y_{-})$ are *informative for stabilization by dynamic measurement feedback* if there exist matrices $K$, $L$ and $M$ such that $\Sigma_{i/s/o} \subseteq \Sigma_{K,L,M}$.

As in the general case of informativity for control, we consider two consequent problems: First, to characterize informativity for stabilization in terms of necessary and sufficient conditions on the data and next to design a controller based on these data. To aid in solving these problems, we will first investigate the case where $U_{-}$ does not have full row rank. In this case, we will show that the problem can be 'reduced' to the full row rank case.

For this, we start with the observation that any $U_{-} \in {\mathbb{R}}^{m \times T}$ of row rank $k < m$ can be decomposed as $U_{-} = {S{\hat{U}}_{-}}$, where $S$ has full column rank and ${\hat{U}}_{-} \in {\mathbb{R}}^{k \times T}$ has full row rank. We now have the following lemma:

### Lemma 33

Consider the data $(U_{-},X,Y_{-})$ and the corresponding set $\Sigma_{i/s/o}$. Let $S$ be a matrix of full column rank such that $U_{-} = {S{\hat{U}}_{-}}$ with ${\hat{U}}_{-}$ a matrix of full row rank. Let $S^{\dagger}$ be a left inverse of $S$.

Then the data $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback if and only if the data $({\hat{U}}_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback.

In particular, if we let ${\hat{\Sigma}}_{i/s/o}$ be the set of systems consistent with the 'reduced' data set $({\hat{U}}_{-},X,Y_{-})$, and if $\hat{K}$ $\hat{L}$ and $\hat{M}$ are real matrices of appropriate dimensions, then: Proof. First note that We will start by proving the following two implications: To prove implication, assume that ${(A,B,C,D)} \in \Sigma_{i/s/o}$. Then, by definition From the definition of $S$, we have $U_{-} = {S{\hat{U}}_{-}}$. Substitution of this results in This implies that ${(A,{BS},C,{DS})} \in {\hat{\Sigma}}_{i/s/o}$. The implication can be proven similarly by substitution of ${\hat{U}}_{-} = {S^{\dagger}U_{-}}$.

To prove the lemma, suppose that the data $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback. This means that there exist $K$, $L$, and $M$ such that is stable for all ${(A,B,C,D)} \in \Sigma_{i/s/o}$. In particular, if ${(\hat{A},\hat{B},\hat{C},\hat{D})} \in {\hat{\Sigma}}_{i/s/o}$ then ${(\hat{A},{\hat{B}S^{\dagger}},\hat{C},{\hat{D}S^{\dagger}})} \in \Sigma_{i/s/o}$. This means that the matrix is stable for all ${(\hat{A},\hat{B},\hat{C},\hat{D})} \in {\hat{\Sigma}}_{i/s/o}$. In other words, ${\hat{\Sigma}}_{i/s/o} \subseteq \Sigma_{K,L,{S^{\dagger}M}}$ and hence implication holds and the data $({\hat{U}}_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback. The proofs of and the 'if' part of the theorem are analogous and hence omitted. $\blacksquare$ We will now solve the informativity and design problems under the condition that $U_{-}$ has full row rank.

### Theorem 34

Consider the data $(U_{-},X,Y_{-})$ and assume that $U_{-}$ has full row rank. Then $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback if and only if the following conditions are satisfied: Equivalently, there exists $\begin{bmatrix} \end{bmatrix}$ such that holds. This means that The pair $({X_{+}V_{1}},{X_{+}V_{2}})$ is stabilizable and $({Y_{-}V_{1}},{X_{+}V_{1}})$ is detectable.

Moreover, if the above conditions are satisfied, a stabilizing controller $(K,L,M)$ can be constructed as follows: Select a matrix $M$ such that $X_{+}{({V_{1} + {V_{2}M}})}$ is stable.

Choose a matrix $L$ such that ${({X_{+} - {LY_{-}}})}V_{1}$ is stable.

### Remark 35

Under the condition that $U_{-}$ has full row rank, Theorem 34 asserts that in order to construct a stabilizing dynamic controller, it is necessary that the data are rich enough to identify the system matrices $A_{s},B_{s},C_{s}$ and $D_{s}$ uniquely. The controller proposed in (a), (b), (c) is a so-called *observer-based* controller, see e.g. \[45, Section 3.12\]. The feedback gains $M$ and $L$ can be computed using standard methods, for example via pole placement or LMI's.

Proof of Theorem 34. To prove the 'if' part, suppose that conditions (i) and (ii) are satisfied. This implies the existence of the matrices $(K,L,M)$ as defined in items (a), (b) and (c). We will now show that these matrices indeed constitute a stabilizing controller. Note that by condition (i), $\Sigma_{i/s/o} = {\{{(A_{s},B_{s},C_{s},D_{s})}\}}$ with By definition of $K$, $L$ and $M$, the matrices $A_{s} + {B_{s}M}$ and $A_{s} - {LC_{s}}$ are stable and $K = {{A_{s} + {B_{s}M}} - {LC_{s}} - {LD_{s}M}}$. This implies that is stable since the matrices are similar \[45, Section 3.12\]. We conclude that $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback and that the recipe given by (a), (b) and (c) leads to a stabilizing controller $(K,L,M)$.

It remains to prove the 'only if' part. To this end, suppose that the data $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback. Let $(K,L,M)$ be such that $\Sigma_{i/s/o} \subseteq \Sigma_{K,L,M}$. This means that is stable for all ${(A,B,C,D)} \in \Sigma_{i/s/o}$. Let $\zeta \in {\mathbb{R}}^{n}$ and $\eta \in {\mathbb{R}}^{m}$ be such that Note that ${({A + {\zeta\zeta^{\top}}},{B + {\zeta\eta^{\top}}},C,D)} \in \Sigma_{i/s/o}$ if ${(A,B,C,D)} \in \Sigma_{i/s/o}$. Therefore, the matrix is stable for all $\alpha \in {\mathbb{R}}$. We conclude that the spectral radius of the matrix is smaller than $1/\alpha$. By taking the limit as $\alpha\rightarrow\infty$, we see that the spectral radius of $\zeta\zeta^{\top}$ must be zero due to the continuity of spectral radius. Therefore, $\zeta$ must be zero. Since $U_{-}$ has full column rank, we can conclude that $\eta$ must be zero too. This proves that condition (i) and therefore $\Sigma_{i/s/o} = {\{{(A_{s},B_{s},C_{s},D_{s})}\}}$. Since the controller $(K,L,M)$ stabilizes $(A_{s},B_{s},C_{s},D_{s})$, the pair $(A_{s},B_{s})$ is stabilizable and $(C_{s},A_{s})$ is detectable. By we conclude that condition (ii) is also satisfied. This proves the theorem. $\blacksquare$ The following corollary follows from Lemma 33 and Theorem 34 and gives necessary and sufficient conditions for informativity for stabilization by dynamic measurement feedback. Note that we do not make any a priori assumptions on the rank of $U_{-}$.

### Corollary 36

Let $S$ be any full column rank matrix such that $U_{-} = {S{\hat{U}}_{-}}$ with ${\hat{U}}_{-}$ full row rank $k$. The data $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback if and only if the following two conditions are satisfied: Equivalently, there exists a matrix $\begin{bmatrix} \end{bmatrix}$ such that The pair $({X_{+}V_{1}},{X_{+}V_{2}})$ is stabilizable and $({Y_{-}V_{1}},{X_{+}V_{1}})$ is detectable.

Moreover, if the above conditions are satisfied, a stabilizing controller $(K,L,M)$ is constructed as follows: Select a matrix $\hat{M}$ such that $X_{+}{({V_{1} + {V_{2}\hat{M}}})}$ is stable. Define $M:={S\hat{M}}$.

Choose a matrix $L$ such that ${({X_{+} - {LY_{-}}})}V_{1}$ is stable.

### Remark 37

In the previous corollary it is clear that the system matrices of the data-generating system are related to the data via Therefore the corollary shows that informativity for stabilization by dynamic measurement feedback requires that $A_{s}$ and $C_{s}$ can be identified uniquely from the data. However, this does not hold for $B_{s}$ and $D_{s}$ in general.

### V-B Stabilization using input and output data

Recall that we consider a system of the form. When given input, state and output data, any system $(A,B,C,D)$ consistent with these data satisfies In this section, we will consider the situation where we have access to input and output measurements only. Moreover, we assume that the data are collected on a single time interval, i.e. $q = 1$. This means that our data are of the form $(U_{-},Y_{-})$, where Again, we are interested in informativity of the data, this time given by $(U_{-},Y_{-})$. Therefore we wish to consider the set of all systems of the form with the state space dimension^55^5The state space dimension of the system may be known a priori. In the case that it is not, it can be computed using subspace identification methods, see e.g. \[2, Theorem 2\]. $n$ that admit the same input/output data. This leads to the following set of consistent systems: As in the previous section, we wish to find a controller of the form that stabilizes the system. This means that, in line with Definition 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"), we have the following notion of informativity:

### Definition 38

We say the data $(U_{-},Y_{-})$ are *informative for stabilization by dynamic measurement feedback* if there exist matrices $K$, $L$ and $M$ such that $\Sigma_{i/o} \subseteq \Sigma_{K,L,M}$.

In order to obtain conditions under which $(U_{-},Y_{-})$ are informative for stabilization, it may be tempting to follow the same steps as in Section V-A. In that section we first proved that we can assume without loss of generality that $U_{-}$ has full row rank. Subsequently, Theorem 34 and Corollary 36 characterize informativity for stabilization by dynamic measurement feedback based on input, state and output data. It turns out that we can perform the first of these two steps for input/output data as well. Indeed, in line with Lemma 33, we can state the following:

### Lemma 39

Consider the data $(U_{-},Y_{-})$ and the corresponding set $\Sigma_{i/o}$. Let $S$ be a matrix of full column rank such that $U_{-} = {S{\hat{U}}_{-}}$ with ${\hat{U}}_{-}$ a matrix of full row rank.

Then the data $(U_{-},Y_{-})$ are informative for stabilization by dynamic measurement feedback if and only if the data $({\hat{U}}_{-},Y_{-})$ are informative for stabilization by dynamic measurement feedback.

The proof of this lemma is analogous to that of Lemma 33 and therefore omitted. Lemma 39 implies that without loss of generality we can consider the case where $U_{-}$ has full row rank.

In contrast to the first step, the second step in Section V-A relies heavily on the affine structure of the considered set $\Sigma_{i/s/o}$. Indeed, the proof of Theorem 34 makes use of the fact that $\Sigma_{i/s/o}^{0}$ is a subspace. However, the set $\Sigma_{i/o}$ is not an affine set. This means that it is not straightforward to extend the results of Corollary 36 to the case of input/output measurements.

Nonetheless, under certain conditions on the input/output data it is possible to construct the corresponding state sequence $X$ of up to similarity transformation. In fact, state reconstruction is one of the main themes of subspace identification, see e.g.. The construction of a state sequence would allow us to reduce the problem of stabilization using input/output data to that with input, state and output data. The following result gives sufficient conditions on the data $(U_{-},Y_{-})$ for state construction.

To state the result, we will first require a few standard pieces of notation. First, let ${f{}},\ldots,{f{({T - 1})}}$ be a signal and $\ell < T$, then we define the Hankel matrix of depth $\ell$ as Given input and output data of the form, and $k$ such that ${2k} < T$ we consider $\mathcal{H}_{2k}{(u)}$ and $\mathcal{H}_{2k}{(y)}$. Next, we partition our data into so-called 'past' and 'future' data as where $U_{p},U_{f},Y_{p}$ and $Y_{f}$ all have $k$ block rows. Let ${x{}},\ldots,{x{(T)}}$ denote the state trajectory of compatible with a given $(U_{-},Y_{-})$. We now denote Lastly, let ${rs}{(M)}$ denote the row space of the matrix $M$. Now we have the following result, which is a rephrasing of \[48, Theorem 3\].

### Theorem 40

Consider the system and assume it is minimal. Let the input/output data $(U_{-},Y_{-})$ be as. Assume that $k$ is such that $n < k < {\frac{1}{2}T}$. If and this row space is of dimension $n$.

Under the conditions of this theorem, we can now find the 'true' state sequence $X_{f}$ up to similarity transformation. That is, we can find $\overline{X} = {SX_{f}}$ for some unknown invertible matrix $S$. This means that, under these conditions, we obtain an input/state/output trajectory given by the matrices We can now state the following sufficient condition for informativity for stabilization with input/output data.

### Corollary 41

Consider the system and assume it is minimal. Let the input/output data $(U_{-},Y_{-})$ be as. Assume that $k$ is such that $n < k < {\frac{1}{2}T}$. Then the data $(U_{-},Y_{-})$ are informative for stabilization by dynamic measurement feedback if the following two conditions are satisfied: The rank condition holds.

The data $({\overline{U}}_{-},\overline{X},{\overline{Y}}_{-})$, as defined , are informative for stabilization by dynamic measurement feedback.

Moreover, if these conditions are satisfied, a stabilizing controller $(K,L,M)$ such that $\Sigma_{i/o} \subseteq \Sigma_{K,L,M}$ can be found by applying Corollary 36 (a),(b),(c) to the data $({\overline{U}}_{-},\overline{X},{\overline{Y}}_{-})$.

The conditions provided in Corollary 41 are sufficient, but not necessary for informativity for stabilization by dynamic measurement feedback. In addition, it can be shown that data satisfying these conditions are also informative for system identification, in the sense that $\Sigma_{i/o}$ contains only the 'true' system and all systems similar to it.

An interesting question is whether the conditions of Corollary 41 can be sharpened to necessary and sufficient conditions. In this case it would be of interest to investigate whether such conditions are weaker than those for informativity for system identification.

At this moment, we do not have a conclusive answer to the above question. However, we note that even for subspace identification there are no known necessary and sufficient conditions for data to be informative, although several sufficient conditions exist, e.g. \[48, Theorems 3 and 5\], \[2, Theorem 2\] and \[49, Theorems 3 and 4\].

## Conclusions and future work

Results in data-driven control should clearly highlight the differences and possible advantages as compared to system identification paired with model-based control. One clear advantage of data-driven control is its capability of solving problems in the presence of data that are not informative for system identification. Therefore, informativity is a very important concept for data-driven analysis and control.

In this paper we have introduced a comprehensive framework for studying informativity problems. We have applied this framework to analyze several system-theoretic properties on the basis of data. The same framework was used to solve multiple data-driven control problems.

After solving these problems, we have made the comparison between our data-driven methods, and the 'classical' combination of identification and model-based control. We have shown that for many analysis and control problems, such as controllability analysis and stabilization, the data-driven approach can indeed be performed on data that are not informative for system identification. On the other hand, for data-driven linear quadratic regulation it has been shown that informativity for system identification is a necessary condition. This effectively means that for this data-driven control problem, we have given a theoretic justification for the use of persistently exciting data.

### Future work

Due to the generality of the introduced framework, many different problems can be studied in a similar fashion: one could consider different types of data, where more results based on only input and output data would be particularly interesting. Many other system-theoretic properties could be considered as well, for example, analyzing passivity or tackling robust control problems based on data.

It would also be of interest to generalize the model class under consideration. One could, for instance, consider larger classes of systems like differential algebraic or polynomial systems. On the other hand, the class under consideration can also be made smaller by prior knowledge of the system. For example, the system might have an observed network structure, or could in general be parametrized.

A framework similar to ours could be employed in the presence of disturbances, which is a problem of practical interest. A study of data-driven control problems in this situation is particularly interesting, because system identification is less straightforward. We note that data-driven stabilization under measurement noise has been studied in and under unknown disturbances . Additionally, the data-driven LQR problem is popular in the machine learning community, where it is typically assumed that the system is influenced by (Gaussian) process noise, see e.g..

In this paper, we have assumed that the data are given. Yet another problem of practical interest is that of experiment design, where inputs need to be chosen such that the resulting data are informative. In system identification, this problem led to the notion of persistence of excitation. For example, it is shown in that the rank condition can be imposed by injecting an input sequence that is persistently exciting of order $n + 1$. However, as we have shown, this rank condition is not necessary for some data-driven control problems, like stabilization by state feedback. The question therefore arises whether we can find tailor-made conditions on the input only, that guarantee informativity for data-driven control.
