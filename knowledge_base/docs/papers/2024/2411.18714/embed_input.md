<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Explainable Deep Learning Improves Human Mental Models of Self-driving Cars

Topics include Safety, Neural networks, Deep learning, Causal inference, Learning, Self driving, Mental model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Self-driving cars increasingly rely on deep neural networks to achieve human-like driving. The opacity of such black-box planners makes it challenging for the human behind the wheel to accurately anticipate when they will fail, with potentially catastrophic consequences. While research into interpreting these systems has surged, most of it is confined to simulations or toy setups due to the difficulty of real-world deployment, leaving the practical utility of such techniques unknown. Here, we introduce the Concept-Wrapper Network (CW-Net), a method for explaining the behavior of machine-learning-based planners by grounding their reasoning in human-interpretable concepts. We deploy CW-Net on a real self-driving car and show that the resulting explanations improve the human driver's mental model of the car, allowing them to better predict its behavior. To our knowledge, this is the first demonstration that explainable deep learning integrated into self-driving cars can be both understandable and useful in a realistic deployment setting. CW-Net accomplishes this level of intelligibility while providing explanations which are causally faithful and do not sacrifice driving performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Overall, our study establishes a general pathway to interpretability for autonomous agents by way of concept-based explanations, which could help make them more transparent and safe.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are hundreds of companies developing autonomous vehicle (AV) technology globally \[badue2021self\], promising to revolutionize transportation for everyone. The industry currently spans two segments: fully autonomous ride-hail systems and consumer vehicles with driver-assistance \[SAEJ3016_2021\]. In consumer vehicles, machine learning (ML) solutions have markedly improved the technology, yet they still require human intervention in unusual or challenging situations where learned planners may not determine the correct action \[xing2021toward\]. As driving is safety-critical, such infrequent failures matter, making it essential that the human driver is able to anticipate and be prepared for such situations \[pereira2020challenges\]. However, the opaque nature of ML planners makes it challenging to interpret and communicate the causes of their decisions, hampering the ability of human drivers to understand and predict AV behavior while achieving real-time situational awareness \[kuznietsov2024explainable, arfini2023design, atakishiyev2024incorporating\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lack of effective communication between the AV and the human driver has contributed to multiple high-profile incidents, some resulting in fatalities \[Titcomb2019, Fang2023, templeton2024waymo\], highlighting the urgent need to make ML planners interpretable \[atakishiyev2024explainable\]. Previous studies have sought to address this using surveys and simulated scenarios \[koo2015did, koo2016understanding, wiegand2020d, wang2021human, schneider2021increasing, schneider2021explain, omeiza2021towards, zemni2023octet\], a human driver emulating the AV \[kim2023and, schneider2023don\], or language models providing rationales for the driving policy in natural language \[marcu2023lingoqa, wang2025alpamayo\]. However, these studies were theoretical, did not provide causally faithful explanations, were only evaluated in simulation, or did not convincingly show the practical utility of the explanations to end users.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This leaves open the question of how to provide explanations that are understandable, useful, and faithful to the decision-making process of the AV in a realistic setting.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To answer this question, we scale up our work on interpretable-by-design deep reinforcement learning \[kenny2023towards\] using motifs from the literature on concept-bottleneck models \[yuksekgonulpost\] to propose the Concept-Wrapper Network (CW-Net). CW-Net grounds the reasoning of a black-box ML planner in human-interpretable concepts, such as "Approaching stopped vehicle" or "Close to cyclist". This method is rooted in case-based reasoning, a classical artificial intelligence (AI) approach \[leake1996case, keane2019case, sormo2005explanation, kenny2019twin\] inspired by cognitive models of human reasoning and memory \[schank1983dynamic\]. CW-Net can be applied to arbitrary pretrained deep neural networks, does not require retraining from scratch, and does not degrade the performance of the original black-box ML planner. Since the inferred concepts are the sole input to the final decision-making module of CW-Net and therefore directly determine AV behavior, we refer to them as causally faithful.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notably, our approach contrasts with popular post-hoc explanation methods \[lundberg2017unified, ribeiro2016should\], which are applied to pretrained models and do not, by construction, guarantee faithfulness to the model decision process \[rudin2019stop\].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply CW-Net to an ML planner trained to imitate human driving behavior using inverse reinforcement learning \[tomov2025treeirl, phan2023driveirl\]. We replace the final (reward) layer of the pretrained deep neural network with a concept classifier, followed by a new reward layer. We then jointly train the classifier and the new reward layer to predict scenario types and driving decisions, respectively, without modifying the rest of the network. Evaluation on a large-scale benchmark \[karnchanachari2024towards\] confirms that CW-Net is able to classify concepts without compromising driving behavior. To study the utility of the explanations, we deploy CW-Net on a real self-driving car with a safety driver in a semi-naturalistic study \[heim2025lab2car\]. We demonstrate three situations in which the driver's initially inaccurate mental model is subsequently improved by the CW-Net explanations, which in turn allows the driver to more accurately predict AV behavior. We then observe similar mental model improvement in larger online studies simulating these scenarios.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lastly, we link these results to more complex real-world situations by deploying CW-Net on public roads in Las Vegas. We use these new data in a large online study ($N=100$) to demonstrate that improvements in mental model goodness lead to improved predictive ability and situational awareness. Overall, our work demonstrates how explainable deep learning can help users of an advanced autonomous system improve their mental model of the system and better anticipate its future behavior.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Black-box planner", "weight": 1.0} -->

We focus on the planning module of the AV stack (Figure 1a), which takes as input a scene context $s$ and outputs a trajectory $\hat{\tau}$. Here, $s$ is a symbolic object-oriented representation of the scene, computed by the perception module, while $\hat{\tau}$ is the trajectory that the subsequent controller module should follow. We use a deep neural network architecture \[tomov2025treeirl, phan2023driveirl\] consisting of a scene encoder $H(s)\rightarrow\mathbf{h}$ and a trajectory generator $G(s)\rightarrow\{\tau_{1}\dots\tau_{k}\}$, followed by a scene-trajectory encoder $E(\mathbf{h},\tau_{i})\rightarrow\mathbf{z}_{i}$ and a final reward layer $R(\mathbf{z}_{i})\rightarrow r_{i}$ (Figure 1b).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Black-box planner", "weight": 1.0} -->

$H$ computes a scene embedding $\mathbf{h}$ and $G$ computes a set of $k$ candidate trajectories $\{\tau_{1}\dots\tau_{k}\}$. Those are combined in $E$ to compute an embedding $\mathbf{z}_{i}$ for each trajectory $\tau_{i}$. Finally, $R$ computes an estimated reward $r_{i}$ for each trajectory $\tau_{i}$, quantifying how human-like it is. In other words, $r_{i}$ is higher when $\tau_{i}$ is more similar to how a human would drive in this situation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Black-box planner", "weight": 1.0} -->

During inference, the trajectory with highest reward is selected on each iteration: We use inverse reinforcement learning to train the planner on 80 hours of human expert driving \[tomov2025treeirl, phan2023driveirl\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Planning over human-friendly concepts", "weight": 1.0} -->

To make the ML planner interpretable, we modify the planner architecture to additionally provide explanations for its behavior \[kenny2023towards\]. Our working definition of explainable AI follows Gunning & Aha \[gunning2019darpa\], who define it as 'AI systems that can explain their rationale to a human user, characterize their strengths and weaknesses, and convey an understanding of how they will behave in the future.'

<!-- chunk {"id": "body-0015", "role": "body", "section": "Planning over human-friendly concepts", "weight": 1.0} -->

Specifically, we replace $R$ with a concept classifier $C(\mathbf{z}_{i})\rightarrow\mathbf{c}_{i}$, followed by a new reward layer $R^{\prime}(\mathbf{c}_{i})\rightarrow r^{\prime}_{i}$ (Figure 1c). The concept classifier $C$ computes a logit vector $\mathbf{c}_{i}$ that is passed through a softmax and/or sigmoid layer that, in turn, assigns probabilities to different human-interpretable concepts. Since $R^{\prime}$ computes trajectory rewards from $\mathbf{c}_{i}$, the final decisions are based solely on these concept assignments and hence they constitute a causally faithful explanation. The rest of the network remains the same.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Planning over human-friendly concepts", "weight": 1.0} -->

Similarly to the black-box planner, trajectories are selected according to: We train CW-Net to jointly predict concept labels and mimic the driving decisions of the black-box planner. Specifically, $\mathbf{c}_{i}$ is supervised with labels corresponding to types of scenarios, such as "Approaching stopped vehicle" or "Close to cyclist" (see Section 9.5 for a full list of concepts). This ensures that CW-Net assigns a unique interpretable concept to each unit in $\mathbf{c}_{i}$. At the same time, $r^{\prime}_{i}$ is supervised with trajectories selected by the black-box planner using a cross-entropy loss. During training, the rest of the deep neural network ($H$, $G$, and $E$) is kept frozen (see Section 9.2 for more details). We focus our study on this particular ML planner architecture, noting that prior work indicates CW-Net would generalize effectively to other architectures \[kenny2023towards\].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Classifying concepts", "weight": 1.0} -->

As a baseline, we first evaluated the black-box planner (without CW-Net) using closed-loop simulations with the nuPlan simulator on the nuPlan dataset \[karnchanachari2024towards\] (Table ED1). Overall, the results were competitive with the top submissions to the nuPlan challenge, although performance was slightly lacking when starting from a stop (see Section 9). This suggests that there is room for improvement and, importantly, opportunities to study explanations of undesirable behavior.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Classifying concepts", "weight": 1.0} -->

We then evaluated the driving performance of CW-Net wrapped around the black-box planner (Table ED1). The results were equivalent, with less than 1% difference across all metrics, confirming that our method did not degrade driving performance. We also evaluated concept classification on held-out datasets (Tables S1, S2). Mean accuracy was 54%, with 23% precision, 77% recall, and an F1 score of 0.31 (see Section 9.3). Overall, these results indicate that CW-Net can be used to ground the decision making of high-performance ML planners in human-interpretable concepts, without sacrificing driving performance.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Mental model improvement in deployment", "weight": 1.0} -->

Our central hypothesis is that the explanations from CW-Net would improve the human driver's mental model of the AV and, by extension, their situational awareness. This would be particularly salient in surprising situations, which is when explanations are most useful \[foster2013surprise\]. Specifically, the explanations should improve the driver's ability to understand and address the reasons for AV failures, and also to predict its future behavior.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Mental model improvement in deployment", "weight": 1.0} -->

To test this hypothesis, we deploy CW-Net on a real AV on a private track using the Lab2Car wrapper \[heim2025lab2car\] and observe how safety drivers react to surprising events and the corresponding CW-Net explanations (Figure 2). These situations were not planned, but instead occurred naturally, with minimal intervention from the researchers, who only dictated high-level plans for each day. This semi-naturalistic study allowed us to assess the utility of the explanations in naturally occurring surprising situations. To measure AV predictability, we record the drivers' ability to make counterfactual predictions about AV behavior in these situations. To note the drivers' mental models, together with their predictive ability, we additionally record their think-aloud thoughts before and after considering CW-Net explanations \[hoffman2023measures\]. We focus on concepts that relate to other road users and can be easily tested counterfactually (see Section 9.5).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Unexpected stopping for nearby vehicles", "weight": 1.0} -->

We observed that the AV repeatedly came to a stop shortly before a pedestrian pickup/drop-off zone (Figure 3a). The driver's intuition was that the car stopped because of the pickup/drop-off zone, but the explanations indicated that the planner stopped because it detected that it was "Close to another vehicle" (the CLOSE concept). To test this hypothesis, the driver manually moved the car farther from the parked cars. At this point, the probability of CLOSE decreased and the AV began moving again, thus supporting the alternative hypothesis. A full timeline of events is detailed in Figure 3a. We fitted the intercept of the CLOSE probability against the speed of the AV globally and found it accurately predicts stopping and starting for this event.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hallucinating a stopped vehicle ahead", "weight": 1.0} -->

At another location, the AV would reliably come to a stop next to a traffic cone (Figure 3b). The driver's initial mental model was that the cone was responsible for the phantom brake. However, the "Approaching stopped vehicle" (ASV) concept peaked shortly before the car stopped. This suggested an alternative hypothesis, that the planner matched the current situation with training scenarios labeled ASV, which in turn promotes stopping behavior associated with such scenarios. As a counterfactual test, the cone was removed. The AV exhibited the same stopping behavior at the same location, along with similar ASV probability and speed profiles ($L_{2}$ similarities of 7.37 (1.12 original version) and 1.6 between the respective time-warped profiles, compared to an average $L_{2}>200$ for random events), thus supporting the alternative hypothesis. Note that although there was no vehicle in front of the AV, the explanation is causally faithful to the underlying planner and explains why it stopped (namely, because it incorrectly detected a stopped vehicle). Figure 3b illustrates a global analysis of ASV, showing it to be a powerful predictor of braking.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Reacting safely to cyclist", "weight": 1.0} -->

Finally, we tested the ability of the AV to stop safely for cyclists (Figure 3c). For each test, the driver engaged self-driving mode while approaching a cyclist. The driver was instructed to engage self-driving from a speed at which they felt safe, since this determines the subsequent speed of the AV. During the initial tests, the AV reliably stopped for the cyclist. However, the BIKE concept maintained a low probability throughout each test ($<$ 1%), indicating that CW-Net was failing to detect the cyclist. Over time, the driver became aware of the concept reading and gradually increased their caution by initiating self-driving from slower speeds. A post-hoc analysis revealed that, although the perception system detected the cyclist, the ML planner was not configured to consume inputs for cyclists. As a result, it chose unsafe trajectories which would have collided with the cyclist. In reality, the AV stopped due to a built-in safety backup system, which commands a brake if collision is imminent. This indicates that the increased caution dictated by the driver's updated mental model was warranted.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Simulation studies", "weight": 1.0} -->

The semi-naturalistic study above illustrates how CW-Net explanations can improve the human driver's mental model of the AV in surprising real-world situations, leading to better understanding and predictability of AV behavior. To validate that these results replicate in larger populations and generalize to naturalistic scenarios, we conduct several larger follow-up studies (Figures ED2-ED8). First, we show that in simulations of the real-world scenarios in Section 5, CW-Net explanations consistently improve mental models and predictions for both experts and non-experts alike. Second, we collect data from CW-Net in naturalistic real-world scenarios on public roads and show that the explanations improve situational awareness -- an indirect measure of mental model goodness \[endsley1995measurement\] -- in surprising situations, without degrading it in unsurprising situations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Mental models and predictability", "weight": 1.0} -->

The purpose of the first study is to demonstrate that the effects observed on the road reproduce in larger populations, and establish a link between direct measures of mental model goodness and performance on downstream tasks --- such as predicting AV behavior --- so that the latter can be used as a proxy for the former. We conducted an online survey in which we showed participants replays of the scenarios from the private track (front camera recordings with overlaid CW-Net explanations; see Figure ED6).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Mental models and predictability", "weight": 1.0} -->

For each scenario, we asked participants to choose the reason for the AV's behavior that best aligns with their current beliefs (i.e., "Why did the AV do that?") and to make a counterfactual prediction (i.e., "What would the AV do if...?"). Following Hoffman et al. \[hoffman2023measures\], we refer to the former as the nearest-neighbor task -- since it forces participants to pick the nearest explanation to their beliefs -- and the latter as the prediction task. Both tasks consist of a multiple-choice question followed by a confidence score. The prediction task additionally includes a free-form text response where participants describe the reasons for their prediction. Both directly probe the participants' mental models, while the prediction task itself also serves as a proxy performance metric for mental model goodness. Importantly, we collected responses before and after observing the explanations. This within-participant design mirrors the experience of the drivers during the real-world tests (Figures ED2, ED6).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Mental models and predictability", "weight": 1.0} -->

The study was conducted with experts ($N=9$ Motional drivers/engineers) and non-experts ($N=30$ pseudo-random participants from Prolific.com).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Mental models and predictability", "weight": 1.0} -->

On the nearest-neighbor task, CW-Net explanations improved mental models for almost all participants (8/9 experts and 27/30 non-experts; Figure ED3). Free-form text responses were initially similar to the initial beliefs of the safety drivers during the on-road tests ($p<10^{-9}$) and then shifted towards their final beliefs ($p<0.0002$) and the ground-truth reasons for AV behavior ($p<10^{-5}$; exact binomial tests for non-experts; Figure ED4A,B). The distribution of mental model updates on both tasks was similar across both groups ($\beta=0.04,p=0.8$, ordinary least-squares regression; Figure ED4C). Importantly, mental model improvement on the nearest-neighbor task correlated with improvements in prediction accuracy ($\beta=2.02\pm 0.87,p=0.02$ for experts, $\beta=9.86\pm 2.07,p<0.001$ for non-experts; linear mixed-effects models \[LMEs\]; Figure ED5, left).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mental models and predictability", "weight": 1.0} -->

A similar effect was observed for the free-form text responses ($\beta=1.70\pm 0.91,p=0.06$ for experts, $\beta=5.03\pm 1.23,p<0.001$ for non-experts; LMEs; Figure ED5, right). Together, these results support the conclusion that CW-Net explanations can reliably improve mental models of the AV and that prediction performance can serve as a reliable proxy for mental model goodness.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Explanations and situational awareness", "weight": 1.0} -->

To verify that the effects observed on the private track generalize to more complex, naturalistic scenarios, we deployed CW-Net on public roads in Las Vegas (Figures ED6, ED8, 3-right). Due to safety reasons and the experimental nature of the ML planner, the safety driver operated the AV in 'manual' mode for several hours, with CW-Net running in the background. This allowed us to collect naturalistic scenarios analogous to those encountered on the private track \[FAA2011FlightTest, schneider2023don\] (Figure ED6). We use replays of those scenarios to conduct a large-scale online study ($N=100$) within the Situation Awareness Global Assessment Technique (SAGAT) framework tailored for explainable AI \[endsley1995measurement, sanneman2022situation\].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Explanations and situational awareness", "weight": 1.0} -->

The SAGAT framework is the gold standard for evaluating situational awareness in complex, dynamic tasks \[endsley1995measurement, sanneman2022situation\]. In contrast to prior benchmark applications of SAGAT in driving research, which have been conducted almost exclusively within controlled driving-simulator environments \[ma2005situation, scholtz2005implementation\], we evaluate situational awareness on replays drawn from real-world public-road operation of the AV, addressing long-standing concerns about the ecological validity of simulator-only assessments. It measures the situational awareness of a human operator by freezing a scenario, querying the operator about their perception (i.e., "What are the inputs to the AV?"), comprehension (i.e., "Why is the AV doing that?"), and projection (i.e., "What would the AV do if...?") of the situation (Figure ED7) and comparing their responses with the ground truth.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Explanations and situational awareness", "weight": 1.0} -->

As counterfactual predictive performance in Section 6.1 aligns with mental model goodness, we use projection in SAGAT as a proxy for mental model elicitation and goodness \[hoffman2023measures\]. For each type of scenario and corresponding concept, we sample two instances in which AV behavior was surprising (e.g., stopping unnecessarily) and two corresponding instances in which it was unsurprising (Table S5), to verify CW-Net did not negatively impact situational awareness. We use a between-participant design in which the experimental group received explanations from CW-Net, while the control group received placeholder explanations of AV kinematics to balance cognitive load \[kenny2021explaining\] (Figure ED8).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Explanations and situational awareness", "weight": 1.0} -->

We found that the CW-Net explanations significantly improved measures of situational awareness for surprising events (Figure ED7, left; Table S6, top), with large effect sizes for perception (Cohen's d = 1.290, 95% CI \[0.857, 1.723\]), comprehension (Cohen's d = 0.996, 95% CI \[0.578, 1.413\]), and a medium effect size for projection (Cohen's d = 0.606, 95% CI \[0.203, 1.009\]). Conversely, explanations did not impact situational awareness for unsurprising events after Bonferroni correction (Figure ED7; Table S6). Together, these results show that the explanations from CW-Net are robust across various conditions and can reliably improve mental models in surprising situations, without significant negative effects in unsurprising situations. Moreover, they demonstrate pragmatic usage of the improved mental models.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work shows how explainable deep learning can provide useful explanations for AVs in a real-world setting. CW-Net achieves this by grounding the reasoning of a pretrained black-box ML planner in human-interpretable concepts that are directly used to make driving decisions. By revealing otherwise inaccessible information about the decision-making process of the AV in real time, CW-Net helps improve the human driver's mental model of the AV. This, in turn, improves the driver's situational awareness and reveals limitations of the robotic system, helping the driver better anticipate its mistakes. While we showcase CW-Net using a particular kind of classification-based ML planner architecture, the core idea can be similarly applied to other architectures, including end-to-end learning systems and vision-language-action models. Additionally, while our experimental setup assumes a human driver observing the explanations in real time --- an application more suited to advanced driver-assistance systems --- CW-Net could equally be applied to debugging and improving fully autonomous AV's.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Critically, whereas prior work on explanations and situational awareness for AV decision making has largely been confined to simulated or controlled scenarios \[koo2015did, koo2016understanding, wiegand2020d, wang2021human, schneider2021increasing, schneider2021explain, omeiza2021towards, zemni2023octet, sanneman2022situation\], our deployment of CW-Net on public roads extends these findings to the environmental complexity of real-world driving, providing evidence of ecological validity and practical relevance for the AV industry.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Many systems involving human-robot interaction require real-time explanations, including AI wingmen, drone navigation systems, and robotic surgeons. Similarly to AVs, many of these applications increasingly rely on deep learning, with a long tail of potentially catastrophic failure cases. Indeed, many regulatory bodies have already made explainable AI a core component of their legislation, with AVs likely to follow suit as they are widely deployed with various users \[atakishiyev2024explainable\]. As such, the success of CW-Net suggests that similar algorithms may prove essential for meeting the regulatory standards for deploying AVs, while building appropriate trust in the technology. In future work, it would be prudent to extend CW-Net to a larger set of concepts --- perhaps in an unsupervised manner to overcome the challenges of labeling --- and better cover the vast array of concepts relevant to AV settings.
