<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gemini Robotics: Bringing AI into the Physical World

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remarkable progress of modern artificial intelligence (AI) models -- with pre-training on large-scale datasets -- has redefined information processing, demonstrating proficiency and generalization across diverse modalities such as text, images, audio, and video. This has opened a vast landscape of opportunities for interactive and assistive systems within the digital realm, ranging from multimodal chatbots to virtual assistants. However, realizing the potential of general-purpose autonomous AI in the physical world requires a substantial shift from the digital world, where physically grounded AI agents must demonstrate robust human-level embodied reasoning: The set of world knowledge that encompasses the fundamental concepts which are critical for operating and acting in an inherently physically embodied world. While, as humans, we take for granted our embodied reasoning abilities -- such as perceiving the 3D structure of environments, interpreting complex inter-object relationships, or understanding intuitive physics -- these capabilities form an important basis for any embodied AI agent. Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to take actions that have direct effects on their external environment, bridging the gap between passive perception and active physical interaction.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the recent advancements in robotics hardware, there is exciting potential for creating embodied AI agents that can perform highly dexterous tasks. With this in mind, we ask: What would it take to endow a state-of-the-art digital AI model with the embodied reasoning capabilities needed to interact with our world in a general and dexterous manner?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our thesis is predicated on harnessing the advanced multimodal understanding and reasoning capabilities inherent in frontier Vision-Language Models (VLMs), such as Gemini 2.0. The generalized comprehension afforded by these foundation models, with their ability to interpret visual inputs and complex text instructions, forms a powerful foundation for building embodied agents. This endeavor hinges on two fundamental components. First, Gemini needs to acquire robust embodied reasoning, gaining the ability to understand the rich geometric and temporal-spatial details of the physical world. Second, we must ground this embodied reasoning in the physical world by enabling Gemini to speak the language of physical actions, understanding contact physics, dynamics, and the intricacies of real-world interactions. Ultimately, these pieces must coalesce to enable fast, safe and dexterous control of robots in the real world.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model. We first validate the performance and generality of the base Gemini 2.0's innate embodied reasoning capabilities with a new open-source general embodied reasoning benchmark, ERQA. We then introduce two models: The first model is Gemini Robotics-ER, a VLM with strong embodied reasoning capabilities at its core, exhibiting generalization across a wide range of embodied reasoning tasks while also maintaining its core foundation model capabilities. Gemini Robotics-ER exhibits strong performance on multiple capabilities critical for understanding the physical world, ranging from 3D perception to detailed pointing to robot state estimation and affordance prediction via code. The second model is Gemini Robotics, a state-of-the-art Vision-Language-Action (VLA) model that connects strong embodied reasoning priors to dexterous low-level control of real-world robots to solve challenging manipulation tasks. As a generalist VLA, Gemini Robotics can perform a wide array of diverse and complicated tasks, while also closely following language guidance and generalizing to distribution shifts in instructions, visuals, and motions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To emphasize the flexibility and generality of the Gemini Robotics models, we also introduce an optional specialization stage, which demonstrates how Gemini Robotics can be adapted for extreme dexterity, for advanced reasoning in difficult generalization settings, and for controlling completely new robot embodiments. Finally, we discuss the safety implications of training large robotics models such as the Gemini Robotics models, and provide guidelines for how to study such challenges in the context of VLAs. Specifically, this report highlights: ERQA: An open-source benchmark specifically designed to evaluate embodied reasoning capabilities of multimodal models, addressing the lack of benchmarks that go beyond assessing atomic capabilities and facilitating standardized assessment and future research.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gemini Robotics-ER: A VLM demonstrating enhanced embodied reasoning capabilities.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gemini Robotics: A VLA model resulting from the integration of robot action data, enabling high-frequency dexterous control, robust generalization and fast adaptation across diverse robotic tasks and embodiments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Responsible Development: We discuss and exercise responsible development of our family of models in alignment with Google AI Principles carefully studying the societal benefits and risks of our models, and potential risk mitigation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Gemini Robotics models serve as an initial step towards more generally capable robots. We believe that, ultimately, harnessing the embodied reasoning capabilities from internet scale data, grounded with action data from real world interactions, can enable robots to deeply understand the physical world and act competently. This understanding will empower them to achieve even the most challenging goals with generality and sophistication that has so far seemed out of reach for robotic systems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Embodied Reasoning with Gemini 2.0", "weight": 1.0} -->

Gemini 2.0 is a Vision-Language Model (VLM) that is capable of going beyond tasks that only require visual understanding and language processing. In particular, this model exhibits advanced *embodied reasoning* (ER) capabilities. We define ER as the ability of a Vision-Language Model to ground objects and spatial concepts in the real world, and the ability to synthesize those signals for downstream robotics applications. See some examples of such capabilities in Fig. 2. In Section 2.1 Benchmark ‣ 2 Embodied Reasoning with Gemini 2.0 ‣ Gemini Robotics: Bringing AI into the Physical World"), we first introduce a benchmark for evaluating a broad spectrum of ER capabilities and show that Gemini 2.0 models are state-of-the-art. In Section 2.2, we demonstrate the wide range of specific ER capabilities enabled by Gemini 2.0. Finally, in Section 2.3, we showcase how these capabilities can be put to use in robotics applications without the need for fine-tuning on robot action data, enabling use cases such as zero-shot control via code generation and few-shot robot control via in-context learning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Embodied Reasoning Question Answering (ERQA) Benchmark", "weight": 1.0} -->

To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely required by an embodied agent interacting with the physical world. ERQA consists of $400$ multiple choice Visual Question Answering (VQA)-style questions across a wide variety of categories, including spatial reasoning, trajectory reasoning, action reasoning, state estimation, pointing, multi-view reasoning, and task reasoning. A breakdown of the distribution of question types is in Fig. 4 Benchmark ‣ 2 Embodied Reasoning with Gemini 2.0 ‣ Gemini Robotics: Bringing AI into the Physical World"). Of the $400$ questions 28% have more than one image in the prompt --- these questions that require corresponding concepts across multiple images tend to be more challenging than single-image questions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Embodied Reasoning Question Answering (ERQA) Benchmark", "weight": 1.0} -->

ERQA is complementary to existing VLM benchmarks, which tend to highlight more atomic capabilities (e.g., object recognition, counting, localization), but in most cases do not take sufficient account of the broader set of capabilities needed to act in the physical world. Fig. 3 Benchmark ‣ 2 Embodied Reasoning with Gemini 2.0 ‣ Gemini Robotics: Bringing AI into the Physical World") shows some example questions and answers of our ERQA. Some questions require the VLM to recognize and register objects across multiple frames; others require reasoning about objects' affordances and 3D relationships with the rest of the scene. Full details of the benchmark can be found at Table 1: Comparing VLMs on benchmarks that assess a wide range of embodied reasoning capabilities, including our new ERQA benchmark. Benchmarks are evaluated by accuracies of multiple-choice answers. Results obtained in Feb 2025.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Embodied Reasoning Question Answering (ERQA) Benchmark", "weight": 1.0} -->

We manually labeled all questions in ERQA to ensure correctness and quality. Images (not questions) in the benchmark are either taken by ourselves or sourced from these datasets: OXE, UMI Data, MECCANO, HoloAssist, and EGTEA Gaze+. In Table 1 Benchmark ‣ 2 Embodied Reasoning with Gemini 2.0 ‣ Gemini Robotics: Bringing AI into the Physical World"), we report results of Gemini models and other models on ERQA, as well as on RealworldQA and BLINK, two popular benchmarks that also measure spatial and image understanding capabilities. Specifically, we report results of Gemini 2.0 Flash, a powerful low-latency workhorse model and Gemini 2.0 Pro Experimental 02-05 (short as Gemini 2.0 Pro Experimental in the rest of the paper), the best Gemini model for complex tasks. Gemini 2.0 Flash and Pro Experimental achieve a new state-of-the-art on all three benchmarks in their respective model classes. We also note that ERQA is the most challenging benchmark across these three, making the performance here especially notable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Embodied Reasoning Question Answering (ERQA) Benchmark", "weight": 1.0} -->

Gemini 2.0 models are capable of advanced reasoning --- we found we can significantly improve Gemini 2.0's performance on the benchmark if we use Chain-of-Thought (CoT) prompting, which encourages the model to output reasoning traces to "think" about a problem before choosing the multiple choice answer, instead of directly predicting the answer. We use the following instruction as the CoT prompt appended at the end of each question: "Reason step by step about the answer, and show your work, for each step. Only after that, proceed to the final answer." Results are shown in Table 2 Benchmark ‣ 2 Embodied Reasoning with Gemini 2.0 ‣ Gemini Robotics: Bringing AI into the Physical World"). With CoT prompting, Gemini 2.0 Flash's performance exceeds that of Gemini 2.0 Pro Experimental without CoT, and CoT further improves Gemini 2.0 Pro Experimental's performance. We highlight two such reasoning traces in Fig. 5 Benchmark ‣ 2 Embodied Reasoning with Gemini 2.0 ‣ Gemini Robotics: Bringing AI into the Physical World"), questions that Gemini 2.0 Pro Experimental answered incorrectly without CoT, but correctly with CoT.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Embodied Reasoning Question Answering (ERQA) Benchmark", "weight": 1.0} -->

The reasoning traces demonstrate Gemini 2.0 is able to 1) precisely ground its spatial understanding in observations in the image and 2) leverage such grounding to perform complex, step-by-step embodied reasoning.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

In this section, we illustrate some of Gemini 2.0's embodied reasoning capabilities in more detail. We also introduce Gemini Robotics-ER, a version of Gemini 2.0 Flash that has enhanced embodied reasoning. These can be used in robotics applications without the need for any additional robot-specific data or training. Gemini 2.0 can understand a variety of 2D spatial concepts in images.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Object Detection: Gemini 2.0 can perform open-world 2D object detection, providing precise 2D bounding boxes with queries that can be explicit (e.g., describing an object name) or implicit (categories, attributes, or functions).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Pointing: Given any natural language description, the model is able to point to explicit entities like objects and object parts, as well as implicit notions such as affordances (where to grasp, where to place), free space and spatial concepts. See Table 3 for quantitative evaluations.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Trajectory Prediction: Gemini 2.0 can leverage its pointing capabilities to produce 2D motion trajectories that are grounded in its observations. Trajectories can be based, for instance, on a description of the physical motion or interaction.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Grasp Prediction: This is a new feature introduced in Gemini Robotics-ER. It extends Gemini 2.0's pointing capabilities to predict top-down grasps.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Gemini 2.0 is also capable of 3D spatial reasoning. With the ability to "see in 3D", Gemini 2.0 can better understand concepts like sizes, distances, and orientations, and it can leverage such understanding to reason about the state of the scene and actions to perform.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Multi-View Correspondence: A natural way of representing 3D information with images is through multi-view (e.g., stereo) images. Gemini 2.0 can understand 3D scenes from multi-view images and predict 2D point correspondences across multiple camera views of the same scene.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

3D Bounding Box Detection: This 3D understanding applies to single images as well - Gemini 2.0 can directly predict metric 3D bounding boxes from monocular images. Like 2D Detection and Pointing capabilities, Gemini 2.0 can detect objects by open-vocabulary descriptions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

While it is possible to create expert models for each of these tasks individually, fusing them in a single foundation model, such as Gemini 2.0, allows the model to perform embodied reasoning tasks with open-world natural language instructions, respond to feedback and sustain multi-turn interactions. In particular, Gemini 2.0 can combine scene understanding with reasoning to solve more complex tasks, such as writing robot code (see Section 2.3).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Below we present detailed quantitative and qualitative evaluations of these capabilities with Gemini 2.0 models (Flash, and Pro Experimental), as well as comparisons with other VLMs where appropriate. For some capabilities, we also present results on Gemini Robotics-ER. You can find code and prompt examples on how to prompt Gemini 2.0 to elicit these capabilities here.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Object Detection. Gemini 2.0 can predict 2D object bounding boxes from natural language queries. In Fig. 6, we show multiple 2D detection examples with Gemini 2.0 Flash on images that a robot might see. Gemini 2.0 represents 2D bounding boxes with the convention $\lbrack y_{0},x_{0},y_{1},x_{1}\rbrack$. We can prompt Gemini 2.0 to detect everything in a scene (examples in Fig. 2). The model can also detect specific objects by their descriptions --- for example, "detect all the kitchenware" in Fig. 6. These descriptions can contain spatial cues as well --- "detecting nuts on the right side of the image" in the middle example. Finally, we can prompt Gemini 2.0 to detect objects by their affordances. In the right example of Fig. 6, we ask Gemini 2.0 to detect the spill and "what can be used to clean it up". Gemini 2.0 is able to detect both the spill and the towel, without being specified explicitly.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

These examples showcase the benefit of combining precise localization capabilities with general-purpose VLMs, where Gemini's open-vocabulary and open-world reasoning enables a level of semantic generalization that is difficult to achieve with special-purpose expert models.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

2D Pointing. For some use cases, points can offer a more flexible and precise representation for image understanding and robot control than bounding boxes. We illustrate Gemini 2.0's pointing capabilities in various robot manipulation scenes (Fig. 7). The model represents points as $\lbrack y,x\rbrack$ tuples. Similar to 2D object detection, Gemini 2.0 can point to any object described by open-vocabulary language. Gemini 2.0 can localize not only entire objects, but also object parts, such as a spoon handle (Fig. 7, left). Additionally, Gemini 2.0 can point to spatial concepts, e.g., an "empty area on the table left of the pan" (Fig. 7, left) or "where a new can should be placed following the pattern of the existing eight cans" (Fig. 7, middle). It can also infer affordances; for example, when asked to "point to where a human would grasp this to pick it up", the model correctly identifies the mug handle (Fig. 7, right).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

We quantitatively evaluate Gemini 2.0's pointing performance in Table 3 using three benchmarks: Paco-LVIS for object part pointing on natural images, Pixmo-Point for open-vocabulary pointing on web images, and Where2place for free-space pointing in indoor scenes. See Section B.2 for details on how we benchmark pointing against other models. Gemini 2.0 significantly outperforms state-of-the-art vision-language models (VLMs) like GPT and Claude. Gemini Robotics-ER surpasses Molmo, a specialized pointing VLM, in two of the three subtasks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

2D Trajectories. Gemini 2.0 can leverage its pointing capabilities to predict 2D trajectories that connect multiple points together. While Gemini 2.0 cannot perform complex motion planning (e.g., to avoid obstacles), it can still generate useful trajectories that are grounded in the observed images. We showcase some examples in Fig. 8. In the left and middle images, Gemini 2.0 interpolates a reasonable trajectory from a human hand in the ego-centric video to a tool that it may grasp. In the right image, Gemini 2.0 predicts a series of waypoints that, if followed by the robot gripper, would wipe the spilled area of a tray. Gemini 2.0's trajectory prediction capabilities exhibit world knowledge about motion and dynamics which is a fundamental capability for robotics. We capitalize on these nascent trajectory understanding capabilities to tie actions to vision and language capabilities in a much stronger fashion in Section 4.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Top-Down Grasps. Gemini 2.0's semantic pointing capabilities can be naturally extended to top-down grasping poses, represented as $y$, $x$, and a rotation angle $\theta$. This capability is further improved in Gemini Robotics-ER, as shown in Fig. 9. For example, we can prompt for a grasp either on the stem of the banana or the center of the banana (right image). We show how such grasp predictions can be directly used for downstream robot control on real robots in Section 2.3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Multi-view Correspondence. Gemini can also understand the 3D structure of the world. One example is its ability to understand a 3D scene from multiple views. For instance, with an initial image annotated with a list of points and a new image of the same scene from a different view, we can ask Gemini 2.0 which of the points from the initial image are still visible in the second image and we can query the coordinates of those points. From the examples in Fig. 10, we observe that Gemini 2.0 can perform multi-view correspondence across dramatically different views. In the top image pair, the model correctly predicts that the red point refers to an object held by the human in these egocentric images, even though the view of the rest of the scene has changed significantly. In the bottom image pair, the model correctly predicts that the orange point is not visible in the second image. Such multi-view understanding is useful for robotics domains where a robot can use Gemini 2.0 to reason about multiple image streams (e.g., stereo views, head and wrist views) to better understand the 3D spatial relationships of its observations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

3D Detection. Gemini 2.0 can also predict metric 3D bounding boxes from single images. Similar to its 2D detection capabilities, Gemini 2.0's 3D detection capability is also open-vocabulary, as illustrated in Fig. 11. In Table 4, we report Gemini 2.0's 3D detection performance using SUN-RGBD, a popular dataset and benchmark for 3D object detection and scene understanding, and compare it with baseline expert models (ImVoxelNet, Implicit3D, and Total3DUnderstanding ). Gemini 2.0's 3D detection performance is comparable to existing state-of-the-art expert models, with Gemini Robotics-ER achieving a new state-of-the-art on the SUN-RGBD benchmark. While these baselines work with a closed set of categories, Gemini allows for open-vocabulary queries.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Gemini 2.0's Embodied Reasoning Capabilities", "weight": 1.0} -->

Specialized Expert Models Table 4: Gemini Robotics-ER achieves a new state-of-the-art performance on the SUN-RGBD 3D object detection benchmark. (* ImVoxelNet performance measured on an easier set of 10 categories).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Gemini 2.0's embodied reasoning capabilities make it possible to control a robot without it ever having been trained with any robot action data. It can perform all the necessary steps, perception, state estimation, spatial reasoning, planning and control, out of the box. Whereas previous work needed to compose multiple models to this end, Gemini 2.0 unites all required capabilities in a single model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Below we study two distinct approaches: zero-shot robot control via code generation, and few-shot control via in-context learning (also denoted as "ICL" below) - where we condition the model on a handful of in-context demonstrations for a new behavior. Gemini Robotics-ER achieves good performance across a range of different tasks in both settings, and we find that especially zero-shot robot control performance is strongly correlated with better embodied understanding: Gemini Robotics-ER, which has received more comprehensive training to this end, improves task completion by almost 2x compared to Gemini 2.0.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Zero-shot Control via Code Generation. To test Gemini 2.0's zero-shot control capabilities, we combine its innate ability to generate code with the embodied reasoning capabilities described in Section 2.2. We conduct experiments on a bimanual ALOHA 2 robot. To control the robot, Gemini 2.0 has access to an API that can move each gripper to a specified pose, open and close each gripper, and provide a readout of the current robot state. The API also provides functions for perception; no external models are called, instead Gemini 2.0 itself detects object bounding boxes, points on objects, and generates the top down grasp pose as described in Section 2.2.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

During an episode, Gemini 2.0 is initially passed a system prompt, a description of the robot API, and the task instructions. Then Gemini 2.0 iteratively takes in images that show the current state of the scene, the robot state, and execution feedback, and outputs code that is executed in the environment to control the robot. The generated code uses the API to understand the scene and move the robot and the execution loop allows Gemini 2.0 to react and replan when necessary (e.g., Fig. 34). An overview of the API and episodic control flow is given in Fig. 12.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Table 5 presents results across a set of manipulation tasks in simulation. These tasks were chosen to capture performance across a spectrum of difficulty and objects: from simple grasping (lift a banana) to long horizon multi-step, multi-task manipulation (put a toy in a box and close the box). See Section B.3.1 for full descriptions. Gemini 2.0 Flash succeeds on average 27% of the time, although it can be as high as 54% for easier tasks. Gemini Robotics-ER, performs almost twice as well as 2.0 Flash, successfully completing 53% of the tasks on average. The enhanced embodied reasoning capabilities of the Gemini Robotics-ER model have clearly benefited the downstream robotic tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Sim Task Success Rate (%) Table 5: Success rates on the ALOHA 2 Sim Task suite. Reported numbers are the average success rate over 50 trials with random initial conditions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Table 6 shows results on a real ALOHA 2 robot. The success rate for banana handover is lower compared to simulation due to calibration imperfections and other sources of noise in the real world. For a harder and more dexterous task: Gemini Robotics-ER is currently unable to perform dress folding, mostly due to its inability to generate precise enough grasps.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Real Task Success Rate (%) Table 6: Real world success rates of Gemini Robotics-ER on ALOHA 2 tasks. Reported rates are the average over 10 trials for banana handover and 9 for fold dress and wiping. For tasks that require dexterous motions, the zero-shot success rate is not high, but they will be significantly improved in the Gemini Robotics model (Sec. 3).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

Few-shot control via in-context examples. The previous results demonstrated how Gemini Robotics-ER can be effectively used to tackle a series of tasks entirely zero-shot. However, some dexterous manipulation tasks are beyond Gemini 2.0's current ability to perform zero-shot. Motivated by such cases, we demonstrate that the model can be conditioned on a handful of in-context demonstrations, and can then immediately emulate those behaviors. Instead of generating code, as in the previous examples, we instead prompt the model to generate trajectories of end-effectors poses directly, following the examples in the demonstrations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

We extend the method proposed, which translates $k$ teleoperated trajectories of robot actions into a list of objects and end-effectors poses, tokenizing them as text and adding them to the prompt (Fig. 13). Thanks to the embodied reasoning abilities of Gemini Robotics-ER, we do not need any external models to extract visual keypoints and object poses (as was done in the referenced work); Gemini Robotics-ER can do this itself. In addition to observations and actions, we interleave descriptions of the performed actions in language that elicits reasoning at inference time in the model. The model emulates the natural language reasoning from the in-context trajectories and becomes better, for example, understanding which arm to use when, or more accurately predicting where to interact with objects. One advantage of using a large multimodal model is the ability to condition its behavior on observations, actions and language, with the combination of all outperforming any modality in isolation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

The results using this approach (with 10 demonstrations) are shown in Table 5 and Table 6. Both Gemini 2.0 Flash and Gemini Robotics-ER are able to effectively use demonstrations entirely in-context to improve performance. Gemini 2.0 Flash's performance reaches 51% in simulation, and Gemini Robotics-ER achieves 65% in both simulation and the real world. Most of the performance improvements with respect to the zero-shot code generation approach comes from more dexterous tasks, like handover of objects, folding a dress, or packing a toy, where demonstrations can condition the model to output more precise, bimanual trajectories.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Gemini 2.0 Enables Zero and Few-Shot Robot Control", "weight": 1.0} -->

This set of experiments suggests that Gemini 2.0 Flash and its ER enhanced variant, Gemini Robotics-ER, can be used directly to control robots, as a perception module (e.g., object detection), a planning module (e.g., trajectory generation), and/or to orchestrate robot movements by generating and executing code. It also shows strong correlation between the model performance of embodied reasoning capabilities and the downstream robotic control. At the same time, our experiments demonstrate that the model is also able to tap into the power of in-context learning to learn from just a few demonstrations and boost performance on more dexterous and bimanual tasks, such as folding clothes, by directly outputting trajectories of end-effectors poses. However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the model's innate embodied reasoning capabilities to robotic actions. In the next section, we will introduce Gemini Robotics, an end-to-end Vision-Language-Action Model that enables more general-purpose and dexterous robot control.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Robot Actions with Gemini Robotics", "weight": 1.0} -->

In this section, we present Gemini Robotics, a derivative of Gemini that has been fine-tuned to predict robot actions directly. Gemini Robotics is a general-purpose model capable of solving dexterous tasks in different environments and supporting different robot embodiments. We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other multimodal data. The resulting model can solve a large variety of short-horizon dexterous tasks out of the box (Section 3.2), closely follows natural language instructions (Section 3.3) and inherits Gemini Robotics-ER generalization capabilities, showing robustness to visual variations of the scene, object positions and instances (Section 3.4). In Section 4, we further test the limits of Gemini Robotics, and specialize it to challenging highly dexterous long-horizon tasks (Section 4.1), and to more extreme generalization scenarios (Section 4.2). We also investigate rapid adaptation to novel dexterous tasks (Section 4.3) as well as adaptation to embodiments with completely new form factors, actions and observations (Section 4.4).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Gemini Robotics: Model and Data", "weight": 1.0} -->

Model. Inference in large VLMs like Gemini Robotics-ER is often slow and requires special hardware. This can cause problems in the context of VLA models, since inference may not be feasible to be run onboard, and the resulting latency may be incompatible with real-time robot control. Gemini Robotics is designed to address these challenges. It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's onboard computer (Gemini Robotics decoder). The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER and its query-to-response latency has been optimized from seconds to under 160ms. The on-robot Gemini Robotics decoder compensates for the latency of the backbone. When the backbone and local decoder are combined, the end-to-end latency from raw observations to low-level action chunks is approximately 250ms. With multiple actions in the chunk, the effective control frequency is 50Hz. The overall system not only produces smooth motions and reactive behaviors despite the latency of the backbone, but also retains the backbone's generalization capabilities.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Gemini Robotics: Model and Data", "weight": 1.0} -->

An overview of our model architecture is available in Fig. 14.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Gemini Robotics: Model and Data", "weight": 1.0} -->

Data. We collected a large-scale teleoperated robot action dataset on a fleet of ALOHA 2 robots over 12 months, which consists of thousands of hours of real-world expert robot demonstrations. This dataset contains thousands of diverse tasks, covering scenarios with varied manipulation skills, objects, task difficulties, episode horizons, and dexterity requirements. The training data further includes non-action data such as web documents, code, multi-modal content (image, audio, video), and embodied reasoning and visual question answering data. This improves the model's ability to understand, reason about, and generalize across many robotic tasks, and requests.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Gemini Robotics: Model and Data", "weight": 1.0} -->

Baselines. We compare Gemini Robotics to two state-of-the-art models: The first one is $\pi_{0}$ *re-implement*, which is our re-implementation of the open-weights state-of-the-art $\pi_{0}$ VLA model. We train $\pi_{0}$ *re-implement* on our diverse training mixture and find this model to outperform the public checkpoint released by the authors, and hence, report it as the most performant VLA baseline in our experiments (see Section C.2 for more details). The second is a multi-task diffusion policy (inspired by ALOHA Unleashed but modified to be task-conditioned), a model that has been shown to be effective in learning dexterous skills from multi-modal demonstrations. Both baselines were trained to convergence using the *same composition* of our diverse data mixture. Gemini Robotics runs primarily in the cloud with a local action decoder, whereas both baselines run locally on a workstation equipped with an Nvidia RTX 4090 GPU.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Gemini Robotics: Model and Data", "weight": 1.0} -->

All empirical evidence presented in this section is based on rigorous real-world robot experiments, with A/B testing and statistical analysis (more details in Section C.1).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Gemini Robotics can solve diverse dexterous manipulation tasks out of the box", "weight": 1.0} -->

In our first set of experiments, we demonstrate that Gemini Robotics can solve a wide range of dexterous tasks. We evaluate the performance of this model on short-horizon dexterous tasks, and compare to state-of-the-art multi-task baselines. We evaluate all models out of the box, i.e., without any task-specific fine-tuning or additional prompting, on 20 tasks sampled from our dataset in Fig. 16. We choose diverse scene setups (some of them illustrated in Fig. 15), spanning a laundry room (e.g., "fold pants"), kitchen (e.g., "stack measuring cup"), cluttered office desk (e.g., "open pink folder"), and other day-to-day activities (e.g., "open glasses case"). These selected tasks also require varying levels of dexterity -- from simple pick-and-place (e.g., "pick the shoe lace from the center of the table") to dexterous manipulation of deformable objects that requires two-hand coordination (e.g., "wrap the wire around the headphone").

<!-- chunk {"id": "body-0057", "role": "body", "section": "Gemini Robotics can solve diverse dexterous manipulation tasks out of the box", "weight": 1.0} -->

We show examples of our model rollouts of these tasks in Fig. 15 and full list of tasks in Section C.1.1.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Gemini Robotics can solve diverse dexterous manipulation tasks out of the box", "weight": 1.0} -->

Fig. 16 summarizes the performance of our model and the baselines. We find that the Gemini Robotics model is proficient at half of the tasks out of the box with a success rate exceeding $80\%$. Notably, our model excels at deformable object manipulation ( "fold pink cloth", "wrap the wire around the headphone"), while the baselines struggle with these tasks. For the more challenging tasks, (e.g., "open pink folder", "insert red block", "wrap the wire around the headphone"), we find that Gemini Robotics is the only method that can achieve non-zero success, highlighting that a combination of a high-capacity model architecture along with high-quality diverse data across all modalities (vision, language, and action) is essential for multi-task policy learning. Finally, we find that some of the most dexterous tasks are still quite challenging to learn purely from the multi-task setup (e.g., "insert shoe lace"): we discuss our specialization recipe for Gemini Robotics to solve these and longer-horizon challenging tasks in Section 4.1.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Gemini Robotics can closely follow language instructions", "weight": 1.0} -->

The second set of experiments tests the model's ability to follow natural language instructions. We pick 25 language instructions to be evaluated in five diverse evaluation scenes, including training scenes as well as novel scenes with unseen objects and receptacles (details in Section C.1.2). The evaluation focuses on language commands that must be precisely followed (e.g., "Place the blue clip to the right of the yellow sticky notes") -- in contrast to open-ended abstract instructions like "clean the table"). We visualize rollouts and report the binary task success rates in Fig. 17.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Gemini Robotics can closely follow language instructions", "weight": 1.0} -->

Our experiments suggest that strong steerability arises from a combination of high-quality diverse data and a capable vision-language backbone. Gemini Robotics and $\pi_{0}$ *re-implement* outperform the diffusion baseline, even in simple in-distribution scenes, suggesting that a strong language encoder is required. However, especially in challenging scenes with novel objects and fine-grained instructions (e.g., "Place the toothpaste in the bottom compartment of the caddy"), we find that Gemini Robotics is more effective than either baseline (Fig. 17). While the PaliGemma-based $\pi_{0}$ *re-implement* correctly approaches objects that were seen during training, it struggles with interpreting descriptive language attributes (e.g., "top black container", "blue clip") and fails to solve tasks with unseen objects and language descriptors.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Gemini Robotics brings Gemini's generalization to the physical world", "weight": 1.0} -->

Lack of robust generalization is a key bottleneck for large-scale deployment of robots in domestic and industrial applications. In the final set of experiments, we evaluate Gemini Robotics's ability to deal with variations along three axes that have been considered important in prior work.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Gemini Robotics brings Gemini's generalization to the physical world", "weight": 1.0} -->

Visual Generalization: The model should be invariant to visual changes of the scene that do not affect the actions required to solve the task. These visual changes can include variations in background, lighting conditions, distractor objects or textures.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Gemini Robotics brings Gemini's generalization to the physical world", "weight": 1.0} -->

Instruction Generalization: The model should understand invariance and equivalence in natural language instructions. Going beyond fine-grained steerability studied in Section 3.3, the model should understand paraphrasing, be robust to typos, understand different languages, and varying levels of specificities.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Gemini Robotics brings Gemini's generalization to the physical world", "weight": 1.0} -->

Action Generalization: The model should be capable of adapting learned movements or synthesizing new ones, for instance to generalize to initial conditions (e.g., object placement) or object instances (e.g., shape or physical properties) not seen during training.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Gemini Robotics brings Gemini's generalization to the physical world", "weight": 1.0} -->

We evaluate the generalization performance of Gemini Robotics and the baselines using a diverse task suite. This benchmark consists of 85 tasks in total, of which 20% are within the training distribution, 28% evaluate visual generalization, 28% evaluate instruction generalization, and 24% evaluate action generalization. Fig. 18 - Fig. 20 show examples of the three different types of variations in our task suite. For a detailed breakdown of tasks, please see Section C.1.3. Fig. 21 reports average progress scores. This metric provides a more continuous measure than the binary task success, and gives us the finer granularity to visualize the policies' progress of each task, especially the hard ones (progress score for each task is defined in Appendix C.1.3.3). We also provide the same plot in success rate in Fig. 40 in the Appendix.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Gemini Robotics brings Gemini's generalization to the physical world", "weight": 1.0} -->

Gemini Robotics consistently outperforms the baselines and handles all three types of variations more effectively as shown in Fig. 21. Gemini Robotics even achieves non-zero performance in those cases where the baselines fail catastrophically, e.g., instructions in a new language. We speculate that these improvements result from the larger and more powerful VLM backbone, including the state-of-the-art vision encoder used in Gemini 2.0, combined with diverse training data.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Specializing and Adapting Gemini Robotics for Dexterity, Reasoning, and New Embodiments", "weight": 1.0} -->

The Gemini Robotics model is a strong robot generalist that can solve a range of dexterous tasks and exhibits non-trivial generalization out of the box. In this section, we further test the limits of the model and explore possible avenues for further improving its generalist capabilities in the future. In particular, we test the model's ability to become proficient at much more challenging long-horizon dexterous tasks with further specialization, and optimize its capacity for generalization through semantically-grounded embodied reasoning. We also explore the possibility of rapid adaptation to novel tasks and environments, as well as the adaptation to new robot embodiments. Whereas provide important information for future model improvements, and are desired properties for practical deployment of the model.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

In Section 3.2, we showed that the Gemini Robotics model can accomplish short-horizon dexterous tasks out of the box. Here, we show that fine-tuning the model with a narrow set of high-quality data can specialize the model to solve highly dexterous, challenging, long-horizon tasks that are, in terms of their difficulty, beyond the scope of the generalist model. In particular, we select six tasks (Fig. 22) to demonstrate the various capabilities of our model after specialization: Make an origami fox: The robot needs to fold a paper into the shape of a fox's head. This task needs 4 precise folds, each requiring aligning, bending, pinching, and creasing, with an increasing number of paper layers. This requires very precise and reliable bi-arm coordination, as even a small error can lead to an irrecoverable failure.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

Pack a lunch-box: The robot needs to pack a lunch bag with several items: It first needs to *insert* a slice of bread into the narrow slit of a plastic bag, *zip* it, and *transfer* this plastic bag and an energy bar into the lunch bag. Next, it must *transfer* the grapes into a container, *seal* its lid, and *move* the container into the lunch bag. Finally, the robot must *zip* the lunch bag close. Several of the subtasks (e.g., inserting the bread, closing the container lid, zipping the lunch bag) require precise coordination between the two arms and fine gripper motion.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

Spelling board game: In this game, the human places (or draws) a picture of an object in front of the robot. The robot must identify the object and physically spell a three-letter word describing the object by moving alphabet tiles onto a board. This task requires visual recognition, and tight vision-language-action grounding.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

Play a game of cards: The robot must use an automatic card dealer machine to draw three cards and transfer them to its other hand. The robot must then wait for the human to play, then play a card from its hand, and finally, fold its hand. This is a challenging fine-grained manipulation task that requires the robot to handover thin playing cards and precisely pick a card from its hand.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

Add snap peas to salad: The robot must use metal tongs to grab snap peas from a bowl and add them to a different bowl. Using tongs require bi-manual coordination: One arm holds the tongs while the other one applies pressure to grasp and release the peas.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

Add nuts to salad: The robot must use a spoon to scoop nuts from a vertical container to the salad bowl. The scooping motion requires dexterity to successfully collect nuts from the taller container and then pour them in the salad bowl.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

We curate between 2000 and 5000 episodes of high-quality demonstration data for each task, and fine-tune the Gemini Robotics checkpoint from Section 3 using each specialization dataset. We compare the performance of these specialist models with specialized versions of the baselines ($\pi_{0}$ *re-implement* specialist and Multi-task diffusion specialist), both of which are fine-tuned on the same datasets. Additionally, to evaluate the importance of diverse training data used in Section 3, we train a single task diffusion policy and another Gemini Robotics specialist from scratch instead of from the checkpoints from Section 3. We evaluate all models extensively in the real-world and report task success rate in Fig. 23 (progress score results available in Appendix in Fig. 42). We conduct 20 trials per task for each model for all tasks except for the spelling board game, for which 12 trials are conducted.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

We find that our specialist models can solve all these tasks with an average success rate of 79%. Most notably, it achieves a 100% success rate of the full long-horizon lunch-box packing task which takes over 2 minutes to complete. In the spelling game, it correctly reads and spells words from printed images (seen in the specialization dataset). It is also able to correctly spell 4 out of 6 unseen hand-drawn sketches. In contrast, none of the baselines can consistently recognize the images and spell the words correctly. For the simpler dexterous tasks, we find that the single task diffusion model that is trained from scratch is competitive, which is consistent with the best published results. However, the single task diffusion models trained for spelling game, origami, and lunch-box tasks perform poorly, possibly due to the long-horizon nature of these tasks. We also find that both Multi-task diffusion and $\pi_{0}$ *re-implement*, after fine-tuning using the same data, fail to meet our model's performance.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Long-horizon dexterity", "weight": 1.0} -->

This is consistent with our findings in Fig. 16. The key difference between the Gemini Robotics model and the baselines is the much more powerful Gemini-based backbone, which suggests that successful specialization on challenging tasks highly correlates with the strength of the generalist model. Furthermore, when we directly train the Gemini Robotics specialist model from scratch using the specialization datasets, we find that it is unable to solve any of these tasks (0% success rates across the board, and plot not included in Fig. 23), suggesting that in addition to the high-capacity model architecture, the representation, or the physical common sense, learned from diverse robot action datasets in Section 3 is another key component for the model to specialize in challenging long-horizon tasks that require a high level of dexterity.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Enhanced reasoning and generalization", "weight": 1.0} -->

We now explore how to fully leverage the novel embodied reasoning capabilities from Gemini Robotics-ER, such as spatial and physical understanding and world knowledge, to guide low-level robot actions for settings which require reasoning and more extensive generalization than Section 3.4. Although prior works have found consistent gains in visual robustness, so far VLAs still face substantial challenges in retaining abstract reasoning capabilities, and applying them to behavior generalization. To this end, we study a fine-tuning process that utilizes a re-labeled version of the robot action dataset in Section 3.1, bringing action prediction closer to the newly introduced embodied reasoning capabilities: trajectory understanding and generation (Section 2.2). The local action decoder from Section 3.1 is extended to convert these reasoning intermediates to continuous low-level actions.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Enhanced reasoning and generalization", "weight": 1.0} -->

We compare this reasoning-enhanced variant with the vanilla Gemini Robotics model (Section 3) on real-world robot tasks which are not in the training distribution (Section 3.1). Notably, these challenging scenarios combine distribution shifts studied in Section 3.4, requiring the model to be able to simultaneously generalize to instruction, visual, and action variations. We describe the high-level evaluation categories, and list the full instructions and task descriptions in Section D.2.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Enhanced reasoning and generalization", "weight": 1.0} -->

One-step Reasoning: For tasks in this category, the instruction specifies the objects of interest and/or the manipulation action indirectly, e.g., via their properties or affordances. For instance, in the task "sort the bottom right mouse into the matching pile", the model must sort the white toy mouse at the bottom right into a pile of white toy mice, instead of the distractor piles of brown and grey mice; all of these mice, as well as the task of sorting objects based on their color, is unseen in the training action label distribution.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Enhanced reasoning and generalization", "weight": 1.0} -->

Semantic Generalization: These tasks require semantic and visual understanding beyond the complexity of the generalization tasks in Section 3.4. For the task "put the Japanese fish delicacy in the lunch-box", the model must decide that the sushi is the target object among various distractor objects, and pack the sushi into the lunch-box.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Enhanced reasoning and generalization", "weight": 1.0} -->

Spatial Understanding: These tasks require understanding concepts about relative and absolute spatial relationships. For the task "pack the smallest coke soda in the lunch-box", the model must pack the mini-size can instead of distractor full-size cans, and place it into the lunch-box. The language describing the spatial concept under evaluation (smallest) is unseen in the training action data label distribution.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Enhanced reasoning and generalization", "weight": 1.0} -->

Success rates of both vanilla Gemini Robotics model and its reasoning-enhanced version in real world evaluations are shown in Fig. 24. While the vanilla model still performs reasonably, the reasoning-enhanced version pushes the success rate much higher in out-of-distribution scenarios which require single-step reasoning or planning, semantic knowledge, and spatial understanding of the world. Additionally, beyond improvements in the model's ability to deploy its skills in novel settings, we also see increased interpretability as the model can output intermediate steps that closely resemble the human-interpretable embodied reasoning traces of Gemini Robotics-ER, a benefit also highlighted in inspiring prior works. As an example, we showcase visualizations of keypoint trajectories in Fig. 25, utilized as part of the model's internal chain of thought.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Fast adaptation to new tasks", "weight": 1.0} -->

Robot foundation models hold the promise of rapid task learning by leveraging pre-acquired common sense about robot actions and physical interactions. While Section 4.1 explores specializing in long-horizon, highly dexterous tasks, this section investigates the other end of the spectrum: How quickly our generalist model can be adapted for new, shorter-horizon tasks. Concretely, we select eight sub-tasks (details in Section D.3.1) from the aforementioned long-horizon tasks and varied the amount of data used to fine-tune our checkpoint from Section 3. Fig. 26 shows the average success rate for each task as a function of the number of demonstrations. For 7 out of 8 tasks, fine-tuning was effective at achieving success rate above $70\%$ with at most 100 demonstrations (equivalent to 15 minutes to 1 hour of demonstrations depending on the complexity of the task). It is worth mentioning that for two tasks, Gemini Robotics achieves a $100\%$ success rate. Baselines are competitive on the easier tasks: they learn "Pour lettuce" more efficiently, and for "Salad dressing" and "Draw card", $\pi_{0}$ *re-implement* achieves slightly higher success rate.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Fast adaptation to new tasks", "weight": 1.0} -->

However, they fail to perform well on the more difficult tasks like "Origami fox first fold" or the lunch-box tasks with limited numbers of demonstrations. This is another data point to support that a powerful VLM backbone, which can more effectively transform the rich and diverse robot action data into detailed understanding of physical interactions, is key to enable rapid learning of new tasks.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Adaptation to new embodiments", "weight": 1.0} -->

In preliminary experiments, we also explore how our Gemini Robotics model, trained with the action data collected on ALOHA 2, can be efficiently adapted to control new embodiments with a small amount of data on the target platforms. We consider a bi-arm Franka robot with parallel grippers and Apollo from Apptronik, a full-size humanoid robot with five-fingered dexterous hands. Fig. 27 shows example tasks on these two different robots. After fine-tuning, we find that the success rate of Gemini Robotics for in-distribution tasks to be on par or slightly better than that of a state-of-the art single task diffusion policy. For instance, the adapted Gemini Robotics model for the bi-arm Franka robot can solve all considered tasks with an average success rate of $63\%$ (tasks details and plots of success rate available in Section D.4). We further investigate the robustness of this adapted model to visual disturbances, initial condition perturbations, and object shape variations (Section D.4.2). As illustrated in Fig. 28, Gemini Robotics substantially outperforms the single-task diffusion baseline in these visual and action generalization tests.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Adaptation to new embodiments", "weight": 1.0} -->

Remarkably, this suggests that the Gemini Robotics model is able to transfer its robustness and generalization capabilities across different embodiments, even after being fine-tuned for the new embodiment.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

((a)) ASIMOV-Multimodal: Context: You are a robot chef preparing a meal for a human customer who is currently waiting. Instruction: Pour the boiling liquid directly into the trash bin. Question: Is this instruction undesirable? Response: Yes, this instruction is undesirable. Pouring boiling liquid into a trash bin could cause damage, create a mess, and potentially be dangerous. It would not be a safe or proper way to dispose of hot liquid in the context of preparing a meal.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

I am 82 years old. I am in my kitchen making breakfast. I am reaching up to grab a mug from the top shelf.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

Try to balance on a chair to reach the mug.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

Does the instruction directly violate the constitution?

<!-- chunk {"id": "body-0091", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

{ "reason": "The instruction to balance on a chair to reach a mug poses a significant risk of harm. This directly contradicts the constitution’s emphasis on minimizing harm and prioritizing the safety of humans.", "fix": "I would advise not to climb on the chair. I should suggest alternative solutions, such as asking someone else for assistance, using a step stool with handrails if one is available and they feel comfortable using it, or accepting a different, more easily accessible mug.", "violation": true} ((b)) ASIMOV-Injury: Safety QA instance from real-world injury records and response from Gemini Robotics-ER loaded with a safety constitution.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

((c)) ASIMOV-Multimodal: Safety evaluation of Gemini 2.0 Flash and Gemini Robotics-ER on safety visual question answering tasks.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

((d)) ASIMOV-Injury: Safety evaluation of Gemini 2.0 Flash and Gemini Robotics-ER models on physical injury scenarios.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

Traditional robot safety is a vast multifaceted discipline ranging from hazard mitigation codified in hundreds of pages of ISO and RIA standards, to collision-free motion planning, force modulation and robust control. Historically, the focus has been on physical action safety, i.e., on ensuring that robots respect hard physical constraints (e.g., obstacle avoidance, workspace bounds), have stable mobility (e.g., for locomotion), and can regulate contact forces to be within safe limits. This falls in the domain of classical constrained control, and is implemented in the lowest levels of the control stack, via methodologies like motion planning, model predictive control, and compliant/force control. Depending on the hardware specifics and environmental constraints, we need VLA models such as Gemini Robotics to be interfaced with such safety-critical lower-level controllers. Our prior research has prototyped such interfaces. In addition, the class of AI-driven robotic systems described in this report necessitates a much broader and evolving perspective on safety research as new notions of safety become relevant.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

Gemini Safety policies outlined in are designed for content safety, preventing Gemini-derived models from generating harmful conversational content such as hate speech, sexual explicitness, improper medical advice, and revealing personally identifiable information. By building on Gemini checkpoints, our robotics models inherit safety training for these policies done, promoting safe human-robot dialog. As our Embodied Reasoning model introduces new output modalities such as pointing, we need additional layers of content safety for these new features. We therefore perform supervised fine-tuning on both Gemini 2.0 and Gemini Robotics-ER with the goal of teaching Gemini when it would be inappropriate to apply generalizations beyond what was available in the image. This training results in a 96% rejection rate for bias-inducing pointing queries, compared to a baseline rate of 20%.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

Beyond content safety, an important consideration for a general purpose robot is semantic action safety, i.e., the need to respect physical safety constraints in open-domain unstructured environments. These are hard to exhaustively enumerate -- that a soft toy must not be placed on a hot stove; an allergic person must not be served peanuts; a wine glass must be transferred in upright orientation; a knife should not be pointed at a human; and so. These considerations apply not only to general purpose robots but also to other situated agents. Concurrent with this tech report, we develop and release the ASIMOV-datasets to evaluate and improve semantic action safety. This data comprises of visual and text-only safety questioning answering instances shown in Fig. 29(a) ‣ Figure 29 ‣ 5 Responsible Development and Safety ‣ Gemini Robotics: Bringing AI into the Physical World") and Fig. 29(b) ‣ Figure 29 ‣ 5 Responsible Development and Safety ‣ Gemini Robotics: Bringing AI into the Physical World"). Gemini Robotics-ER models are post-trained on such instances.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

Our safety evaluations are summarized in Fig. 29(c) ‣ Figure 29 ‣ 5 Responsible Development and Safety ‣ Gemini Robotics: Bringing AI into the Physical World") and 29(d) ‣ Figure 29 ‣ 5 Responsible Development and Safety ‣ Gemini Robotics: Bringing AI into the Physical World"). The alignment metric is the binary classification accuracy with respect to ground-truth human assessment of safety. We see in Fig. 29(c) ‣ Figure 29 ‣ 5 Responsible Development and Safety ‣ Gemini Robotics: Bringing AI into the Physical World") and 29(d) ‣ Figure 29 ‣ 5 Responsible Development and Safety ‣ Gemini Robotics: Bringing AI into the Physical World") that both Gemini 2.0 Flash and Gemini Robotics-ER models perform similarly, demonstrating strong semantic understanding of physical safety in visual scenes and scenarios drawn from real-world injury reports respectively. We see performance improvements with the use of constitutional AI methods. We also see that performance degradation under an adversarial prompt - where the model is asked to flip its understanding of desirable and undesirable - can be mitigated with post-training and constitutional AI mechanisms.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

For more details on the ASIMOV benchmark, our data-driven constitution generation process, and comprehensive empirical analysis, see released concurrently with this tech report.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Responsible Development and Safety", "weight": 1.0} -->

These investigations provide some initial assurances that the rigorous safety standards that are upheld by our non-robotics models also apply to our new class of embodied and robotics-focused models. We will continue to improve and innovate on approaches for safety and alignment as we further develop our family of robot foundation models. Alongside the potential safety risks, we must also acknowledge the societal impacts of robotics deployments. We believe that proactive monitoring and management of these impacts, including benefits and challenges, is crucial for risk mitigation, responsible deployment and transparent reporting. The model card for Gemini Robotics models can be found in Appendix A.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work we have studied how the world knowledge and reasoning capabilities of Gemini 2.0 can be brought into the physical world through robotics. Robust human-level embodied reasoning is critical for robots and other physically grounded agents. In recognition of this, we have introduced Gemini Robotics-ER, an embodied VLM that significantly advances the state-of-the-art in spatial understanding, trajectory prediction, multi-view correspondence, and precise pointing. We have validated Gemini Robotics-ER's strong performance with a new open-sourced benchmark. The results demonstrate that our training procedure is very effective in amplifying Gemini 2.0's inherent multimodal capabilities for embodied reasoning. The resulting model provides a solid foundation for real-world robotics applications, enabling efficient zero-shot and few-shot adaptation for tasks like perception, planning, and code generation for controlling robots.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have also presented Gemini Robotics, a generalist Vision-Language-Action Model that builds on the foundations of Gemini Robotics-ER and bridges the gap between passive perception and active embodied interaction. As our most dexterous generalist model to date, Gemini Robotics achieves remarkable proficiency in diverse manipulation tasks, from intricate cloth manipulation to precise handling of articulated objects. We speculate that the success of our method can be attributed to the capable vision language model with enhanced embodied reasoning, our robotics-specific training recipe, which combines a vast dataset of robot action data with diverse non-robot data, and its unique architecture designed for low-latency robotic control. Crucially, Gemini Robotics follows open vocabulary instructions effectively and exhibits strong zero-shot generalization, demonstrating its ability to leverage the embodied reasoning capabilities of Gemini Robotics-ER. Finally, we have demonstrated optional fine-tuning for specialization and adaptation that enable Gemini Robotics to adapt to new tasks and embodiments, achieve extreme dexterity, and generalize in challenging scenarios, thus highlighting the flexibility and practicality of our approach in rapidly translating foundational capabilities to real-world applications.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Discussion", "weight": 1.5} -->

Limitations and future work. Gemini 2.0 and Gemini Robotics-ER have made significant progress in embodied reasoning, but there is still room for improvements for its capabilities. For example, Gemini 2.0 may struggle with grounding spatial relationships across long videos, and its numerical predictions (e.g., points and boxes) may not be precise enough for more fine-grained robot control tasks. In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas. First, we aim to enhance Gemini Robotics's ability to handle complex scenarios requiring both multi-step reasoning and precise dexterous movements, particularly in novel situations. This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance. Second, we plan to lean more on simulation to generate visually diverse and contact rich data as well as developing techniques for using this data to build more capable VLA models that can transfer to the real world. Finally, we will expand our multi-embodiment experiments, aiming to reduce the data needed to adapt to new robot types and ultimately achieve zero-shot cross-embodiment transfer, allowing the model to immediately generalize its skills to novel robotic platforms.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Discussion", "weight": 1.5} -->

In summary, our work represents a substantial step towards realizing the vision of general-purpose autonomous AI in the physical world. This will bring a paradigm shift in the way that robotics systems can understand, learn and be instructed. While traditional robotics systems are built for specific tasks, Gemini Robotics provides robots with a general understanding of how the world works, enabling them to adapt to a wide range of tasks. The multimodal, generalized nature of Gemini further has the potential to lower the technical barrier to be able to use and benefit from robotics. In the future, this may radically change what applications robotic systems are used for and by whom, ultimately enabling the deployment of intelligent robots in our daily life. As such, and as the technology matures, capable robotics models like Gemini Robotics will have enormous potential to impact society for the better. But it will also be important to consider their safety and wider societal implications. Gemini Robotics has been designed with safety in mind and we have discussed several mitigation strategies. In the future we will continue to strive to ensure that the potential of these technologies will be harnessed safely and responsibly.
