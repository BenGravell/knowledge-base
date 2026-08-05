<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DDPNOpt: Differential Dynamic Programming Neural Optimizer

Topics include Optimal control, Trajectory optimization, Neural networks, Attention mechanisms, Online algorithms, Optimization, Control, DDPNOpt, Differential dynamic programming, Dynamic programming.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interpretation of Deep Neural Networks (DNNs) training as an optimal control problem with nonlinear dynamical systems has received considerable attention recently, yet the algorithmic development remains relatively limited. In this work, we make an attempt along this line by reformulating the training procedure from the trajectory optimization perspective. We first show that most widely-used algorithms for training DNNs can be linked to the Differential Dynamic Programming (DDP), a celebrated second-order method rooted in the Approximate Dynamic Programming. In this vein, we propose a new class of optimizer, DDP Neural Optimizer (DDPNOpt), for training feedforward and convolution networks. DDPNOpt features layer-wise feedback policies which improve convergence and reduce sensitivity to hyper-parameter over existing methods. It outperforms other optimal-control inspired training methods in both convergence and complexity, and is competitive against state-of-the-art first and second order methods. We also observe DDPNOpt has surprising benefit in preventing gradient vanishing. Our work opens up new avenues for principled algorithmic design built upon the optimal control theory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we consider the following optimal control problem (OCP) in the discrete-time setting: where x t ∈ R n and u t ∈ R m represent the state and control at each time step t. f t (·, ·), ℓ t (·, ·) and φ (·) respectively denote the nonlinear dynamics, intermediate cost and terminal cost functions. OCP aims to find a control trajectory, ¯ u ≜ { u t } T -1 t =0, such that the accumulated cost J over the finite horizon t ∈ { 0, 1, · · ·, T } is minimized. Problems with the form of OCP appear in multidisciplinary areas since it describes a generic multi-stage decision making problem, and have gained commensurate interest recently in deep learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Central to the research along this line is the interpretation of DNNs as discrete-time nonlinear dynamical systems, where each layer is viewed as a distinct time step. The dynamical system perspective provides a mathematically-sound explanation for existing DNN models. It also leads to new architectures inspired by numerical differential equations and physics. In this vein, one may interpret the training as the parameter identification (PI) of nonlinear dynamics. However, PI typically involves (i) searching time-independent parameters (ii) given trajectory measurements at each time step. Neither setup holds in piratical DNNs training, which instead optimizes time- ( i.e. layer-) varying parameters given the target measurements only at the final stage.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An alternative perspective, which often leads to a richer analysis, is to recast network weights as control variables. Through this lens, OCP describes w.l.o.g. the training objective composed of layerwise loss ( e.g. weight decay) and terminal loss ( e.g. cross-entropy). This perspective (see Table 1) has been explored recently to provide theoretical statements for convergence and generalization. On the algorithmic side, while OCP has motivated new architectures and methods for breaking sequential computation, OCP-inspired optimizers remain relatively limited, often restricted to either specific network class ( e.g. discrete weight) or small-size dataset.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The aforementioned works are primarily inspired by the Pontryagin Maximum Principle (PMP, Boltyanskii et al. ), which characterizes the first-order optimality conditions to OCP. Another parallel methodology which receives little attention is the Approximate Dynamic Programming (ADP, Bertsekas et al. ). Despite both originate from the optimal control theory, ADP differs from PMP in that at each time step a locally optimal feedback policy (as a function of state x t ) is computed. These policies, as opposed to the vector update from PMP, are known to enhance the numerical stability of the optimization process when models admit chain structures ( e.g. in DNNs). Practical ADP algorithms such as the Differential Dynamic Programming (DDP, Jacobson & Mayne ) appear extensively in modern autonomous systems for complex trajectory optimization. However, whether they can be lifted to large-scale stochastic optimization, as in the DNN training, remains unclear.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we make a significant advance toward optimal-control-theoretic training algorithms inspired by ADP. We first show that most existing first- and second-order optimizers can be derived from DDP as special cases. Built upon this intriguing connection, we present a new class of optimizer which marries the best of both. The proposed method, DDP Neural Optimizer (DDPNOpt), features layer-wise feedback policies, which, as we will show through experiments, improve convergence and robustness. To enable Table 1: Terminology mapping | | Deep Learning | Optimal Control | efficient training, DDPNOpt adapts key components including (i) curvature adaption from existing methods, (ii) stabilization techniques used in trajectory optimization, and (iii) an efficient factorization to OCP. These lift the complexity by orders of magnitude compared with other OCP-inspired baselines, without sacrificing the performance. In summary, we present the following contributions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- We draw a novel perspective of DNN training from the trajectory optimization viewpoint, based on a theoretical connection between existing training methods and the DDP algorithm. - We present a new class of optimizer, DDPNOpt, that performs a distinct backward pass inherited with Bellman optimality and generates layer-wise feedback policies to robustify the training against unstable hyperparameter (e.g. large learning rate) setups. - We show that DDPNOpt achieves competitive performance against existing training methods on classification datasets and outperforms previous OCP-inspired methods in both training performance and runtime complexity. We also identify DDPNOpt can mitigate vanishing gradient.

<!-- chunk {"id": "body-0009", "role": "body", "section": "TRAINING DNNS AS TRAJECTORY OPTIMIZATION", "weight": 1.0} -->

Recall that DNNs can be interpreted as dynamical systems where each layer is viewed as a distinct time step. Consider e.g. the propagation rule in feedforward layers, x t ∈ R n t and x t +1 ∈ R n t +1 represent the activation vector at layer t and t +1, with h t ∈ R n t +1 being the pre-activation vector. σ t and g t respectively denote the nonlinear activation function and the affine transform parametrized by the vectorized weight u t ≜ [vec(W t), b t] T. Eq. 6 can be seen as a dynamical system (by setting f t ≡ σ t ◦ g t in OCP) propagating the activation vector x t using u t.

<!-- chunk {"id": "body-0010", "role": "body", "section": "TRAINING DNNS AS TRAJECTORY OPTIMIZATION", "weight": 1.0} -->

Next, notice that the gradient descent (GD) update, denoted δ ¯ u ∗ ≡ -η ∇ ¯ u J with η being the learning rate, can be break down into each layer, i.e. δ ¯ u ∗ ≜ { δ u ∗ t } T -1 t =0, and computed backward by is the per-layer objective 1 at layer t. It can be readily verified that p t ≡ ∇ x t J t gives the exact Back-propagation dynamics. Eq. 8 suggests that GD minimizes the quadratic expansion of J t with the Hessian ∇ 2 u t J t replaced by 1 η I t. Similarly, adaptive first-order methods, such as RMSprop and Adam, approximate the Hessian with the diagonal of the covariance matrix. Second-order methods, such as KFAC and EKFAC, compute full matrices using Gauss-Newton (GN) approximation: We now draw a novel connection between the training procedure of DNNs and DDP. Let us first summarize the Back-propagation (BP) with gradient descent in Alg. 2 and compare it with DDP (Alg. 1).

<!-- chunk {"id": "body-0011", "role": "body", "section": "TRAINING DNNS AS TRAJECTORY OPTIMIZATION", "weight": 1.0} -->

At each training iteration, we treat the current weight as the control ¯ u that simulates the activation sequence ¯ x. Starting from this nominal trajectory (¯ x, ¯ u), both algorithms recursively define some layer-wise objectives (J t in Eq. 8 vs V t in Eq. 1), compute the weight/control update from the quadratic expansions (Eq. 7 vs Eq. 2), and then carry certain information (∇ x t J t vs (V t x, V t xx)) backward to the preceding layer. The computation graph between the two approaches is summarized in Fig. 1. In the following proposition, we make this connection formally and provide conditions when the two algorithms become equivalent.

<!-- chunk {"id": "body-0012", "role": "body", "section": "TRAINING DNNS AS TRAJECTORY OPTIMIZATION", "weight": 1.0} -->

Proposition 2. Assume Q t ux = 0 at all stages, then the backward dynamics of the value derivative can be described by the Back-propagation, In this case, the DDP policy is equivalent to the stage-wise Newton, in which the gradient is preconditioned by the block-wise inverse Hessian at each layer: If further we have Q t uu ≈ 1 η I, then DDP degenerates to Back-propagation with gradient descent.

<!-- chunk {"id": "body-0013", "role": "body", "section": "TRAINING DNNS AS TRAJECTORY OPTIMIZATION", "weight": 1.0} -->

Proof is left in Appendix A.2. Proposition 2 states that the backward pass in DDP collapses to BP when Q ux vanishes at all stages. In other words, existing training methods can be seen as special cases of DDP when the mixed derivatives ( i.e. ∇ x t u t ) of the layer-wise objective are discarded.

<!-- chunk {"id": "body-0014", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Motivated by Proposition 2, we now present a new class of optimizer, DDP Neural Optimizer (DDPNOpt), on training feedforward and convolution networks. DDPNOpt follows the same procedure in vanilla DDP (Alg. 1) yet adapts several key traits arising from DNN training, which we highlight below.

<!-- chunk {"id": "body-0015", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Evaluate derivatives of Q t with layer dynamics. The primary computation in DDPNOpt comes from constructing the derivatives of Q t at each layer. When the dynamics is represented by the layer propagation (recall Eq. 6 where we set f t ≡ σ t ◦ g t), we can rewrite Eq. 3 as: 1 Hereafter we drop x t in all ℓ t (·) as the layer-wise loss typically involves weight regularization alone.

<!-- chunk {"id": "body-0016", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Curvature approximation. Next, since DNNs are highly over-parametrized models, u t (i.e. the layer weight) will be in high-dimensional space. This makes Q t uu and (Q t uu) -1 computationally intractable to solve; thus requires approximation. Recall the interpretation we draw in Eq. 8 where existing optimizers differ in approximating the Hessian ∇ 2 u t J t. DDPNOpt adapts the same curvature approximation to Q t uu. For instance, we can approximate Q t uu simply with an identity matrix I t, adaptive diagonal matrix diag(√ E [Q t u ⊙ Q t u]), or the GN matrix: Table 2 summarizes the difference in curvature approximation (i.e. the precondition M t) for different methods. Note that DDPNOpt constructs these approximations using (V, Q) rather than J since they consider different layer-wise objectives. As a direct implication from Proposition 2, DDPNOpt will degenerate to the optimizer it adapts for curvature approximation whenever all Q t ux vanish.

<!-- chunk {"id": "body-0017", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Outer-product factorization. When the memory efficiency becomes nonnegligible as the problem scales, we make GN approximation to ∇ 2 φ, since the low-rank structure at the prediction layer has been observed for problems concerned in this work. In the following proposition, we show that for a specific type of OCP, which happens to be the case of DNN training, such a low-rank structure preserves throughout the DDP backward pass.

<!-- chunk {"id": "body-0018", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Proposition 3 (Outer-product factorization in DDPNOpt). Consider the OCP where ℓ t ≡ ℓ t (u t) is independent of x t, If the terminal-stage Hessian can be expressed by the outer product of vector z T x, ∇ 2 φ (x T) = z T x ⊗ z T x (for instance, z T x = ∇ φ for GN), then we have the factorization for all t: q t u, q t x, and z t x are outer-product vectors which are also computed along the backward pass.

<!-- chunk {"id": "body-0019", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

The derivation is left in Appendix A.3. In other words, the outer-product factorization at the final layer can be backward propagated to all proceeding layers. Thus, large matrices, such as Q t ux, Q t xx, V t xx, and even feedback policies K t, can be factorized accordingly, greatly reducing the complexity.

<!-- chunk {"id": "body-0020", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Algorithm 3 Differential Dynamic Programming Neural Optimizer (DDPNOpt) 1: Input: dataset D, learning rate η, training iteration K, batch size B, regularization ϵ V xx 2: Initialize the network weights ¯ u (i.e. nominal control trajectory) 3: for k = 1 to K do 4: Sample batch initial state from dataset, X 0 ≡ { x (i) 0 } B i =1 ∼ D 5: Forward propagate to generate nominal batch trajectory X t ▷ Forward simulation 6: Set V T x (i) = ∇ x (i) Φ(x (i) T) and V T xx (i) = ∇ 2 x (i) Φ(x (i) T) 7: for t = T -1 to 0 do ▷ Backward Bellman pass 8: Compute Q t u, Q t x, Q t xx, Q t ux with Eq. 12 (or Eq. 16-17 if factorization is used) 9: Compute E [Q t uu] with one of the precondition matrices in Table 2 10: Store the layer-wise feedback policy δ u ∗ t (δ X t) = 1 B ∑ B i

<!-- chunk {"id": "body-0021", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

=1 k (i) t + K (i) t δ x (i) t 11: Compute V t x (i) and V t xx (i) with Eq. 5 (or Eq. 16-17 if factorization is used) 12: V t xx (i) ← V t xx (i) + ϵ V xx I t if regularization is used 13: end for 14: Set ˆ x (i) 0 = x (i) 0 15: for t = 0 to T -1 do ▷ Additional forward pass 16: u ∗ t = u t + δ u ∗ t (δ X t), where δ X t = { ˆ x (i) t -x (i) t } B i =1 17: ˆ x (i) t +1 = f t (ˆ x (i) t, u ∗ t) 18: end for 19: ¯ u (k +1) ←{ u ∗ t } T -1 t =0 20: end for Regularization on V xx.

<!-- chunk {"id": "body-0022", "role": "body", "section": "EFFICIENT APPROXIMATION AND FACTORIZATION", "weight": 1.0} -->

Finally, we apply Tikhonov regularization to the value Hessian V t xx (line 12 in Alg. 3). This can be seen as placing a quadratic state-cost and has been shown to improve stability on optimizing complex humanoid behavior. For the application of DNN where the dimension of the state (i.e. the vectorized activation) varies during forward/backward pass, the Tikhonov regularization prevents the value Hessian from low rank (throught g t T u V t hh g t x); hence we also observe similar stabilization effect in practice.

<!-- chunk {"id": "body-0023", "role": "body", "section": "THE ROLE OF FEEDBACK POLICIES", "weight": 1.0} -->

DDPNOpt differs from existing methods in the use of feedback K t and state differential δ x t. The presence of these terms result in a distinct backward pass inherited with the Bellman optimality. As shown in Table 2, the two frameworks differ in computing the update directions d t, where the Bellman formulation applies the feedback policy through additional forward pass with δ x t. We have built the connection between these two d t in Proposition 2. In this section, we further characterize the role of the feedback policy K t and state differential δ x t during optimization.

<!-- chunk {"id": "body-0024", "role": "body", "section": "THE ROLE OF FEEDBACK POLICIES", "weight": 1.0} -->

First we discuss the relation of DDPNOpt with other second-order methods and highlight the role feedback during training. To do so let us consider the example in Fig. 2a. Given an objective L expanded at ( x 0, u 0 ), standard second-order methods compute the Hessian w.r.t. u then apply the update δu = -L -1 uu L u (shown as green arrows). DDPNOpt differs in that it also computes the mixed partial derivatives, i.e. L ux. The resulting update law has the same intercept but with an additional feedback term linear in δx (shown as red arrows). Thus, DDPNOpt searches for an update from the affine mapping Γ ′ δ x t (Eq. 2), rather than the vector space R m t (Eq. 7).

<!-- chunk {"id": "body-0025", "role": "body", "section": "THE ROLE OF FEEDBACK POLICIES", "weight": 1.0} -->

Next, to show how the state differential δ x t arises during optimization, notice from Alg. 1 that ˆ x t can be compactly expressed as ˆ x t = F t (x 0, ¯ u + δ ¯ u ∗ (δ ¯ x)) 2. Therefore, δ x t = ˆ x t -x t captures the state difference when new updates δ ¯ u ∗ (δ ¯ x) are applied until layer t -1. Now, consider the 2D example in Fig 2b. Back-propagation proposes the update directions (shown as blue arrows) from the first-order derivatives expanded along the nominal trajectory (¯ x, ¯ u). However, as the weight at each layer is correlated, parameter updates from previous layers δ ¯ u ∗ s affect proceeding states { x t: t > s }, thus the trustworthiness of their descending directions. As shown in Fig 2c, cascading these (green) updates may cause an over-shoot w.r.t. the designed target.

<!-- chunk {"id": "body-0026", "role": "body", "section": "THE ROLE OF FEEDBACK POLICIES", "weight": 1.0} -->

From the trajectory optimization perspective, a much stabler direction will be instead ∇ u t J t (ˆ x t, u t) (shown as orange), where the derivative is evaluated at the new cascading state ˆ x t, which accounts for previous updates, rather than the original state x t. This is exactly what DDPNOpt proposes, as we can derive the relation (see Appendix A.5), 2 F t ≜ f t ◦ · · · ◦ f 0 denotes the compositional dynamics propagating x 0 with the control sequence { u s } t s =0.

<!-- chunk {"id": "body-0027", "role": "body", "section": "THE ROLE OF FEEDBACK POLICIES", "weight": 1.0} -->

Thus, the feedback direction compensates the over-shoot by steering the GD update toward ∇ u t J t (ˆ x t, u t ) after observing δ x t. The difference between ∇ u t J (ˆ x t, u t ) and ∇ u t J ( x t, u t ) cannot be neglected especially during early training when the loss landscape contains nontrivial curvature everywhere. In short, the use of feedback K t and state differential δ x t arises from the fact that deep nets exhibit chain structures. DDPNOpt feedback policies thus have a stabilization effect on robustifying the training dynamics against e.g. improper hyper-parameters which may cause unstable training. This perspective ( i.e. optimizing chained parameters) is explored rigorously in trajectory optimization, where DDP is shown to be numerically stabler than direct optimization such as Newton method.

<!-- chunk {"id": "body-0028", "role": "body", "section": "THE ROLE OF FEEDBACK POLICIES", "weight": 1.0} -->

Remarks on other optimizers. Our discussions so far rigorously explore the connection between DDP and stage/layer-wise Newton, thus include many popular second-order training methods. General Newton method coincides with DDP only for linear dynamics, despite both share the same convergence rate when the dynamics is fully expanded to second order. We note that computing layer-wise value Hessians with only first-order expansion on the dynamics (Eq. 12) resembles the computation in Gauss-Newton method. For other controltheoretic methods, e.g. PID optimizers, they mostly consider the dynamics over training iterations. DDPNOpt instead focuses on the dynamics inherited in the DNN architecture.

<!-- chunk {"id": "body-0029", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

Networks & Baselines Setup. We first validate the performance of training fully-connected (FCN) and convolution networks (CNN) using DDPNOpt on classification datasets. FCN consists of 5 fully-connected layers with the hidden dimension ranging from 10 to 32, depending on the size of the dataset. CNN consists of 4 convolution layers (with 3 × 3 kernel, 32 channels), followed by 2 fully-connected layers. We use ReLU activation on all datasets except Tanh for WINE and DIGITS to better distinguish the differences between optimizers. The batch size is set to 8 -32 for datasets trained with FCN, and 128 for datasets trained with CNN. As DDPNOpt combines strengths from both standard training methods and OCP framework, we select baselines from both sides. This includes first-order methods, i.e. SGD (with tuned momentum), RMSprop, Adam, and second-order method EKFAC, which is a recent extension of the popular KFAC.

<!-- chunk {"id": "body-0030", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

For OCP-inspired methods, we compare DDPNOpt with vanilla DDP and E-MSA, which is also a second-order method yet built upon the PMP framework. Regarding the curvature approximation used in DDPNOpt ( M t in Table 2), we found that using adaptive diagonal and GN matrices respectively for FCNs and CNNs give the best performance in practice. We leave the complete experiment setup and additional results in Appendix A.6.

<!-- chunk {"id": "body-0031", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

Training Results. Table 3 presents the results over 10 random trials. It is clear that DDPNOpt outperforms two OCP baselines on all datasets and network types. In practice, both baselines suffer from unstable training and require careful tuning on the hyper-parameters. In fact, we are not able to obtain results for vanilla DDP with any reasonable amount of computational resources when the problem size goes beyond FC networks. This is in contrast to DDPNOpt which adapts amortized curvature estimation from widely-used methods; thus exhibits much stabler training dynamics with superior convergence. In Table 4, we provide the analytic runtime and memory complexity among different methods. While vanilla DDP grows cubic w.r.t. BX, DDPNOpt reduces the computation by orders of magnitude with efficient approximation presented in Sec. 3. As a result, when measuring the actual computational performance with GPU parallelism, DDPNOpt runs nearly as fast as standard methods and outperforms E-MSA by a large margin. The additional memory complexity, when comparing DDP-inspired methods with Back-propagation methods, comes from the layer-wise feedback policies.

<!-- chunk {"id": "body-0032", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

However, DDPNOpt is much memory-efficient compared with vanilla DDP by exploiting the factorization in Proposition 3.

<!-- chunk {"id": "body-0033", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

| | DataSet | | Standard baselines | Standard baselines | | OCP-inspired baselines | OCP-inspired baselines | DDPNOpt (ours) | Figure 3: Runtime comparison on MNIST.

<!-- chunk {"id": "body-0034", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

In Fig. 4a we report the performance difference between each baseline and its associated DDPNOpt variant. Each grid corresponds to a distinct training configuration that is averaged over 10 random trails, and we keep all hyper-parameters ( e.g. learning rate and weight decay) the same between baselines and their DDPNOpt variants. Thus, the performance gap only comes from the feedback policies, or equivalently the update directions in Table 2. Blue ( resp. red) indicates an improvement ( resp. degradation) when the feedback policies are presented. Clearly, the improvement over baselines remains consistent across most hyper-parameters setups, and the performance gap tends to become obvious as the learning rate increases. This aligns with the previous study on numerical stability, which suggests the feedback can stabilize the optimization when e.g. larger control updates are taken. Since larger control corresponds to a further step size in the application of DNN training, one should expect DDPNOpt to show its robustness as the learning rate increases. As shown in Fig. 4b, such a stabilization can also lead to smaller variance and faster convergence.

<!-- chunk {"id": "body-0035", "role": "body", "section": "PERFORMANCE ON CLASSIFICATION DATASET", "weight": 1.0} -->

This sheds light on the benefit gained by bridging two seemly disconnected methodologies between DNN training and trajectory optimization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "DISCUSSION ON FEEDBACK POLICIES", "weight": 1.5} -->

Visualization of Feedback Policies. To understand the effect of feedback policies more perceptually, in Fig. 5 we visualize the feedback policy when training CNNs. This is done by first conducting Vxx regularization x+δxmax singular-value decomposition on the feedback matrices K t, then projecting the leading right-singular vector back to image space (see Alg. 4 and Fig. 7 in Appendix for the pseudo-code). These feature maps, denoted δx max in Fig. 5, correspond to the dominating differential image that the policy shall respond with during weight update. Fig. 5 shows that the feedback policies indeed capture non-trivial visual features related to the pixel-wise difference between spatially similar classes, e.g. or. These differential maps differ from adversarial perturbation as the former directly links the parameter update to the change in activation; thus being more interpretable.

<!-- chunk {"id": "body-0037", "role": "body", "section": "DISCUSSION ON FEEDBACK POLICIES", "weight": 1.5} -->

Vanishing Gradient. Lastly, we present an interesting finding on how the feedback policies help mitigate vanishing gradient (VG), a notorious effect when DNNs become impossible to train as gradients vanish along Back-propagation. Fig. 6a reports results on training a sigmoid-activated DNN on DIGITS. We select SGD-VGR, which imposes a specific regularization to mitigate VG, and EKFAC as our baselines. While both baselines suffer to make any progress, DDPNOpt continues to generate non-trivial updates as the state-dependent feedback, i.e. K t δ x t, remains active. The effect becomes significant when dynamics is fully expanded to the second order. As shown in Fig. 6b, the update norm from DDPNOpt is typically 5 -10 times larger. We note that in this experiment, we replace the cross-entropy (CE) with Max-Mahalanobis center (MMC) loss, a new classification objective that improves robustness on standard vision datasets. MMC casts classification to distributional regression, providing denser Hessian and making problems similar to original trajectory optimization. None of the algorithms escape from VG using CE.

<!-- chunk {"id": "body-0038", "role": "body", "section": "DISCUSSION ON FEEDBACK POLICIES", "weight": 1.5} -->

We highlight that while VG is typically mitigated on the architecture basis, by having either unbounded activation function or residual blocks, DDPNOpt provides an alternative from the algorithmic perspective.

<!-- chunk {"id": "body-0039", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this work, we introduce DDPNOpt, a new class of optimizer arising from a novel perspective by bridging DNN training to optimal control and trajectory optimization. DDPNOpt features layer-wise feedback policies which improve convergence and robustness to hyper-parameters over existing optimizers. It outperforms other OCP-inspired methods in both training performance and scalability. This work provides a new algorithmic insight and bridges between deep learning and optimal control.
