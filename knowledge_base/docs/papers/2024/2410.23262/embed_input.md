EMMA: End-to-End Multimodal Model for Autonomous Driving

Topics include Autonomous driving, Multimodal models, Vision-language models, End-to-end driving, Motion planning, 3D object detection, Road graph prediction, Generalist models.

Introduces EMMA, a camera-primary multimodal model that casts driving tasks such as trajectory planning, object detection, and road graph prediction into a unified language-style output space. The central value is showing how pretrained multimodal world knowledge can be co-trained with driving-specific prompts, while also exposing current limits in frame context, sensor coverage, and compute cost.

We introduce EMMA, an End-to-end Multimodal Model for Autonomous driving. Built upon a multi-modal large language model foundation like Gemini, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planner trajectories, perception objects, and road graph elements. EMMA maximizes the utility of world knowledge from the pre-trained large language models, by representing all non-sensor inputs (e.g. navigation instructions and ego vehicle status) and outputs (e.g. trajectories and 3D locations) as natural language text. This approach allows EMMA to jointly process various driving tasks in a unified language space, and generate the outputs for each task using task-specific prompts. Empirically, we demonstrate EMMA's effectiveness by achieving state-of-the-art performance in motion planning on nuScenes as well as competitive results on the Waymo Open Motion Dataset (WOMD). EMMA also yields competitive results for camera-primary 3D object detection on the Waymo Open Dataset (WOD)....

## Introduction

Autonomous driving technology has made significant progress in recent years. To make autonomous vehicles a ubiquitous form of transportation, they must navigate increasingly complex real-world scenarios that require understanding rich scene context as well as sophisticated reasoning and decision-making.

Historically, autonomous driving systems employed a modular approach, consisting of specialized components for perception, mapping, prediction (Nayakanti et al. Shi et al., ), and planning (Teng et al. Lioutas et al., ). While this design lends itself to easier debugging and optimization of individual modules, it poses scalability challenges due to the limited inter-module communication. In particular, the expert-designed interfaces between modules, such as the perception and behavior modules, may struggle to adapt to novel environments because they are often pre-defined based on targeted scenarios (Bansal et al. Jiang et al....

## Conclusion

In this paper, we present EMMA, a Gemini-powered end-to-end multimodal model for autonomous driving. It treats Gemini as a first class citizen and recasts autonomous driving tasks as vision question answering problems to fit the paradigm of MLLMs, aiming at maximizing the utility of Gemini's world knowledge and its reasoning capability equipped with chain-of-thought tools. Unlike historical cascaded systems with specialized components, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planning trajectories, perception objects, and road graph elements....

Table 2: End-to-end motion planning experiments on an internal planning benchmark. CoT denotes equipping with chain-of-thought reasoning (Eq. 3). EMMA+ achieves the best quality across different prediction time horizons. EMMA† and EMMA+† denotes using PaLI-X as our base model, while the default EMMA and EMMA+ use Gemini as the base model. ∗Enhanced, reproduced baselines.

While edges within each polyline are directional, each polyline does not necessarily have a unique order relative to the other elements. This bears similarity to object detection (e.g., ), where each box is defined by ordered attributes (top-left corner, bottom-right corner), but a relative ordering between boxes does not necessarily exist....
