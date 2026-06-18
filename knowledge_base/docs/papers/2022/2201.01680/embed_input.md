Regret Lower Bounds for Learning Linear Quadratic Gaussian Systems

TWe establish regret lower bounds for adaptively controlling an unknown linear Gaussian system with quadratic costs. We combine ideas from experiment design, estimation theory and a perturbation bound of certain information matrices to derive regret lower bounds exhibiting scaling on the order of magnitude sqrt(T) in the time horizon T. Our bounds accurately capture the role of control-theoretic parameters and we are able to show that systems that are hard to control are also hard to learn to control; when instantiated to state feedback systems we recover the dimensional dependency of earlier work but with improved scaling with system-theoretic constants such as system costs and Gramians. Furthermore, we extend our results to a class of partially observed systems and demonstrate that systems with poor observability structure also are hard to learn to control.

## Introduction

Learning algorithms are set to play an increasing role in modern engineering solutions. Early successes include walking robots and playing repeated games such as Go and are likely to become increasingly important in modern safety-critical infrastructure such as smart grids and intelligent transportation. However, their emergence in safety-critical systems is not without problems. Indeed, one of the hallmarks of these early successes is abundant data from a relatively unchanging source, potentially even through simulation access....

Such an understanding must necessarily be based on two components: *i.* the study of fundamental performance limitations, which no algorithm can excede, and *ii.* the provision of algorithms which match these fundamental limitations. In this work, we focus on the first component and provide an information-theoretic framework for understanding the fundamental limits of adaptive controlling an a priori unknown linear Gaussian system subject to a quadratic cost function....

While the lower bound (LABEL:eq:asymptoticpolb) is interpreted much like its fully observed analogue (LABEL:eq:asymptoticlb) (in particular, see the ensuing discussion), there are two new failure modes that arise. First, as ${\| C_{23}\|}_{\mathsf{o}\mathsf{p}}$ tends to zero, the lower bound (LABEL:eq:asymptoticpolb) diverges. In this case, the learner faces vanishing information available to them about $B_{2}$, which is needed to regulate the system....

It is also interesting to note that it has been proven by Lale et al. that logarithmic regret against the best possible, in hindsight, persistently exciting controller^33^3We refer to Lale et al. for their definition, but this roughly corresponds to having well-conditioned Fisher information. whenever the covariance of the measurement noise is positive definite, i.e., $\Sigma_{V} \succ 0$. Unfortunately, it is not clear whether the optimal LQG controller is persistently exciting under these hypotheses and so the notion of regret in Lale et al. may differ from the standard one....

We next turn our attention to establishing that uninformative state feedback systems satisfy the information-regret-boundedness property.

Fix $\varepsilon > 0$ and let $\mu$ be a smooth and compactly supported prior on $B{(\theta,\varepsilon)}$....
