<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Imitation: Constraint-Aware Trajectory Generation with Flow Matching for End-to-End Autonomous Driving

Topics include Autonomous driving, Flow matching, Trajectory generation, Constraints, Multimodal planning, Safety.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes constraint-aware trajectory generation for end-to-end driving using flow matching instead of pure imitation. The method explicitly injects safety and physical constraints into the generative process, reducing the need for a separate post-generation optimization stage.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning is a critical component of end-to-end autonomous driving. However, prevailing imitation learning methods often suffer from mode collapse, failing to produce diverse trajectory hypotheses. Meanwhile, existing generative approaches struggle to incorporate crucial safety and physical constraints directly into the generative process, necessitating an additional optimization stage to refine their outputs. To address these limitations, we propose CATG, a novel planning framework that leverages Constrained Flow Matching. Concretely, CATG explicitly models the flow matching process, which inherently mitigates mode collapse and allows for flexible guidance from various conditioning signals. Our primary contribution is the novel imposition of explicit constraints directly within the flow matching process, ensuring that the generated trajectories adhere to vital safety and kinematic rules. Secondly, CATG parameterizes driving aggressiveness as a control signal during generation, enabling precise manipulation of trajectory style. Notably, on the NavSim v2 challenge, CATG achieved 2nd place with an EPDMS score of 51.31 and was honored with the Innovation Award.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end multimodal planning has established itself as a critical methodology in autonomous driving systems, significantly enhancing robustness and adaptability during inference when compared to single-trajectory prediction approaches. This capability is especially vital in ambiguous or highly interactive driving scenarios---such as unprotected left turns, merging in dense traffic, or navigating intersections---where multiple distinct trajectories may be equally appropriate. Despite these advantages, the majority of contemporary multimodal methods remain dependent on imitation learning frameworks. Such approaches learn from a limited set of demonstrated expert trajectories, and due to the lack of strategy diversity of ground-truth trajectories, often yield predictions that are homogenized, and deficient in behavioral diversity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In response to these shortcomings, several alternative strategies have been proposed. A series of works incorporates generative models, such as diffusion processes, to capture a broader distribution of plausible trajectories. However, many of these methods do not explicitly supervise the generative denoising process, still relying heavily on behavior cloning objectives. As a result, they remain susceptible to mode collapse. Another paradigm represents a further shift, depending entirely on generative models for trajectory planning and abandoning the use of imitation learning. While these methods benefit from generative models, they introduce new challenges: the stochasticity in noise initialization can lead to high-variance predictions, and the absence of a mechanism for hard constraint integration, such as obstacle avoidance or compliance with traffic rules, compromises the safety and interpretability of generated trajectories.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these limitations, we propose CATG, a novel trajectory generation framework based on flow matching that completely eliminates imitation learning while enabling flexible injection of explicit constraints into the generative process.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(1\) Novel generative framework. We introduce CATG, a multimodal trajectory generator built upon flow matching. Unlike conventional methods, CATG eliminates the reliance on imitation learning while supporting diverse and flexible conditional controls.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(2\) Constraint-guided generation. We explicitly integrate feasibility and safety constraints into the generative process through a progressive mechanism: prior-informed anchor design is used to construct constraint-guided probability flows, and energy-based guidance further steers trajectories toward feasible regions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(3\) Reward-conditioned controllability. We treat environmental reward signals as conditional inputs, enabling controllable trade-offs between aggressive and conservative driving styles during inference.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

CATG is extensively evaluated on the ICCV NAVSIM V2 End-to-End Driving Challenge, where it demonstrates superior planning accuracy and robust generalization to out-of-distribution data. When combined with an open-source scoring model, CATG achieves an EPDMS score of 51.31, competitive with state-of-the-art alternatives.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Preliminary", "weight": 1.0} -->

Let ${\mathbb{R}}^{d}$ denote the data space, two important objects we use in this paper are: the probability density path $p$: ${{\lbrack 0,1\rbrack} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}_{> 0}$, which is a time dependent probability density function i.e., ${\int{p_{t}{(x)}{dx}}} = 1$, and a time-dependent vector field, $v:{{{\lbrack 0,1\rbrack} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{d}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Preliminary", "weight": 1.0} -->

A vector field $v_{t}$ can be used to construct a time-dependent diffeomorphic map, called a flow, $\phi:{{{\lbrack 0,1\rbrack} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{d}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Preliminary", "weight": 1.0} -->

And, we can model the vector field $v_{t}$ with a neural network, $v_{t}{(t;\theta)}$. Let $X_{1}$ denote a random variable distributed according to an unknown data distribution $\pi_{1}$. We assume that we only have access to data samples from $\pi_{1}$, but not to the density function itself. Furthermore, we let $\pi_{0}$ be a simple distribution, such as a standard normal distribution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Flexible conditioning signal", "weight": 1.0} -->

We followed the Transfuser as our perception backbone. For flow matching progress, we sample $X_{0}$ from a standard Gaussian distribution and normalize the target trajectory $X_{1}$ to the range $\lbrack{- 1},{+ 1}\rbrack$. CATG constructs a flow with the starting point as $X_{0}$ and the endpoint as$X_{1}$. Then, we apply positional encoding to $X_{t}$ and utilize a Unet Encoder to encode $X_{t}$ into a feature $F_{X_{t}}$. Subsequent to the CATG perception module, CATG obtains the agent's query $Q_{ag}$, ego query $Q_{eg}$, and BEV feature $F_{B}$. In a separate preprocessing step, the BEV map segmentation result is first converted into a binary road map $M_{0,1}$ and then fused with BEV grid positional encoding $Pos_{B}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Flexible conditioning signal", "weight": 1.0} -->

Finally, CATG fuses the feature $F_{X_{t}}$ with all these elements ($Q_{ag}$, $Q_{eg}$, $F_{B}$ and $M_{0,1}$) through multiple layers of cross-attention as shown in Fig. 2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Flexible conditioning signal", "weight": 1.0} -->

\(1\) Trajectory anchor: CATG treat pre-clustered trajectory anchors as high-level abstractions of driving modes. CATG first constructs a trajectory vocabulary $vocab_{anchor}$ of size 8,192 by applying FPS (farthest-point sampling) over the entire training dataset. CATG is trained in a classifier-free guidance manner, where driving anchors are incorporated as conditional signals to guide trajectory generation. During training, the anchor most similar to the GT trajectory is utilized as the conditional signal, which is determined by DTW distance between trajectory vocabulary and GT trajectory. At inference time, a pre-trained scoring model, GTRS (with a V2-99 backbone), is employed to select the top-100 anchors with the highest likelihood, which subsequently serve as conditional inputs for generating diverse and compliant trajectories.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Flexible conditioning signal", "weight": 1.0} -->

\(2\) Target point: During training, CATG takes the endpoint of the GT trajectory as the conditional signal. During testing, in contrast, the endpoint of the anchor obtained from a scoring model serves as the conditional control signal.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Flexible conditioning signal", "weight": 1.0} -->

\(3\) Driving command: The driving command is also a type of control signal. CATG converts the command types in NAVSIM into a one-hot encoding for use as a conditional signal.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

A significant challenge in generative models is the lack of interpretability in their intermediate representations, posing difficulties for directly constraining the outputs. Specifically in the NAVSIM V2 challenge, constraining the generated trajectories to satisfy the Driving Area Compliance (DAC) metric proved highly challenging. Unlike constraints such as inter-agent collision avoidance which can be integrated by using vehicle distances as conditional signals, as seen in Diffusion-Planner, road geometry is far more complex. Therefore, in the following discussion, we will primarily focus on constraining trajectories to satisfy road compliance. However, it is noteworthy that our method can also be adapted to other types of constraints. To address this, we introduced three more direct and efficient methods for constraining the generation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

Since the formulation above indicates that the generated state $X_{t + 1}$ at the next timestep is determined by the intermediate variable $X_{t}$ and the velocity field $v_{t}$, a compelling hypothesis arises: could one constrain the generation process by imposing constraints on these two quantities ?

<!-- chunk {"id": "body-0021", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

\(1\) Constraining velocity field $v_{t}$ (CVF): Based on the road segmentation result, a trajectory $X_{1}^{C}$ that satisfying the DAC constraint is first selected from trajectory vocabulary $vocab_{anchor}$. Subsequently, for a given Gaussian sample $X_{0}$ as the flow's starting point, the ideal velocity field that leads to trajectory $X_{1}^{C}$ can be computed.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

CATG leverages this precomputed field $v_{t}^{c}$ to correct the potentially biased velocity field $v_{t}$ predicted by the model. Consequently, we propose the concept of a synthetic velocity field $v_{t}^{^{\prime}}$, which is a combination of the model predicted velocity field $v_{t}$ and the precomputed one $v_{t}^{c}$ during the sampling process as shown in Fig.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

\(2\) Constraining intermediate variables $X_{t}$ (CIV): A flow generated by a model-predicted velocity field often deviates from the ideal, leading to a final sample that fails to meet constraints. This flow can be discretized into a series of intermediate variables $X_{0},\ldots,X_{t},\ldots,X_{1}$; Therefore, if these intermediate variables can be effectively constrained, the final generated outcome can consequently be controlled. However, correcting $X_{t}$ at every timestep is inefficient. Instead, inspired, CATG addresses this by correcting the flow at its origin. It replaces the initial Gaussian random sample $X_{0}$ with an anchor $X_{1}^{C}$ selected from the trajectory vocabulary $vocab_{anchor}$ as shown in Fig. 1 (b), which complies with the DAC constraint, even though this anchor might perform poorly on other evaluation metrics. However, CATG can refines this anchor to make it more reasonable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

As shown in Fig. 2, this approach of starting from a DAC-compliant anchor enables the model to produce more plausible trajectories.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Constraint-Aware Trajectory Generation", "weight": 1.0} -->

\(3\) Constraint-Aware Training (CAT): In contrast to Diffusion-Planner, which only introduces energy term during inference, we incorporate constraints into the training phase by encoding them as an energy function. When trajectory are sampled along the direction of ascending energy, they exhibit a higher probability of satisfying the constraints as shown in Fig. 1 (c). Specifically, the DAC constraint can be represented by computing a Euclidean Signed Distance Field. The energy of a trajectory decreases as it moves closer to the road boundary, penalizing undesirable deviations. We follow the Energy Matching framework for model training. A two-stage procedure is employed, the first stage trains the Flow Matching process, and the second stage trains the Energy Matching process.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reward as condition", "weight": 1.0} -->

To control trajectory aggressiveness at inference time, CATG utilizes an EP (ego process) score as a conditioning signal. This score is derived by evaluating each GT trajectory in the NavTrain set within the NAVSIM simulator. By setting the EP condition to 1 during inference, the model is encouraged to produce more aggressive driving behavior.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments Setup", "weight": 1.0} -->

Our model is trained in two stages. The first stage of training encompasses the Flow Matching process, the perception module, and the map segmentation module. It was conducted with a batch size of 64, a learning rate of $2 \times 10^{- 4}$, and trained for 90 epochs by using NavTrain split. The second stage of training adhered to the Energy Matching framework, focusing solely on fine-tuning the Flow Matching process. This stage used a batch size of 64, a learning rate of $2 \times 10^{- 4}$, and trained for 10 epochs by using NavTrain split. During inference, CATG generates 100 candidate trajectories with 100 sampling steps.These candidates and trajectory vocabulary $vocab_{anchor}$ are then ranked by an open-source, pre-trained GTRS scorer model (with a V2-99 backbone) to select the most plausible trajectory as the final output.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments result", "weight": 1.0} -->

We present our proposed CATG architecture's results as shown in Tab. 1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments result", "weight": 1.0} -->

drivable area compliance stage one

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments result", "weight": 1.0} -->

driving direction compliance stage one

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments result", "weight": 1.0} -->

traffic light compliance stage one

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments result", "weight": 1.0} -->

time to collision within bound stage one

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments result", "weight": 1.0} -->

two frame extended comfort stage one

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments result", "weight": 1.0} -->

drivable area compliance stage two

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments result", "weight": 1.0} -->

driving direction compliance stage two

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments result", "weight": 1.0} -->

traffic light compliance stage two

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments result", "weight": 1.0} -->

time to collision within bound stage two

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments result", "weight": 1.0} -->

two frame extended comfort stage two

<!-- chunk {"id": "body-0039", "role": "body", "section": "Limitation", "weight": 1.5} -->

Sampling trajectories with 100 steps remains computationally expensive. Nevertheless, accelerating this process may lead to a degradation in trajectory quality. Therefore, a promising direction for future work is to enhance sampling efficiency while preserving the quality of the generated trajectories.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presents an end-to-end planner that leverages flow matching. Our approach is capable of incorporating flexible conditional signals to control trajectory generation. Furthermore, we innovatively propose three distinct strategies to enforce explicit constraints throughout the generation process. Experimental results presented in Tab. 1 demonstrate that our framework achieves a EPDMS of 51.31.
