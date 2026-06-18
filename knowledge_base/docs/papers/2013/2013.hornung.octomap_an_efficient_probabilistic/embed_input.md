<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OctoMap: An Efficient Probabilistic 3D Mapping Framework Based on Octrees

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Three-dimensional models provide a volumetric representation of space which is important for a variety of robotic applications including flying robots and robots that are equipped with manipulators. In this paper, we present an open-source framework to generate volumetric 3D environment models. Our mapping approach is based on octrees and uses probabilistic occupancy estimation. It explicitly represents not only occupied space, but also free and unknown areas. Furthermore, we propose an octree map compression method that keeps the 3D models compact. Our framework is available as an open-source C++ library and has already been successfully applied in several robotics projects. We present a series of experimental results carried out with real robots and on publicly available real-world datasets. The results demonstrate that our approach is able to update the representation efficiently and models the data consistently while keeping the memory requirement at a minimum.
