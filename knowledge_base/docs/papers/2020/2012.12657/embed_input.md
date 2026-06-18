Assume/Guarantee Contracts for Dynamical Systems: Theory and Computational Tools

Topics include Linear programming, Autonomous driving, Vehicles, Safety, Control, Contract theory, Dynamical systems theory, Formal verification.

Modern engineering systems include many components of different types and functions. Verifying that these systems satisfy given specifications can be an arduous task, as most formal verification methods are limited to systems of moderate size. Recently, contract theory has been proposed as a modular framework for defining specifications. In this paper, we present a contract theory for discrete-time dynamical control systems relying on assume/guarantee contracts, which prescribe assumptions on the input of the system and guarantees on the output. We then focus on contracts defined by linear constraints, and develop efficient computational tools for verification of satisfaction and refinement based on linear programming. We exemplify these tools in a simulation example, proving a certain safety specification for a two-vehicle autonomous driving setting.

## Introduction

Engineering systems are often comprised of many components having different types and functions, including sensing, control, and actuation. Moreover, systems are subject to many specifications, such as safety and performance. Safety specifications can be captured using the notions of set-invariance (Blanchini and Miani ), while performance specifications are usually defined using a bound on the gain of the system, or using passivity, both can be captured using the framework of dissipativity (Van der Schaft ).

However, modern systems such as intelligent transportation systems, complex robotics and smart manufacturing systems have more complex specifications which cannot be captured by the safety and dissipativity frameworks, e.g. behaviour, tracking, and temporal logic specifications. Formal methods in control have been developed to address this issue (Belta et al.; Tabuada; Wongpiromsarn et al. ). This framework can be used to express temporal logic specifications (Tabuada and Pappas )....

## Conclusions and Future Research

We presented an assume/guarantee contract framework for discrete-time dynamical systems. The framework puts assumptions on the input signal to the system, and prescribes guarantees on the output relative the the input. In particular, as the guarantees do not include the state, systems of different orders can satisfy the same contract. We also defined corresponding fundamental notions such as satisfaction, refinement, and cascaded composition....

Assuming $(A^{1},A^{0},a^{0})$ (or $(G^{1},G^{0},g^{0})$) is extendable is not very restrictive. It is equivalent to assuming that any signal $v{( \cdot )}$ adhering to the assumption, and defined for times $k = {0,\ldots,n}$, can be extended to a signal defined for all times $k \in {\mathbb{N}}$ while satisfying the assumption.

### Proposition 1

### Remark 3.3

In this paper we present a verification approach relying on contract theory. Contract theory was first developed in the field of software engineering as a modular approach to system design (Meyer ), and it has proved useful for design of cyber-physical methods, both in theory and in practice (Nuzzo et al.; Naik and Nuzzo; Phan-Minh et al. ). Contracts prescribe assumptions on the environments a software component can act in, and guarantees on its behaviour in those environments (Benveniste et al. )....
