<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Foam: A Tool for Spherical Approximation of Robot Geometry

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many applications in robotics require primitive spherical geometry, especially in cases where efficient distance queries are necessary. Manual creation of spherical models is time-consuming and prone to errors. This paper presents Foam, a tool to generate spherical approximations of robot geometry from an input Universal Robot Description Format (URDF) file. Foam provides a robust preprocessing pipeline to handle mesh defects and a number of configuration parameters to control the level and approximation of the spherization, and generates an output URDF with collision geometry specified only by spheres. We demonstrate Foam on a number of standard robot models on common tasks, and demonstrate improved collision checking and distance query performance with only a minor loss in fidelity compared to the true collision geometry. We release our tool as an open source Python library and containerized command-line application to facilitate adoption across the robotics community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficient collision detection (both as binary classification and measuring distance to collision) is a fundamental challenge throughout robotics; algorithms and control strategies from real-time model-predictive control \[chiu2022collision, gaertner2021collision\], sampling-based motion planning \[sundaralingam2023curobo, thomason2024motions\], simulation \[Coumans2016, todorov2012mujoco\], and more all rely on effective collision detection of the robot's geometry with that of the environments. Although effective collision detection strategies exist for complex geometries (e.g., space decompositions, parallel approaches, GPU-accelerated algorithms), these approaches scale on the complexity of the involved geometry, and performance improves when the representative geometry of the robot and environment is simple.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, many robot descriptions (usually in URDF) are exported from CAD tools \[tola2024understanding\], which may contain extraneous details for coarse collision checking. These complex meshes also often contain non-manifold geometry (that is, non-watertight) and may contain geometry that violates assumptions made by geometric processing pipelines, e.g., flat planes or single faces. A common approach is to provide simplified geometry to represent the collision geometry of the robot, either with a set of convex meshes \[schulman2014motion\] or with a set of primitives \[zucker2013chomp\]. This is advantageous as collision checking with primitive approximations is more efficient for collision checking and signed distance queries (e.g., as in \\citetmukadam2018continuous,sundaralingam2023curobo), which are prevalent in modern robotics applications. However, although these primitive approximations are useful and widely used, existing tools lack robust automation for converting existing robot geometry into these primitive decompositions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents foam, an automated framework for generating spherical approximations of robot geometries directly from Universal Robot Description Format (URDF) specifications. The foam spherization pipeline balances geometric accuracy with computational efficiency through a number of configurable approximation parameters, building upon existing work on the medial sphere-tree approximation for meshes \[bradshaw2004adaptive\]. Our preprocessing pipeline handles and fixes common mesh defects gracefully, while maintaining critical geometric features needed for collision detection. The output of foam is an equivalent URDF of the input robot, but with all collision geometry replaced by spheres. We evaluated the output URDFs of foam across multiple standard robots and applications, and we demonstrated that foam-generated models achieve collision checking performance improvements while maintaining geometric fidelity suitable for practical robotic tasks. To the authors' knowledge, while spherization tools for just meshes exist open source, nothing has been packaged as a convenient tool for roboticists; we release our tool as open source at as a Python library and containerized command-line tool.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The Foam Library", "weight": 1.0} -->

The foam Library provides an automated framework for creating spherical approximations of robot geometries directly from Universal Robot Description Format (URDF) specifications. By converting complex polygonal meshes into simplified sphere-based representations, foam significantly improves computational efficiency for collision detection while maintaining sufficient geometric fidelity for practical robotics applications. The library offers a configurable pipeline that handles common mesh defects gracefully, preserves critical geometric features, and outputs equivalent URDFs with collision geometry replaced by spheres.

<!-- chunk {"id": "body-0007", "role": "body", "section": "III-A URDF Collision Geometry", "weight": 1.0} -->

In a robot's URDF, the collision geometry is specified by some number of \<collision/\> tags in each of the robot's \<link/\> tags. These can either be primitives (e.g., spheres, cuboids, cylinders), or by most of the time referencing external mesh files that are composed of complex polygons. Some robot manufacturers provide convex hulls, simplified mesh geometry, or primitive approximations for collision checking, but many are simply raw CAD file output \[tola2024understanding\]; in some cases the details are potentially so fine that screw holes are captured in the geometry.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A URDF Collision Geometry", "weight": 1.0} -->

foam creates simple, accurate spherized approximations of the geometries within a robot's URDF, either specified as meshes or as primitives. Our tool can either output spheres in a JSON database or in standard URDF representation (that is, a copy of the original robot's URDF with all the collision geometry replaced by a set of sphere primitives). The foam library provides some utility functions to load URDFs, retrieve all mesh files used in a URDF, modify a URDF to include spheres, and save the output file, respectively load_urdf, get_urdf_meshes, set_urdf_spheres and save_urdf.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A URDF Collision Geometry", "weight": 1.0} -->

We note that our simplified spherized models can be easily utilized in simulators such as MuJoCo \[todorov2012mujoco\], and spherization removes the dependency on external mesh assets. Generated spheres can be used in other applications that may benefit from simplified spherical approximations. For example, Pinocchio, which uses FCL collision checking, benefits greatly from mesh simplification due to using a collision library that is optimized for simplified geometry \[carpentier2019pinocchio, fcl\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Mesh Preprocessing", "weight": 1.0} -->

Many polygonal mesh processing algorithms (including our desired spherization approach) assume that the input mesh is *watertight* or *manifold* (specifically a 2-manifold). As implied by the name, a watertight mesh is such that it can "hold water", that is, it does not have holes or other broken geometry, e.g., edges with more than two incident faces, mesh faces intersecting each other, faces that are not connected together, etc. Watertight meshes also have a clear definition of the interior and exterior of the mesh. Unfortunately, many URDFs contain robot geometry that has been exported from automated tools \[tola2024understanding\], and therefore may contain multiple defects. These defects are also common among many meshes used in everyday tools, e.g., it is known that many of the meshes in ShapeNet \[chang2015shapenet\] are non-manifold. Moreover, for our downstream tasks of collision checking and spherization, these meshes may have extraneous detail that adds additional complexity to the mesh which is unessential.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Mesh Preprocessing", "weight": 1.0} -->

In order to handle non-watertight meshes, foam uses a preprocessing pipeline to handle these defects while preserving essential geometric features required for collision detection. This preprocessing pipeline also reduces the complexity of the mesh, improving the performance of the final spherization algorithm. A representative output from each stage of the pipeline is shown in Fig. 2. Each of these steps has a number of configurable hyperparameters to control the amount of simplification, smoothing, and processing the input mesh goes through.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Mesh Preprocessing", "weight": 1.0} -->

The preprocessing workflow begins after the collision meshes are loaded with Trimesh \[trimesh\] (Fig. 2-1). The mesh is then transformed into a guaranteed watertight mesh using the method of \\citethuang2018robust (Fig. 2-2). This step is crucial and ensures topological consistency by eliminating non-manifold edges, dangling faces, and small holes that could otherwise compromise the accuracy of subsequent spherization. Following this step, we then simplify the manifold mesh with a quadric-based edge collapse simplification method \[garland1997surface\] to reduce complexity, as downstream algorithms scale with the number of triangles in the mesh and are more robust with less complex input (e.g., see Fig. 3). This produces a simplified mesh (Fig. 2-3) with significantly fewer vertices and faces, yet preserves the essential shape characteristics of the original geometry.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Mesh Preprocessing", "weight": 1.0} -->

The process continues with a smoothing phase (Fig. 2-4) that applies both Laplacian smoothing and Humphrey filtering \[vollmer1999improved\] (smooth_manifold in the foam library) to remove small-scale irregularities and noise from the mesh surface, creating a more uniform geometric representation suitable for sphere fitting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Spherization of Meshes", "weight": 1.0} -->

After the mesh has been processed into a simplified, watertight mesh, it is then spherized with an implementation of the Adaptive Medial Axis Approximation (AMAA) algorithm of \\citetbradshaw2004adaptive (spherize_mesh using the medial option in the foam library). An output from the AMAA processing can be seen in Fig. 2-5, which shows how the mesh can be effectively covered with only 9 spheres. We contrast the output of AMAA after our preprocessing to the provided spherization tool in cuRobo \[sundaralingam2023curobo\], where a variety of outputs are shown in Fig. 2-6. Their approach performs a simplified voxelization of the mesh into spheres with a given sphere radius.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Spherization of Meshes", "weight": 1.0} -->

We also expose other methods for spherization (e.g., a voxel grid-based decomposition with grid), but these notably provide less high-fidelity spherizations There are also a number of keyword arguments to control the spherization process---a number of them are listed in the example code in Fig. 5 (e.g., the maximum number of desired spheres can be specified with the branch parameter). This control of the amount of desired spherization is illustrated in Fig. 4, which shows the Franka Emika Panda robot spherized with increasing amounts of spheres. This allows users to control the fidelity and complexity of the output spherized model, either remaining coarse or reaching a close-fitting approximation. We contrast the output of foam (Fig. 4-1--5) with a custom-made spherization from \\citetfishman2023motion (Fig. 4-6). foam's spherization more closely matches the true robot collision geometry (Fig. 4-7) and is a conservative overapproximation, rather than an underapproximation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-D The Foam Tool", "weight": 1.0} -->

1def main(mesh: str, output: str):
2 mesh_filepath = Path(mesh)
3 # kwargs for spherization
24 # kwargs for mesh processing
29 # Call spherize_mesh with kwargs
30 spheres = spherize_mesh(
32 spherization_kwargs=sphere_kwargs,
33 process_kwargs=process_kwargs
35 # Write the result to a JSON file
36 output = mesh_filepath.stem + "-spheres"
37 with open(output + ".json", ’w’) as f:
38 f.write(dumps(spheres, indent=4, cls=SphereEncoder))
Figure 5: Example script to process a mesh using foam.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-D The Foam Tool", "weight": 1.0} -->

We provide the mesh preprocessing pipeline and spherization tools as the foam Python library and command-line tool, along with a Docker container to provide easy use to end users. The code is available in A simple example script that demonstrates how foam can be used as a library to convert a mesh into a set of spheres is given in Fig. 5. After defining the spherization_kwargs and process_kwargs, the spherize_mesh function is called and the spheres are written to a JSON file.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-D The Foam Tool", "weight": 1.0} -->

Beyond the foam library, we provide standalone scripts that can be used to spherize an input mesh or URDF:\
\$ python generate_spheres.py \<mesh\>\
\$ python generate_sphere_urdf.py \<urdf\>

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D The Foam Tool", "weight": 1.0} -->

foam has already proven useful for other publications. For example, foam was used to generate the spherized geometry for the UR5, Fetch, Baxter robots as well as some environments used in \\citetthomason2024motions,ramsey2024,quintero2024impdist.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

We observe foam's effectiveness across a variety of fundamental robotics tasks in various simulators and collision checking backends. We selected MuJoCo \[todorov2012mujoco\], PyBullet \[Coumans2016\], and Pinocchio \[carpentier2019pinocchio\] as these are widely used throughout the field---MuJoCo and PyBullet are popular off-the-shelf robotics-focused physics simulators due to their wide functionality, high fidelity, and accessibility. Pinocchio is a library for robot kinematics and dynamics modeling and uses the FCL library for collision checking \[fcl\]. We present results in Table I that show the difference in collision checking and signed distance query speed over these three libraries for five robots: the Hello Robot Stretch, the Franka Emika Panda, the KUKA IIWA, the Kinova Jaco, and the Rethink Robotics Baxter.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Examples of the spherized models for the Panda, KUKA, and Kinova are shown in Fig. 1. While collision checking speed remains relatively consistent in PyBullet and MuJoCo between the spherized models and base models, signed distance query time is significantly faster in all engines. FCL in particular is highly compatible with the spherized primitive representation, giving large performance gains over all robots except for the Stretch.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Additionally, we also investigate how model simplification can affect physics iteration time in a parallelized simulator, Genesis \[Genesis\], shown in Table II. The demand for parallelized simulators has seen a recent uptick as parallelized training for large models has become more prevalent, requiring a large-scale high-speed simulation for training and validation---simplified models may be a way to increase performance in certain tasks. Benchmarking the frames per second (FPS) in Genesis with 300 parallel simulations of the Franka Panda shows a 10% speedup when using a simplified model with 30 spheres, compared to the original model, shown in Table II. Spherization also improved FPS across all models. These results demonstrate that spherized models outperform the original, offering better computational efficiency in applications that demand numerous parallelized environments.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

All experiments were performed on a PC with a 13th Gen Intel(R) Core(TM) i7-13700K CPU, an NVIDIA GeForce RTX 4070Ti, and 32GB of system memory.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have presented foam, a library and tool to generate spherical approximations of robot geometry from an input URDF, addressing a critical limitation in existing tools to bridge general robots to methods that require spherical approximations. foam handles common mesh defects gracefully while preserving essential geometric features; our pipeline enables roboticists to easily convert complex CAD-derived meshes into computationally efficient primitive representations. foam also provides a number configurable parameters allow users to balance geometric fidelity with computational efficiency according to downstream requirements.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our empirical results also demonstrate that spherical approximations of robot geometries provide significant computational advantages while maintaining acceptable geometric fidelity for practical robotics tasks. Across multiple standard robots (Franka Emika Panda, Baxter, KUKA IIWA, Kinova, and Stretch), we observed substantial performance improvements in collision checking times, particularly for distance queries, with speedups of up to two orders of magnitude in some cases (e.g., Kinova through FCL-based collision checking in the Pinocchio framework). These findings suggest that simplified robot geometry should be preferred for robotics tasks unless absolute geometric precision is essential, especially for applications involving signed distance fields or real-time control.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Discussion", "weight": 1.5} -->

foam also opens the door for general robots to be applied to tools that require spherical models, such as cuRobo \[sundaralingam2023curobo\], GPMP2 \[mukadam2018continuous\], VAMP \[thomason2024motions\], and more. In the future, we plan to provide not only spherical approximations in foam, but also convex decompositions, cuboid decompositions, and other mesh processing tools. We are especially interested in other spherization algorithms that could be run more tightly "in-the-loop" to address situations that require faster spherization, such as dynamic manipulation requiring spherization of objects on the fly.
