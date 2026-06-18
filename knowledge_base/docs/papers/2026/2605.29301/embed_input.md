<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Open Motion Planning Library 2.0

Topics include Motion planning, Sampling-based planning, Software libraries, OMPL, Benchmarking, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes OMPL 2.0 as a major update to the long-running Open Motion Planning Library, adding modern planning abstractions, planners, and benchmarking support. The paper is an infrastructure reference for sampling-based motion planning rather than a single-planner algorithm paper.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Open Motion Planning Library (OMPL), first released in 2008, has become a cornerstone of the motion planning community, providing implementations of a wide range of state-of-the-art sampling-based algorithms. Over almost two decades of continuous development, we have steadily expanded the library with new planners, state spaces, and problem formulations. These additions range from asymptotically optimal and lazy planners to constrained motion planning and planning with temporal-logic goals. Building on this foundation, we introduce OMPL 2.0, a major evolution of the library that targets real-time motion planning through hardware acceleration and integrates seamlessly with modern AI research workflows. We also reflect on how OMPL and the field of motion planning have grown together over the years, and discuss the library's broader impact on the research community.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The history of motion planning can be traced back to the late 1970s, when the concept of configuration space was introduced to formally describe robot motion planning problems. Early approaches focused on exact algorithms and potential field methods. However, these techniques often struggled with the high computational complexity of realistic robotic systems, as research has proven that motion planning in configuration space is NP-hard. In the 1990s, sampling-based motion planning emerged as a practical approach. Algorithms such as the probabilistic roadmap (PRM), expansive-space tree (EST), and rapidly-exploring random trees (RRT) developed before 2000, approximate the connectivity of the configuration space through random sampling and enable efficient planning in high-dimensional spaces. These approaches quickly became a dominant paradigm in robotics. Several early sampling-based planners were accompanied by theoretical analyses that characterized their trade-offs. Subsequent research introduced improved sampling strategies and algorithmic refinements. Later, in the 2010s, asymptotically optimal planners such as PRM\*, RRT\*, and SST provided convergence guarantees to optimal solutions. As sampling-based motion planning algorithms rapidly developed, implementing and fairly comparing new planners became increasingly challenging.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Researchers often needed to reimplement existing algorithms and supporting data structures, making reproducibility and benchmarking difficult.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the reproducibility and benchmarking challenges, the Open Motion Planning Library (OMPL) was developed and released in 2008 as an open-source software framework for motion planning. OMPL provides implementations of a wide range of sampling-based planners together with reusable and flexible abstractions for defining planning problems, enabling researchers and practitioners to easily evaluate algorithms, benchmark with other planners, and integrate motion planning into robotics applications.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Almost two decades have passed since OMPL's first release. Over this period, motion planning research, computer architectures, and the broader robotics ecosystem have all advanced substantially. OMPL has evolved alongside these changes, continually incorporating new planners, state space representations, and problem formulations. In this paper, we introduce OMPL 2.0, a major evolution of the library that targets real-time motion planning through hardware acceleration and integrates with modern AI research workflows.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The Open Motion Planning Library", "weight": 1.0} -->

Before introducing new features of OMPL 2.0, we recap the main components of OMPL. This design, introduced in the original OMPL paper, remains largely unchanged and has stood the test of time. OMPL is structured as a set of modular components that correspond closely to the fundamental concepts of sampling-based motion planning. The core abstractions include state space, state validator, state sampler, start and goal, and motion planners, which together define the planning problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Open Motion Planning Library", "weight": 1.0} -->

The *state space* defines the representation and topology of the robot's configuration space, along with its limits and any kinematic or dynamic constraints. A *state validator* provides a generic interface for collision checking, allowing users to connect any collision checking library or simulator. Finally, a *state sampler* draws configurations uniformly or from a Gaussian distribution over the state space. With these foundational components in place, users can select or build their own *motion planner* and specify *start* and *goal* states to solve the problem. Beyond solving individual planning problems, the *benchmark* component provides extensible infrastructure for running evaluations and analysis across multiple planners. Results and metadata are stored in a database to support reproducibility.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Open Motion Planning Library", "weight": 1.0} -->

A key design choice in OMPL is to focus exclusively on motion planning algorithms and to not include specific representations of robots, workspaces, or collision detection. Instead, OMPL relies on external software components to provide these capabilities. This minimalist design allows the library to remain general and easily integrated with a wide range of robotics systems and simulation environments. OMPL is a community effort, with contributions from many researchers over the years.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Two Decades of Adoption", "weight": 1.0} -->

OMPL has become a widely used tool in the motion planning community. The original paper has accumulated over 2,400 citations, reflecting sustained and widespread adoption. By providing carefully maintained reference implementations of canonical planners, it has helped standardize how the community benchmarks and communicates algorithmic contributions, allowing researchers to focus on novel contributions rather than reimplementing baselines.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Two Decades of Adoption", "weight": 1.0} -->

A key factor behind this adoption is OMPL's separation from robot models, workspace representations, and collision geometry. By defining a clean interface around state spaces, validity checkers, and planners, OMPL integrates naturally with external systems without imposing constraints on how they are built. OMPL can be called from MoveIt, robot simulators such as CoppeliaSim and Flightmare, industrial frameworks like Tesseract, and research toolkits including AIKIDO, EXOTica, and the Kautham Project. OMPL's planners have also been used in task-and-motion planning and mobile robot navigation via Nav2, while tools such as HyperPlan, Robowflex, and MotionBenchMaker build on its benchmarking infrastructure for standardized algorithm evaluation. OMPL has also been used in non-robotics applications, such as modeling the conformational flexibility of large macromolecules.

<!-- chunk {"id": "body-0013", "role": "body", "section": "OMPL 2.0: Key Technical Improvements", "weight": 1.0} -->

Rather than emerging from a single landmark release, OMPL has matured through more than a decade of incremental development. Since the publication of the original paper, over 30 versions have been released along the path from OMPL 0.x through OMPL 1.0 to OMPL 2.0, each contributing new algorithms and capabilities. These updates reflect both advances in motion planning research and the evolving needs of the robotics community.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Set Expansion", "weight": 1.0} -->

OMPL 2.0 now supports a wider range of planning paradigms, including asymptotically optimal planners \[42, 10: informed asymptotically optimal anytime search")\] and lazy planning methods. Beyond extending its set of algorithms, OMPL 2.0 has also broadened the kinds of planning problems it can express. Constrained motion planning enables any sampling-based planner to operate directly on an implicit constraint manifold, supporting practical problems involving contact constraints and closed kinematic chains. For task-level specifications, LTLPlanner is a kinodynamic planner that produces trajectories satisfying a given linear temporal logic formula by searching the cross product of the continuous state space and the discrete space of the formula's accepting traces. In addition, the library has expanded its set of state space representations to cover a broader class of problems, including discrete state spaces, time-augmented spaces for planning under temporal constraints, and non-Euclidean spaces such as Dubins and Reeds--Shepp for car-like vehicles. Together, these additions significantly broaden the types of planning problems that can be addressed within OMPL 2.0.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Set Expansion", "weight": 1.0} -->

The ever-growing number of planning algorithms, each with its own parameters, can make it challenging to select an appropriate planner for a specific robot or environment. We have shown that hyperparameter tuning can be used as an effective tool for planning algorithm selection and tuning.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Performance Evolution", "weight": 1.0} -->

Beyond advances in planning algorithms, OMPL 2.0 integrates VAMP, which leverages CPU SIMD instructions to perform collision checking and forward kinematics with fine-grained, hardware-efficient parallelism. With this integration, planners can find solutions in microseconds, and aggregate solution rates can reach the kilohertz range, all without specialized hardware such as a GPU. OMPL now also includes CAPT, which extends the SIMD philosophy to point cloud collision checking. These capabilities open up new opportunities for applications that require extremely fast planning in dynamic environments, including reactive planning and task-and-motion planning. The OMPL 2.0's integration with VAMP and CAPT also makes it straightforward to apply motion planning to realistic robots operating in real-world scenes (see Fig. 1).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Modernized Development Infrastructure", "weight": 1.0} -->

When OMPL was first released, many of the software development tools and practices now common in open-source projects were not yet widely adopted. At the time, OMPL used Py++ to generate its Python bindings. The tool is no longer maintained. To address this, OMPL 2.0 has transitioned to nanobind, a modern C++ binding framework that provides a lightweight and efficient interface between C++ and Python while simplifying the maintenance of binding code. In addition, OMPL 2.0 has adopted contemporary development infrastructure such as GitHub Actions for continuous integration, enabling automated building and testing across multiple platforms. The project also employs automated pipelines to build and publish Python wheels to PyPI, significantly simplifying installation and distribution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Streamlining", "weight": 1.0} -->

Earlier versions of OMPL included OMPL.app, a graphical front end that demonstrated integration with external libraries for mesh loading, collision checking, and visualization. Over the past decade, the robotics ecosystem has matured, with widely used simulation platforms and collision detection libraries that integrate naturally with OMPL, making a dedicated graphical interface no longer necessary. OMPL.app has therefore been removed in OMPL 2.0, allowing the library to focus on efficient planning infrastructure and tighter integration with external robotics software.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Project Community and Organization", "weight": 1.0} -->

The goal from the beginning of the OMPL project has always been to create a resource that is useful for research, education, and real-world use. This goal has been achieved, but it is also something that requires ongoing effort to retain relevance. Long-term software maintenance and support remain a challenge in an academic environment. Shortly after the initial release, we organized a few tutorials at robotics conferences to get researchers started with OMPL and help start a user community. Improved documentation and more general awareness of OMPL have reduced the need for this. We provide the link to the most recent OMPL tutorial.^11^1

<!-- chunk {"id": "body-0020", "role": "body", "section": "Project Community and Organization", "weight": 1.0} -->

We also decided early on to spend significant time on building an extensible infrastructure for benchmarking motion planning algorithms. This has been invaluable in quantifying how new planners advance the state of the art. More recently, we have also generated large datasets of realistic hard motion planning problems (and made the tooling for generating such datasets available as well). Benchmark results can be visualized through an interactive browser-based tool called Planner Arena.^22^2 Fig. 2 shows sample results for a parameterized benchmark. The parameters in this case are the specific motion planning problem, how the environment is represented (mesh vs. point cloud), and the type of robot (a Fetch, a Panda, and a UR5 in this example). The UI enables comparison of planning algorithms on all robots for a single problem, on a single robot on all problems, etc. In each case, there are many performance metrics that can be visualized, such as planning time and solution path length. The table in the bottom right shows the number of missing values: if a planner was not able to find a path on some runs, the path length would be considered missing for those runs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Project Community and Organization", "weight": 1.0} -->

In summary, Planner Arena encourages exploration and a nuanced characterization of planner performance.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Project Community and Organization", "weight": 1.0} -->

The abstractions that OMPL imposes on planning algorithms are minimal and make it straightforward to develop prototypes of planners. Evaluation in simplified environments (e.g., a point robot in 2D) makes testing easy, before deployment in realistic environments without having to change the planning algorithm implementation itself.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Project Community and Organization", "weight": 1.0} -->

Many motion planning researchers have developed new motion planning algorithms using OMPL. Oftentimes, the original authors contributed their implementations to the OMPL repository. For example, Karaman and Frazzoli contributed the initial RRT\* implementation to OMPL shortly after publication. Bekris et al. contributed implementations of their asymptotically near-optimal algorithms. Gammell et al. have contributed many algorithms such as BIT\*, ABIT\*, AIT\*, EIT\*, and AORRTC \[39 and effort informed trees (eit*): asymmetric bidirectional sampling-based path planning"), 42\]. Orthey et al. have contributed implementations of their work on multi-level planning and planning in space-time. This is by no means an exclusive list.^33^3A list of contributors is maintained in

<!-- chunk {"id": "body-0024", "role": "body", "section": "Project Community and Organization", "weight": 1.0} -->

Over time, the OMPL community has grown to include many AI researchers, who often use OMPL simply as a black box. Because Python is the primary language for integrating software components in the AI community, OMPL's Python bindings have become increasingly important. Originally, these bindings were intended mainly to lower the barrier to entry for beginning programmers. Today, their performance penalty is small enough to be acceptable for many use cases, though we still recommend the C++ API directly when optimal performance is needed.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Next Decade of OMPL", "weight": 1.0} -->

Looking ahead, we see several directions that will shape the future development of OMPL. Motion planning is increasingly used as a component within larger decision-making systems: task and motion planning combines symbolic reasoning with geometric planning, planning under uncertainty, such as POMDPs, demands rapid replanning as beliefs evolve, and reactive planning requires algorithms that quickly adapt to changing environments. Supporting these paradigms will require continued investment in fast, anytime planning and interfaces that facilitate integration with higher-level reasoning. Beyond robotics pipelines, OMPL can also serve the broader AI ecosystem. By providing a Model Context Protocol server and agent skills, we aim to let LLM-based agents invoke motion planning directly as a tool.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Next Decade of OMPL", "weight": 1.0} -->

As robotic systems scale from single manipulators to teams of cooperating robots, multi-robot planning in composite configuration spaces becomes a central challenge. Recent work has shown that sampling-based methods can be extended to these settings by exploiting problem structure, and future versions of OMPL aim to provide support for multi-robot coordination. At the same time, GPU-parallel approaches to tree construction and collision checking offer the potential for massive speedups. Finally, emerging applications in soft and growing robots involve high-dimensional, continuously deformable state spaces that challenge existing representations and will require extending OMPL's state space abstractions to new physical domains.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Next Decade of OMPL", "weight": 1.0} -->

These directions share a common theme: the core abstractions of sampling-based planning remain the right foundation, but must be extended to meet the demands of increasingly complex robotic systems. We see OMPL 2.0 not as an endpoint, but as a starting point for the next decade of motion planning research.
