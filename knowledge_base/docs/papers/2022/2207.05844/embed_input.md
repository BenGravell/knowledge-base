Wayformer: Motion Forecasting via Simple & Efficient Attention Networks

Topics include Motion forecasting, Transformers, Attention mechanisms, Autonomous driving, Multi-modal prediction, Waymo, Wayformer.

Proposes a simple and efficient transformer-based architecture for motion forecasting, showing that a straightforward attention design over scene and agent context can match or surpass more complex architectures on standard benchmarks like Waymo Open Motion Dataset (WOMD).

Motion forecasting for autonomous driving is a challenging task because complex driving scenarios involve a heterogeneous mix of static and dynamic inputs. It is an open problem how best to represent and fuse information about road geometry, lane connectivity, time-varying traffic light state, and history of a dynamic set of agents and their interactions into an effective encoding. To model this diverse set of input features, many approaches proposed to design an equally complex system with a diverse set of modality specific modules. This results in systems that are difficult to scale, extend, or tune in rigorous ways to trade off quality and efficiency. In this paper, we present Wayformer, a family of simple and homogeneous attention based architectures for motion forecasting. Wayformer offers a compact model description consisting of an attention based scene encoder and a decoder. In the scene encoder we study the choice of early, late and hierarchical fusion of input modalities. For each fusion type we explore strategies to trade off efficiency and quality via factorized attention or latent query attention.

## Introduction

In this work, we focus on the general task of future behavior prediction of agents (pedestrians, vehicles, cyclists) in real-world driving environments.

This is an essential task for safe and comfortable human-robot interactions, enabling high-impact robotics applications like autonomous driving.

The modeling needed for such scene understanding is challenging for many reasons. For one, the *output* is highly unstructured and multimodal---*e.g.*, a person driving a vehicle could carry out one of many underlying intents unknown to an observer, and representing a distribution over diverse and disjoint possible futures is required. A second challenge is that the *input* consists of a heterogeneous mix of modalities, including agents' past physical state, static road information (*e.g.* location of lanes and their connectivity), and time-varying traffic light information.

Many previous efforts address how to model the multimodal output, and develop hand-engineered architectures to fuse different input types, each requiring their own preprocessing (*e.g.*, image rasterization ). Here, we focus on the multimodality of the *input space*, and develop a simple yet effective modality-agnostic framework that avoids complex and heterogeneous architectures, and leads to a simpler architecture parameterization.

Our experiments suggest the domain of motion forecasting conforms to Occam's Razor. We show state of the art results with the simplest design choices and making minimal domain specific assumptions, which is in stark contrast to previous work. When tested in simulation and on real AVs, these Wayformer models showed good understanding of the scene.

## Limitations

Scope of the current study is subject to the following limitations: Ego-centric modeling is subject to repeated computations on dense scenes. This can be alleviated by encoding the scene only once in a global frame of reference. Our system input is a sparse abstract state description of the world, which fails to capture some important nuances in highly interactive scenes, e.g., visual cues from pedestrians or fine-granularity contour or wheel angle information for vehicles. Learning perception and prediction end-to-end could unlock improvements.
