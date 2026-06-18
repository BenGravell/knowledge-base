<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FactoryNet: A Large-Scale Dataset Toward Industrial Time-Series Foundation Models

Topics include Industrial time series, Foundation models, Datasets, Anomaly detection, Cross-embodiment transfer, Robotic telemetry, Schema design, Factory data.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces FactoryNet, a large industrial time-series corpus built around a shared Setpoint-Effort-Feedback-Context schema for actuated systems. The dataset is designed to make pretraining and transfer across machines possible, with annotated anomalies, healthy baselines, counterfactual pairs, and early evidence of cross-embodiment transfer.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce the first universal pretraining corpus for industrial time-series data: FactoryNet. 51M datapoints across 23k end-to-end task executions (13.3k real, 9.8k synthetic) on six embodiments, unified by a shared schema that enables robust zero-shot cross-embodiment transfer and highly parameter-efficient anomaly detection. We introduce a novel schema: Setpoint, Effort, Feedback, Context (S-E-F-C) underlying the whole pipeline that maps any actuated system into a common representational frame. The corpus spans 27 annotated anomaly types alongside healthy baselines and counterfactual pairs across robotic manipulation and machining domains. Cross-embodiment transfer experiments yield positive results: under bias-aware metrics our model demonstrates fair cross-embodiment transfer capabilities on the evaluated source-target pair, while 24 schema-aligned signals achieves competitive anomaly detection performance compared to high-dimensional baselines. We release FactoryNet as a growing, multi-embodiment dataset to drive progress toward industrial foundation models.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The manufacturing sector accounts for approximately 15% of global GDP, relying heavily on the continuous operation of complex actuated machinery ). While predictive maintenance and process optimization present significant opportunities for machine learning, industrial AI remains largely confined to single-machine, bespoke deployments. Foundation models have transformed vision and language by pretraining on large, structurally coherent corpora, yet no analogous substrate exists for industrial time-series. The gap is not merely volume: existing anomaly detection and forecasting datasets record sensor outcomes without separating *commanded intent* from *measured response*. For actuated systems, learning transferable dynamics requires observing the full control loop from target trajectory through actuation effort to the resulting physical state. While partial solutions exist for specific machines (as discussed in Section 2), no unified open dataset provides this explicit decomposition across multiple embodiments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Every signal is mapped into the Setpoint-Effort-Feedback-Context (S-E-F-C) schema: a machine-agnostic signal taxonomy grounded in IEC 81346 functional classification that separates intent from outcome across arbitrary actuated systems. For physics-oriented modeling, S--E--F--C plays the role of a compact, structured interface for short rollouts: Setpoint and Context fix commanded intent and boundary conditions, while Effort and Feedback make *commanded versus realized* dynamics comparable as explicit prediction residuals rather than opaque reconstruction scores. Paired real and Isaac episodes under the same schema let sim-to-real mismatch be read as *forward-model error* under matched inputs, in line with the bias-aware transfer and phase-aware gap analyses.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Industrial Fault-Detection Datasets", "weight": 1.0} -->

The availability of open-source data in the manufacturing domain lags significantly behind other modalities. Most existing datasets focus on single-machine, run-to-failure scenarios or specific rotating machinery components. Canonical examples include the NASA C-MAPSS turbofan degradation benchmark and recent robotic datasets: voraus-AD provides 2,122 episodes of industrial robot recordings and AURSAD offers 2,045 episodes. However, these datasets are bounded in scale and lack an explicit control-loop structure mapping commands to outcomes. By unifying these sources alongside novel laboratory data under a standard control-theoretic decomposition, FactoryNet provides the largest open-source, fault-injected industrial robot dataset to date (see Table 1 for a comprehensive comparison with existing datasets).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Industrial Fault-Detection Datasets", "weight": 1.0} -->

Beyond single-component datasets, broader industrial anomaly detection benchmarks such as SKAB ), MetroPT, WADI and the Tennessee-Eastman process provide system-level multivariate time-series. Similarly, general-purpose time-series anomaly detection benchmarks like TSB-AD and TODS have driven algorithmic progress (e.g., Anomaly-Transformer ). However, these datasets record holistic system states without the explicit commanded-versus-measured structural decomposition necessary for learning robotic dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Foundation Models for Time-Series and Robotics", "weight": 1.0} -->

Current foundation model research diverges into two distinct tracks. In robotics, efforts such as Open X-Embodiment and DROID pool data across diverse kinematics to train generalizable, cross-embodiment behavioral policies. Simultaneously, in the structured time-series domain, models such as Chronos, TimesFM, Moirai, MOMENT, Timer, Lag-Llama, and TabPFN-TS leverage pretraining corpora to yield powerful zero-shot forecasters. However, because these TS-FMs are predominantly trained on web-scraped, financial, or ecological data, we hypothesize that they lack grounding in physical actuation and may struggle to disentangle static payload biases from actual dynamic behavior in industrial settings. FactoryNet is designed as a bridge between these two tracks: an industrial-scale, control-theoretically structured corpus for training and evaluating TS-FMs on complex dynamics across embodiments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Physics-Informed and Structured Dynamics", "weight": 1.0} -->

In parallel to data-driven forecasting, Physics-Informed Neural Networks (PINNs) and grey-box models incorporate known governing equations into the learning process. While these approaches excel in scenarios with well-defined partial differential equations, applying them to complex multi-joint robotic systems often requires residual-dynamics learning or structured priors. FactoryNet complements this literature by providing the empirical Setpoint-Effort-Feedback decomposition required to train and evaluate structured or physics-inspired models at scale.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The FactoryNet Dataset", "weight": 1.0} -->

FactoryNet v1.0 is the largest open-source industrial-robot time-series dataset containing labelled anomalies and organized around a control-theoretic schema. It comprises three pillars: real-world laboratory recordings, standardized open-source adaptations, and a synthetic generation pipeline. Because industrial data is sampled at high frequencies across many joints and sensors, 23k episodes yield a high-density, continuous corpus of the kind required to learn complex physical dynamics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dataset Composition", "weight": 1.0} -->

As detailed in Table 2 and Figure 2, the corpus encompasses multiple data streams. The laboratory track consists of novel recordings we collected from UR3 and KUKA industrial robotic arms executing three complex tasks: Pick & Place, Screwdriving, and Peg-in-Hole. We ingested and restructured existing high-quality open-source datasets (voraus-AD, AURSAD, and UMich CNC ) into our unified schema. The dataset is structured using a hierarchical taxonomy grounded in the IEC 81346 standard for industrial systems, allowing the schema to seamlessly integrate diverse modalities such as CNC milling centres and rotating machinery. A parallel synthetic track generated via NVIDIA Isaac Sim provides procedurally scaled data for model pretraining.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Dataset Composition", "weight": 1.0} -->

Our Lab (Real)
P&amp;P, Screw, Peg

<!-- chunk {"id": "body-0013", "role": "body", "section": "The S-E-F-C Signal Taxonomy: A Unified Vocabulary", "weight": 1.0} -->

The defining feature of FactoryNet is its control-theoretic structure. Most existing benchmarks simply log raw sensor streams, intrinsically tangling the controller's target variables with the machine's actual physical execution. This conflates cause and effect while suffering from vendor-specific naming conventions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The S-E-F-C Signal Taxonomy: A Unified Vocabulary", "weight": 1.0} -->

To resolve this, we employ embodiment-specific adapter scripts to programmatically map over 300 heterogeneous data columns into four standardized roles (machine-readable tables: Appendix B). These categories are: Setpoint (S) (commanded intent, e.g., target joint positions), Effort (E) (actuation energy expended, e.g., motor current/torque), Feedback (F) (measured physical outcome, e.g., actual positions), and Context (C) (environmental or static variables, e.g., payload mass).

<!-- chunk {"id": "body-0015", "role": "body", "section": "The S-E-F-C Signal Taxonomy: A Unified Vocabulary", "weight": 1.0} -->

This taxonomy allows a single dataloader to work across UR3, KUKA, and CNC machinery: a 6-DOF rotational arm and a 4-axis CNC gantry expose the same four roles, only with different axis counts and units. By enforcing this taxonomy, S-E-F-C acts as a unified vocabulary for cross-embodiment models, providing a principled inductive bias for learning the difference between expected dynamics and external disturbances. Signal availability varies by embodiment: KUKA (KSS 8.3) does not expose joint velocities, commanded TCP pose, or TCP force/torque via its RSI interface; these channels are marked absent in the S-E-F-C mapping (Appendix B).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

To reduce dependence on real-only data, FactoryNet includes a synthetic pipeline in NVIDIA Isaac Sim with procedural generation and domain randomization (mass, friction, controller gains), yielding 9799 Pick & Place episodes with aligned S-E-F-C metadata and matched healthy twins for controlled fault-deviation analysis. To ensure the synthetic pretraining corpus captures robust physical dynamics and helps bridge the sim-to-real gap, we employ extensive domain randomization across the procedurally generated UR5 Pick & Place episodes in NVIDIA Isaac Sim.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Mass Randomization: The payload (cube) mass is uniformly sampled per episode between $0.10$ and $0.30$ kg (with broader exploratory configurations allowing up to $0.80$ kg). Robot link masses remain fixed to isolate payload-driven dynamic variations and ensure baseline kinematic stability.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Surface Friction: We randomize the general Coulomb friction coefficient of the target object between $0.30$ and $0.50$ per episode. The end-effector gripper pad maintains a fixed, high-friction coefficient of $1.2$ to ensure stable grasps once contact is successfully established.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Controller Gains: To simulate variations in actuation force and mechanical compliance at the end-effector, the proportional gain ($K_{p}$) of the gripper is randomized uniformly in the range of $\lbrack 5000.0,12000.0\rbrack$. The UR5 arm's main joint PID controllers remain fixed to nominal values.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Sensor Noise Model: We inject artificial Gaussian noise into the simulated telemetry to mimic real-world sensor degradation, encoder quantization, and signal noise. Using a base standard deviation of $\sigma_{\text{base}} = 0.002$, noise is scaled across modalities: joint positions ($\sigma = 0.002$ rad), joint velocities ($\sigma = 0.02$ rad/s), and joint efforts/torques ($\sigma = 0.1$). Additionally, spatial perception noise is applied to the object's tracked state ($\sigma_{xy} = 0.002$ m, $\sigma_{z} = 0.001$ m).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Task and Geometric Variation: The task features procedural geometric and spatial variations to prevent policy overfitting. The target cube's physical dimensions (width, depth, and height) are independently randomized within specified bounds for every episode. Furthermore, the object's initial spawn position on the conveyor is continuously randomized within an $8 \times 8$ cm ($0.08$ m) bounding box relative to the nominal pick center.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Simulation Dynamics: The internal physics simulation engine operates at a fixed temporal step size of ${\Deltat} \approx 0.016667$ s (60 Hz). To align this synthetic track with the 100 Hz standard utilized by the physical laboratory recordings (see Section 3), the raw 60 Hz simulation telemetry undergoes temporal interpolation during the data ingestion pipeline.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Synthetic Pipeline and Sim-to-Real", "weight": 1.0} -->

Batch sim-to-real validation (pairing real and simulated episodes under the same RTDE-shaped schema, phase-aware gap metrics) is reported in Section 3.4.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Batch sim-to-real validation", "weight": 1.0} -->

We run sim2real rollouts in Isaac Sim 4.5.0 (headless Docker, PhysX) using the built-in UR3 USD asset and a position-control stack (ArticulationAction) with phase-consistent waypoint replay from real target_joint\_\* signals. The task is UR3 pick-and-place with a 10-phase structure (above_pick to return). Simulation steps at 240 Hz and logs at 10 Hz. Real episodes are exported from FactoryWave parquet to per-episode RTDE-shaped CSVs, converted to per-episode simulation configs, replayed in Isaac, and paired by episode ID/filename. Simulated logs preserve FactoryWave-compatible fields (joint\_\*, target_joint\_\*, joint_current\_\*, tcp\_\*, task_phase, and status/context fields). Gap metrics are computed phase-wise with time normalization/interpolation. Results of the gap analysis are shown in Table 3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Batch sim-to-real validation", "weight": 1.0} -->

An important source of residual pose discrepancy is end-effector mismatch: the Isaac setup used a Robotiq 2FG85-style gripper configuration, whereas the real FactoryWave episodes used an OnRobot 2FG14 gripper. Differences in tool geometry/TCP definition and mounting can bias absolute TCP and orientation metrics. We therefore interpret remaining TCP rotation spread conservatively and treat gripper-accurate tool calibration as future work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Faults and Anomalies", "weight": 1.0} -->

To support anomaly detection and robust control research, of the 9,114 lab episodes, approximately 40% are healthy and 60% contain injected faults across 27 anomaly types spanning three tasks: Pick & Place, Screwdriving, and Peg-in-Hole.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data Accessibility and Licensing", "weight": 1.0} -->

Novel laboratory and synthetic data are released under the MIT license; adapted open-source subsets retain their original licenses (CC-BY 4.0 or equivalent). The repository provides S-E-F-C Parquet files, metadata, and framework-native dataloaders at

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dataset Utility & Validation", "weight": 1.0} -->

To demonstrate that FactoryNet provides a viable substrate for both single-machine modelling and foundation model pretraining, we evaluate the dataset across standard industrial baselines and establish the open challenge of cross-embodiment transfer.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dataset Utility & Validation", "weight": 1.0} -->

Evaluation Protocol. Evaluation protocols are task-specific. For voraus-AD anomaly detection, we follow the official protocol of Brockmann et al.: training on 948 healthy episodes only, and testing on the 1,174-episode labelled set (419 healthy + 755 anomalous). In contrast, the TCN-Transformer forecasting experiments utilize a separate pretraining split (1,093 training / 137 validation, randomly sampled from all healthy episodes) to maximize observed dynamics. Confidence intervals for our S-E-F-C MLP are 95% bootstrap CIs computed over 1,000 resamplings of episode-level anomaly scores; CIs for unstructured baselines are reported as standard deviation across fault categories as published in Brockmann et al..

<!-- chunk {"id": "body-0030", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Anomaly Detection: MLP Architecture. The S-E-F-C MLP is a supervised regressor trained to predict motor torque from setpoint signals. Inputs: 18 Setpoint signals (setpoint_pos_0...5, setpoint_vel_0...5, setpoint_acc_0...5). Outputs: 6 Effort signals (effort_motor_torque_0...5). Anomaly score: per-episode mean absolute error (MAE) between predicted and true motor torque---higher error indicates anomaly. To maintain parity with standard anomaly detection protocols, the model is trained on healthy episodes only (948 episodes from voraus-AD).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Architecture: The network is constructed with three hidden layers consisting of 512, 256, and 128 units, respectively. We apply the Rectified Linear Unit (ReLU) activation function after each hidden layer. Dropout is not utilized in this architecture.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Training Details: The model is optimized using Adam (torch.optim.Adam) with an initial learning rate of $5 \times 10^{- 4}$, a weight decay ($L_{2}$ penalty) of $1 \times 10^{- 5}$, and a batch size of 4,096. The learning rate is decayed following a cosine annealing schedule. Models are trained for a maximum of 500 epochs, utilizing an early stopping criterion that halts training if the validation loss fails to improve for 30 consecutive epochs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

TCN-Transformer Architecture and Training. The TCN-Transformer comprises a 3-layer dilated Temporal Convolutional Network (kernel size 3) for local feature extraction, followed by a 2-layer Transformer encoder (4 attention heads, hidden dimension 64, feedforward dimension 128) for sequence modelling. The total parameter count is approximately 105,000. Training was conducted using the AdamW optimizer (learning rate $1 \times 10^{- 4}$) for 100 epochs. (Note: Due to the reduced parameter count, training is highly efficient on standard hardware.)

<!-- chunk {"id": "body-0034", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

The model predicts joint acceleration; Euler integration (${\Deltat} = 0.01$ s) yields position and velocity. Survival steps are computed as the first step at which per-joint position error exceeds 0.01 rad, averaged across all test episodes and joints.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

For the anomaly detection evaluation (Table 4), all unstructured baselines (1-NN, PCA, GANF, CAE, LSTM-VAE, HMM, and MVT-Flow) utilize the exact architectures and hyperparameters established in the original voraus-AD benchmark.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

For the multi-step forecasting and zero-shot transfer evaluations (Tables 15 and 6), we evaluate our model against four baseline forward-dynamics predictors. All trainable baselines utilize the identical 10-step context window to predict 1-step-ahead joint accelerations, which are subsequently integrated.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Training Details: All trainable forecasting baselines (Linear, Flat MLP, TCN) were trained on the exact same 1,093-episode pretraining split as the main TCN-Transformer model. They were trained to minimize Mean Squared Error (MSE) on the predicted joint accelerations using the Adam optimizer.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Linear Baseline: A standard linear regression model consisting of a single nn.Linear layer that maps the flattened context window (${{{10\text{~steps}} \times 36}\text{~features}} = {360\text{~inputs}}$) directly to the target acceleration space.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Flat MLP: A multi-layer perceptron utilizing two hidden layers (128 units and 64 units, respectively) with ReLU activation functions, mapping the flattened context window to the target predictions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

TCN Baseline: A 2-layer Temporal Convolutional Network (Conv1d) utilizing a kernel size of 3 and a hidden dimension of 64. This serves as a representative pre-2023 benchmark for sequence modeling on industrial control data.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Model architectures and training", "weight": 1.0} -->

Kinematic Baseline (Zero-Predictor): A non-learned, naive physics baseline that constantly predicts zero acceleration. It assumes the robot maintains constant velocity from the final observation step, generating its trajectory purely through the kinematic integrator.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Single-Machine Baselines: Validating the S-E-F-C Schema", "weight": 1.0} -->

Anomaly Detection. We use voraus-AD to test whether S-E-F-C enables competitive anomaly detection via supervised dynamics rather than holistic reconstruction. Unstructured baselines reconstruct all 130 channels end-to-end; our S-E-F-C MLP is a regressor on 24 signals, mapping 18 Setpoints (setpoint_pos_0...5, setpoint_vel_0...5, setpoint_acc_0...5) to 6 Efforts (effort_motor_torque_0...5). Per-episode MAE on Effort is the anomaly score. On 24 signals alone it reaches 83.2% mean AUROC. Table 4 shows it beats weaker full-channel baselines (1-NN, GANF, PCA) but not the strongest ones (CAE, LSTM-VAE, MVT-Flow). Architectures follow Brockmann et al..

<!-- chunk {"id": "body-0043", "role": "body", "section": "Single-Machine Baselines: Validating the S-E-F-C Schema", "weight": 1.0} -->

Table 5 reports per-category AUROC on the voraus-AD subset for all seven methods compared in the main paper. The S-E-F-C MLP achieves the highest AUROC on mechanically distinctive faults (Miscommutation: 99.2, Additional Axis Weight: 95.8) where sustained Effort--Feedback divergence provides a strong discriminative signal, but struggles on transient or subtle gripping failures (Collision w/ Cables: 67.6, Losing Can: 71.8) where the anomaly window is brief and the single-step MLP lacks temporal modelling capacity.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Single-Machine Baselines: Validating the S-E-F-C Schema", "weight": 1.0} -->

Multi-Step Forecasting. To demonstrate support for high-fidelity dynamics modelling, we evaluate an autoregressive TCN-Transformer (105k parameters) on the voraus-AD Pick & Place data. Operating strictly on S-E-F-C inputs, the model acts as a forward-dynamics predictor: it forecasts 1-step-ahead joint accelerations via a 10-step context window, which are integrated (Euler, ${\Deltat} = 0.01$ s) to derive position and velocity. Models are trained on 1,093 normal episodes and validated on 137 held-out normal episodes. Full architecture and training hyperparameters are detailed in Section 4.1.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Single-Machine Baselines: Validating the S-E-F-C Schema", "weight": 1.0} -->

As shown in Figure 3 and Table 15 (Appendix D), the TCN-Transformer achieves an average of 156.7 steps (78.4% of the 200-step horizon at 100 Hz) without exceeding a strict 0.01 rad per-joint position error threshold, substantially outperforming all baselines. At 200 steps the TCN-Transformer's MSE ($0.11 \times 10^{- 4}$ rad^2^) is more than four orders of magnitude below the next best baseline.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Cross-Embodiment Transfer: An Open Challenge", "weight": 1.0} -->

The S-E-F-C schema enables structured zero-shot transfer across machine types. To evaluate this, we define the *mean-centered MAE* (MC-MAE) metric. By subtracting the per-episode, per-joint mean from both the ground truth and predictions prior to computing the absolute error, MC-MAE explicitly isolates dynamic forces from static payload biases.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Cross-Embodiment Transfer: An Open Challenge", "weight": 1.0} -->

A TCN-Transformer trained solely on voraus-AD (Yu-Cobot) Pick & Place data achieves a mean-centered MAE of 0.339 $\pm$ 0.006 on 1,433 AURSAD (UR3e) Screwdriving episodes, outperforming every baseline including the kinematic baseline ($0.373 \pm 0.005$) and all structureless learned models (Table 6). Raw effort-MAE remains high (1.74 vs. 1.51 for a zero-predictor) due to static payload and gravity-compensation differences between embodiments, but MC-MAE confirms that the *shape* of the dynamics transfers successfully across machines.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion & Limitations", "weight": 1.5} -->

FactoryNet provides the largest open-source, fault-injected time-series corpus for industrial robotics, unified by the S-E-F-C taxonomy. Our experiments show that the schema enables competitive anomaly detection with 5$\times$ fewer signals, accurate multi-step dynamics forecasting, and positive zero-shot cross-embodiment transfer. The sim-to-real gaps we quantify are naturally interpreted as errors of learned *forward* dynamics under S--E--F--C-aligned inputs, not merely covariate shift in raw telemetry. Current limitations include synthetic data restricted to Pick & Place and cross-embodiment transfer evaluated on a single source-target pair; future work will expand to additional machine families, tasks, and transfer settings.
