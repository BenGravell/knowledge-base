<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stabilization with Relaxed Controls

Topics include Stabilization, Relaxed control, Control Lyapunov functions, Nonlinear control, Feedback control, Artstein theorem.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Establishes the relaxed-control stabilization result now associated with Artstein theorem, connecting stabilizability and control-Lyapunov-type conditions to feedback construction. It is a foundational reference behind later universal CLF feedback formulas.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nonlinear systems of the form i = f(x, u) cannot in general be stabilized using a continuous closed loop control U(X), even if each state separately can be driven asymptotically to the origin. (An example is analyzed in Section 2.) In this paper we examine the possibility of stabilizing such systems with a continuous closed loop relaxed control. We find, indeed, that the family of systems stabilizable with relaxed controls is larger than the family of those stabilizable with ordinary controls. An even larger class is obtained if the continuity of the closed loop at the origin is not required. The latter class includes all one dimensional systems for which states can be driven asymptotically to the origin. This result does not hold in two dimensional systems and we provide a counter-example. It should be pointed that relaxed control-type stabilization is used both in theory and in practice; the method is known as dither. We shall comment on the similarities. Lyapunov functions for the system help us in the construction of the continuous closed loop stabilizers.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In fact, we find that the existence of a smooth Lyapunov function is equivalent to the existence of a stabilizing closed loop which is continuous except possibly at the origin; an additional condition on the Lyapunov function implies the continuity at the origin as well. We present these results in Section 4, after a brief introduction of closed loop relaxed controls, notations and terminology in Section 3. Prior to that, in Section 2, we discuss an example illustrating the power of relaxed controls. In the particular case of systems linear in the controls, relaxed controls can be replaced by ordinary controls, this is discussed in Section 5. The role of Lyapunov functions in the stability and stabilization theories is of course well known. Examples of systems with Lyapunov functions are available in the literature. We display some in Section 6, along with general comments on the construction, applications and counterexamples, including one which cannot be continuously stabilized, yet possesses a nonsmooth Lyapunov function.
