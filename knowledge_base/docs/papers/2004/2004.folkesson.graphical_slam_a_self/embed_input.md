Graphical SLAM - a Self-correcting Map

Topics include Simultaneous localization and mapping, Graph-based mapping, Mobile robotics, Data association, Loop closure, Topological consistency, Outdoor robots.

Presents a graph-based SLAM approach designed to tolerate data-association errors and apply global constraints such as loop closure even when they induce large map shifts. The method uses the map graph for efficient updates and local-to-global simplification, anticipating later graph-SLAM formulations.

We describe an approach to simultaneous localization and mapping, SLAM. This approach has the highly desirable property of robustness to data association errors. Another important advantage of our algorithm is that non-linearities are computed exactly, so that global constraints can be imposed even if they result in large shifts to the map. We represent the map as a graph and use the graph to find an efficient map update algorithm. We also show how topological consistency can be imposed on the map, such as, closing a loop. The algorithm has been implemented on an outdoor robot and we have experimental validation of our ideas. We also explain how the graph can be simplified leading to linear approximations of sections of the map. This reduction gives us a natural way to connect local map patches into a much larger global map.
