<!-- arxiv-full-text:v1 {"arxiv_id": "2302.10488", "source": "arxiv-pdf"} -->

## The informativity approach

TO DATA-DRIVEN ANALYSIS AND CONTROL HENK J. VAN WAARDE, JAAP EISING, M. KANAT CAMLIBEL, and HARRY L. TRENTELMAN R oughly speaking, systems and control theory deals with the problem of making a concrete physical system behave according to certain desired specifications. In order to achieve this desired behavior, the system can be interconnected with a physical device, called a controller. The problem of finding a mathematical description of such a controller is called the control design problem.

In order to obtain a mathematical description of a controller for a to-be-controlled physical system, a possible first step is to obtain a mathematical model of the physical system. Such a mathematical model can take many forms. For example, the model could be in terms of ordinary or partial differential equations, difference equations, or transfer matrices.

There are several ways to obtain a mathematical model for the physical system. The usual way is to apply the basic physical laws that are satisfied by the variables appearing in the system. This method is called fi rst principles modeling. For example, for electro-mechanical systems, the set of basic physical laws that govern the behavior of the variables in the system (conservation laws, Newton's laws, Kirchoff's laws, etc.) form a mathematical model.

An alternative way to obtain a model is to do experiments on the physical system: certain external variables in the physical system are set to take particular values, while at the same time other variables are measured. In this way, one obtains data on the system that can be used to find mathematical descriptions of laws that are obeyed by the system variables, thus obtaining a model. This method is Digital Object Identifier 10.1109/MCS.2020.000000 Date of current version: XXXXXX called system identification.

The second step in a control system design problem is to decide which desired behavior we would like the physical system to have. Very often, this desired behavior can be formalized by requiring the mathematical model to have certain qualitative or quantitative mathematical properties. Together, these properties form the design objective.

Based on the mathematical model of the physical system and the design objective, the third, ultimate, step is to design a mathematical model of a suitable controller. This approach, leading from a model and a design objective (or list of design specifications) to a model of a controller is an important paradigm in systems and control, and is often called model-based control.

An approach that has recently gained popularity is to design controllers without the step of finding a mathematical model of the to-be-controlled physical system. This alternative approach deals with the problem of synthesizing control laws directly on the basis of measured data, and is called the data-driven approach to control design. Of course, one can argue that also the combination of system identification followed by model based control as described above is an instance of data driven control design. Indeed, methods using this combination are often called indirect methods of data-driven control, consisting of the two-step process of data-driven modeling (i.e., system identification -) followed by model-based control.

Early contributions to direct data-driven control include PID control, direct adaptive control, iterative feedback tuning virtual reference feedback tuning and unfalsified control. Recently, direct optimal control design - and predictive control - have received considerable attention. Some of these ap-

## regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient" information

proaches, such as and, strongly rely on the socalled fundamental lemma by Willems and co-authors. This result provides a convenient parameterization of all trajectories of a linear time-invariant system in terms of data. Originally developed in a behavioral context, the fundamental lemma is also instrumental for direct output matching control and control by interconnection. The result has been extended in various ways to different model classes and data setups -. Although initially developed for linear systems, the fundamental lemma has been applied in the context of data-driven control of nonlinear dynamics, such as polynomial and Lur'e systems -. In addition to control problems, also analysis problems have been studied within a direct databased framework. Some examples include the analysis of stability, controllability and observability -, and dissipativity -.

Investigating the different pros and cons of indirect and direct methods is an area of active research,. However, regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient" information. Indeed, as an extreme example one can consider the zero input-output trajectory generated by an unknown linear time-invariant system: clearly this trajectory does not reveal much about the system and would be a poor basis for an identification or control scheme. The purpose of this paper is to introduce a framework in which we can systematically study the richness of data that is required for various system analysis and control problems.

The concept of 'data informativity" plays a central role in this paper. This concept finds its roots in system identification, -, where informativity is usually understood as a condition on the data under which it is possible to distinguish between different models in a (parametric) model class. Here, however, we will define a general notion of data informativity for system analysis and control design. We are thus not necessarily interested in distinguishing between different models on the basis of the data, but rather want to understand whether it is possible to assess a system-theoretic property, or to synthesize a controller for the physical system from the data. If this is possible, we will say that the data are informative for the system property, or for the control design problem. Although we will introduce the concept of informativity in general terms, it is important to note that the conditions for informative data depend on the particular analysis or control problem at hand. For example, as we will see, the conditions under which stabilizing controllers can be obtained from data are less stringent than those for obtaining optimal controllers. This motivates a rigorous analysis of data informativity for different system analysis and control problems.

In some situations the data obtained from the physical system contain sufficient information to identify the system model uniquely. For our purposes, this situation is the least interesting because informativity for system analysis and control design simply boil down to properties of the (unique) model of the physical system. In general however, it is not possible to uniquely identify the physical system because the data set may contain a small number of samples or the data may be corrupted by noise. In this case, we will make use of consistent systems sets that comprise all dynamical system models that are unfalsified by the data. Such sets also play an important role in set membership identification, where they are called feasible systems sets.

In the case that unique system identification is impossible, it will turn out that there are still many relevant cases in which the data are informative for system analysis or control design. In fact, our main results can be interpreted as robust analysis and control methods for sets of consistent systems. For example, in our study of noise-free data the approach leads to a robust theory for affine sets of systems, which, to the best of our knowledge has not received much attention before. In the noisy data setting, our methods draw inspiration from classical robust control results like Yakubovich's S-lemma and extensions thereof.

Besides conditions for data informativity, this paper also puts forward a number of control design methods that enable the synthesis of a controller from informative data. In many cases, these design methods are based on data-based linear matrix inequalities. The methods thus contribute to the aforementioned lines of work on direct data-driven control, since no (explicit) model identification is needed. Although we believe that the direct approach is appealing from a conceptual point of view (why focus on models while the goal is control design?), we also acknowledge that it would be possible to formulate indirect alternatives to our methods by describing the set of systems consistent with the data as a model plus an uncertainty description around this model. In view of this observation, we are inclined to believe that the discussion on direct versus

## informative data is the cornerstone of this paper, since any data-driven identification, analysis or control task is impossible without it

indirect control is, perhaps, not the most fundamental one. Instead, the concept of informative data is the cornerstone of this paper, since any data-driven identification, analysis or control task is impossible without it.

## DATA INFORMATIVITY FRAMEWORK

In this section we will introduce the concept of data informativity for verifying a given system property or solving a certain control design problem.

To start , we fix a certain model class M. This model class is a given set of systems that is assumed to contain the 'true' system (i.e., a mathematical model of the underlying unknown physical system), denoted by S. We assume that the true system S is not known but that we do have access to a set of data, D, which is generated by this system. As explained in the introduction, we are interested in assessing system-theoretic properties of S and designing control laws for it from the data D. Given the set of data D, we define Σ D ⊆ M to be the set of all systems in M that are consistent with the data D, i.e., that could also have generated the same data. In other words, it is impossible to distinguish the true system S from any other system in Σ D on the basis of the given data D alone. As noted before, the setup introduced above is in line with set membership identification (SMI) methods, where sets of systems consistent with the data also play an important role (in SMI these are typically called feasible system sets ).

We will now first focus on data-driven analysis of system theoretic properties. Let P be some system theoretic property. We will denote the set of all systems within M having this property by Σ P. Suppose we are interested in the question whether our true system S has the property P. Since the only information we have to base our answer on are the data D obtained from the true system, we can only conclude from the data that the true system has property P if all systems consistent with the data D have the property P. If this is the case, we call the data informative for the system property. This leads to the following definition, see also Figures 1 and 2.

## Definition 1 (Informativity for analysis)

We say that the data D are informative for property P if Σ D ⊆ Σ P, i.e., all systems that are consistent with the data have property P.

In general, if the true system S can be uniquely de- Σ D: data consistent systems D: given data set Σ P: systems with property P FIGURE 1 The data are informative for property P as Σ D ⊆ Σ P.

FIGURE 2 The data are not informative for property P. Depending on the situation, either S ∈ Σ P or S ̸∈ Σ P. On the basis of the given data D, it is impossible to distinguish these two cases. termined from the data D, that is Σ D = {S} and S has the property P, then it is evident that the data D are informative for P. However, the converse may not be true: Σ D might contain many systems, all of which have property P. In the data informativity framework, we are interested in necessary and sufficient conditions for informativity of the data. Such conditions reveal the minimal amount of information required to assess the property P. A natural problem statement is therefore the following:

## Problem 1 (Informativity problem for analysis)

Provide necessary and sufficient conditions on the data D under which these data are informative for property P.

The above gives us a general framework to deal with data-driven analysis problems. We will also deal with datadriven control problems. The objective in such problems is the data-based design of controllers such that the closed loop system, obtained from the interconnection of the true system S and the controller, satisfies the given control objective. As for the analysis problem, we have only the information from the data to base our design . Therefore, we can only guarantee that our control objective is achieved if the designed controller achieves the design objective when interconnected with any system from the set Σ D.

For the framework to allow for data-driven control problems, we will consider a given control objective O (for example, a system theoretic property or a guaranteed performance of the closed loop system). Denote by Σ O the set of all systems that satisfy the control objective O. For a given controller K, denote by Σ D ( K ) the set of all systems obtained as the interconnection of a system in Σ D with the controller K. We then have the following variant of informativity:

## Definition 2 (Informativity for control)

We say that the data D are informative for the control objective O if there exists a controller K such that Σ D ( K ) ⊆ Σ O.

Obviously, the first step in any data-driven control problem is to determine whether it is possible to obtain, from the given data, a suitable controller. This leads to the following informativity problem:

## Problem 2 (Informativity problem for control)

Provide necessary and sufficient conditions on D under which the data are informative for the control objective O.

The second step of data-driven control involves the design of a suitable controller. In terms of our framework, this can be stated as:

## Problem 3 (Control design problem)

Under the assumption that the data D are informative for the control objective O, find a controller K such that Σ D ( K ) ⊆ Σ O.

The data-driven control design problem as formulated here has a rather natural interpretation as a problem of robust control. Indeed, the aim is to find one single controller that achieves the design objective for all systems that are consistent with the data. In other words, the 'system uncertainty' is determined directly by the given data, and no attempt is made to identify in any sense an uncertainty description that is suitable for existing methods in robust control design. The given data are called informative for a given design objective if the associated robust control problem allows a solution for the system uncertainty imposed by the data.

The data informativity framework has already been applied to various analysis and design problems. Generally speaking, there is a dichotomy between two main directions. On the one hand there are analysis and design problems based on exact, i.e., noiseless data. On the other hand we consider the more realistic situation that the data are noisy, in the sense that they are obtained from a true, unknown, system that is corrupted by additive noise. Table 1 provides an overview of the results. The first column of the table states the considered system property or control design problem. The second column refers to the type of data that are used. Here, 'E' refers to exact data, and 'N' to noisy data. State, input-state, input-stateoutput and input-output are denoted by 'S', 'IS', 'ISO' and 'IO', respectively. The results in the table apply to discretetime systems, and most of the results are for linear timeinvariant dynamics.

TABLE 1 Summary of results within the informativity approach to data-driven analysis and control.

| Problem | Data | References | The purpose of this paper is to highlight the strength of the informativity framework by reviewing a selection of analysis and design problems, indicated in Table 1 in red.

Both exact and noisy data will be discussed in the present paper.

This paper is divided into three main sections. These sections are divided into subsections, each devoted to a particular analysis or control design problem. In the first main section our model class will be chosen as the set of all discrete-time linear input-state systems with given state and input dimensions. The data are measurements of the state and input obtained from a true, unknown, system on a given finite time-interval. In this first section it is assumed that the data are noiseless, in the sense that the true system does not contain any noise input. In this noiseless framework we discuss the problem of informativity for the system properties controllability and stabilizability. Next, as a first control design problem we discuss the problem of stabilization by static state feedback, and take a look at the corresponding informativity problem. In the third subsection we study informativity in the context of the linear quadratic regulator problem, and, finally, in the fourth subsection we look at the classical problem of tracking and regulation.

In the second main section we incorporate noise into the models and data. The model class consists of all inputstate systems with additive noise and the input-state data are assumed to be obtained from the noisy true system. The additive noise is unknown, but its samples on the data sampling interval are assumed to satisfy a given quadratic matrix inequality. In this framework we discuss a number of analysis and control design problems. In the first subsection we again look at the problem of stabilization by state feedback, this time in a noisy setting. The next subsection deal with informativity in the context of the well known H ∞ control problem. The final subsection of this part deals with the problem of determining from noisy data whether an unknown system is dissipative with respect to a given supply rate.

In the third, final, main section we abandon the state space framework and shift to input-output systems represented by higher order difference equation, also called autoregressive (AR) systems. As model class we take all AR systems with additive noise, of a given order and with given input and output dimensions. The data are now input-output data that are obtained from the true noisy input-output system. We study data-driven stabilization by dynamic output feedback and discuss informativity in this framework.

## Notation

The set of nonnegative integers will be denoted by Z +. We will denote by R n the n -dimensional Euclidean space. For given positive integers m and n the linear space of all real m × n matrices will be denoted by R m × n. The subset of R n × n consisting of all symmetric matrices will be denoted by S n. For vectors x and y we will denote [ x ⊤ y ⊤ ] ⊤ by col ( x, y ). For given integer n we denote by In the n × n identity matrix and 0 n the n × n zero matrix. In order to enhance readability, we sometimes denote the n × m zero matrix by 0 n × m. Given a real matrix M, we will denote its Moore-Penrose pseudo-inverse by M †. For a given matrix M of full row rank we denote any right-inverse by M ♯.

## ANALYSIS AND CONTROL USING EXACT INPUT-STATE DATA

In order to provide a solid foundation for more complex problems, in this section we will first consider the essential model class of linear, time-invariant input-state systems. Our goal is to analyze and control these systems on the basis of input-state data, consisting of a finite number of measurements of the input and state trajectories. Moreover, we will assume that these measurements are exact, that is, not corrupted by any noise.

Given this situation, we can make the abstract framework that was introduced in the introduction more tangible. To be precise, the unknown system S is assumed to be the following: where x denotes the n -dimensional state and u the m -dimensional input. In the following, we assume that the dimensions n and m are known, but the matrices As and Bs are unknown. As such, we see that S is contained in the model class M given by the set of all discrete-time linear input-state systems of the form with given state space and input dimensions n and m.

Suppose that we collect input-state data from the true system on a set of time instances { 0, 1,..., T }, in the sense that we excite the true system with an input sequence u, u,..., u (T -1) and obtain measurements of a corresponding state sequence x, x,..., x (T). We can collect these measurements in matrices by defining: If, additionally, we define the matrices we have X + = AsX -+ BsU -, since the data were assumed to be generated by the true system. Moreover, this is all the information we have regarding the true system on the basis of the data D: = (U -, X). As explained in the introduction, we are interested in the set Σ D containing all systems in M that are consistent with these data. Obviously, this set In fact, there is no need for the data to be collected sequentially. It is straightforward to adapt the results above to the situation of measurements on multiple sets of time instances.

First, we consider the problem of system identification. In the terminology of this paper, we say that the data (U -, X) are informative for system identification if the set Σ D contains exactly one element. Since by definition the true system (As, Bs) ∈ Σ D the data are informative for identification if and only if Σ D = { (As, Bs) }. Moreover it is the solution set of the affine equation appearing. Therefore, the data are informative for system identification if and only if the full rank condition holds. There exists a unique system in Σ D if and only if the condition holds, and this true system can then be obtained from the data as Once we have identified the true system is this way, we can apply model-based methods in order to verify its properties or to achieve the desired control objective. In the Sidebar 'Willems' fundamental lemma' we discuss the problem of designing inputs such that the resulting measurements are guaranteed to be informative for system identification.

## Controllability and stabilizability

As we will show in this subsection, condition is not necessary to perform data-driven analysis in general. As an illustration, we will establish necessary and sufficient conditions in terms of the data for verifying controllability and stabilizability, which do not require the rank condition to hold.

Recall from Definition 1 the definition of informativity of data for a given system property. In accordance with Definition 1 we say that the data ( U -, X ) are informative for controllability if all systems in Σ D are controllable. Likewise, we call the data informative for stabilizability if all systems in Σ D are stabilizable.

In order to establish tests for these notions of informativity, the well known Hautus test for controllability can be used: a system (A, B) is controllable if and only if for all λ ∈ C. For stabilizability, the Hautus test requires that holds for all λ outside the open unit disc.

The following theorem gives necessary and sufficient conditions on the input-state data to be informative for these two properties. The result provides tests on the given data matrices.

## Theorem 1 (Data-driven Hautus tests )

The data (U -, X) are informative for controllability if and only if Similarly, the data (U -, X) are informative for stabilizability if and only if As announced at the beginning of this section, there are situations in which we can conclude controllability or stabilizability from the data without being able to identify the true system uniquely. This can be seen by the fact that in order for to hold we require at least m + n separate measurements, whereas the conditions of Theorem 1 can hold for n measurements. This is illustrated in the following example.

## Example 1 (Full rank is not necessary)

Suppose that n = 2 and m = 1. Assume we collect data on the single time interval { 0, 1..., T } with T = 2 to obtain This implies that Using Theorem 1 we see that these data are informative for controllability, as Recall that this means that all systems consistent with the data are controllable. Therefore we can conclude that also the true system is controllable. Moreover, note that the rank condition does not hold, and therefore Σ D is not a singleton. To be precise: This means that there are multiple systems consistent with the data.

Computationally, the conditions and might seem daunting, since these require to test the rank of a matrix for each λ ∈ C. However, it is well known that in order for the classical Hautus test to be satisfied, it suffices to test the rank of for only λ ∈ σ ( A ), where σ ( A ) denotes the set of eigenvalues of the matrix A.

## Willems' fundamental lemma

A s explained in the main text, the input-state data satisfy the full row rank condition if and only if the data are informative for identification, meaning that the true system can be uniquely determined from the data by solving a linear equation. This brings up the question whether it is possible to choose a time horizon T and a finite input sequence u, u,..., u ( T -1 ) such that condition is guaranteed to hold for any resulting state sequence. Indeed, if this could be done, then the true system could be uniquely determined from the data by choosing a suitable input sequence. In this sidebar we will discuss this question in the context of persistently exciting inputs and Willems' fundamental lemma.

In the sequel, denote any given finite sequence f, f,..., f (T -1) by f [0, T -1]. For a given finite input sequence u [0, T -1], define the associated Hankel matrix of depth k by The input sequence u [0, T -1] is called persistently exciting of order k if Hk (u [0, T -1]) has full row rank.

A special case of Willems' fundamental lemma [36, Thm. 1] (originally proven in a behavioral context in [33, Thm. 1]) is relevant in the context of informativity for identification. Consider a linear input-state-output system, defined by the quadrupel of matrices (A, B, C, D), with input, state and output denoted by u, x and y respectively. Let x [0, T -1] and y [0, T -1] denote the finite length state and output trajectories corresponding to the input sequence u [0, T -1]. Suppose that the system is controllable and observable, and that the input sequence u [0, T -1] is persistently exciting of order n + L. Denote XL = [x · · · x (T -L)]. Then a consequence of Willems' fundamental lemma is that the In a similar fashion, the conditions of Theorem 1 can be verified in a finite number of steps. Indeed, is equivalent to for all λ = 0 with λ -1 ∈ σ (X -X ♯ +), where X ♯ + is any right inverse of X +. Regarding stabilizability, we obtain that is equivalent to

## Stabilization

After considering data-driven controllability and stabilizability analysis in the previous subsection, we now turn attention to data-driven control design. In particular, we has full row rank. A special case of this arises for L = 1, which shows that holds if we take u [0, T -1] to be persistently exciting of degree n + 1. This resolves the problem of designing inputs for informativity for identification in the context of inputstate measurements. More generally, in the case of input-output measurements, full row rank of (S1) enables the identification of the system matrices (A, B, C, D) up to similarity transformation if L is larger than the so-called lag of the system. This can be done, for example, by using subspace identification methods,.

On the other hand, in many applications an identified (state space) model might not be the most convenient representation to work. One of these applications is Data-enabled Predictive control (DeePC), introduced. As a data-driven variant of Model Predictive Control (MPC), the central problem is to minimize a cost function over all lengthL trajectories. A consequence of the fundamental lemma is that if the input sequence u [0, T -1] is persistently exciting of order n + L, then any ¯ u [0, L -1], ¯ y [0, L -1] is an input/output trajectory of the system if and only if As such, the fundamental lemma allows this problem to be formulated directly in terms of measurements, without explicitly finding a system model.

As it turns out, there are many other applications where avoiding the modeling step, and dealing with data directly is convenient. For example, the paper treats data-based simulation and output matching control, while provides methods for stabilization on the basis measurements for which holds. consider the quintessential control problem of stabilization by state feedback.

Recall the definition of informativity for control as given in Definition 2. We take the model class M and data D as before, and take as the control objective O: 'interconnection with a state feedback controller yields a stable 1, closed loop system'. This means that the set Σ O of all systems that satisfy the control objective is equal to the set of all stable n × n matrices For a given state feedback controller K ∈ R m × n, the corresponding set of closed loop systems consistent with 1 meaning Schur, that is, all its eigenvalues λ satisfy | λ | < 1. the data is equal to In line with Definition 2 we say that the data (U -, X) are informative for stabilization by state feedback if there exists a K ∈ R m × n such that Σ D (K) ⊆ M n × n stab.

At this point, one may wonder about the relation between informativity for stabilizability and informativity for stabilization. It is clear that the data ( U -, X ) are informative for stabilizability if ( U -, X ) are informative for stabilization by state feedback. However, the reverse statement does not hold in general. This is due to the fact that all systems ( A, B ) in Σ D may be stabilizable, but there may not exist a common feedback gain K such that A + BK is stable for all of these systems.

In other words, the input-state data ( U -, X ) are informative for stabilization by state feedback if there exists a single real m × n matrix K such that A + BK is stable for all ( A, B ) ∈ M that are consistent with the data.

The following example further illustrates the difference between informativity for stabilizability and informativity for stabilization.

## Example 2 (Stabilizability and stabilization)

Consider the scalar system x ( t + 1 ) = u ( t ), where x, u ∈ R. Suppose that we collect data on the single time interval { 0, 1 }, specifically, x = 0, u = 1 and x = 1. This means that U -= and X =. It can be shown that Σ D = { ( a, 1 ) | a ∈ R }. Clearly, all systems in Σ D are stabilizable. Nonetheless, the data are not informative for stabilization. This is because the systems ( -1, 1 ) and in Σ D cannot be stabilized by the same controller of the form u ( t ) = Kx ( t ). We conclude that informativity of the data for stabilizability does not imply informativity for stabilization by state feedback.

Having defined the notion of informativity for stabilization, we now take the steps described in the introduction. First, we resolve Problem 2, that is, we find necessary and sufficient conditions for informativity for stabilization by state feedback. After this, we design a corresponding controller, as described in Problem 3.

In order to do this, we first state a useful lemma. Recall from that (A, B) ∈ Σ D if and only if it is a solution of the the corresponding affine equation. Now let Σ 0 D denote the solution set of the corresponding homogeneous equation. That is, This allows us to state the following lemma.

## Lemma 1 (A necessary condition )

Suppose that the data (U -, X) are informative for stabi- lization by state feedback, and let K be a feedback gain such that A + BK is stable for all (A, B) ∈ Σ D. Then A 0 + B 0 K = 0 for all (A 0, B 0) ∈ Σ 0 D. Equivalently, The solution set of an affine equation is equal to the sum of any solution and the solution set of the corresponding homogenous equation. Since we know that (As, Bs) ∈ Σ D by definition, this means that we can write Using this, as a consequence of Lemma 1 we have that if K is a feedback gain such that A + BK is stable for all (A, B) ∈ Σ D, then that is, the set of closed-loop systems consistent with the data is a singleton. It is important to note, however, that this does not mean that Σ D is necessarily a singleton.

The above observation turns out to be instrumental in proving the following theorem, which gives necessary and sufficient conditions for informativity for stabilization by state feedback.

## Theorem 2 (Conditions for stabilization )

The data ( U -, X ) are informative for stabilization by state feedback if and only if the matrix X -has full row rank and there exists a right inverse X ♯ -of X -such that X + X ♯ -is stable.

Moreover, K is such that A + BK is stable for all ( A, B ) ∈ Σ D if and only if K = U -X ♯ -, where X ♯ -satisfies the above properties. In that case, A + BK = X + X ♯ -for all ( A, B ) ∈ Σ D.

Theorem 2 gives a characterization of all input-state data that are informative for stabilization by state feedback and provides a stabilizing controller. Nonetheless, the procedure to compute this controller might not be entirely satisfactory since it is not clear how to find a right inverse of X -that makes X + X ♯ -stable. In general, X -has many right inverses, and X + X ♯ -can be stable or unstable depending on the particular right inverse X ♯ -. To deal with this problem and to solve the design problem, we give a characterization of informativity for stabilization in terms of linear matrix inequalities (LMIs). The feasibility of such LMIs can be verified using standard tools.

LMI conditions for data-driven stabilization were first studied . In that work, the following conditions were presented under the additional assumption that the measurements satisfy, that is, the measurements are informative for system identification. As it turns out, this assumption can be removed, leading to the following result.

## Theorem 3 (LMI conditions for stabilization )

The data (U -, X) are informative for stabilization by state feedback if and only if there exists a matrix Θ ∈ R T × n satisfying Moreover, K is such that A + BK is stable for all (A, B) ∈ Σ D if and only if K = U -Θ (X -Θ) -1 for some matrix Θ satisfying.

The following example provides a simple illustration of the above results.

## Example 3 (Full rank not necessary for informativity)

Consider an unstable system (As, Bs), where As and Bs are given by We collect data from this system on a single time interval from t = 0 until t = 2, which results in the data matrices Clearly, the matrix X -is square and invertible, and it can be verified that is stable, since its eigenvalues are 1 2 (1 ± √ 2 i). We conclude by Theorem 2 that the data (U -, X) are informative for stabilization by state feedback. The same conclusion can be drawn from Theorem 3 since solves. Next, we can conclude from either Theorem 2 or Theorem 3 that the stabilizing feedback gain in this example is unique, and given by K = U -X -1 -= [-1 -0.5]. Finally, it is worth noting that the data are not informative for identification. In fact, (A, B) ∈ Σ D if and only if for some a 1 and a 2 ∈ R.

## The linear quadratic regulator problem

An important classical control design problem is the optimal linear quadratic regulator (LQR) problem. In this subsection we will study the data-driven version of this problem within the informativity framework.

For given state and input dimensions n and m, again consider the model class M of all discrete-time linear input-state systems. Assume we have input-state data on multiple time intervals, leading to data D: = ( U -, X ) as given . As before, the set Σ D of all systems in M that are consistent with the data is then given . We assume that the data are generated by the true (but unknown) system ( As, Bs ), which is therefore in Σ D itself.

In the context of the optimal LQR problem the control objective O is: 'the system must be controlled using the optimal feedback gain'. In order to formalize this, we introduce the following notation. For any given K, let Σ Q, R K denote the set of all systems of the form for which K is the optimal feedback gain corresponding to Q and R, that is, This gives rise to yet another notion of informativity in line with Definition 2. Indeed, informativity requires the existence of a single feedback gain that is optimal for all systems consistent with the data. For the definition of solvability of the optimal LQR problem we refer to the sidebar 'The linear quadratic regulator problem'.

## Definition 3 (Informativity for LQR)

Given matrices Q and R, we say that the data D = ( U -, X ) are informative for optimal linear quadratic regulation if the optimal LQR problem is solvable for all ( A, B ) ∈ Σ D and there exists K such that Σ D ⊆ Σ Q, R K.

An instrumental result in obtaining necessary and sufficient conditions for informativity for optimal linear quadratic regulation is the following lemma.

## Lemma 2 (Common solution of the Riccati equation)

Let Q = Q ⊤ be positive semidefinite and R = R ⊤ be positive definite. Suppose the data (U -, X) are informative for optimal linear quadratic regulation. Let K be such that Σ D ⊆ Σ Q, R K. Then, there exist a square matrix M and a positive semidefinite matrix P + such that for all (A, B) ∈ Σ D Statement of the lemma says that if the data are informative, there exists a common solution P + ⩾ 0 to the whole collection of AREs associated with systems (A, B) that are consistent with the data. Statement says that if K is the common optimal gain for all systems that are consistent with the data, then it must be of the expected form for all (A, B) consistent with the data. According to, the optimal closed loop system matrices A + BK are identical for all consistent pairs (A, B).

The following theorem gives necessary and sufficient

## The linear quadratic regulator problem

Consider the discrete time linear system where A and B are matrices of dimensions n × n and n × m, and where x is the n -dimensional state and u the m -dimensional input. In the linear quadratic regulator problem we quantify the performance of the system using a quadratic cost functional J (x 0, u) involving the state trajectory x and the input u. The optimal linear quadratic regulator problem is then the problem of finding, for each initial state x 0 of the system, an optimal input, i.e. an input that minimizes the cost functional. In this sidebar the basics of discrete-time linear quadratic optimal control are reviewed. In the sequel, the abbreviation 'LQR' will be used for 'linear quadratic regulator'.

For an initial state x 0, let x x 0, u be the state sequence of ( S2 ) resulting from the input u and initial condition x = x 0. We omit the subscript and simply write x whenever the dependence on x 0 and u is clear from the context.

Associated to system (S2), we define the quadratic cost functional where Q ∈ S n is positive semidefinite and R ∈ S m is positive definite. Then, the optimal LQR problem is the following:

## Problem 4 (The LQR problem)

Determine for every initial condition x 0 an input u ∗, such that lim t → ∞ x x 0, u ∗ ( t ) = 0, and the cost functional J ( x 0, u ) is minimized under this constraint.

Such an input u ∗ is called optimal for the given x 0. Of course, an optimal input does not necessarily exist for all x 0. We say that the optimal LQR problem is solvable for ( A, B, Q, R ) if for every x 0 there exists an input u ∗ such that

- 1) The cost J (x 0, u ∗) is finite. - 2) The limit lim t → ∞ x x 0, u ∗ (t) = 0. conditions for informativity for optimal linear quadratic regulation.

## Theorem 5 (Conditions for informativity )

Let Q ⩾ 0 and R > 0. Then the data ( U -, X ) are informative for optimal linear quadratic regulation if and only if at least one of the following two conditions hold:

- 1) The data (U -, X) are informative for identification, that is, Σ D = { (As, Bs) }, and the optimal LQR problem is solvable for (As, Bs, Q, R). In this case, the optimal feedback gain K is of the form where P + is the largest real symmetric solution to with - 3) The input u ∗ minimizes the cost functional, i.e., for all ¯ u such that lim t → ∞ x x 0, ¯ u (t) = 0.

In the sequel, we will require the notion of observable eigenvalues. An eigenvalue λ of A is called (Q, A) -observable if The following theorem provides necessary and sufficient conditions for the solvability of the optimal LQR problem for (A, B, Q, R). This theorem is the discrete-time analogue to the continuous-time case stated in [83, Thm. 10.18].

## Theorem 4 (Conditions for LQR)

Let Q ⩾ 0 and R > 0. Then the following statements hold:

- 1) If (A, B) is stabilizable, there exists a unique largest real symmetric solution P + to the discrete-time algebraic Riccati equation (DARE) in the sense that P + ⩾ P for every real symmetric P satisfying (S4). The matrix P + is positive semidefinite.

- 2) If, in addition to stabilizability of (A, B), every eigenvalue of A on the unit circle is (Q, A) -observable then for every x 0 a unique optimal input u ∗ exists. Furthermore, this input sequence is generated by the feedback law u = K x, where Moreover, the matrix A + BK is stable.

- 3) In fact, the optimal LQR problem is solvable for ( A, B, Q, R ) if and only if ( A, B ) is stabilizable and every eigenvalue of A on the unit circle is ( Q, A ) -observable.

If the optimal LQR problem is solvable for ( A, B, Q, R ), we say that the matrix K given by ( S5 ) is the optimal feedback gain for ( A, B, Q, R ).

- 2) For all ( A, B ) ∈ Σ D we have A = As. Moreover, As is stable, QAs = 0, and the optimal feedback gain is given by K = 0.

This theorem should be interpreted as follows. Condition 2) of Theorem 5 can be considered as a pathological case in which the only A consistent with the data is the true one, namely As. This matrix As is stable and QAs = 0. Since x ( t ) ∈ im As for all t > 0, we have Q x ( t ) = 0 for all t > 0 if the input function is chosen as u = 0. Additionally, since As is stable, this shows that the optimal input is equal to u ∗ = 0. If we set aside the pathological case 2), the main message of Theorem 5 is the following: if the data are informative for optimal linear quadratic regulation they are also informative for system identification, in the sense that the set of systems consistent with the data contains only one element, i.e., Σ D = { ( As, Bs ) }. This observation is consistent with the paper that showed the necessity of identifiability of the true system in adaptive LQ control.

At first sight, this might seem like a negative result in the sense that data-driven LQR is only possible with data that are also informative enough to uniquely identify the system. However, at the same time, Theorem 5 can be viewed as a positive result in the sense that it provides fundamental justification for the data conditions imposed in e.g.. Indeed, in the data-driven infinite horizon LQR problem 2 is solved using input-state data under the assumption that the input is persistently exciting of sufficiently high order. Under the latter assumption, the input-state data are informative for system identification, i.e., the matrices As and Bs can be uniquely determined from data. Theorem 5 justifies such a strong assumption on the richness of data in data-driven linear quadratic regulation. The data-driven finite horizon LQR problem was solved under a persistency of excitation assumption . Our results suggest that also in this case informativity for system identification is necessary for data-driven LQR, although further analysis is required to prove this claim.

Although Theorem 5 gives necessary and sufficient conditions under which the data are informative for optimal linear quadratic regulation, it might not be directly clear how these conditions can be verified given the input-state data. Therefore, in what follows we rephrase the conditions of Theorem 5 in terms of the data matrices X and U -.

## Theorem 6 (Alternative conditions for informativity )

Let Q ⩾ 0 and R > 0. Then the data ( U -, X ) are informative for optimal linear quadratic regulation if and only if at least one of the following two conditions hold:

- 1) The data (U -, X) are informative for identification, equivalently, there exists [V 1 V 2] such that Moreover, the optimal LQR problem is solvable for (As, Bs, Q, R), where As = X + V 1 and Bs = X + V 2.

- 2) There exists Θ ∈ R T × n such that X -Θ = (X -Θ) ⊤, U Θ = 0, 2 Note that the authors of formulate this problem as the minimization of the H 2-norm of a certain transfer matrix.

It is also possible to directly compute the optimal LQR feedback gain K from the given data. Indeed, the following theorem asserts that P + as in Lemma 2 can be found as the unique solution to an optimization problem involving only the data. Furthermore, the optimal feedback gain K can subsequently be found by solving a set of linear equations. In the sequel, for a given square matrix M, tr ( M ) will denote the trace of M.

## Theorem 7 (A semi-definite programming approach )

Let Q ⩾ 0 and R > 0. Suppose that the data (U -, X) are informative for optimal linear quadratic regulation. Consider the linear operator P ↦→L (P) defined by Let P + be as in Lemma 2. The following statements hold: 1) The matrix P + is equal to the unique solution to the optimization problem

- 2) There exists a right inverse X ♯ -of X -such that Moreover, if X ♯ -satisfies, then the optimal feedback gain is given by K = U -X ♯ -.

From a design viewpoint, the optimal feedback gain K can be found in the following way. First solve the semidefinite program in Theorem 7. Subsequently, compute a solution X ♯ -to the linear equations X -X ♯ -= I and. Then, the optimal feedback gain is given by K = U -X ♯ -.

## The problem of tracking and regulation

Yet another important classical control design problem is the problem of tracking and regulation, also called the algebraic regulator problem, as studied, for example, in - and the textbooks, ). This is the problem of finding a feedback controller (called a regulator) such that the output of the resulting controlled system tracks a given reference signal, regardless of the disturbance input entering the system and the initial state. The relevant reference signals and disturbances (such as step functions, ramps or sinusoids) are assumed to be solutions of a suitable autonomous linear system. Given a class of reference and disturbance signals, one first constructs a suitable autonomous system (called the exosystem) that has these reference and disturbance signals as solutions. Next, this exosystem is interconnected to the system to be controlled (called the endosystem) and the difference between the original system output and the reference signal is taken as output. Finally, a regulator should be designed to make the output of the interconnection converge to zero for all disturbances and initial states.

In a data-driven context, the true endosystem is assumed to be unknown, and no mathematical model is available. Instead, we collect data on the input, endosystem state, and exosystem state in the form of samples on a finite time-interval. Whereas the true endo-system is unknown, the exosystem is assumed to be known, since this system models the reference signals and possible disturbance inputs. Also, the matrices in the output equations are assumed to be known, since these specify the design specification (namely the output that should converge to zero) on the controlled system. A given set of data will then be called informative for regulator design if the data contain sufficient information to design a single regulator for the entire family of systems that are consistent with this set of data. In this section we will study this data-driven regulator problem, and provide necessary and sufficient conditions for informativity for regulator design.

Consider a true, unknown, endosystem represented by Here, x 2 is the n 2 -dimensional state, u the m -dimensional input, and x 1 the n 1-dimensional state of the exosystem that generates all possible reference signals and disturbance inputs. The dimensions n 1, n 2 and m are known, but the matrices A 2 s and B 2 s are unknown. Since A 3 specifies how the disturbances and reference signals enter the system, we assume that it is known. Also the exosystem matrix A 1 is known. The output to be regulated is specified by where the matrices D 1, D 2 and E are known. By interconnecting the endosystem with the state feedback controller we obtain the controlled system If z (t) → 0 as t → ∞ for all initial states x 1 and x 2, we say that the controlled system is output regulated. If A 2 s + B 2 sK 2 is a stable matrix we call the controlled system endo-stable. If the control law makes the controlled system both output regulated and endo-stable, we call it a regulator.

Since we do not know the true endosystem, the design of a regulator can only be based on available data.

These data are finite sequences of samples of x 1 (t), x 2 (t) and u (t) on a given time interval { 0, 1,..., T } given by An endosystem with (unknown) system matrices (A 2, B 2) is called consistent with these data if A 2 and B 2 satisfy the equation The set of all (A 2, B 2) that are consistent with the data is denoted by Σ D, i.e., We assume that the true endosystem (A 2 s, B 2 s) is in Σ D, i.e. the true system is consistent with the data. In general, the equation does not specify the true system uniquely, and many endosystems (A 2, B 2) may be consistent with the same data.

Now we turn to controller design based on the data ( U -, X 1 -, X 2 ). Since on the basis of the given data we can not distinguish between the true endosystem and any other endosystem consistent with these data, a controller will be a regulator for the true system only if it is a regulator for any endosystem with ( A 2, B 2 ) in Σ D. If such regulator exists, we call the data informative for regulator design. More precisely:

## Definition 4 (Informativity for regulator design)

We say that the data ( U -, X 1 -, X 2 ) are informative for regulator design if there exists K 1 and K 2 such that the control law u ( t ) = K 1 x 1 ( t ) + K 2 x 2 ( t ) is a regulator for any endosystem with ( A 2, B 2 ) in Σ D.

In this subsection we will present necessary and sufficient conditions on the data ( U -, X 1 -, X 2 ) to be informative for regulator design. Also, in case that these conditions are satisfied, we will explain how to compute a regulator using only these data.

The following theorem gives necessary and sufficient conditions on the data to be informative for regulator design, and explains how suitable regulators are computed using only these data.

## Theorem 8 (Conditions for informativity )

Assume that the matrix A 1 is anti-stable 3. Then the data (U -, X 1 -, X 2) are informative for regulator design if and 3 Anti-stable means that all its eigenvalues λ satisfy | λ | ⩾ 1

- only if at least one of the following two conditions hold 4: 1) has full row rank, and there exists a right-inverse - -2) X 2 -has full row rank and there exists a right-inverse X ♯ 2 -of X 2 -such that (X 2 + -A 3 X 1 -) X ♯ 2 -is stable. Moreover, there exists a solution W to the linear equations - X 2 -X ♯ 2 -of X 2 -such that (X 2 + -A 3 X 1 -) X ♯ 2 -is stable and D 2 + EU -X ♯ 2 -= 0. Moreover, im D 1 ⊆ im E. In this case, a regulator is found as follows: choose K 1 such that D 1 + EK 1 = 0 and define K 2: = U -X ♯ 2.

In this case, a regulator is found as follows: choose K 1: = U -( I -X ♯ 2 -X 2 -) W and K 2: = U -X ♯ 2 -.

This theorem can be applied as follows. What we know about the system are the system matrices A 1, A 3, D 1, D 2 and E and the data ( U -, X 1 -, X 2 ). The aim is to use this knowledge to compute a single regulator ( K 1, K 2 ) that works for all endosystems ( A 2, B 2 ) in the set Σ D defined .

In order to check the existence of such regulator, we verify the two conditions 1) and 2) in Theorem 8. If neither of the two conditions holds, then the data are not informative. On the other hand, if condition 1) holds then a regulator ( K 1, K 2 ) is computed as follows:

- » fi nd a right-inverse X ♯ 2 -of X 2 -such that the matrix (X 2 + -A 3 X 1 -) X ♯ 2 -is stable and D 2 + EU -X ♯ 2 -= 0, » compute K 1 as a solution of D 1 + EK 1 = 0, -If condition 2) holds then a regulator is computed as follows:

- -» fi nd a solution W of the data-driven regulator equations, - » fi nd a right-inverse X ♯ 2 -of X 2 -such that the matrix (X 2 + -A 3 X 1 -) X ♯ 2 is stable, -Although Theorem 8 gives a characterization of all data that are informative for regulator design and gives a method to design a suitable regulator, the procedure to compute this regulator is not entirely satisfactory. Indeed, in the case that condition 2) holds it is not clear how to find a right inverse of X 2 -such that (X 2 + -A 3 X 1 -) X ♯ 2 -is stable. In the case of condition 1), the additional constraint D 2 + EU -X ♯ 2 -= 0 needs to be satisfied. In general, X 2 -has many right inverses, and (X 2 + -A 3 X 1 -) X ♯ 2 -can be stable, with or without D 2 + EU -X ♯ 2 -= 0, depending on the choice of the particular right inverse X ♯ 2 -. To deal with this problem and to solve the problem of regulator 4 We denote by im M the image of the matrix M. design, the problem of finding a suitable right inverse can be reformulated in terms of feasibility of an LMI, drawing some inspiration from Theorem 3.

## Theorem 9 (An LMI approach )

Let ( U -, X 1 -, X 2 ) be given data. Then the following hold:

- 1) X 2 -has full row rank and has a right inverse X ♯ 2 -such that ( X 2 + -A 3 X 1 -) X ♯ 2 -is stable if and only if there exists a matrix Θ ∈ R T × n such that

- 2) X 2 -has full row rank and has a right inverse X ♯ 2 -such that (X 2 + -A 3 X 1 -) X ♯ 2 -is stable, in addition, D 2 + EU -X ♯ 2 -= 0 if and only if there exists a solution Θ ∈ R T × n of and that satisfies the linear equation In both cases, a suitable right-inverse is given by X ♯ 2 -: = Θ (X 2 -Θ) -1.

It is also possible to consider the situation that, in addition to A 2 and B 2, the matrix A 3 (representing how the exosignal x 1 enters the endosystem) is unknown. In that case, the set all endosystems consistent with the data (U -, X 2, X -) is given: The data are then called informative for regulator design if there exists a single regulator u = K 1 x 1 + K 2 x 2 for all endosystems in Σ D. The analogue of Theorem 8 for this situation is as follows.

## Theorem 10 (Conditions for informativity )

Assume that the matrix A 1 is anti-stable. Then the data ( U -, X 1 -, X 2 ) are informative for regulator design if and only if at least one of the following two conditions hold:

- 1) X 2 -has full row rank, and there exists a rightinverse X ♯ 2 -of X 2 -such that X 1 -X ♯ 2 -= 0, (X 2 + -A 3 X 1 -) X ♯ 2 -is stable and D 2 + EU -X ♯ 2 -= 0. Moreover, im D 1 ⊆ im E. In this case, a regulator is found as follows: choose K 1 such that D 1 + EK 1 = 0 and define K 2: = U -X ♯ 2. 2. -2) X 2 -has full row rank and there exists a rightinverse X ♯ 2 -of X 2 -such that X 1 -X ♯ 2 -= 0 and (X 2 + -A 3 X 1 -) X ♯ 2 -is stable. Moreover, there exists a solution W to the linear equations In this case, a regulator is found as follows: choose K 1: = U -(I -X ♯ 2 -X 2 -) W and K 2: = U -X ♯ 2 -.

Note that, as expected, A 3 no longer appears in the equations (it is unknown). In both cases, the formulas for K 1 and K 2 are the same as in Theorem 8.

Finally, we illustrate the application of Theorem 8 in the following example.

## Example 4 (Illustration of the theory)

Consider the two-dimensional endosystem where A 2 s and B 2 s are unknown 2 × 2 and 2 × 1 matrices, respectively. Let x 2 = [x 21 x 22] T. The disturbance input d is assumed to be a constant signal with finite amplitude, so is generated by d (t + 1) = d (t). We want to design a regulator so that 2 x 21 + 1 2 x 22 tracks a given reference signal. In this example, the reference signals r are assumed to be generated by a given autonomous linear system with state space dimension, say, n 1. Its representation will be irrelevant here. The total exosystem will then have state space dimension n 1 + 1, and our output equation is given by z (t) = D 1 x 1 (t) + D 2 x 2 (t) + E u (t), with D 1 a 1 × (n 1 + 1) matrix such that D 1 x 1 = -r and D 2 =. We take E = 2. Also note that A 3 = [01 × n 1 0 01 × n 1 1]. Here, 0 1 × n 1 denotes 1 × n 1 zero matrix. Suppose that T = 2 and assume we have the following data: These data can be seen to be generated by the true endosystem A 2 s =, B 2 s =. We now check condition 1) of Theorem 8. First note that, indeed, im D 1 ⊆ im E. Also, X 2 -is non-singular and (X 2 + -A 3 X 1 -) X -1 2 -=. This matrix has eigenvalues 1 2 ± 1 2 i, so is stable. Finally, D 2 + EU -X -1 2 -= 0. According to Theorem 8, a regulator for all endosystems consistentwith the given data is given by It can be verified that the set of endosystems consistentwith our data is equal to the affine set The controller given by is a regulator for all these endosystems.

Data-driven regulator design has also been studied in and. The perspective of these contributions is however quite different from the one discussed in this subsection. We also mention alternative methods that deal with tracking objectives, such as iterative feedback tuning (IFT) and virtual reference feedback tuning (VRFT) as developed in and, respectively. Also these methods do not address the classical regulator problem, and are very different from the work discussed here.

## ANALYSIS AND CONTROL USING NOISY INPUT-STATE DATA

So far, we have focused on analysis and design of inputstate systems using exact data. In this section, we shift our attention to input-state systems with noise. We will first introduce the model class that we will be using, and discuss the assumptions that will be made on the noise samples.

Suppose that the unknown, true system is given by where x ∈ R n is the state, u ∈ R m is the control input and w ∈ R n is an unknown noise term. The matrices As ∈ R n × n and Bs ∈ R n × m denote the unknown state and input matrices. We embed this unknown system into the model class M of all input-state systems with unknown process noise, with fixed dimensions n and m, of the form Suppose that we obtain input-state data from the true system. These data are given in the matrices We denote the submatrix of X consisting of its first (respectively, last) T columns by X -(respectively, X +). The noise w is unknown, so w, w,..., w (T -1) are not measured, and therefore are not part of the data. We do however assume that we have the following information on the noise during the data sampling period.

## Assumption 11 (Noise model)

The unknown noise samples w, w,..., w (T -1), collected in the matrix satisfy the quadratic matrix inequality where Φ ∈ S n + T is a given partitioned matrix with Φ 11 ∈ S n, Φ 12 ∈ R n × T, Φ 21 = Φ ⊤ 12 and Φ 22 ∈ S T, and where we assume that Φ ∈ Π n, T (as defined in (S7) of the Sidebar 'Quadratic matrix inequalities').

In other words, the data D consist of the measurements ( U -, X ) together with the information that the noise on the sampling interval { 0,..., T } satisfies the inequality for a partitioned matrix Φ ∈ Π n, T.

Of course, an issue is whether the set of noise matrices W -defined by is nonempty. This is equivalent to the nonemptiness of the set Z T ( Φ ), as defined in ( S6 ). This issue is discussed in more detail in the Sidebar 'Quadratic matrix inequalities'. Indeed, under the assumption Φ ∈ Π n, T the set Z T ( Φ ) is nonempty and convex. Consequently then, the set of of noise matrices W -satisfying is nonempty and convex.

In order to make the above quadratic inequality constraint on the matrix of noise samples more concrete, we will now look at a number of special cases.

- 1) In the special case Φ 12 = 0 and Φ 22 = -I, the quadratic inequality reduces to The inequality can be interpretated as saying that the energy of w has a given upper bound on the time interval { 0,..., T -1 }.

- 3) In some cases, we may know a priori that the noise w does not directly affect the entire state-space, but is contained in a subspace, say im E, with E a known n × d matrix. This prior knowledge can be captured by the noise model in Assumption 11. Indeed, suppose that w (t) = E ˆ w (t) for all t = 0, 1, 2..., T -1, where ˆ w (t) ∈ R d and E ∈ R n × d is a given matrix of full column rank. The matrix ˆ W -= [ˆ w ˆ w · · · ˆ w (T -1)] captures the noise. As before, ˆ W -is unknown but is assumed to satisfy ˆ W ⊤ -∈ Z T (ˆ Φ), where ˆ Φ ∈ Π d, T is such that ˆ Φ 22 < 0. It can then be shown that W -= E ˆ W -for some ˆ W ⊤ -∈ Z T (ˆ Φ) if and only if W ⊤ -∈ Z T (Φ), where - 2) Norm bounds on the individual noise samples w (t) also give rise to bounds of the form, although this does introduce some conservatism in general. Indeed, note that for all t the pointwise norm bound ‖ w (t) ‖ 2 2 ⩽ ϵ is equivalent to the matrix inequality w (t) w (t) ⊤ ⩽ ϵ I. As such, the bound is satisfied for Φ 11 = T ϵ I.

The conclusion is that Assumption 11 also covers the case in which the noise is constrained to a known subspace, which is captured by the noise bound with Φ .

- 4) As shown in [70, Section 5.4], these noise models can also be applied in settings of Gaussian noise. To be precise, such sets can be employed as confidence intervals corresponding to a given probability.

## Quadratic stabilization

In this subsection we will take a look at the problem of quadratic stabilization using noisy input-state data. Quadratic stabilization means that all systems in the set Σ D of systems consistent with the data can be stabilized by the same state feedback gain, with a common Lyapunov function for all closed loop systems. In particular then, this feedback gain will stabilize the unknown system. Conditions for the existence of such feedback gain will be in terms of feasibility of certain linear matrix inequalities involving the data ( X, U -) and the (known) matrix Φ representing the quadratic inequality constraint on the matrix of noise samples. In addition, the controller gain will be computed in terms of solution to these linear matrix inequalities.

As explained before, we have access to the input-state data D = (U -, X). The possible matrices W -of noise samples satisfy the quadratic inequality for a given matrix Φ ∈ Π n, T. This means that the set Σ D of all systems consistent with the data is equal to the set of all systems (A, B) satisfying for some W -satisfying, i.e., Σ D = { (A, B) | holds for some W -satisfying }.

## Definition 5 (Informativity for quadratic stabilization)

The data (U -, X) are called informative for quadratic stabilization if there exists a feedback gain K ∈ R m × n and a matrix P ∈ S n such that P > 0 and We are interested in quadratic stabilization in the sense that we ask for a common Lyapunov matrix P for all (A, B) ∈ Σ D. Note that P > 0 satisfies if and only Q: = P -1 satisfies Q -(A + BK) ⊤ Q (A + BK) > 0, which expresses that V (x) = x T Qx is a Lyapunov function for the system x (t + 1) = (A + BK) x (t).

Definition 5 leads to two natural problems. First, we are interested in the question under which conditions the data are informative. The second problem is a design issue: we are interested in procedures to come up with a feedback gain that stabilizes all systems in Σ D. By making use of the

## Quadratic matrix inequalities

A great deal can be said about sets defined in terms of quadratic matrix inequalities (QMIs). Such sets play an important role in robust control, where they are used to describe parameter uncertainty -. Also in the context of this paper they are important, since they describe sets of systems consistent with the data. We will briefly discuss sets of the form   for Π ∈ S q + r, and we refer to for more details. In what follows, we assume that Π ∈ S q + r is partitioned as where Π 11 ∈ S q, Π 12 = Π ⊤ 21 ∈ R q × r and Π 22 ∈ S r. The very first question one may ask is: under what conditions on Π is the set Z r (Π) nonempty? An immediate necessary condition is that Π must have at least q nonnegative eigenvalues. However this is not sufficient in general. It turns out that for particular matrices Π, a Schur complement argument on the matrix Π leads to a simple characterization of nonemptiness of the set Z r (Π). Specifically, suppose that Π 22 ⩽ 0 and ker Π 22 ⊆ ker Π 12. Since the latter condition is equivalent to Π 12 Π 22 Π † 22 = Π 12, we have that where Π | Π 22: = Π 11 -Π 12 Π † 22 Π 21 is the (generalized) Schur complement of Π with respect to Π 22. This can be used to prove the following conditions for nonemptiness of Z r (Π).

## Theorem 12 (Nonemptiness of Z r ( Π ) )

Let Π ∈ S q + r and assume that ker Π 22 ⊆ ker Π 12. Then Z r ( Π ) is nonempty if Π | Π 22 ⩾ 0. Moreover, under the assumption that Π 22 ⩽ 0 we have that Z r ( Π ) is nonempty if and only if Π | Π 22 ⩾ 0.

## Motivated by this, we define the set

Next, for Π ∈ Π q, r we will investigate properties of the sets Z r (Π) and the following closely related set  involving a strict inequality.

## MATRIX VERSIONS OF YAKUBOVICH'S S-LEMMA

Yakubovich' S-lemma is a classical result with a wide range of applications, most notably the problem of absolute stability of Lur'e systems. Roughly speaking, this result says that one quadratic inequality implies another one if and only if a certain linear matrix inequality (LMI) is feasible. A seemingly difficult implication involving quadratic functions is thereby replaced by a convex problem which can be solved using computational tools such as Sedumi and Mosek. In this section we deal with matrix versions of the S-lemma, i.e., with the question under what conditions all solutions to one quadratic matrix inequality also satisfy another QMI. In other words, we state necessary and sufficient conditions for the inclusion Z r (N) ⊆ Z r (M), where M, N ∈ S q + r. We will also consider a similar inclusion with Z + r (M) instead of Zr (M). This leads to non-strict and strict versions of Y akubovich's S-lemma.

## Non-strict inequalities

The following theorem states the matrix S-lemma for nonstrict inequalities.

## Theorem 13 (Matrix S-lemma )

Let M, N ∈ S q + r. If there exists a real α ⩾ 0 such that M -α N ⩾ 0, then Z r ( N ) ⊆ Z r ( M ). Next, assume that N ∈ Π q, r and N has at least one positive eigenvalue. Then Z r ( N ) ⊆ Z r ( M ) if and only if there exists a real α ⩾ 0 such that M -α N ⩾ 0.

Similar to the 'standard' S-lemma we note that the matrix S-lemma requires N to have at least one positive eigenvalue, an assumption known as the Slater condition. It turns out, however, that under additional assumptions on M and N, a result similar to Theorem 13 holds when N has no positive eigenvalues. This leads to a matrix version of Finsler's lemma, which will not be further discussed here.

## A strict and non-strict inequality

Next, we consider strict versions of the matrix S-lemma. This means that we consider the set Z + r ( M ) instead of Z r ( M ), i.e., a strict inequality on the QMI induced by M. Note that in this case, the Slater condition on N is not required.

## Theorem 14 (Strict matrix S-lemma )

Let M, N ∈ S q + r. If there exists a real α ⩾ 0 such that M -α N > 0, then Z r ( N ) ⊆ Z + r ( M ). Next, assume that N ∈ Π q, r and N 22 < 0. Then Z r ( N ) ⊆ Z + r ( M ) if and only if there exists a real α ⩾ 0 such that M -α N > 0.

It is also possible to proceed if N 22 is not necessarily negative definite, but an extra condition on M holds. In that case two real numbers α ⩾ 0 and β > 0 are required to arrive at a necessary and sufficient condition.

Theorem 15 (Strict matrix S-lemma with α and β) Let M, N ∈ S q + r. Then Z r (N) ⊆ Z + r (M) if there exist scalars α ⩾ 0 and β > 0 such that Next, assume that N ∈ Π q, r and M 22 ⩽ 0. Then Z r (N) ⊆ Z + r (M) if and only if there exist α ⩾ 0 and β > 0 such that (S9) holds. linear equation and the assumption on the noise, it is straightforward to see that (A, B) ∈ Σ D if and only if Next, suppose that we fix a Lyapunov matrix P > 0 and a feedback gain K. The inequality is equivalent to which is also a quadratic matrix inequality in A and B. Therefore, finding conditions for quadratic stabilization amounts to finding conditions under which the quadratic matrix inequality holds for all (A, B) satisfying the quadratic matrix inequality. Let N be defined by Then we need to find conditions on the data such that there exist P > 0 and K such that the inclusion holds. In order to find such conditions, we can use a matrix version of the S-lemma, as reported in Theorem 15 of the Sidebar 'Quadratic matrix inequalities'. It is straightforward to verify the assumptions of this result, i.e., M 22 ⩽ 0 and N ∈ Π n, T. Theorem 15 then asserts that holds if and only if there exist scalars α ⩾ 0 and β > 0 such that From a design point of view, the matrices P and K that appear in M are not given. However, the idea is now to compute matrices P, K and scalars α and β such that holds. In fact, by the above discussion, the data (U -, X) are informative for quadratic stabilization if and only if there exist P ∈ S n, P > 0, K ∈ R m × n and two scalars α ⩾ 0 and β > 0 such that holds. We note that (in particular, M) is not linear in P and K. Nonetheless, by a rather standard change of variables and a Schur complement argument, we can transform into a linear matrix inequality. Moreover, it turns out that the scalar α is necessarily positive. By a scaling argument then, it can be chosen to be equal to 1. We summarize our result in the following theorem.

## Theorem 16 (Informativity for quadratic stabilization )

Suppose that the data (U -, X) are collected from system with noise as in Assumption 11. The data (U -, X) are informative for quadratic stabilization if and only if there exist P ∈ S n, P > 0, L ∈ R m × n and a scalar β > 0 satisfying Moreover, if P and L satisfy then K: = LP -1 is a stabilizing feedback gain for all (A, B) ∈ Σ D.

Theorem 16 provides a necessary and sufficient condition under which quadratically stabilizing controllers can be obtained from noisy data. The theorem leads to an effective design procedure for obtaining stabilizing controllers directly from data. Indeed, the approach entails solving the linear matrix inequality for P, L and β and computing a controller as K = LP -1. Below, we discuss some of the features of our control design procedure.

- 1) First of all, we stress that the procedure is nonconservative since Theorem 16 provides a necessary and sufficient condition for obtaining quadratically stabilizing controllers from data. - 2) The variables P, L and β are independent of the time horizon T of the experiment. In fact, note that P ∈ R n × n, L ∈ R m × n and β ∈ R. Also, the LMI is of dimension (3 n + m) × (3 n + m) and thus independent of T. This T -independent design method can play a crucial role in control design from larger data sets. We note that collections of big data sets are often unavoidable, for example because the signal-to-noise ratio is small, or because the data-generating system is large-scale.

We note that under the extra assumptions Φ 22 < 0 and it is possible to prove a variant Theorem 16 in which the non-strict inequality is replaced by a strict inequality, and the term -β I is removed. This can be done by invoking Theorem 14 of Sidebar 'Quadratic matrix inequalities', which is possible since the conditions Φ 22 < 0 and yield N 22 < 0. Thus we obtain the following theorem.

## Theorem 17 (Informativity via a strict inequality )

Suppose that the data (U -, X) are collected from system with noise as in Assumption 11. In addition, assume that Φ 22 < 0 and the rank condition holds. Then the data (U -, X) are informative for quadratic stabilization if and only if there exist P ∈ S n, P > 0 and L ∈ R m × n satisfying Moreover, if P and L satisfy then K: = LP -1 is a stabilizing feedback gain for all (A, B) ∈ Σ D.

Assume now that Φ 22 < 0 . Under this assumption, it turns out that if the data ( U -, X ) are informative for quadratic stabilization and if K stabilizes all systems in Σ D with a common Lyapunov matrix P > 0, then, in fact, X -must have full row rank, and K must be of the form K = U -X ♯ -for some right inverse X ♯ -of X -. Thus, the following theorem extends Lemma 1 to the noisy case.

## Theorem 18 (Necessary conditions for informativity )

Suppose that the data (U -, X) are collected from system with noise as in Assumption 11. In addition, assume Φ 22 < 0. Let the data (U -, X -) be informative for quadratic stabilization and suppose that P > 0 and K are such that holds. Then Consequently, X -has full row rank n and there exists a right-inverse X ♯ -of X -such that K = U -X ♯ -.

## Related conditions for quadratic stabilization

Theorem 17 gives a necessary and sufficient LMI condition under which all systems consistent with the data are quadratically stabilizable by a single feedback gain K. In this section we compare this result to other conditions within the literature on data-driven control.

We begin with [22, Thm. 6]. This result works under the assumption that holds, and X + has full row rank. Moreover, it is assumed that for some γ > 0. Under these assumptions, [22, Thm. 6] states that the data (U -, X) are informative for quadratic stabilization if there exists a matrix Q ∈ R T × n and a scalar α > 0 such that X -Q is symmetric and If (Q, α) solve, then K: = U -Q (X -Q) -1 quadratically stabilizes all systems in Σ (U -, X). We note that the inequality can be interpreted as a special case of with Φ 11 = γ X + X ⊤ +, Φ 12 = 0 and Φ 22 = -I.

Yet another condition for quadratic stabilization is given. This paper works with a noise model that can be interpreted as the dual of. More precisely, it is assumed that for known matrices Qw ∈ S n, Sw ∈ R n × T and Rw ∈ S T with Rw > 0. To make a meaningful comparison, we will assume the same bound as. This can also be stated equivalently in terms of the noise model by choosing the specific matrices Qw = -(γ X + X ⊤ +) -1, Sw = 0 and Rw = I. Then, the main result of [100, Cor. 6, Rem. 7] is that the data (U -, X) are informative for quadratic stabilization if there exist matrices Y ∈ S n and M ∈ R T × n satisfying We note that the conditions from and are stated as sufficient conditions for quadratic stabilization. It is an interesting question whether these conditions are also necessary for quadratic stabilization. Indeed, in this case, they would then be equivalent to those of Theorem 17 (for the noise model in). It turns out, however, that this is not the case.

To show this, one can consider the true system described by the matrices As = 1 and Bs = 1. Suppose that T = 3 and the noise matrix is given by We collect the data samples Throughout the example, we assume that we have access to the noise bound W -W ⊤ -⩽ 1. Note that this bound is indeed satisfied, and that it can be captured using Assumption 11 by the choices Φ 11 = 1, Φ 12 = 0 and Φ 22 = -I. We also note that this is equivalent to noise model with Qw = -1, Sw = 0 and Rw = I, and to noise model with γ = 1. As such, we can compare the design methods reported in Theorem 17 of this paper with the approaches in [100, Cor. 6, Rem. 7] and [22, Thm. 6].

For this example, it can be shown analytically that only the LMI condition of Theorem 17 is feasible while those in - and - are not. At a high level, the reason for this is that the approach of relies on a number of possibly conservative bounds, while the method from utilizes an overparameterization of the set of consistent systems.

## The H ∞ control problem

Denote by ℓ q 2 (Z +) the linear space of all sequences v with v (t) ∈ R q and t ∈ Z + such that ∑ ∞ t = 0 ‖ v (t) ‖ 2 < ∞. For any such sequence v, define its ℓ 2-norm as The informativity framework also allows a treatment of the data-driven H ∞ control problem. This will be the topic of the current subsection. We first review some basic material that will be needed in order to formulate the problem.

Next, consider the discrete-time input-state-output system with w (t) ∈ R q and z (t) ∈ R p. Let its transfer matrix be denoted by G (z): = C (zI -A) -1 E + D. If we take as initial state x = 0, then each input sequence w on Z + yields a unique output sequence z on Z +. If A is stable, then this output sequence z is in ℓ p 2 (Z +) whenever w is in ℓ q 2 (Z +). The H ∞ performance of is now defined as Due to the fact that A is stable, the H ∞ performance is indeed a finite number, and is in fact equal to the H ∞ -norm of the transfer matrix G (z), which is given by As is well known, the famous bounded real lemma gives necessary and sufficient conditions for the H ∞ performance to be strictly less than a given tolerance:

## Proposition 1 (Discrete-time bounded real lemma)

Consider the system. Let γ > 0. Then A is stable and J H ∞ < γ if and only if there exists P > 0 such that The data-driven H ∞ control problem in the context of noisy input-state data deals with the true (but unknown) system where x ∈ R n is the state, u ∈ R m is the control input and w ∈ R n is an unknown noise input. The matrices As and Bs denote the unknown state and input matrices. As model class M we take the set of all input-state systems with unknown noise inputs, with given, known, dimensions n and m, of the form We assume that data (U -, X) have been collected on the time interval { 0, 1,..., T }. Since the noise input w is unknown, the noise samples w, w,..., w (T -1) are not measured, and are therefore not part of the data. However, we adopt the noise model specified in Assumption 11, and assume that the (unknown) matrix W -= [w w · · · w (T -1)] satisfies the quadratic matrix inequality for a given, known, partitioned matrix Φ ∈ Π n, T.

As before, the set Σ D of all systems in M that are consistent with the data (U -, X) is then equal to the set of all (A, B) that satisfy the QMI A standing assumption remains that the unknown system is consistent with the data, i.e., is in Σ D, i.e., (As, Bs) satisfies the QMI.

We associate to the output equation where z (t) ∈ R p, and C and D are known matrices. For any (A, B) ∈ Σ D, the feedback law u = K x yields the closedloop system Denote the transfer matrix of the closed loop system by GK (z). For any K such that A + BK is stable, the H ∞ performance associated with is then given by Let γ > 0. By applying Proposition 1 to the closed loop system, the matrix A + BK is stable and J H ∞ (K) < γ if and only if there exists a matrix P > 0 such that where AK: = A + BK and CK: = C + DK. In order to make this applicable to data-driven H ∞ control design, will be restated in a different form. Clearly, P > 0 satisfies if and only if Since P -1 2 (γ 2 I -P) P -1 2 = γ 2 (P -1 -1 γ 2 I) and P + P (γ 2 I -P) -1 P = (P -1 -1 γ 2 I) -1, the inequalities and can be reformulated as This leads to the following definition of informativity for H ∞ control.

## Definition 6 (Informativity for H ∞ control)

Let γ > 0. The data ( U -, X ) are informative for H ∞ control with performance γ if there exist matrices P > 0 and K such that and hold for all ( A, B ) ∈ Σ D.

Of course, if K satisfies the conditions of Definition 6, then it is a suitable control gain for all ( A, B ) ∈ Σ D, in the sense that A + BK is stable and J H ∞ ( K ) < γ for all ( A, B ) ∈ Σ D.

The problem is now to derive necessary and sufficient conditions for informativity, and to find a suitable control gain. By pre- and postmultiplication of by P -1 we obtain that and are equivalent to where we define Y: = P -1, L: = KY, AY, L: = AY + BL and CY, L: = CY + DL. Next, note that holds if and only if which in turn is equivalent to Note that is independent of A and B. In addition, we can write as A crucial observation is now that the inequality is of a form where A and B appear on the left and their transposes appear on the right, analogous to and. As before, let and let M be defined by Then, for given γ > 0, informativity for H ∞ control with performance γ holds if and only if there exist matrices Y > 0 and L that satisfy the inequality Y -C ⊤ Y, L CY, L > 0 with in addition Moreover, in that case a suitable control gain is given by K = LY -1.

Using the sets (S6) and (S8) introduced in 'Quadratic Matrix Inequalities', condition is equivalent to This observation brings us in a position to apply Corollary 15. In fact, combining Corollary 15 with some suitable Schur complement arguments leads to the following necessary and sufficient conditions for informativity for H ∞ control with a given performance. In addition, a control gain is computed that achieves H ∞ performance strictly less that γ for all systems consistent with the data.

## Theorem 19 (Conditions for informativity)

Suppose that the data (U -, X) are collected from system with noise as in Assumption 11. In addition, let γ > 0. Then the data (U -, X) are informative for H ∞ control with performance γ if and only if there exist matrices Y ∈ S n, L ∈ R m × n and scalars α ⩾ 0 and β > 0 satisfying Moreover, if Y and L satisfy then K: = LY -1 is such that A + BK is stable and J H ∞ (K) < γ for all (A, B) ∈ Σ D.

If Y and L satisfy then K: = LY -1 and P: = Y -1 satisfy for all (A, B) in the set Σ D of systems consistent with the data. Clearly, implies that for all t ∈ Z +, where x, w and z satisfy the closed loop system equations. This can be interpreted as saying that the system is dissipative with respect to the supply rate with storage function x ⊤ Px. In other words: the control law u = K x with K: = LY -1 makes all systems in Σ D dissipative with common storage function given by P: = Y -1.

## Dissipativity analysis

In this subsection, we study dissipativity of linear finitedimensional input-state-output systems from a data-driven perspective. This problem has received considerable attention, and we mention the papers as the approaches that are closest to the one taken here. In, the notion of (finite-horizon) L -dissipativity was introduced. This was further studied . Both contributions rely on the notion of persistently exciting input data (see and the sidebar 'Willems' fundamental lemma"). This property of the input sequence implies that the data-generating system is uniquely identifiable from the data.

In this paper we adopt the more classical notion of dissipativity for linear systems, rather than L -dissipativity. Indeed, we consider a setup similar to that of, where sufficient data-based conditions were given for dissipativity. Here, we employ the informativity approach to derive necessary and sufficient conditions.

We will first review the definition of dissipativity. Consider a discrete-time linear input-state-output system where A ∈ R n × n, B ∈ R n × m, C ∈ R p × n, and D ∈ R p × m are given matrices. Let S ∈ S m + p. The system is said to be dissipative with respect to the supply rate if there exists P ∈ S n with P ⩾ 0 such that the dissipation inequality holds for all t ⩾ 0 and for all trajectories (u, x, y): Z + → R m + n + p of. It follows from that dissipativity with respect to the supply rate is equivalent with the feasibility of the linear matrix inequalities P ⩾ 0 and In the framework of data-driven system analysis, the system matrices are unknown. The question we want to study then is whether we can verify dissipativity using only the input-state-output data obtained from the unknown system. In the present section we will study this question for the situation that our data are noiseless.

Consider the unknown input-state-output system with u (t) ∈ R m, x (t) ∈ R n and y (t) ∈ R p the input, state and output. We assume that the dimensions m, n and p are known, but the true system matrices (As, Bs, Cs, Ds) are unknown. What is known instead are a finite number of input-state-output measurements of.

More concrete, we suppose that we have collected input-state-output data. Let U -, X, X -, and X + be defined as the previous section and let Y -be defined in a similar way as U -. Our data are now given by D = (U -, X, Y -). These data are assumed to be generated by the true system (As, Bs, Cs, Ds), which means that The set of all systems that are consistent with these data is then given: It follows from that the unknown system (As, Bs, Cs, Ds) is contained in Σ (U -, X, Y -). Our goal is to infer from the data (U -, X, Y -) whether the unknown system is dissipative.

On the basis of the given data we are unable to distinguish between the systems in Σ ( U -, X, Y -), in the sense that any of these systems could have generated the data. Nonetheless, if all of these systems are dissipative, then we can also conclude that the true data-generating system is dissipative. With this in mind, we now define the property of informativity for dissipativity for the case of noiseless data.

## Definition 7 (Informativity of noiseless data)

The data ( U -, X, Y -) are informative for dissipativity with respect to the supply rate if there exists a matrix P ∈ S n, P ⩾ 0, such that the LMI holds for every system ( A, B, C, D ) ∈ Σ ( U -, X, Y -).

Note that our definition of informativity for dissipativity requires the systems in Σ ( U -, X, Y -) to be dissipative with a common storage function.

We will restrict ourselves to the case that the number of negative eigenvalues of the matrix S representing the supply rate is equal to the output dimension p and the number of positive eigenvalues of S is equal to the input dimension m. In particular then, S is nonsingular. In other words, we will impose the following assumption on the inertia of S: It is a well-known fact that a necessary condition for dissipativity of any system of the form is that the input dimension does not exceed the positive signature of S. Our assumption requires that the input dimension is equal to this positive signature and in addition that the matrix S is nonsingular. This assumption is satisfied, for example, for the positive-real and bounded-real case. Indeed, in the positive-real case we have that m = p and so that In (S) = (m, 0, m). In the bounded-real case we have for some γ > 0, which implies that In (S) = (p, 0, m).

Before establishing conditions for informativity for dissipativity, we note that Σ (U -, X, Y -) contains exactly one element if and only if in this case, we say the data (U -, X, Y -) are informative for system identification.

As the main result of this part we will now show that the noiseless input-state-output data ( U -, X, Y -) are informative for dissipativity if and only if they are informative for system identification and the unique system consistent with these data is dissipative. In addition, dissipativity of this unknown true system can be expressed in terms of feasibility of an LMI involving the data.

## Theorem 20 (Informativity of noiseless data )

Assume that In (S) = (p, 0, m). Then the data (U -, X, Y -) are informative for dissipativity with respect to the supply rate if and only if they are informative for system identification and there exists P = P ⊤ ⩾ 0 such that Next, we proceed with studying informativity for dissipativity in the case that our input-state-output data are obtained from an unknown system subject to unknown process noise and measurement noise. We assume that the unknown system is given by where u (t) ∈ R m, x (t) ∈ R n and y (t) ∈ R p are the input, state and output. The dimensions m, n and p are assumed to be known. The terms w (t) ∈ R n and z (t) ∈ R p represent process and measurement noise, respectively, and are assumed to be unknown. Also the system matrices (As, Bs, Cs, Ds) are assumed to be unknown. Again, we assume that a supply rate is represented by a given matrix S ∈ S m + p, viz.. The problem that we will study is whether we can determine whether the unknown system is dissipative with respect to the given supply rate.

Suppose that we obtain input-state-output data data from the unknown system. These data are collected in the matrices ( U -, X, Y -). The auxiliary matrices X -and X + are as defined before. The noise terms w and z are unknown, so w, w,..., w ( T -1 ) and z, z,..., z ( T -1 ) are not measured, and are therefore not part of the data. We do have the following information on the noise during the data sampling period.

## Assumption 21 (Noise model)

The noise samples, collected in the real (n + p) × T matrix satisfy the quadratic matrix inequality where Φ ∈ S n + p + T is a given partitioned matrix with Φ 11 ∈ S n + p, Φ 12 ∈ R (n + p) × T, Φ 21 = Φ ⊤ 12 and Φ 22 ∈ S T. We assume that Φ ∈ Π n + p, T. Then Z T (Φ) is nonempty and convex (see Sidebar 'Quadratic matrix inequalities"). We have that V -satisfies if and only if V ⊤ - ∈ Z T (Φ).

We now turn to defining the property of informativity for dissipativity for noisy input-state-output data, i.e. data that are generated by the unknown system with unknown process noise and measurement noise whose samples satisfy the quadratic matrix inequality. As our model class M we take all noisy input-state-output systems with input dimension m, state space dimension n and output dimension p. Given the input-state-output data (U -, X, Y -) together with the information that the matrices of noise samples satisfy, the set of all systems consistent with the data is then given by We assume that the data have been obtained from the unknown system, i.e., (As, Bs, Cs, Ds) ∈ Σ D. Therefore, Σ D is nonempty. Define Note that (A, B, C, D) ∈ Σ D if and only if This can be restated equivalently as From Assumption 21 we have Φ 22 ⩽ 0 and therefore N 22 ⩽ 0. It follows from the assumption ker Φ 22 ⊆ ker Φ 12 that ker N 22 ⊆ ker N 12. Since Z n + m (N) is nonempty it follows from Theorem 12 of Sidebar 'Quadratic matrix inequalities" that N | N 22 ⩾ 0. Thus the matrix N given by is in Π n + p, n + m.

Next, we give the definition of informativity for dissipativity in the context of noisy input-state-output data. Again, we will require that all systems consistent with the data are dissipative with a common storage function.

## Definition 8 (Informativity of noisy data)

The noisy input-state-output data ( U -, X, Y -) are informative for dissipativity with respect to the supply rate if there exists a matrix P ⩾ 0 such that the LMI holds for all systems ( A, B, C, D ) ∈ Σ D.

Similar to the noiseless case as studied before, in the remainder of this section we will assume that the matrix S representing the supply rate satisfies the inertia condition In ( S ) = ( p, 0, m ).

The following preliminary lemma states that also in the context of noisy data, the rank condition on the inputstate data is necessary for informativity.

## Lemma 3 (Necessity of full row rank condition )

Assume that In ( S ) = ( p, 0, m ). If the data ( U -, X, Y -) are informative for dissipativity with respect to the supply rate then holds.

In addition, we need the following lemma which states that if the data are informative for dissipativity with all systems in Σ D having a given common storage function P ⩾ 0, then P is necessarily positive definite. This is true under the additional assumption that the Schur complement N | N 22 is positive definite. Combining this with the fact that N ∈ Π n + p, n + m as was already established above, this implies that the set Σ D has a nonempty interior.

## Lemma 4 (Necessity of positive definite storage )

Suppose that In ( S ) = ( p, 0, m ) and that N | N 22 > 0. If P ⩾ 0 satisfies the dissipation inequality for all ( A, B, C, D ) ∈ Σ D then P > 0.

Our next step is to partition where F ∈ R m × m, G ∈ R m × p, H ∈ R p × p. For any P ⩾ 0 define Then the system (A, B, C, D) can be seen to satisfy the dissipation inequality if and only if Moreover, with this notation in place, the problem of characterizing informativity for dissipativity is equivalent to finding conditions for the existence of a matrix P > 0 such that the inequality holds for all (A, B, C, D) satisfying the inequality.

Our strategy to solve this problem is to invoke the nonstrict matrix S-lemma, Theorem 13 of Sidebar 'Quadratic matrix inequalities". Before we can apply Theorem 13 however, note that the inequality is in terms of ( A, B, C, D ) while the inequality is in terms of the transposed matrices ( A ⊤, C ⊤, B ⊤, D ⊤ ). Therefore, we will need an additional dualization result that we formulate in the following lemma.

## Lemma 5 (Dualization of dissipation inequality )

Let P > 0 and let (A, B, C, D) be any system with input dimension m, state space dimension n and output dimension p. Assume that In (S) = (p, 0, m). Define Lemma 5 can be interpreted as saying that the system defined by the quadruple (A, B, C, D) is dissipative with respect to the supply rate S, with storage function P if and only if the dual system (A ⊤, C ⊤, B ⊤, D ⊤) is dissipative with respect to the supply rate ˆ S, with storage function P -1. A behavioral analogue of this result was obtained, Proposition 12. where ˆ F = ˆ F ⊤ ∈ R m × m, ˆ G ∈ R m × p, and ˆ H = ˆ H ⊤ ∈ R p × p and define Then it is easily seen that (A ⊤, C ⊤, B ⊤, D ⊤) satisfies the inequality if and only if We may now observe that, under the assumptions that In (S) = (p, 0, m) and N | N 22 > 0, informativity for dissipativity with respect to the supply rate given by S holds if and only if there exists P > 0 such that the quadratic inequality holds for all (A, B, C, D) that satisfy the the quadratic inequality, equivalently This brings us in position to apply Theorem 13 and to obtain the following characterization for informativity for dissipativity for noisy input-state-output data.

## Theorem 22 (Informativity of noisy data )

Suppose that the data (U -, X, Y -) are collected from system with noise as in Assumption 21. In addition, assume that In (S) = (p, 0, m) and that the data (U -, X, Y -) are such that N | N 22 > 0. Partition where ˆ F = ˆ F ⊤ ∈ R m × m, ˆ G ∈ R m × p, and ˆ H = ˆ H ⊤ ∈ R p × p. Then the data are informative for dissipativity with respect to the supply rate if and only if there exist a real n × n In that case P: = Q -1 is a common storage function for all systems consistent with the data.

Theorem 22 provides a tractable method for verifying informativity for dissipativity of noisy data given the noise model introduced in Assumption 21. The procedure involves solving the linear matrix inequality for Q and α. Given Q, a common storage function P for all systems in Σ D is also readily computable as P = Q -1.

## AUTO-REGRESSIVE SYSTEMS AND NOISY INPUT-OUTPUT DATA

Whereas the first two sections of this paper have dealt with input-output systems in state space form together with input-state data, in the current section we will abandon the state space framework and consider input-output systems described by higher order difference equations, also called auto-regressive (AR) systems. Instead of input-state data we will assume to have (noisy) input-output data. In this framework we will discuss data-driven stabilization. Several contributions in the literature have also dealt with input-output data. A general strategy in these papers is to construct an artificial state-space representation of the system with a state comprised of shifts of the inputs and outputs. This leads to an inputstate-output system to which techniques for state data (as discussed before in this paper) are applicable. A drawback of this approach is that the obtained state space systems are non-minimal and of high dimension. Thus a large amount of data can be required for control (see e.g. [22, Section VIC]). In addition, the system matrices of the state-space representation are structured and consist of a combination of known and unknown blocks. Often, this structure is not taken fully into account, which can lead to rather conservative conditions for data-driven control design. Exploiting this prior knowledge of the system matrices is an important problem, which has recently been studied .

Motivated by these limitations of an artificial state space, the main purpose of this section is to discuss a theory on data driven design of stabilizing feedback controllers on the basis of input-output data, without relying on state construction.

## Stabilization using input-output data

We consider input-output systems with additive noise represented by auto-regressive AR models of the form Here L is a positive integer, called the order of the system. The input u (t) and output y (t) are assumed to take their values in R m and R p, respectively. The term v (t) represents unknown noise. The parameters of the model are real p × p matrices P 0, P 1,..., PL -1 and p × m matrices Q 0, Q 1,..., QL -1. Using the shift operator (σ f)(t) = f (t + 1), can be written as where P (ξ) and Q (ξ) are the real p × p and p × m polynomial matrices defined by Since the leading coefficient matrix of P (ξ) is the p × p identity matrix, P is invertible as a rational matrix and P -1 (ξ) Q (ξ) is strictly proper. Thus, indeed, represents a causal input-output system with control input u, noise input v and output y. A feedback controller for the input-output system with P (ξ) and Q (ξ) of the form will be taken to be of the form The leading coefficient matrix of G (ξ) is assumed to be the m × m identity matrix and Gi ∈ R m × m, Fi ∈ R m × p for i = 0, 1,..., L -1. The closed loop system obtained by interconnecting a system of the form and the controller is represented by Note that the leading coefficient matrix is the q × q identity matrix. We call the controller a stabilizing controller for if the corresponding autonomous system is stable, in the sense that all solutions u and y of tend to zero as time tends to infinity. The problem that we consider is to find a feedback controller of the form that stabilizes the unknown true system For this, we assume that the order L is known, and that only data obtained from the true system can be used. These data are the input-output data given by u, u,..., u (T), y, y,..., y (T) on the interval [0, T] with T ⩾ L. These are samples of u and y satisfying the system equation for some noise signal v. The noise v is unknown, but its samples are assumed to satisfy an assumption analogously to Assumption 11:

## Assumption 23 (Assumption on the noise)

The noise samples v, v,..., v (T -L), collected in the real p × (T -L + 1) matrix satisfy the quadratic matrix inequality where Π ∈ S p + T -L + 1 is a known partitioned matrix with Π 11 ∈ S p, Π 12 ∈ R p × (T -L + 1), Π 21 = Π ⊤ 12 and Π 22 ∈ S T -L + 1. We assume that Π ∈ Π p, T -L + 1 By Proposition 12 the set of matrices V that satisfy is nonempty.

As noted before in this paper, in general the given data u, u,..., u ( T ), y, y,..., y ( T ) do not determine the true system uniquely. In fact, the data determine a whole set of systems that are consistent with the data. As a consequence, finding a stabilizing controller for the true system based only on the data requires finding a controller that stabilizes all systems that are consistent with the data. If, for given data, such controller exists, then we call the input-output data informative for stabilization. This will now be made precise. In order to do this, first the set of all systems that are consistent with the data will be specified.

After denoting q: = p + m, R (ξ) = [-Q (ξ) P (ξ)] and z = col (u, y), can be rewritten as Collect the (unknown) coefficient matrices of the polynomial matrix R (ξ) in the p × qL matrix Note that, with a slight abuse of notation, we denote both the polynomial matrix and its coefficient matrix by R. We call the coefficient matrix of the system. Arrange the data u, u,..., u (T), y, y,..., y (T) into the vectors and define the associated depth L + 1 Hankel matrix by where H 1 (z) contains the first qL rows and H 2 (z) the last p rows. It is then easily verified that any input-output system for which the coefficient matrix R defined in satisfies for some V ∈ Z T -L + 1 (Π), could have generated the given input-output data. In other words, z, z,..., z (T) are also samples on the interval [0, T] of a z that satisfies R (σ) z = v for some v satisfying Assumption 23. Therefore, R satisfies for some V ∈ Z T -L + 1 (Π) if and only if the AR system with coefficient matrix R is consistent with the data. Recall that, in particular, the true system is consistent with the data. Now define Then by combining and we see that the system with coefficient matrix R is consistent with the data if and only if R ⊤ satisfies the QMI Thus we have succeeded in finding an explicit expression for the set of systems that are consistent with the data. Indeed, this set is equal to Since the true system is consistent with the data, this set is nonempty.

Our aim is to find a single controller of the form that stabilizes all input-output systems that are consistent with the data, so all systems in Σ D. In order to investigate the existence of such controller, we will now first study stability of autonomous systems in AR form.

Given a nonsingular p × p polynomial matrix P ( ξ ), the corresponding autonomous AR system P ( σ ) y = 0 is called stable if y ( t ) → 0 as t → ∞ for all solutions y: Z + → R p. This space of all solutions on Z + is called the behavior of the system and is denoted by B ( P ). Stability of autonomous AR systems can be characterized in terms of quadratic difference forms on behaviors. For details on QDFs, see: 'Quadratic Difference Forms'. In a continuoustime context, the connection between stability and QDFs was studied , while the discrete-time version was considered . The following proposition holds:

## Proposition 2 (A QDF as Lyapunov function )

Let P ( ξ ) be a nonsingular polynomial matrix. The corresponding autonomous system P ( σ ) y = 0 is stable if and only if there exists a QDF Q Ψ such that Q Ψ ⩾ 0 on B ( P ) and Q ∇ Ψ < 0 on B ( P ).

For obvious reasons, we refer to Q Ψ as a Lyapunov function. In principle, the above theorem does not specify the degree of Q Ψ. However, it turns out that if P (ξ) is of the form (with leading coefficient matrix the identity matrix) and the corresponding autonomous system P (σ) y = 0 of order L is stable, there exists a Lyapunov function of degree at most L -1. Indeed, we have

## Lemma 6 (A degree bound on the Lyapunov QDF )

Let P ( ξ ) be a polynomial matrix of the form. The corresponding autonomous system P ( σ ) y = 0 order L is stable if and only if there exists a QDF Q Ψ ( y ) of degree at most L -1 such that Q Ψ ⩾ 0 and Q ∇ Ψ < 0 on B ( P ).

The fact that the degree of the QDF defining the Lyapunov function can be bounded from above by the order of the system is crucial for enabling us to express stability of the system P ( σ ) y = 0 in terms of a quadratic matrix inequality. This QMI involves a symmetric matrix Ψ of dimensions pL × pL leading to a Lyapunov function Q Ψ, and the matrix P = [ P 0 P 1 · · · PL -1 ]. Again, for ease of notation we denote both the polynomial matrix and its coefficient matrix by P. Then we have:

## Theorem 24 (A QMI condition for stability )

Let P (ξ) = I ξ L + PL -1 ξ L -1 +... + P 1 ξ + P 0 and let P (σ) y = 0 be the corresponding autonomous system. This system is stable if and only if there exists Ψ ∈ S pL such that Ψ ⩾ 0 and Any such Ψ defines a Lyapunov function Q Ψ.

Next, we turn to the data-driven stabilization problem. For a given controller of the form, denote and recall that z = col (u, y). Then can equivalently be written as

## Quadratic difference forms

A crucial instrument in studying stability of systems is the notion of Lyapunov function. Studying stability of autonomous systems in AR form requires the notion of Lyapunov functions given by quadratic difference forms (QDFs). In this sidebar we review the basic material on QDFs and establish some useful preliminary results. For more details, we refer to,.

Let N and q be positive integers and for i, j = 0, 1,..., N let Φ i, j ∈ R q × q be such that Φ i, i ∈ S q and Φ i, j = Φ ⊤ j, i for all i = j. Arrange these matrices into the partitioned matrix Φ ∈ S (N + 1) q given by Then the quadratic difference form associated with Φ is the operator Q Φ that maps R q -valued functions z on Z + to R -valued functions Q Φ (z) on Z + defined by In terms of the matrix Φ this can be written as Thus, vector valued functions are mapped to quadratic expressions in terms of these function and their time shifts up to a certain dergree.

Obviously, some of the matrices Φ i, j, or even an entire block row or column of Φ could be zero. We define the degree of the QDF (S1) as the smallest integer d such that Φ ij = 0 for Collect the coefficient matrices of F (ξ) and G (ξ) in the matrix C defined by and recall the definition of the coefficient matrix R associated likewise with R (ξ). Note that the leading coefficient matrix of the polynomial matrix [C (ξ) ⊤ R (ξ) ⊤] ⊤ is the q × q identity matrix. Furthermore, its coefficient matrix is [C ⊤ R ⊤] ⊤. Recall that the controller is a stabilizing controller for the input-ouput system if and only if the autonomous system is stable. As an immediate consequence of Theorem 24 we then have

## Lemma 7 (A QMI condition for stabilization )

The controller C ( σ ) z = 0 is a stabilizing controller for the system if and only if there exists Ψ ∈ S qL such that all i > d or j > d. This degree is denoted by deg ( Q Φ ). The matrix Φ is called a coefficient matrix of the QDF. Note that a given QDF does not determine the coefficient matrix uniquely. However, if the degree of the QDF is d, it allows a coefficient matrix Φ ∈ S ( d + 1 ) q.

The QDF Q Φ is called nonnegative if Q Φ ( z ) ⩾ 0 for all z: Z + → R q. We denote this as Q Φ ⩾ 0. Clearly, this holds if and only if Φ ⩾ 0. The QDF is called positive if it is nonnegative and, in addition, Q Φ ( z ) = 0 if and only if z = 0. This is denoted as Q Φ > 0. Likewise we define nonpositivity and negativity.

For a given QDF Q Φ, its rate of change along a given z: Z + → R q is given by Q Φ (z)(t + 1) -Q Φ (z)(t). It turns out that the rate of change defines a QDF itself. Indeed, by defining the matrix ∇ Φ ∈ S (N + 2) q by it is easily verified that for all z: Z + → R q and t ∈ Z +.

Quadratic difference forms are particularly relevant in combination with behaviors defined by AR systems. Let R (ξ) be a real p × q polynomial matrix and consider the AR system represented by R (σ) z = 0. Let B (R) be the behavior of this system, i.e., the space of all solutions as given by The QDF Q Φ is called nonnegative on B (R) if Q Φ (z) ⩾ 0 for all z ∈ B (R). It is called positive on B (R) if, in addition, Q Φ (z) = 0 if and only if z = 0. We denote this as Q Φ ⩾ 0 on B (R) and Q Φ > 0 on B (R), respectively. Likewise we define nonpositivity and negativity on B (R).

Moreover, if Ψ ⩾ 0 satisfies, then Ψ > 0.

Now recall that our aim is to find a single stabilizing controller for all systems in Σ D = { R ∈ R p × qL | R ⊤ ∈ Z qL ( N ) }, i.e. for all systems whose coefficient matrix satisfies the QMI. This leads to the following definition of informativity for quadratic stabilization.

## Definition 9 (Informativity for quadratic stabilization)

The input-output data u,..., u (T), y,..., y (T) are called informative for quadratic stabilization if there exist C ∈ R m × qL and Ψ ∈ S qL with Ψ ⩾ 0 such that the QMI holds for all R that satisfy the QMI, with N defined.

Informativity for quadratic stabilization thus means that there exist a controller C ( σ ) z = 0 (equivalently, G ( σ ) u = F ( σ ) y ) and a matrix Ψ ∈ S qL such that the QDF Q Ψ is a common Lyapunov function for all closed loop systems obtained by interconnecting the controller with an arbitrary system that is consistent with the data.

We now aim at finding necessary and sufficient conditions on the given data to be informative for quadratic stabilization. Define the q (L -1) × qL matrix J by It can be proven that holds if and only if Ψ > 0 and where the 2 qL × 2 qL matrix M is defined by This means that informativity for quadratic stabilization is equivalent to the existence of an m × qL matrix C and a matrix Ψ ∈ S qL, Ψ > 0 such that the QMI holds for all matrices R that satisfy the QMI. The matrix C is then the coefficient matrix of a suitable controller. In terms of solutions sets of QMIs this can be restated as In order to be able to apply the strict matrix S-lemma in Theorem 14, we will express the set on the left in as the solution set of a QMI. Define the 2 qL × 2 qL matrix ¯ N by Then indeed the following can be proven:

## Lemma 8 (An instrumental lemma )

Assume that the Hankel matrix H 1 ( z ) has full row rank. Then Z qL ( N ) [ 0 0 -Ip ] = Z qL ( ¯ N ).

From the above we see that, under the assumption that H 1 ( z ) has full row rank, informativity for quadratic stabilization requires the existence of C and Ψ > 0 such that the inclusion Z qL ( ¯ N ) ⊆ Z + qL ( M ). holds. This inclusion is dealt with in Theorem 14.

## Lemma 9 (A condition for informativity )

Let Ψ > 0, C ∈ R m × qL and let M be given. Assume that H 1 (z) has full row rank. Then Z qL (¯ N) ⊆ Z + qL (M) if and only if there exists a scalar α ⩾ 0 such that Note that the unknowns C and Ψ appear in the matrix M in a nonlinear way, and even in the form of an inverse. However, by putting Φ: = Ψ -1 we can get rid of the inverse, and rewrite the condition M -α ¯ N > 0 as Thus, informativity for quadratic stabilization holds if and only if there exists Φ > 0, a matrix C and a scalar α ⩾ 0 such that holds. Note that α must be positive due to the negative definite lower right block. By scaling Φ we can therefore take α = 1. Finally, by introducing the new variable D: = -C Φ and taking a suitable Schur complement, can be reformulated as the following LMI in the unknowns Φ and D: This then immediately leads to the following characterization of informativity for quadratic stabilization and a method to compute a suitable feedback controller together with a common Lyapunov function.

## Theorem 25 (An LMI condition for informativity )

Suppose that the data u, u,..., u ( T ), y, y,..., y ( T ) are collected from system with noise as in Assumption 23. In addition, assume that H 1 ( z ) has full row rank. Let the matrix ¯ N be given , with N defined . Then the input-output data are informative for quadratic stabilization if and only if there exist matrices D ∈ R m × qL and Φ ∈ S qL such that Φ > 0 and the LMI holds.

In that case, the feedback controller with coefficient matrix C: = -D Φ -1 stabilizes all systems that are consistent with the input-output data. Moreover, the QDF Q Ψ with Ψ: = Φ -1 is a common Lyapunov function for all closed loop systems.

Thus, in order to compute a controller that stabilizes all systems consistent with the data and which gives a common Lyapunov function, first compute the matrix ¯ N using the Hankel matrix associated with the data. Next, check feasibility of the LMI and, if it is feasible, compute solutions D and Φ. An AR representation of the controller with coefficient matrix C = -D Φ -1 is then obtained as follows: partition with Fi ∈ R m × p and Gi ∈ R m × m. Next define F (ξ): = FL -1 ξ L -1 + · · · + F 0 and G (ξ): = I ξ L + GL -1 ξ L -1 + · · · + G 0. The corresponding controller is then given in AR representation by G (σ) u = F (σ) y.

## Simulation example

In this example, we consider a model of a magnetic suspension system, where an electromagnet is used to levitate a magnetic mass. We assume that we can measure the vertical position of the mass and control the current of the electromagnet with the aim of stabilizing the mass at a pre-determined position. Of course, in the context of this paper, we will develop such a controller on the basis of collected measurements.

For a detailed derivation of the model, see [109, Example 1.18]. Following [109, Example 12.8], we let x 1 denote the vertical position and x 2 the vertical velocity of the ball. Moreover, x 3 denotes the current and ˆ u the voltage of the circuit. The model is then given: where L (x 1) = L 1 + L 0 a a + x 1. Defining the function f accordingly, we write this system as ˙ x = f (x, ˆ u).

As noted, we are interested in stabilizing the ball at x 1 = r > 0, on the basis of measurements of x 1. In order to apply the results of this paper, we will first linearize the model around the corresponding equilibrium point. After this, we will discretize and rewrite it to an AR model of the form considered in this paper.

For the physical quantities we will use the following values: First, we solve f (x, ˆ u) = 0 with x 1 = r in order to obtain the equilibrium point of interest of the system. This yields the solution We can shift the equilibrium point to the origin by defining ¯ x = x -x 0, and u = ˆ u -ˆ u 0, obtaining in the new variables: Linearizing this around the origin yields ˙ ¯ x = A ¯ x + Bu, where Since we want to control the system on the basis of measurements of ¯ x 1, we add an output y = C ¯ x, where C: =. Now, we can discretize this with step size δ > 0 and obtain In order to obtain an AR model, note that for each s ⩾ 1 we have that The characteristic polynomial of I + δ A is denoted The Cayley-Hamilton theorem states that χ (I + δ A) = 0. Therefore, we obtain that: where the matrices Q 0, Q 1, and Q 2 are given: This brings the model into the form considered in this paper.

In this simulation example, we will perform measurements on the (discretized) nonlinear system. We will treat this nonlinear system as an AR model of the form where the additive noise term v ( t ) captures the nonlinearities. Using the methods of this paper, we will find a stabilizing controller for all such systems consistent with the measurements and a noise model of the form VV ⊤ ⩽ ϵ.

We obtain measurements of the system close to the equilibrium point. To be precise we take δ = 0.005, T = 28, and generate random inputs from the interval 10 -5. These are applied to the nonlinear system with given initial conditions. The measurements resulting from this can be seen . For these measurements, we observe that VV ⊤ ⩽ 10 -17.

FIGURE 3 The results of interconnecting the controller with the linearized system, two other systems consistent with the data, and the original nonlinear system.

We will use Theorem 25 to show that these measurements are informative for quadratic stabilization. For this, we first form the matrices H ′ 1, H ′ 2 and ¯ N. It is straightforward to see that H ′ 1 has full row rank. We now use Yalmip with Mosek as a solver in order to find matrices D ∈ R 1 × 6, and Φ ∈ S 6, such that Φ > 0 and the LMI holds. Indeed, such matrices exist, and therefore the data are informative for quadratic stabilization. We can find a stabilizing controller by taking C = -D Φ -1, which results in That is, a controller of the form: By definition, this means that the controller C stabilizes all linear systems of the form that are compatible with the measurements. A few trajectories of compatible systems interconnected with the controller are shown in Figure 3. More specifically, the linearization derived earlier is consistent with the measurements, and is therefore stabilized by the found controller. As a last remark, we can interconnect the controller with the discrete-time nonlinear plant. Given that the controller stabilizes the linearization, it locally stabilizes the nonlinear system. This is also illustrated in Figure 3.

## CONCLUSIONS AND DISCUSSION

In this paper, we have given an introduction to the informativity approach to data-driven control. By using a combination of a new viewpoint, classical methods, and novel technical results, we have illustrated the framework by providing a number of solutions to problems with different model classes of linear systems, different types of measurements, and various control objectives. There remain, however, certain limitations to the results. While a number of these limitations yield interesting directions for future research, some of them are inherent to the approach.

First of all, we have been interested in providing necessary and sufficient conditions for informativity. Of course, such conditions are in a certain sense the gold standard, as they precisely characterize the information contained in the data. On the other hand, it might well be the case that the data contain more information than required. As such, a potentially interesting variant of these problems is to provide condition which are easier to check, but only sufficient. In many cases, such an approach might computationally outperform the methods of this paper. In a similar vein, a number of heuristic methods can drastically outperform the design methods of this paper, albeit without strong theoretical guarantees. In particular, in the case of very small noise samples, the set of consistent systems may be small. In this case, an intuitive method of performing data-driven control is a certainty-equivalent approach: Find any compatible system and solve the control problem for that system.

The informativity approach has a number of moving parts: The control objective, model class, and noise model. In this paper, we have mainly varied our choice of control objective or analysis problem. In particular, we have focused entirely on model classes consisting of different flavors of linear systems. An extension towards nonlinear systems could improve the applicability of the results. For well-behaved nonlinear systems, we can draw certain conclusions on the basis of the behavior of its linearization. However, a more natural approach would be to investigate informativity problems for certain classes of nonlinear systems directly. Of course, when changing the model class one needs to balance the benefits of more general model classes and the tractability of the resulting robust control problems. Some classes of systems have shown a favorable trade-off in this regard, such as bilinear systems polynomial systems rational systems and systems with quadratic or sector bounded nonlinearities,. As was shown in the aforementioned works, a thorough understanding of the linear case often remains invaluable for the proposal of nonlinear extensions.

Another problem of interest is changing the way the noise acts on our system and measurements. Measurement noise, that is, noise which acts only on the measurements but not on the system, can be modeled in a similar manner as in this paper. However, an open problem is to provide conditions for data informativity in this setting, because the structure of the set of consistent systems appears to be more complicated than the ones studied here. So far, we are only aware of sufficient conditions for quadratic stabilization with measurement noise [22, Sec. VA] that rely on somewhat conservative bounds.

The noise models considered in this paper can be applied to treat different scenarios such as energy bounds and sample covariance bounds on the noise. An advantage of these noise models is that the resulting informativity conditions take the form of LMIs with a complexity that is independent of the number of measurements. Clearly, such limited computational complexity is desirable in any control problem. However, the assumption that the noise signal can be described by the solution set of a QMI also comes with certain limitations.

In particular, with the noise models described in this paper, it is not possible to treat the situation of sample bounds without conservatism. More generally, combining different sets of measurements is a nontrivial problem in this setting, given that the intersection of solution sets of QMIs can generally not be described as the solution set of a single QMI. Without either developing tools that can deal with such intersections or alternative noise models, two important problems are difficult to tackle. First of all, the question of incremental informativity: Does adding more measurements lead to more informative data? Moreover, this lack of scalability inhibits the development of online or adaptive methods as compared to the offline methods of this paper. This motivates the development for new technical results for sample-bounded noise. In [78, Sec. VII] a simple sufficient LMI condition was proposed for quadratic stabilization in the presence of sample-bounded noise, which was further studied . Although this approach appears to be less conservative than describing sample-bounded noise by a QMI, it is not well-understood from a theoretical perspective.

One of the strengths of methods based on the fundamental lemma (see also the Sidebar 'Willems' fundamental lemma") is the following: For controllable linear systems, we can guarantee that the input-output data have favorable rank properties by injecting inputs that are persistently exciting. The fundamental lemma is thus an experiment design result, that provides a guide for choosing the inputs of the experiment in order to generate informative data (for system identification). It can be shown that the persistency of excitation condition can be replaced by an online design of the inputs, which uses less data samples. An important topic for future work, however, is to develop experiment design methods corresponding to the various problems studied in this paper, especially those for noisy data. Although this is a largely unexplored area of research, we believe that the conditions provided in this paper will form the basis for an experiment design theory. Indeed, to be able to guarantee that the data are informative requires a thorough understanding of informativity in the first place.
