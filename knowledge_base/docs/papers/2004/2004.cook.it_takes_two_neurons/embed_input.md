<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

It Takes Two Neurons to Ride a Bicycle

Topics include Bicycle control, Neural control, Balance, Simulation, Minimal controllers.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Demonstrates a two-neuron controller that stabilizes and steers a simulated bicycle toward changing goals without lengthy reinforcement learning or explicit inversion of its dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Past attempts to get computers to ride bicycles have required an inordinate amount of learning time (1700 practice rides for a reinforcement learning approach, while still failing to be able to ride in a straight line), or have required an algebraic analysis of the exact equations of motion for the specific bicycle to be controlled. Mysteriously, humans do not need to do either of these when learning to ride a bicycle. Here we present a two-neuron network that can ride a bicycle in a desired direction (for example, towards a desired goal or along a desired path), which may be chosen or changed at run time. Just as when a person rides a bicycle, the network is very accurate for long range goals, but in the short run stability issues dominate the behavior. This happens not by explicit design, but arises as a natural consequence of how the network controls the bicycle.
