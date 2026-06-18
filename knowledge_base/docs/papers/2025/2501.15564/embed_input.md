<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Diffusion-Based Planning for Autonomous Driving with Flexible Guidance

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Achieving human-like driving behaviors in complex open-world environments is a critical challenge in autonomous driving. Contemporary learning-based planning approaches such as imitation learning methods often struggle to balance competing objectives and lack of safety assurance,due to limited adaptability and inadequacy in learning complex multi-modal behaviors commonly exhibited in human planning, not to mention their strong reliance on the fallback strategy with predefined rules. We propose a novel transformer-based Diffusion Planner for closed-loop planning, which can effectively model multi-modal driving behavior and ensure trajectory quality without any rule-based refinement. Our model supports joint modeling of both prediction and planning tasks under the same architecture, enabling cooperative behaviors between vehicles. Moreover, by learning the gradient of the trajectory score function and employing a flexible classifier guidance mechanism, Diffusion Planner effectively achieves safe and adaptable planning behaviors. Evaluations on the large-scale real-world autonomous planning benchmark nuPlan and our newly collected 200-hour delivery-vehicle driving dataset demonstrate that Diffusion Planner achieves state-of-the-art closed-loop performance with robust transferability in diverse driving styles.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving as a cornerstone technology, is poised to usher transportation into a safer and more efficient era of mobility. The key challenge is achieving human-like driving behaviors in complex open-world environment, while ensuring safety, efficiency, and comfort. Rule-based planning methods have demonstrated initial success in industrial applications, by defining driving behaviors and establishing boundaries derived from human knowledge. However, their reliance on predefined rules limits adaptability to new traffic situations, and modifying rules demands extensive engineering effort. In contrast, learning-based planning methods acquire driving skills by cloning human driving behaviors from collected datasets, a process made simpler through straightforward imitation learning losses. Additionally, the capabilities of these models can potentially be enhanced by scaling up training resources.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though promising, current learning-based planning methods still face several limitations. Firstly, human drivers often exhibit multi-modal behaviors in planning scenarios. Existing methods that rely on behavior cloning lack a guarantee of fitting such complex data distributions, even when utilizing large transformer-based model architecture or sampling multiple trajectories. Secondly, when encountering out-of-distribution (OOD) scenarios, directly using model output may result in low-quality planning outcomes, forcing many methods to fall back on rule-based approaches for trajectory refinement optimization or filtering (Vitelli et al. Huang et al., ), inevitably facing the same inherent limitations associated with rule-based methods. Thirdly, imitation learning alone is inadequate to capture the vast diversity of driving behaviors required for autonomous driving. For example, penalizing unsafe planning via auxiliary loss, as employed in existing methods (Bansal et al. Cheng et al., ), often results in multi-objective conflicts and poor safety performance due to the lack of learning signals that can teach the agent to recover from mistakes (Zheng et al. Chen et al., ). Additionally, well-trained models may be difficult to adapt behaviors to meet specific needs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this study, we discover that diffusion model possesses huge potential to address the aforementioned issues. Its ability to model complex data distributions allows for effective capturing of multi-modal human driving behavior. Additionally, the high-quality generation capability of the diffusion model also provides opportunities for improving the output trajectory quality through appropriate structural design, removing the reliance on rule-based refinement. The best part of diffusion lies in its flexible guidance mechanism, which allows adaptation to various planning behavioral needs without additional training. Inspired by these observations, we introduce a novel learning-based approach, Diffusion Planner, which pioneers the use of diffusion models for enhancing closed-loop planning performance without any rule-based refinement. Diffusion Planner is realized by learning the gradient of vehicles' trajectory score function to model the multi-modal data distribution, and further enables personalized planning behavior adaptation through a classifier guidance mechanism. Specifically, we propose a new network architecture built upon the diffusion transformer. The diffusion loss is employed to jointly train both prediction and planning tasks within the same architecture, enabling cooperative behaviors between vehicles without the need for additional loss functions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the versatility of classifier guidance is further demonstrated by its ability to modify the planning behavior of the trained model, such as enhancing safety and comfort, or controlling the vehicle's speed. The differentiable classifier score can be computed in parallel and is flexible for combination, without requiring additional training. Evaluation results on the large-scale real-world autonomous planning benchmark nuPlan demonstrate that Diffusion Planner achieves state-of-the-art closed-loop performance among learning-based baselines, comparable to or even surpassing rule-based methods, directly using the model's output without any additional post-processing. By appending a existing post-processing module to the model, we further achieved state-of-the-art performance among all baselines. Additionally, we collected $200$ hours of long-term delivery-vehicle driving data in various city-driving scenarios that further validate the transferability and robustness of the model in diverse driving styles.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, we are the first to fully harness the power of diffusion models with a specifically designed architecture for high-performance motion planning, without overly reliant on rule-based refinement.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We achieve state-of-the-art performance on the real-world nuPlan dataset, generating more robust and smoother trajectories compared to the baselines.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that our model can achieve personalized driving behavior at runtime by utilizing a flexible guidance mechanism, which is a desirable feature for real-world applications.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We have collected and evaluated a new 200-hour delivery-vehicle dataset, which is compatible with the nuPlan framework, and we will open-source it.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Autonomous Driving and closed-loop Planning", "weight": 1.0} -->

The primary objective of autonomous driving is to allow vehicles to navigate complex environments with minimal human intervention, where a critical challenge is closed-loop planning. Unlike open-loop planning or motion prediction (Ngiam et al. Zhou et al., ), which only involves decision making that adapts to static conditions, closed-loop planning requires a seamless integration of real-time perception, prediction, and control. Vehicles must continuously assess their surroundings, predict the behavior of other neighboring vehicles, and implement precise maneuvers. The dynamic nature of real-world driving scenarios, combined with uncertainty in sensor data and environmental factors, makes closed-loop planning a formidable task.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Diffusion Model and Guidance Schemes", "weight": 1.0} -->

Diffusion Model. Diffusion Probabilistic Models (Sohl-Dickstein et al. Ho et al., ) are a class of generative models that generate outputs by reversing a Markov chain process known as the forward diffusion process.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Diffusion Model and Guidance Schemes", "weight": 1.0} -->

which gradually adds Gaussian noise to generate a series of noised data from ${\mathbf{x}}^{}$ to ${\mathbf{x}}^{(t)}$ with $t \in {\lbrack 0,1\rbrack}$. $\sigma_{t} > 0$ is a variance term that controls the introduced noise and $\alpha_{t} > 0$ is typically defined as $\alpha_{t} = \sqrt{1 - \sigma_{t}^{2}}$, ensuring ${\mathbf{x}}^{(t)}\rightarrow{\mathcal{N}{(0,\mathbf{I})}}$, as $t\rightarrow 1$. The reversed denoising process of Eq.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diffusion Model and Guidance Schemes", "weight": 1.0} -->

Classifier Guidance. Classifier guidance is a technique used to generate preferred data by guiding the sampling process with a classifier $\mathcal{E}_{\phi}{({\mathbf{x}}^{(t)},t)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Diffusion Model and Guidance Schemes", "weight": 1.0} -->

In autonomous driving, this approach offers greater flexibility compared to rule-based refinement because it directly improves the model's inherent ability, rather than overly relying on sub-optimal post-processing that requires significant human effort and targeted data collection.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Methodology", "weight": 1.0} -->

In this section, we redefine the planning task as a future trajectory generation task, which jointly generates the ego vehicle's planning and the prediction of neighboring vehicles. We then introduce the Diffusion Planner, a novel approach that leverages the expressive and flexible diffusion model for enhanced autonomous planning. Lastly, we demonstrate how the guidance mechanism in diffusion models can be utilized to align planning behavior with safe or human-preferred driving styles.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Task Redefinition", "weight": 1.0} -->

Autonomous driving requires considering the close interaction between the ego and neighboring vehicles, resulting in a cooperative relationship between planning and motion prediction tasks. Supervising the future trajectories of neighboring vehicles has been shown to be helpful to enhance the ability of closed-loop planning models to handle complex interaction scenarios. For real-world deployment, motion prediction can also enhance safety by providing more controllable measures, facilitating the implementation of the system. Consequently, the trajectories of neighboring vehicles have become crucial privileged information for model training. However, the common approaches that use a dedicated sub module or additional loss design (Cheng et al. Huang et al., ) to capture privileged information limit their modeling power during training and also lead to a more complex framework.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Task Redefinition", "weight": 1.0} -->

In this work, we address this issue by collectively considering the status of key participants in the driving scenario and jointly modeling the motion prediction and closed-loop planning tasks as a future trajectory generation task. Specifically, given conditions $\mathbf{C}$, which include current vehicle states, historical data, lane information, and navigation information, our goal is to generate future trajectories for all key participants simultaneously, enabling the modeling of cooperative behaviors among them. However, this joint modeling of complex distributions is challenging to solve with a simple behavior cloning approach.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Task Redefinition", "weight": 1.0} -->

where we use superscripts with parentheses to represent the timeline of diffusion denoising, and regular superscripts to indicate the timeline of the future trajectory, which contains $\tau$ time steps. For each state $x$, we only consider the coordinates and the sine and cosine of the heading angle, which are sufficient for the downstream LQR controller. We select the nearest $M$ neighboring vehicles to predict their possible future trajectories.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Task Redefinition", "weight": 1.0} -->

where the goal is to recover the data distribution from noisy data. We can get the score function as ${\mathbf{s}}_{\theta} = {{({{\alpha_{t}\mu_{\theta}} - {\mathbf{x}}^{(t)}})}/\sigma_{t}^{2}}$ and apply it during the denoising process. The joint prediction of multiple vehicles is similar to motion prediction and traffic simulation tasks, but we focus more on the ego vehicle's closed-loop planning performance and real-time deployment. We will introduce the specific designs as follows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

Diffusion Planner is a model based on the DiT architecture, with a core design focusing on the fusion mechanism between noised future vehicle trajectories $\mathbf{x}$ and conditional information $\mathbf{C}$. Figure provides an overview of the complete architecture. A detailed description of these interaction and fusion modules is provided as follows.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

Vehicle Information Integration. In the first step, the future vehicle trajectory $\mathbf{x}$ is concatenated with the current state of each vehicle, represented as $x^{0} = {\lbrack x_{ego}^{0},x_{neighbor1}^{0},\ldots,x_{{neighbor}_{M}}^{0}\rbrack}^{T}$. This concatenation acts as a constraint to guide the model, simplifying the planning task by providing a clear starting point. Notably, velocity and acceleration information for the ego vehicle is excluded, which has been shown to enhance closed-loop performance, as highlighted in previous works (Cheng et al. Li et al., ). Integration of the information from different vehicles during model execution is achieved through multi-head self-attention mechanisms.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

Historical Status and Lane Information Fusion. The historical status of neighboring vehicles and lane information is represented using vectors. Specifically, each neighboring vehicle is represented as ${\mathbf{S}}_{neighbor} \in {\mathbb{R}}^{L \times D_{neighbor}}$, and lanes as ${\mathbf{S}}_{lane} \in {\mathbb{R}}^{P \times D_{lane}}$, where $L$ refers to the number of past timestamps, and $P$ indicates the number of points per polyline. $D_{neighbor}$ contains data such as vehicle coordinates, heading, velocity, size, and category, while $D_{lane}$ provides lane details such as coordinates, traffic light status, and speed limits. Since these vectors are information-sparse, directly fusing them would make training challenging. To address this, we use MLP-Mixer network to extract information-dense representations. Compared to existing work (Huang et al. Cheng et al., ) that uses complex structural designs, we offer a more unified and simplified solution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

This is achieved by iteratively passing the vectors through the MLP mixing layers, which operate on both the vector and feature dimensions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

We use two separate MLP-Mixer networks for neighboring vehicles and lanes. Here, $\mathbf{S}$ represents the features for each neighboring vehicle or lane. After passing through multiple mixing layers, we apply pooling on the final output along the vector dimension. We also consider the static objects information ${\mathbf{S}}_{static} \in {\mathbb{R}}^{D_{static}}$, where $D_{static}$ includes data such as coordinates, heading, size, and category. For this, we use an MLP to extract the representation. Finally, we concatenate all representations and feed them into a vanilla transformer encoder for further aggregation, resulting in the encoder representation ${\mathbf{Q}}_{f}$. The fusion of ${\mathbf{Q}}_{f}$ with $\mathbf{x}$ proceeds as follows: f

<!-- chunk {"id": "body-0026", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

where MHCA donate multi-head cross-attention.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Diffusion Planner", "weight": 1.0} -->

Navigation Information Fusion. Navigation information is crucial for autonomous driving planning, as it provides essential guidance on the intended route, enabling the vehicle to make informed decisions. In the nuPlan benchmark, navigation information is represented as a set of lanes along a route, ${\mathbf{S}}_{route} \in {\mathbb{R}}^{{({K \times P})} \times D_{route}}$, where $K$ denotes the number of route lanes, and $D_{route}$ contains only coordinate information. We first employ an MLP-Mixer network, as described in equation, to extract the essential guidance representations ${\mathbf{Q}}_{n}$. ${\mathbf{Q}}_{n}$ is then added to the diffusion timestep condition ${\mathbf{Q}}_{t}$ and applied through an adaptive layer norm block to guide trajectory generation across all tokens.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Enforcing versatile and controllable driving behavior is crucial for real-world autonomous driving. For example, vehicles must ensure safety and comfort while adjusting speeds to align with user preferences. Thanks to its close relationship to Energy-Based Models, diffusion model can conveniently inject such preferences via classifier guidance. It can steer the model outputs via gradient surgery during inference, offering significant potential for customized adaptation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Specifically, given the original driving behavior $q_{0}{({\mathbf{x}}^{})}$, we aim to encode additional guidance to reinforce some preferred behavior upon the existing behavior $q_{0}$. This operation can be formulated as generating a target behavior: ${p_{0}{({\mathbf{x}}^{})}} \propto {q_{0}{({\mathbf{x}}^{})}e^{- {\mathcal{E}{({\mathbf{x}}^{})}}}}$, where $\mathcal{E}{({\mathbf{x}}^{})}$ can be some form of energy function that encodes safety or preferred behavior. As mentioned in Section 3.2, the gradient of the intermediate energy is employed to adjust the original probability score, promoting the generation of trajectories within the target distribution. This process often necessitates an additional trained classifier to provide an accurate approximation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

However, diffusion posterior sampling (Chung et al. Xu et al., ) offers a training free method that only uses the trained diffusion model $\mu_{\theta}$ in Eq.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

One restriction of this method is that Eq. needs to use a pre-defined differentiable energy function $\mathcal{E}{( \cdot )}$ to calculate the guidance energy. Fortunately, in autonomous driving scenarios, many trajectory evaluation protocols can be defined using differentiable functions. Next, we briefly describe some applicable energy functions that can be used to customize the planning behavior of the model, more details are shown in Appendix C.3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Target speed maintenance: The speed difference is used as the energy, calculated by comparing the planned average speed with the set target speed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Comfort: The energy function is calculated by measuring the amount by which the vehicle's state exceeds the predefined limits.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Collision avoidance: The signed distance between the ego vehicle and neighboring vehicles is computed at each timestamp.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Staying within drivable area: The distance the ego vehicle deviates outside the lane at each time step is calculated.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Planning Behavior alignment via Classifier Guidance", "weight": 1.0} -->

Additionally, this training-free approach supports flexible combinations during inference time, providing a solution for controllable trajectory generation in complex scenarios. For example, as shown in Figure, under collision guidance alone, the ego vehicle veers off the road to avoid a rear-approaching vehicle. However, when drivable guidance is added, the vehicle stays on the road while maintaining safety. For more case studies, please refer to Section 5.1 and the Appendix B.2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Practical Implementation for Closed-Loop Planning", "weight": 1.0} -->

Data augmentation can help alleviate the out-of-distribution issue and is widely used in planning. Before training, we add random perturbations to the current state. Then, interpolation is applied to create a physically feasible transition, enabling the model to resist perturbations and regress to the ground-truth trajectory. After that, we transform the data from the global coordinate system into an ego-centric formulation through coordinate transformation. Considering the significant difference between the longitudinal and lateral distances traveled by the vehicle, z-score normalization is used to ensure the mean of the data distribution is close to zero, thereby further stabilizing the training process. During inference, DPM-Solver is employed to achieve faster sampling, while low-temperature sampling enhances determinism in the planning process. We can complete trajectory planning for the next $8$ seconds at $10$ Hz, along with predictions for neighboring vehicles, with an inference frequency of approximately $20$ Hz. Please see Appendix C for implementation details.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Evaluation Setups. We conduct extensive evaluations on the large-scale real-world autonomous planning benchmark, nuPlan, to compare Diffusion Planner with other state-of-the-art planning methods. The and -hard benchmarks are utilized, with all experimental results tested in both closed-loop non-reactive and reactive modes. The final score is calculated as the average across all scenarios, ranging from $0$ to $100$, where a higher score indicates better algorithm performance. To further validate the algorithm's performance across diverse driving scenarios and with vehicles exhibiting different driving behaviors, we collected 200 hours of real-world data using a delivery vehicle from Haomo.AI. Unlike nuPlan, the delivery vehicle demonstrates more conservative planning behavior and operates in bike lanes, which involve dense human-vehicle interactions and unique traffic regulations. The collected data were integrated into the nuPlan framework, and the same evaluation metrics were applied in closed-loop simulations, as detailed in Appendix D.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baselines. The baselines are categorized into three groups: Rule-based, Learning-based, and Hybrid, which incorporate additional refinement to the outputs of the learning-based model. To enable a more comprehensive comparison, we utilize an existing refinement module, which applies offsets to the model outputs and scores all trajectories. Without any parameter tuning, we integrate this module as post-processing for the Diffusion Planner (Diffusion Planner w/ refine.). We compare the Diffusion Planner against the following baselines, with more implementation details provided in Appendix C.4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

IDM: A classic rule-based method implemented by nuPlan.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

PDM: The first-place winner of the nuPlan challenge offers a rule-based version that follows the centerline (PDM-Closed), a learning-based version conditioned on the reference line (PDM-Open), and a hybrid approach that combines both (PDM-Hybrid).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

UrbanDriver: A learning-based method using policy gradient optimization and implemented by nuPlan.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

GameFormer: Modeling ego and neighboring vehicle interactions using game theory (GameFormer w/o refine.), followed by rule-based refinement.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

PlanTF: A state-of-the-art learning-based method built on a transformer architecture, exploring various designs suitable for closed-loop planning.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

PLUTO: Building on PDM-Open, a complex model with contrastive learning enhances environmental understanding (PLUTO w/o refine.), followed by post-processing.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

Main Results. Evaluation results on the nuPlan benchmark are presented in Table. The Diffusion Planner achieves state-of-the-art performance across more benchmarks compared to all learning-based baselines. With the addition of post-processing, Diffusion Planner w/ refine. outperforms hybrid and rule-based baselines, achieving scores that even surpass human performance. This is due to our model's ability to output high-quality trajectories, which are further enhanced by post-processing. Notably, compared to the transformer-based PlanTF and PLUTO, Diffusion Planner leverages the power of diffusion to achieve better performance. GameFormer, which models the interactions between the ego vehicle and neighboring vehicles using game theory, exhibits limited model capabilities, making it overly reliant on rule-based refinements. We further present the planning results on delivery-vehicle driving dataset as shown in Table. PDM, GameFormer, and PLUTO include certain designs specifically tailored to the nuPlan benchmark, which limits their ability to transfer to delivery-vehicle driving tasks, resulting in a drop in performance. In contrast, Diffusion Planner demonstrates strong transferability across different driving behaviors.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also compared works that utilize diffusion for planning, as shown in Table in Appendix B.1. The Diffusion Planner better leverages the powerful capabilities of diffusion and is more practical.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

Qualitative Results. To further demonstrate the capabilities of learning-based models, we show the trajectory generation results of representative baselines (without refinement) as shown in Figure. Diffusion Planner shows high-quality trajectory generation, with accurate predictions for neighboring vehicles and smooth ego planning trajectories that reasonably account for the speed of the vehicle ahead, demonstrating the advantages of joint modeling of both prediction and planning tasks. More closed-loop planning results are shown in Appendix A. In contrast, GameFormer w/o refine produces less smooth trajectories and inaccurate predictions for neighboring vehicles, which explains why it heavily relies on refinement. Although PlanTF and PLUTO w/o refine. sample multiple trajectories at once, most of them are of low quality.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Empirical Studies of Diffusion Planner Properties", "weight": 1.0} -->

Multi-modal Planning Behavior. We selected an intersection scenario and performed multiple inferences without low temperature sampling from the same initial position to obtain different possible outputs, in order to evaluate the model's ability to fit multi-modal driving behaviors. As shown in Figure, without navigation information, the vehicle can exhibit three distinct driving behaviors---left turn, right turn, and straight ahead---with clear differentiation. When navigation information is provided, the model accurately follows it to make a left turn, demonstrating the diffusion model's ability to fit driving behaviors with varying distributions and its capacity for switching between them.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Empirical Studies of Diffusion Planner Properties", "weight": 1.0} -->

Flexible guidance mechanism. Based on the trained Diffusion Planner model, different types of classifier guidance, as described in Section 4.3, are added during inference time without requiring additional training. We present two cases to demonstrate the effectiveness of guidance and its flexible composability, as shown in Figure. 1) For target speed setting, we masked all lane speed limit information to prevent it from influencing the model's planning, ensuring that speed adjustments are made solely through guidance. As a result, the model exhibited a lower speed without guidance. By setting the speed between $10\text{m/s}$ and $14\text{m/s}$, the model closely matches the desired speed range while maintaining smooth speed transitions. 2) For comfort guidance, we effectively alleviate discomfort and can even use it simultaneously with collision guidance. We also provide additional case studies on collision and drivable guidance, as shown in Appendix B.2, as well as cases demonstrating the flexible combination of collision and drivable guidance, as illustrated in Figure.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Design Choices for training. We demonstrate the effectiveness of key components of our method: data processing, the handling approach of ego current state, and the number of predicted vehicles. 1) We ablate the model's performance without using z-score normalization (w/o z-score norm), as well as without data augmentation (w/o augmentation), or by only perturbing the current state without applying interpolation to future trajectories (w/o interpolation). The results are summarized in Table LABEL:tab:ablationtraining. For the w/o z-score norm variant, even with ego-centric transformation, the data range remains large, making it difficult for the model to fit the distribution. The w/o augmentation variant faces out-of-distribution issues, leading to poor performance. Results also show that future trajectory interpolation is essential compared to perturbing only the current state. 2) We analyze the impact of the ego vehicle's current state on the model. Retaining velocity, acceleration, and yaw rate (w/ ego state) may lead to learning shortcuts, resulting in decreased planning capability.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

While a state dropout encoder (w/ SDE) mitigates this, directly discarding the information is more effective. Additionally, the w/o current state shows that adding current state information to the decoder improves planning capability. 3) We also ablate the choice of the number of $M$. Figure shows that including too many neighboring vehicles in the decoder introduces noise, affecting the performance of the ego vehicle. However, most choices still outperform PlanTF.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Design Choices for Inference. We sweep two hyperparameters: the number of denoise steps and the magnitude of low-temperature sampling, as shown in Figure. Low temperature helps improve the stability of the output trajectories. Additionally, the model leverages DPM-Solver to achieve efficient denoising and remains robust across different step counts. We report the detailed parameter selection in Table.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We propose Diffusion Planner, a learning-based approach that fully exploits the expressive power and flexible guidance mechanism of diffusion models for high-quality autonomous planning. A transformer-based architecture is introduced to jointly model the multi-modal data distribution in motion prediction and planning tasks through a diffusion objective. Classifier guidance is employed to align planning behavior with safe or user preferred driving styles. Diffusion Planner achieves state-of-the-art closed-loop performance without relying on any rule-based refinement on the nuPlan benchmark and a newly collected 200-hour delivery-vehicle driving dataset, demonstrating strong adaptability across diverse driving styles. Due to space limit, more discussion on limitations and future direction can be found in Appendix E.
