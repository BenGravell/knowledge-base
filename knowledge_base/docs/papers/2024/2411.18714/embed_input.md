Explainable Deep Learning Improves Human Mental Models of Self-driving Cars

Topics include Safety, Neural networks, Deep learning, Causal inference, Learning, Self driving, Mental model.

Self-driving cars increasingly rely on deep neural networks to achieve human-like driving. The opacity of such black-box planners makes it challenging for the human behind the wheel to accurately anticipate when they will fail, with potentially catastrophic consequences. While research into interpreting these systems has surged, most of it is confined to simulations or toy setups due to the difficulty of real-world deployment, leaving the practical utility of such techniques unknown. Here, we introduce the Concept-Wrapper Network (CW-Net), a method for explaining the behavior of machine-learning-based planners by grounding their reasoning in human-interpretable concepts. We deploy CW-Net on a real self-driving car and show that the resulting explanations improve the human driver's mental model of the car, allowing them to better predict its behavior. To our knowledge, this is the first demonstration that explainable deep learning integrated into self-driving cars can be both understandable and useful in a realistic deployment setting. CW-Net accomplishes this level of intelligibility while providing explanations which are causally faithful and do not sacrifice driving performance.

## Introduction

There are hundreds of companies developing autonomous vehicle (AV) technology globally \[badue2021self\], promising to revolutionize transportation for everyone. The industry currently spans two segments: fully autonomous ride-hail systems and consumer vehicles with driver-assistance \[SAEJ3016_2021\]. In consumer vehicles, machine learning (ML) solutions have markedly improved the technology, yet they still require human intervention in unusual or challenging situations where learned planners may not determine the correct action \[xing2021toward\].

Lack of effective communication between the AV and the human driver has contributed to multiple high-profile incidents, some resulting in fatalities \[Titcomb2019, Fang2023, templeton2024waymo\], highlighting the urgent need to make ML planners interpretable \[atakishiyev2024explainable\].

## Conclusion

Our work shows how explainable deep learning can provide useful explanations for AVs in a real-world setting. CW-Net achieves this by grounding the reasoning of a pretrained black-box ML planner in human-interpretable concepts that are directly used to make driving decisions. By revealing otherwise inaccessible information about the decision-making process of the AV in real time, CW-Net helps improve the human driver's mental model of the AV. This, in turn, improves the driver's situational awareness and reveals limitations of the robotic system, helping the driver better anticipate its mistakes.

Many systems involving human-robot interaction require real-time explanations, including AI wingmen, drone navigation systems, and robotic surgeons. Similarly to AVs, many of these applications increasingly rely on deep learning, with a long tail of potentially catastrophic failure cases. Indeed, many regulatory bodies have already made explainable AI a core component of their legislation, with AVs likely to follow suit as they are widely deployed with various users \[atakishiyev2024explainable\].
