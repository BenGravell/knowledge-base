Dissipativity Theory for Nesterov's Accelerated Method

Topics include Semidefinite programming, Lyapunov methods, Control, Lyapunov functions, Ordinary differential equation, Differential equation.

In this paper, we adapt the control theoretic concept of dissipativity theory to provide a natural understanding of Nesterov's accelerated method. Our theory ties rigorous convergence rate analysis to the physically intuitive notion of energy dissipation. Moreover, dissipativity allows one to efficiently construct Lyapunov functions (either numerically or analytically) by solving a small semidefinite program. Using novel supply rate functions, we show how to recover known rate bounds for Nesterov's method and we generalize the approach to certify both linear and sublinear rates in a variety of settings. Finally, we link the continuous-time version of dissipativity to recent works on algorithm analysis that use discretizations of ordinary differential equations.

## Introduction

Nesterov's accelerated method has garnered interest in the machine learning community because of its fast global convergence rate guarantees. The original convergence rate proofs of Nesterov's accelerated method are derived using the method of estimate sequences, which has proven difficult to interpret. This observation motivated a sequence of recent works on new analysis and interpretations of Nesterov's accelerated method.

Many of these recent papers rely on Lyapunov-based stability arguments. Lyapunov theory is an analogue to the principle of minimum energy and brings a physical intuition to convergence behaviors. When applying such proof techniques, one must construct a Lyapunov function, which is a nonnegative function of the algorithm's state (an "internal energy") that decreases along all admissible trajectories. Once a Lyapunov function is found, one can relate the rate of decrease of this internal energy to the rate of convergence of the algorithm. The main challenge in applying Lyapunov's method is finding a suitable Lyapunov function.

In this paper, we developed new notions of dissipativity theory for understanding of Nesterov's accelerated method. Our approach enjoys advantages of both the IQC framework and the discretization approach in the sense that our proposed LMI condition is simple enough for analytical rate analysis of Nesterov's method and can also be easily generalized to more complicated algorithms. Our approach also gives an intuitive interpretation of the convergence behavior of Nesterov's method using an energy dissipation perspective.

One potential application of our dissipativity theory is for the design of accelerated methods that are robust to gradient noise. This is similar to the algorithm design work in Lessard et al.. However, compared with the IQC approach in Lessard et al., our dissipativity theory leads to smaller LMIs. This can be beneficial since smaller LMIs are generally easier to solve analytically. In addition, the IQC approach in Lessard et al. is only applicable to strongly-convex objective functions while our dissipativity theory may facilitate the design of robust algorithm for weakly-convex objective functions....

It is noted in Lessard et al. that searching over combinations of multiple IQCs may yield improved rate bounds. The same is true of supply rates....
