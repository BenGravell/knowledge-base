<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robowflex: Robot Motion Planning with MoveIt Made Easy

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robowflex is a software library for robot motion planning in industrial and research applications, leveraging the popular MoveIt library and Robot Operating System (ROS) middleware. Robowflex provides an augmented API for crafting and manipulating motion planning queries within a single program, making motion planning with MoveIt easy. Robowflex's high-level API simplifies many common use-cases while still providing low-level access to the MoveIt library when needed. Robowflex is particularly useful for 1) developing new motion planners, 2) evaluating motion planners, and 3) complex problems that use motion planning as a subroutine (e.g., task and motion planning). Robowflex also provides visualization capabilities, integrations to other robotics libraries (e.g., DART and Tesseract), and is complementary to other robotics packages. With our library, the user does not need to be an expert at ROS or MoveIt to set up motion planning queries, extract information from results, and directly interface with a variety of software components. We demonstrate its efficacy through several example use-cases.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A core component of any autonomous system is *motion planning*, which finds feasible motions that satisfy task requirements (e.g., reaching the goal, satisfying some motion constraint, etc.). There are many motion planning software system for general manipulators; a popular library for motion planning is MoveIt, which is built on top of the ubiquitous Robot Operating System (ros) framework. MoveIt has four key advantages: it is widely adopted in industry and research, it is easy to setup for new robots and over 150 robots are already available, it is easy to integrate with a ros system, and it has a large and vibrant open source community. However, due to MoveIt's massive scope and abstract architecture, many tasks are challenging for both engineers and researchers. For example, it can be difficult to evaluate and develop planning algorithms, extend a planner's functionality, extract low-level information from planners, or use a planner within the scope of a broader planning algorithm, e.g., task and motion planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper introduces *Robowflex*, a software library designed to simplify the use of MoveIt for industrial and research applications of motion planning. *Robowflex* is a high-level api to easily manipulate robots, collision environments, planning requests, and motion planners. *Robowflex* "wraps" the underlying MoveIt library within a c++ interface that provides many utilities that simplify the use and evaluation of motion planners. Moreover, *Robowflex* provides direct access to the implementation (that is, not through ros messaging). The key advantage of this approach is the ability to 1) develop self-contained scripts to evaluate motion planning, 2) retain the capability of easy system integration through ros when necessary, and 3) implement integrated algorithms that use motion planning extensively (e.g., task and motion planning). *Robowflex* also integrates other libraries, e.g., the Open Motion Planning Library (ompl), dart, ros Industrial's Tesseract, and visualization with Blender.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, these integrations enable comparison of MoveIt's rrtConnect against Tesseract's TrajOpt on the same scene in a single, short script. We demonstrate the usefulness of *Robowflex* in several example use-cases, such as benchmarking for motion planning experiments and an industry-focused use-case of evaluating Robonaut 2 walking from nasa. *Robowflex* is open-source^11^1 documented online^22^2 and has already been used in a number of publications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

*Robowflex* is intended for use in research, education, and industry. *Robowflex* is informed by the following design goals.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

*Clarity of Interface*: Provide an easy to understand interface that meshes with intuitive understanding of the concepts involved in motion planning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

*Minimize ros*: Encapsulate ros as much as possible such that it is easy to write independent programs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

*Leverage MoveIt's Ubiquity*: By being based on MoveIt, many robots are supported in *Robowflex* out of the box. The use of MoveIt also enables *Robowflex* scripts to effortlessly connect to the greater ros system.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

*Unrestricted Access and Integration*: While providing a high-level api, give access to underlying libraries so users are not hampered by *Robowflex* in any way. A key advantage *Robowflex* provides is that all the underlying data structures used in MoveIt, ompl, or other libraries can be accessed and modified. *Robowflex* provides a common interface and adapters to convert between the representations used by each library.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

*Consistency Across Versions*: *Robowflex* provides adapters such that *Robowflex* code is not tied to a specific version of ros or MoveIt. *Robowflex* supports all versions from ros Indigo to ros Noetic.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The *Robowflex* Library", "weight": 1.0} -->

At a high-level, *Robowflex* provides wrappers around core MoveIt concepts so that it is easy to create and manage robots, scenes, and planners within a script. The primary building blocks of *Robowflex* are the robot's kinematics, the collision environment, and the motion planner. Although other facades to MoveIt exist, *Robowflex* provides a higher level of abstraction that allows users who are unfamiliar with MoveIt to still achieve complex programming tasks. Moreover, these core features are supported by a suite of utilities, such as input-and-output helpers for a variety of formats, benchmarking tools, visualization within RViz, and more. Beyond the core library are auxiliary modules for other robotics libraries, and support seamless integration between *Robowflex* and native formats.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Many complicated robotic problems require large amounts of file input and output (io), e.g., for configuration, loading problems and scenes, and more.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Files and ros Packages", "weight": 1.0} -->

It is common to access files that exist in ros packages that are specified with package uris---*Robowflex* provides helper functions to resolve file paths and to either open or create said file.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Files", "weight": 1.0} -->

Many configuration files in robotics are written in Extensible Markup Language (xml) or in the macro xml language xacro. *Robowflex* provides helper functions to load these files (including unprocessed xacro) as well as inject changes on the fly.

<!-- chunk {"id": "body-0016", "role": "body", "section": "yaml Files", "weight": 1.0} -->

It is common to save and load ros messages as yaml files. However, there is no easy way to load or save ros messages in yaml in c++. *Robowflex* has broad yaml support, and can load yaml from ros Python and ros topics. Many *Robowflex* classes can load ros messages, e.g., motion planning requests, robot states, and more. This makes it easy to load problems using yaml files.

<!-- chunk {"id": "body-0017", "role": "body", "section": "ros Parameters", "weight": 1.0} -->

Many ros programs rely on the parameter server, a distributed key-value store available in ros. As a result, it is sometimes difficult to have multiple programs running simultaneously that require similar parameters, leading to issues with managing namespaces. By default, *Robowflex* uses an anonymous namespace so that many instances of *Robowflex* code can simultaneously run. Moreover, there is support to load yaml files onto the parameter server, which is typically only available through ros launch, making it easy to have scripts load their parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "ros Parameters", "weight": 1.0} -->

There is also support for ros bag files, hdf5 files, various transformation representations, and others.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Robot Kinematics", "weight": 1.0} -->

Commonly, the kinematics and geometry of a robot are described using the Universal Robot Description Format (urdf). Moreover, MoveIt requires a Semantic Robot Description Format (srdf) file, which describes additional properties such as what links are allowed to collide with each other, what groups of joints should be used for planning, and what parts of the robot are the end-effector. There are also additional configuration files MoveIt requires, such as yaml files that describe kinematics plugins and additional joint limits. Typically, most robots are configured through the MoveIt setup assistant wizard which generates a ros package containing all necessary configuration files. Part of this configuration are complicated ros launch files that contain parameters necessary to start MoveGroup, and in order to modify the behavior of MoveIt, both the program and launch file need to be modified.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Robot Kinematics", "weight": 1.0} -->

*Robowflex* takes care of all the necessary legwork to load and configure a robot without the need for a launch file. Moreover, *Robowflex* enables loading multiple robots within the same program, and duplicating robots if necessary---with default MoveIt, this process can become convoluted. An example of loading a robot is shown in Fig. 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Robot Kinematics", "weight": 1.0} -->

4 std::make_shared<rx::Robot>("wam7"); 6 "package://barrett_model/robots/wam_7dof_wam_bhand.urdf.xacro", // urdf 7 "package://barrett_wam_moveit_config/config/wam7_hand.srdf", // srdf 8 "package://barrett_wam_moveit_config/config/joint_limits.yaml", // joint limits 9 "package://barrett_wam_moveit_config/config/kinematics.yaml" // kinematics Figure 1: Loading a robot (here, a Barrett WAM® arm) in Robowflex.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Collision Environment", "weight": 1.0} -->

The robot can be used to initialize a planning scene, which contains the collision geometry of the environment. The scene can be used for adding and moving collision objects and computing collisions and distance to collision.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Collision Environment", "weight": 1.0} -->

For example, scenes can be loaded from yaml files, which encode full planning scenes: [⬇](data:text/plain;base64,IGF1dG8gc2NlbmUgPSBzdGQ6Om1ha2Vfc2hhcmVkPHJ4OjpTY2VuZT4od2FtNyk7CiBzY2VuZS0+ZnJvbVlBTUxGaWxlKCAvLwogICJwYWNrYWdlOi8vcm9ib3dmbGV4X2xpYnJhcnkveWFtbC9zY2VuZS55bWwiKTs=){download=""} 1 auto scene = std$::$make_shared\<rx$::$Scene\>(wam7); 2 scene$\rightarrow$fromYAMLFile(//3 \"package://robowflex_library/yaml/scene.yml\");

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Collision Environment", "weight": 1.0} -->

[⬇](data:text/plain;base64,IGF1dG8gc2NlbmUgPSBzdGQ6Om1ha2Vfc2hhcmVkPHJ4OjpTY2VuZT4od2FtNyk7CiBhdXRvIGdlb21ldHJ5ID0gLy8KICAgcng6Okdlb21ldHJ5OjptYWtlQ3lsaW5kZXIoMC4wMjUsIDAuMSk7CiBhdXRvIHBvc2UgPSAvLwogICByeDo6VEY6OmNyZWF0ZVBvc2VYWVooIC8vCiAgICAgLTAuMjY4LCAtMC44MjYsIDEuMzEzLCAgICAvLyBwb3NpdGlvbgogICAgICAgICAwLiwgICAgIDAuLCAgICAwLikpOyAgLy8gWFlaIEV1bGVyCiBzY2VuZS0+dXBkYXRlQ29sbGlzaW9uT2JqZWN0KCAvLwogICAiY3lsaW5kZXIiLCBnZW9tZXRyeSwgcG9zZSk7){download=""} 1 auto scene = std$::$make_shared\<rx$::$Scene\>(wam7); 8 scene$\rightarrow$updateCollisionObject(//9 \"cylinder\", geometry, pose); Note that many scenes can be loaded simultaneously, can be copied and modified, and saved and loaded to and from disk.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Motion Planner", "weight": 1.0} -->

MoveIt uses a plugin-based system to load motion planning pipelines^66^6 which consist of adapters that filter and process both the planning request and output trajectory found by a motion planner. *Robowflex* provides an implementation to access any pipeline, and helpers for common plugins such as the default ompl planning pipeline plugin. To specify a planning request, a helper class is provided which simplifies the design of complex goal and path constraints, as well as setting start and goal states. This helper class can also save and load motion planning requests to yaml files, for later evaluation or setup. Many planners can be loaded simultaneously and used in tandem. Moreover, *Robowflex* supports inserting new planners, either through MoveIt's api or its own.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-E Example Script", "weight": 1.0} -->

1 // Create a default Fetch robot. 2 auto fetch = std::make_shared<rx::FetchRobot>; 5 // Create an empty scene. 6 auto scene = std::make_shared<rx::Scene>(fetch); 8 // Create the default planner for the Fetch. 10 std::make_shared< //11 rx::OMPL::FetchOMPLPipelinePlanner>(fetch); 14 // Create a motion planning request. 16 planner, "arm_with_torso"); 18 // Set the start state. 19 fetch→setGroupState("arm_with_torso", 24 // Set the goal state. 25 fetch→setGroupState("arm_with_torso", 30 // Set the desired planner. 31 request.setConfig("RRTConnect"); 34 auto result = planner→plan(//35 scene, request.getRequest); Figure 2: A code snippet demonstrating basic motion planning on a Fetch robot, from a “stow” position of the arm to an “unfurled” position.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-E Example Script", "weight": 1.0} -->

Note this does not use any ros messages, similar to the internals of MoveIt’s MoveGroup program.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-E Example Script", "weight": 1.0} -->

Fig. 2 shows a simple script for motion planning with *Robowflex* using the Fetch robot. The robot is loaded on line 2---*Robowflex* comes with some preconfigured robots. An empty planning scene for the robot is created on line 6. The standard ompl planner for the Fetch is created and initialized in lines 9 to 12. A simple request, which unfurls the Fetch's arm from the stow position to an extended position, is created in lines 15 to 31. Finally, motion planning occurs on line 34. A version of this script is available in the repository^77^7 This simple script is akin to basic planning using the MoveIt's MoveGroupInterface class^88^8 The critical difference is that, rather than having to use roslaunch to run an instance of the MoveGroup program and then communicate plans over ros messages, all of MoveIt's internal structures are loaded in the *Robowflex* program^99^9See for how this could be done without *Robowflex*. Also, see footnote 5 for other helper classes that can set up planning without *Robowflex*..

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-E Example Script", "weight": 1.0} -->

Providing access to these structures within a single program is a key benefit of *Robowflex*. The scripting paradigm offered by *Robowflex* is more amenable to rapid testing and scripting than MoveGroup, which is designed primarily to be a "live" component of a ros system extant in some world.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-F Integrations", "weight": 1.0} -->

*Robowflex* also provides a number of auxiliary modules that enable compatibility with different robotics libraries.

<!-- chunk {"id": "body-0031", "role": "body", "section": "ompl Integration", "weight": 1.0} -->

The *Robowflex* ompl module provides deeper access for motion planning to the default MoveIt ompl motion planning plugin. This includes extracting the underlying ompl setup for a given planning problem, which enables users to modify the behavior of ompl planning without having to recompile either the MoveIt planning plugin or ompl. An example script for how to extract and customize the underlying ompl planner used by MoveIt is shown in Fig. 3. With *Robowflex*, it easy to use a custom planner or feature in ompl, as compared to integrating a new planner into MoveIt (e.g., this was done in ).

<!-- chunk {"id": "body-0032", "role": "body", "section": "ompl Integration", "weight": 1.0} -->

1 // Create an OMPL planner 3 std::make_shared< //4 rx::OMPL::OMPLInterfacePlanner>(fetch); 6 // Extract underlying OMPL structures 8 planner→getPlanningContext(scene, request); 9 auto ss = context→getOMPLSimpleSetup; 11 // Customize OMPL planner 13 auto space = ss→getStateSpace; Figure 3: A code snippet demonstrating how to use the Robowflex ompl integration to access internal ompl features.

<!-- chunk {"id": "body-0033", "role": "body", "section": "dart Integration", "weight": 1.0} -->

The *Robowflex* dart module provides an alternative to MoveIt, by modeling robots and scenes in the dart framework with bidirectional conversion to/from MoveIt constructs. The module provides an implementation of motion planning through ompl, including motion planning with manifold constraints. Moreover, this module provides an easy way to plan for multi-robot systems, allowing arbitrary composition of MoveIt enabled robots. This capability was used by the multi-robot task-motion planning framework discussed in Sec. IV-B. An example script demonstrating the dart module is given shown in Fig. 4.

<!-- chunk {"id": "body-0034", "role": "body", "section": "dart Integration", "weight": 1.0} -->

1 namespace rd = robowflex::darts; 3 // Convert MoveIt robot to Dart 4 auto fetch1 = std::make_shared<rd::Robot>(fetch); 6 // Copy the Fetch for multi-robot planning 7 auto fetch2 = fetch1→cloneRobot("other"); 8 fetch2→setDof; // Offset on X-axis 10 // Combine kinematic structures into a world 11 auto world = std::make_shared<rd::World>; 12 world→addRobot(fetch1); 13 world→addRobot(fetch2); 15 // Plan using planning groups from both robots 16 rd::PlanBuilder builder(world); 17 builder.addGroup("fetch", "arm_with_torso"); 18 builder.addGroup("other", "arm_with_torso"); 20 // Set start configuration for both robots 27 // Set goal configuration and setup planning 28 auto goal = builder.setGoalConfiguration({ //32 builder.setGoal(goal); 35 // Solve using OMPL 36 auto

<!-- chunk {"id": "body-0035", "role": "body", "section": "dart Integration", "weight": 1.0} -->

result = builder.ss→solve(30.0); Figure 4: A code snippet demonstrating Robowflex’s dart module for multi-robot motion planning.

<!-- chunk {"id": "body-0036", "role": "body", "section": "dart Integration", "weight": 1.0} -->

Here, the Fetch robot that was loaded in the prior script (Fig. 2) is converted to dart and copied, created a multi-robot system. A plan is generated in the composite space of both robots.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Tesseract Integration", "weight": 1.0} -->

The *Robowflex* Tesseract module provides access to the ros Industrial Consortium's planning framework, which includes an implementation of the TrajOpt planner. Similar to the dart module, methods for converting data (e.g., scenes and plans) back and forth are provided. *Robowflex*'s Tesseract module was used in to access and modify TrajOpt for comparison against ompl planners.

<!-- chunk {"id": "body-0038", "role": "body", "section": "MoveGroup Integration", "weight": 1.0} -->

The *Robowflex* MoveGroup module provides an easy connection to a live instance of MoveIt's MoveGroup. This connection can be used to obtain the current collision environment, publish plans to be executed, and generally synchronize information between MoveGroup and a *Robowflex* script.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Visualization with Blender", "weight": 1.0} -->

The *Robowflex* visualization module makes it easy to render robots within Blender, a tool for 3D modeling and animation. An example rendered still is shown in Fig. 5. Moreover, it is easy to animate motion plans generated by *Robowflex* to create appealing visualizations and videos^1010^10 This module has also been used to generate figures.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example Use-Cases", "weight": 1.0} -->

Crucial to the particular use-cases listed here as well as many others, *Robowflex* simplifies the pipeline of creating, editing, inspecting, saving, and loading motion planning problems (both collision environments and motion planning requests). These capabilities are essential for many research and industrial tasks that rely on reproducibility, experimentation, and debugging.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Benchmarking Motion Planners", "weight": 1.0} -->

A core use-case for *Robowflex* is benchmarking motion planners in a variety of planning scenes. The task of evaluating motion planners on realistic robots in many environments, extracting detailed planner information, and collating all collected data is difficult. *Robowflex* provides a benchmarking tool that enables easy benchmarking of different planners, scenes, and requests. The tool enables configurable benchmark output in a number of formats. For example, a default format provided is the ompl benchmark log output, so output is compatible with the standard ompl benchmarking suite and tools. In addition, recall that *Robowflex* supports loading both environments and requests from disk, making it easy to craft datasets for evaluation. As new planners are developed, targeted benchmarking can be done for many planner properties, a contribution to the motion planning community due to the difficulty of setting up consistent benchmarking criteria.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Benchmarking Motion Planners", "weight": 1.0} -->

For example, the following could be added after line 31 of Fig. 2 to benchmark the motion planning request: [⬇](data:text/plain;base64,ICByeDo6UHJvZmlsZXI6Ok9wdGlvbnMgb3B0aW9uczsKICByeDo6RXhwZXJpbWVudCBleHBlcmltZW50KCAvLwogICAgImV4YW1wbGUiLCAgLy8gTmFtZSBvZiBleHBlcmltZW50CiAgICBvcHRpb25zLCAgICAvLyBPcHRpb25zIGZvciBpbnRlcm5hbCBwcm9maWxlcgogICAgNjAuMCwgICAgICAgLy8gUXVlcnkgdGltZW91dAogICAgMTAwKTsgICAgICAgLy8gTnVtYmVyIG9mIHRyaWFscwoKICBleHBlcmltZW50LmFkZFF1ZXJ5KCJwbGFubmVyIiwKICAgIHNjZW5lLCBwbGFubmVyLCByZXF1ZXN0LT5nZXRSZXF1ZXN0KCkpOwoKICBhdXRvICpkYXRhc2V0ID0gZXhwZXJpbWVudC5iZW5jaG1hcmsoKTsKICByeDo6T01QTFBsYW5EYXRhU2V0T3V0cHV0dGVyIG91dHB1dCggLy8KICAgICJiZW5jaG1hcmtfZXhhbXBsZSIpOwogIG91dHB1dC5kdW1wKCpkYXRhc2V0KTs=){download=""} 1 rx$::$Profiler$::$Options options; 3 \"example\", // Name of experiment 4 options, // Options for internal profiler 8 experiment.addQuery(\"planner\", 9 scene, planner, request$\rightarrow$getRequest); 11 auto \*dataset = experiment.benchmark; 14 output.dump(\*dataset); Moreover, benchmarking can capture *progress properties* of a motion planner, if properly exposed. These properties are important for profiling the performance of asymptotically (near-)optimal motion planning algorithms, such as rrt\*. An example is shown in footnote 12. *Robowflex*'s benchmarking was used.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Benchmarking Motion Planners", "weight": 1.0} -->

Compared to MoveIt's built in benchmarking capabilities^1313^13 *Robowflex* provides a self-contained means of benchmarking that is more easily extendable. MoveIt's benchmarking requires use of ros Warehouse for constructing benchmark datasets as opposed to *Robowflex*'s simple file storage, and does not easily support planning scenes with obstacle variation, which is important for learning-based methods. For example, take advantage of these two features by running *Robowflex* benchmarking instances in containers federated over many machines. Moreover, *Robowflex* enables creation of custom metrics with access to underlying planner results (e.g,. progress properties are not available in MoveIt, properties of a particular method), and can be run as a single script.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Task and Motion Planning", "weight": 1.0} -->

One of the strengths of *Robowflex* is motion planning in isolation. That is, being able to use many different instances of robots, scenes, and motion planners all within the same script. This is essential to efficient task and motion planning (tamp), as a tamp algorithm will evaluate many different motion plans in a variety of scenes to find a feasible task-and-motion plan. *Robowflex* has been used as the motion planning component in a few tamp algorithms (e.g., ), one of which is shown in Fig. 7. Here, *Robowflex* and *Robowflex*'s dart module are leveraged to provide the motion planning components necessary for a multi-robot tamp algorithm. Crucial to tamp is the evaluation of many possible scene configurations---*Robowflex* allows for many copies of the collision environment to be considered in parallel. Moreover, *Robowflex* enables information on planning progress to be extracted from the underlying planner, which is used to inform the task planner. Finally, the dart module allows for multi-robot planning, as shown in Fig. 4.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Robonaut 2 and nasa", "weight": 1.0} -->

*Robowflex* has also been used by nasa for motion planning for Robonaut 2. Robonaut 2 is a highly dexterous system, with many degrees of freedom. One of the many motion planning challenges Robonaut 2 faces is climbing across handrails in the International Space Station, as shown in Fig. 8. To this end, *Robowflex* was used to evaluate potential handrail grasps and the difficulty of motion planning between different grasps to automate walking across the station. *Robowflex* provides the means to use, inspect, and evaluate custom inverse kinematics solvers for Robonaut 2 and to benchmark the variety of handrail grasp configurations and scenes. Additionally, *Robowflex* was used for the Robonaut 2 experiments and figure. As demonstrated by the examples presented here, the affordances provided by *Robowflex* are general and broadly useful to different members of the robotics community.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have presented *Robowflex*, a c++ library that enables the use of MoveIt in an easier, more flexible way for the creation of advanced robot software for industry, research, and education. The core advantage that *Robowflex* provides over the default distribution of MoveIt is the ability to easily access and modify core data structures within the program itself, rather than through ros messages to the provided MoveGroup program. This also enables the use of motion planning within more complex algorithms, such as task and motion planning approaches. Moreover, *Robowflex* provides a high-level api, enabling many use-cases such as benchmarking and motion planning without any ros or MoveIt expertise required. *Robowflex* also has a number of auxiliary modules that provide access to other robotics libraries and visualization tools, such as ompl, dart, Tesseract, and Blender. Beyond motion planning software development, we hope that *Robowflex* will enable broader application and adoption of motion planning algorithms and raise the level of experimental evaluation in comparisons.
