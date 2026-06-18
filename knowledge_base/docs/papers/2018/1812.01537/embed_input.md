A Micro Lie Theory for State Estimation in Robotics

A Lie group is an old mathematical abstract object dating back to the XIX century, when mathematician Sophus Lie laid the foundations of the theory of continuous transformation groups. As it often happens, its usage has spread over diverse areas of science and technology many years later. In robotics, we are recently experiencing an important trend in its usage, at least in the fields of estimation, and particularly in motion estimation for navigation. Yet for a vast majority of roboticians, Lie groups are highly abstract constructions and therefore difficult to understand and to use. This may be due to the fact that most of the literature on Lie theory is written by and for mathematicians and physicists, who might be more used than us to the deep abstractions this theory deals with. In estimation for robotics it is often not necessary to exploit the full capacity of the theory, and therefore an effort of selection of materials is required. In this paper, we will walk through the most basic principles of the Lie theory, with the aim of conveying clear and useful ideas, and leave a significant corpus of the Lie theory behind....

## Introduction

There has been a remarkable effort in the last years in the robotics community to formulate estimation problems properly. This is motivated by an increasing demand for precision, consistency and stability of the solutions. Indeed, proper modeling of the states and measurements, the functions relating them, and their uncertainties, is crucial to achieving these goals. This has led to designs involving what has been known as 'manifolds', which in this context are no less than the smooth topologic surfaces of the Lie groups where the state representations evolve....

Figure 1: Representation of the relation between the Lie group and the Lie algebra. The Lie algebra Tℰ ℳ (red plane) is the tangent space to the Lie group’s manifold ℳ (here represented as a blue sphere) at the identity ℰ. Through the exponential map, each straight path v t through the origin on the Lie algebra produces a path exp (v t) around the manifold which runs along the respective geodesic. Conversely, each element of the group has an equivalent in the Lie algebra....

Finally, we accompany this text with the new C++ library manif implementing the tools described here. manif can be found at The applications in Section V are demonstrated in manif as examples.

Though we do not introduce any new theoretical material, we believe the form in which Lie theory is here exposed will help many researchers enter the field for their future developments. We also believe this alone represents a valuable contribution.

Many examples of this mechanism can be observed in Section III and the appendices. Remark that whenever the function $f$ passes from one manifold to another, the plus and minus operators in (41a) must be selected appropriately: $\oplus$ for the domain $\mathcal{M}$, and $\ominus$ for the codomain or image $\mathcal{N}$.

where the factor 2 accounts for the double effect of the quaternion in the rotation action, x′ = q x q*. With this choice of Hat and Vee, the quaternion exponential

which is defined with (41a). The right Jacobian maps variations of the argument $\mathbf{τ}$ into variations in the *local* tangent space at $\operatorname{Exp}{({\mathbf{τ}})}$. From (41a) it is easy to prove that, for small $\delta{\mathbf{τ}}$, the following approximations hold,
