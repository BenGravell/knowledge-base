Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization

Topics include Metric-semantic simultaneous localization and mapping, 3D scene graphs, Spatial perception, Euclidean signed distance field, Topological mapping, Loop closure, Embedded deformation, Real-time systems, Hydra.

Presents Hydra, a real-time spatial perception system that constructs layered 3D scene graphs online from robot sensor data. The key contribution is tying metric mapping, place and room abstraction, hierarchical loop-closure descriptors, and deformation-based graph optimization into a single online stack.

3D scene graphs have recently emerged as a powerful high-level representation of 3D environments. A 3D scene graph describes the environment as a layered graph where nodes represent spatial concepts at multiple levels of abstraction and edges represent relations between concepts. While 3D scene graphs can serve as an advanced "mental model" for robots, how to build such a rich representation in real-time is still uncharted territory. This paper describes a real-time Spatial Perception System, a suite of algorithms to build a 3D scene graph from sensor data in real-time. Our first contribution is to develop real-time algorithms to incrementally construct the layers of a scene graph as the robot explores the environment; these algorithms build a local Euclidean Signed Distance Function (ESDF) around the current robot location, extract a topological map of places from the ESDF, and then segment the places into rooms using an approach inspired by community-detection techniques. Our second contribution is to investigate loop closure detection and optimization in 3D scene graphs....

## Introduction

The next generation of robots and autonomous systems will be required to build persistent high-level representations of unknown environments in real-time. *High-level* representations are required for a robot to understand and execute instructions from humans (*e.g.,* "bring me the cup of tea I left on the dining room table"); high-level representations also enable fast planning (*e.g.,* by allowing planning over compact abstractions rather than dense low-level geometry). Such representations must be built in *real-time* to support just-in-time decision-making....

Figure 1: We present Hydra, a highly parallelized architecture to build 3D scene graphs from sensor data in real-time. The figure shows sample input data and the 3D scene graph created by Hydra in a large-scale real environment.

## Disclaimer

Research was sponsored by the United States Air Force Research Laboratory and the United States Air Force Artificial Intelligence Accelerator and was accomplished under Cooperative Agreement Number FA8750-19-2-1000. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the United States Air Force or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein.

### IV-B 3D Scene Graph Optimization

### III-B Layer 4: Room Detection

This section shows that Hydra builds 3D scene graphs in real-time with an accuracy comparable to batch offline methods.

3D Scene Graphs have recently emerged as powerful high-level representations of 3D environments. A 3D scene graph (Fig. 1 and Fig. 6) is a layered graph where nodes represent spatial concepts at multiple levels of abstraction (from low-level geometry to objects, places, rooms, buildings, etc.) and edges represent relations between concepts. Armeni *et al.* pioneered the use of 3D scene graphs in computer vision and proposed the first algorithms to parse a metric-semantic 3D mesh into a 3D scene graph. Kim *et al.* reconstruct a 3D scene graph of objects and their relations....

While 3D scene graphs can serve as an advanced "mental model" for robots, how to build such a rich representation in real-time remains uncharted territory....
