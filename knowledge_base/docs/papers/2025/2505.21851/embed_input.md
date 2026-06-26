<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Streaming Flow Policy: Simplifying Diffusion/Flow-Matching Policies by Treating Action Trajectories as Flow Trajectories

Topics include Flow matching, Diffusion models, Robot learning, Imitation learning, Visuomotor policy, Streaming flow policy.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Simplifies flow-matching robot policies by treating the entire action trajectory as a flow trajectory rather than denoising per-timestep, reducing inference overhead while maintaining expressive multimodal action distributions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent advances in diffusion/flow-matching policies have enabled imitation learning of complex, multi-modal action trajectories. However, they are computationally expensive because they sample a *trajectory of trajectories*—a diffusion/flow trajectory of action trajectories. They discard intermediate action trajectories, and must wait for the sampling process to complete before any actions can be executed on the robot. We simplify diffusion/flow policies by *treating action trajectories as flow trajectories*. Instead of starting from pure noise, our algorithm samples from a narrow Gaussian around the last action. Then, it incrementally integrates a velocity field learned via flow matching to produce a sequence of actions that constitute a *single* trajectory. This enables actions to be streamed to the robot on-the-fly *during* the flow sampling process, and is well-suited for receding horizon policy execution. Despite streaming, our method retains the ability to model multi-modal behavior. We train flows that *stabilize* around demonstration trajectories to reduce distribution shift and improve imitation learning performance.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Streaming flow policy outperforms prior methods while enabling faster policy execution and tighter sensorimotor loops for learning-based robot control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in robotic imitation learning, such as diffusion policy and flow-matching policy have enabled robots to learn complex, multi-modal action distributions for challenging real-world tasks such as cooking, laundry folding, robot assembly and navigation. They take a history of observations as input, and output a sequence of actions (also called an "action chunk"). Conventional diffusion$/$flow policies represent a direct application of diffusion models and flow-matching to robot action sequences --- they formulate the generative process as probabilistic transport in the space of action sequences, starting from pure Gaussian noise. Therefore, diffusion$/$flow policies represent a "trajectory of trajectories" --- a diffusion$/$flow trajectory of action trajectories. This approach has several drawbacks. The sampling process discards all intermediate action trajectories, making diffusion$/$flow policies computationally inefficient. Importantly, the robot must wait for the diffusion$/$flow process to complete before executing any actions. Thus, diffusion$/$flow policies often require careful hyper-parameter tunning to admit tight control loops.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a novel imitation learning framework that harnesses the temporal structure of action trajectories. We simplify diffusion$/$flow policies by treating action trajectories as flow trajectories. Our aim is to learn a flow transport in the action space ${\mathcal{A}}$, as opposed to trajectory space ${\mathcal{A}}^{T}$. Unlike diffusion$/$flow policies that start the sampling process from pure Gaussian noise (in ${\mathcal{A}}^{T}$), our initial sample comes from a narrow Gaussian centered around the most recently generated action (in ${\mathcal{A}}$). Then, we iteratively integrate a learned velocity field to generate a sequence of future actions that forms a single trajectory. The "flow time" --- indicating progress of the flow process --- coincides with execution time of the sampled trajectory. Iteratively generating the sequence of actions allows the actions to be streamed to the robot's controller on-the-fly during the flow generation process, significantly improving the policy's speed and reactivity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show how a streaming flow policy with the above desiderata can be learned using flow matching. Given an action trajectory from the training set, we construct a velocity field conditioned on this example that samples paths in a narrow Gaussian "tube" around the demonstration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our training procedure is remarkably simple --- we regress a neural network $v_{\theta}(a,t\,|\,h)$ that takes as input (i) an observation history $h$, (ii) flow timestep $t\in$, and (iii) action $a$, to match the constructed velocity field. We are able to re-use existing architectures for diffusion$/$flow policy while only modifying the input and output dimension of the network from ${\mathcal{A}}^{T}$ to ${\mathcal{A}}$. Flow matching guarantees that the marginal flow learned over all training trajectories, as shown in Streaming Flow Policy Simplifying diffusion$/$flow-matching policies by treating action trajectories as flow trajectories Website: (c, d), is multi-modal. Specifically, the marginal distribution of actions at each timestep $t$ matches that of the training distribution. Our approach thus retains diffusion$/$flow policy's ability to represent multi-modal trajectories while allowing for streaming trajectory generation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

How should we construct the target velocity field? Prior work has shown that low-level stabilizing controllers can reduce distribution shift and improve theoretical imitation learning guarantees. We leverage the flexibility of the flow matching framework to construct velocity fields that stabilize around a given demonstration trajectory, by adding velocity components that guide the flow back to the demonstration. In our experiments, we find that stabilizing flow significantly improves performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method can leverage two key properties specific to robotics applications: (i) robot actions are often represented as position setpoints of the robot's joints or end-effector pose that are tracked by a low-level controller, (ii) the robot's joint positions$/$end-effector poses can be accurately measured via proprioceptive sensors (e.g. joint encoders) and forward kinematics. Streaming flow policy can not only imitate action trajectories, but is especially suited to imitate state trajectories when a stiff controller is available that can closely track state trajectories. In this case, the flow sampling process can be initialized from the known ground truth robot state instead of the state predicted from the previous chunk. This reduces uncertainty and error in the generated trajectory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unlike diffusion$/$flow policies, streaming flow policy is only guaranteed to match the marginal distribution of actions at each timestep, but not necessarily the joint distribution. Consequently, our method can produce trajectories that are compositions of segments of training trajectories, even if the composition was not part of the training dataset. While this may be seen as a limitation of our method, we argue that for most robotics tasks, compositionality is not only valid, but a desirable property that requires fewer demonstrations. Furthermore, while streaming flow policy is unable to capture global constraints that can only be represented in the joint distribution, it can learn local constraints such as joint constraints, and convex velocity constraints; see Sec. 9 for more details. In practice, we find that streaming flow policy performs comparably to diffusion policy while being significantly faster.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Symbol Description Domain Tpred Prediction time horizon of trajectories during training ℝ+ Tchunk Time horizon of action chunk during inference ℝ+ t Flow time = execution time rescaled from [0, Tpred] to a Robot action (often a robot configuration) 𝒜 v Action velocity $T\hskip-1.99997pt{\mathcal{A}}$ o, h Observation, Observation history 𝒪, ℋ ξ Action trajectory (chunk), where time is rescaled from [0, Tpred] to → 𝒜 ξ̇ Time derivative of action trajectory: $\dot{\xi}(t)=\frac{d}{dt}\xi(t)$ $\to T\hskip-1.99997pt{\mathcal{A}}$ p𝒟(h, ξ) Distribution of observation histories and future action chunks. Training set is assumed to be sampled from this distribution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Δ(ℋ × → 𝒜) vθ(a, t | h) Learned marginal velocity field with network parameters θ $T\hskip-1.99997pt{\mathcal{A}}$ $\hskip-1.99997ptv_{\xi}(a,t)$ Conditional velocity field for demonstration ξ $T\hskip-1.99997pt{\mathcal{A}}$ $\hskip-1.99997ptp_{\xi}(a\,|\,t)$ Marginal probability distribution over a at time t induced by vξ Δ(𝒜) v*(a, t | h) Optimal marginal velocity field under data distribution p𝒟 $T\hskip-1.99997pt{\mathcal{A}}$ $\hskip-3.99994ptp^{*}(a\,|\,t,h)$ Marginal probability distribution over a at time t induced by v* Δ(𝒜) k, σ0 Stabilizing gain, Initial standard deviation ℝ ≥ 0, ℝ+ Table 1: Mathematical notation used throughout the paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Analytically constructing conditional velocity fields", "weight": 1.0} -->

Given an action trajectory $\xi$, we first analytically construct a stabilizing conditional flow that travels closely along $\xi$. This will be used as a target to train a neural network velocity field. In particular, we construct a velocity field $v_{\xi}(a,t)$ and an initial distribution $p^{0}_{\xi}(a)$ such that the induced marginal probability distributions $p_{\xi}(a\,|\,t)$ form a thin Gaussian "tube" around $\xi$. By "Gaussian tube", we mean that $p_{\xi}(a\,|\,t)$ is a narrow Gaussian distribution centered at $\xi(t)$ for every $t\in$. This is illustrated in Streaming Flow Policy Simplifying diffusion$/$flow-matching policies by treating action trajectories as flow trajectories Website: (a,b).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Analytically constructing conditional velocity fields", "weight": 1.0} -->

We construct the stabilizing conditional flow as: The initial distribution $p_{\xi}^{0}(a)$ is a narrow Gaussian centered at the initial action $\xi$ with a small standard deviation $\sigma_{0}$. The velocity has two components. The trajectory velocity is the time-derivative of the action trajectory $\xi$ at time $t$, and does not depend on $a$. This term serves to move along the direction of the trajectory. The stabilization term is a negative proportional error feedback that corrects deviations from the trajectory. Controllers that stabilize around demonstration trajectories are known to reduce distribution shift and improve theoretical imitation learning guarantees. We empirically observe that the stabilizing term produces significantly more robust and performant policies, compared to setting $k=0$. We note that our framework leverages time derivatives of action trajectories $\dot{\xi}(t)$ during training, which are easily accessible, in addition to $\xi(t)$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Analytically constructing conditional velocity fields", "weight": 1.0} -->

This is in contrast to conventional diffusion$/$flow policies that only use $\xi(t)$ but not $\dot{\xi}(t)$. Throughout this paper, the term 'velocity' refers to $\dot{\xi}(t)$, and not the physical velocity of the robot. While they may coincide for certain choices of the action space ${\mathcal{A}}$, $\dot{\xi}(t)$ may not represent any physical velocity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Analytically constructing conditional velocity fields", "weight": 1.0} -->

Theorem 1: The stabilizing conditional flow given by Eq. 2 induces the following per-timestep marginal distributions over the action space: Proof: See App. A. The distribution of states sampled at any timestep $t\in$ is a Gaussian centered at the trajectory $\xi(t)$. Furthermore, the standard deviation $\ignorespaces\sigma_{t}=\sigma_{0}e^{-kt}$ starts from $\sigma_{0}$ at $t=0$ and decays exponentially with time at rate $k$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning objective for velocity fields to match marginal action distributions", "weight": 1.0} -->

Let $p_{\mathcal{D}}(h,\xi)$ denote the unknown data generating distribution from which the training dataset is sampled. The conditional velocity field $v_{\xi}(a,t)$ defined in Sec. 3 models a single action trajectory. If multiple behaviors $\xi$ are valid for the same input history $h$, how can we learn a velocity field $v(a,t\,|\,h)$ that represents multi-modal trajectory distributions? We use flow matching with $v_{\xi}(a,t)$ the target. The conditional flow matching loss for a history-conditioned velocity field $v(a,t\,|\,h)$ is defined as: This is simply an expected $L_{2}$ loss between a candidate velocity field $v(a,t\,|\,h)$ and the the analytically constructed conditional velocity field $v_{\xi}(a,t)$ as target.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning objective for velocity fields to match marginal action distributions", "weight": 1.0} -->

The expectation is over histories and trajectories under the probability distribution $p_{\mathcal{D}}(h,\xi)$, time $t$ sampled uniformly from $$, and action $a$ sampled from the constructed conditional flow known in closed-form in Eq. 3. The following theorem characterizes the per-timestep marginal distributions induced by the minimizer of this loss: Theorem 2: The minimizer $v^{*}=\arg\min_{v}\mathcal{L}_{\mathrm{CFM}}(v,p_{\mathcal{D}})$ induces the following per-timestep marginal distribution for each $t\in$ and observation history $h$: Proof: This is a direct consequence of the flow matching theorems (Thms. 1 and 2) in Lipman et al..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning objective for velocity fields to match marginal action distributions", "weight": 1.0} -->

Intuitively, the per-timestep marginal distribution induced by the minimizer of $\mathcal{L}_{\mathrm{CFM}}$ is the average of per-timestep marginal distributions of constructed conditional flows $p_{\xi}(a\,|\,t)$, over the distribution of future trajectories in $p_{\mathcal{D}}(\xi\,|\,h)$ that share the same observation history $h$. Since our conditional flows are constructed to sample narrow Gaussian tubes around demonstrated action sequences, the optimal $v^{*}$ will produce a multi-modal mixture distribution over future actions from the data-generating distribution consistent with observation history $h$, convolved with small noise $\sigma_{t}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Learning objective for velocity fields to match marginal action distributions", "weight": 1.0} -->

Matching the per-timestep marginal distributions is desirable and necessary for representing multi-modal distributions. Consider the example in Streaming Flow Policy Simplifying diffusion$/$flow-matching policies by treating action trajectories as flow trajectories Website: that constructs two conditional flows, one that samples actions to the right ($a>0$), and the other that samples actions to the left ($a<0$). In order for a learned model to sample both modes with probability 0.5 each, its per-timestep marginal distribution must match the averaged per-timestep marginal distributions of conditional flows. Unlike flow policies that only require matching the target distributions at $t=1$, our method leverages the fact that flow matching matches the marginal distributions at all timesteps $t\in$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Learning objective for velocity fields to match marginal action distributions", "weight": 1.0} -->

Algorithm 1 Training algorithm 1:Training set 𝒟 = {(hi, ξi)}i = 1N, Tpred 2: • ξ has time horizon Tpred rescaled to 3:while not converged do 4: (h, ξ) ∼ 𝒟 5: t ∼ Uniform 6: a ∼ pξ(a | t) (defined in Eq. 3) 7: $\theta\leftarrow\theta-\hskip 0.0pt\lambda\nabla_{\theta}\hskip-1.99997pt\underbrace{\|v_{\xi}(a,t)-v_{\theta}(a,t\,|\,h)\|^{2}}_{{\text{Conditional flow matching loss}}}$ 8:return vθ Algorithm 2 Inference algorithm 1:vθ(a, t | h), Tpred, Tchunk, Δt 2:h, a ← {}, qcurr (current robot configuration) 3:while True do 4: t, hchunk ← 0, h 5: if imitating state: a ← qcurr

<!-- chunk {"id": "body-0023", "role": "body", "section": "Learning objective for velocity fields to match marginal action distributions", "weight": 1.0} -->

6: while t ≤ Tchunk/Tpred do // open loop 7: o ← Execute(a) // stream action during flow 8: h ← h ∪ {o} 9: a ← a + vθ(a, t | hchunk)Δt // integration step 10: t ← t + Δt

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

Inference: While behavior policies are trained to predict sequences of horizon $T_{\mathrm{pred}}$, they are usually run in a receding horizon fashion with a potentially different action chunk horizon $T_{\mathrm{chunk}}\leq T_{\mathrm{pred}}$. The integration timestep $\Delta t$ is another hyperparameter that controls the granularity of the action sequence. Therefore, to generate an action chunk, we integrate the velocity field in $t\in[0,T_{\mathrm{chunk}}/T_{\mathrm{pred}}]$, producing $T_{\mathrm{chunk}}/(T_{\mathrm{pred}}\Delta t)$ many actions. The action chunk is computed and executed open-loop i.e. the neural network $v_{\theta}$ inputs the same observation history $h_{\mathrm{chunk}}$ for all integration steps. Importantly, we are able to stream and execute actions on the robot as soon as they are computed (see Alg. 2, 7).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

In contrast, diffusion$/$flow policies must wait for the inner loop to complete before executing any actions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

Deterministic execution at test time: Our learning framework suggests the initial action be sampled from $a_{0}\sim\mathcal{N}\left(a_{0}\,|\,a_{\mathrm{prev}},\sigma_{0}^{2}\right)$ (see Eqs. 1 and 2). However, during inference time, we avoid adding noise to actions by setting $\sigma_{0}=0$ to produce deterministic behavior. We do so because the ability to represent multi-modal distributions is primarily motivated by the need to prevent "averaging" distinct but valid behaviors of the same task. While representing multi-modality is crucial during training, the learned policy can be run deterministically at test time without loss in performance. For example, ACT sets its variance parameter to zero at test time to produce deterministic behavior. In App. B, we present a variant of streaming flow policy in an extended state space that decouples stochasticity into additional latent variables. This variant allows us to sample multiple modes of the trajectory distribution at test time without adding noise to actions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

However, we found that simply setting $\sigma_{0}=0$ at test time works better in practice; therefore we follow this strategy in all our experiments.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

Imitating actions vs. states: When training trajectories correspond to actions, we start integration of the current action chunk from the most recently generated action in the previous chunk. Streaming flow policy can also be used to imitate robot state trajectories when a controller is available that can closely track desired states. It is especially suited for state imitation because we can start integration of the current state chunk from the current robot state that is accurately measured by proprioceptive sensors. Therefore, streaming flow policy is able to leverage state feedback in two ways: in the history $h$ and the initialization $a_{0}$ for flow integration. This reduces error in the generated trajectory.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

95.1% / 96.0% 91.7% / 93.7% 03.5 ms 83.9% / 84.8% 08.8 ms Table 2: Imitation learning accuracy on the Push-T dataset. Our method (in green) compared against baselines (in red) / and ablations (in blue). See text for details.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training and inference algorithms for streaming flow policy", "weight": 1.0} -->

84.0% 4.5 ms Table 3: Imitation learning accuracy on RoboMimic environment. Our method (in green) compared against baselines (in red) / and ablations (in blue). See text for details.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate streaming flow policy on two imitation learning benchmarks: the Push-T environment, and RoboMimic, and perform real-world experiments on a Franka Research 3 robot arm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare our method (in green ) against 4 baselines (in red ): Row 1 (DP): standard diffusion policy that uses 100 DDPM steps, Row 2 (DP): a faster version of diffusion policy that uses 10 DDIM steps, Row 3: conventional flow matching-based policy and Row 4: Streaming Diffusion Policy, a recent method that runs diffusion policy in a streaming manner (see Sec. 7). We also compare against streaming flow policy that does not construct stabilizing flows during training, i.e. uses $k=0$ (in blue ). This ablation is designed to measure the contribution of stabilization to task performance. Following Chi et al., we report the average score for the 5 best checkpoints, the best score across all checkpoints, and the average latency per action for each method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Table 2, we report results on the Push-T environment: a simulated 2D planar pushing task where the robot state is the 2-D position of the cylindrical pusher in global coordinates, and actions are 2-D setpoints tracked by a PD controller. Push-T contains 200 training demonstrations and 50 evaluation episodes. We perform experiments in two settings: when simulator state is used as observations, and when images are used as observations. "Action imitation" is the standard practice of imitating action sequences provided in the benchmark training set. We also perform experiments with "state imitation" (see Sec. 4), where we directly imitate the measured 2D positions of the robot. Here, we use the known ground-truth robot position at the beginning of each action chunk to as a starting point for velocity field integration. In Table 3, we report results on the RoboMimic environment, specifically the "lift" and "can" tasks, with state inputs. Both tasks involve predicting sequences of 6-DOF end-effector poses with respect to a global frame that are tracked by a PD controller. Each task contains 300 training demonstrations, and 50 evaluation episodes.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

The tasks involve picking objects and placing them at specific locations, including picking a square nut and placing it on a rod.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

The neural network for streaming flow policy $v_{\theta}:{\mathcal{A}}\times\times{\mathcal{H}}\to T\hskip-1.99997pt{\mathcal{A}}$ is structurally similar to diffusion$/$flow policies (e.g. ${\epsilon}_{\theta}:{\mathcal{A}}^{T}\times\times{\mathcal{H}}\to{\mathcal{A}}^{T}$) with the only change being the input and output spaces (action space ${\mathcal{A}}$ vs. action-trajectory space ${\mathcal{A}}^{T}$). Therefore, we are able to re-use existing diffusion$/$flow policy architectures by changing the input and output dimension of the network and replacing 1-D temporal convolution/attention layers over action sequences with a fully connected layer.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Furthermore, due to the reduced dimensionality of the flow sampling space, we found that streaming flow policy is faster to train and has a smaller GPU memory footprint compared to diffusion$/$flow policies. figure Real-world experiments on a 7-DOF Franka Research 3 robot arm on the tasks of (a) reaching and picking an apple, and (b) reorienting a block. We compare our method against diffusion policy, and find that our method is noticeably faster and produces smoother motion; see comparison videos on our project website.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct real-world experiments on a Franka Research 3 robot arm with a RealSense D435f depth camera on two tasks: (a) reaching and picking an object, and (b) reorienting a block to a vertical goal orientation (see Sec. 6). We find that streaming flow policy is noticeably faster and produces smoother motion than diffusion policy, as shown in videos on the project website.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Conclusions: Stabilizing flow policy performs comparably to diffusion policy and other baselines in terms of performance on most tasks, while being significantly faster per action. Furthermore, the reported latency does not even take into account the fact that streaming flow policy can asynchronously run action generation and robot execution in parallel. In practice, this can avoid delays and jerky robot movements. Diffusion policy can be sped up by running fewer diffusion steps via DDIM. And flow-matching policy is also faster than diffusion policy. However, their speed seems to come at the cost of sometimes significant reduction in accuracy. In App. C, we analyze the performance of streaming flow policy as a function of the action chunk horizon $T_{\mathrm{chunk}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have presented a novel approach to imitation learning that addresses the computational limitations of existing diffusion and flow-matching policies. Our key contribution is a simplified approach that treats action trajectories as flow trajectories. This enables incremental integration of a learned velocity field that allows actions to be streamed to the robot during the flow sampling process. The streaming capability makes our method particularly well-suited for receding horizon policy execution. Despite the streaming nature of our approach, the flow matching framework guarantees the ability to model multi-modal action trajectories. By constructing flows that stabilize around demonstration trajectories, we reduce distribution shift and improve imitation learning performance. Our experimental results demonstrate that streaming flow policy performs comparably to prior imitation learning approaches on benchmark tasks, but enables faster policy execution and tighter sensorimotor loops, making it more practical for reactive, real-world robot control.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Limitations", "weight": 1.5} -->

In this section, we discuss some limitations of our approach.

<!-- chunk {"id": "body-0041", "role": "body", "section": "SFP does not match joint distribution, only per-timestep marginal distributions", "weight": 1.0} -->

Our flow matching framework ensures that the learned distribution over trajectories conditioned on the history matches the training distribution in terms of marginal distributions of actions at each timestep $t\in$. We however, do not guarantee that the joint distribution of actions across a trajectory matches the training distribution. This is in contrast to diffusion policy, that is able to match the joint distribution since the diffusion model operates in trajectory space ${\mathcal{A}}^{T}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "SFP does not match joint distribution, only per-timestep marginal distributions", "weight": 1.0} -->

Sections 9.1 and 9.1 illustrate a toy example where streaming flow policy matches marginal distributions but not the joint distribution. The $x$-axis represents 1-D robot actions, and the $y$-axis represents flow time ($t\in$). Sec. 9.1a shows two trajectories in blue and red, of shapes "S" and " S " respectively. The trajectories intersect at $t=0.5$. The learned flow field is shown in Sec. 9.1c, and the induced marginal distribution over actions is shown in Sec. 9.1d. The marginal distribution of actions matches the training distribution at each $t\in$. Trajectories sampled from the flow field are shown in Sec. 9.1d. The trajectory distribution contains two modes of equal probability: trajectories that always lie either in $a<0$ (shown in blue), or in $a>0$ (shown in red). The shapes formed by sampled trajectories --- " 3 " and "3" respectively --- do not match the shapes of trajectories in the training data.

<!-- chunk {"id": "body-0043", "role": "body", "section": "SFP does not match joint distribution, only per-timestep marginal distributions", "weight": 1.0} -->

A similar phenomenon is illustrated in Sec. 9.1 using the latent-space variant of streaming flow policy (see App. B) trained on the same dataset of intersecting trajectories. While the marginal distribution of actions again matches with the training distribution, the trajectories contain four modes, with shapes "S", " S ", " 3 " and "3". Note that the per-timestep marginal distributions over actions still match the training data. figure A toy example illustrating how streaming flow policy matches marginal distribution of actions in the trajectory at all time steps, but not necessarily their joint distribution. The x-axis represents a 1-D action space, and the y-axis represents both trajectory time and flow time. (a) The bi-modal training set contains two intersecting demonstration trajectories, illustrated in blue and red, with shapes “S” and “ S ” respectively. (b) The marginal distribution of actions at each time step learned by our streaming flow policy. The marginal distributions perfectly match the training data. (c) The learned velocity flow field vθ(a, t | h) that yeilds the marginal distributions in (b).

<!-- chunk {"id": "body-0044", "role": "body", "section": "SFP does not match joint distribution, only per-timestep marginal distributions", "weight": 1.0} -->

(d) Trajectories sampled from the learned velocity field. Trajectories that start from a < 0 are shown in blue, and those starting from a > 0 are shown in red. The sampled trajectories have shapes “ 3 ” and “3”, with equal probability. These shapes are different from the shapes “S” and “ S ” in the training distribution, although their margin distributions are identical. figure Different variants of streaming flow policy can produce different joint distributions of actions that are consistent with the marginal distributions in the training data. This example is produced using the latent-variable version of streaming flow policy, described in App. B. (a) The marginal distribution of actions at each time step learned by the streaming flow policy matches the training data. (b) Samples from the trained policy produces four modes with shapes “S”, “ S ”, “ 3 ” and “3”, whereas the training data contains only two modes with shapes “S” and “ S ”.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Streaming flow policies exhibit compositionality", "weight": 1.0} -->

The loss of fidelity to the joint distribution is a potential weakness of our framework. Therefore, this framework may not be the right choice when learning the correct joint distributions is crucial. However, another perspective is to think of our method as providing compositionality over training demonstrations. The sampled trajectories can be composed of pieces across the training data.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Streaming flow policies exhibit compositionality", "weight": 1.0} -->

For many robotics tasks, compositionality might be both valid and desirable. For example, in quasi-static tasks where the robot moves slowly, if two demonstration trajectories are valid, then the compositions across these trajectories are often also valid. Under this assumption, compositionality allows the flow model to learn many valid combinations of partial trajectories with fewer demonstrations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Streaming flow policies exhibit compositionality", "weight": 1.0} -->

What constraints on trajectories reflected in the training data can streaming flow policy learn? Streaming flow policy is unable to capture global constraints that can only be represented in the joint distribution. However, it can learn certain local constraints.

<!-- chunk {"id": "body-0048", "role": "body", "section": "SFPs can learn arbitrary position constraints", "weight": 1.0} -->

Robot actions $a\in Q\subseteq{\mathcal{A}}$ may be constrained to lie in a subset $Q\subseteq{\mathcal{A}}$. For example, $Q$ may reflect joint limits of a robot arm. Then, a well-trained streaming flow policy should learn this constraint as well.

<!-- chunk {"id": "body-0049", "role": "body", "section": "SFPs can learn arbitrary position constraints", "weight": 1.0} -->

To see why, consider Eq. 5 which states that the learned marginal density of actions $p^{*}(a\,|\,t,h)=\int_{\xi}p_{\xi}(a\,|\,t)\,p_{\mathcal{D}}(\xi\,|\,h)\,\mathrm{d}\xi$ at time $t$ is a weighted average of marginal densities of conditional flows $p_{\xi}(a\,|\,t)$. Recall that we construct $p_{\xi}(a\,|\,t)$ to be narrow Gaussian tubes around demonstration trajectories $\xi$. Assume that the thickness of the Gaussian tube is sufficiently small that $a\notin Q\implies p_{\xi}(a\,|\,t)<\epsilon$, for some small $\epsilon>0$ and for all $\xi,t$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "SFPs can learn arbitrary position constraints", "weight": 1.0} -->

Then we have from Eq. 5 that $p_{\xi}(a\,|\,t)<\epsilon\implies p^{*}(a\,|\,t,h)<\epsilon$ for all $t\in$. Therefore, the probability of sampling an action $a$ that violates the constraint $Q$ is extremely low.

<!-- chunk {"id": "body-0051", "role": "body", "section": "SFPs can learn convex velocity constraints", "weight": 1.0} -->

Theorem 2 of Lipman et al. implies that the minimizer of the conditional flow matching loss $v^{*}\coloneq\arg\min_{v}\mathcal{L}_{\mathrm{CFM}}(v,p_{\mathcal{D}})$ has the following form: Intuitively, the target velocity field $v^{*}$ at $(a,t)$ is a weighted average of conditional flow velocities $v_{\xi}(a,t)$ over demonstrations $\xi$. The weight for $\xi$ is the Bayesian posterior probability of $\xi$, where the prior probability $p_{\mathcal{D}}(\xi\,|\,h)$ is the probability of $\xi$ given $h$ in the training distribution, and the likelihood $p_{\xi}(a\,|\,t)$ is the probability that the conditional flow around $\xi$ generates $a$ at time $t$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "SFPs can learn convex velocity constraints", "weight": 1.0} -->

Under sufficiently small values of $k$, we have from Eq. 2 that $v_{\xi}(a,t)\approx\dot{\xi}(t)$. Note that $v^{*}$ is then a convex combination of demonstration velocities $\dot{\xi}(t)$. Consider convex constraints over velocities $\dot{\xi}(t)\in C$ i.e. $\dot{\xi}(t)$ is constrained to lie in a convex set $C$ for all $\xi$ with non-zero support $p_{\mathcal{D}}(\xi)>0$ and for all $t\in$. This is the case, for example, when robot joint velocities lie in a closed interval $[v_{\mathrm{min}},v_{\mathrm{max}}]$. Then, Eq. 6 implies that $v^{*}$ also lies in $C$.
