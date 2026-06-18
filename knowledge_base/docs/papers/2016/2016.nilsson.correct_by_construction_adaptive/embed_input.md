<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Correct-by-Construction Adaptive Cruise Control: Two Approaches

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motivated by the challenge of developing control software provably meeting specifications for real-world problems, this paper applies formal methods to adaptive cruise control (ACC). Starting from a linear temporal logic specification for ACC, obtained by interpreting relevant ACC standards, we discuss in this paper two different control software synthesis methods. Each method produces a controller that is correct-by-construction, meaning that trajectories of the closed-loop systems provably meet the specification. Both methods rely on fixed-point computations of certain set-valued mappings. However, one of the methods performs these computations on the continuous state space whereas the other method operates on a finite-state abstraction. While controller synthesis is based on a low-dimensional model, each controller is tested on CarSim, an industry-standard vehicle simulator. Our results demonstrate several advantages over classical control design techniques. First, a formal approach to control design removes potential ambiguity in textual specifications by translating them into precise mathematical requirements. Second, because the resulting closed-loop system is known a priori to satisfy the specification, testing can then focus on the validity of the models used in control design and whether the specification captures the intended requirements.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, the set from where the specification (e.g., safety) can be enforced is explicitly computed and thus conditions for passing control to an emergency controller are clearly defined.
