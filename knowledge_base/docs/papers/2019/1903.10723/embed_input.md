A Trajectory-Based Framework for Data-Driven System Analysis and Control

Topics include Data-driven control, Behavioral systems, Trajectory spaces, Persistency of excitation, Data-driven simulation, Nonlinear systems, Kernel methods.

Recasts behavioral trajectory spanning in state-space language and extends the idea toward nonlinear systems that admit linear input-output coordinates. It helps connect classical control intuition, data-driven simulation, and later kernelized or nonlinear fundamental-lemma variants.

The vector space of all input-output trajectories of a discrete-time linear time-invariant (LTI) system is spanned by time-shifts of a single measured trajectory, given that the respective input signal is persistently exciting. This fact, which was proven in the behavioral control framework, shows that a single measured trajectory can capture the full behavior of an LTI system and might therefore be used directly for system analysis and controller design, without explicitly identifying a model. In this paper, we translate the result from the behavioral context to the classical state-space control framework and we extend it to certain classes of nonlinear systems, which are linear in suitable input-output coordinates. Moreover, we show how this extension can be applied to the data-driven simulation problem, where we introduce kernel-methods to obtain a rich set of basis functions.

## Introduction

Finding rigorous and efficient ways to integrate data into control theory has been a problem of great interest for many decades. Since most of the classical contributions in control theory rely on model knowledge, the problem of finding such a model from measured data, i.e., system identification, has become a mature research field. More recently, learning controllers directly from data has received increasing interest, not least due to many successful practical applications of reinforcement learning techniques.

In this paper, we consider an alternative, unitary framework for data-driven control theory, which allows for the development of various system analysis and controller design methods based directly on measured data. This framework relies on the characterization of all trajectories of an unknown system using a single measured data trajectory. The latter problem has been solved in the context of behavioral systems theory for discrete-time linear time-invariant (LTI) systems . In the behavioral approach, a system is not defined via a differential or difference equation with inputs and outputs, but rather as the space of all system trajectories.

The remainder of this paper is structured as follows. In Section III, we phrase the main theorem of, which uses measured data to characterize all system trajectories, in the classical control setting, and we show how this result can be improved by weaving multiple such trajectories together. In Section IV, we provide a novel extension of to classes of nonlinear systems, which are linear in suitably chosen and known nonlinear coordinates. Building on these results, we solve the data-driven simulation problem for such nonlinear systems in Section V. The paper is concluded in Section VI.

## Conclusion

This paper described a purely data-driven framework for system analysis and control. All trajectories of an unknown system can be constructed from a single measured trajectory and thus, this trajectory captures all the required information needed for analysis and controller design, without explicit identification of a model. After describing this result in the classical control framework, we extended it to certain classes of nonlinear systems and we applied this extension to the data-driven simulation problem via kernel methods.
