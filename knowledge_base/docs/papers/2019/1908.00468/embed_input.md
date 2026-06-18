<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data Informativity: A New Perspective on Data-Driven Analysis and Control

Topics include Data informativity, Data-driven control, Behavioral systems, Persistency of excitation, System analysis, Stabilization, Model uncertainty, Direct control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Establishes the informativity framework: data are judged by whether all systems consistent with the data satisfy a property or admit a controller, not by whether the data uniquely identify a model. This reframing separates direct data-driven control from system identification and explains when persistency of excitation is stronger than necessary.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The use of persistently exciting data has recently been popularized in the context of data-driven analysis and control. Such data have been used to assess system theoretic properties and to construct control laws, without using a system model. Persistency of excitation is a strong condition that also allows unique identification of the underlying dynamical system from the data within a given model class. In this paper, we develop a new framework in order to work with data that are not necessarily persistently exciting. Within this framework, we investigate necessary and sufficient conditions on the informativity of data for several data-driven analysis and control problems. For certain analysis and design problems, our results reveal that persistency of excitation is not necessary. In fact, in these cases data-driven analysis/control is possible while the combination of (unique) system identification and model-based control is not. For certain other control problems, our results justify the use of persistently exciting data as data-driven control is possible only with data that are informative for system identification.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the main paradigms in the field of systems and control is that of *model-based* control. Indeed, many control design techniques rely on a system model, represented by e.g. a state-space system or transfer function. In practice, system models are rarely known a priori and have to be identified from measured data using system identification methods such as prediction error or subspace identification. As a consequence, the use of model-based control techniques inherently leads to a two-step control procedure consisting of system identification followed by control design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, *data-driven* control aims to bypass this two-step procedure by constructing controllers directly from data, without (explicitly) identifying a system model. This direct approach is not only attractive from a conceptual point of view but can also be useful in situations where system identification is difficult or even impossible because the data do not give sufficient information.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first contribution to data-driven control is often attributed to Ziegler and Nichols for their work on tuning PID controllers. Adaptive control, iterative feedback tuning and unfalsified control can also be regarded as classical data-driven control techniques. More recently, the problem of finding optimal controllers from data has received considerable attention. The proposed solutions to this problem are quite varied, ranging from the use of batch-form Riccati equations to approaches that apply reinforcement learning. Additional noteworthy data-driven control problems include predictive control, model reference control and (intelligent) PID control. For more references and classifications of data-driven control techniques, we refer to the survey.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition to control problems, also *analysis* problems have been studied within a data-based framework. The authors of analyze the stability of an input/output system using time series data. The papers deal with data-based controllability and observability analysis. Moreover, the problem of verifying dissipativity on the basis of measured system trajectories has been studied.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A result that is becoming increasingly popular in the study of data-driven problems is the so-called *fundamental lemma* by Willems and coworkers. This result roughly states that all possible trajectories of a linear time-invariant system can be obtained from any given trajectory whose input component is persistently exciting. The fundamental lemma has clear implications for system identification. Indeed, it provides criteria under which the data are sufficiently informative to uniquely identify the system model within a given model class. In addition, the result has also been applied to data-driven control problems. The idea is that control laws can be obtained directly from data, with the underlying mechanism that the system is represented implicitly by the so-called Hankel matrix of a measured trajectory. This framework has led to several interesting control strategies, first in a behavioral setting, and more recently in the context of state-space systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above approaches all use persistently exciting data in the control design, meaning that one could (hypothetically) identify the system model from the same data. An intriguing question is therefore the following: is it possible to obtain a controller from data that are *not* informative enough to uniquely identify the system? An affirmative answer would be remarkable, since it would highlight situations in which data-driven control is more powerful than the combination of system identification and model-based control. On the other hand, a negative answer would also be significant, as it would give a theoretic justification for the use of persistently exciting data for data-driven analysis and control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the above question, this paper introduces a general framework to study data informativity problems for data-driven analysis and control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by the concept of data informativity in system identification, we introduce a general notion of informativity for data-driven analysis and control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the data-driven analysis of several system theoretic properties like stability, stabilizability and controllability. For each of these problems, we provide necessary and sufficient conditions under which the data are informative for this property, i.e., conditions required to ascertain the system's property from data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study data-driven control problems such as stabilization by state feedback, stabilization by dynamic measurement feedback, deadbeat control and linear quadratic regulation. In each of the cases, we give conditions under which the data are informative for controller design.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

For each of the studied control problems, we develop methods to compute a controller from data, assuming that the informativity conditions are satisfied.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work has multiple noteworthy implications. First of all, we show that for problems like stabilization by state feedback, the corresponding informativity conditions on the data are *weaker* than those for system identification. This implies that a stabilizing feedback can be obtained from data that are not sufficiently informative to uniquely identify the system.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, for problems such as linear quadratic regulation (LQR), we show that the informativity conditions are essentially the same as for system identification. Therefore, our results provide a theoretic justification for imposing the strong persistency of excitation conditions in prior work on the LQR problem, such as and.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. In Section II we introduce the problem at a conceptual level. Subsequently, in Section III we provide data informativity conditions for controllability and stabilizability. Section IV deals with data-driven control problems with input/state data. Next, Section V discusses control problems where ouput data plays a role. Finally, Section VI contains our conclusions and suggestions for future work.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In this section we will first introduce the informativity framework for data-driven analysis and control in a fairly abstract manner.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Let $\Sigma$ be a model class, i.e. a given set of systems containing the 'true' system denoted by $\mathcal{S}$. We assume that the 'true' system $\mathcal{S}$ is not known but that we have access to a set of data, $\mathcal{D}$, which are generated by this system. In this paper we are interested in assessing system-theoretic properties of $\mathcal{S}$ and designing control laws for it from the data $\mathcal{D}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Given the data $\mathcal{D}$, we define $\Sigma_{\mathcal{D}} \subseteq \Sigma$ to be the set of all systems that are consistent with the data $\mathcal{D}$, i.e. that could also have generated these data.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We first focus on data-driven analysis. Let $\mathcal{P}$ be a system-theoretic property. We will denote the set of all systems within $\Sigma$ having this property by $\Sigma_{\mathcal{P}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Now suppose we are interested in the question whether our 'true' system $\mathcal{S}$ has the property $\mathcal{P}$. As the only information we have to base our answer on are the data $\mathcal{D}$ obtained from the system, we can only conclude that the 'true' system has property $\mathcal{P}$ if all systems consistent with the data $\mathcal{D}$ have the property $\mathcal{P}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 2", "weight": 1.0} -->

For given $n$ and $m$, let $\Sigma$ be the set of all discrete-time linear input/state systems of the form

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 2", "weight": 1.0} -->

where $\mathbf{x}$ is the $n$-dimensional state and $\mathbf{u}$ is the $m$-dimensional input. Let the 'true' system $\mathcal{S}$ be represented by the matrices $(A_{s},B_{s})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 2", "weight": 1.0} -->

An example of a data set $\mathcal{D}$ arises when considering data-driven problems on the basis of input and state measurements. Suppose that we collect input/state data on $q$ time intervals $\{ 0,1,\ldots,T_{i}\}$ for $i = {1,2,\ldots,q}$. Let

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 2", "weight": 1.0} -->

denote the input and state data on the $i$-th interval. By defining

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 2", "weight": 1.0} -->

Suppose that we are interested in the system-theoretic property $\mathcal{P}$ of stabilizability. The corresponding set $\Sigma_{\mathcal{P}}$ is then equal to $\Sigma_{stab}$ defined by

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 2", "weight": 1.0} -->

Then, the data $(U_{-},X)$ are informative for stabilizability if $\Sigma_{(U_{-},X)} \subseteq \Sigma_{stab}$. That is, if all systems consistent with the input/state measurements are stabilizable.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 2", "weight": 1.0} -->

In general, if the 'true' system $\mathcal{S}$ can be uniquely determined from the data $\mathcal{D}$, that is $\Sigma_{\mathcal{D}} = {\{\mathcal{S}\}}$ and $\mathcal{S}$ has the property $\mathcal{P}$, then it is evident that the data $\mathcal{D}$ are informative for $\mathcal{P}$. However, the converse may not be true: $\Sigma_{\mathcal{D}}$ might contain many systems, all of which have property $\mathcal{P}$. This paper is interested in necessary and sufficient conditions for informativity of the data. Such conditions reveal the minimal amount of information required to assess the property $\mathcal{P}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 1 (Informativity problem)", "weight": 1.0} -->

Provide necessary and sufficient conditions on $\mathcal{D}$ under which the data are informative for property $\mathcal{P}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem 1 (Informativity problem)", "weight": 1.0} -->

The above gives us a general framework to deal with data-driven analysis problems. Such analysis problems will be the main focus of Section III.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem 1 (Informativity problem)", "weight": 1.0} -->

This paper also deals with data-driven control problems. The objective in such problems is the data-based design of controllers such that the closed loop system, obtained from the interconnection of the 'true' system $\mathcal{S}$ and the controller, has a specified property.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem 1 (Informativity problem)", "weight": 1.0} -->

As for the analysis problem, we have only the information from the data to base our design. Therefore, we can only guarantee our control objective if the designed controller imposes the specified property when interconnected with any system from the set $\Sigma_{\mathcal{D}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem 1 (Informativity problem)", "weight": 1.0} -->

For the framework to allow for data-driven control problems, we will consider a system-theoretic property $\mathcal{P}{(\mathcal{K})}$ that depends on a given controller $\mathcal{K}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 4", "weight": 1.0} -->

For systems and data like in Example 2, we can take the controller $\mathcal{K} = K \in {\mathbb{R}}^{m \times n}$ and the property ${\mathcal{P}{(\mathcal{K})}}:$ 'interconnection with the state feedback $K$ yields a stable closed loop system'. The corresponding set of systems $\Sigma_{\mathcal{P}{(\mathcal{K})}}$ is equal to $\Sigma_{K}$ defined by

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 4", "weight": 1.0} -->

The first step in any data-driven control problem is to determine whether it is possible to obtain a suitable controller from given data.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem 2 (Informativity problem for control)", "weight": 1.0} -->

Provide necessary and sufficient conditions on $\mathcal{D}$ under which there exists a controller $\mathcal{K}$ such that the data are informative for property $\mathcal{P}{(\mathcal{K})}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem 2 (Informativity problem for control)", "weight": 1.0} -->

The second step of data-driven control involves the design of a suitable controller.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

Under the assumption that the data $\mathcal{D}$ are informative for property $\mathcal{P}{( \cdot )}$, find a controller $\mathcal{K}$ such that $\Sigma_{\mathcal{D}} \subseteq \Sigma_{\mathcal{P}{(\mathcal{K})}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

As stated in the introduction, we will highlight the strength of this framework by solving multiple problems. We stress that throughout the paper it is assumed that the data are given and are not corrupted by noise.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data-driven analysis", "weight": 1.0} -->

In this section, we will study data-driven analysis of controllability and stabilizability given input and state measurements. As in Example 2, consider the discrete-time linear system

<!-- chunk {"id": "body-0042", "role": "body", "section": "Data-driven analysis", "weight": 1.0} -->

We will consider data consisting of input and state measurements. We define the matrices $U_{-}$ and $X$ as in (3a) and define $X_{-}$ and $X_{+}$ as in (3b). The set of all systems compatible with these data was introduced. In order to stress that we deal with input/state data, we rename it here as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Data-driven analysis", "weight": 1.0} -->

Note that the defining equation of is a system of linear equations in the unknowns $A$ and $B$. The solution space of the corresponding homogeneous equations is denoted by $\Sigma_{i/s}^{0}$ and is equal to

<!-- chunk {"id": "body-0044", "role": "body", "section": "Data-driven analysis", "weight": 1.0} -->

We consider the problem of data-driven analysis for systems of the form. If $(A_{s},B_{s})$ is the only system that explains the data, data-driven analysis could be performed by first identifying this system and then analyzing its properties. It is therefore of interest to know under which conditions there is only one system that explains the data.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Similar to the classical Hautus test, (11. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) and (12. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) can be verified by checking the rank for finitely many complex numbers $\lambda$. Indeed, (11. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) is equivalent to ${{rank}{(X_{+})}} = n$ and

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 9", "weight": 1.0} -->

for all $\lambda \neq 0$ with $\lambda^{- 1} \in {\sigma{({X_{-}X_{+}^{\dagger}})}}$, where $X_{+}^{\dagger}$ is any right inverse of $X_{+}$. Here, $\sigma{(M)}$ denotes the spectrum, i.e. set of eigenvalues of the matrix $M$. Similarly, (12. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control")) is equivalent to ${{rank}{({X_{+} - X_{-}})}} = n$ and

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 9", "weight": 1.0} -->

A noteworthy point to mention is that there are situations in which we can conclude controllability/stabilizability from the data without being able to identify the 'true' system uniquely, as illustrated next.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 10", "weight": 1.0} -->

Clearly, by Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control") we see that these data are informative for controllability, as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 10", "weight": 1.0} -->

As therefore all systems explaining the data are controllable, we conclude that the 'true' system is controllable. It is worthwhile to note that the data are not informative for system identification, as

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 10", "weight": 1.0} -->

Proof of Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control"). We will only prove the characterization of informativity for controllability. The proof for stabilizability uses very similar arguments, and is hence omitted.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 10", "weight": 1.0} -->

Suppose that the implication holds. Let ${(A,B)} \in \Sigma_{i/s}$ and suppose that ${z^{\ast}\begin{bmatrix}
\end{bmatrix}} = 0$. We want to prove that $z = 0$. Note that ${z^{\ast}\begin{bmatrix}
\end{bmatrix}} = 0$ implies that

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 10", "weight": 1.0} -->

or equivalently ${z^{\ast}X_{+}} = {\lambdaz^{\ast}X_{-}}$. This means that $z = 0$. We conclude that $(A,B)$ is controllable, i.e., $(U_{-},X)$ are informative for controllability.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 10", "weight": 1.0} -->

We now distinguish two cases, namely the case that $\lambda$ is real, and the case that $\lambda$ is complex. First suppose that $\lambda$ is real. Without loss of generality, $z$ is real. We want to prove that $z = 0$. Suppose on the contrary that $z \neq 0$ and ${z^{\top}z} = 1$. We define the (real) matrices

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example 10", "weight": 1.0} -->

In view of, we find that ${(\overline{A},\overline{B})} \in \Sigma_{i/s}$. Moreover,

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example 10", "weight": 1.0} -->

However, this is a contradiction as $(\overline{A},\overline{B})$ is controllable by the hypothesis that $(U_{-},X)$ are informative for controllability. We conclude that $z = 0$ which shows that holds for the case that $\lambda$ is real.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example 10", "weight": 1.0} -->

It suffices to prove now that $p$ and $q$ are linearly dependent. Suppose on the contrary that $p$ and $q$ are linearly independent. Since $\lambda$ is complex, $n \geqslant 2$. Therefore, by linear independence of $p$ and $q$ there exist ${\eta,\zeta} \in {\mathbb{R}}^{n}$ such that

<!-- chunk {"id": "body-0057", "role": "body", "section": "Example 10", "weight": 1.0} -->

We now define the real matrices $\overline{A}$ and $\overline{B}$ as

<!-- chunk {"id": "body-0058", "role": "body", "section": "Example 10", "weight": 1.0} -->

By we have ${(\overline{A},\overline{B})} \in \Sigma_{i/s}$. Next, we compute

<!-- chunk {"id": "body-0059", "role": "body", "section": "Example 10", "weight": 1.0} -->

This implies that ${z^{\ast}\begin{bmatrix}
{\overline{A} - {\lambdaI}} & \overline{B}
\end{bmatrix}} = 0$. Using the fact that $(\overline{A},\overline{B})$ is controllable, we conclude that $z = 0$. This is a contradiction with the fact that $p$ and $q$ are linearly independent. Thus $p$ and $q$ are linearly dependent and therefore implication holds. This proves the theorem. $\blacksquare$

<!-- chunk {"id": "body-0060", "role": "body", "section": "Example 10", "weight": 1.0} -->

In addition to controllability and stabilizability, we can also study the *stability* of an autonomous system of the form

<!-- chunk {"id": "body-0061", "role": "body", "section": "Example 10", "weight": 1.0} -->

To this end, let $X$ denote the matrix of state measurements obtained, as defined in (3a). The set of all autonomous systems compatible with these data is

<!-- chunk {"id": "body-0062", "role": "body", "section": "Example 10", "weight": 1.0} -->

Then, we say the data $X$ are *informative for stability* if any matrix $A \in \Sigma_{\text{s}}$ is stable, i.e. Schur. Using Theorem 8. ‣ III Data-driven analysis ‣ Data informativity: a new perspective on data-driven analysis and control") we can show that stability can only be concluded if the 'true' system can be uniquely identified.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Control using input and state data", "weight": 1.0} -->

In this section we will consider various state feedback control problems on the basis of input/state measurements. First, we will consider the problem of data-driven stabilization by static state feedback, where the data consist of input and state measurements. As described in the problem statement we will look at the informativity and design problems separately as special cases of Problem 2. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control") and Problem 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"). We will then use similar techniques to obtain a result for deadbeat control.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Control using input and state data", "weight": 1.0} -->

After this, we will shift towards the linear quadratic regulator problem, where we wish to find a stabilizing feedback that additionally minimizes a specified quadratic cost.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A Stabilization by state feedback", "weight": 1.0} -->

In what follows, we will consider the problem of finding a stabilizing controller for the system, using only the data $(U_{-},X)$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A Stabilization by state feedback", "weight": 1.0} -->

In addition, recall the set $\Sigma_{i/s}$ as defined in and $\Sigma_{i/s}^{0}$. In line with Definition 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control") we obtain the following notion of informativity for stabilization by state feedback.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 13", "weight": 1.0} -->

At this point, one may wonder about the relation between informativity for stabilizability (as in Section III) and informativity for stabilization. It is clear that $(U_{-},X)$ are informative for stabilizability if $(U_{-},X)$ are informative for stabilization by state feedback. However, the reverse statement does not hold in general. This is due to the fact that all systems $(A,B)$ in $\Sigma_{i/s}$ may be stabilizable, but there may not be a *common* feedback gain $K$ such that $A + {BK}$ is stable for all of these systems. Note that the existence of a common stabilizing $K$ for all systems in $\Sigma_{i/s}$ is essential, since there is no way to distinguish between the systems in $\Sigma_{i/s}$ based on the given data $(U_{-},X)$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 13", "weight": 1.0} -->

The following example further illustrates the difference between informativity for stabilizability and informativity for stabilization.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Example 14", "weight": 1.0} -->

This is because the systems $({- 1},1)$ and $$ in $\Sigma_{i/s}$ cannot be stabilized by the *same* controller of the form ${u{(t)}} = {Kx{(t)}}$. We conclude that informativity of the data for stabilizability does not imply informativity for stabilization by state feedback.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Example 14", "weight": 1.0} -->

The notion of informativity for stabilization by state feedback is a specific example of informativity for control. As described in Problem 2. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control"), we will first find necessary and sufficient conditions for informativity for stabilization by state feedback. After this, we will design a corresponding controller, as described in Problem 3. ‣ II Problem formulation ‣ Data informativity: a new perspective on data-driven analysis and control").

<!-- chunk {"id": "body-0071", "role": "body", "section": "Example 14", "weight": 1.0} -->

In order to be able to characterize informativity for stabilization, we first state the following lemma.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 18", "weight": 1.0} -->

To the best of our knowledge, LMI conditions for data-driven stabilization were first studied. In fact, the linear matrix inequality is the same as that of \[40, Theorem 3\]. However, an important difference is that the results in assume that the input $u$ is persistently exciting of sufficiently high order. In contrast, Theorem 17, as well as Theorem 16, do not require such conditions. The characterization provides the minimal conditions on the data under which it is possible to obtain a stabilizing controller.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 19", "weight": 1.0} -->

Consider an unstable system of the form, where $A_{s}$ and $B_{s}$ are given by

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 19", "weight": 1.0} -->

We collect data from this system on a single time interval from $t = 0$ until $t = 2$, which results in the data matrices

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 19", "weight": 1.0} -->

Clearly, the matrix $X_{-}$ is square and invertible, and it can be verified that

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 19", "weight": 1.0} -->

is stable, since its eigenvalues are $\frac{1}{2}{({1 \pm {\sqrt{2}i}})}$. We conclude by Theorem 16 that the data $(U_{-},X)$ are informative for stabilization by state feedback. The same conclusion can be drawn from Theorem 17 since

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 19", "weight": 1.0} -->

solves. Next, we can conclude from either Theorem 16 or Theorem 17 that the stabilizing feedback gain in this example is unique, and given by $K = {U_{-}X_{-}^{- 1}} = \begin{bmatrix}
\end{bmatrix}$. Finally, it is worth noting that the data are not informative for system identification. In fact, ${(A,B)} \in \Sigma_{i/s}$ if and only if

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example 19", "weight": 1.0} -->

Proof of Theorem 17. To prove the 'if' part of the first statement, suppose that there exists a $\Theta$ satisfying. In particular, this implies that $X_{-}\Theta$ is symmetric positive definite. Therefore, $X_{-}$ has full row rank. By taking a Schur complement and multiplying by $- 1$, we obtain

<!-- chunk {"id": "body-0079", "role": "body", "section": "Example 19", "weight": 1.0} -->

Since $X_{-}\Theta$ is positive definite, this implies that $X_{+}\Theta{({X_{-}\Theta})}^{- 1}$ is stable. In other words, there exists a right inverse $X_{-}^{\dagger}:={\Theta{({X_{-}\Theta})}^{- 1}}$ of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is stable. By Theorem 16, we conclude that $(U_{-},X)$ are informative for stabilization by state feedback, proving the 'if' part of the first statement. Using Theorem 16 once more, we see that $K:={U_{-}\Theta{({X_{-}\Theta})}^{- 1}}$ stabilizes all systems in $\Sigma_{i/s}$, which in turn proves the 'if' part of the second statement.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Example 19", "weight": 1.0} -->

Subsequently, to prove the 'only if' part of the first statement, suppose that the data $(U_{-},X)$ are informative for stabilization by state feedback. Let $K$ be any feedback gain such that $\Sigma_{i/s} \subseteq \Sigma_{K}$. By Theorem 16, $X_{-}$ has full row rank and $K$ is of the form $K = {U_{-}X_{-}^{\dagger}}$, where $X_{-}^{\dagger}$ is a right inverse of $X_{-}$ such that $X_{+}X_{-}^{\dagger}$ is stable. The stability of $X_{+}X_{-}^{\dagger}$ implies the existence of a symmetric positive definite matrix $P$ such that

<!-- chunk {"id": "body-0081", "role": "body", "section": "Example 19", "weight": 1.0} -->

Via the Schur complement we conclude that

<!-- chunk {"id": "body-0082", "role": "body", "section": "Example 19", "weight": 1.0} -->

In addition to the stabilizing controllers discussed in Theorems 16 and 17, we may also look for a controller of the form ${{\mathbf{u}}{(t)}} = {K{\mathbf{x}}{(t)}}$ that stabilizes the system in *finite time*. Such a controller is called a *deadbeat controller* and is characterized by the property that ${{({A_{s} + {B_{s}K}})}^{t}x_{0}} = 0$ for all $t \geqslant n$ and all $x_{0} \in {\mathbb{R}}^{n}$. Thus, $K$ is a deadbeat controller if and only if $A_{s} + {B_{s}K}$ is nilpotent. Now, for a given matrix $K$ define

<!-- chunk {"id": "body-0083", "role": "body", "section": "Example 19", "weight": 1.0} -->

Then, analogous to the definition of informativity for stabilization by state feedback, we have the following definition of informativity for deadbeat control.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 22", "weight": 1.0} -->

In order to compute a suitable right inverse $X_{-}^{\dagger}$ such that $X_{+}X_{-}^{\dagger}$ is nilpotent, we can proceed as follows. Since $X_{-}$ has full row rank, we have $T \geqslant n$. We now distinguish two cases: $T = n$ and $T > n$. In the former case, $X_{-}$ is nonsingular and hence $X_{+}X_{-}^{- 1}$ is nilpotent. In the latter case, there exist matrices $F \in {\mathbb{R}}^{T \times n}$ and $G \in {\mathbb{R}}^{T \times {({T - n})}}$ such that $\begin{bmatrix}
\end{bmatrix}$ is nonsingular and ${X_{-}\begin{bmatrix}
\end{bmatrix}} = \begin{bmatrix}
\end{bmatrix}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Remark 22", "weight": 1.0} -->

Note that $X_{-}^{\dagger}$ is a right inverse of $X_{-}$ if and only if $X_{-}^{\dagger} = {F + {GH}}$ for some $H \in {\mathbb{R}}^{{({T - n})} \times n}$. Finding a right inverse $X_{-}^{\dagger}$ such that $X_{+}X_{-}^{\dagger}$ is nilpotent, therefore, amounts to finding $H$ such that ${X_{+}F} + {X_{+}GH}$ is nilpotent, i.e. has only zero eigenvalues. Such a matrix $H$ can be computed by invoking \[45, Thm. 3.29 and Thm.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-B Informativity for linear quadratic regulation", "weight": 1.0} -->

Consider the discrete-time linear system. Let $x_{x_{0},u}{( \cdot )}$ be the state sequence of resulting from the input $u{( \cdot )}$ and initial condition ${x{}} = x_{0}$. We omit the subscript and simply write $x{( \cdot )}$ whenever the dependence on $x_{0}$ and $u$ is clear from the context.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-B Informativity for linear quadratic regulation", "weight": 1.0} -->

Associated to system, we define the quadratic cost functional

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-B Informativity for linear quadratic regulation", "weight": 1.0} -->

where $Q = Q^{\top}$ is positive semidefinite and $R = R^{\top}$ is positive definite.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Problem 4 (LQR)", "weight": 1.0} -->

Such an input $u^{\ast}$ is called optimal for the given $x_{0}$. Of course, an optimal input does not necessarily exist for all $x_{0}$. We say that the linear quadratic regulator problem is solvable for $(A,B,Q,R)$ if for every $x_{0}$ there exists an input $u^{\ast}$ such that

<!-- chunk {"id": "body-0090", "role": "body", "section": "Problem 4 (LQR)", "weight": 1.0} -->

The input $u^{\ast}$ minimizes the cost functional, i.e.,

<!-- chunk {"id": "body-0091", "role": "body", "section": "Problem 4 (LQR)", "weight": 1.0} -->

In the sequel, we will require the notion of observable eigenvalues. Recall from e.g. \[45, Section 3.5\] that an eigenvalue $\lambda$ of $A$ is $(Q,A)$-observable if

<!-- chunk {"id": "body-0092", "role": "body", "section": "Problem 4 (LQR)", "weight": 1.0} -->

The following theorem provides necessary and sufficient conditions for the solvability of the linear quadratic regulator problem for $(A,B,Q,R)$. This theorem is the discrete-time analogue to the continuous-time case stated in \[45, Theorem 10.18\].

<!-- chunk {"id": "body-0093", "role": "body", "section": "Remark 27", "weight": 1.0} -->

Condition (ii) of Theorem 26 is a pathological case in which $A$ is stable and ${QA} = 0$ for all matrices $A$ that are compatible with the data. Since ${x{(t)}} \in {{im}A}$ for all $t > 0$, we have ${Qx{(t)}} = 0$ for all $t > 0$ if the input function is chosen as $u = 0$. Additionally, since $A$ is stable, this shows that the optimal input is equal to $u^{\ast} = 0$. If we set aside condition (ii), the implication of Theorem 26 is the following: if the data are informative for linear quadratic regulation they are also informative for system identification.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Remark 27", "weight": 1.0} -->

At first sight, this might seem like a negative result in the sense that data-driven LQR is only possible with data that are also informative enough to uniquely identify the system. However, at the same time, Theorem 26 can be viewed as a positive result in the sense that it provides fundamental justification for the data conditions imposed in e.g.. Indeed, in the data-driven infinite horizon LQR problem^33^3Note that the authors of formulate this problem as the minimization of the $H_{2}$-norm of a certain transfer matrix. is solved using input/state data under the assumption that the input is persistently exciting of sufficiently high order. Under the latter assumption, the input/state data are informative for system identification, i.e., the matrices $A_{s}$ and $B_{s}$ can be uniquely determined from data. Theorem 26 justifies such a strong assumption on the richness of data in data-driven linear quadratic regulation.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Remark 27", "weight": 1.0} -->

The data-driven *finite* horizon LQR problem was solved under a persistency of excitation assumption. Our results suggest that also in this case informativity for system identification is necessary for data-driven LQR, although further analysis is required to prove this claim.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Remark 27", "weight": 1.0} -->

Proof of Theorem 26. We first prove the 'if' part. Sufficiency of the condition (i) readily follows from Theorem 23. To prove the sufficiency of the condition (ii), assume that the matrix $A$ is stable and ${QA} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. By the discussion following Theorem 26, this implies that $u^{\ast} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. Hence, for $K = 0$ we have $\Sigma_{i/s} \subseteq \Sigma_{K}^{Q,R}$, i.e., the data are informative for linear quadratic regulation.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Remark 27", "weight": 1.0} -->

To prove the 'only if' part, suppose that the data $(U_{-},X)$ are informative for linear quadratic regulation. From Lemma 25, we know that there exist $M$ and $P^{+}$ satisfying -- for all ${(A,B)} \in \Sigma_{i/s}$. By substituting into and using, we obtain

<!-- chunk {"id": "body-0098", "role": "body", "section": "Remark 27", "weight": 1.0} -->

Since and hold for all ${(A,B)} \in \Sigma_{i/s}$, we have that

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 27", "weight": 1.0} -->

for all ${(A,B)} \in \Sigma_{i/s}$. From the identity

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 27", "weight": 1.0} -->

we see that ${P^{+}A} = 0$ for all ${(A,B)} \in \Sigma_{i/s}$. Then, it follows from that $K = 0$. Since ${A_{0} + {B_{0}K}} = 0$ for all ${(A_{0},B_{0})} \in \Sigma_{i/s}^{0}$ due to Lemma 15, we see that $A_{0}$ must be zero. Hence, we have $A = A_{s}$ for all ${(A,B)} \in \Sigma_{i/s}$ and $A_{s}$ is stable. Moreover, it follows from that $P^{+} = Q$. Therefore, ${QA_{s}} = 0$. In other words, condition (ii) is satisfied, which proves the theorem. $\blacksquare$

<!-- chunk {"id": "body-0101", "role": "body", "section": "Remark 27", "weight": 1.0} -->

Theorem 26 gives necessary and sufficient conditions under which the data are informative for linear quadratic regulation. However, it might not be directly clear how these conditions can be verified given input/state data. Therefore, in what follows we rephrase the conditions of Theorem 26 in terms of the data matrices $X$ and $U_{-}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "IV-C From data to LQ gain", "weight": 1.0} -->

In this section our goal is to devise a method in order to compute the optimal feedback gain $K$ directly from the data. For this, we will employ ideas from the study of Riccati inequalities (see e.g ).

<!-- chunk {"id": "body-0103", "role": "body", "section": "IV-C From data to LQ gain", "weight": 1.0} -->

The following theorem asserts that $P^{+}$ as in Lemma 25 can be found as the unique solution to an optimization problem involving only the data. Furthermore, the optimal feedback gain $K$ can subsequently be found by solving a set of linear equations.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Remark 30", "weight": 1.0} -->

From a design viewpoint, the optimal feedback gain $K$ can be found in the following way. First solve the semidefinite program in Theorem 29(i). Subsequently, compute a solution $X_{-}^{\dagger}$ to the linear equations ${X_{-}X_{-}^{\dagger}} = I$ and. Then, the optimal feedback gain is given by $K = {U_{-}X_{-}^{\dagger}}$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Remark 31", "weight": 1.0} -->

The data-driven LQR problem was first solved using semidefinite programming in \[40, Theorem 4\]. There, the optimal feedback gain was found by minimizing the trace of a weighted sum of two matrix variables, subject to two LMI constraints. The semidefinite program in Theorem 29 is attractive since the dimension of the unknown $P$ is (only) $n \times n$. In comparison, the dimensions of the two unknowns in \[40, Theorem 4\] are $T \times n$ and $m \times m$, respectively. In general, the number of samples $T$ is much larger^44^4In fact, this is always the case under the persistency of excitation conditions imposed in as such conditions can only be satisfied provided that $T \geqslant {{nm} + n + m}$. than $n$. An additional attractive feature of Theorem 29 is that $P^{+}$ is obtained from the data.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Remark 31", "weight": 1.0} -->

This is useful since the minimal cost associated to any initial condition $x_{0}$ can be computed as $x_{0}^{\top}P^{+}x_{0}$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 31", "weight": 1.0} -->

The data-driven LQR approach in is quite different from Theorem 29 since the solution to the Riccati equation is approximated using a batch-form solution to the *Riccati difference equation*. A similar approach was used in for the *finite horizon* data-driven LQR/LQG problem. In the setup of, the approximate solution to the Riccati equation is exact only if the number of data points tends to infinity. The main difference between our approach and the one in is hence that the solution $P^{+}$ to the Riccati equation can be obtained exactly from *finite* data via Theorem 29.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 31", "weight": 1.0} -->

Proof of Theorem 29. We begin with proving the first statement. Note that

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 31", "weight": 1.0} -->

To prove this claim, let $P$ be such that $P = P^{\top} \geqslant 0$ and ${\mathcal{L}{(P)}} \leqslant 0$. Since the data are informative for linear quadratic regulation, they are also informative for stabilization by state feedback. Therefore, the optimal feedback gain $K$ satisfies

<!-- chunk {"id": "body-0110", "role": "body", "section": "Remark 31", "weight": 1.0} -->

due to Lemma 15. Therefore, the above expression for $\mathcal{L}{(P)}$ implies that

<!-- chunk {"id": "body-0111", "role": "body", "section": "Remark 31", "weight": 1.0} -->

for all ${(A,B)} \in \Sigma_{i/s}$. This yields

<!-- chunk {"id": "body-0112", "role": "body", "section": "Remark 31", "weight": 1.0} -->

where $M$ is as in Lemma 25. By subtracting this, we obtain

<!-- chunk {"id": "body-0113", "role": "body", "section": "Remark 31", "weight": 1.0} -->

Since $M$ is stable, this discrete-time Lyapunov inequality implies that ${P^{+} - P} \geqslant 0$ and hence $P^{+} \geqslant P$. This proves the claim.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Remark 31", "weight": 1.0} -->

Note that $R + {B^{\top}P^{+}B}$ is positive definite. Then, it follows from that

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 31", "weight": 1.0} -->

via a Schur complement argument. Therefore, ${\mathcal{L}{(P^{+})}} \leqslant 0$. Since $P^{+} \geqslant P$, we have ${{tr}P^{+}} \geqslant {{tr}P}$. Together, this shows that $P^{+}$ is a solution to the optimization problem stated in the theorem.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Remark 31", "weight": 1.0} -->

Finally, we prove the second statement. It follows from and that

<!-- chunk {"id": "body-0117", "role": "body", "section": "Remark 31", "weight": 1.0} -->

The optimal feedback $K$ is stabilizing, therefore it follows from Theorem 16 that $K$ can be written as $K = {U_{-}\Gamma}$, where $\Gamma$ is some right inverse of $X_{-}$. Note that this implies the existence of a right inverse $X_{-}^{\dagger}$ of $X_{-}$ satisfying. Indeed, $X_{-}^{\dagger}:=\Gamma$ is such a matrix. Moreover, if $X_{-}^{\dagger}$ is a right inverse of $X_{-}$ satisfying then ${{({U_{-} - {KX_{-}}})}X_{-}^{\dagger}} = 0$ by and positive definiteness of $R$. We conclude that the optimal feedback gain is equal to $K = {U_{-}X_{-}^{\dagger}}$, which proves the second statement. $\blacksquare$

<!-- chunk {"id": "body-0118", "role": "body", "section": "Control using input and output data", "weight": 1.0} -->

In this section, we will consider problems where the output does play a role. In particular, we will consider the problem of stabilization by dynamic measurement feedback. We will first consider this problem based on input, state and output measurements. Subsequently, we will turn our attention to the case of input/output data.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Control using input and output data", "weight": 1.0} -->

We want to design a stabilizing dynamic controller of the form

<!-- chunk {"id": "body-0120", "role": "body", "section": "Control using input and output data", "weight": 1.0} -->

such that the closed-loop system, given by

<!-- chunk {"id": "body-0121", "role": "body", "section": "Control using input and output data", "weight": 1.0} -->

is stable. This is equivalent to the condition that

<!-- chunk {"id": "body-0122", "role": "body", "section": "V-A Stabilization using input, state and output data", "weight": 1.0} -->

Suppose that we collect input/state/output data on $\ell$ time intervals $\{ 0,1,\ldots,T_{i}\}$ for $i = {1,2,\ldots,q}$. Let ${U_{-},X,X_{-}},$ and $X_{+}$ be defined as in and let $Y_{-}$ be defined in a similar way as $U_{-}$. Then, we have

<!-- chunk {"id": "body-0123", "role": "body", "section": "V-A Stabilization using input, state and output data", "weight": 1.0} -->

relating the data and the 'true' system.

<!-- chunk {"id": "body-0124", "role": "body", "section": "V-A Stabilization using input, state and output data", "weight": 1.0} -->

In addition, for given $K$, $L$ and $M$, we define the set of systems that are stabilized by the dynamic controller by

<!-- chunk {"id": "body-0125", "role": "body", "section": "Remark 35", "weight": 1.0} -->

Under the condition that $U_{-}$ has full row rank, Theorem 34 asserts that in order to construct a stabilizing dynamic controller, it is necessary that the data are rich enough to identify the system matrices $A_{s},B_{s},C_{s}$ and $D_{s}$ uniquely. The controller proposed in (a), (b), (c) is a so-called *observer-based* controller, see e.g. \[45, Section 3.12\]. The feedback gains $M$ and $L$ can be computed using standard methods, for example via pole placement or LMI's.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Remark 35", "weight": 1.0} -->

Proof of Theorem 34. To prove the 'if' part, suppose that conditions (i) and (ii) are satisfied. This implies the existence of the matrices $(K,L,M)$ as defined in items (a), (b) and (c). We will now show that these matrices indeed constitute a stabilizing controller. Note that by condition (i), $\Sigma_{i/s/o} = {\{{(A_{s},B_{s},C_{s},D_{s})}\}}$ with

<!-- chunk {"id": "body-0127", "role": "body", "section": "Remark 35", "weight": 1.0} -->

are similar \[45, Section 3.12\]. We conclude that $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback and that the recipe given by (a), (b) and (c) leads to a stabilizing controller $(K,L,M)$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Remark 35", "weight": 1.0} -->

It remains to prove the 'only if' part. To this end, suppose that the data $(U_{-},X,Y_{-})$ are informative for stabilization by dynamic measurement feedback. Let $(K,L,M)$ be such that $\Sigma_{i/s/o} \subseteq \Sigma_{K,L,M}$. This means that

<!-- chunk {"id": "body-0129", "role": "body", "section": "Remark 35", "weight": 1.0} -->

is stable for all $\alpha \in {\mathbb{R}}$. We conclude that the spectral radius of the matrix

<!-- chunk {"id": "body-0130", "role": "body", "section": "Remark 35", "weight": 1.0} -->

is smaller than $1/\alpha$. By taking the limit as $\alpha\rightarrow\infty$, we see that the spectral radius of $\zeta\zeta^{\top}$ must be zero due to the continuity of spectral radius. Therefore, $\zeta$ must be zero. Since $U_{-}$ has full column rank, we can conclude that $\eta$ must be zero too. This proves that condition (i) and therefore $\Sigma_{i/s/o} = {\{{(A_{s},B_{s},C_{s},D_{s})}\}}$. Since the controller $(K,L,M)$ stabilizes $(A_{s},B_{s},C_{s},D_{s})$, the pair $(A_{s},B_{s})$ is stabilizable and $(C_{s},A_{s})$ is detectable. By we conclude that condition (ii) is also satisfied. This proves the theorem.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Remark 35", "weight": 1.0} -->

The following corollary follows from Lemma 33 and Theorem 34 and gives necessary and sufficient conditions for informativity for stabilization by dynamic measurement feedback. Note that we do not make any a priori assumptions on the rank of $U_{-}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Remark 37", "weight": 1.0} -->

In the previous corollary it is clear that the system matrices of the data-generating system are related to the data via

<!-- chunk {"id": "body-0133", "role": "body", "section": "Remark 37", "weight": 1.0} -->

Therefore the corollary shows that informativity for stabilization by dynamic measurement feedback requires that $A_{s}$ and $C_{s}$ can be identified uniquely from the data. However, this does not hold for $B_{s}$ and $D_{s}$ in general.

<!-- chunk {"id": "body-0134", "role": "body", "section": "V-B Stabilization using input and output data", "weight": 1.0} -->

Recall that we consider a system of the form. When given input, state and output data, any system $(A,B,C,D)$ consistent with these data satisfies

<!-- chunk {"id": "body-0135", "role": "body", "section": "V-B Stabilization using input and output data", "weight": 1.0} -->

In this section, we will consider the situation where we have access to input and output measurements only. Moreover, we assume that the data are collected on a single time interval, i.e. $q = 1$. This means that our data are of the form $(U_{-},Y_{-})$, where

<!-- chunk {"id": "body-0136", "role": "body", "section": "V-B Stabilization using input and output data", "weight": 1.0} -->

Again, we are interested in informativity of the data, this time given by $(U_{-},Y_{-})$. Therefore we wish to consider the set of all systems of the form with the state space dimension^55^5The state space dimension of the system may be known a priori. In the case that it is not, it can be computed using subspace identification methods, see e.g. \[2, Theorem 2\]. $n$ that admit the same input/output data.

<!-- chunk {"id": "body-0137", "role": "body", "section": "V-B Stabilization using input and output data", "weight": 1.0} -->

As in the previous section, we wish to find a controller of the form that stabilizes the system. This means that, in line with Definition 3.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Results in data-driven control should clearly highlight the differences and possible advantages as compared to system identification paired with model-based control. One clear advantage of data-driven control is its capability of solving problems in the presence of data that are not informative for system identification. Therefore, informativity is a very important concept for data-driven analysis and control.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

In this paper we have introduced a comprehensive framework for studying informativity problems. We have applied this framework to analyze several system-theoretic properties on the basis of data. The same framework was used to solve multiple data-driven control problems.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

After solving these problems, we have made the comparison between our data-driven methods, and the 'classical' combination of identification and model-based control. We have shown that for many analysis and control problems, such as controllability analysis and stabilization, the data-driven approach can indeed be performed on data that are not informative for system identification. On the other hand, for data-driven linear quadratic regulation it has been shown that informativity for system identification is a necessary condition. This effectively means that for this data-driven control problem, we have given a theoretic justification for the use of persistently exciting data.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Future work", "weight": 1.5} -->

Due to the generality of the introduced framework, many different problems can be studied in a similar fashion: one could consider different types of data, where more results based on only input and output data would be particularly interesting. Many other system-theoretic properties could be considered as well, for example, analyzing passivity or tackling robust control problems based on data.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Future work", "weight": 1.5} -->

It would also be of interest to generalize the model class under consideration. One could, for instance, consider larger classes of systems like differential algebraic or polynomial systems. On the other hand, the class under consideration can also be made smaller by prior knowledge of the system. For example, the system might have an observed network structure, or could in general be parametrized.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Future work", "weight": 1.5} -->

A framework similar to ours could be employed in the presence of disturbances, which is a problem of practical interest. A study of data-driven control problems in this situation is particularly interesting, because system identification is less straightforward. We note that data-driven stabilization under measurement noise has been studied in and under unknown disturbances. Additionally, the data-driven LQR problem is popular in the machine learning community, where it is typically assumed that the system is influenced by (Gaussian) process noise, see e.g..

<!-- chunk {"id": "body-0144", "role": "body", "section": "Future work", "weight": 1.5} -->

In this paper, we have assumed that the data are given. Yet another problem of practical interest is that of experiment design, where inputs need to be chosen such that the resulting data are informative. In system identification, this problem led to the notion of persistence of excitation. For example, it is shown in that the rank condition can be imposed by injecting an input sequence that is persistently exciting of order $n + 1$. However, as we have shown, this rank condition is not necessary for some data-driven control problems, like stabilization by state feedback. The question therefore arises whether we can find tailor-made conditions on the input only, that guarantee informativity for data-driven control.
