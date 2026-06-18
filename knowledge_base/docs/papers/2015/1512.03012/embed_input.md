ShapeNet: An Information-Rich 3D Model Repository

Topics include Graphs, Datasets, Benchmarks, ShapeNet.

We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects. ShapeNet contains 3D models from a multitude of semantic categories and organizes them under the WordNet taxonomy. It is a collection of datasets providing many semantic annotations for each 3D model such as consistent rigid alignments, parts and bilateral symmetry planes, physical sizes, keywords, as well as other planned annotations. Annotations are made available through a public web-based interface to enable data visualization of object attributes, promote data-driven geometric analysis, and provide a large-scale quantitative benchmark for research in computer graphics and vision. At the time of this technical report, ShapeNet has indexed more than 3,000,000 models, 220,000 models out of which are classified into 3,135 categories (WordNet synsets). In this report we describe the ShapeNet effort as a whole, provide details for all currently available datasets, and summarize future plans.

## Introduction

Recent technological developments have led to an explosion in the amount of 3D data that we can generate and store. Repositories of 3D CAD models are expanding continuously, predominantly through aggregation of 3D content on the web. RGB-D sensors and other technology for scanning and reconstruction are providing increasingly higher fidelity geometric representations of objects and real environments that can eventually become CAD-quality models.

At the same time, there are many open research problems due to fundamental challenges in using 3D content. Computing segmentations of 3D shapes, and establishing correspondences between them are two basic problems in geometric shape analysis. Recognition of shapes from partial scans is a research goal shared by computer graphics and vision. Scene understanding from 2D images is a grand challenge in vision that has recently benefited tremendously from 3D CAD models. Navigation of autonomous robots and planning of grasping manipulations are two large areas in robotics that benefit from an understanding of 3D shapes....

### ShapeNetSem

ShapeNetSem is a smaller, more densely annotated subset consisting of 12,000 models spread over a broader set of 270 categories. In addition to manually verified category labels and consistent alignments, these models are annotated with real-world dimensions, estimates of their material composition at the category level, and estimates of their total volume and weight. The total numbers of models for the top 100 categories in this subset are given in Section 5.2.
6 Discussion and Future Work
The construction of ShapeNet is a continuous, ongoing effort....

Many objects, especially man-made artifacts such as furniture and appliances, can be used by humans. Functional annotations describe these usage patterns. Such annotations are often highly correlated with specific regions of an object. In addition, it is often related with the specific type of human action. ShapeNet aims to store functional annotations at the global shape level and at the object part level.

### Data Collection

As described in Section 3.2, we assign each 3D model to one or more synsets in the WordNet taxonomy.

Recently, data-driven methods from the machine learning community have been exploited by researchers in vision and NLP (natural language processing)....
