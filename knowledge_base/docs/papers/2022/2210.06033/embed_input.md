<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Local Planner Bench: Benchmarking for Local Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Local motion planning is a heavily researched topic in the field of robotics with many promising algorithms being published every year. However, it is difficult and time-consuming to compare different methods in the field. In this paper, we present localPlannerBench, a new benchmarking suite that allows quick and seamless comparison between local motion planning algorithms. The key focus of the project lies in the extensibility of the environment and the simulation cases. Out-of-the-box, localPlannerBench already supports many simulation cases ranging from a simple 2D point mass to full-fledged 3D 7DoF manipulators, and it is straightforward to add your own custom robot using a URDF file. A post-processor is built-in that can be extended with custom metrics and plots. To integrate your own motion planner, simply create a wrapper that derives from the provided base class. Ultimately we aim to improve the reproducibility of local motion planning algorithms and encourage standardized open-source comparison.
