<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

dm_control: Software and Tasks for Continuous Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The dm_control software package is a collection of Python libraries and task suites for reinforcement learning agents in an articulated-body simulation. A MuJoCo wrapper provides convenient bindings to functions and data structures. The PyMJCF and Composer libraries enable procedural model manipulation and task authoring. The Control Suite is a fixed set of tasks with standardised structure, intended to serve as performance benchmarks. The Locomotion framework provides high-level abstractions and examples of locomotion tasks. A set of configurable manipulation tasks with a robot arm and snap-together bricks is also included. dm_control is publicly available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controlling the physical world is an integral part and arguably a prerequisite of general intelligence. Indeed, the only known example of general-purpose intelligence emerged in primates whose behavioural niche was already contingent on two-handed manipulation for millions of years.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unlike board games, language and other symbolic domains, physical tasks are fundamentally continuous in state, time and action. Physical dynamics are subject to second-order equations of motion -- the underlying state is composed of positions and velocities. Sensory signals (i.e. observations) carry meaningful physical units and vary over corresponding timescales. These properties, along with their prevalence and importance, make control problems a unique subset of general Markov Decision Processes. The most familiar physical control tasks have a fixed subset of degrees of freedom (the *body*) that are directly actuated, while the rest are unactuated (the *environment*). Such *embodied* tasks are the focus of dm_control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Software for research", "weight": 1.0} -->

The dm_control package was designed by DeepMind scientists and engineers to facilitate their own continuous control and robotics needs, and is therefore well-suited for research. It is written in Python, exploiting the agile workflow of a dynamic language, while relying on the C-based MuJoCo physics library, a fast and accurate simulator, itself designed to facilitate research.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Software for research", "weight": 1.0} -->

The ctypes-based MuJoCo wrapper (Sec. 2) provides full access to the simulator, conveniently exposing quantities with named indexing. A Python-based interactive visualiser (Sec. 2.2) allows the user to examine and perturb scene elements with a mouse.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Software for research", "weight": 1.0} -->

The PyMJCF library (Sec. 3) can procedurally assemble model elements and allows the user to configure or randomise parameters and initial states.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Software for research", "weight": 1.0} -->

An environment API that exposes actions, observations, rewards and terminations in a consistent yet flexible manner (Sec. 4).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Software for research", "weight": 1.0} -->

Finally, we combine the above functionality in the high-level task-definition framework Composer (Sec. 5). Amongst other things it provides a Model Variation module (Sec. 5.2) for policy robustification, and an Observable module for delayed, corrupted, and stacked sensor data (Sec. 5.1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Software for research", "weight": 1.0} -->

dm_control has been used extensively in DeepMind, serving as a fundamental component of continuous control research. See \\href for a montage of clips from selected publications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Tasks", "weight": 1.0} -->

Recent years have seen rapid progress in the application of Reinforcement Learning (RL) to difficult problem domains such as video games. The Arcade Learning Environment was and continues to be a vital facilitator of these developments, providing a set of standard benchmarks for evaluating and comparing learning algorithms. Similarly, it could be argued that control and robotics require well-designed task suites as a standardised playing field, where different approaches can compete and new ones can emerge.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tasks", "weight": 1.0} -->

The OpenAI Gym includes a set of continuous control domains that have become a popular benchmark in continuous RL. More recent task suites such as Meta-world, SURREAL, RLbench and IKEA, have been published in an attempt to satisfy the demand for tasks suites that facilitate the study of algorithms related to multi-scale control, multi-task transfer, and meta learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Tasks", "weight": 1.0} -->

The DeepMind Control Suite (Section 6), first introduced, built directly with the MuJoCo wrapper, provides a set of standard benchmarks for continuous control problems. The unified reward structure offers interpretable learning curves and aggregated suite-wide performance measures. Furthermore, we emphasise high-quality, well-documented code using uniform design patterns, offering a readable, transparent and easily extensible codebase.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Tasks", "weight": 1.0} -->

The Locomotion framework (Section 7) was inspired by our work in Heess et al.. It is designed to facilitate the implementation of a wide range of locomotion tasks for RL algorithms by introducing self-contained, reusable components which compose into different task variants. The Locomotion framework has enabled a number of research efforts including Merel et al., Merel et al., Merel et al. and more recently has been employed to support Multi-Agent domains in Liu et al., Sunehag et al. and Banarse et al..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tasks", "weight": 1.0} -->

We also provide examples of constructing robotic manipulation tasks (Sec. 8). These tasks involve grabbing and manipulating objects with a 3D robotic arm. The set of tasks includes examples of reaching, placing, stacking, throwing, assembly and disassembly. The tasks are designed to be solved using a simulated 6 degree-of-freedom robotic arm based on the Kinova Jaco, though their modular design permit the use of other arms with minimal changes. These tasks make use of reusable components such as bricks that snap together, and provide examples of reward functions for manipulation. Tasks can be run using vision, low-level features, or combinations of both.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Part I Software Infrastructure", "weight": 1.0} -->

Sections 2, 3, 4 and 5 include code snippets showing how to use dm_control software.

<!-- chunk {"id": "body-0017", "role": "body", "section": "MuJoCo Python interface", "weight": 1.0} -->

The mujoco module provides a general-purpose wrapper of the MuJoCo engine, using Python's \\href library to auto-generate bindings to MuJoCo structs, enums and API functions. We provide a brief introductory overview which assumes familiarity with Python; see in-code documentation for more detail.

<!-- chunk {"id": "body-0018", "role": "body", "section": "MuJoCo physics", "weight": 1.0} -->

MuJoCo is a fast, reduced-coordinate, continuous-time physics engine. It compares favourably to other popular simulators, especially for articulated, low-to-medium degree-of-freedom regimes ($\lessapprox 100$) in the presence of contacts. The \\href model definition format and reconfigurable computation pipeline have made MuJoCo a popular choice for robotics and reinforcement learning research.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The Physics class encapsulates MuJoCo's most commonly used functionality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The Physics.from_xml_string

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBtdWpvY28Kc2ltcGxlX01KQ0YgPSAiIiIKPG11am9jbz4KICA8d29ybGRib2R5PgogICAgPGxpZ2h0IG5hbWU9InRvcCIgcG9zPSIwIDAgMSIvPgogICAgPGJvZHkgbmFtZT0iYm94X2FuZF9zcGhlcmUiIGV1bGVyPSIwIDAgLTMwIj4KICAgICAgPGpvaW50IG5hbWU9InN3aW5nIiB0eXBlPSJoaW5nZSIgYXhpcz0iMSAtMSAwIiBwb3M9Ii0uMiAtLjIgLS4yIi8+CiAgICAgIDxnZW9tIG5hbWU9InJlZF9ib3giIHR5cGU9ImJveCIgc2l6ZT0iLjIgLjIgLjIiIHJnYmE9IjEgMCAwIDEiLz4KICAgICAgPGdlb20gbmFtZT0iZ3JlZW5fc3BoZXJlIiBwb3M9Ii4yIC4yIC4yIiBzaXplPSIuMSIgcmdiYT0iMCAxIDAgMSIvPgogICAgPC9ib2R5PgogIDwvd29ybGRib2R5Pgo8L211am9jbz4KIiIiCnBoeXNpY3MgPSBtdWpvY28uUGh5c2ljcy5mcm9tX3htbF9zdHJpbmcoc2ltcGxlX01KQ0Yp){download=""}

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics = mujoco.Physics.from_xml_string(simple_MJCF)

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Physics class", "weight": 1.0} -->

The Physics.render method outputs a NumPy array of pixel values.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,cGl4ZWxzID0gcGh5c2ljcy5yZW5kZXIoKQ==){download=""}

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.65]figure[\FBwidth]
Optional arguments to render specify the resolution, camera ID, whether to render RGB, depth or segmentation images, and other visualisation options (e.g. the joint visualisation on the left). dm_control on Linux supports both OSMesa software rendering and hardware-accelerated rendering using either EGL or GLFW. The rendering backend can be selected by setting the MUJOCO_GL environment variable to glfw, egl, or osmesa, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Physics class", "weight": 1.0} -->

: Physics.model and Physics.data

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Physics class", "weight": 1.0} -->

MuJoCo's underlying mjModel and mjData data structures, describing static and dynamic simulation parameters respectively, can be accessed via the model and data properties of Physics. They contain NumPy arrays that have direct, writeable views onto MuJoCo's internal memory.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,IyBUaGlzIGZhaWxzIHdpdGggYEF0dHJpYnV0ZUVycm9yOiBjYW4ndCBzZXQgYXR0cmlidXRlYDoKcGh5c2ljcy5kYXRhLnFwb3MgPSBucC5yYW5kb20ucmFuZG4ocGh5c2ljcy5tb2RlbC5ucSkKIyBUaGlzIHN1Y2NlZWRzOgpwaHlzaWNzLmRhdGEucXBvc1s6XSA9IG5wLnJhbmRvbS5yYW5kbihwaHlzaWNzLm1vZGVsLm5xKQ==){download=""}

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qpos = np.random.randn(physics.model.nq)

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qpos = np.random.randn(physics.model.nq)

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Physics class", "weight": 1.0} -->

MuJoCo's top-level mj_step function computes the next state --- the joint-space configuration qpos and velocity qvel --- in two stages. Quantities that depend only on the state are computed in the first stage, mj_step1, and those that also depend on the control (including forces) are computed in the subsequent mj_step2. Physics.step calls these sub-functions in reverse order, as follows. Assuming that mj_step1 has already been called, it first completes the computation of the new state with mj_step2, and then calls mj_step1, updating the quantities that depend on the state alone. In particular, this means that after a Physics.step, rendered pixels will correspond to the current state, rather than the previous one. Quantities that depend on forces, like accelerometer and touch sensor readings, are still with respect to the last transition.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Physics class", "weight": 1.0} -->

: Setting the state with reset_context

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Physics class", "weight": 1.0} -->

For the above assumption above to hold, mj_step1 must always be called after setting the state. We therefore provide the Physics.reset_context,

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,d2l0aCBwaHlzaWNzLnJlc2V0X2NvbnRleHQoKToKICAgIyBtal9yZXNldCgpIGlzIGNhbGxlZCB1cG9uIGVudGVyaW5nIHRoZSBjb250ZXh0OiBkZWZhdWx0IHN0YXRlLgogICBwaHlzaWNzLmRhdGEucXBvc1s6XSA9IC4uLiAgIyBTZXQgcG9zaXRpb24uCiAgIHBoeXNpY3MuZGF0YS5xdmVsWzpdID0gLi4uICAjIFNldCB2ZWxvY2l0eS4KIyBtal9mb3J3YXJkKCkgaXMgY2FsbGVkIHVwb24gZXhpdGluZyB0aGUgY29udGV4dC4gTm93IGFsbCBkZXJpdmVkCiMgcXVhbnRpdGllcyBhbmQgc2Vuc29yIG1lYXN1cmVtZW50cyBhcmUgdXAtdG8tZGF0ZS4=){download=""}

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Physics class", "weight": 1.0} -->

\# mj_reset is called upon entering the context: default state.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qpos = \... \# Set position.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.data.qvel = \... \# Set velocity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Physics class", "weight": 1.0} -->

\# mj_forward is called upon exiting the context. Now all derived

<!-- chunk {"id": "body-0039", "role": "body", "section": "The Physics class", "weight": 1.0} -->

\# quantities and sensor measurements are up-to-date.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Note that we call mj_forward upon exit, which includes mj_step1, but continues up to the computation of accelerations (but does not increment the state). This is so that force- or acceleration-dependent sensors have sensible values even at the initial state, before any steps have been taken.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Everything in a MuJoCo model can be named. It is often more convenient and less error-prone to refer to model elements by name rather than by index. To address this, Physics.named.model and Physics.named.data provide array-like containers that provide convenient named views.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,cHJpbnQoIlRoZSBgZ2VvbV94cG9zYCBhcnJheToiKQpwcmludChwaHlzaWNzLmRhdGEuZ2VvbV94cG9zKQpwcmludCgiSXMgbXVjaCBlYXNpZXIgdG8gaW5zcGVjdCB1c2luZyBgUGh5c2ljcy5uYW1lZGA6IikKcHJpbnQocGh5c2ljcy5uYW1lZC5kYXRhLmdlb21feHBvcyk=){download=""}

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(\"The 'geom_xpos' array:\")

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(physics.data.geom_xpos)

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(\"Is much easier to inspect using 'Physics.named':\")

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(physics.named.data.geom_xpos)

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,VGhlIGBnZW9tX3hwb3NgIGFycmF5OgpbWzAuICAgICAgICAgMC4gICAgICAgICAwLiAgICAgICAgXQogWzAuMjczMjA1MDggMC4wNzMyMDUwOCAwLjIgICAgICAgXV0KSXMgbXVjaCBlYXNpZXIgdG8gaW5zcGVjdCB1c2luZyBgUGh5c2ljcy5uYW1lZGA6CiAgICAgICAgICAgICAgICAgeCAgICAgICAgIHkgICAgICAgICB6CjAgICAgICByZWRfYm94IFsgMCAgICAgICAgIDAgICAgICAgICAwICAgICAgIF0KMSBncmVlbl9zcGhlcmUgWyAwLjI3MyAgICAgMC4wNzMyICAgIDAuMiAgICAgXQ==){download=""}

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Is much easier to inspect using 'Physics.named':

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,d2l0aCBwaHlzaWNzLnJlc2V0X2NvbnRleHQoKToKICBwaHlzaWNzLm5hbWVkLmRhdGEucXBvc1snc3dpbmcnXSA9IG5wLnBpCnByaW50KHBoeXNpY3MubmFtZWQuZGF0YS5nZW9tX3hwb3NbJ2dyZWVuX3NwaGVyZScsIFsneiddXSk=){download=""}

<!-- chunk {"id": "body-0050", "role": "body", "section": "The Physics class", "weight": 1.0} -->

physics.named.data.qpos\['swing'\] = np.pi

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Physics class", "weight": 1.0} -->

print(physics.named.data.geom_xpos\['green_sphere', \['z'\]\])

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,Wy0wLjZd){download=""}

<!-- chunk {"id": "body-0053", "role": "body", "section": "The Physics class", "weight": 1.0} -->

Note that in the example above we use a joint name in order to index into the generalised position array qpos. Indexing into a multi-DoF ball or free joint outputs the appropriate slice.

<!-- chunk {"id": "body-0054", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,cGh5c2ljcy5tb2RlbC5pZDJuYW1lKDAsICJnZW9tIik=){download=""}

<!-- chunk {"id": "body-0055", "role": "body", "section": "The Physics class", "weight": 1.0} -->

[⬇](data:text/plain;base64,J3JlZF9ib3gn){download=""}

<!-- chunk {"id": "body-0056", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

The viewer module provides playback and interaction with physical models using mouse input. This type of visual debugging is often critical for cases when an agent finds an "exploit" in the physics.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBzdWl0ZSwgdmlld2VyCgplbnZpcm9ubWVudCA9IHN1aXRlLmxvYWQoZG9tYWluX25hbWU9Imh1bWFub2lkIiwgdGFza19uYW1lPSJzdGFuZCIpCgojIERlZmluZSBhIHVuaWZvcm0gcmFuZG9tIHBvbGljeS4Kc3BlYyA9IGVudmlyb25tZW50LmFjdGlvbl9zcGVjKCkKZGVmIHJhbmRvbV9wb2xpY3kodGltZV9zdGVwKToKICByZXR1cm4gbnAucmFuZG9tLnVuaWZvcm0oc3BlYy5taW5pbXVtLCBzcGVjLm1heGltdW0sIHNwZWMuc2hhcGUpCgojIExhdW5jaCB0aGUgdmlld2VyIGFwcGxpY2F0aW9uLgp2aWV3ZXIubGF1bmNoKGVudmlyb25tZW50LCBwb2xpY3k9cmFuZG9tX3BvbGljeSk=){download=""}

<!-- chunk {"id": "body-0058", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

from dm_control import suite, viewer

<!-- chunk {"id": "body-0059", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

environment = suite.load(domain_name=\"humanoid\", task_name=\"stand\")

<!-- chunk {"id": "body-0060", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

return np.random.uniform(spec.minimum, spec.maximum, spec.shape)

<!-- chunk {"id": "body-0061", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

viewer.launch(environment, policy=random_policy)

<!-- chunk {"id": "body-0062", "role": "body", "section": "Interactive Viewer", "weight": 1.0} -->

See the documentation at \\href for a screen capture of the viewer application.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

The bindings provide easy access to all MuJoCo library functions and enums, automatically converting NumPy arrays to data pointers where appropriate.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLm11am9jby53cmFwcGVyLm1qYmluZGluZ3MgaW1wb3J0IG1qbGliCmltcG9ydCBudW1weSBhcyBucAoKcXVhdCA9IG5wLmFycmF5KCguNSwgLjUsIC41LCAuNSkpCm1hdCA9IG5wLnplcm9zKDkpCm1qbGliLm1qdV9xdWF0Mk1hdChtYXQsIHF1YXQpCgpwcmludCgiTXVKb0NvIGNvbnZlcnRzIHRoaXMgcXVhdGVybmlvbjoiKQpwcmludChxdWF0KQpwcmludCgiVG8gdGhpcyByb3RhdGlvbiBtYXRyaXg6IikKcHJpbnQobWF0LnJlc2hhcGUoMywzKSk=){download=""}

<!-- chunk {"id": "body-0065", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

from dm_control.mujoco.wrapper.mjbindings import mjlib

<!-- chunk {"id": "body-0066", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

mjlib.mju_quat2Mat(mat, quat)

<!-- chunk {"id": "body-0067", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

print(\"MuJoCo converts this quaternion:\")

<!-- chunk {"id": "body-0068", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

[⬇](data:text/plain;base64,TXVKb0NvIGNvbnZlcnRzIHRoaXMgcXVhdGVybmlvbjoKWyAwLjUgIDAuNSAgMC41ICAwLjVdClRvIHRoaXMgcm90YXRpb24gbWF0cml4OgpbWyAwLiAgMC4gIDEuXQogWyAxLiAgMC4gIDAuXQogWyAwLiAgMS4gIDAuXV0=){download=""}

<!-- chunk {"id": "body-0069", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLm11am9jby53cmFwcGVyLm1qYmluZGluZ3MgaW1wb3J0IGVudW1zCnByaW50KGVudW1zLm1qdEpvaW50KQ==){download=""}

<!-- chunk {"id": "body-0070", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

from dm_control.mujoco.wrapper.mjbindings import enums

<!-- chunk {"id": "body-0071", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

[⬇](data:text/plain;base64,bWp0Sm9pbnQobWpKTlRfRlJFRT0wLCBtakpOVF9CQUxMPTEsIG1qSk5UX1NMSURFPTIsIG1qSk5UX0hJTkdFPTMp){download=""}

<!-- chunk {"id": "body-0072", "role": "body", "section": "Wrapper bindings", "weight": 1.0} -->

mjtJoint(mjJNT_FREE=0, mjJNT_BALL=1, mjJNT_SLIDE=2, mjJNT_HINGE=3)

<!-- chunk {"id": "body-0073", "role": "body", "section": "The PyMJCF library", "weight": 1.0} -->

The PyMJCF library provides a Python object model for MuJoCo's MJCF modelling language, which can describe complex scenes with articulated bodies. The goal of the library is to allow users to interact with and modify MJCF models programmatically using Python, similarly to what the JavaScript DOM does for HTML.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The PyMJCF library", "weight": 1.0} -->

A key feature of the library is the ability to compose multiple MJCF models into a larger one, while automatically maintaining a consistent, collision-free namespace. Additionally, it provides Pythonic access to the underlying C data structures with the bind method of mjcf.Physics, a subclass of Physics which associates a compiled model with the PyMJCF object tree.

<!-- chunk {"id": "body-0075", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

The following code snippets constitute a tutorial example of a typical use case.

<!-- chunk {"id": "body-0076", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBtamNmCgpjbGFzcyBMZWcob2JqZWN0KToKICAiIiIgQSAyLURvRiBsZWcgd2l0aCBwb3NpdGlvbiBhY3R1YXRvcnMuIiIiCiAgZGVmIF9faW5pdF9fKHNlbGYsIGxlbmd0aCwgcmdiYSk6CiAgICBzZWxmLm1vZGVsID0gbWpjZi5Sb290RWxlbWVudCgpCgogICAgIyBEZWZhdWx0czoKICAgIHNlbGYubW9kZWwuZGVmYXVsdC5qb2ludC5kYW1waW5nID0gMgogICAgc2VsZi5tb2RlbC5kZWZhdWx0LmpvaW50LnR5cGUgPSAnaGluZ2UnCiAgICBzZWxmLm1vZGVsLmRlZmF1bHQuZ2VvbS50eXBlID0gJ2NhcHN1bGUnCiAgICBzZWxmLm1vZGVsLmRlZmF1bHQuZ2VvbS5yZ2JhID0gcmdiYSAgIyBDb250aW51ZWQgYmVsb3cuLi4KICAgICMgVGhpZ2g6CiAgICBzZWxmLnRoaWdoID0gc2VsZi5tb2RlbC53b3JsZGJvZHkuYWRkKCdib2R5JykKICAgIHNlbGYuaGlwID0gc2VsZi50aGlnaC5hZGQoJ2pvaW50JywgYXhpcz1bMCwgMCwgMV0pCiAgICBzZWxmLnRoaWdoLmFkZCgnZ2VvbScsIGZyb210bz1bMCwgMCwgMCwgbGVuZ3RoLCAwLCAwXSwgc2l6ZT1bbGVuZ3RoLzRdKQoKICAgICMgU2hpbjoKICAgIHNlbGYuc2hpbiA9IHNlbGYudGhpZ2guYWRkKCdib2R5JywgcG9zPVtsZW5ndGgsIDAsIDBdKQogICAgc2VsZi5rbmVlID0gc2VsZi5zaGluLmFkZCgnam9pbnQnLCBheGlzPVswLCAxLCAwXSkKICAgIHNlbGYuc2hpbi5hZGQoJ2dlb20nLCBmcm9tdG89WzAsIDAsIDAsIDAsIDAsIC1sZW5ndGhdLCBzaXplPVtsZW5ndGgvNV0pCgogICAgIyBQb3NpdGlvbiBhY3R1YXRvcnM6CiAgICBzZWxmLm1vZGVsLmFjdHVhdG9yLmFkZCgncG9zaXRpb24nLCBqb2ludD1zZWxmLmhpcCwga3A9MTApCiAgICBzZWxmLm1vZGVsLmFjdHVhdG9yLmFkZCgncG9zaXRpb24nLCBqb2ludD1zZWxmLmtuZWUsIGtwPTEwKQ==){download=""}

<!-- chunk {"id": "body-0077", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\"\"\" A 2-DoF leg with position actuators.\"\"\"

<!-- chunk {"id": "body-0078", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.model.default.joint.damping = 2

<!-- chunk {"id": "body-0079", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.model.default.joint.type = 'hinge'

<!-- chunk {"id": "body-0080", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.model.default.geom.type = 'capsule'

<!-- chunk {"id": "body-0081", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.model.default.geom.rgba = rgba \# Continued below\.

<!-- chunk {"id": "body-0082", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.thigh = self.model.worldbody.add('body')

<!-- chunk {"id": "body-0083", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.hip = self.thigh.add('joint', axis=)

<!-- chunk {"id": "body-0084", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.thigh.add('geom', fromto=\[0, 0, 0, length, 0, 0\], size=\[length/4\])

<!-- chunk {"id": "body-0085", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.shin = self.thigh.add('body', pos=\[length, 0, 0\])

<!-- chunk {"id": "body-0086", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.knee = self.shin.add('joint', axis=)

<!-- chunk {"id": "body-0087", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.shin.add('geom', fromto=\[0, 0, 0, 0, 0, -length\], size=\[length/5\])

<!-- chunk {"id": "body-0088", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.model.actuator.add('position', joint=self.hip, kp=10)

<!-- chunk {"id": "body-0089", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

self.model.actuator.add('position', joint=self.knee, kp=10)

<!-- chunk {"id": "body-0090", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

The Leg class describes an abstract articulated leg, with two joints and corresponding proportional-derivative actuators. Note the following.

<!-- chunk {"id": "body-0091", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

MJCF attributes correspond directly to arguments of the add method^11^1The exception is the class attribute which is a reserved Python symbol and renamed dclass..

<!-- chunk {"id": "body-0092", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

When referencing elements, e.g. when specifying the joint to which an actuator is attached in the last two lines above, the MJCF element itself can be used, rather than its name (though a name string is also supported).

<!-- chunk {"id": "body-0093", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,Qk9EWV9SQURJVVMgPSAwLjEKQk9EWV9TSVpFID0gKEJPRFlfUkFESVVTLCBCT0RZX1JBRElVUywgQk9EWV9SQURJVVMgLyAyKQoKZGVmIG1ha2VfY3JlYXR1cmUobnVtX2xlZ3MpOgogICIiIkNvbnN0cnVjdHMgYSBjcmVhdHVyZSB3aXRoIGBudW1fbGVnc2AgbGVncy4iIiIKICByZ2JhID0gbnAucmFuZG9tLnVuaWZvcm0oWzAsIDAsIDAsIDFdLCBbMSwgMSwgMSwgMV0pCiAgbW9kZWwgPSBtamNmLlJvb3RFbGVtZW50KCkKICBtb2RlbC5jb21waWxlci5hbmdsZSA9ICdyYWRpYW4nICAjIFVzZSByYWRpYW5zLgoKICAjIE1ha2UgdGhlIHRvcnNvIGdlb20uCiAgdG9yc28gPSBtb2RlbC53b3JsZGJvZHkuYWRkKAogICAgICAnZ2VvbScsIG5hbWU9J3RvcnNvJywgdHlwZT0nZWxsaXBzb2lkJywgc2l6ZT1CT0RZX1NJWkUsIHJnYmE9cmdiYSkKCiAgIyBBdHRhY2ggbGVncyB0byBlcXVpZGlzdGFudCBzaXRlcyBvbiB0aGUgY2lyY3VtZmVyZW5jZS4KICBmb3IgaSBpbiByYW5nZShudW1fbGVncyk6CiAgICB0aGV0YSA9IDIgKiBpICogbnAucGkgLyBudW1fbGVncwogICAgaGlwX3BvcyA9IEJPRFlfUkFESVVTICogbnAuYXJyYXkoW25wLmNvcyh0aGV0YSksIG5wLnNpbih0aGV0YSksIDBdKQogICAgaGlwX3NpdGUgPSBtb2RlbC53b3JsZGJvZHkuYWRkKCdzaXRlJywgcG9zPWhpcF9wb3MsIGV1bGVyPVswLCAwLCB0aGV0YV0pCiAgICBsZWcgPSBMZWcobGVuZ3RoPUJPRFlfUkFESVVTLCByZ2JhPXJnYmEpCiAgICBoaXBfc2l0ZS5hdHRhY2gobGVnLm1vZGVsKQoKICByZXR1cm4gbW9kZWw=){download=""}

<!-- chunk {"id": "body-0094", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

BODY_SIZE = (BODY_RADIUS, BODY_RADIUS, BODY_RADIUS / 2)

<!-- chunk {"id": "body-0095", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\"\"\"Constructs a creature with 'num_legs' legs.\"\"\"

<!-- chunk {"id": "body-0096", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

model.compiler.angle = 'radian' \# Use radians.

<!-- chunk {"id": "body-0097", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

'geom', name='torso', type='ellipsoid', size=BODY_SIZE, rgba=rgba)

<!-- chunk {"id": "body-0098", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Attach legs to equidistant sites on the circumference.

<!-- chunk {"id": "body-0099", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

hip_pos = BODY_RADIUS \* np.array(\[np.cos(theta), np.sin(theta), 0\])

<!-- chunk {"id": "body-0100", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

hip_site = model.worldbody.add('site', pos=hip_pos, euler=\[0, 0, theta\])

<!-- chunk {"id": "body-0101", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

leg = Leg(length=BODY_RADIUS, rgba=rgba)

<!-- chunk {"id": "body-0102", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

hip_site.attach(leg.model)

<!-- chunk {"id": "body-0103", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

The make_creature function uses PyMJCF's attach method to procedurally attach legs to the torso. Note that both the torso and hip attachment sites are children of the worldbody, since their parent body has yet to be instantiated.

<!-- chunk {"id": "body-0104", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,YXJlbmEgPSBtamNmLlJvb3RFbGVtZW50KCkKY2hlY2tlciA9IGFyZW5hLmFzc2V0LmFkZCgndGV4dHVyZScsIHR5cGU9JzJkJywgYnVpbHRpbj0nY2hlY2tlcicsIHdpZHRoPTMwMCwKICAgICAgICAgICAgICAgICAgICAgICAgICBoZWlnaHQ9MzAwLCByZ2IxPVsuMiwgLjMsIC40XSwgcmdiMj1bLjMsIC40LCAuNV0pCmdyaWQgPSBhcmVuYS5hc3NldC5hZGQoJ21hdGVyaWFsJywgbmFtZT0nZ3JpZCcsIHRleHR1cmU9Y2hlY2tlciwKICAgICAgICAgICAgICAgICAgICAgICB0ZXhyZXBlYXQ9WzUsNV0sIHJlZmxlY3RhbmNlPS4yKQphcmVuYS53b3JsZGJvZHkuYWRkKCdnZW9tJywgdHlwZT0ncGxhbmUnLCBzaXplPVsyLCAyLCAuMV0sIG1hdGVyaWFsPWdyaWQpCmZvciB4IGluIFstMiwgMl06CiAgYXJlbmEud29ybGRib2R5LmFkZCgnbGlnaHQnLCBwb3M9W3gsIC0xLCAzXSwgZGlyPVsteCwgMSwgLTJdKQ==){download=""}

<!-- chunk {"id": "body-0105", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

checker = arena.asset.add('texture', type='2d', builtin='checker', width=300,

<!-- chunk {"id": "body-0106", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

grid = arena.asset.add('material', name='grid', texture=checker,

<!-- chunk {"id": "body-0107", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

arena.worldbody.add('geom', type='plane', size=\[2, 2,.1\], material=grid)

<!-- chunk {"id": "body-0108", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

arena.worldbody.add('light', pos=\[x, -1, 3\], dir=\[-x, 1, -2\])

<!-- chunk {"id": "body-0109", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,IyBJbnN0YW50aWF0ZSA2IGNyZWF0dXJlcyB3aXRoIDMgdG8gOCBsZWdzLgpjcmVhdHVyZXMgPSBbbWFrZV9jcmVhdHVyZShudW1fbGVncz1udW1fbGVncykgZm9yIG51bV9sZWdzIGluICgzLDQsNSw2LDcsOCldCgojIFBsYWNlIHRoZW0gb24gYSBncmlkIGluIHRoZSBhcmVuYS4KaGVpZ2h0ID0gLjE1CmdyaWQgPSA1ICogQk9EWV9SQURJVVMKeHBvcywgeXBvcywgenBvcyA9IG5wLm1lc2hncmlkKFstZ3JpZCwgMCwgZ3JpZF0sIFswLCBncmlkXSwgW2hlaWdodF0pCmZvciBpLCBtb2RlbCBpbiBlbnVtZXJhdGUoY3JlYXR1cmVzKToKICAjIFBsYWNlIHNwYXduIHNpdGVzIG9uIGEgZ3JpZC4KICBzcGF3bl9wb3MgPSAoeHBvcy5mbGF0W2ldLCB5cG9zLmZsYXRbaV0sIHpwb3MuZmxhdFtpXSkKICBzcGF3bl9zaXRlID0gYXJlbmEud29ybGRib2R5LmFkZCgnc2l0ZScsIHBvcz1zcGF3bl9wb3MsIGdyb3VwPTMpCiAgIyBBdHRhY2ggdG8gdGhlIGFyZW5hIGF0IHRoZSBzcGF3biBzaXRlcywgd2l0aCBhIGZyZWUgam9pbnQuCiAgc3Bhd25fc2l0ZS5hdHRhY2gobW9kZWwpLmFkZCgnZnJlZWpvaW50JykKCiMgSW5zdGFudGlhdGUgdGhlIHBoeXNpY3MgYW5kIHJlbmRlci4KcGh5c2ljcyA9IG1qY2YuUGh5c2ljcy5mcm9tX21qY2ZfbW9kZWwoYXJlbmEpCnBpeGVscyA9IHBoeXNpY3MucmVuZGVyKCk=){download=""}

<!-- chunk {"id": "body-0110", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

creatures = \[make_creature(num_legs=num_legs) for num_legs in \]

<!-- chunk {"id": "body-0111", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Place them on a grid in the arena.

<!-- chunk {"id": "body-0112", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

xpos, ypos, zpos = np.meshgrid(\[-grid, 0, grid\], \[0, grid\], \[height\])

<!-- chunk {"id": "body-0113", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

spawn_pos = (xpos.flat\[i\], ypos.flat\[i\], zpos.flat\[i\])

<!-- chunk {"id": "body-0114", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

spawn_site = arena.worldbody.add('site', pos=spawn_pos, group=3)

<!-- chunk {"id": "body-0115", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Attach to the arena at the spawn sites, with a free joint.

<!-- chunk {"id": "body-0116", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

spawn_site.attach(model).add('freejoint')

<!-- chunk {"id": "body-0117", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Instantiate the physics and render.

<!-- chunk {"id": "body-0118", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

physics = mjcf.Physics.from_mjcf_model(arena)

<!-- chunk {"id": "body-0119", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=left,top, capbesidewidth=0.42]figure[\FBwidth]
Multi-legged creatures, ready to roam! Let us inject some controls and watch them move. We will generate a sinusoidal open-loop control signal of fixed frequency and random phase, recording both a video and the horizontal positions of the torso geoms, in order to plot the movement trajectories.

<!-- chunk {"id": "body-0120", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZHVyYXRpb24gID0gMTAgICMgKFNlY29uZHMpCmZyYW1lcmF0ZSA9IDMwICAjIChIeikKdmlkZW8gPSBbXTsgcG9zX3ggPSBbXTsgcG9zX3kgPSBbXQp0b3Jzb3MgPSBbXSAgIyBMaXN0IG9mIHRvcnNvIGdlb20gZWxlbWVudHMuCmFjdHVhdG9ycyA9IFtdICAjIExpc3Qgb2YgYWN0dWF0b3IgZWxlbWVudHMuCmZvciBjcmVhdHVyZSBpbiBjcmVhdHVyZXM6CiAgdG9yc29zLmFwcGVuZChjcmVhdHVyZS5maW5kKCdnZW9tJywndG9yc28nKSkKICBhY3R1YXRvcnMuZXh0ZW5kKGNyZWF0dXJlLmZpbmRfYWxsKCdhY3R1YXRvcicpKQoKIyBDb250cm9sIHNpZ25hbCBmcmVxdWVuY3ksIHBoYXNlLCBhbXBsaXR1ZGUuCmZyZXEgPSA1CnBoYXNlID0gMiAqIG5wLnBpICogbnAucmFuZG9tLnJhbmQobGVuKGFjdHVhdG9ycykpCmFtcCA9IDAuOQoKIyBTaW11bGF0ZSwgc2F2aW5nIHZpZGVvIGZyYW1lcyBhbmQgdG9yc28gbG9jYXRpb25zLgpwaHlzaWNzLnJlc2V0KCkKd2hpbGUgcGh5c2ljcy5kYXRhLnRpbWUgPCBkdXJhdGlvbjoKICAjIEluamVjdCBjb250cm9scyBhbmQgc3RlcCB0aGUgcGh5c2ljcy4KICBwaHlzaWNzLmJpbmQoYWN0dWF0b3JzKS5jdHJsID0gYW1wKm5wLnNpbihmcmVxKnBoeXNpY3MuZGF0YS50aW1lICsgcGhhc2UpCiAgcGh5c2ljcy5zdGVwKCkKCiAgIyBTYXZlIHRvcnNvIGhvcml6b250YWwgcG9zaXRpb25zIHVzaW5nIGJpbmQoKS4KICBwb3NfeC5hcHBlbmQocGh5c2ljcy5iaW5kKHRvcnNvcykueHBvc1s6LCAwXS5jb3B5KCkpCiAgcG9zX3kuYXBwZW5kKHBoeXNpY3MuYmluZCh0b3Jzb3MpLnhwb3NbOiwgMV0uY29weSgpKQoKICAjIFNhdmUgdmlkZW8gZnJhbWVzLgogIGlmIGxlbih2aWRlbykgPCBwaHlzaWNzLmRhdGEudGltZSAqIGZyYW1lcmF0ZToKICAgIHBpeGVscyA9IHBoeXNpY3MucmVuZGVyKCkKICAgIHZpZGVvLmFwcGVuZChwaXhlbHMuY29weSgpKQ==){download=""}

<!-- chunk {"id": "body-0121", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

torsos = \# List of torso geom elements.

<!-- chunk {"id": "body-0122", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

torsos.append(creature.find('geom','torso'))

<!-- chunk {"id": "body-0123", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

actuators.extend(creature.find_all('actuator'))

<!-- chunk {"id": "body-0124", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Control signal frequency, phase, amplitude.

<!-- chunk {"id": "body-0125", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

phase = 2 \* np.pi \* np.random.rand(len(actuators))

<!-- chunk {"id": "body-0126", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Simulate, saving video frames and torso locations.

<!-- chunk {"id": "body-0127", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Inject controls and step the physics.

<!-- chunk {"id": "body-0128", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

physics.bind(actuators).ctrl = amp\*np.sin(freq\*physics.data.time + phase)

<!-- chunk {"id": "body-0129", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

\# Save torso horizontal positions using bind.

<!-- chunk {"id": "body-0130", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

pos_x.append(physics.bind(torsos).xpos.copy)

<!-- chunk {"id": "body-0131", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

pos_y.append(physics.bind(torsos).xpos.copy)

<!-- chunk {"id": "body-0132", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

if len(video) \< physics.data.time

<!-- chunk {"id": "body-0133", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y3JlYXR1cmVfY29sb3JzID0gcGh5c2ljcy5iaW5kKHRvcnNvcykucmdiYVs6LCA6M10KZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSg4LCA4KSkKYXguc2V0X3Byb3BfY3ljbGUoY29sb3I9Y3JlYXR1cmVfY29sb3JzKQpheC5wbG90KHBvc194LCBwb3NfeSwgbGluZXdpZHRoPTQp){download=""}

<!-- chunk {"id": "body-0134", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

creature_colors = physics.bind(torsos).rgba

<!-- chunk {"id": "body-0135", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

ax.set_prop_cycle(color=creature_colors)

<!-- chunk {"id": "body-0136", "role": "body", "section": "PyMJCF Tutorial", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=left,top, capbesidewidth=0.57]figure[\FBwidth]
\href shows a clip of the locomotion. The plot on the right shows the corresponding movement trajectories of creature positions. Note how physics.bind(torsos) was used to access both xpos and rgba values. Once the Physics had been instantiated by from_mjcf_model, the bind method will expose both the associated mjData and mjModel fields of an mjcf element, providing unified access to all quantities in the simulation.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Debugging", "weight": 1.0} -->

In order to aid in troubleshooting MJCF compilation problems on models that are assembled programmatically, PyMJCF implements a debug mode where individual XML elements and attributes can be traced back to the line of Python code that last modified it. This feature is not enabled by default since the tracking mechanism is expensive to run. However when a compilation error is encountered the user is instructed to restart the program with the \--pymjcf_debug runtime flag. This flag causes PyMJCF to internally log the Python stack trace each time the model is modified. MuJoCo's error message is parsed to determine the line number in the generated XML document, which can be used to cross-reference to the XML element that is causing the error. The logged stack trace then allows PyMJCF to report the line of Python code that is likely to be responsible.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Debugging", "weight": 1.0} -->

Occasionally, the XML compilation error arises from incompatibility between attached models or broken cross-references. Such errors are not necessarily local to the line of code that last modified a particular element. For such a scenario, PyMJCF provides an additional \--pymjcf_debug_full_dump_dir flag that causes the entirety of the internal stack trace logs to be written to files at the specified directory.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Reinforcement learning interface", "weight": 1.0} -->

Reinforcement learning is a computational framework wherein an *agent*, through sequential interactions with an *environment*, tries to learn a behaviour policy that maximises future rewards.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Reinforcement Learning API", "weight": 1.0} -->

Environments in dm_control adhere to DeepMind's dm_env interface, defined in the \\href repository. In brief, a run-loop using dm_env may look like

<!-- chunk {"id": "body-0141", "role": "body", "section": "Reinforcement Learning API", "weight": 1.0} -->

[⬇](data:text/plain;base64,Zm9yIF8gaW4gcmFuZ2UobnVtX2VwaXNvZGVzKToKICB0aW1lc3RlcCA9IGVudi5yZXNldCgpCiAgd2hpbGUgVHJ1ZToKICAgIGFjdGlvbiA9IGFnZW50LnN0ZXAodGltZXN0ZXApCiAgICB0aW1lc3RlcCA9IGVudi5zdGVwKGFjdGlvbikKICAgIGlmIHRpbWVzdGVwLmxhc3QoKToKICAgICAgYWdlbnQuc3RlcCh0aW1lc3RlcCkKICAgICAgYnJlYWs=){download=""}

<!-- chunk {"id": "body-0142", "role": "body", "section": "Reinforcement Learning API", "weight": 1.0} -->

Each call to an environment's step method returns a TimeStep namedtuple with step_type, reward, discount and observation fields. Each episode starts with a step_type of FIRST, ends with a step_type of LAST, and has a step_type of MID for all intermediate timesteps. A TimeStep also has corresponding first, mid and last methods, as illustrated above. Please see the dm_env \\href documentation for more details.

<!-- chunk {"id": "body-0143", "role": "body", "section": "The Environment class", "weight": 1.0} -->

The class Environment, found within the dm_control.rl.control

<!-- chunk {"id": "body-0144", "role": "body", "section": "The Environment class", "weight": 1.0} -->

: Initialises the state, sampling from some initial state distribution.

<!-- chunk {"id": "body-0145", "role": "body", "section": "The Environment class", "weight": 1.0} -->

: Accepts an action, advances the simulation by one time-step, and returns a TimeStep namedtuple.

<!-- chunk {"id": "body-0146", "role": "body", "section": "The Environment class", "weight": 1.0} -->

: describes the actions accepted by an Environment. The method returns an ArraySpec, with attributes that describe the shape, data type, and optional lower and upper bounds for the action arrays. For example, random agent interaction can be implemented as

<!-- chunk {"id": "body-0147", "role": "body", "section": "The Environment class", "weight": 1.0} -->

[⬇](data:text/plain;base64,c3BlYyA9IGVudi5hY3Rpb25fc3BlYygpCnRpbWVfc3RlcCA9IGVudi5yZXNldCgpCndoaWxlIG5vdCB0aW1lX3N0ZXAubGFzdCgpOgogIGFjdGlvbiA9IG5wLnJhbmRvbS51bmlmb3JtKHNwZWMubWluaW11bSwgc3BlYy5tYXhpbXVtLCBzcGVjLnNoYXBlKQogIHRpbWVfc3RlcCA9IGVudi5zdGVwKGFjdGlvbik=){download=""}

<!-- chunk {"id": "body-0148", "role": "body", "section": "The Environment class", "weight": 1.0} -->

while not time_step.last:

<!-- chunk {"id": "body-0149", "role": "body", "section": "The Environment class", "weight": 1.0} -->

action = np.random.uniform(spec.minimum, spec.maximum, spec.shape)

<!-- chunk {"id": "body-0150", "role": "body", "section": "The Environment class", "weight": 1.0} -->

time_step = env.step(action)

<!-- chunk {"id": "body-0151", "role": "body", "section": "The Environment class", "weight": 1.0} -->

: returns an OrderedDict of ArraySpecs describing the shape and data type of each corresponding observation.

<!-- chunk {"id": "body-0152", "role": "body", "section": "The Environment class", "weight": 1.0} -->

step_type, an enum with a value in \[FIRST, MID, LAST\].

<!-- chunk {"id": "body-0153", "role": "body", "section": "The Environment class", "weight": 1.0} -->

reward, a floating point scalar, representing the reward from the previous transition.

<!-- chunk {"id": "body-0154", "role": "body", "section": "The Environment class", "weight": 1.0} -->

discount, a scalar floating point number $\gamma \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "The Environment class", "weight": 1.0} -->

observation, an OrderedDict of NumPy arrays matching the specification returned by observation_spec.

<!-- chunk {"id": "body-0156", "role": "body", "section": "The Environment class", "weight": 1.0} -->

Whereas the step_type specifies whether or not the episode is terminating, it is the discount $\gamma$ that determines the termination type. $\gamma = 0$ corresponds to a terminal state^22^2i.e. the sum of future reward is equal to the current reward. as in the first-exit or finite-horizon formulations. A terminal TimeStep with $\gamma = 1$ corresponds to the infinite-horizon formulation; in this case an agent interacting with the environment should treat the episode as if it could have continued indefinitely, even though the sequence of observations and rewards is truncated. In this case a parametric value function may be used to estimate future returns.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Reward functions", "weight": 1.0} -->

Rewards in dm_control tasks are in the unit interval, ${r{(\mathbf{s},\mathbf{a})}} \in {\lbrack 0,1\rbrack}$. Some tasks have "sparse" rewards, i.e., ${r{(\mathbf{s},\mathbf{a})}} \in {\{ 0,1\}}$. This structure is facilitated by the tolerance function, see Figure 3. Since terms output by tolerance are in the unit interval, both *averaging* and *multiplication* operations maintain that property, facilitating reward design.

<!-- chunk {"id": "body-0158", "role": "body", "section": "The Composer task definition library", "weight": 1.0} -->

The Composer framework organises RL environments into a common structure and endows scene elements with optional event handlers.

<!-- chunk {"id": "body-0159", "role": "body", "section": "The Composer task definition library", "weight": 1.0} -->

composer.Entity represents a reusable self-contained building block that consists of an MJCF model, observables (Section 5.1), and possibly callbacks executed at specific stages of the environment's life time, as detailed in Section 5.3. A collection of entities can be organised into a tree structure by attaching one or more child entities to a parent. The root entity is conventionally referred to as an "arena", and provides a fixed \<worldbody\> for the final, combined MJCF model.

<!-- chunk {"id": "body-0160", "role": "body", "section": "The Composer task definition library", "weight": 1.0} -->

composer.Task consists of a tree of composer.Entity objects that occupy the physical scene and provides reward, observation and termination methods. A task may also define callbacks to implement "game logic", e.g. to modify the scene in response to various events, and provide additional task observables.

<!-- chunk {"id": "body-0161", "role": "body", "section": "The Composer task definition library", "weight": 1.0} -->

composer.Environment wraps a composer.Task instance with an RL environment that agents can interact. It is responsible for compiling the MJCF model, triggering callbacks at appropriate points of an episode (see Section 5.3), and determining when to terminate, either through task-defined termination criteria or a user defined time limit. It also holds a random number generator state that is used by the callbacks, enabling reproducibility.

<!-- chunk {"id": "body-0162", "role": "body", "section": "The Composer task definition library", "weight": 1.0} -->

Section 5.1 describes observable, a Composer module for exposing observations, supporting noise, buffering and delays. Section 5.2 describes variation, a module for implementing model variations. Section 5.3 describes the callbacks used by Composer to implement these and additional user-defined behaviours. A self-contained Composer tutorial follows in Section 5.4

<!-- chunk {"id": "body-0163", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

An "observable" represents a quantity derived from the state of the simulation, that may be returned as an observation to the agent. Observables may be bound to a particular entity (e.g. sensors belonging to a robot), or they may be defined at the task level. The latter is often used for providing observations that relate to more than one entity in the scene (e.g. the distance between an end effector of a robot entity and a site on a different entity). A particular entity may define any number of observables (such as joint angles, pressure sensors, cameras), and it is up to the task designer to select which of these should appear in the agent's observations.

<!-- chunk {"id": "body-0164", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

enabled: (boolean) Whether the observable is computed and returned to the agent. Set to False by default.

<!-- chunk {"id": "body-0165", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

update_interval: (integer or callable returning an integer) Specifies the interval, in simulation steps, at which the values of the observable will be updated. The last value will be repeated between updates. This parameter may be used to simulate sensors with different sample rates. Sensors with stochastic rates may be modelled by passing a callable that returns a random integer.

<!-- chunk {"id": "body-0166", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

buffer_size: (integer) Controls the size of the internal FIFO buffer used to store observations that were sampled on previous simulation time-steps. In the default case where no aggregator is provided (see below), the entire contents of the buffer is returned as an observation at each control timestep. This can be used to avoid discarding observations from sensors whose values may change significantly within the control timestep. If the buffer size is sufficiently large, it will contain observations from previous control timesteps, endowing the environment with a simple form of memory.

<!-- chunk {"id": "body-0167", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

corruptor: (callable) Performs a point-wise transformation of each observation value before it is inserted into the buffer. Corruptors are most commonly used to simulate observation noise.

<!-- chunk {"id": "body-0168", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

aggregator: (callable or predefined string) Performs a reduction over all of the elements in the observation buffer. For example this can be used to take a moving average over previous observation values.

<!-- chunk {"id": "body-0169", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

delay: (integer or callable returning an integer) Specifies a delay (in terms of simulation timesteps) between when the value of the observable is sampled, and when it will appear in the observations returned by the environment. This parameter can be used to model sensor latency. Stochastic latencies may be modelled by passing a callable that returns a randomly sampled integer.

<!-- chunk {"id": "body-0170", "role": "body", "section": "The \\\\texorpdfstringobservableobservable module", "weight": 1.0} -->

During each control step the evaluation of observables is optimized such that only callables for observables that can appear in future observations are evaluated. For example, if we have an observable with update_interval=1 and buffer_size=1 then it will only be evaluated once per control step, even if there are multiple simulation steps per control step. This avoids the overhead of computing intermediate observations that would be discarded.

<!-- chunk {"id": "body-0171", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

To improve the realism of the simulation, it is often desirable to randomise elements of the environment, especially those whose values are uncertain. Stochasticity can be added to both the observables e.g. sensor noise (the corruptor of the previous section), as well as the model itself (a.k.a. "domain randomisation"). The latter is a popular method for increasing the robustness learned control policies. The variation module provides methods to add and configure forms of stochasticity in the Composer framework.

<!-- chunk {"id": "body-0172", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

Variation: The base class. Subclasses should implement the abstract method \_\_call\_\_(self, initial_value, current_value, random_state),\
which returns a numerical value, possibly depending on an initial_value (e.g. original geom mass) and current_value (e.g. previously sampled geom mass). Variation objects support arithmetic operations with numerical primitives and other Variation objects.

<!-- chunk {"id": "body-0173", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

MJCFVariator: A class for varying attributes of MJCF elements, e.g. geom size. The MJCFVariator keeps track of initial and current attribute values and passes them to the Variation object. It should be called in the initialize_episode_mjcf stage, before the model is compiled.

<!-- chunk {"id": "body-0174", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

PhysicsVariator: Similar to MJCFVariator, except for bound attributes, e.g. external forces. Should be called in the initialize_episode stage after the model has been compiled.

<!-- chunk {"id": "body-0175", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

evaluate: Method to traverse an arbitrarily nested structure of callables or constant values, and evaluate any callables (such as Variation objects).

<!-- chunk {"id": "body-0176", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

colors: Used to define variations in different colour spaces, such as RGB, HSV and grayscale.

<!-- chunk {"id": "body-0177", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

deterministic: Deterministic variations such as constant and fixed sequences of values, in case more control over the exact values is required.

<!-- chunk {"id": "body-0178", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

distributions: Wraps a number of distributions available in numpy.random as Variation objects. Any distribution parameters passed can themselves also be Variation objects.

<!-- chunk {"id": "body-0179", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

noises: Used to define additive and multiplicative noise using the distributions mentioned above, e.g. for modelling sensor noise.

<!-- chunk {"id": "body-0180", "role": "body", "section": "The \\\\texorpdfstringvariationvariation module", "weight": 1.0} -->

rotations: Useful for defining variations in quaternion space, e.g. random rotation on a composer.Entity's pose.

<!-- chunk {"id": "body-0181", "role": "body", "section": "The Composer callback lifecycle", "weight": 1.0} -->

The first of the two callbacks in reset is initialize_episode_mjcf, which allows the MJCF model to be modified between episodes. It is useful for changing quantities that are fixed once the model has been compiled. These modifications affect the generated XML which is then compiled into a Physics instance and passed to the initialize_episode callback, where the initial state can be set.

<!-- chunk {"id": "body-0182", "role": "body", "section": "The Composer callback lifecycle", "weight": 1.0} -->

The Environment.step sequence begins at the before_step callback. One key role of this callback is to translate agent actions into the Physics control vector.

<!-- chunk {"id": "body-0183", "role": "body", "section": "The Composer callback lifecycle", "weight": 1.0} -->

To guarantee stability, it is often necessary to reduce the time-step of the physics simulation. In order to decouple these possibly very small steps and the agent's control time-step, we introduce a substep loop. Each Physics substep is preceded by before_substep and followed by after_substep. These callbacks are useful for detecting transient events that may occur in the middle of an environment step, e.g. a button press. The internal observation buffers are then updated according to the configured update_interval of each individual Observable, unless the substep happens to be the last one in the environment step, in which case the after_step callback is called first before the final update of the observation buffers. The internal observation buffers are then processed according to the delay, buffer_size, and aggregator settings of each Observable to generate "output buffers" that are returned externally.

<!-- chunk {"id": "body-0184", "role": "body", "section": "The Composer callback lifecycle", "weight": 1.0} -->

At the end of each Environment.step, the Task's get_reward, get_discount, and should_terminate_episode callbacks are called in order to obtain the step's reward, discount, and termination status respectively. Usually, the these three are not entirely independent of each other, and it is therefore recommended to compute all of these in the after_step callback, cache the values in the Task instance, and return them in the respective callbacks.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

In this tutorial we will create a task requiring our "creature" from Section 3.1 to press a colour-changing button on the floor with a prescribed force. We begin by implementing our "creature" as a composer.Entity:

<!-- chunk {"id": "body-0186", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBjb21wb3Nlcgpmcm9tIGRtX2NvbnRyb2wuY29tcG9zZXIub2JzZXJ2YXRpb24gaW1wb3J0IG9ic2VydmFibGUKCmNsYXNzIENyZWF0dXJlKGNvbXBvc2VyLkVudGl0eSk6CiAgIiIiQSBtdWx0aS1sZWdnZWQgY3JlYXR1cmUgZGVyaXZlZCBmcm9tIGBjb21wb3Nlci5FbnRpdHlgLiIiIgogIGRlZiBfYnVpbGQoc2VsZiwgbnVtX2xlZ3MpOgogICAgc2VsZi5fbW9kZWwgPSBtYWtlX2NyZWF0dXJlKG51bV9sZWdzKQoKICBkZWYgX2J1aWxkX29ic2VydmFibGVzKHNlbGYpOgogICAgcmV0dXJuIENyZWF0dXJlT2JzZXJ2YWJsZXMoc2VsZikKCiAgQHByb3BlcnR5CiAgZGVmIG1qY2ZfbW9kZWwoc2VsZik6CiAgICByZXR1cm4gc2VsZi5fbW9kZWwKCiAgQHByb3BlcnR5CiAgZGVmIGFjdHVhdG9ycyhzZWxmKToKICAgIHJldHVybiB0dXBsZShzZWxmLl9tb2RlbC5maW5kX2FsbCgnYWN0dWF0b3InKSkKCmNsYXNzIENyZWF0dXJlT2JzZXJ2YWJsZXMoY29tcG9zZXIuT2JzZXJ2YWJsZXMpOgogICIiIkFkZCBzaW1wbGUgb2JzZXJ2YWJsZSBmZWF0dXJlcyBmb3Igam9pbnQgYW5nbGVzIGFuZCB2ZWxvY2l0aWVzLiIiIgogIEBjb21wb3Nlci5vYnNlcnZhYmxlCiAgZGVmIGpvaW50X3Bvc2l0aW9ucyhzZWxmKToKICAgIGFsbF9qb2ludHMgPSBzZWxmLl9lbnRpdHkubWpjZl9tb2RlbC5maW5kX2FsbCgnam9pbnQnKQogICAgcmV0dXJuIG9ic2VydmFibGUuTUpDRkZlYXR1cmUoJ3Fwb3MnLCBhbGxfam9pbnRzKQoKICBAY29tcG9zZXIub2JzZXJ2YWJsZQogIGRlZiBqb2ludF92ZWxvY2l0aWVzKHNlbGYpOgogICAgYWxsX2pvaW50cyA9IHNlbGYuX2VudGl0eS5tamNmX21vZGVsLmZpbmRfYWxsKCdqb2ludCcpCiAgICByZXR1cm4gb2JzZXJ2YWJsZS5NSkNGRmVhdHVyZSgncXZlbCcsIGFsbF9qb2ludHMp){download=""}

<!-- chunk {"id": "body-0187", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

from dm_control.composer.observation import observable

<!-- chunk {"id": "body-0188", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\"\"\"A multi-legged creature derived from 'composer.Entity'.\"\"\"

<!-- chunk {"id": "body-0189", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_model = make_creature(num_legs)

<!-- chunk {"id": "body-0190", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return tuple(self.\_model.find_all('actuator'))

<!-- chunk {"id": "body-0191", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\"\"\"Add simple observable features for joint angles and velocities.\"\"\"

<!-- chunk {"id": "body-0192", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

all_joints = self.\_entity.mjcf_model.find_all('joint')

<!-- chunk {"id": "body-0193", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return observable.MJCFFeature('qpos', all_joints)

<!-- chunk {"id": "body-0194", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

all_joints = self.\_entity.mjcf_model.find_all('joint')

<!-- chunk {"id": "body-0195", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return observable.MJCFFeature('qvel', all_joints)

<!-- chunk {"id": "body-0196", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

The Creature Entity includes generic Observables for joint angles and velocities. Because find_all is called on the Creature's MJCF model, it will only return the creature's leg joints, and not the "free" joint with which it will be attached to the world. Note that Composer Entities should override the \_build and \_build_observables methods rather than \_\_init\_\_. The implementation of \_\_init\_\_ in the base class calls \_build and \_build_observables, in that order, to ensure that the entity's MJCF model is created before its observables. This was a design choice which allows the user to refer to an observable as an attribute (entity.observables.foo) while still making it clear which attributes are observables. The stateful Button class derives from composer.Entity and implements the initialize_episode and after_substep callbacks.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,TlVNX1NVQlNURVBTID0gMjUgICMgVGhlIG51bWJlciBvZiBwaHlzaWNzIHN1YnN0ZXBzIHBlciBjb250cm9sIHRpbWVzdGVwLgpjbGFzcyBCdXR0b24oY29tcG9zZXIuRW50aXR5KToKICAiIiJBIGJ1dHRvbiBFbnRpdHkgd2hpY2ggY2hhbmdlcyBjb2xvdXIgd2hlbiBwcmVzc2VkIHdpdGggY2VydGFpbiBmb3JjZS4iIiIKICBkZWYgX2J1aWxkKHNlbGYsIHRhcmdldF9mb3JjZV9yYW5nZT0oNSwgMTApKToKICAgIHNlbGYuX21pbl9mb3JjZSwgc2VsZi5fbWF4X2ZvcmNlID0gdGFyZ2V0X2ZvcmNlX3JhbmdlCiAgICBzZWxmLl9tamNmX21vZGVsID0gbWpjZi5Sb290RWxlbWVudCgpCiAgICBzZWxmLl9nZW9tID0gc2VsZi5fbWpjZl9tb2RlbC53b3JsZGJvZHkuYWRkKAogICAgICAgICdnZW9tJywgdHlwZT0nY3lsaW5kZXInLCBzaXplPVswLjI1LCAwLjAyXSwgcmdiYT1bMSwgMCwgMCwgMV0pCiAgICBzZWxmLl9zaXRlID0gc2VsZi5fbWpjZl9tb2RlbC53b3JsZGJvZHkuYWRkKAogICAgICAgICdzaXRlJywgdHlwZT0nY3lsaW5kZXInLCBzaXplPXNlbGYuX2dlb20uc2l6ZSoxLjAxLCByZ2JhPVsxLCAwLCAwLCAwXSkKICAgIHNlbGYuX3NlbnNvciA9IHNlbGYuX21qY2ZfbW9kZWwuc2Vuc29yLmFkZCgndG91Y2gnLCBzaXRlPXNlbGYuX3NpdGUpCiAgICBzZWxmLl9udW1fYWN0aXZhdGVkX3N0ZXBzID0gMAoKICBkZWYgX2J1aWxkX29ic2VydmFibGVzKHNlbGYpOgogICAgcmV0dXJuIEJ1dHRvbk9ic2VydmFibGVzKHNlbGYpCgogIEBwcm9wZXJ0eQogIGRlZiBtamNmX21vZGVsKHNlbGYpOgogICAgcmV0dXJuIHNlbGYuX21qY2ZfbW9kZWwKICBkZWYgX3VwZGF0ZV9hY3RpdmF0aW9uKHNlbGYsIHBoeXNpY3MpOgogICAgIiIiVXBkYXRlIHRoZSBhY3RpdmF0aW9uIGFuZCBjb2xvdXIgaWYgdGhlIGRlc2lyZWQgZm9yY2UgaXMgYXBwbGllZC4iIiIKICAgIGN1cnJlbnRfZm9yY2UgPSBwaHlzaWNzLmJpbmQoc2VsZi50b3VjaF9zZW5zb3IpLnNlbnNvcmRhdGFbMF0KICAgIGlzX2FjdGl2YXRlZCA9IChjdXJyZW50X2ZvcmNlID49IHNlbGYuX21pbl9mb3JjZSBhbmQKICAgICAgICAgICAgICAgICAgICBjdXJyZW50X2ZvcmNlIDw9IHNlbGYuX21heF9mb3JjZSkKICAgIHJlZCA9IFsxLCAwLCAwLCAxXQogICAgZ3JlZW4gPSBbMCwgMSwgMCwgMV0KICAgIHBoeXNpY3MuYmluZChzZWxmLl9nZW9tKS5yZ2JhID0gZ3JlZW4gaWYgaXNfYWN0aXZhdGVkIGVsc2UgcmVkCiAgICBzZWxmLl9udW1fYWN0aXZhdGVkX3N0ZXBzICs9IGludChpc19hY3RpdmF0ZWQpCgogIGRlZiBpbml0aWFsaXplX2VwaXNvZGUoc2VsZiwgcGh5c2ljcywgcmFuZG9tX3N0YXRlKToKICAgIHNlbGYuX3Jld2FyZCA9IDAuMAogICAgc2VsZi5fbnVtX2FjdGl2YXRlZF9zdGVwcyA9IDAKICAgIHNlbGYuX3VwZGF0ZV9hY3RpdmF0aW9uKHBoeXNpY3MpCgogIGRlZiBhZnRlcl9zdWJzdGVwKHNlbGYsIHBoeXNpY3MsIHJhbmRvbV9zdGF0ZSk6C

<!-- chunk {"id": "body-0198", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

iAgICBzZWxmLl91cGRhdGVfYWN0aXZhdGlvbihwaHlzaWNzKQoKICBAcHJvcGVydHkKICBkZWYgdG91Y2hfc2Vuc29yKHNlbGYpOgogICAgcmV0dXJuIHNlbGYuX3NlbnNvcgoKICBAcHJvcGVydHkKICBkZWYgbnVtX2FjdGl2YXRlZF9zdGVwcyhzZWxmKToKICAgIHJldHVybiBzZWxmLl9udW1fYWN0aXZhdGVkX3N0ZXBzCgpjbGFzcyBCdXR0b25PYnNlcnZhYmxlcyhjb21wb3Nlci5PYnNlcnZhYmxlcyk6CiAgIiIiQSB0b3VjaCBzZW5zb3Igd2hpY2ggYXZlcmFnZXMgY29udGFjdCBmb3JjZSBvdmVyIHBoeXNpY3Mgc3Vic3RlcHMuIiIiCiAgQGNvbXBvc2VyLm9ic2VydmFibGUKICBkZWYgdG91Y2hfZm9yY2Uoc2VsZik6CiAgICByZXR1cm4gb2JzZXJ2YWJsZS5NSkNGRmVhdHVyZSgnc2Vuc29yZGF0YScsIHNlbGYuX2VudGl0eS50b3VjaF9zZW5zb3IsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBidWZmZXJfc2l6ZT1OVU1fU1VCU1RFUFMsIGFnZ3JlZ2F0b3I9J21lYW4nKQ==){download=""}

<!-- chunk {"id": "body-0199", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

NUM_SUBSTEPS = 25 \# The number of physics substeps per control timestep.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\"\"\"A button Entity which changes colour when pressed with certain force.\"\"\"

<!-- chunk {"id": "body-0201", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_min_force, self.\_max_force = target_force_range

<!-- chunk {"id": "body-0202", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_mjcf_model = mjcf.RootElement

<!-- chunk {"id": "body-0203", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_geom = self.\_mjcf_model.worldbody.add(

<!-- chunk {"id": "body-0204", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

'geom', type='cylinder', size=\[0.25, 0.02\], rgba=)

<!-- chunk {"id": "body-0205", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_site = self.\_mjcf_model.worldbody.add(

<!-- chunk {"id": "body-0206", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

'site', type='cylinder', size=self.\_geom.size\*1.01, rgba=)

<!-- chunk {"id": "body-0207", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_sensor = self.\_mjcf_model.sensor.add('touch', site=self.\_site)

<!-- chunk {"id": "body-0208", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\"\"\"Update the activation and colour if the desired force is applied.\"\"\"

<!-- chunk {"id": "body-0209", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

current_force = physics.bind(self.touch_sensor).sensordata

<!-- chunk {"id": "body-0210", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

is_activated = (current_force \>= self.\_min_force and

<!-- chunk {"id": "body-0211", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

current_force \<= self.\_max_force)

<!-- chunk {"id": "body-0212", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

physics.bind(self.\_geom).rgba = green if is_activated else red

<!-- chunk {"id": "body-0213", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_num_activated_steps += int(is_activated)

<!-- chunk {"id": "body-0214", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return self.\_num_activated_steps

<!-- chunk {"id": "body-0215", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\"\"\"A touch sensor which averages contact force over physics substeps.\"\"\"

<!-- chunk {"id": "body-0216", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return observable.MJCFFeature('sensordata', self.\_entity.touch_sensor,

<!-- chunk {"id": "body-0217", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

buffer_size=NUM_SUBSTEPS, aggregator='mean')

<!-- chunk {"id": "body-0218", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

Note how the Button counts the number of sub-steps during which it is pressed with the desired force. It also exposes an Observable of the force being applied to the button, whose value is an average of the readings over the physics time-steps.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLmNvbXBvc2VyIGltcG9ydCB2YXJpYXRpb24KZnJvbSBkbV9jb250cm9sLmNvbXBvc2VyLnZhcmlhdGlvbiBpbXBvcnQgZGlzdHJpYnV0aW9ucwpmcm9tIGRtX2NvbnRyb2wuY29tcG9zZXIudmFyaWF0aW9uIGltcG9ydCBub2lzZXMKZnJvbSBkbV9jb250cm9sLmxvY29tb3Rpb24uYXJlbmFzIGltcG9ydCBmbG9vcnM=){download=""}

<!-- chunk {"id": "body-0220", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

from dm_control.composer import variation

<!-- chunk {"id": "body-0221", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

from dm_control.composer.variation import distributions

<!-- chunk {"id": "body-0222", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

from dm_control.composer.variation import noises

<!-- chunk {"id": "body-0223", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

from dm_control.locomotion.arenas import floors

<!-- chunk {"id": "body-0224", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y2xhc3MgVW5pZm9ybUNpcmNsZSh2YXJpYXRpb24uVmFyaWF0aW9uKToKICAiIiIgQSB1bmlmb3JtbHkgc2FtcGxlZCBob3Jpem9udGFsIHBvaW50IG9uIGEgY2lyY2xlIG9mIHJhZGl1cyBgZGlzdGFuY2VgIiIiCiAgZGVmIF9faW5pdF9fKHNlbGYsIGRpc3RhbmNlKToKICAgIHNlbGYuX2Rpc3RhbmNlID0gZGlzdGFuY2UKICAgIHNlbGYuX2hlYWRpbmcgPSBkaXN0cmlidXRpb25zLlVuaWZvcm0oMCwgMipucC5waSkKCiAgZGVmIF9fY2FsbF9fKHNlbGYsIGluaXRpYWxfdmFsdWU9Tm9uZSwKICAgICAgICAgICAgICAgY3VycmVudF92YWx1ZT1Ob25lLCByYW5kb21fc3RhdGU9Tm9uZSk6CiAgICBkaXN0YW5jZSwgaGVhZGluZyA9IHZhcmlhdGlvbi5ldmFsdWF0ZSgKICAgICAgICAoc2VsZi5fZGlzdGFuY2UsIHNlbGYuX2hlYWRpbmcpLCByYW5kb21fc3RhdGU9cmFuZG9tX3N0YXRlKQogICAgcmV0dXJuIChkaXN0YW5jZSpucC5jb3MoaGVhZGluZyksIGRpc3RhbmNlKm5wLnNpbihoZWFkaW5nKSwgMCk=){download=""}

<!-- chunk {"id": "body-0225", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\"\"\" A uniformly sampled horizontal point on a circle of radius 'distance'\"\"\"

<!-- chunk {"id": "body-0226", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

(self.\_distance, self.\_heading), random_state=random_state)

<!-- chunk {"id": "body-0227", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return (distance\*np.cos(heading), distance\*np.sin(heading), 0)

<!-- chunk {"id": "body-0228", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

We will now define the PressWithSpecificForce Task, which combines all the above elements.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y2xhc3MgUHJlc3NXaXRoU3BlY2lmaWNGb3JjZShjb21wb3Nlci5UYXNrKToKCiAgZGVmIF9faW5pdF9fKHNlbGYsIGNyZWF0dXJlKToKICAgIHNlbGYuX2NyZWF0dXJlID0gY3JlYXR1cmUKICAgIHNlbGYuX2FyZW5hID0gZmxvb3JzLkZsb29yKCkKICAgIHNlbGYuX2FyZW5hLmFkZF9mcmVlX2VudGl0eShzZWxmLl9jcmVhdHVyZSkKICAgIHNlbGYuX2FyZW5hLm1qY2ZfbW9kZWwud29ybGRib2R5LmFkZCgnbGlnaHQnLCBwb3M9KDAsIDAsIDQpKQogICAgc2VsZi5fYnV0dG9uID0gQnV0dG9uKCkKICAgIHNlbGYuX2FyZW5hLmF0dGFjaChzZWxmLl9idXR0b24pCgogICAgIyBDb25maWd1cmUgaW5pdGlhbCBwb3NlcwogICAgc2VsZi5fY3JlYXR1cmVfaW5pdGlhbF9wb3NlID0gKDAsIDAsIDAuMTUpCiAgICBidXR0b25fZGlzdGFuY2UgPSBkaXN0cmlidXRpb25zLlVuaWZvcm0oMC41LCAuNzUpCiAgICBzZWxmLl9idXR0b25faW5pdGlhbF9wb3NlID0gVW5pZm9ybUNpcmNsZShidXR0b25fZGlzdGFuY2UpCgogICAgIyBDb25maWd1cmUgdmFyaWF0b3JzCiAgICBzZWxmLl9tamNmX3ZhcmlhdG9yID0gdmFyaWF0aW9uLk1KQ0ZWYXJpYXRvcigpCiAgICBzZWxmLl9waHlzaWNzX3ZhcmlhdG9yID0gdmFyaWF0aW9uLlBoeXNpY3NWYXJpYXRvcigpCgogICAgIyBDb25maWd1cmUgYW5kIGVuYWJsZSBvYnNlcnZhYmxlcwogICAgcG9zX2NvcnJ1cHRvciA9IG5vaXNlcy5BZGRpdGl2ZShkaXN0cmlidXRpb25zLk5vcm1hbChzY2FsZT0wLjAxKSkKICAgIHNlbGYuX2NyZWF0dXJlLm9ic2VydmFibGVzLmpvaW50X3Bvc2l0aW9ucy5jb3JydXB0b3IgPSBwb3NfY29ycnVwdG9yCiAgICBzZWxmLl9jcmVhdHVyZS5vYnNlcnZhYmxlcy5qb2ludF9wb3NpdGlvbnMuZW5hYmxlZCA9IFRydWUKICAgIHZlbF9jb3JydXB0b3IgPSBub2lzZXMuTXVsdGlwbGljYXRpdmUoZGlzdHJpYnV0aW9ucy5Mb2dOb3JtYWwoc2lnbWE9MC4wMSkpCiAgICBzZWxmLl9jcmVhdHVyZS5vYnNlcnZhYmxlcy5qb2ludF92ZWxvY2l0aWVzLmNvcnJ1cHRvciA9IHZlbF9jb3JydXB0b3IKICAgIHNlbGYuX2NyZWF0dXJlLm9ic2VydmFibGVzLmpvaW50X3ZlbG9jaXRpZXMuZW5hYmxlZCA9IFRydWUKICAgIHNlbGYuX2J1dHRvbi5vYnNlcnZhYmxlcy50b3VjaF9mb3JjZS5lbmFibGVkID0gVHJ1ZQoKICAgICMgQWRkIGJ1dHRvbiBwb3NpdGlvbiBvYnNlcnZhYmxlIGluIHRoZSBDcmVhdHVyZSdzIGVnb2NlbnRyaWMgZnJhbWUKICAgIHNlbGYuX3Rhc2tfb2JzZXJ2YWJsZXMgPSB7fQogICAgZGVmIHRvX2J1dHRvbihwaHlzaWNzKToKICAgICAgYnV0dG9uX3BvcywgXyA9IHNlbGYuX2J1dHRvbi5nZXRfcG9zZShwaHlzaWNzKQogICAgICByZXR1cm4gc2VsZi5fY3JlYXR1cmUuZ2xvYmFsX3ZlY3Rvcl90b19sb2NhbF9mcmFtZShwaHlzaWNzLCBidXR0b25fcG9zKQogICAgc2VsZi5fdGFza19vYnNlcnZhYmxlc1snYnV0dG9uX3Bvc2l0aW9uJ10gPSBvY

<!-- chunk {"id": "body-0230", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

nNlcnZhYmxlLkdlbmVyaWModG9fYnV0dG9uKQogICAgZm9yIG9icyBpbiBzZWxmLl90YXNrX29ic2VydmFibGVzLnZhbHVlcygpOgogICAgICBvYnMuZW5hYmxlZCA9IFRydWUgICMgRW5hYmxlIGFsbCBvYnNlcnZhYmxlcy4KCiAgICBzZWxmLmNvbnRyb2xfdGltZXN0ZXAgPSBOVU1fU1VCU1RFUFMgKiBzZWxmLnBoeXNpY3NfdGltZXN0ZXAKIyBDb250aW51ZWQgYmVsb3cuLi4=){download=""}

<!-- chunk {"id": "body-0231", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_arena.add_free_entity(self.\_creature)

<!-- chunk {"id": "body-0232", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_arena.mjcf_model.worldbody.add('light', pos=)

<!-- chunk {"id": "body-0233", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_arena.attach(self.\_button)

<!-- chunk {"id": "body-0234", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_button_initial_pose = UniformCircle(button_distance)

<!-- chunk {"id": "body-0235", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_mjcf_variator = variation.MJCFVariator

<!-- chunk {"id": "body-0236", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_physics_variator = variation.PhysicsVariator

<!-- chunk {"id": "body-0237", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

pos_corruptor = noises.Additive(distributions.Normal(scale=0.01))

<!-- chunk {"id": "body-0238", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_creature.observables.joint_positions.corruptor = pos_corruptor

<!-- chunk {"id": "body-0239", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_creature.observables.joint_positions.enabled = True

<!-- chunk {"id": "body-0240", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

vel_corruptor = noises.Multiplicative(distributions.LogNormal(sigma=0.01))

<!-- chunk {"id": "body-0241", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_creature.observables.joint_velocities.corruptor = vel_corruptor

<!-- chunk {"id": "body-0242", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_creature.observables.joint_velocities.enabled = True

<!-- chunk {"id": "body-0243", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_button.observables.touch_force.enabled = True

<!-- chunk {"id": "body-0244", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

\# Add button position observable in the Creature's egocentric frame

<!-- chunk {"id": "body-0245", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

button_pos, \_ = self.\_button.get_pose(physics)

<!-- chunk {"id": "body-0246", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return self.\_creature.global_vector_to_local_frame(physics, button_pos)

<!-- chunk {"id": "body-0247", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_task_observables\['button_position'\] = observable.Generic(to_button)

<!-- chunk {"id": "body-0248", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

for obs in self.\_task_observables.values:

<!-- chunk {"id": "body-0249", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

obs.enabled = True \# Enable all observables.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.control_timestep = NUM_SUBSTEPS \* self.physics_timestep

<!-- chunk {"id": "body-0251", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,IyBDb250aW51ZWQgZnJvbSBhYm92ZS4uLgogIEBwcm9wZXJ0eQogIGRlZiByb290X2VudGl0eShzZWxmKToKICAgIHJldHVybiBzZWxmLl9hcmVuYQoKICBAcHJvcGVydHkKICBkZWYgdGFza19vYnNlcnZhYmxlcyhzZWxmKToKICAgIHJldHVybiBzZWxmLl90YXNrX29ic2VydmFibGVzCgogIGRlZiBpbml0aWFsaXplX2VwaXNvZGVfbWpjZihzZWxmLCByYW5kb21fc3RhdGUpOgogICAgc2VsZi5fbWpjZl92YXJpYXRvci5hcHBseV92YXJpYXRpb25zKHJhbmRvbV9zdGF0ZSkKCiAgZGVmIGluaXRpYWxpemVfZXBpc29kZShzZWxmLCBwaHlzaWNzLCByYW5kb21fc3RhdGUpOgogICAgc2VsZi5fcGh5c2ljc192YXJpYXRvci5hcHBseV92YXJpYXRpb25zKHBoeXNpY3MsIHJhbmRvbV9zdGF0ZSkKICAgIGNyZWF0dXJlX3Bvc2UsIGJ1dHRvbl9wb3NlID0gdmFyaWF0aW9uLmV2YWx1YXRlKAogICAgICAgIChzZWxmLl9jcmVhdHVyZV9pbml0aWFsX3Bvc2UsIHNlbGYuX2J1dHRvbl9pbml0aWFsX3Bvc2UpLAogICAgICAgIHJhbmRvbV9zdGF0ZT1yYW5kb21fc3RhdGUpCiAgICBzZWxmLl9jcmVhdHVyZS5zZXRfcG9zZShwaHlzaWNzLCBwb3NpdGlvbj1jcmVhdHVyZV9wb3NlKQogICAgc2VsZi5fYnV0dG9uLnNldF9wb3NlKHBoeXNpY3MsIHBvc2l0aW9uPWJ1dHRvbl9wb3NlKQoKICBkZWYgZ2V0X3Jld2FyZChzZWxmLCBwaHlzaWNzKToKICAgIHJldHVybiBzZWxmLl9idXR0b24ubnVtX2FjdGl2YXRlZF9zdGVwcyAvIE5VTV9TVUJTVEVQUw==){download=""}

<!-- chunk {"id": "body-0252", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_mjcf_variator.apply_variations(random_state)

<!-- chunk {"id": "body-0253", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_physics_variator.apply_variations(physics, random_state)

<!-- chunk {"id": "body-0254", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

creature_pose, button_pose = variation.evaluate(

<!-- chunk {"id": "body-0255", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

(self.\_creature_initial_pose, self.\_button_initial_pose),

<!-- chunk {"id": "body-0256", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_creature.set_pose(physics, position=creature_pose)

<!-- chunk {"id": "body-0257", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

self.\_button.set_pose(physics, position=button_pose)

<!-- chunk {"id": "body-0258", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

return self.\_button.num_activated_steps / NUM_SUBSTEPS

<!-- chunk {"id": "body-0259", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

Finally, we can instantiate a Creature Entity,

<!-- chunk {"id": "body-0260", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y3JlYXR1cmUgPSBDcmVhdHVyZShudW1fbGVncz00KQ==){download=""}

<!-- chunk {"id": "body-0261", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

pass it to the PressWithSpecificForce constructor to instantiate the task,

<!-- chunk {"id": "body-0262", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,dGFzayA9IFByZXNzV2l0aFNwZWNpZmljRm9yY2UoY3JlYXR1cmUp){download=""}

<!-- chunk {"id": "body-0263", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

and expose it as an environment complying with the dm_env.Environment

<!-- chunk {"id": "body-0264", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZW52ID0gY29tcG9zZXIuRW52aXJvbm1lbnQodGFzayk=){download=""}

<!-- chunk {"id": "body-0265", "role": "body", "section": "Composer tutorial", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=left,top, capbesidewidth=0.57]figure[\FBwidth]
Here is our creature with a large red button, waiting to be pressed.

<!-- chunk {"id": "body-0266", "role": "body", "section": "The Control Suite", "weight": 1.0} -->

The Control Suite is a set of stable, well-tested tasks designed to serve as a benchmark for continuous control learning agents. Tasks are written using the basic MuJoCo interface of Section 2. Standardised action, observation and reward structures make suite-wide benchmarking simple and learning curves easy to interpret. Unlike the more elaborate domains of the Sections 7 and 8, Control Suite domains are not meant to be modified, in order to facilitate benchmarking. For more details regarding benchmarking, refer to our original publication. A video montage of Control Suite domains can be found at \\href

<!-- chunk {"id": "body-0267", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

: With the exception of the LQR domain (see below), the action vector is in the unit box, i.e., $\mathbf{a} \in \mathcal{A} \equiv \left\lbrack {- 1},1 \right\rbrack^{\dim{(\mathcal{A})}}$.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

: While the state notionally evolves according to a continuous ordinary differential equation $\overset{˙}{\mathbf{s}} = {\mathbf{f}_{c}{(\mathbf{s},\mathbf{a})}}$, in practice temporal integration is discrete^33^3Most domains use MuJoCo's default semi-implicit Euler integrator. A few domains which have smooth dynamics use 4th-order Runge Kutta. with some fixed, finite time-step: $\mathbf{s}_{t + h} = {\mathbf{f}{(\mathbf{s}_{t},\mathbf{a}_{t})}}$.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

: When using the default observations (rather than pixels, see below), all tasks^44^4With the exception of point-mass:hard (see below). are strongly observable, i.e. the state can be recovered from a single observation. Observation features which depend only on the state (position and velocity) are functions of the current state. Features which are also dependent on controls (e.g. touch sensor readings) are functions of the previous transition.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

: Rewards in the Control Suite, with the exception of the LQR domain, are in the unit interval, i.e., ${r{(\mathbf{s},\mathbf{a})}} \in {\lbrack 0,1\rbrack}$. Some rewards are "sparse", i.e., ${r{(\mathbf{s},\mathbf{a})}} \in {\{ 0,1\}}$. This structure is facilitated by the tolerance function, see Figure 3.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

: Control problems are usually classified as finite-horizon, first-exit and infinite-horizon. Control Suite tasks have no terminal states or time limit and are therefore of the infinite-horizon variety.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

In the limit $\tau\rightarrow\infty$ (equivalently $\gamma\rightarrow 1$), the policies of the discounted-horizon and average-return formulations are identical. All Control Suite tasks with the exception of LQR^55^5The LQR task terminates with $\gamma = 0$ when the state is very close to the origin, as a proxy for the exponential convergence of stabilised linear systems. return $\gamma = 1$ at every step, including on termination.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Control Suite design conventions", "weight": 1.0} -->

: While agents are expected to optimise for infinite-horizon returns, these are difficult to measure. As a proxy we use fixed-length episodes of 1000 time steps. Since all reward functions are designed so that $r \approx 1$ near goal states, learning curves measuring total returns can all have the same y-axis limits of $\lbrack 0,1000\rbrack$, making them easier to interpret and to average over all tasks. While a perfect score of 1000 is not usually achievable, scores outside the $\lbrack 800,1000\rbrack$ range can be confidently said to be sub-optimal.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Model and Task verification", "weight": 1.0} -->

Simulated physics can easily destabilise and diverge, mostly due to errors introduced by time discretisation. Smaller time-steps are more stable, but require more computation per unit of simulation time, so the choice of time-step is always a trade-off between stability and speed. What's more, learning agents are very good at discovering and exploiting instabilities.^66^6This phenomenon, known as Sims' Law, was first articulated: "Any bugs that allow energy leaks from non-conservation, or even round-off errors, will inevitably be discovered and exploited".

<!-- chunk {"id": "body-0275", "role": "body", "section": "Model and Task verification", "weight": 1.0} -->

It is surprisingly easy to write tasks that are much easier or harder than intended, that are impossible to solve or that can be solved by very different strategies than expected (i.e. "cheats"). To prevent these situations, the Atari™ games that make up ALE were extensively tested over more than 10 man-years^77^7Marc Bellemare, personal communication.. However, many continuous control domains cannot be solved by humans with standard input devices, due to the large action space, so a different approach must be taken.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Model and Task verification", "weight": 1.0} -->

In order to tackle both of these challenges, we ran variety of learning agents against all tasks, and iterated on each task's design until we were satisfied that the physics was stable and non-exploitable, and that the task is solved correctly by at least one agent. Tasks that were solvable were collated into the benchmarking set. Tasks which were not yet solved at the time of development are in the extra set of tasks.

<!-- chunk {"id": "body-0277", "role": "body", "section": "The suite module", "weight": 1.0} -->

To load an environment representing a task from the suite, use suite.load:

<!-- chunk {"id": "body-0278", "role": "body", "section": "The suite module", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBzdWl0ZQoKIyBMb2FkIG9uZSB0YXNrOgplbnYgPSBzdWl0ZS5sb2FkKGRvbWFpbl9uYW1lPSJjYXJ0cG9sZSIsIHRhc2tfbmFtZT0ic3dpbmd1cCIpCgojIEl0ZXJhdGUgb3ZlciBhIHRhc2sgc2V0Ogpmb3IgZG9tYWluX25hbWUsIHRhc2tfbmFtZSBpbiBzdWl0ZS5CRU5DSE1BUktJTkc6CiAgZW52ID0gc3VpdGUubG9hZChkb21haW5fbmFtZSwgdGFza19uYW1lKQogIC4uLg==){download=""}

<!-- chunk {"id": "body-0279", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(domain_name=\"cartpole\", task_name=\"swingup\")

<!-- chunk {"id": "body-0280", "role": "body", "section": "The suite module", "weight": 1.0} -->

for domain_name, task_name in suite.BENCHMARKING:

<!-- chunk {"id": "body-0281", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(domain_name, task_name)

<!-- chunk {"id": "body-0282", "role": "body", "section": "The suite module", "weight": 1.0} -->

: Pixel observations: By default, Control Suite environments return feature observations. The pixel.Wrapper adds or replaces these with images.

<!-- chunk {"id": "body-0283", "role": "body", "section": "The suite module", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLnN1aXRlLndyYXBwZXJzIGltcG9ydCBwaXhlbHMKZW52ID0gc3VpdGUubG9hZCgiY2FydHBvbGUiLCAic3dpbmd1cCIpCiMgUmVwbGFjZSBleGlzdGluZyBmZWF0dXJlcyBieSBwaXhlbCBvYnNlcnZhdGlvbnM6CmVudl9vbmx5X3BpeGVscyA9IHBpeGVscy5XcmFwcGVyKGVudikKIyBQaXhlbCBvYnNlcnZhdGlvbnMgaW4gYWRkaXRpb24gdG8gZXhpc3RpbmcgZmVhdHVyZXMuCmVudl9wbHVzX3BpeGVscyA9IHBpeGVscy5XcmFwcGVyKGVudiwgcGl4ZWxzX29ubHk9RmFsc2Up){download=""}

<!-- chunk {"id": "body-0284", "role": "body", "section": "The suite module", "weight": 1.0} -->

from dm_control.suite.wrappers import pixels

<!-- chunk {"id": "body-0285", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(\"cartpole\", \"swingup\")

<!-- chunk {"id": "body-0286", "role": "body", "section": "The suite module", "weight": 1.0} -->

env_only_pixels = pixels.Wrapper(env)

<!-- chunk {"id": "body-0287", "role": "body", "section": "The suite module", "weight": 1.0} -->

\# Pixel observations in addition to existing features.

<!-- chunk {"id": "body-0288", "role": "body", "section": "The suite module", "weight": 1.0} -->

env_plus_pixels = pixels.Wrapper(env, pixels_only=False)

<!-- chunk {"id": "body-0289", "role": "body", "section": "The suite module", "weight": 1.0} -->

: Reward visualisation: Models in the Control Suite use a common set of colours and textures for visual uniformity. As illustrated in the \\href this also allows us to modify colours in proportion to the reward, providing a convenient visual cue.

<!-- chunk {"id": "body-0290", "role": "body", "section": "The suite module", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZW52ID0gc3VpdGUubG9hZCgiZmlzaCIsICJzd2ltIiwgdGFza19rd2FyZ3MsIHZpc3VhbGl6ZV9yZXdhcmQ9VHJ1ZSk=){download=""}

<!-- chunk {"id": "body-0291", "role": "body", "section": "The suite module", "weight": 1.0} -->

env = suite.load(\"fish\", \"swim\", task_kwargs, visualize_reward=True)

<!-- chunk {"id": "body-0292", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

A domain refers to a physical model, while a task refers to an instance of that model with a particular MDP structure. For example the difference between the swingup and balance tasks of the cartpole domain is whether the pole is initialised pointing downwards or upwards, respectively. In some cases, e.g. when the model is procedurally generated, different tasks might have different physical properties. Tasks in the Control Suite are collated into tuples according to predefined tags. Tasks used for benchmarking are in the BENCHMARKING tuple (Figure 1), while those not used for benchmarking (because they are particularly difficult, or because they do not conform to the standard structure) are in the EXTRA tuple. All suite tasks are accessible via the ALL_TASKS tuple. In the domain descriptions below, names are followed by three integers specifying the dimensions of the state, control and observation spaces: $\text{Name~}\left( {\dim{(\mathcal{S})}},{\dim{(\mathcal{A})}},{\dim{(\mathcal{O})}} \right)$.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Pendulum: The classic inverted pendulum. The torque-limited actuator is 1/6th as strong as required to lift the mass from motionless horizontal, necessitating several swings to swing up and balance. The swingup task has a simple sparse reward: 1 when the pole is within 30∘ of the vertical position and 0 otherwise.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Acrobot: The underactuated double pendulum, torque applied to the second joint. The goal is to swing up and balance. Despite being low-dimensional, this is not an easy control problem. The physical model conforms to rather than the earlier Spong 1995. The swingup and swingup_sparse tasks have smooth and sparse rewards, respectively.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Cart-pole: Swing up and balance an unactuated pole by applying forces to a cart at its base. The physical model conforms to Barto et al. 1983. Four benchmarking tasks: in swingup and swingup_sparse the pole starts pointing down while in balance and balance_sparse the pole starts near the upright position.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.585]figure[\FBwidth]
Cart-k-pole (2 k + 2, 1, 3 k + 2): The cart-pole domain allows to procedurally adding more poles, connected serially. Two non-benchmarking tasks, two_poles and three_poles are available.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Ball in cup: A planar ball-in-cup task. An actuated planar receptacle can translate in the vertical plane in order to swing and catch a ball attached to its bottom. The catch task has a sparse reward: 1 when the ball is in the cup, 0 otherwise.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Point-mass: A planar point mass receives a reward of 1 when within a target at the origin. In the easy task, one of simplest in the suite, the two actuators correspond to the global x and y axes. In the hard task, the gain matrix from the controls to the axes is randomised for each episode, making it impossible to solve by memoryless agents. This task is not in the benchmarking set.

<!-- chunk {"id": "body-0299", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Reacher: The simple two-link planar reacher with a randomised target location. The reward is one when the end effector penetrates the target sphere. In the easy task the target sphere is bigger than on the hard task (shown on the left).

<!-- chunk {"id": "body-0300", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Finger: A 3-DoF toy manipulation problem based. A planar ‘finger’ is required to rotate a body on an unactuated hinge. In the turn_easy and turn_hard tasks, the tip of the free body must overlap with a target (the target is smaller for the turn_hard task). In the spin task, the body must be continually rotated.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Hopper: The planar one-legged hopper introduced, initialised in a random configuration. In the stand task it is rewarded for bringing its torso to a minimal height. In the hop task it is rewarded for torso height and forward velocity.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Fish: A fish is required to swim to a target. This domain relies on MuJoCo’s simplified fluid dynamics. There are two tasks: in the upright task, the fish is rewarded only for righting itself with respect to the vertical, while in the swim task it is also rewarded for swimming to the target.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Cheetah: A running planar biped based. The reward r is linearly proportional to the forward velocity v up to a maximum of 10 m/s i.e. r (v) = max (0,min (v/10,1)).

<!-- chunk {"id": "body-0304", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Walker: An improved planar walker based on the one introduced. In the stand task reward is a combination of terms encouraging an upright torso and some minimal torso height. The walk and run tasks include a component encouraging forward velocity.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Manipulator: A planar manipulator is rewarded for bringing an object to a target location. In order to assist with exploration, in 10% of episodes the object is initialised in the gripper or at the target. Four manipulator tasks: {bring,insert}_{ball,peg} of which only bring_ball is in the benchmarking set. The other three are shown below.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.415]figure[\FBwidth]
Manipulator extra: insert_ball: place the ball inside the basket. bring_peg: bring the peg to the target peg. insert_peg: insert the peg into the slot. See \href video for solutions of insertion tasks.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Stacker (6 k + 16, 5, 11 k + 26): Stack k boxes. Reward is given when a box is at the target and the gripper is away from the target, making stacking necessary. The height of the target is sampled uniformly from {1, …, k}.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Swimmer (2 k + 4, k − 1, 4 k + 1): This procedurally generated k-link planar swimmer is based on Coulom 2002, but using MuJoCo’s high-Reynolds fluid drag model. A reward of 1 is provided when the nose is inside the target and decreases smoothly with distance like a Lorentzian. The two instances provided in the benchmarking set are the 6-link and 15-link swimmers.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Humanoid: A simplified humanoid with 21 joints, based on the model. Three tasks: stand, walk and run are differentiated by the desired horizontal speed of 0, 1 and 10 m/s, respectively. Observations are in an egocentric frame and many movement styles are possible solutions e.g. running backwards or sideways. This facilitates exploration of local optima.

<!-- chunk {"id": "body-0310", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
Humanoid_CMU: A humanoid body with 56 joints, adapted from and based on the ASF model of subject #8 in the CMU Motion Capture Database. This domain has the same stand, walk and run tasks as the simpler humanoid. We include tools for parsing and playback of the CMU MoCap data, see below. A newer version of this model is now available; see Section 7.

<!-- chunk {"id": "body-0311", "role": "body", "section": "Domains and Tasks", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top, capbesidewidth=0.79]figure[\FBwidth]
LQR (2n, m, 2n): n masses, of which m ( ≤ n) are actuated, move on linear joints which are connected serially. The reward is a quadratic in the position and controls. Analytic transition and control-gain matrices are derived and the optimal policy and value functions are computed in lqr_solver.py using Riccati iterations. Since both controls and reward are unbounded, LQR is not in the benchmarking set.

<!-- chunk {"id": "body-0312", "role": "body", "section": "Control Suite Benchmarking", "weight": 1.0} -->

Please see the original tech report for the Control Suite for detailed benchmarking results of the BENCHMARKING tasks, with several popular Reinforcement Learning algorithms.

<!-- chunk {"id": "body-0313", "role": "body", "section": "CMU Motion Capture Data", "weight": 1.0} -->

We enable humanoid_CMU to be used for imitation learning as in Merel et al., by providing tools for parsing, conversion and playback of human motion capture data from the CMU Motion Capture Database. The convert function in the parse_amc module loads an AMC data file and returns a sequence of configurations for the humanoid_CMU model. The example script CMU_mocap_demo.py uses this function to generate a video.

<!-- chunk {"id": "body-0314", "role": "body", "section": "Quadruped", "weight": 1.0} -->

The quadruped (Figure 5 ‣ 6.3 Additional domains ‣ 6 The Control Suite ‣ Part II Tasks ‣ dm_control: Software and Tasks for Continuous Control")) has 56 state dimensions. Each leg has 3 actuators for a total of 12 actions. Besides the basic walk and run tasks on flat ground, in the escape task the quadruped must climb over procedural random terrain using an array of 20 range-finder sensors (Figure 5 ‣ 6.3 Additional domains ‣ 6 The Control Suite ‣ Part II Tasks ‣ dm_control: Software and Tasks for Continuous Control"), middle). In the fetch task (Figure 5 ‣ 6.3 Additional domains ‣ 6 The Control Suite ‣ Part II Tasks ‣ dm_control: Software and Tasks for Continuous Control"), right), the quadruped must run after a moving ball and dribble it to a target at the centre of an enclosed arena. See solutions in \\href

<!-- chunk {"id": "body-0315", "role": "body", "section": "Dog", "weight": 1.0} -->

A realistic model of a Pharaoh Dog (Figure 6 ‣ 6.3 Additional domains ‣ 6 The Control Suite ‣ Part II Tasks ‣ dm_control: Software and Tasks for Continuous Control")) was prepared for DeepMind by \\href and is made available to the wider research community. The kinematics, skinning weights and collision geometry are created procedurally using PyMJCF. The static model includes muscles and tendon attachment points (Figure 6 ‣ 6.3 Additional domains ‣ 6 The Control Suite ‣ Part II Tasks ‣ dm_control: Software and Tasks for Continuous Control"), *Right*). Including these in the dynamical model using MuJoCo's support for tendons and muscles requires detailed anatomical knowledge and remains future work.

<!-- chunk {"id": "body-0316", "role": "body", "section": "Rodent (184, 38, 107 + 64$\\times$`<!-- -->`{=html}64$\\times$`<!-- -->`{=html}3 pixels)", "weight": 1.0} -->

In order to better compare learned behaviour with experimental settings common in the life sciences, we have built a model of a rodent. See for initial research training a policy to control this model using visual inputs and analysing the resulting neural representations. Related videos of rodent tasks therein: \\href \\href \\href and \\href The skeleton reference model was made by \\href (not included).

<!-- chunk {"id": "body-0317", "role": "body", "section": "Locomotion tasks", "weight": 1.0} -->

Inspired by our early work in Heess et al. 2017, the Locomotion library provides a framework and a set of high-level components for creating rich locomotion-related task domains. The central abstractions are the Walker, an agent-controlled Composer Entity that can move itself, and the Arena, the physical environment in which behaviour takes place. Walkers expose locomotion-specific methods, like observation transformations into an egocentric frame, while Arenas can re-scale themselves to fit Walkers of different sizes. Together with the Task, which includes a specification of episode initialisation, termination, and reward logic, a full RL environment is specified. The library currently includes navigating a corridor with obstacles, foraging for rewards in a maze, traversing rough terrain and multi-agent soccer. Many of these tasks were first introduced in Merel et al. 2019a and Liu et al. 2019.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

As an illustrative example of using the Locomotion infrastructure to build an RL environment, consider placing a humanoid in a corridor with walls, and a task specifying that the humanoid will be rewarded for running along this corridor, navigating around the wall obstacles using vision. We instantiate the environment as a composition of the Walker, Arena, and Task as follows. First, we build a position-controlled CMU humanoid walker.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

[⬇](data:text/plain;base64,d2Fsa2VyID0gY211X2h1bWFub2lkLkNNVUh1bWFub2lkUG9zaXRpb25Db250cm9sbGVkVjIwMjAoCiAgb2JzZXJ2YWJsZV9vcHRpb25zPXsnZWdvY2VudHJpY19jYW1lcmEnOiBkaWN0KGVuYWJsZWQ9VHJ1ZSl9KQ==){download=""}

<!-- chunk {"id": "body-0320", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

observable_options={'egocentric_camera': dict(enabled=True)})

<!-- chunk {"id": "body-0321", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

Note that this CMU humanoid is "V2020", an improved version from the initial one released in Tassa et al.. Modifications include overall body height and mass better matching a typical human, more realistic body proportions, and better tuned gains and torque limits for position-control actuators.

<!-- chunk {"id": "body-0322", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

Next, we construct a corridor-shaped arena that is obstructed by walls.

<!-- chunk {"id": "body-0323", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

[⬇](data:text/plain;base64,YXJlbmEgPSBhcmVuYXMuV2FsbHNDb3JyaWRvcih3YWxsX2dhcD0zLiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3YWxsX3dpZHRoPWRpc3RyaWJ1dGlvbnMuVW5pZm9ybSgyLiwgMy4pLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdhbGxfaGVpZ2h0PWRpc3RyaWJ1dGlvbnMuVW5pZm9ybSgyLjUsIDMuNSksCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29ycmlkb3Jfd2lkdGg9NC4sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29ycmlkb3JfbGVuZ3RoPTMwLik=){download=""}

<!-- chunk {"id": "body-0324", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

arena = arenas.WallsCorridor(wall_gap=3.,

<!-- chunk {"id": "body-0325", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

Finally, a task that rewards the agent for running down the corridor at a specific velocity is instantiated as a composer.Environment.

<!-- chunk {"id": "body-0326", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

[⬇](data:text/plain;base64,dGFzayA9IHRhc2tzLlJ1blRocm91Z2hDb3JyaWRvcih3YWxrZXI9d2Fsa2VyLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFyZW5hPWFyZW5hLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdhbGtlcl9zcGF3bl9wb3NpdGlvbj0oMC41LCAwLCAwKSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0YXJnZXRfdmVsb2NpdHk9My4wLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBoeXNpY3NfdGltZXN0ZXA9MC4wMDUsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udHJvbF90aW1lc3RlcD0wLjAzKQoKZW52aXJvbm1lbnQgPSBjb21wb3Nlci5FbnZpcm9ubWVudCh0aW1lX2xpbWl0PTEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRhc2s9dGFzaywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdHJpcF9zaW5nbGV0b25fb2JzX2J1ZmZlcl9kaW09VHJ1ZSk=){download=""}

<!-- chunk {"id": "body-0327", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

task = tasks.RunThroughCorridor(walker=walker,

<!-- chunk {"id": "body-0328", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

environment = composer.Environment(time_limit=10,

<!-- chunk {"id": "body-0329", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

strip_singleton_obs_buffer_dim=True)

<!-- chunk {"id": "body-0330", "role": "body", "section": "Humanoid running along corridor with obstacles", "weight": 1.0} -->

shows a video of a solution of this task, produced with Abdolmaleki et al. 2018's MPO agent.

<!-- chunk {"id": "body-0331", "role": "body", "section": "Maze navigation and foraging", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=left,top, capbesidewidth=0.57]figure[\FBwidth]
We include a procedural maze generator for arenas, to construct navigation and foraging tasks. On the right is the CMU humanoid in a human-sized maze, with spherical rewarding elements. \href shows the Rodent navigating a rodent-scale maze arena.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

Building on Composer and Locomotion libraries, the Multi-agent soccer environments, introduced in Liu et al. 2019, follow a consistent task structure of Walkers, Arena, and Task where instead of a single walker, we inject multiple walkers that can interact with each other physically in the same scene. The code snippet below shows how to instantiate a 2-vs-2 Multi-agent Soccer environment with the simple, 5 degree-of-freedom BoxHead walker type. For example it can trivially be replaced by WalkerType.ANT, as shown in Figure 9.

<!-- chunk {"id": "body-0333", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sLmxvY29tb3Rpb24gaW1wb3J0IHNvY2NlcgoKdGVhbV9zaXplID0gMgpudW1fd2Fsa2VycyA9IDIgKiB0ZWFtX3NpemUKCmVudiA9IHNvY2Nlci5sb2FkKHRlYW1fc2l6ZT10ZWFtX3NpemUsCiAgICAgICAgICAgICAgICAgIHRpbWVfbGltaXQ9NDUsCiAgICAgICAgICAgICAgICAgIHdhbGtlcl90eXBlPXNvY2Nlci5XYWxrZXJUeXBlLkJPWEhFQUQp){download=""}

<!-- chunk {"id": "body-0334", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

from dm_control.locomotion import soccer

<!-- chunk {"id": "body-0335", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

env = soccer.load(team_size=team_size,

<!-- chunk {"id": "body-0336", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

walker_type=soccer.WalkerType.BOXHEAD)

<!-- chunk {"id": "body-0337", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

To implement a synchronous multi-agent environment, we adopt the convention that each TimeStep contains a sequence of per-agent observation dictionaries and expects a sequence of per-agent action arrays in return.

<!-- chunk {"id": "body-0338", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

[⬇](data:text/plain;base64,YXNzZXJ0IGxlbihlbnYuYWN0aW9uX3NwZWMoKSkgPT0gbnVtX3dhbGtlcnMKYXNzZXJ0IGxlbihlbnYub2JzZXJ2YXRpb25fc3BlYygpKSA9PSBudW1fd2Fsa2VycwoKIyBSZXNldCBhbmQgaW5pdGlhbGl6ZSB0aGUgZW52aXJvbm1lbnQuCnRpbWVzdGVwID0gZW52LnJlc2V0KCkKCiMgR2VuZXJhdGVzIGEgcmFuZG9tIGFjdGlvbiBhY2NvcmRpbmcgdG8gdGhlIGBhY3Rpb25fc3BlY2AuCnJhbmRvbV9hY3Rpb25zID0gW3NwZWMuZ2VuZXJhdGVfdmFsdWUoKSBmb3Igc3BlYyBpbiBlbnYuYWN0aW9uX3NwZWMoKV0KdGltZXN0ZXAgPSBlbnYuc3RlcChyYW5kb21fYWN0aW9ucykKCiMgQ2hlY2sgdGhhdCB0aW1lc3RlcCByZXNwZWN0cyBtdWx0aS1hZ2VudCBhY3Rpb24gYW5kIG9ic2VydmF0aW9uIGNvbnZlbnRpb24uCmFzc2VydCBsZW4odGltZXN0ZXAub2JzZXJ2YXRpb24pID09IG51bV93YWxrZXJzCmFzc2VydCBsZW4odGltZXN0ZXAucmV3YXJkKSA9PSBudW1fd2Fsa2Vycw==){download=""}

<!-- chunk {"id": "body-0339", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

assert len(env.action_spec) == num_walkers

<!-- chunk {"id": "body-0340", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

assert len(env.observation_spec) == num_walkers

<!-- chunk {"id": "body-0341", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

\# Reset and initialize the environment.

<!-- chunk {"id": "body-0342", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

\# Generates a random action according to the 'action_spec'.

<!-- chunk {"id": "body-0343", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

random_actions = \[spec.generate_value for spec in env.action_spec\]

<!-- chunk {"id": "body-0344", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

timestep = env.step(random_actions)

<!-- chunk {"id": "body-0345", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

\# Check that timestep respects multi-agent action and observation convention.

<!-- chunk {"id": "body-0346", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

assert len(timestep.observation) == num_walkers

<!-- chunk {"id": "body-0347", "role": "body", "section": "Multi-Agent soccer", "weight": 1.0} -->

assert len(timestep.reward) == num_walkers

<!-- chunk {"id": "body-0348", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

The manipulation module provides a robotic arm, a set of simple objects, and tools for building reward functions for manipulation tasks.

<!-- chunk {"id": "body-0349", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

Arm joint positions, velocities, and torques.

<!-- chunk {"id": "body-0350", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

Task-specific privileged features (including the positions and velocities of other movable objects in the scene).

<!-- chunk {"id": "body-0351", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

Arm joint positions, velocities, and torques.

<!-- chunk {"id": "body-0352", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

Fixed RGB camera view showing the workspace.

<!-- chunk {"id": "body-0353", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

All of the manipulation environments return a reward ${r{(\mathbf{s},\mathbf{a})}} \in {\lbrack 0,1\rbrack}$ per timestep, and have an episode time limit of 10 seconds.

<!-- chunk {"id": "body-0354", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZnJvbSBkbV9jb250cm9sIGltcG9ydCBtYW5pcHVsYXRpb24KCiMgYEFMTGAgaXMgYSB0dXBsZSBjb250YWluaW5nIHRoZSBuYW1lcyBvZiBhbGwgb2YgdGhlIGVudmlyb25tZW50cy4KcHJpbnQoJ1xuJy5qb2luKG1hbmlwdWxhdGlvbi5BTEwpKQ==){download=""}

<!-- chunk {"id": "body-0355", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

\# 'ALL' is a tuple containing the names of all of the environments.

<!-- chunk {"id": "body-0356", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

Environments are also tagged according to what types of observation they return.

<!-- chunk {"id": "body-0357", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

[⬇](data:text/plain;base64,cHJpbnQoJ1xuJy5qb2luKG1hbmlwdWxhdGlvbi5nZXRfZW52aXJvbm1lbnRzX2J5X3RhZygndmlzaW9uJykpKQ==){download=""}

<!-- chunk {"id": "body-0358", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

print('\\n'.join(manipulation.get_environments_by_tag('vision')))

<!-- chunk {"id": "body-0359", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

Environments are instantiated by name using the load method, which also takes an optional seed argument that can be used to seed the random number generator used by the environment.

<!-- chunk {"id": "body-0360", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZW52ID0gbWFuaXB1bGF0aW9uLmxvYWQoJ3N0YWNrXzNfYnJpY2tzX3Zpc2lvbicsIHNlZWQ9NDIp){download=""}

<!-- chunk {"id": "body-0361", "role": "body", "section": "Manipulation tasks", "weight": 1.0} -->

env = manipulation.load('stack_3_bricks_vision', seed=42)

<!-- chunk {"id": "body-0362", "role": "body", "section": "Studded brick model", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=left,top, capbesidewidth=0.67]figure[\FBwidth]
The stack_3_bricks_vision task, like most of the included manipulation tasks, makes use of the studded bricks shown on the right. These were modelled on Lego Duplo® bricks, snapping together when properly aligned and force is applied, and holding together using friction.

<!-- chunk {"id": "body-0363", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

reach_site: Move the end effector to a target location in 3D space.

<!-- chunk {"id": "body-0364", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

reach_brick: Move the end effector to a brick resting on the ground.

<!-- chunk {"id": "body-0365", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

lift_brick: Elevate a brick above a threshold height.

<!-- chunk {"id": "body-0366", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

lift_large_box: Elevate a large box above a threshold height. The box is too large to be grasped by the gripper, requiring non-prehensile manipulation.

<!-- chunk {"id": "body-0367", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

place_cradle: Place a brick inside a concave 'cradle' situated on a pedestal.

<!-- chunk {"id": "body-0368", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

place_brick: Place a brick on top of another brick that is attached to the top of a pedestal. Unlike the stacking tasks below, the two bricks are not required to be snapped together in order to obtain maximum reward.

<!-- chunk {"id": "body-0369", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

stack_2_bricks: Snap together two bricks, one of which is attached to the floor.

<!-- chunk {"id": "body-0370", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

stack_2_bricks_moveable_base: Same as stack_2_bricks, except both bricks are movable.

<!-- chunk {"id": "body-0371", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

stack_2_of_3_bricks_random_order: Same as stack_2_bricks, except there is a choice of two color-coded movable bricks, and the agent must place the correct one on top of the fixed bottom brick. The goal configuration is represented by a visual hint consisting of a stack of translucent, contactless bricks to the side of the workspace. In the features version of the task the observations also contain a vector of indices representing the desired order of the bricks.

<!-- chunk {"id": "body-0372", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

stack_3_bricks: Assemble a tower of 3 bricks. The bottom brick is attached to the floor, whereas the other two are movable. The top two bricks must be assembled in a specific order.

<!-- chunk {"id": "body-0373", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

stack_3_bricks_random_order: Same as stack_3_bricks, except the order of the top two bricks does not matter.

<!-- chunk {"id": "body-0374", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

reassemble_3_bricks_fixed_order: The episode begins with all three bricks already assembled in a stack, with the bottom brick being attached to the floor. The agent must disassemble the top two bricks in the stack, and reassemble them in the opposite order.

<!-- chunk {"id": "body-0375", "role": "body", "section": "Task descriptions", "weight": 1.0} -->

reassemble_5_bricks_random_order: Same as the previous task, except there are 5 bricks in the initial stack. There are therefore ${4!} - 1$ possible alternative configurations in which the top 4 bricks in the stack can be reassembled, of which only one is correct.

<!-- chunk {"id": "body-0376", "role": "body", "section": "Conclusion", "weight": 1.5} -->

dm_control is a starting place for the testing and performance comparison of reinforcement learning algorithms for physics-based control. It offers a wide range of pre-designed RL tasks and a rich framework for designing new ones. We are excited to be sharing these tools with the wider community and hope that they will be found useful. We look forward to the diverse research the Control Suite and associated libraries may enable, and to integrating community contributions in future releases.
