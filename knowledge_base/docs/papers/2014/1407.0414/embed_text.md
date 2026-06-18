## Introduction

Let $x_{t} \in {\mathbb{R}}^{n}$ be a joint configuration and $x_{0:T} = {(x_{0},\ldots,x_{T})}$ a trajectory of length $T$. Note that troughout this framework we *do not* represent trajectories in the phase space, where the state is $(x_{t},{\overset{˙}{x}}_{t})$---we represent trajectories directly in configuration space. We consider optimization problems of a general "$k$-order non-linear sum-of-squares constrained" form

where $x_{{t - k}:t} = {(x_{t - k},..,x_{t - 1},x_{t})}$ are $k + 1$ tuples of consecutive states. The functions ${f_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{d_{t}}$, ${g_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{m_{t}}$, and ${h_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{l_{t}}$ are arbitrary first-order differentiable non-linear $k$-order vector-valued functions. These define cost terms or inequality/equality constraints for each $t$. Note that the first cost vector $f_{0}{(x_{- k},..,x_{0})}$ depends on states $x_{t}$ with negative $t$. We call these $(x_{- k},..,x_{- 1})$ the *prefix*. The prefix defines the initial condition of the robot, which could for instance be resting at some given $x_{0}$. (A postfix to constrain the endcondition in configuration space is optional.)

The term $k{(t,t^{\prime})}$ is an optional kernel measuring the (desired) correlation between time steps $t$ and $t^{\prime}$, which we explored but in practice hardly used.

The $k$-order cost vectors ${f_{t}{(x_{{t - k}:t})}} \in {\mathbb{R}}^{d_{t}}$ are very flexible in including various elements that can represent both transition and task-related costs. This is detailed below. To give first examples, for transitional costs we can penalize square velocities using $k = 1$ (depending on two consecutive configurations) ${f_{t}{(x_{t\text{-}1},x_{t})}} = {({x_{t} - x_{t\text{-}1}})}$, and square accelerations using $k = 2$ (depending on three consecutive configurations) ${f_{t}{(x_{t\text{-}2},x_{t\text{-}1},x_{t})}} = {({{x_{t} + x_{t\text{-}2}} - {2x_{t\text{-}1}}})}$. Likewise, for larger values of $k$, we can penalize higher-order finite-differencing approximations of trajectory derivatives (e.g., jerk). Moreover, for $k = 2$, using the equations of motion ${{M{\overset{¨}{x}}_{t}} + F} = \tau_{t}$ with ${\overset{¨}{x}}_{t} \approx {{x_{t + 1} + x_{t - 1}} - {2x_{t}}}$, we can explicitly penalize square torques using $f_{t} = \sqrt{H}M{(x_{t} - 2x_{t\text{-}1} + x_{t\text{-}2})} + F)$, where $\sqrt{H}$ is the Cholesky decomposition of a torque cost metric $H$, implying costs ${f_{t}^{\top}f_{t}} = {u_{t}^{\top}Hu_{t}}$.

The inequality and equality constraints $g_{t}$ and $h_{t}$ are equally general: we can impose $k$-order constraints on joint configuration transitions (velocities, accelerations, torques) or in task spaces.

The optimization problem can be rewritten as

where $f = {(f_{0};..;f_{T})}$ is the concatenation of all $f_{t}$ and $g = {(g_{0};..;g_{T})}$, $h = {(h_{0};..;h_{T})}$. This defines a constrained sum-of-squares problem which lends to Gauss-Newton methods. Let $J = {\nabla_{x_{0:T}}\Phi}$ be the global Jacobian. It is essential to realize that the pseudo-Hessian $J^{\top}J$ (as used by Gauss-Newton) is a *banded* symmetric matrix. The band-width is ${({k + 1})}n$.

### The KOMO code

The goal of the implementation is the separation between the code of optimizers and code to specify motion problems. The problem form provides the abstraction for that interface. The optimization methods all assume the general form

of a non-linear constrained optimization problem, with the additional assumption that the (approximate) Hessian ${\nabla^{2}f}{(x)}$ can be provided and is semi-pos-def. Therefore, the KOMO code essentially does the following

Provide interfaces to define sets of $k$-order task spaces and costs/constraints in these task spaces at various time slices; which constitutes a MotionProblem. Such a MotionProblem definition is very semantic, referring to the kinematics of the robot.

Abstracts and converts a MotionProblem definition into the general form using a kinematics engine. The resulting MotionProblemFunction is not semantic anymore and provides the interface to the generic optimization code.

Converts the problem definition into the general forms and using appropriate matrix packings to exploit the chain structure of the problem. This code does not refer to any robotics or kinematics anymore.

Applies various optimizers. This is generic code.

The code introduces specialized matrix packings to exploit the structure of $J$ and to efficiently compute the banded matrix $J^{\top}J$. Note that the rows of $J$ have at most ${({k + 1})}n$ non-zero elements since a row refers to exactly one task and depends only on one specific tuple $(x_{t - k},..,x_{t})$. Therefore, although $J$ is generally a ${D \times {({T + 1})}}n$ matrix (with $D = {\sum_{t}{\dim{(f_{t})}}}$), each row can be packed to store only ${({k + 1})}n$ non-zero elements. We introduced a *row-shifted* matrix packing representation for this. Using specialized methods to compute $J^{\top}J$ and $J^{\top}x$ for any vector $x$ for the row-shifted packing, we can efficiently compute the banded Hessian and any other terms we need in Gauss-Newton methods.

## Formal problem representation

The following definitions also document the API of the code.

: is a mapping $\Gamma:{x\mapsto{\Gamma{(x)}}}$ that maps a joint configuration to a data structure $\Gamma{(x)}$ which allows to efficiently evaluate task maps. Typically $\Gamma{(x)}$ stores the frames of all bodies/shapes/objects and collision information. More abstractly, $\Gamma{(x)}$ is any data structure that is sufficient to define the task maps below.

Note: In the code there is yet no abstraction KinematicEngine. Only one specific engine (KinematicWorld) is used. It would be straight-forward to introduce an abstraction for kinematic engines pin-pointing exactly their role for defining task maps.

: is a mapping $\phi:{(\Gamma_{- k},..,\Gamma_{0})}\mapsto{(y,J)}$ which gets $k + 1$ kinematic data structures as input and returns some vector $y \in {\mathbb{R}}^{d}$ and its Jacobian $J \in {{\mathbb{R}}{({d \times n})}}$.

: is a tuple $c = {(\phi,\varrho_{0:T},y_{0:T}^{\ast},\text{mode})}$ where $\phi$ is a TaskMap and the parameters ${\varrho_{0:T},y_{0:T}^{\ast}} \in {\mathbb{R}}^{{d \times T}\text{+}1}$ allow for an additional linear transformation in each time slice. Here, $d = {\dim{(\phi)}}$ is the dimensionality of the task map. This defines the transformed task map

which depending on $\text{mode} \in {\{\text{cost, constraint}\}}$ is interpreted as cost or constraint term. Note that, in the cost case, $y_{0:T}^{\ast}$ has the semantics of a reference target for the task variable, and $\varrho_{0:T}^{\ast}$ of a precision. In the code, $\varrho_{0:T},y_{0:T}^{\ast}$ may optionally be given as $1 \times 1$, ${1 \times T}\text{+}1$, $d \times 1$, or ${d \times T}\text{+}1$ matrices---and an interpreted constant along the missing dimensions.

: is a tuple $(T,\mathcal{C},x_{{- k}:{- 1}})$ which gives the number of time steps, a list $\mathcal{C} = {\{ c_{i}\}}$ of Tasks, and a *prefix* $x_{{- k}:{- 1}} \in {\mathbb{R}}^{k \times n}$. The prefix allows to evaluate tasks also for time $t = 0$, where the prefix defines the kinematic configurations $\Gamma{(x_{- k})},..,\Gamma{(x_{0})}$ at negative times.^11^1Optionally one can set a postfix $x_{{T + 1}:{T + k}}$ which fixes the final condition. This defines the optimization problem

Here, $f_{t}$ is the concatenation of all ${\hat{\phi}}_{t}^{c}$ over tasks $c \in \mathcal{C}:c.\text{mode=cost} \land c.\varrho_{t} \neq 0$; and $g_{t}$ is the concatenation of all ${\hat{\phi}}_{t}^{c}$ over tasks $c \in \mathcal{C}:c.\text{mode=constraint} \land c.\varrho_{t} \neq 0$.

## User Interfaces

### Easy

For convenience there is a single high-level method to call the optimization, defined in \<Motion/komo.h\>\

/// Return a trajectory that moves the endeffector to a desired target position
arr moveTo(ors::KinematicWorld& world, //in initial state
ors::Shape& endeff, //endeffector to be moved
ors::Shape& target, //target shape
byte whichAxesToAlign=0, //bit coded options to align axes
uint iterate=1); //usually the optimization methods may be called just
//once; multiple calls -> safety

The method returns an optimized joint space trajectory so that the endeff reaches the target. Optionally the optimizer additionaly aligns some axes between the coordinate frames. This is just one typical use case; others would include constraining vector-alignments to zero (orthogonal) instead of +1 (parallel), or directly specifying quaternions, or using many other existing task maps. See expert interface.

This interface specifies the relevant coordinate frames by referring to Shapes. Shapes (ors::Shape) are rigidly attached to bodies ("links") and usually represent a (convex) collision mesh/primitive. However, a Shape can also just be a marker frame (ShapeType markerST=5), in which case it is just a convenience to define reference frames attached to bodies. So, the best way to determine the geometric parameters of the endeffector and target (offsets, relative orientations etc) is by transforming the respective shape frames (Shape::rel).

The method uses implicit parameters (grabbed from cfg file or command line or default):\

double posPrec = MT::getParameter("KOMO/moveTo/precision", 1e3);
double colPrec = MT::getParameter("KOMO/moveTo/collisionPrecision", -1e0);
double margin = MT::getParameter("KOMO/moveTo/collisionMargin",.1);
double zeroVelPrec = MT::getParameter("KOMO/moveTo/finalVelocityZeroPrecision", 1e1);
double alignPrec = MT::getParameter("KOMO/moveTo/alignPrecision", 1e3);

### Expert using the included kinematics engine

See the implementation of moveTo! This really is the core guide to build your own cost functions.

More generically, if the user would like to implement new TaskMaps or use some of the existing ones:

The user can define new $k$-order task maps by instantiating the abstraction. There exist a number of predefined task maps. The specification of a task map usually has only a few parameters like "which endeffector shape(s) are you referring to". Typically, a good convention is to define task maps in a way such that *zero* is a desired state or the constraint boundary, such as relative coordinates, alignments or orientation. (But that is not necessary, see the linear transformation below.)

To define an optimization problem, the user creates a list of tasks, where each task is defined by a task map and parameters that define how the map is interpreted as a) a cost term or b) an inequality constraint. This interpretation allows: a linear transformation separately for each $t$ (=setting a reference/target and precision); how maps imply a constraint. This interpretation has a significant number of parameters: for each time slice different targets/precisions could be defined.

### Expert with own kinematics engine

The code needs a data structure $\Gamma{(q_{t})}$ to represent the (kinematic) state $q_{t}$, where coordinate frames of all bodies/shapes/objects have been precomputed so that evaluation of task maps is fast. Currently this is KinematicWorld.

Users that prefer using the own kinematics engine can instantiate the abstraction. Note that the engine needs to fulfill two roles: it must have a setJointState method that also precomputes all frames of all bodies/shapes/objects. And it must be siffucient as argument of your task map instantiations.

### Optimizers

The user can also only use the optimizers, directly instantiating the $k$-order Markov problem abstraction; or, yet a level below, directly instantiating the ConstrainedProblem abstraction. Examples are given in examples/Optim/kOrderMarkov and examples/Optim/constrained. Have a look at the specific implementations of the benchmark problems, esp. the ParticleAroundWalls problem.

### Parameters & Reporting

Every run of the code generates a MT.log file, which tells about every parameter that was internally used. You can overwrite any of these parameters on command line or in an MT.cfg file.

Inspecting the cost report after an optimization is important. Currently, the code goes through the task list $\mathcal{C}$ and reports for each the costs associated to it. There are also methods to display the cost arising in the different tasks over time.

## Potential Improvements

There is many places the code code be improved (beyond documenting it better):

Implementing equality constraints: For a lack of necessity the code does not yet handle equality constraints. We typically handle equality tasks (reach a point) using cost terms; while focussing on inequality constraints for collisions and joint limits.

The KinematicEngine should be abstracted to allow for easier plugin of alternative engines.

Our kinematics engine uses SWIFT++ for proximity and penetration computation. The methods would profit enormously from better (faster, more accurate) proximity engines (signed distance functions, sphere-swept primitives).

## Disclaimer

This document by no means aims to document all aspects of the code, esp. those relating to the used kinematics engine etc. It only tries to introduce to the concepts and design decisions behind the KOMO code.

More documentation of optimization and kinematics concepts used in the code can be drawn from my teaching lectures on Optimization and Robotics.
