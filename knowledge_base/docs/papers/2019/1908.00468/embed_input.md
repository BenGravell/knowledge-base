Data Informativity: A New Perspective on Data-Driven Analysis and Control

Topics include Data informativity, Data-driven control, Behavioral systems, Persistency of excitation, System analysis, Stabilization, Model uncertainty, Direct control.

Establishes the informativity framework: data are judged by whether all systems consistent with the data satisfy a property or admit a controller, not by whether the data uniquely identify a model. This reframing separates direct data-driven control from system identification and explains when persistency of excitation is stronger than necessary.

The use of persistently exciting data has recently been popularized in the context of data-driven analysis and control. Such data have been used to assess system theoretic properties and to construct control laws, without using a system model. Persistency of excitation is a strong condition that also allows unique identification of the underlying dynamical system from the data within a given model class. In this paper, we develop a new framework in order to work with data that are not necessarily persistently exciting. Within this framework, we investigate necessary and sufficient conditions on the informativity of data for several data-driven analysis and control problems. For certain analysis and design problems, our results reveal that persistency of excitation is not necessary. In fact, in these cases data-driven analysis/control is possible while the combination of (unique) system identification and model-based control is not. For certain other control problems, our results justify the use of persistently exciting data as data-driven control is possible only with data that are informative for system identification.

## Introduction

One of the main paradigms in the field of systems and control is that of *model-based* control. Indeed, many control design techniques rely on a system model, represented by e.g. a state-space system or transfer function. In practice, system models are rarely known a priori and have to be identified from measured data using system identification methods such as prediction error or subspace identification. As a consequence, the use of model-based control techniques inherently leads to a two-step control procedure consisting of system identification followed by control design.

In contrast, *data-driven* control aims to bypass this two-step procedure by constructing controllers directly from data, without (explicitly) identifying a system model. This direct approach is not only attractive from a conceptual point of view but can also be useful in situations where system identification is difficult or even impossible because the data do not give sufficient information.

To address the above question, this paper introduces a general framework to study data informativity problems for data-driven analysis and control.

Inspired by the concept of data informativity in system identification, we introduce a general notion of informativity for data-driven analysis and control.

For each of the studied control problems, we develop methods to compute a controller from data, assuming that the informativity conditions are satisfied.

## Future work

Due to the generality of the introduced framework, many different problems can be studied in a similar fashion: one could consider different types of data, where more results based on only input and output data would be particularly interesting. Many other system-theoretic properties could be considered as well, for example, analyzing passivity or tackling robust control problems based on data.

It would also be of interest to generalize the model class under consideration. One could, for instance, consider larger classes of systems like differential algebraic or polynomial systems. On the other hand, the class under consideration can also be made smaller by prior knowledge of the system. For example, the system might have an observed network structure, or could in general be parametrized.
