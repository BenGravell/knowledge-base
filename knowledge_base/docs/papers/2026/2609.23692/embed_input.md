<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Benefits of Linear Dynamic State Feedback in Co-stabilization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Co-stabilization, i.e., designing a single controller that stabilizes multiple systems, is a fundamental problem in robust and data-driven control. While any stabilizable linear system admits a stabilizing linear static state feedback controller, this equivalence does not extend to co-stabilization. In particular, there exist system collections that cannot be co-stabilized by linear static state feedback but can be co-stabilized using linear dynamic state feedback. In this paper, we study the role of controller memory in co-stabilization. We show that linear dynamic state feedback strictly enlarges the set of co-stabilizable systems compared to static feedback, for both scalar systems and high-dimensional examples. At the same time, we identify structural limitations that cannot be overcome even with dynamic controllers. We also develop a path-integral-based algorithm for computing co-stabilizing controllers for a finite set of systems. Numerical results demonstrate that increasing controller memory enlarges the feasible co-stabilization region. These results highlight controller architecture as a key structural factor in co-stabilization, with potential implications for reducing the sample complexity of learning-based control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning a stabilizing controller is a key step in many learning-based control tasks. Recent works have studied fundamental limits of learning to stabilize from a statistical perspective. In these works, the hardness of the problem is characterized by sample complexity, i.e., the number of samples required to achieve stabilization with high probability. Of particular relevance is, which shows that the hardness of learning to stabilize is governed by two key factors: distinguishability and co-stabilizability of the systems involved. While these principles appear broadly applicable, most existing sample complexity results focus on linear systems under full state observation with linear static state feedback controllers.^11^ 1 While dynamic controllers are used in some learning-based control approaches, the specific benefits of controller memory for stabilization have not been systematically investigated to the best of our knowledge.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by these observations, we focus on the *co-stabilization* problem, i.e., designing a single controller that stabilizes multiple systems. Co-stabilization is a fundamental structural property underlying robustness and learning-based control: the ability to stabilize a larger set of systems directly translates into increased tolerance to model uncertainty.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key fact underlying our work is the following. While any stabilizable fully observed linear system admits a stabilizing linear static state feedback controller, this equivalence does not extend to co-stabilization. In particular, there exist pairs of systems that cannot be co-stabilized by any linear static state feedback controller but can be co-stabilized by a linear dynamic state feedback controller. This observation suggests that controller memory can fundamentally enlarge the class of systems that can be co-stabilized by a single policy. In this paper, we formalize this intuition and develop an algorithm to empirically demonstrate the benefits of dynamic state feedback for co-stabilization. Specifically, our contributions are summarized as follows: First, we prove that the linear dynamic state feedback is more expressive on the co-stabilization problem than the linear static state feedback for some typical examples from the literature. This is achieved by using results from strong stabilization and simultaneous stabilization in robust control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by our theoretical results, we design a co-stabilization path integral algorithm, which iteratively updates linear dynamic state feedback policies, and empirically verify the advantage of linear dynamic state feedback on co-stabilization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. In Section II, we introduce the problem setup. In Section III, we present our main theoretical results. In Section IV, we develop a path-integral-based algorithm for computing co-stabilizing controllers. Section V provides numerical experiments. Finally, Section VI concludes the paper and discusses future directions. All proofs are deferred to the appendix.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We consider the following fully-observed discrete-time linear time-invariant (LTI) system: where $\mathbf{x}_{t}\in\mathbb{R}^{n}$, $\mathbf{u}_{t}\in\mathbb{R}^{m}$ are the state and input at time $t$. For simplicity, we assume $\mathbb{E}[\mathbf{x}_{0}\mathbf{x}_{0}^{\top}]=\mathbf{I}_{n}$. In the remainder of the paper, we denote a system in the form by the pair $(\mathbf{A},\mathbf{B})$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We consider linear dynamic state feedback controllers, represented with a linear time-invariant system of the form: where the parameter matrices $\mathbf{K}\in\mathbb{R}^{m\times n}$, $\mathbf{H}\in\mathbb{R}^{m\times p}$, $\mathbf{G}\in\mathbb{R}^{p\times n}$, $\mathbf{F}\in\mathbb{R}^{p\times p}$, and the state of the controller $\mathbf{z}_{t}\in\mathbb{R}^{p}$, where $p$ is the memory of the controller.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Since a linear static state feedback controller is a special case of a linear dynamic state feedback controller, any task that can be achieved by the former can also be achieved by the latter. On the other hand, when $(\mathbf{A},\mathbf{B})$ is given, it is well known that there exists a controller that stabilizes $(\mathbf{A},\mathbf{B})$ if and only if there exists a linear static state feedback controller that does so (see, e.g., \[9, Theorem 14.5\]). Next, we look at the problem of co-stabilization (also known as simultaneous stabilization ).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Linear Static State Feedback vs. Linear Dynamic State Feedback", "weight": 1.0} -->

Pair with $a_{1}=a_{2}=a,\tfrac{b_{1}}{b_{2}}>\tfrac{a+1}{a-1}$ exp (n)-hard pair from exp (n)-hard pair from TABLE I: Co-Stabilizability Summary (|a1|,|a2| > 1, b > 0) In this section, we compare the co-stabilization capabilities of linear static state feedback and linear dynamic state feedback controllers on scalar systems and $\exp(n)$-hard systems. We show that linear dynamic state feedback controllers are strictly more expressive in certain settings than linear static state feedback controllers.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Scalar Systems", "weight": 1.0} -->

We first consider a class of discrete-time scalar systems. Let where $i\in\{1,2\}$, $x_{t},u_{t}\in\mathbb{R}$, and $b_{i}\neq 0$ for $i=1,2$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Scalar Systems", "weight": 1.0} -->

The following theorem shows that linear dynamic state feedback can strictly enlarge the class of co-stabilizable system pairs compared to linear static state feedback.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B $\\exp(n)$-Hard Systems", "weight": 1.0} -->

This naturally raises the question of whether dynamic state feedback can remove the $\exp(n)$ hardness of learning to stabilize, which was established for static state feedback. Consider the parametrized pair: where $i\in\{3,4\}$ and $n\geq 2$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B $\\exp(n)$-Hard Systems", "weight": 1.0} -->

In the construction of $\exp(n)$-hard systems, co-stabilization by a linear static state feedback controller requires the system parameters to be exponentially close in the state dimension $n$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Co-Stabilization by Path Integral with State-History Feedback", "weight": 1.0} -->

In the previous section, we established that linear dynamic state feedback is strictly more expressive than static feedback for co-stabilization. We now turn to the algorithmic problem of computing such controllers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Co-Stabilization by Path Integral with State-History Feedback", "weight": 1.0} -->

Finding a co-stabilizing controller for a given set of systems is, in general, hard. Existing work based on linear matrix inequalities (LMIs) provides sufficient conditions by requiring a shared Lyapunov function (see, e.g., Section 7.2.3 in ). Policy gradient methods have recently emerged as an alternative to LMIs, sometimes with global or local convergence guarantees. In this section, inspired by the path-integral policy search framework developed, and the stabilization strategy proposed, we propose a path integral algorithm for computing co-stabilizing controllers for a finite set of linear systems.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Co-Stabilization by Path Integral with State-History Feedback", "weight": 1.0} -->

We first present our algorithm for linear static state feedback controllers. Then we will show that based on the reparametrizations, the same algorithm can be used to search for dynamic controllers.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The previous section focuses on the theoretical characterization of co-stabilization of two systems, reflecting the inherent limitations of existing analytical tools in robust control. In contrast, the algorithm developed here is applicable to co-stabilize multiple systems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We now present the co-stabilization path-integral algorithm, summarized in Alg. 1, where $\underline{\sigma}$ denotes the least singular value of a matrix. The inner loop performs a zeroth-order stochastic descent via exponential reweighting of sampled perturbations, which follows the path integral idea. The update of $\alpha_{j}$ follows the stabilization idea. Unstable candidate gains are penalized by assigning a large cost $J_{\max}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 3 (Limits of LMI-based Co-Stabilization with Memory)", "weight": 1.0} -->

Although linear dynamic state feedback and state-history feedback can strictly enlarge the set of co-stabilizable systems, this advantage is not captured by standard LMI-based approaches based on a common quadratic Lyapunov function. In particular, it can be proved that augmenting the system with linear dynamic state feedback or state-history feedback does not enlarge the feasibility region of the corresponding co-stabilization LMI. This highlights a fundamental limitation of LMI-based methods: while dynamic controllers provide additional expressive power for co-stabilization, convex formulations based on common Lyapunov functions fail to exploit this benefit.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct three numerical experiments to validate the theoretical results developed in the previous sections. The first two experiments are to check how Alg. 1 with linear state-history feedback^22^ 2 Empirically, we have not observed a substantial performance difference when using linear dynamic feedback versus linear state-history feedback with our algorithm. Hence, we restrict our experiments to the latter. is affected the controller memory and the original state dimension. The third experiment is to compare Alg. 1 with a co-stabilization policy gradient method from the literature.

<!-- chunk {"id": "body-0023", "role": "body", "section": "V-A Horizon vs. Co-Stabilization Gap", "weight": 1.0} -->

We first investigate how increasing the horizon of a linear state-history controller enlarges the co-stabilization region. Consider the scalar pair in with $a_{1}=a_{2}=1.2$, $b_{1}=1$, and $b_{2}>0$. We apply Alg. 1 to compute a co-stabilizing linear state-history feedback controller for $\{(a_{i},b_{i})\}_{i=1,2}$. For horizon $h$, the systems are lifted according to.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Largest admissible gap", "weight": 1.0} -->

For each horizon $h$, we apply a bisection procedure to determine the largest $\bar{b}_{2}$ such that Alg. 1 remains feasible. Fig. 1 plots $\bar{b}_{2}$ as a function of $h$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Largest admissible gap", "weight": 1.0} -->

The results in Fig. 1 show that in our experiments, the estimated feasible region increases monotonically with horizon. In particular, state-history feedback ($h>1$) achieves a strictly larger $\bar{b}_{2}$ than static state feedback ($h=1$), empirically supporting Theorem 1.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Largest admissible gap", "weight": 1.0} -->

Fig. 1: Largest feasible b2 versus horizon h. In addition, the largest feasible b2 by solving LMI with a common quadratic Lyapunov function is 10.99.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-B Exponential Hardness in System Dimension", "weight": 1.0} -->

We next examine how the co-stabilization gap scales with system dimension. Consider the system in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) with parameters $r=1.2$, $v=0.5$, $b^{}=0$, and $b^{}=\bar{b}>0$. We vary the state dimension $n\in\{2,3,4,5\}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B Exponential Hardness in System Dimension", "weight": 1.0} -->

We compare three approaches: i) LMI-based common quadratic Lyapunov method, which is also employed, ii) linear static state-feedback co-stabilization using Alg. 1 ($h=1$); and iii) linear state-history feedback co-stabilization using Alg. 1 ($h=3$). The hyperparameters of Alg. 1 follow the setup in Section V-A.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B Exponential Hardness in System Dimension", "weight": 1.0} -->

Fig. 2 shows $\bar{m}$ versus $n$. While the chosen $v$ does not satisfy the conditions in Theorem 3-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), all methods exhibit exponential decay of the feasible co-stabilization gap as $n$ increases, suggesting fixed-horizon linear state-history feedback may not remove the $\exp(n)$ hardness identified.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B Exponential Hardness in System Dimension", "weight": 1.0} -->

Fig. 2: Largest feasible b̄ versus system dimension n.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-C Path Integral vs. Policy Gradient", "weight": 1.0} -->

In this part, we compare our Alg. 1 with the co-stabilization policy gradient algorithm given in for linear static state feedback ($h=1$) and linear state-history feedback with $h=3$. We implement the comparison experiment on the co-stabilization of two scalar systems and two single-input order-$2$ systems. The first one is the scalar pair in with $a_{1}=a_{2}=1.2$ and $b_{1},b_{2}$ are uniformly sampled from $$. The second one is the discretized and linearized inverted pendulum system: with known $dt=1e-4$ and $g=10$. For unknown $l$ and $m$, we independently sample two values from uniform distributions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-C Path Integral vs. Policy Gradient", "weight": 1.0} -->

Specifically, for each sample $i=1,2$, we draw $m_{i}\sim\mathcal{U}[0.75,1.25]$ and $\ell_{i}\sim\mathcal{U}[0.75,1.25]$, and define the corresponding linearized inverted pendulum system $(\mathbf{A}_{i},\mathbf{B}_{i})$. The hyperparameters of Alg. 1 follow the setup in Section V-A. The co-stabilization policy gradient algorithm uses the original implementation in the GitHub repository of. For each case, we run $20$ experiments independently to compute the co-stabilization success rates, which are summarized in Table II. Based on the table, we can see that the path-integral method in Alg. 1 is better than the co-stabilization policy gradient, and the controller memory increases the performance of Alg. 1 for the two implemented cases. A limitation of our Alg. 1 is that it is more time-expensive than the co-stabilization policy gradient.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we study the role of controller memory in co-stabilization. We show that linear dynamic state feedback strictly enlarges the class of co-stabilizable systems compared to static feedback, while fundamental limitations remain. On the algorithmic side, we develop a path-integral method for computing co-stabilizing controllers. Future work includes understanding how the controller memory affects the sample complexity of learning-to-stabilize problems. We are also interested in investigating the convergence properties of the proposed path integral algorithm for co-stabilization.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Acknowledgments: This work is supported in part by ONR grant N00014-21-1-2431 (CLEVR-AI). NO would like to thank Constantino Lagoa for some inspiring discussions on co-stabilization.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Some Frequency Domain Preliminary Results", "weight": 1.0} -->

In this section, we introduce some continuous-time frequency domain tools from the book. First, we need to introduce coprime factorization, which plays a critical role in feedback and robust control, followed by two useful lemmas.
