<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Unified Autonomy Stack: Toward a Blueprint for Generalizable Robot Autonomy

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce and open-source the Unified Autonomy Stack, a system-level solution that enables resilient autonomy across diverse aerial and ground robot morphologies. The architecture centers on three synergistic modules - multi-modal perception, multi-behavior planning, and multi-layered safe navigation - that together deliver comprehensive mission autonomy. The stack fuses data from LiDAR, radar, vision, and inertial sensing, enabling (a) robust localization and mapping through factor graph-based fusion, (b) semantic scene understanding, (c) motion and informative path planning through sampling-based techniques adaptive across spatial scales, as well as (d) multi-layered safe navigation both through planning on the online reconstructed map and deep learning-driven exteroceptive policies alongside last-resort safety filters using control barrier functions. The resulting behaviors include safe GNSS-denied navigation into unknown and perceptually-degraded regions, exploration of complex environments, object discovery, and efficient inspection planning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The stack has been field-tested and validated on both aerial (rotorcraft) and ground (legged) robots operating in a host of demanding environments, including self-similar and smoke-filled settings, with complex geometries and high obstacle clutter. These tests demonstrate resilient performance in challenging conditions. To facilitate ease of adoption, we open-source the implementation alongside supporting documentation, validation, and evaluation datasets A video giving the overview of the paper and the field experiments is available at
