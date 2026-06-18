Data-Efficient Design Exploration through Surrogate-Assisted Illumination

Topics include Optimization, Surrogate-assisted illumination, SAIL, Surrogate model.

Design optimization techniques are often used at the beginning of the design process to explore the space of possible designs. In these domains illumination algorithms, such as MAP-Elites, are promising alternatives to classic optimization algorithms because they produce diverse, high-quality solutions in a single run, instead of only a single near-optimal solution. Unfortunately, these algorithms currently require a large number of function evaluations, limiting their applicability. In this article we introduce a new illumination algorithm, Surrogate-Assisted Illumination (SAIL), that leverages surrogate modeling techniques to create a map of the design space according to user-defined features while minimizing the number of fitness evaluations. On a 2-dimensional airfoil optimization problem SAIL produces hundreds of diverse but high-performing designs with several orders of magnitude fewer evaluations than MAP-Elites or CMA-ES. We demonstrate that SAIL is also capable of producing maps of high-performing designs in realistic 3-dimensional aerodynamic tasks with an accurate flow simulation.

## Introduction

Creators of design optimization techniques often think of their algorithms as a finalizing step in the design process. Imagining that their techniques will be used to push the limits of performance, they judge success by the ability of an algorithm to refine a design to its most optimal form, with the ultimate goal of outperforming the best engineers.

If, however, the goal of these algorithms is to support designers in discovering the best possible designs, the emphasis on optimal performance may be misplaced. In an interview study by Autodesk, it was found that computational design tools most common use was not at the end of the design process to hone existing designs. Instead the engineers, designers, and architects interviewed reported that they more commonly used optimization tools at the beginning of the design process to explore the space of possible designs.

In computationally expensive problems it is common to use surrogate models, that is, approximate models of the objective function based on previously evaluated solutions. These models are refined through iterative evaluation of new solutions based on an *acquisition function*, which balances exploitation and exploration to improve accuracy in high-fitness regions. By substituting expensive objective functions with these computationally efficient approximations, the optimization process can be greatly accelerated.

In this article, we present the Surrogate-Assisted Illumination (SAIL) algorithm to improve the efficiency, and so expand the applicability, of MAP-Elites.

## Discussion

The SAIL algorithm produces a model of the objective function in high-fitness regions across the feature space, even with a limited computational budget. With the aid of these models, illumination algorithms can produce a diversity of high-performing designs which reveal relationships between features as well as biases in encodings.

Our experiments have shown that SAIL is effective without a carefully tuned domain specific encoding, which opens up the possibility of using it as a tool to assist in the creation and tuning of new encodings. Whether testing the capabilities of a newly designed representation, or iteratively improving an existing encoding, SAIL provides a way of understanding the inherent biases of a representation.
