SceneDiffuser++: City-Scale Traffic Simulation via a Generative World Model

Topics include Driving simulation, Traffic simulation, Generative world models, Diffusion models, Autonomous driving, City-scale simulation, Agent behavior modeling, Waymo open motion dataset.

Extends the SceneDiffuser line toward city-scale traffic simulation, integrating scene generation, agent behavior, dynamic spawning and removal, and environment state such as traffic lights into a single generative world model. The contribution is important because it moves from isolated scene snippets toward point-to-point synthetic driving miles over larger map regions.

The goal of traffic simulation is to augment a potentially limited amount of manually-driven miles that is available for testing and validation, with a much larger amount of simulated synthetic miles. The culmination of this vision would be a generative simulated city, where given a map of the city and an autonomous vehicle (AV) software stack, the simulator can seamlessly simulate the trip from point A to point B by populating the city around the AV and controlling all aspects of the scene, from animating the dynamic agents (e.g., vehicles, pedestrians) to controlling the traffic light states. We refer to this vision as CitySim, which requires an agglomeration of simulation technologies: scene generation to populate the initial scene, agent behavior modeling to animate the scene, occlusion reasoning, dynamic scene generation to seamlessly spawn and remove agents, and environment simulation for factors such as traffic lights. While some key technologies have been separately studied in various works, others such as dynamic scene generation and environment simulation have received less attention in the research community.

## Introduction

Imagine an ideal traffic simulation at the city-scale: Starting from a logged or synthetic scene, we initiate the simulation. The virtual world comes alive with agents behaving realistically: cars navigate roads, pedestrians cross streets, and interactions unfold naturally. A pedestrian emerges from behind a bus, prompting a reaction from the ego agent. Vehicles disappear and reappear as they become occluded and disoccluded. Turning onto a new road reveals a fresh stream of traffic. The ego vehicle responds to traffic signals, stopping at red lights and proceeding when they turn green.

We refer to such a city-scale closed-loop traffic simulation system as CitySim. CitySim can enable point-to-point driving simulation for obtaining trip-level statistics. This allows holistic driving assessment, for instance trip-level travel time comparisons to average human drivers, pick-up and drop-off quality assessment, as well as evaluation of driving behaviors during the trip, including safety and driving quality. Such simulators also allow for playing out events that take longer to unfold, such as interactions between an AV and emergency vehicles.

We propose a unified generative world model: SceneDiffuser++, enabling realistic long simulations while accounting for dynamic agent generation, occlusion reasoning and traffic light simulation via simple autoregressive rollout using a novel method to generate sparse tensors.

We demonstrate our performance on a map-augmented WOMD dataset and achieve state-of-the-art trip-level simulation realism.

## Conclusion

We have introduced SceneDiffuser++, a scene-level diffusion prior designed for city-scale traffic simulation. SceneDiffuser++ is a unified world model that enables trip-level long simulations with dynamic agent generation, occlusion reasoning, removal and traffic light simulation. We demonstrate SceneDiffuser++ has strong performance for long-term traffic simulation. We hope our work leads to more realistic trip-level simulation to improve AV safety.
