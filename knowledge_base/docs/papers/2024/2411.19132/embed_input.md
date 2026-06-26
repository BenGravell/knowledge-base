<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conformal Prediction for Distribution-free Optimal Control of Linear Stochastic Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We address an optimal control problem for linear stochastic systems with unknown noise distributions and joint chance constraints using conformal prediction. Our approach involves designing a feedback controller to maintain an error system within a prediction region (PR). We define PRs as sublevel sets of a nonconformity score over error trajectories, enabling the handling of joint chance constraints. We propose two methods to design feedback control and PRs: one through direct optimization over error trajectory samples, and the other indirectly using the S-procedure with a disturbance ellipsoid obtained from data. By tightening constraints with PRs, we solve a relaxed problem to synthesize a feedback policy. Our method ensures reliable probabilistic guarantees based on marginal coverage, independent of data size.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

P ROBABILISTIC guarantees play a crucial role in many applications that involve stochastic disturbances and safety. As chance-constrained problems are generally nonconvex and computationally intractable, most approaches solve deterministic relaxations by applying constraint-tightening techniques based on available information about uncertainty. Constraint tightening for probabilistic satisfaction has been studied when the underlying probability distribution is known, in cases of bounded disturbances, or using probabilistic reachable sets -. These approaches may be restricted to Gaussian settings, involve computationally costly operations, or often rely on the multivariate Chebyshev inequality, which can lead to conservative bounds. In contrast, sampling-based methods such as - can be significantly more flexible in relaxing chance-constrained problems by utilizing available disturbance samples, termed scenarios, and can provide formal guarantees based on scenario optimization (SO),.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This work was supported by the Swedish Research Council (VR), the Knut & Alice Wallenberg Foundation (KAW), the Horizon Europe Grant SymAware and the ERC Consolidator Grant LEAFHOUND.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

E.E. Vlahakis and D.V. Dimarogonas are with the Division of Decision and Control Systems, School of Electrical Engineering and Computer Science, KTH Royal Institute of Technology, 10044, Stockholm, Sweden. Email: { vlahakis,dimos } @kth.se. L. Lindemann is with the Thomas Lord Department of Computer Science and the Ming Hsieh Department of Electrical and Computer Engineering, Viterbi School of Engineering, University of Southern California, Los Angeles, 90089, CA, USA. Email: llindema@usc.edu. P. Sopasakis is with the School of Electronics, Electrical Engineering and Computer Science, Queen's University Belfast, Northern Ireland, UK. Email: p.sopasakis@qub.ac.uk An alternative distribution-free framework for streamlined uncertainty quantification, equipped with formal guarantees, is provided by conformal prediction (CP). Originally introduced by Vovk and Shafer CP uses a calibration dataset to infer prediction regions for a test dataset with a specified probability, while remaining distribution-agnostic.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

CP has been applied in machine learning, chance-constrained optimization, and control for safety verification and planning -, see for a recent survey.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Leveraging its distribution independence, we apply CP to tackle an optimal control problem for linear stochastic systems under joint chance constraints, assuming data-driven noise information. Our approach is closely related to which employ offline sampling for constraint tightening and probabilistic reachable set computation. Both methods assume a fixed feedback control policy, which preserves convexity in the underlying scenario-based relaxed programs, as required by SO, to enable solutions with a priori guarantees. Disturbance feedback parameterization is employed in for online SO-based stochastic optimal control, which maintains convexity and is well-suited for short control horizons. In our approach, we design a feedback controller using disturbance samples to ensure the error system remains within a prediction region (PR). Although state-feedback control introduces a nonlinear dependence of dynamics on the feedback gain, we can derive formal guarantees through a twostep training-calibration procedure provided by CP. We define PRs as sublevel sets of nonconformity scores, with thresholds based on empirical quantiles computed from data. To handle joint chance constraints, we introduce nonconformity scores capturing the maximum error across a trajectory. We propose two methods.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In the first, we use a training dataset to optimize nonconformity score quantiles for controller design, followed by PR construction via CP on a calibration dataset. In the second method, we first obtain a disturbance PR via CP, and subsequently use the S -procedure to design a PR and a feedback gain for the error system. The PRs are used to tighten the constraints, enabling us to solve a deterministic relaxation problem that yields a feedback control policy with probabilistic guarantees. We demonstrate the performance of both methods through a numerical example and compare our approach with the SO-based randomized method.

<!-- chunk {"id": "body-0009", "role": "body", "section": "MAIN RESULTS", "weight": 1.0} -->

Due to linearity in (3b), the state x (t) can be decomposed into a deterministic part, z (t), and an error, e (t), i.e., x (t) = z (t) + e (t). We will tackle the stochastic control problem in - by the control law u (t) = Ke (t) + v (t), where K ∈ I R m × n is a state-feedback gain for the pair (A,B), and v (t) is a feedforward control action. Then, we may write where z = x, e = 0, and ¯ A = A + BK. This standard decomposition technique allows the two systems in to be analyzed independently. Unlike existing approaches that assume a fixed feedback controller we aim to design both feedback and feedforward control terms using the available disturbance dataset D w.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MAIN RESULTS", "weight": 1.0} -->

We partition D w into training and calibration datasets, D w train = { w (k 1 +1),..., w (k) } and D w cal = { w,..., w (k 1) }, where k 1 + 1 < k. The training dataset is used to compute design parameters, such as K, while the calibration dataset is used to generate empirical distributions of nonconformity scores defined over error and input trajectories. Using Lemma 1, we then derive prediction regions for the error state e (t) and the feedback term Ke (t), with formal guarantees. Next, we define prediction regions for random vectors, and subsequently, show how to solve a relaxation of the problem in optimizing over control actions, given a fixed feedback gain K.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Definition 1 Let ξ ∈ I R n be a random vector. We call E 1 -θ ( ξ ) ⊆ I R n a prediction region (PR) for ξ at a confidence level 1 -θ, if Pr { ξ ∈ E 1 -θ ( ξ ) } ≥ 1 -θ. We also denote E a: b 1 -θ ( ξ ( t )) a prediction region for the random process ( ξ ( a ),..., ξ ( b )), if Pr { ξ ( t ) ∈ E a: b 1 -θ ( ξ ( t )) ∀ t ∈ I N [ a,b ] } ≥ 1 -θ.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Given PRs E 1: N 1 -θ ( e ( t )), E 0: N -1 1 -θ ( Ke ( t )), we can tighten the constraints in to produce constraints for the deterministic variables z ( t ), v ( t ), in (5a). Conditions for tightening of the constraints in are given next.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Lemma 2 Consider the ellipsoidal constraints, and the error system in (5b). Let E 1: N 1 -θ (e (t)) and E 0: N -1 1 -θ (Ke (t)) be prediction regions for (e,..., e (N)) and (Ke,..., Ke (N -1)), respectively. If E 1: N 1 -θ (e (t)) ⊆ B (C e) and E 0: N -1 1 -θ (Ke (t)) ⊆ B (C u), with C e ∈ (0, 1 / √ λ max (P t)), ∀ t ∈ I N [1,N], and C u ∈ (0, 1 / √ λ max (Q)), respectively, then Proof: Define c min = min t 1 / √ λ max (P t). For the condition in (6a), it suffices to show that int(ˆ X t ⊖ B (C e)) = ∅, ∀ t ∈ I N [1,N], where ˆ X t = X t -p t.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Note that ˆ X t ∋ 0 is an ellipsoid, with the length of its smallest semi-axis equal to 1 / √ λ max (P t). Thus, B (c min) ⊆ ˆ X t, ∀ t ∈ I N [1,N]. Moreover, since C e ∈ (0, c min), we have B (c min) ⊖ B (C e) = B (c min -C e) ⊆ ˆ X t ⊖ B (C e), ∀ t ∈ I N [1,N]. Taking the interior on both sides of this inclusion, the result follows, i.e., int(B (c min -C e)) ⊆ int(ˆ X t ⊖ B (C e)) = ∅, since int(B (c min -C e)) = ∅. The condition in (6b) is proved similarly.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

We now present a relaxation of the problem in with tighter state and input constraints based on PRs for a fixed K similar to the approaches.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Theorem 1 Consider the optimization problem in -, the system in with PRs, E 1: N 1 -θ (e (t)) ⊊ I R n, E 0: N -1 1 -θ (Ke (t)) ⊊ I R m, for a fixed gain K, and where Z t = X t ⊖ E 1: N 1 -θ (e (t)), t ∈ I N [1,N], and V = U ⊖ E 0: N -1 1 -θ (Ke (t)). Assume that the conditions in are true, and that is feasible for z = x 0, with an optimal solution (v ∗ (0: N -1), z ∗ (1: N)). Let u (0: N -1) = (u,..., u (N -1)), with u (t) = Ke ∗ (t) + v ∗ (t), where e ∗ (t) = x (t) -z ∗ (t), t ∈ I N [0,N -1], and x (t) is the state of the system (3b).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Let the trajectory of (3b), x (1: N), originated at x 0 be driven by input and disturbance sequences, u (0: N -1), w (0: N -1), where individual disturbances follow the same distribution as the elements of D w cal. Then, (u (0: N -1), x (1: N)) is a feasible solution to.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Proof: Since the conditions in are true, it suffices to show that the probabilistic constraints in (3c)-(3d) are feasible.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

Define events X:= x ( t ) ∈ X t ∀ t ∈ I N [1,N ], E:= e ( t ) ∈ E 1: N 1 -θ ( e ( t )) ∀ t ∈ I N [1,N ], and Z:= z ( t ) ∈ Z t ∀ t ∈ I N [1,N ], and let ˆ E be the complement of E. Since is feasible by assumption, Pr { Z } = 1, implying that Pr { X | E } = 1, by definition of Z t = X t ⊖ E 1: N 1 -θ ( e ( t )). From the law of total probability, we have Pr { X } = Pr { X | E } Pr { E } +Pr { X | ˆ E } Pr { ˆ E } ≥ 1 -θ, which follows from the fact that Pr { X | E } = 1, Pr { E } ≥ 1 -θ, and Pr { X | ˆ E } Pr { ˆ E } ≥ 0. The constraint in (3d) can be shown by similar reasoning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Open-loop control", "weight": 1.0} -->

We note that the conditions in of Lemma 2 ensure that is well defined. Theorem 1 can be stated independently. We also remark that the input u ( t ) = Ke ( t ) + v ( t ) may be unbounded as e ( t ) is influenced by a stochastic, potentially unbounded, disturbance. The chance constraint in (3d) allows the input constraint to be violated for some disturbance realizations, with the parameter θ specifying the extent of such violations. Next, we design PRs that bound the feedback term Ke ( t ) with a probability of at least 1 -θ.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Assuming that PRs for the error system in (5b) with a fixed state-feedback gain K are available, Theorem 1 provides a method to construct a feasible solution for the problem in - by solving a tractable optimization problem. Here, we outline two methods for designing K and approximate PRs for the error system. The first method formulates an optimization problem over a training dataset of error trajectories, where each trajectory sample depends nonlinearly on K. After solving this, conformal prediction is applied on a calibration dataset to compute PRs, referred to as the direct method, as CP is applied directly to error trajectories. The second method uses conformal prediction on disturbance samples to identify an ellipsoidal set that bounds disturbance sequences with the specified probability. The S -procedure is then used to compute an admissible state-feedback gain and an ellipsoidal PR. This is called the indirect method, as CP is applied to disturbance samples to indirectly infer coverage for the error system's PRs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

1) Direct method: From the available disturbance dataset w D, we define a trajectory dataset as In the following, we partition D e into D e train and D e cal, where trajectory samples in D e train are constructed by disturbance samples in D w train and are parameterized by the feedback gain K, while trajectory samples in D e cal are constructed by disturbance samples in D w cal for a fixed K. We also introduce the nonconformity scores which will help us identify PRs for the random processes (e,..., e (N)) and (Ke,..., Ke (N -1)), as Euclidean balls bounding ‖ e (t) ‖ and ‖ Ke (t) ‖ uniformly for all t ∈ N [0,N], enabling efficient tightening of the ellipsoids.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Consider now the optimization problem where the objective is to obtain a state-feedback gain K and minimal PRs E 1: N 1 -θ (e (t)), E 0: N -1 1 -θ (Ke (t)) induced by the constraints in (10b)-(10c), and the nonconformity scores R (j) e, R (j) u. The objective in (10a) balances the trade-off between minimizing the error cost η e and the feedback control cost η u, as indicated by the nonconformity scores R e and R u. A specific value for the tuning parameter γ, which leads to a cost function that supports the desired performance while adhering to state and input constraints, is recommended later.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

At first glance, one might consider using Lemma 1 to replace the probabilistic constraints in (10b)-(10c) with constraints as, that is, Quantile({R e,..., R (k 1) e, ∞}, 1 -θ) ≤ η e, and Quantile({R u,..., R (k 1) u, ∞}, 1 -θ) ≤ η u, by constructing empirical nonconformity scores R (j) e and R (j) u using the available calibration dataset D e cal. However, this is not straightforward because the random variables R e,..., R (k 1) e and R u,..., R (k 1) u do not retain the i.i.d property, as they depend on the decision variable K. Instead, we can first obtain a state-feedback gain K using a separate training dataset D e train and subsequently apply conformal prediction to attain coverage guarantees for the constraints in (10b)-(10c) by computing a calibration dataset D e cal for the obtained gain K. This approach is shown next.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Let D e train = { e (k 1 +1),..., e (k) }, where e (j) is a trajectory sample parameterized over state-feedback gains K ∈ I R m × n and driven by a training disturbance sequence w (j) ∈ D w train, with j ∈ I N [k 1 +1,k]. Then, we formulate the problem of finding a state-feedback gain K by solving where η max e = min t ∈ I N [1,N] (1 / √ λ max (P t)), η max u = 1 / √ λ max (Q), R (j) e (K) (R (j) u (K)) denotes the parameterization over the feedback gain K, and we choose γ = η max e η max u, and ˆ θ = (1 + 1 k -k 1 -1)(1 -θ). Note that ∞ is omitted from the empirical distributions in (11b)-(11c) and 1 -θ is replaced by (1 + 1 k -k 1 -1)(1 -θ) (see [19, Sec. 2.1] for details).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Solving is indeed difficult due to the nonlinear dependence of the constraints in (11b)-(11c) on the decision variable K. One can employ a nonlinear solver to obtain a feasible solution to. See, e.g., Sec. IV, where we employ a genetic algorithm to solve for an academic example.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Next, given a state-feedback gain K obtained, we can provide PRs, E 1: N 1 -θ ( e ( t )), E 0: N -1 1 -θ ( Ke ( t )), via conformal prediction using empirical distributions of the nonconformity scores in generated by constructing the calibration dataset D e cal. This is formally stated next.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Lemma 3 Construct the calibration trajectory dataset D e cal as, using the calibration disturbance set D w cal and the solution K. Let {R e,..., R (k 1) e }, {R u,..., R (k 1) u } be the empirical distributions in (9a), (9b), respectively, computed by the samples in D e cal and the gain K. Compute C e = Quantile({R e,..., R (k 1) e, ∞}, 1 -θ) and C Ke = Quantile({R u,..., R (k 1) u, ∞}, 1 -θ). Then, if E 1: N 1 -θ (e (t)):= B (C e), E 0: N -1 1 -θ (Ke (t)):= B (C Ke), we have Proof: First we prove that D e cal consists of k 1 +1 i.i.d. random trajectories of (5b).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

For each fixed t ∈ I N [1,N], the random vector e (j) (t) in (8c) is identically distributed across all j ∈ I N [0,k 1]. This means that for any fixed time index t, the distribution of e (j) (t) does not depend on the index j for a given K. Therefore, since the distribution of each individual e (j) (t) is the same for all j, it follows that the entire random process e (j) (1: N) in (8b) is identically distributed across j ∈ I N [0,k 1]. By the independence of w (j) across all j ∈ I N [0,k 1], e (j) (1: N), j ∈ I N [0,k 1], are i.i.d. random processes, implying that R e,..., R (k 1) e are k 1 +1 i.i.d random variables.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Thus, by Lemma 1, we obtain the coverage Pr {R e ≤ C e } ≥ 1 -θ, which can be written as Pr { max(‖ e ‖,..., ‖ e (N) ‖) ≤ C e } ≥ 1 -θ by (9a), or as Pr { e ∈ B (C e) ∧ · · · ∧ e (N) ∈ B (C e) } ≥ 1 -θ, leading to (12a). The proof of (12b) follows identical lines.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

We summarize important remarks for selecting the nonconformity scores in as follows: 1) The PRs obtained in Lemma 3 give marginal guarantees, that is, the probabilities in are averaged over the randomness of both the training and calibration data. 2) The ball B (‖ K ‖ C e) is a conservative PR, i.e., E 0: N -1 1 -θ (Ke (t)), motivating the use of two nonconformity scores. 3) We can select ∞ -norm-based nonconformity scores to infer box-shaped PRs when more appropriate, e.g., for polyhedral constraints. 2) Indirect method: First, we compute an ellipsoid containing all the training disturbance samples in D w train by solving the optimization Note that is a convex problem [23, Sec. 8.4], with ˆ Y being a symmetric positive definite matrix.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Also, the volume of ˆ W = { w | ‖ ˆ Y w ‖ ≤ 1 } is minimum since it is proportional to det ˆ Y by ˆ Y ≻ 0. Next, we obtain an ellipsoidal prediction region E 0: N -1 1 -θ (w (t)). Consider the nonconformity score over the calibration dataset D w cal. Then, by Lemma 1, we obtain Pr {R w ≤ C w } ≥ 1 -θ, which implies that Pr {‖ ˆ Y w (t) ‖ ≤ C w ∀ t ∈ I N [0,N -1] } ≥ 1 -θ, i.e., the ellipsoid is a PR, E 0: N -1 1 -θ (w (t)), where Y = ˆ Y ⊤ ˆ Y /C 2 w. Thus, the feedback design problem can be reduced to the synthesis of an ellipsoidal region for the error system (5b) that is robustly controlled invariant [24, Def.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

2.3] by a feedback controller K for all disturbances lying in W. In other words, we seek where Φ ≻ 0 is a symmetric positive definite matrix, and a state-feedback gain K, such that which ensures that E in is invariant for all disturbance sequences in W, thereby serving as a PR. By S -procedure [23, Appendix B.2], and the fact that Φ ≻ 0 and Y ≻ 0 [25, Theorem 4.2], the invariance condition in can be translated into finding a feasible solution to the BMI: where ¯ A = A + BK. By applying Schur complement twice and noting that λ 1 Y -Φ ≻ 0 is equivalent to Φ -1 -1 / λ 1 Y -1 ≻ 0, (19a) can be enforced by requiring which is linear in ˆ Φ and Ψ, where ˆ Φ = Φ -1 and Ψ = K ˆ Φ.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

To ensure that K = Ψ ˆ Φ -1 is an admissible linear controller, we also require that max e ⊤ Φ e ≤ 1 ‖ Q 1 / 2 Ke ‖ < 1, which, by using the state-space transformation ˆ e = Φ 1 / 2 e, is written as We are now ready to state the following result.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Theorem 2 Consider the ellipsoid W as defined in such that Pr { w (t) ∈ W ∀ t ∈ I N [0,N -1] } ≥ 1 -θ. Let ˆ Φ ∗, Ψ ∗, λ ∗ 0, λ ∗ 1 be a feasible solution to the following program: and define Φ = (ˆ Φ ∗) -1. Consider the error system in (5b), with K = Ψ ∗ Φ, and the ellipsoidal regions, and define E = { e | e ⊤ Φ e ≤ 1 }. Then, i) Pr { e (t) ∈ E ∀ t ∈ I N [1,N] } ≥ 1 -θ, ii) int(X t ⊖E) = ∅ ∀ t ∈ I N [1,N], iii) int(U ⊖ E u) = ∅, where E u = { u = Ke | e ∈ E}.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Proof: i) By the feasibility of, the ellipsoid E is robustly invariant for (5b) for all w (t) ∈ W when K = Ψ ∗ Φ, that is e (t) ∈ E for all w (t) ∈ W. Since Pr { w (t) ∈ W ∀ t ∈ I N [0,N -1] } ≥ 1 -θ, one can deduce that Pr { e (t) ∈ E ∀ t ∈ I N [1,N] } ≥ 1 -θ. ii) Without loss of generality, assume that X t Note that the optimization in is convex for any fixed pair (λ 0, λ 1) and thus can be solved using a grid search over (λ 0, λ 1). It also minimizes an upper bound on det ˆ Φ, as shown by det ˆ Φ ≤ (1 n trace ˆ Φ) n. is centered at the origin. By the feasibility of the constraints in (22b), we have that Φ ≻ P t, for t ∈ I N [1,N], which implies that E ⊊ int(X t), ∀ t ∈ I N [1,N].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Prediction regions and feedback control", "weight": 1.0} -->

Then, it follows that int(X t ⊖E) = ∅. iii) Similarly, by the feasibility of the LMI, it follows that E u ⊊ int(U), which implies that int(U ⊖ E u) = ∅.

<!-- chunk {"id": "body-0038", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

We consider the problem in - for a discrete-time double integrator system, with a horizon of N = 100 time steps, cost functions ℓ ( x ( t ), u ( t )) = ( u ( t )) 2, V f ( x ) = 100 x ⊤ x, failure probability θ = 0. 05, A = [ 1 0. 5 0 1 ], B = [ 0 0. 5 ], and initial condition x = (2, -1). For the constraints in (3c)-(3d), we select P t = I 2 1 / 10, p t = 0, for t ∈ I N [1,N ], and Q = 1. For the unknown vector w ( t ) = ( w 1 ( t ), w 2 ( t )), we generate calibration and training disturbance datasets, D w train and D w cal, each with 100 sequence samples. We sample w 1 ( t ) from N ( -0. 01, 0. 005), and w 2 ( t ) from a gamma distribution with shape 5.5 and scale 0.005, each multiplied equally likely by 1 or -1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

Indirect method: We construct an ellipsoid ˆ W that confines all training disturbance samples in D w train by solving the problem. Then, using the nonconformity score from and computing the empirical quantile from over the calibration dataset D w cal we obtain a tighter ellipsoid W ⊆ ˆ W, defined in with Y = [ 12. 6733 -1. 0720 -1. 0720 114. 7949 ], which is a PR, E 0: N -1 1 -θ ( w ( t )), by Lemma 3. For the obtained PR, W, we construct a feedback gain K ind = [ -1. 4140 -2. 3412 ], and the ellipsoid E = { e | e ⊤ Φ e ≤ 1 }, with Φ = [ 3. 4644 3. 8069 3. 8069 5. 6494 ], by solving. The problem was formulated in YALMIP and solved using the SDP solver SEDUMI, with a grid search over 210 pairs ( λ 0, λ 1 ), within 37 seconds.

<!-- chunk {"id": "body-0040", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

Direct method: We formulate the problem, where γ = η max e / η max u, with η max e = √ 10, η max u = 1, and the constraints in (11b)-(11c) are constructed using the training dataset D w train. To solve this problem we employ a genetic algorithm (GA), with a population size of 150 candidates for 50 generations. The GA returns K dir = [ -0. 241 -0. 787 ] within 5 minutes. Next, we obtain PRs, E 1: N 0. 95 ( e ( t )), E 0: N -1 0. 95 ( Ke ( t )), by constructing a calibration trajectory dataset D e cal by the disturbance dataset D w cal as in for the obtained K dir. Following Lemma 3, we obtain E 1: N 1 -θ ( e ( t )) = B (0. 5785) (see blue dashed circle in Fig. 1 (left)) and E 0: N -1 1 -θ ( Ke ( t )) = B (0. 1271), which verify the conditions in of Lemma 2.

<!-- chunk {"id": "body-0041", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

We use the PRs, E 1: N 1 -θ ( e ( t )) and E 0: N -1 1 -θ ( Ke ( t )), from the direct and indirect methods to tighten the constraints in (3c)(3d) and solve the deterministic problem. The average solve time for the problem in on a laptop with an Intel i7-1185G7 processor and 32 GB of RAM is less than 0.02 seconds using the MOSEK solver in YALMIP. Using the resulting solutions, we test constraint satisfaction for 10 4 new disturbance realizations. For the direct method, state and input constraints are satisfied with frequencies of 99. 11% and 100%, meeting the specified probability. For the indirect method, state and input constraints are satisfied for all sampled disturbances. Noisy trajectories are illustrated for both methods in Fig. 1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

Fig. 1: Direct method (left), Indirect method (right): Representation of the original state constraint X t (solid black), the tighter state constraint Z t = X t ⊖ E 1: N 0. 95 ( e ( t )) (dashed black), the PR E 1: N 0. 95 ( e ( t )) (dashed blue), 100 sample trajectories x ( j ) (0: N ) (light red), and the deterministic trajectory z (0: N ) (red), with initial condition x (red cross).

<!-- chunk {"id": "body-0043", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

The conservatism of the indirect method is expected, as the dashed blue ellipsoid in Fig. 1 (right) is a PR for the error state e ( t ) for all t > 0 and any disturbance within E 0. 95 ( w ( t )). In contrast, the direct method synthesizes a gain K dir from available training disturbance sequences. The merit of our approach is that the two methods can be used independently or in combination. With long horizons, it may be advantageous to collect disturbance samples and solve the problem, followed by determining PRs using Lemma 3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "EXAMPLE", "weight": 1.0} -->

Comparison with SO: We evaluate our method's efficiency against the randomized approach, which uses disturbance feedback parameterization to maintain a convex scenario-based relaxation. By enforcing a timeinvariant feedback structure (see [7, Sec. III]), we generate scenarios for the constraints in (3b)-(3d) and solve the scenario optimization with 100 scenarios within 1.5 minutes using the MOSEK solver. However, achieving the specified probabilistic constraints, e.g., with confidence level β = 10 -3 requires at least 5,739 scenarios by [7, Theorem 1] and [9, Theorem 1], which demands computational time exceeding one hour using our software. In contrast, our synthesis approach in or does not impose a minimum number of training scenarios. The desired confidence can be achieved offline through calibration by Lemma 3 for any number of scenarios. Notably, calibration for 5,739 scenarios can be completed within 4 seconds on our computer. The software used in this section is.

<!-- chunk {"id": "body-0045", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have addressed an optimal control problem for linear stochastic systems with unknown distributions using conformal prediction. We propose two methods to design a feedback controller from data that keeps the error state within a prediction region. We provide guarantees independent of data size through a two-step training-calibration process. In future work, we will extend this approach to a stochastic model predictive control setting, exploring closed-loop properties.
