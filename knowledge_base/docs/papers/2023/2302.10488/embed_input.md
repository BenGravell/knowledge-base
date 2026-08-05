<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Informativity Approach to Data-Driven Analysis and Control

Topics include Data informativity, Data-driven control, Data-driven analysis, Behavioral systems, Robust control, Quadratic matrix inequalities, Dissipativity, H-infinity control, Measurement feedback.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Expands the informativity tutorial into a longer map of analysis and synthesis problems, including controllability, stabilizability, LQR, tracking, dissipativity, H-infinity control, and dynamic measurement feedback. It is the broadest single overview of the framework in this group.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The goal of this paper is to provide a tutorial on the so-called informativity framework for direct data-driven analysis and control. This framework achieves certified data-based analysis and control by assessing system properties and determining controllers for sets of systems unfalsified by the data. We will first introduce the informativity approach at an abstract level. Thereafter, we will report case studies where we highlight the strength of the framework in the context of various problems involving both noiseless and noisy data. In particular, we will treat controllability and stabilizability, and stabilization, linear quadratic regulation, and tracking and regulation using exact input-state measurements. Thereafter, we will treat dissipativity analysis, stabilization, and H_inf control using noisy input-state data. Finally, we will study dynamic measurement feedback stabilization using noisy input-output data. We will provide several examples to illustrate the approach. In addition, we will highlight the main tools underlying the framework, such as quadratic matrix inequalities in robust control and quadratic difference forms in behavioral systems theory.

<!-- chunk {"id": "body-0004", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

TO DATA-DRIVEN ANALYSIS AND CONTROL HENK J. VAN WAARDE, JAAP EISING, M. KANAT CAMLIBEL, and HARRY L. TRENTELMAN R oughly speaking, systems and control theory deals with the problem of making a concrete physical system behave according to certain desired specifications. In order to achieve this desired behavior, the system can be interconnected with a physical device, called a controller. The problem of finding a mathematical description of such a controller is called the control design problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

In order to obtain a mathematical description of a controller for a to-be-controlled physical system, a possible first step is to obtain a mathematical model of the physical system. Such a mathematical model can take many forms. For example, the model could be in terms of ordinary or partial differential equations, difference equations, or transfer matrices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

There are several ways to obtain a mathematical model for the physical system. The usual way is to apply the basic physical laws that are satisfied by the variables appearing in the system. This method is called fi rst principles modeling. For example, for electro-mechanical systems, the set of basic physical laws that govern the behavior of the variables in the system (conservation laws, Newton's laws, Kirchoff's laws, etc.) form a mathematical model.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

An alternative way to obtain a model is to do experiments on the physical system: certain external variables in the physical system are set to take particular values, while at the same time other variables are measured. In this way, one obtains data on the system that can be used to find mathematical descriptions of laws that are obeyed by the system variables, thus obtaining a model. This method is Digital Object Identifier 10.1109/MCS.2020.000000 Date of current version: XXXXXX called system identification.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

The second step in a control system design problem is to decide which desired behavior we would like the physical system to have. Very often, this desired behavior can be formalized by requiring the mathematical model to have certain qualitative or quantitative mathematical properties. Together, these properties form the design objective.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

Based on the mathematical model of the physical system and the design objective, the third, ultimate, step is to design a mathematical model of a suitable controller. This approach, leading from a model and a design objective (or list of design specifications) to a model of a controller is an important paradigm in systems and control, and is often called model-based control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

An approach that has recently gained popularity is to design controllers without the step of finding a mathematical model of the to-be-controlled physical system. This alternative approach deals with the problem of synthesizing control laws directly on the basis of measured data, and is called the data-driven approach to control design. Of course, one can argue that also the combination of system identification followed by model based control as described above is an instance of data driven control design. Indeed, methods using this combination are often called indirect methods of data-driven control, consisting of the two-step process of data-driven modeling (i.e., system identification -) followed by model-based control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The informativity approach", "weight": 1.0} -->

Early contributions to direct data-driven control include PID control, direct adaptive control, iterative feedback tuning virtual reference feedback tuning and unfalsified control. Recently, direct optimal control design - and predictive control - have received considerable attention. Some of these ap-

<!-- chunk {"id": "body-0012", "role": "body", "section": "regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient\" information", "weight": 1.0} -->

proaches, such as and, strongly rely on the socalled fundamental lemma by Willems and co-authors. This result provides a convenient parameterization of all trajectories of a linear time-invariant system in terms of data. Originally developed in a behavioral context, the fundamental lemma is also instrumental for direct output matching control and control by interconnection. The result has been extended in various ways to different model classes and data setups -. Although initially developed for linear systems, the fundamental lemma has been applied in the context of data-driven control of nonlinear dynamics, such as polynomial and Lur'e systems -. In addition to control problems, also analysis problems have been studied within a direct databased framework. Some examples include the analysis of stability, controllability and observability -, and dissipativity -.

<!-- chunk {"id": "body-0013", "role": "body", "section": "regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient\" information", "weight": 1.0} -->

Investigating the different pros and cons of indirect and direct methods is an area of active research,. However, regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient" information. Indeed, as an extreme example one can consider the zero input-output trajectory generated by an unknown linear time-invariant system: clearly this trajectory does not reveal much about the system and would be a poor basis for an identification or control scheme. The purpose of this paper is to introduce a framework in which we can systematically study the richness of data that is required for various system analysis and control problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient\" information", "weight": 1.0} -->

The concept of 'data informativity" plays a central role in this paper. This concept finds its roots in system identification, -, where informativity is usually understood as a condition on the data under which it is possible to distinguish between different models in a (parametric) model class. Here, however, we will define a general notion of data informativity for system analysis and control design. We are thus not necessarily interested in distinguishing between different models on the basis of the data, but rather want to understand whether it is possible to assess a system-theoretic property, or to synthesize a controller for the physical system from the data. If this is possible, we will say that the data are informative for the system property, or for the control design problem. Although we will introduce the concept of informativity in general terms, it is important to note that the conditions for informative data depend on the particular analysis or control problem at hand. For example, as we will see, the conditions under which stabilizing controllers can be obtained from data are less stringent than those for obtaining optimal controllers. This motivates a rigorous analysis of data informativity for different system analysis and control problems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient\" information", "weight": 1.0} -->

In some situations the data obtained from the physical system contain sufficient information to identify the system model uniquely. For our purposes, this situation is the least interesting because informativity for system analysis and control design simply boil down to properties of the (unique) model of the physical system. In general however, it is not possible to uniquely identify the physical system because the data set may contain a small number of samples or the data may be corrupted by noise. In this case, we will make use of consistent systems sets that comprise all dynamical system models that are unfalsified by the data. Such sets also play an important role in set membership identification, where they are called feasible systems sets.

<!-- chunk {"id": "body-0016", "role": "body", "section": "regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient\" information", "weight": 1.0} -->

In the case that unique system identification is impossible, it will turn out that there are still many relevant cases in which the data are informative for system analysis or control design. In fact, our main results can be interpreted as robust analysis and control methods for sets of consistent systems. For example, in our study of noise-free data the approach leads to a robust theory for affine sets of systems, which, to the best of our knowledge has not received much attention before. In the noisy data setting, our methods draw inspiration from classical robust control results like Yakubovich's S-lemma and extensions thereof.

<!-- chunk {"id": "body-0017", "role": "body", "section": "regardless of whether a direct or indirect approach is used, any certified data-driven method requires data that contain 'sufficient\" information", "weight": 1.0} -->

Besides conditions for data informativity, this paper also puts forward a number of control design methods that enable the synthesis of a controller from informative data. In many cases, these design methods are based on data-based linear matrix inequalities. The methods thus contribute to the aforementioned lines of work on direct data-driven control, since no (explicit) model identification is needed. Although we believe that the direct approach is appealing from a conceptual point of view (why focus on models while the goal is control design?), we also acknowledge that it would be possible to formulate indirect alternatives to our methods by describing the set of systems consistent with the data as a model plus an uncertainty description around this model. In view of this observation, we are inclined to believe that the discussion on direct versus

<!-- chunk {"id": "body-0018", "role": "body", "section": "informative data is the cornerstone of this paper, since any data-driven identification, analysis or control task is impossible without it", "weight": 1.0} -->

indirect control is, perhaps, not the most fundamental one. Instead, the concept of informative data is the cornerstone of this paper, since any data-driven identification, analysis or control task is impossible without it.

<!-- chunk {"id": "body-0019", "role": "body", "section": "DATA INFORMATIVITY FRAMEWORK", "weight": 1.0} -->

In this section we will introduce the concept of data informativity for verifying a given system property or solving a certain control design problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "DATA INFORMATIVITY FRAMEWORK", "weight": 1.0} -->

To start, we fix a certain model class M. This model class is a given set of systems that is assumed to contain the 'true' system (i.e., a mathematical model of the underlying unknown physical system), denoted by S. We assume that the true system S is not known but that we do have access to a set of data, D, which is generated by this system. As explained in the introduction, we are interested in assessing system-theoretic properties of S and designing control laws for it from the data D. Given the set of data D, we define Σ D ⊆ M to be the set of all systems in M that are consistent with the data D, i.e., that could also have generated the same data. In other words, it is impossible to distinguish the true system S from any other system in Σ D on the basis of the given data D alone. As noted before, the setup introduced above is in line with set membership identification (SMI) methods, where sets of systems consistent with the data also play an important role (in SMI these are typically called feasible system sets ).

<!-- chunk {"id": "body-0021", "role": "body", "section": "DATA INFORMATIVITY FRAMEWORK", "weight": 1.0} -->

We will now first focus on data-driven analysis of system theoretic properties. Let P be some system theoretic property. We will denote the set of all systems within M having this property by Σ P. Suppose we are interested in the question whether our true system S has the property P. Since the only information we have to base our answer on are the data D obtained from the true system, we can only conclude from the data that the true system has property P if all systems consistent with the data D have the property P. If this is the case, we call the data informative for the system property. This leads to the following definition, see also Figures 1 and 2.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem 1 (Informativity problem for analysis)", "weight": 1.0} -->

Provide necessary and sufficient conditions on the data D under which these data are informative for property P.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem 1 (Informativity problem for analysis)", "weight": 1.0} -->

The above gives us a general framework to deal with data-driven analysis problems. We will also deal with datadriven control problems. The objective in such problems is the data-based design of controllers such that the closed loop system, obtained from the interconnection of the true system S and the controller, satisfies the given control objective. As for the analysis problem, we have only the information from the data to base our design. Therefore, we can only guarantee that our control objective is achieved if the designed controller achieves the design objective when interconnected with any system from the set Σ D.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem 1 (Informativity problem for analysis)", "weight": 1.0} -->

For the framework to allow for data-driven control problems, we will consider a given control objective O (for example, a system theoretic property or a guaranteed performance of the closed loop system). Denote by Σ O the set of all systems that satisfy the control objective O. For a given controller K, denote by Σ D ( K ) the set of all systems obtained as the interconnection of a system in Σ D with the controller K.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem 2 (Informativity problem for control)", "weight": 1.0} -->

Provide necessary and sufficient conditions on D under which the data are informative for the control objective O.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem 2 (Informativity problem for control)", "weight": 1.0} -->

The second step of data-driven control involves the design of a suitable controller.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

Under the assumption that the data D are informative for the control objective O, find a controller K such that Σ D ( K ) ⊆ Σ O.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

The data-driven control design problem as formulated here has a rather natural interpretation as a problem of robust control. Indeed, the aim is to find one single controller that achieves the design objective for all systems that are consistent with the data. In other words, the 'system uncertainty' is determined directly by the given data, and no attempt is made to identify in any sense an uncertainty description that is suitable for existing methods in robust control design. The given data are called informative for a given design objective if the associated robust control problem allows a solution for the system uncertainty imposed by the data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

The data informativity framework has already been applied to various analysis and design problems. Generally speaking, there is a dichotomy between two main directions. On the one hand there are analysis and design problems based on exact, i.e., noiseless data. On the other hand we consider the more realistic situation that the data are noisy, in the sense that they are obtained from a true, unknown, system that is corrupted by additive noise. Table 1 provides an overview of the results. The first column of the table states the considered system property or control design problem. The second column refers to the type of data that are used. Here, 'E' refers to exact data, and 'N' to noisy data. State, input-state, input-stateoutput and input-output are denoted by 'S', 'IS', 'ISO' and 'IO', respectively. The results in the table apply to discretetime systems, and most of the results are for linear timeinvariant dynamics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

| Problem | Data | References | The purpose of this paper is to highlight the strength of the informativity framework by reviewing a selection of analysis and design problems, indicated in Table 1 in red.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

Both exact and noisy data will be discussed in the present paper.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

This paper is divided into three main sections. These sections are divided into subsections, each devoted to a particular analysis or control design problem. In the first main section our model class will be chosen as the set of all discrete-time linear input-state systems with given state and input dimensions. The data are measurements of the state and input obtained from a true, unknown, system on a given finite time-interval. In this first section it is assumed that the data are noiseless, in the sense that the true system does not contain any noise input. In this noiseless framework we discuss the problem of informativity for the system properties controllability and stabilizability. Next, as a first control design problem we discuss the problem of stabilization by static state feedback, and take a look at the corresponding informativity problem. In the third subsection we study informativity in the context of the linear quadratic regulator problem, and, finally, in the fourth subsection we look at the classical problem of tracking and regulation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

In the second main section we incorporate noise into the models and data. The model class consists of all inputstate systems with additive noise and the input-state data are assumed to be obtained from the noisy true system. The additive noise is unknown, but its samples on the data sampling interval are assumed to satisfy a given quadratic matrix inequality. In this framework we discuss a number of analysis and control design problems. In the first subsection we again look at the problem of stabilization by state feedback, this time in a noisy setting. The next subsection deal with informativity in the context of the well known H ∞ control problem. The final subsection of this part deals with the problem of determining from noisy data whether an unknown system is dissipative with respect to a given supply rate.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem 3 (Control design problem)", "weight": 1.0} -->

In the third, final, main section we abandon the state space framework and shift to input-output systems represented by higher order difference equation, also called autoregressive (AR) systems. As model class we take all AR systems with additive noise, of a given order and with given input and output dimensions. The data are now input-output data that are obtained from the true noisy input-output system. We study data-driven stabilization by dynamic output feedback and discuss informativity in this framework.

<!-- chunk {"id": "body-0035", "role": "body", "section": "ANALYSIS AND CONTROL USING EXACT INPUT-STATE DATA", "weight": 1.0} -->

In order to provide a solid foundation for more complex problems, in this section we will first consider the essential model class of linear, time-invariant input-state systems. Our goal is to analyze and control these systems on the basis of input-state data, consisting of a finite number of measurements of the input and state trajectories. Moreover, we will assume that these measurements are exact, that is, not corrupted by any noise.

<!-- chunk {"id": "body-0036", "role": "body", "section": "ANALYSIS AND CONTROL USING EXACT INPUT-STATE DATA", "weight": 1.0} -->

Given this situation, we can make the abstract framework that was introduced in the introduction more tangible. To be precise, the unknown system S is assumed to be the following: where x denotes the n -dimensional state and u the m -dimensional input. In the following, we assume that the dimensions n and m are known, but the matrices As and Bs are unknown. As such, we see that S is contained in the model class M given by the set of all discrete-time linear input-state systems of the form with given state space and input dimensions n and m.

<!-- chunk {"id": "body-0037", "role": "body", "section": "ANALYSIS AND CONTROL USING EXACT INPUT-STATE DATA", "weight": 1.0} -->

Suppose that we collect input-state data from the true system on a set of time instances { 0, 1,..., T }, in the sense that we excite the true system with an input sequence u, u,..., u (T -1) and obtain measurements of a corresponding state sequence x, x,..., x (T). We can collect these measurements in matrices by defining: If, additionally, we define the matrices we have X + = AsX -+ BsU -, since the data were assumed to be generated by the true system. Moreover, this is all the information we have regarding the true system on the basis of the data D: = (U -, X). As explained in the introduction, we are interested in the set Σ D containing all systems in M that are consistent with these data. Obviously, this set In fact, there is no need for the data to be collected sequentially. It is straightforward to adapt the results above to the situation of measurements on multiple sets of time instances.

<!-- chunk {"id": "body-0038", "role": "body", "section": "ANALYSIS AND CONTROL USING EXACT INPUT-STATE DATA", "weight": 1.0} -->

First, we consider the problem of system identification. In the terminology of this paper, we say that the data (U -, X) are informative for system identification if the set Σ D contains exactly one element. Since by definition the true system (As, Bs) ∈ Σ D the data are informative for identification if and only if Σ D = { (As, Bs) }. Moreover it is the solution set of the affine equation appearing. Therefore, the data are informative for system identification if and only if the full rank condition holds. There exists a unique system in Σ D if and only if the condition holds, and this true system can then be obtained from the data as Once we have identified the true system is this way, we can apply model-based methods in order to verify its properties or to achieve the desired control objective. In the Sidebar 'Willems' fundamental lemma' we discuss the problem of designing inputs such that the resulting measurements are guaranteed to be informative for system identification.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Controllability and stabilizability", "weight": 1.0} -->

As we will show in this subsection, condition is not necessary to perform data-driven analysis in general. As an illustration, we will establish necessary and sufficient conditions in terms of the data for verifying controllability and stabilizability, which do not require the rank condition to hold.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Controllability and stabilizability", "weight": 1.0} -->

Recall from Definition 1 the definition of informativity of data for a given system property. In accordance with Definition 1 we say that the data ( U -, X ) are informative for controllability if all systems in Σ D are controllable. Likewise, we call the data informative for stabilizability if all systems in Σ D are stabilizable.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Controllability and stabilizability", "weight": 1.0} -->

In order to establish tests for these notions of informativity, the well known Hautus test for controllability can be used: a system (A, B) is controllable if and only if for all λ ∈ C. For stabilizability, the Hautus test requires that holds for all λ outside the open unit disc.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Controllability and stabilizability", "weight": 1.0} -->

The following theorem gives necessary and sufficient conditions on the input-state data to be informative for these two properties. The result provides tests on the given data matrices.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 1 (Full rank is not necessary)", "weight": 1.0} -->

Suppose that n = 2 and m = 1. Assume we collect data on the single time interval { 0, 1..., T } with T = 2 to obtain This implies that Using Theorem 1 we see that these data are informative for controllability, as Recall that this means that all systems consistent with the data are controllable. Therefore we can conclude that also the true system is controllable. Moreover, note that the rank condition does not hold, and therefore Σ D is not a singleton. To be precise: This means that there are multiple systems consistent with the data.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1 (Full rank is not necessary)", "weight": 1.0} -->

Computationally, the conditions and might seem daunting, since these require to test the rank of a matrix for each λ ∈ C. However, it is well known that in order for the classical Hautus test to be satisfied, it suffices to test the rank of for only λ ∈ σ ( A ), where σ ( A ) denotes the set of eigenvalues of the matrix A.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Willems' fundamental lemma", "weight": 1.0} -->

A s explained in the main text, the input-state data satisfy the full row rank condition if and only if the data are informative for identification, meaning that the true system can be uniquely determined from the data by solving a linear equation. This brings up the question whether it is possible to choose a time horizon T and a finite input sequence u, u,..., u ( T -1 ) such that condition is guaranteed to hold for any resulting state sequence. Indeed, if this could be done, then the true system could be uniquely determined from the data by choosing a suitable input sequence. In this sidebar we will discuss this question in the context of persistently exciting inputs and Willems' fundamental lemma.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Willems' fundamental lemma", "weight": 1.0} -->

In the sequel, denote any given finite sequence f, f,..., f (T -1) by f [0, T -1]. For a given finite input sequence u [0, T -1], define the associated Hankel matrix of depth k by The input sequence u [0, T -1] is called persistently exciting of order k if Hk (u [0, T -1]) has full row rank.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Willems' fundamental lemma", "weight": 1.0} -->

A special case of Willems' fundamental lemma [36, Thm. 1] (originally proven in a behavioral context in [33, Thm. 1]) is relevant in the context of informativity for identification. Consider a linear input-state-output system, defined by the quadrupel of matrices (A, B, C, D), with input, state and output denoted by u, x and y respectively. Let x [0, T -1] and y [0, T -1] denote the finite length state and output trajectories corresponding to the input sequence u [0, T -1]. Suppose that the system is controllable and observable, and that the input sequence u [0, T -1] is persistently exciting of order n + L. Denote XL = [x · · · x (T -L)]. Then a consequence of Willems' fundamental lemma is that the In a similar fashion, the conditions of Theorem 1 can be verified in a finite number of steps. Indeed, is equivalent to for all λ = 0 with λ -1 ∈ σ (X -X ♯ +), where X ♯ + is any right inverse of X +.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Willems' fundamental lemma", "weight": 1.0} -->

Regarding stabilizability, we obtain that is equivalent to

<!-- chunk {"id": "body-0049", "role": "body", "section": "Stabilization", "weight": 1.0} -->

After considering data-driven controllability and stabilizability analysis in the previous subsection, we now turn attention to data-driven control design. In particular, we has full row rank. A special case of this arises for L = 1, which shows that holds if we take u [0, T -1] to be persistently exciting of degree n + 1. This resolves the problem of designing inputs for informativity for identification in the context of inputstate measurements. More generally, in the case of input-output measurements, full row rank of (S1) enables the identification of the system matrices (A, B, C, D) up to similarity transformation if L is larger than the so-called lag of the system. This can be done, for example, by using subspace identification methods,.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Stabilization", "weight": 1.0} -->

On the other hand, in many applications an identified (state space) model might not be the most convenient representation to work. One of these applications is Data-enabled Predictive control (DeePC), introduced. As a data-driven variant of Model Predictive Control (MPC), the central problem is to minimize a cost function over all lengthL trajectories. A consequence of the fundamental lemma is that if the input sequence u [0, T -1] is persistently exciting of order n + L, then any ¯ u [0, L -1], ¯ y [0, L -1] is an input/output trajectory of the system if and only if As such, the fundamental lemma allows this problem to be formulated directly in terms of measurements, without explicitly finding a system model.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Stabilization", "weight": 1.0} -->

As it turns out, there are many other applications where avoiding the modeling step, and dealing with data directly is convenient. For example, the paper treats data-based simulation and output matching control, while provides methods for stabilization on the basis measurements for which holds. consider the quintessential control problem of stabilization by state feedback.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Stabilization", "weight": 1.0} -->

Recall the definition of informativity for control as given in Definition 2. We take the model class M and data D as before, and take as the control objective O: 'interconnection with a state feedback controller yields a stable 1, closed loop system'. This means that the set Σ O of all systems that satisfy the control objective is equal to the set of all stable n × n matrices For a given state feedback controller K ∈ R m × n, the corresponding set of closed loop systems consistent with 1 meaning Schur, that is, all its eigenvalues λ satisfy | λ | < 1. the data is equal to In line with Definition 2 we say that the data (U -, X) are informative for stabilization by state feedback if there exists a K ∈ R m × n such that Σ D (K) ⊆ M n × n stab.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Stabilization", "weight": 1.0} -->

At this point, one may wonder about the relation between informativity for stabilizability and informativity for stabilization. It is clear that the data ( U -, X ) are informative for stabilizability if ( U -, X ) are informative for stabilization by state feedback. However, the reverse statement does not hold in general. This is due to the fact that all systems ( A, B ) in Σ D may be stabilizable, but there may not exist a common feedback gain K such that A + BK is stable for all of these systems.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Stabilization", "weight": 1.0} -->

In other words, the input-state data ( U -, X ) are informative for stabilization by state feedback if there exists a single real m × n matrix K such that A + BK is stable for all ( A, B ) ∈ M that are consistent with the data.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Stabilization", "weight": 1.0} -->

The following example further illustrates the difference between informativity for stabilizability and informativity for stabilization.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example 2 (Stabilizability and stabilization)", "weight": 1.0} -->

Consider the scalar system x ( t + 1 ) = u ( t ), where x, u ∈ R. Suppose that we collect data on the single time interval { 0, 1 }, specifically, x = 0, u = 1 and x = 1. This means that U -= and X =. It can be shown that Σ D = { ( a, 1 ) | a ∈ R }. Clearly, all systems in Σ D are stabilizable. Nonetheless, the data are not informative for stabilization. This is because the systems ( -1, 1 ) and in Σ D cannot be stabilized by the same controller of the form u ( t ) = Kx ( t ). We conclude that informativity of the data for stabilizability does not imply informativity for stabilization by state feedback.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Example 2 (Stabilizability and stabilization)", "weight": 1.0} -->

Having defined the notion of informativity for stabilization, we now take the steps described in the introduction. First, we resolve Problem 2, that is, we find necessary and sufficient conditions for informativity for stabilization by state feedback. After this, we design a corresponding controller, as described in Problem 3.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Example 2 (Stabilizability and stabilization)", "weight": 1.0} -->

In order to do this, we first state a useful lemma. Recall from that (A, B) ∈ Σ D if and only if it is a solution of the the corresponding affine equation. Now let Σ 0 D denote the solution set of the corresponding homogeneous equation. That is, This allows us to state the following lemma.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Example 3 (Full rank not necessary for informativity)", "weight": 1.0} -->

Consider an unstable system (As, Bs), where As and Bs are given by We collect data from this system on a single time interval from t = 0 until t = 2, which results in the data matrices Clearly, the matrix X -is square and invertible, and it can be verified that is stable, since its eigenvalues are 1 2 (1 ± √ 2 i). We conclude by Theorem 2 that the data (U -, X) are informative for stabilization by state feedback. The same conclusion can be drawn from Theorem 3 since solves. Next, we can conclude from either Theorem 2 or Theorem 3 that the stabilizing feedback gain in this example is unique, and given by K = U -X -1 -= [-1 -0.5]. Finally, it is worth noting that the data are not informative for identification. In fact, (A, B) ∈ Σ D if and only if for some a 1 and a 2 ∈ R.

<!-- chunk {"id": "body-0060", "role": "body", "section": "The linear quadratic regulator problem", "weight": 1.0} -->

An important classical control design problem is the optimal linear quadratic regulator (LQR) problem. In this subsection we will study the data-driven version of this problem within the informativity framework.

<!-- chunk {"id": "body-0061", "role": "body", "section": "The linear quadratic regulator problem", "weight": 1.0} -->

For given state and input dimensions n and m, again consider the model class M of all discrete-time linear input-state systems. Assume we have input-state data on multiple time intervals, leading to data D: = ( U -, X ) as given. As before, the set Σ D of all systems in M that are consistent with the data is then given. We assume that the data are generated by the true (but unknown) system ( As, Bs ), which is therefore in Σ D itself.

<!-- chunk {"id": "body-0062", "role": "body", "section": "The linear quadratic regulator problem", "weight": 1.0} -->

In the context of the optimal LQR problem the control objective O is: 'the system must be controlled using the optimal feedback gain'. In order to formalize this, we introduce the following notation. For any given K, let Σ Q, R K denote the set of all systems of the form for which K is the optimal feedback gain corresponding to Q and R, that is, This gives rise to yet another notion of informativity in line with Definition 2. Indeed, informativity requires the existence of a single feedback gain that is optimal for all systems consistent with the data. For the definition of solvability of the optimal LQR problem we refer to the sidebar 'The linear quadratic regulator problem'.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The linear quadratic regulator problem", "weight": 1.0} -->

Consider the discrete time linear system where A and B are matrices of dimensions n × n and n × m, and where x is the n -dimensional state and u the m -dimensional input. In the linear quadratic regulator problem we quantify the performance of the system using a quadratic cost functional J (x 0, u) involving the state trajectory x and the input u. The optimal linear quadratic regulator problem is then the problem of finding, for each initial state x 0 of the system, an optimal input, i.e. an input that minimizes the cost functional. In this sidebar the basics of discrete-time linear quadratic optimal control are reviewed. In the sequel, the abbreviation 'LQR' will be used for 'linear quadratic regulator'.

<!-- chunk {"id": "body-0064", "role": "body", "section": "The linear quadratic regulator problem", "weight": 1.0} -->

For an initial state x 0, let x x 0, u be the state sequence of ( S2 ) resulting from the input u and initial condition x = x 0. We omit the subscript and simply write x whenever the dependence on x 0 and u is clear from the context.

<!-- chunk {"id": "body-0065", "role": "body", "section": "The linear quadratic regulator problem", "weight": 1.0} -->

Associated to system (S2), we define the quadratic cost functional where Q ∈ S n is positive semidefinite and R ∈ S m is positive definite.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Problem 4 (The LQR problem)", "weight": 1.0} -->

Determine for every initial condition x 0 an input u ∗, such that lim t → ∞ x x 0, u ∗ ( t ) = 0, and the cost functional J ( x 0, u ) is minimized under this constraint.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Problem 4 (The LQR problem)", "weight": 1.0} -->

Such an input u ∗ is called optimal for the given x 0. Of course, an optimal input does not necessarily exist for all x 0. We say that the optimal LQR problem is solvable for ( A, B, Q, R ) if for every x 0 there exists an input u ∗ such that

<!-- chunk {"id": "body-0068", "role": "body", "section": "Problem 4 (The LQR problem)", "weight": 1.0} -->

- 1) The cost J (x 0, u ∗) is finite. - 2) The limit lim t → ∞ x x 0, u ∗ (t) = 0. conditions for informativity for optimal linear quadratic regulation.

<!-- chunk {"id": "body-0069", "role": "body", "section": "The problem of tracking and regulation", "weight": 1.0} -->

Yet another important classical control design problem is the problem of tracking and regulation, also called the algebraic regulator problem, as studied, for example, in - and the textbooks, ). This is the problem of finding a feedback controller (called a regulator) such that the output of the resulting controlled system tracks a given reference signal, regardless of the disturbance input entering the system and the initial state. The relevant reference signals and disturbances (such as step functions, ramps or sinusoids) are assumed to be solutions of a suitable autonomous linear system. Given a class of reference and disturbance signals, one first constructs a suitable autonomous system (called the exosystem) that has these reference and disturbance signals as solutions. Next, this exosystem is interconnected to the system to be controlled (called the endosystem) and the difference between the original system output and the reference signal is taken as output. Finally, a regulator should be designed to make the output of the interconnection converge to zero for all disturbances and initial states.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The problem of tracking and regulation", "weight": 1.0} -->

In a data-driven context, the true endosystem is assumed to be unknown, and no mathematical model is available. Instead, we collect data on the input, endosystem state, and exosystem state in the form of samples on a finite time-interval. Whereas the true endo-system is unknown, the exosystem is assumed to be known, since this system models the reference signals and possible disturbance inputs. Also, the matrices in the output equations are assumed to be known, since these specify the design specification (namely the output that should converge to zero) on the controlled system. A given set of data will then be called informative for regulator design if the data contain sufficient information to design a single regulator for the entire family of systems that are consistent with this set of data. In this section we will study this data-driven regulator problem, and provide necessary and sufficient conditions for informativity for regulator design.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The problem of tracking and regulation", "weight": 1.0} -->

Consider a true, unknown, endosystem represented by Here, x 2 is the n 2 -dimensional state, u the m -dimensional input, and x 1 the n 1-dimensional state of the exosystem that generates all possible reference signals and disturbance inputs. The dimensions n 1, n 2 and m are known, but the matrices A 2 s and B 2 s are unknown. Since A 3 specifies how the disturbances and reference signals enter the system, we assume that it is known. Also the exosystem matrix A 1 is known. The output to be regulated is specified by where the matrices D 1, D 2 and E are known. By interconnecting the endosystem with the state feedback controller we obtain the controlled system If z (t) → 0 as t → ∞ for all initial states x 1 and x 2, we say that the controlled system is output regulated. If A 2 s + B 2 sK 2 is a stable matrix we call the controlled system endo-stable. If the control law makes the controlled system both output regulated and endo-stable, we call it a regulator.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The problem of tracking and regulation", "weight": 1.0} -->

Since we do not know the true endosystem, the design of a regulator can only be based on available data.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The problem of tracking and regulation", "weight": 1.0} -->

These data are finite sequences of samples of x 1 (t), x 2 (t) and u (t) on a given time interval { 0, 1,..., T } given by An endosystem with (unknown) system matrices (A 2, B 2) is called consistent with these data if A 2 and B 2 satisfy the equation The set of all (A 2, B 2) that are consistent with the data is denoted by Σ D, i.e., We assume that the true endosystem (A 2 s, B 2 s) is in Σ D, i.e. the true system is consistent with the data. In general, the equation does not specify the true system uniquely, and many endosystems (A 2, B 2) may be consistent with the same data.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The problem of tracking and regulation", "weight": 1.0} -->

Now we turn to controller design based on the data ( U -, X 1 -, X 2 ). Since on the basis of the given data we can not distinguish between the true endosystem and any other endosystem consistent with these data, a controller will be a regulator for the true system only if it is a regulator for any endosystem with ( A 2, B 2 ) in Σ D. If such regulator exists, we call the data informative for regulator design.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 4 (Illustration of the theory)", "weight": 1.0} -->

Consider the two-dimensional endosystem where A 2 s and B 2 s are unknown 2 × 2 and 2 × 1 matrices, respectively. Let x 2 = [x 21 x 22] T. The disturbance input d is assumed to be a constant signal with finite amplitude, so is generated by d (t + 1) = d (t). We want to design a regulator so that 2 x 21 + 1 2 x 22 tracks a given reference signal. In this example, the reference signals r are assumed to be generated by a given autonomous linear system with state space dimension, say, n 1. Its representation will be irrelevant here. The total exosystem will then have state space dimension n 1 + 1, and our output equation is given by z (t) = D 1 x 1 (t) + D 2 x 2 (t) + E u (t), with D 1 a 1 × (n 1 + 1) matrix such that D 1 x 1 = -r and D 2 =. We take E = 2. Also note that A 3 = [01 × n 1 0 01 × n 1 1]. Here, 0 1 × n 1 denotes 1 × n 1 zero matrix.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 4 (Illustration of the theory)", "weight": 1.0} -->

Suppose that T = 2 and assume we have the following data: These data can be seen to be generated by the true endosystem A 2 s =, B 2 s =. We now check condition 1) of Theorem 8. First note that, indeed, im D 1 ⊆ im E. Also, X 2 -is non-singular and (X 2 + -A 3 X 1 -) X -1 2 -=. This matrix has eigenvalues 1 2 ± 1 2 i, so is stable. Finally, D 2 + EU -X -1 2 -= 0. According to Theorem 8, a regulator for all endosystems consistentwith the given data is given by It can be verified that the set of endosystems consistentwith our data is equal to the affine set The controller given by is a regulator for all these endosystems.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 4 (Illustration of the theory)", "weight": 1.0} -->

Data-driven regulator design has also been studied in and. The perspective of these contributions is however quite different from the one discussed in this subsection. We also mention alternative methods that deal with tracking objectives, such as iterative feedback tuning (IFT) and virtual reference feedback tuning (VRFT) as developed in and, respectively. Also these methods do not address the classical regulator problem, and are very different from the work discussed here.

<!-- chunk {"id": "body-0078", "role": "body", "section": "ANALYSIS AND CONTROL USING NOISY INPUT-STATE DATA", "weight": 1.0} -->

So far, we have focused on analysis and design of inputstate systems using exact data. In this section, we shift our attention to input-state systems with noise. We will first introduce the model class that we will be using, and discuss the assumptions that will be made on the noise samples.

<!-- chunk {"id": "body-0079", "role": "body", "section": "ANALYSIS AND CONTROL USING NOISY INPUT-STATE DATA", "weight": 1.0} -->

Suppose that the unknown, true system is given by where x ∈ R n is the state, u ∈ R m is the control input and w ∈ R n is an unknown noise term. The matrices As ∈ R n × n and Bs ∈ R n × m denote the unknown state and input matrices. We embed this unknown system into the model class M of all input-state systems with unknown process noise, with fixed dimensions n and m, of the form Suppose that we obtain input-state data from the true system. These data are given in the matrices We denote the submatrix of X consisting of its first (respectively, last) T columns by X -(respectively, X +). The noise w is unknown, so w, w,..., w (T -1) are not measured, and therefore are not part of the data. We do however assume that we have the following information on the noise during the data sampling period.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

The unknown noise samples w, w,..., w (T -1), collected in the matrix satisfy the quadratic matrix inequality where Φ ∈ S n + T is a given partitioned matrix with Φ 11 ∈ S n, Φ 12 ∈ R n × T, Φ 21 = Φ ⊤ 12 and Φ 22 ∈ S T, and where we assume that Φ ∈ Π n, T (as defined in (S7) of the Sidebar 'Quadratic matrix inequalities').

<!-- chunk {"id": "body-0081", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

In other words, the data D consist of the measurements ( U -, X ) together with the information that the noise on the sampling interval { 0,..., T } satisfies the inequality for a partitioned matrix Φ ∈ Π n, T.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

Of course, an issue is whether the set of noise matrices W -defined by is nonempty. This is equivalent to the nonemptiness of the set Z T ( Φ ), as defined in ( S6 ). This issue is discussed in more detail in the Sidebar 'Quadratic matrix inequalities'. Indeed, under the assumption Φ ∈ Π n, T the set Z T ( Φ ) is nonempty and convex. Consequently then, the set of of noise matrices W -satisfying is nonempty and convex.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

In order to make the above quadratic inequality constraint on the matrix of noise samples more concrete, we will now look at a number of special cases.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

- 1) In the special case Φ 12 = 0 and Φ 22 = -I, the quadratic inequality reduces to The inequality can be interpretated as saying that the energy of w has a given upper bound on the time interval { 0,..., T -1 }.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

- 3) In some cases, we may know a priori that the noise w does not directly affect the entire state-space, but is contained in a subspace, say im E, with E a known n × d matrix. This prior knowledge can be captured by the noise model in Assumption 11. Indeed, suppose that w (t) = E ˆ w (t) for all t = 0, 1, 2..., T -1, where ˆ w (t) ∈ R d and E ∈ R n × d is a given matrix of full column rank. The matrix ˆ W -= [ˆ w ˆ w · · · ˆ w (T -1)] captures the noise.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

As before, ˆ W -is unknown but is assumed to satisfy ˆ W ⊤ -∈ Z T (ˆ Φ), where ˆ Φ ∈ Π d, T is such that ˆ Φ 22 < 0. It can then be shown that W -= E ˆ W -for some ˆ W ⊤ -∈ Z T (ˆ Φ) if and only if W ⊤ -∈ Z T (Φ), where - 2) Norm bounds on the individual noise samples w (t) also give rise to bounds of the form, although this does introduce some conservatism in general. Indeed, note that for all t the pointwise norm bound ‖ w (t) ‖ 2 2 ⩽ ϵ is equivalent to the matrix inequality w (t) w (t) ⊤ ⩽ ϵ I. As such, the bound is satisfied for Φ 11 = T ϵ I.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

The conclusion is that Assumption 11 also covers the case in which the noise is constrained to a known subspace, which is captured by the noise bound with Φ.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Assumption 11 (Noise model)", "weight": 1.0} -->

- 4) As shown in [70, Section 5.4], these noise models can also be applied in settings of Gaussian noise. To be precise, such sets can be employed as confidence intervals corresponding to a given probability.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Quadratic stabilization", "weight": 1.0} -->

In this subsection we will take a look at the problem of quadratic stabilization using noisy input-state data. Quadratic stabilization means that all systems in the set Σ D of systems consistent with the data can be stabilized by the same state feedback gain, with a common Lyapunov function for all closed loop systems. In particular then, this feedback gain will stabilize the unknown system. Conditions for the existence of such feedback gain will be in terms of feasibility of certain linear matrix inequalities involving the data ( X, U -) and the (known) matrix Φ representing the quadratic inequality constraint on the matrix of noise samples. In addition, the controller gain will be computed in terms of solution to these linear matrix inequalities.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Quadratic stabilization", "weight": 1.0} -->

As explained before, we have access to the input-state data D = (U -, X). The possible matrices W -of noise samples satisfy the quadratic inequality for a given matrix Φ ∈ Π n, T. This means that the set Σ D of all systems consistent with the data is equal to the set of all systems (A, B) satisfying for some W -satisfying, i.e., Σ D = { (A, B) | holds for some W -satisfying }.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Quadratic matrix inequalities", "weight": 1.0} -->

A great deal can be said about sets defined in terms of quadratic matrix inequalities (QMIs). Such sets play an important role in robust control, where they are used to describe parameter uncertainty -. Also in the context of this paper they are important, since they describe sets of systems consistent with the data. We will briefly discuss sets of the form   for Π ∈ S q + r, and we refer to for more details. In what follows, we assume that Π ∈ S q + r is partitioned as where Π 11 ∈ S q, Π 12 = Π ⊤ 21 ∈ R q × r and Π 22 ∈ S r. The very first question one may ask is: under what conditions on Π is the set Z r (Π) nonempty? An immediate necessary condition is that Π must have at least q nonnegative eigenvalues. However this is not sufficient in general. It turns out that for particular matrices Π, a Schur complement argument on the matrix Π leads to a simple characterization of nonemptiness of the set Z r (Π).

<!-- chunk {"id": "body-0092", "role": "body", "section": "Quadratic matrix inequalities", "weight": 1.0} -->

Specifically, suppose that Π 22 ⩽ 0 and ker Π 22 ⊆ ker Π 12. Since the latter condition is equivalent to Π 12 Π 22 Π † 22 = Π 12, we have that where Π | Π 22: = Π 11 -Π 12 Π † 22 Π 21 is the (generalized) Schur complement of Π with respect to Π 22. This can be used to prove the following conditions for nonemptiness of Z r (Π).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Motivated by this, we define the set", "weight": 1.0} -->

Next, for Π ∈ Π q, r we will investigate properties of the sets Z r (Π) and the following closely related set  involving a strict inequality.

<!-- chunk {"id": "body-0094", "role": "body", "section": "MATRIX VERSIONS OF YAKUBOVICH'S S-LEMMA", "weight": 1.0} -->

Yakubovich' S-lemma is a classical result with a wide range of applications, most notably the problem of absolute stability of Lur'e systems. Roughly speaking, this result says that one quadratic inequality implies another one if and only if a certain linear matrix inequality (LMI) is feasible. A seemingly difficult implication involving quadratic functions is thereby replaced by a convex problem which can be solved using computational tools such as Sedumi and Mosek. In this section we deal with matrix versions of the S-lemma, i.e., with the question under what conditions all solutions to one quadratic matrix inequality also satisfy another QMI. In other words, we state necessary and sufficient conditions for the inclusion Z r (N) ⊆ Z r (M), where M, N ∈ S q + r. We will also consider a similar inclusion with Z + r (M) instead of Zr (M). This leads to non-strict and strict versions of Y akubovich's S-lemma.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Non-strict inequalities", "weight": 1.0} -->

The following theorem states the matrix S-lemma for nonstrict inequalities.

<!-- chunk {"id": "body-0096", "role": "body", "section": "A strict and non-strict inequality", "weight": 1.0} -->

Next, we consider strict versions of the matrix S-lemma. This means that we consider the set Z + r ( M ) instead of Z r ( M ), i.e., a strict inequality on the QMI induced by M. Note that in this case, the Slater condition on N is not required.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Related conditions for quadratic stabilization", "weight": 1.0} -->

Theorem 17 gives a necessary and sufficient LMI condition under which all systems consistent with the data are quadratically stabilizable by a single feedback gain K. In this section we compare this result to other conditions within the literature on data-driven control.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Related conditions for quadratic stabilization", "weight": 1.0} -->

We begin with [22, Thm. 6]. This result works under the assumption that holds, and X + has full row rank. Moreover, it is assumed that for some γ > 0. Under these assumptions, [22, Thm. 6] states that the data (U -, X) are informative for quadratic stabilization if there exists a matrix Q ∈ R T × n and a scalar α > 0 such that X -Q is symmetric and If (Q, α) solve, then K: = U -Q (X -Q) -1 quadratically stabilizes all systems in Σ (U -, X). We note that the inequality can be interpreted as a special case of with Φ 11 = γ X + X ⊤ +, Φ 12 = 0 and Φ 22 = -I.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Related conditions for quadratic stabilization", "weight": 1.0} -->

Yet another condition for quadratic stabilization is given. This paper works with a noise model that can be interpreted as the dual of. More precisely, it is assumed that for known matrices Qw ∈ S n, Sw ∈ R n × T and Rw ∈ S T with Rw > 0. To make a meaningful comparison, we will assume the same bound as. This can also be stated equivalently in terms of the noise model by choosing the specific matrices Qw = -(γ X + X ⊤ +) -1, Sw = 0 and Rw = I. Then, the main result of [100, Cor. 6, Rem. 7] is that the data (U -, X) are informative for quadratic stabilization if there exist matrices Y ∈ S n and M ∈ R T × n satisfying We note that the conditions from and are stated as sufficient conditions for quadratic stabilization. It is an interesting question whether these conditions are also necessary for quadratic stabilization. Indeed, in this case, they would then be equivalent to those of Theorem 17 (for the noise model in). It turns out, however, that this is not the case.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Related conditions for quadratic stabilization", "weight": 1.0} -->

To show this, one can consider the true system described by the matrices As = 1 and Bs = 1. Suppose that T = 3 and the noise matrix is given by We collect the data samples Throughout the example, we assume that we have access to the noise bound W -W ⊤ -⩽ 1. Note that this bound is indeed satisfied, and that it can be captured using Assumption 11 by the choices Φ 11 = 1, Φ 12 = 0 and Φ 22 = -I. We also note that this is equivalent to noise model with Qw = -1, Sw = 0 and Rw = I, and to noise model with γ = 1. As such, we can compare the design methods reported in Theorem 17 of this paper with the approaches in [100, Cor. 6, Rem. 7] and [22, Thm. 6].

<!-- chunk {"id": "body-0101", "role": "body", "section": "Related conditions for quadratic stabilization", "weight": 1.0} -->

For this example, it can be shown analytically that only the LMI condition of Theorem 17 is feasible while those in - and - are not. At a high level, the reason for this is that the approach of relies on a number of possibly conservative bounds, while the method from utilizes an overparameterization of the set of consistent systems.

<!-- chunk {"id": "body-0102", "role": "body", "section": "The H ∞ control problem", "weight": 1.0} -->

Denote by ℓ q 2 (Z +) the linear space of all sequences v with v (t) ∈ R q and t ∈ Z + such that ∑ ∞ t = 0 ‖ v (t) ‖ 2 < ∞. For any such sequence v, define its ℓ 2-norm as The informativity framework also allows a treatment of the data-driven H ∞ control problem. This will be the topic of the current subsection. We first review some basic material that will be needed in order to formulate the problem.

<!-- chunk {"id": "body-0103", "role": "body", "section": "The H ∞ control problem", "weight": 1.0} -->

Next, consider the discrete-time input-state-output system with w (t) ∈ R q and z (t) ∈ R p. Let its transfer matrix be denoted by G (z): = C (zI -A) -1 E + D. If we take as initial state x = 0, then each input sequence w on Z + yields a unique output sequence z on Z +. If A is stable, then this output sequence z is in ℓ p 2 (Z +) whenever w is in ℓ q 2 (Z +).

<!-- chunk {"id": "body-0104", "role": "body", "section": "Dissipativity analysis", "weight": 1.0} -->

In this subsection, we study dissipativity of linear finitedimensional input-state-output systems from a data-driven perspective. This problem has received considerable attention, and we mention the papers as the approaches that are closest to the one taken here. In, the notion of (finite-horizon) L -dissipativity was introduced. This was further studied. Both contributions rely on the notion of persistently exciting input data (see and the sidebar 'Willems' fundamental lemma"). This property of the input sequence implies that the data-generating system is uniquely identifiable from the data.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Dissipativity analysis", "weight": 1.0} -->

In this paper we adopt the more classical notion of dissipativity for linear systems, rather than L -dissipativity. Indeed, we consider a setup similar to that of, where sufficient data-based conditions were given for dissipativity. Here, we employ the informativity approach to derive necessary and sufficient conditions.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Dissipativity analysis", "weight": 1.0} -->

We will first review the definition of dissipativity. Consider a discrete-time linear input-state-output system where A ∈ R n × n, B ∈ R n × m, C ∈ R p × n, and D ∈ R p × m are given matrices. Let S ∈ S m + p. The system is said to be dissipative with respect to the supply rate if there exists P ∈ S n with P ⩾ 0 such that the dissipation inequality holds for all t ⩾ 0 and for all trajectories (u, x, y): Z + → R m + n + p of. It follows from that dissipativity with respect to the supply rate is equivalent with the feasibility of the linear matrix inequalities P ⩾ 0 and In the framework of data-driven system analysis, the system matrices are unknown. The question we want to study then is whether we can verify dissipativity using only the input-state-output data obtained from the unknown system. In the present section we will study this question for the situation that our data are noiseless.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Dissipativity analysis", "weight": 1.0} -->

Consider the unknown input-state-output system with u (t) ∈ R m, x (t) ∈ R n and y (t) ∈ R p the input, state and output. We assume that the dimensions m, n and p are known, but the true system matrices (As, Bs, Cs, Ds) are unknown. What is known instead are a finite number of input-state-output measurements of.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Dissipativity analysis", "weight": 1.0} -->

More concrete, we suppose that we have collected input-state-output data. Let U -, X, X -, and X + be defined as the previous section and let Y -be defined in a similar way as U -. Our data are now given by D = (U -, X, Y -). These data are assumed to be generated by the true system (As, Bs, Cs, Ds), which means that The set of all systems that are consistent with these data is then given: It follows from that the unknown system (As, Bs, Cs, Ds) is contained in Σ (U -, X, Y -). Our goal is to infer from the data (U -, X, Y -) whether the unknown system is dissipative.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Dissipativity analysis", "weight": 1.0} -->

On the basis of the given data we are unable to distinguish between the systems in Σ ( U -, X, Y -), in the sense that any of these systems could have generated the data. Nonetheless, if all of these systems are dissipative, then we can also conclude that the true data-generating system is dissipative. With this in mind, we now define the property of informativity for dissipativity for the case of noiseless data.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Assumption 21 (Noise model)", "weight": 1.0} -->

The noise samples, collected in the real (n + p) × T matrix satisfy the quadratic matrix inequality where Φ ∈ S n + p + T is a given partitioned matrix with Φ 11 ∈ S n + p, Φ 12 ∈ R (n + p) × T, Φ 21 = Φ ⊤ 12 and Φ 22 ∈ S T. We assume that Φ ∈ Π n + p, T. Then Z T (Φ) is nonempty and convex (see Sidebar 'Quadratic matrix inequalities"). We have that V -satisfies if and only if V ⊤ - ∈ Z T (Φ).

<!-- chunk {"id": "body-0111", "role": "body", "section": "Assumption 21 (Noise model)", "weight": 1.0} -->

We now turn to defining the property of informativity for dissipativity for noisy input-state-output data, i.e. data that are generated by the unknown system with unknown process noise and measurement noise whose samples satisfy the quadratic matrix inequality. As our model class M we take all noisy input-state-output systems with input dimension m, state space dimension n and output dimension p. Given the input-state-output data (U -, X, Y -) together with the information that the matrices of noise samples satisfy, the set of all systems consistent with the data is then given by We assume that the data have been obtained from the unknown system, i.e., (As, Bs, Cs, Ds) ∈ Σ D. Therefore, Σ D is nonempty.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Assumption 21 (Noise model)", "weight": 1.0} -->

Define Note that (A, B, C, D) ∈ Σ D if and only if This can be restated equivalently as From Assumption 21 we have Φ 22 ⩽ 0 and therefore N 22 ⩽ 0. It follows from the assumption ker Φ 22 ⊆ ker Φ 12 that ker N 22 ⊆ ker N 12. Since Z n + m (N) is nonempty it follows from Theorem 12 of Sidebar 'Quadratic matrix inequalities" that N | N 22 ⩾ 0. Thus the matrix N given by is in Π n + p, n + m.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Assumption 21 (Noise model)", "weight": 1.0} -->

Next, we give the definition of informativity for dissipativity in the context of noisy input-state-output data. Again, we will require that all systems consistent with the data are dissipative with a common storage function.

<!-- chunk {"id": "body-0114", "role": "body", "section": "AUTO-REGRESSIVE SYSTEMS AND NOISY INPUT-OUTPUT DATA", "weight": 1.0} -->

Whereas the first two sections of this paper have dealt with input-output systems in state space form together with input-state data, in the current section we will abandon the state space framework and consider input-output systems described by higher order difference equations, also called auto-regressive (AR) systems. Instead of input-state data we will assume to have (noisy) input-output data. In this framework we will discuss data-driven stabilization. Several contributions in the literature have also dealt with input-output data. A general strategy in these papers is to construct an artificial state-space representation of the system with a state comprised of shifts of the inputs and outputs. This leads to an inputstate-output system to which techniques for state data (as discussed before in this paper) are applicable. A drawback of this approach is that the obtained state space systems are non-minimal and of high dimension. Thus a large amount of data can be required for control (see e.g. [22, Section VIC]). In addition, the system matrices of the state-space representation are structured and consist of a combination of known and unknown blocks.

<!-- chunk {"id": "body-0115", "role": "body", "section": "AUTO-REGRESSIVE SYSTEMS AND NOISY INPUT-OUTPUT DATA", "weight": 1.0} -->

Often, this structure is not taken fully into account, which can lead to rather conservative conditions for data-driven control design. Exploiting this prior knowledge of the system matrices is an important problem, which has recently been studied.

<!-- chunk {"id": "body-0116", "role": "body", "section": "AUTO-REGRESSIVE SYSTEMS AND NOISY INPUT-OUTPUT DATA", "weight": 1.0} -->

Motivated by these limitations of an artificial state space, the main purpose of this section is to discuss a theory on data driven design of stabilizing feedback controllers on the basis of input-output data, without relying on state construction.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Stabilization using input-output data", "weight": 1.0} -->

We consider input-output systems with additive noise represented by auto-regressive AR models of the form Here L is a positive integer, called the order of the system. The input u (t) and output y (t) are assumed to take their values in R m and R p, respectively. The term v (t) represents unknown noise. The parameters of the model are real p × p matrices P 0, P 1,..., PL -1 and p × m matrices Q 0, Q 1,..., QL -1. Using the shift operator (σ f)(t) = f (t + 1), can be written as where P (ξ) and Q (ξ) are the real p × p and p × m polynomial matrices defined by Since the leading coefficient matrix of P (ξ) is the p × p identity matrix, P is invertible as a rational matrix and P -1 (ξ) Q (ξ) is strictly proper. Thus, indeed, represents a causal input-output system with control input u, noise input v and output y.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Stabilization using input-output data", "weight": 1.0} -->

A feedback controller for the input-output system with P (ξ) and Q (ξ) of the form will be taken to be of the form The leading coefficient matrix of G (ξ) is assumed to be the m × m identity matrix and Gi ∈ R m × m, Fi ∈ R m × p for i = 0, 1,..., L -1. The closed loop system obtained by interconnecting a system of the form and the controller is represented by Note that the leading coefficient matrix is the q × q identity matrix. We call the controller a stabilizing controller for if the corresponding autonomous system is stable, in the sense that all solutions u and y of tend to zero as time tends to infinity. The problem that we consider is to find a feedback controller of the form that stabilizes the unknown true system For this, we assume that the order L is known, and that only data obtained from the true system can be used.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Stabilization using input-output data", "weight": 1.0} -->

These data are the input-output data given by u, u,..., u (T), y, y,..., y (T) on the interval [0, T] with T ⩾ L. These are samples of u and y satisfying the system equation for some noise signal v.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Assumption 23 (Assumption on the noise)", "weight": 1.0} -->

The noise samples v, v,..., v (T -L), collected in the real p × (T -L + 1) matrix satisfy the quadratic matrix inequality where Π ∈ S p + T -L + 1 is a known partitioned matrix with Π 11 ∈ S p, Π 12 ∈ R p × (T -L + 1), Π 21 = Π ⊤ 12 and Π 22 ∈ S T -L + 1. We assume that Π ∈ Π p, T -L + 1 By Proposition 12 the set of matrices V that satisfy is nonempty.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Assumption 23 (Assumption on the noise)", "weight": 1.0} -->

As noted before in this paper, in general the given data u, u,..., u ( T ), y, y,..., y ( T ) do not determine the true system uniquely. In fact, the data determine a whole set of systems that are consistent with the data. As a consequence, finding a stabilizing controller for the true system based only on the data requires finding a controller that stabilizes all systems that are consistent with the data. If, for given data, such controller exists, then we call the input-output data informative for stabilization. This will now be made precise. In order to do this, first the set of all systems that are consistent with the data will be specified.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Assumption 23 (Assumption on the noise)", "weight": 1.0} -->

After denoting q: = p + m, R (ξ) = [-Q (ξ) P (ξ)] and z = col (u, y), can be rewritten as Collect the (unknown) coefficient matrices of the polynomial matrix R (ξ) in the p × qL matrix Note that, with a slight abuse of notation, we denote both the polynomial matrix and its coefficient matrix by R. We call the coefficient matrix of the system. Arrange the data u, u,..., u (T), y, y,..., y (T) into the vectors and define the associated depth L + 1 Hankel matrix by where H 1 (z) contains the first qL rows and H 2 (z) the last p rows. It is then easily verified that any input-output system for which the coefficient matrix R defined in satisfies for some V ∈ Z T -L + 1 (Π), could have generated the given input-output data.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Assumption 23 (Assumption on the noise)", "weight": 1.0} -->

In other words, z, z,..., z (T) are also samples on the interval [0, T] of a z that satisfies R (σ) z = v for some v satisfying Assumption 23. Therefore, R satisfies for some V ∈ Z T -L + 1 (Π) if and only if the AR system with coefficient matrix R is consistent with the data. Recall that, in particular, the true system is consistent with the data. Now define Then by combining and we see that the system with coefficient matrix R is consistent with the data if and only if R ⊤ satisfies the QMI Thus we have succeeded in finding an explicit expression for the set of systems that are consistent with the data. Indeed, this set is equal to Since the true system is consistent with the data, this set is nonempty.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Assumption 23 (Assumption on the noise)", "weight": 1.0} -->

Our aim is to find a single controller of the form that stabilizes all input-output systems that are consistent with the data, so all systems in Σ D. In order to investigate the existence of such controller, we will now first study stability of autonomous systems in AR form.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Assumption 23 (Assumption on the noise)", "weight": 1.0} -->

Given a nonsingular p × p polynomial matrix P ( ξ ), the corresponding autonomous AR system P ( σ ) y = 0 is called stable if y ( t ) → 0 as t → ∞ for all solutions y: Z + → R p. This space of all solutions on Z + is called the behavior of the system and is denoted by B ( P ). Stability of autonomous AR systems can be characterized in terms of quadratic difference forms on behaviors. For details on QDFs, see: 'Quadratic Difference Forms'. In a continuoustime context, the connection between stability and QDFs was studied, while the discrete-time version was considered.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Quadratic difference forms", "weight": 1.0} -->

A crucial instrument in studying stability of systems is the notion of Lyapunov function. Studying stability of autonomous systems in AR form requires the notion of Lyapunov functions given by quadratic difference forms (QDFs). In this sidebar we review the basic material on QDFs and establish some useful preliminary results. For more details, we refer to,.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Quadratic difference forms", "weight": 1.0} -->

Let N and q be positive integers and for i, j = 0, 1,..., N let Φ i, j ∈ R q × q be such that Φ i, i ∈ S q and Φ i, j = Φ ⊤ j, i for all i = j. Arrange these matrices into the partitioned matrix Φ ∈ S (N + 1) q given by Then the quadratic difference form associated with Φ is the operator Q Φ that maps R q -valued functions z on Z + to R -valued functions Q Φ (z) on Z + defined by In terms of the matrix Φ this can be written as Thus, vector valued functions are mapped to quadratic expressions in terms of these function and their time shifts up to a certain dergree.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Quadratic difference forms", "weight": 1.0} -->

Obviously, some of the matrices Φ i, j, or even an entire block row or column of Φ could be zero. We define the degree of the QDF (S1) as the smallest integer d such that Φ ij = 0 for Collect the coefficient matrices of F (ξ) and G (ξ) in the matrix C defined by and recall the definition of the coefficient matrix R associated likewise with R (ξ). Note that the leading coefficient matrix of the polynomial matrix [C (ξ) ⊤ R (ξ) ⊤] ⊤ is the q × q identity matrix. Furthermore, its coefficient matrix is [C ⊤ R ⊤] ⊤. Recall that the controller is a stabilizing controller for the input-ouput system if and only if the autonomous system is stable. As an immediate consequence of Theorem 24 we then have

<!-- chunk {"id": "body-0129", "role": "body", "section": "Simulation example", "weight": 1.0} -->

In this example, we consider a model of a magnetic suspension system, where an electromagnet is used to levitate a magnetic mass. We assume that we can measure the vertical position of the mass and control the current of the electromagnet with the aim of stabilizing the mass at a pre-determined position. Of course, in the context of this paper, we will develop such a controller on the basis of collected measurements.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Simulation example", "weight": 1.0} -->

For a detailed derivation of the model, see [109, Example 1.18]. Following [109, Example 12.8], we let x 1 denote the vertical position and x 2 the vertical velocity of the ball. Moreover, x 3 denotes the current and ˆ u the voltage of the circuit. The model is then given: where L (x 1) = L 1 + L 0 a a + x 1. Defining the function f accordingly, we write this system as ˙ x = f (x, ˆ u).

<!-- chunk {"id": "body-0131", "role": "body", "section": "Simulation example", "weight": 1.0} -->

As noted, we are interested in stabilizing the ball at x 1 = r > 0, on the basis of measurements of x 1. In order to apply the results of this paper, we will first linearize the model around the corresponding equilibrium point. After this, we will discretize and rewrite it to an AR model of the form considered in this paper.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Simulation example", "weight": 1.0} -->

For the physical quantities we will use the following values: First, we solve f (x, ˆ u) = 0 with x 1 = r in order to obtain the equilibrium point of interest of the system. This yields the solution We can shift the equilibrium point to the origin by defining ¯ x = x -x 0, and u = ˆ u -ˆ u 0, obtaining in the new variables: Linearizing this around the origin yields ˙ ¯ x = A ¯ x + Bu, where Since we want to control the system on the basis of measurements of ¯ x 1, we add an output y = C ¯ x, where C: =. Now, we can discretize this with step size δ > 0 and obtain In order to obtain an AR model, note that for each s ⩾ 1 we have that The characteristic polynomial of I + δ A is denoted The Cayley-Hamilton theorem states that χ (I + δ A) = 0. Therefore, we obtain that: where the matrices Q 0, Q 1, and Q 2 are given: This brings the model into the form considered in this paper.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Simulation example", "weight": 1.0} -->

In this simulation example, we will perform measurements on the (discretized) nonlinear system. We will treat this nonlinear system as an AR model of the form where the additive noise term v ( t ) captures the nonlinearities. Using the methods of this paper, we will find a stabilizing controller for all such systems consistent with the measurements and a noise model of the form VV ⊤ ⩽ ϵ.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Simulation example", "weight": 1.0} -->

We obtain measurements of the system close to the equilibrium point. To be precise we take δ = 0.005, T = 28, and generate random inputs from the interval 10 -5. These are applied to the nonlinear system with given initial conditions. The measurements resulting from this can be seen. For these measurements, we observe that VV ⊤ ⩽ 10 -17.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Simulation example", "weight": 1.0} -->

FIGURE 3 The results of interconnecting the controller with the linearized system, two other systems consistent with the data, and the original nonlinear system.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Simulation example", "weight": 1.0} -->

We will use Theorem 25 to show that these measurements are informative for quadratic stabilization. For this, we first form the matrices H ′ 1, H ′ 2 and ¯ N. It is straightforward to see that H ′ 1 has full row rank. We now use Yalmip with Mosek as a solver in order to find matrices D ∈ R 1 × 6, and Φ ∈ S 6, such that Φ > 0 and the LMI holds. Indeed, such matrices exist, and therefore the data are informative for quadratic stabilization. We can find a stabilizing controller by taking C = -D Φ -1, which results in That is, a controller of the form: By definition, this means that the controller C stabilizes all linear systems of the form that are compatible with the measurements. A few trajectories of compatible systems interconnected with the controller are shown in Figure 3. More specifically, the linearization derived earlier is consistent with the measurements, and is therefore stabilized by the found controller. As a last remark, we can interconnect the controller with the discrete-time nonlinear plant. Given that the controller stabilizes the linearization, it locally stabilizes the nonlinear system.

<!-- chunk {"id": "body-0137", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

In this paper, we have given an introduction to the informativity approach to data-driven control. By using a combination of a new viewpoint, classical methods, and novel technical results, we have illustrated the framework by providing a number of solutions to problems with different model classes of linear systems, different types of measurements, and various control objectives. There remain, however, certain limitations to the results. While a number of these limitations yield interesting directions for future research, some of them are inherent to the approach.

<!-- chunk {"id": "body-0138", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

First of all, we have been interested in providing necessary and sufficient conditions for informativity. Of course, such conditions are in a certain sense the gold standard, as they precisely characterize the information contained in the data. On the other hand, it might well be the case that the data contain more information than required. As such, a potentially interesting variant of these problems is to provide condition which are easier to check, but only sufficient. In many cases, such an approach might computationally outperform the methods of this paper. In a similar vein, a number of heuristic methods can drastically outperform the design methods of this paper, albeit without strong theoretical guarantees. In particular, in the case of very small noise samples, the set of consistent systems may be small. In this case, an intuitive method of performing data-driven control is a certainty-equivalent approach: Find any compatible system and solve the control problem for that system.

<!-- chunk {"id": "body-0139", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

The informativity approach has a number of moving parts: The control objective, model class, and noise model. In this paper, we have mainly varied our choice of control objective or analysis problem. In particular, we have focused entirely on model classes consisting of different flavors of linear systems. An extension towards nonlinear systems could improve the applicability of the results. For well-behaved nonlinear systems, we can draw certain conclusions on the basis of the behavior of its linearization. However, a more natural approach would be to investigate informativity problems for certain classes of nonlinear systems directly. Of course, when changing the model class one needs to balance the benefits of more general model classes and the tractability of the resulting robust control problems. Some classes of systems have shown a favorable trade-off in this regard, such as bilinear systems polynomial systems rational systems and systems with quadratic or sector bounded nonlinearities,. As was shown in the aforementioned works, a thorough understanding of the linear case often remains invaluable for the proposal of nonlinear extensions.

<!-- chunk {"id": "body-0140", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

Another problem of interest is changing the way the noise acts on our system and measurements. Measurement noise, that is, noise which acts only on the measurements but not on the system, can be modeled in a similar manner as in this paper. However, an open problem is to provide conditions for data informativity in this setting, because the structure of the set of consistent systems appears to be more complicated than the ones studied here. So far, we are only aware of sufficient conditions for quadratic stabilization with measurement noise [22, Sec. VA] that rely on somewhat conservative bounds.

<!-- chunk {"id": "body-0141", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

The noise models considered in this paper can be applied to treat different scenarios such as energy bounds and sample covariance bounds on the noise. An advantage of these noise models is that the resulting informativity conditions take the form of LMIs with a complexity that is independent of the number of measurements. Clearly, such limited computational complexity is desirable in any control problem. However, the assumption that the noise signal can be described by the solution set of a QMI also comes with certain limitations.

<!-- chunk {"id": "body-0142", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

In particular, with the noise models described in this paper, it is not possible to treat the situation of sample bounds without conservatism. More generally, combining different sets of measurements is a nontrivial problem in this setting, given that the intersection of solution sets of QMIs can generally not be described as the solution set of a single QMI. Without either developing tools that can deal with such intersections or alternative noise models, two important problems are difficult to tackle. First of all, the question of incremental informativity: Does adding more measurements lead to more informative data? Moreover, this lack of scalability inhibits the development of online or adaptive methods as compared to the offline methods of this paper. This motivates the development for new technical results for sample-bounded noise. In [78, Sec. VII] a simple sufficient LMI condition was proposed for quadratic stabilization in the presence of sample-bounded noise, which was further studied. Although this approach appears to be less conservative than describing sample-bounded noise by a QMI, it is not well-understood from a theoretical perspective.

<!-- chunk {"id": "body-0143", "role": "body", "section": "CONCLUSIONS AND DISCUSSION", "weight": 1.0} -->

One of the strengths of methods based on the fundamental lemma (see also the Sidebar 'Willems' fundamental lemma") is the following: For controllable linear systems, we can guarantee that the input-output data have favorable rank properties by injecting inputs that are persistently exciting. The fundamental lemma is thus an experiment design result, that provides a guide for choosing the inputs of the experiment in order to generate informative data (for system identification). It can be shown that the persistency of excitation condition can be replaced by an online design of the inputs, which uses less data samples. An important topic for future work, however, is to develop experiment design methods corresponding to the various problems studied in this paper, especially those for noisy data. Although this is a largely unexplored area of research, we believe that the conditions provided in this paper will form the basis for an experiment design theory. Indeed, to be able to guarantee that the data are informative requires a thorough understanding of informativity in the first place.
