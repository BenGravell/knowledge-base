LMI Properties and Applications in Systems, Stability, and Control Theory

Topics include Stability analysis, Optimization, Control, Control theory.

Linear matrix inequalities (LMIs) commonly appear in systems, stability, and control applications. Many analysis and synthesis problems in these areas can be solved as feasibility or optimization problems subject to LMI constraints. Although most well-known LMI properties and manipulation tricks, such as the Schur complement and the congruence transformation, can be found in standard references, many useful LMI properties are scattered throughout the literature. The purpose of this document is to collect and organize properties, tricks, and applications related to LMIs from a number of references together in a single document. In this sense, the document can be thought of as an "LMI encyclopedia" or "LMI cookbook." Proofs of the properties presented in this document are not included when they can be found in the cited references in the interest of brevity. Illustrative examples are included whenever necessary to fully explain a certain property. Multiple equivalent forms of LMIs are often presented to give the reader a choice of which form may be best suited for a particular problem at hand....

### Introduction

Linear matrix inequalities (LMIs) commonly appear in systems, stability, and control applications. Many analysis and synthesis problems in these areas can be solved as feasibility or optimization problems subject to LMI constraints. Although most well-known LMI properties and manipulation tricks (e.g., Schur complement, congruence transformation) can be found in standard references, many useful LMI properties are scattered throughout the literature. The purpose of this document is to collect and organize properties, tricks, and applications related to LMIs from a number of references together in a single document....

The document is organized as follows. In the remaining portions of Section 1, the notation used throughout the document is presented and some fundamental LMI properties are discussed. Section 2 features a collection of LMI properties and tricks that are interesting and potentially useful. The LMI properties and tricks in this section are grouped together based on similarities when possible. Applications involving LMIs in systems and stability theory are included in Section 3. Section 4 presents a number of LMI-based optimal controller synthesis methods, while Section 5 includes LMI-based optimal estimation synthesis methods.

### Synthesis Method 5.13

This synthesis method is derived from the discrete-time $\mathcal{H}_{\infty}$-optimal dynamic output feedback controller synthesis method in Synthesis Method 4.11 using the fact that $\mathcal{H}_{\infty}$-optimal filter synthesis is a special case of this problem.

where $a \in {\mathbb{R}}$, $b \in {\mathbb{R}}_{> 0}$, and $a < b$. The following generalized KYP Lemmas give conditions for $\mathcal{G}$ to be inside the cone $\lbrack a,b\rbrack$ within finite frequency bandwidths.

### Proof

Consider the continuous-time LTI system with state-space realization

The authors would like to thank the following individuals for alerting us of errors, and providing useful comments and suggestions for improvement: Leila Bridgeman, Jyot Buch, Manash Chakraborty, Steven Dahdah, William Elke, Robyn Fortune, Peter Seiler.

Please note that this document is a work in progress. If you notice any errors or inaccuracies, or have any suggestions of content that should be included in this document, please email either of the authors at rcaverly@umn.edu or james.richard.forbes@mcgill.ca so...
