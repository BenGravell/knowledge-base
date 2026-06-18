EMMA: End-to-End Multimodal Model for Autonomous Driving

Topics include Autonomous driving, Multimodal models, Vision-language models, End-to-end driving, Motion planning, 3D object detection, Road graph prediction, Generalist models.

Introduces EMMA, a camera-primary multimodal model that casts driving tasks such as trajectory planning, object detection, and road graph prediction into a unified language-style output space. The central value is showing how pretrained multimodal world knowledge can be co-trained with driving-specific prompts, while also exposing current limits in frame context, sensor coverage, and compute cost.

We introduce EMMA, an End-to-end Multimodal Model for Autonomous driving. Built upon a multi-modal large language model foundation like Gemini, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planner trajectories, perception objects, and road graph elements. EMMA maximizes the utility of world knowledge from the pre-trained large language models, by representing all non-sensor inputs (e.g. navigation instructions and ego vehicle status) and outputs (e.g. trajectories and 3D locations) as natural language text. This approach allows EMMA to jointly process various driving tasks in a unified language space, and generate the outputs for each task using task-specific prompts. Empirically, we demonstrate EMMA's effectiveness by achieving state-of-the-art performance in motion planning on nuScenes as well as competitive results on the Waymo Open Motion Dataset (WOMD). EMMA also yields competitive results for camera-primary 3D object detection on the Waymo Open Dataset (WOD).

## Introduction

Autonomous driving technology has made significant progress in recent years. To make autonomous vehicles a ubiquitous form of transportation, they must navigate increasingly complex real-world scenarios that require understanding rich scene context as well as sophisticated reasoning and decision-making.

Historically, autonomous driving systems employed a modular approach, consisting of specialized components for perception, mapping, prediction (Nayakanti et al. Shi et al., ), and planning (Teng et al. Lioutas et al., ). While this design lends itself to easier debugging and optimization of individual modules, it poses scalability challenges due to the limited inter-module communication.

We introduce the End-to-End Multimodal Model for Autonomous Driving (EMMA), built on top of a multimodal large language model, such as Gemini or PaLI without additional specialized components. Figure shows the overview of the EMMA framework. EMMA accepts camera images and plain text for other non-vision inputs such as high-level driving commands and historical context. By recasting driving tasks as visual question answering (VQA) problems, EMMA leverages Gemini's pre-trained capabilities and extensive world knowledge.

EMMA exhibits strong performance in end-to-end motion planning, achieving state-of-the-art performance on public benchmarks nuScenes and competitive results on the Waymo Open Motion Dataset (WOMD). We also show that we can further improve motion planning quality with more internal training data and chain-of-thought reasoning.

Finally, we show EMMA's capacity to reason and make decisions in complex, long-tail driving scenarios.

## Conclusion

In this paper, we present EMMA, a Gemini-powered end-to-end multimodal model for autonomous driving. It treats Gemini as a first class citizen and recasts autonomous driving tasks as vision question answering problems to fit the paradigm of MLLMs, aiming at maximizing the utility of Gemini's world knowledge and its reasoning capability equipped with chain-of-thought tools. Unlike historical cascaded systems with specialized components, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planning trajectories, perception objects, and road graph elements.
